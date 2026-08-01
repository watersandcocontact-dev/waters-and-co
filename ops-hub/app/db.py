import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "hub.sqlite3"

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    business_line TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'New',
    next_action TEXT,
    deadline TEXT,                 -- ISO date YYYY-MM-DD, nullable
    estimated_value REAL,
    notes TEXT,
    contact_name TEXT,
    contact_phone TEXT,
    contact_email TEXT,
    au_state TEXT,                 -- NSW/VIC/QLD/... nullable, relevant to several lines
    source TEXT DEFAULT 'manual',  -- manual | webhook | referral | import
    extra_json TEXT DEFAULT '{}',  -- business-line-specific fields, see app/config.py
    task_type TEXT,                -- 'setup' | 'management' | null, see config.TASK_TYPE_LINES
    time_estimate_hours REAL,      -- per-lead override of the rate-card default
    done_summary TEXT,             -- what's already done/automated, 1-2 lines
    left_for_you_summary TEXT,     -- what's left for the human, 1-2 lines
    source_url TEXT,                -- link to the primary source (gov page, platform, etc.)
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_leads_business_line ON leads(business_line);
CREATE INDEX IF NOT EXISTS idx_leads_deadline ON leads(deadline);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);

CREATE TABLE IF NOT EXISTS webhook_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    received_at TEXT NOT NULL DEFAULT (datetime('now')),
    source TEXT,
    payload_json TEXT,
    lead_id INTEGER,
    note TEXT
);

CREATE TABLE IF NOT EXISTS time_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    hours REAL NOT NULL,
    note TEXT,
    logged_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_time_entries_lead_id ON time_entries(lead_id);

-- Expansion budget + kill-switch tracking (2026-07-31). Phase 1 = $0 budget,
-- no real spend yet — this table exists so the tracking is ready the
-- moment spend actually starts, not built retroactively. See
-- app/config.py EVALUATION_WINDOWS_WEEKS and BUDGET_PHASE.
CREATE TABLE IF NOT EXISTS expansion_spend (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    spend_date TEXT NOT NULL,          -- ISO date
    business_line TEXT,                -- which business line this supported, nullable if brand-wide
    spend_type TEXT NOT NULL,          -- search_ads | meta_ads | content | tool_subscription | referral_partnership | other
    campaign_tag TEXT,                 -- short UTM-style tag for attribution matching against leads.source
    amount REAL NOT NULL,
    funded_by TEXT NOT NULL DEFAULT 'personal_income',  -- personal_income | business_profit
    notes TEXT,
    evaluation_due TEXT,               -- ISO date; spend_date + this spend_type's evaluation window
    status TEXT NOT NULL DEFAULT 'active',  -- active | kept | adjusted | killed
    outcome_leads INTEGER DEFAULT 0,   -- manually updated count of attributed leads
    outcome_revenue REAL DEFAULT 0,    -- manually updated attributed revenue
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_expansion_spend_business_line ON expansion_spend(business_line);
CREATE INDEX IF NOT EXISTS idx_expansion_spend_status ON expansion_spend(status);

-- Tax tracking (2026-07-31) — day job (PAYG) + all business deductions,
-- feeding one combined accountant export. See app/config.py TAX_FIGURES
-- (sourced from wave3-unscoped/tax_tracking/ato_figures_verification.md)
-- and docs/tax_tracking.md for what this is and isn't (organisation/
-- flagging tool, not tax advice, not lodgement).
CREATE TABLE IF NOT EXISTS day_job_pay_periods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pay_date TEXT NOT NULL,        -- ISO date of the pay day
    gross REAL NOT NULL,
    tax_withheld REAL NOT NULL,
    net REAL NOT NULL,
    super_amount REAL,             -- employer SG paid this period, nullable if unknown
    hours_worked REAL,             -- nullable — needed for the day-job-vs-business $/hr comparison
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_day_job_pay_periods_date ON day_job_pay_periods(pay_date);

CREATE TABLE IF NOT EXISTS deductible_expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_date TEXT NOT NULL,
    context TEXT NOT NULL,          -- 'day_job' or a business_line key
    category TEXT NOT NULL,         -- see config.EXPENSE_CATEGORIES
    amount REAL NOT NULL,
    description TEXT,
    receipt_held TEXT NOT NULL DEFAULT 'yes',  -- yes | no_receipt_exception | no_receipt_uncovered
    no_receipt_bucket TEXT,         -- which cap this counts toward if receipt_held != 'yes': combined_300 | laundry_150 | small_expense_200 | phone_internet_50 | cents_per_km | home_office_hours | null
    deduction_treatment TEXT,       -- immediate | depreciated | n/a (only meaningful for equipment-type categories)
    km_count REAL,                  -- for category = vehicle_km entries
    hours_count REAL,               -- for category = home_office entries (fixed-rate hours)
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_deductible_expenses_context ON deductible_expenses(context);
CREATE INDEX IF NOT EXISTS idx_deductible_expenses_category ON deductible_expenses(category);

-- Stripe payments (2026-08-01) -- one row per payment request sent to a
-- client, created against a lead. Status starts 'pending' and is flipped
-- to 'paid' by the Stripe webhook (app/payments.py) on
-- checkout.session.completed -- never set client-side, since that would let
-- someone mark themselves paid by just hitting the success_url.
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    checkout_session_id TEXT NOT NULL UNIQUE,
    payment_intent_id TEXT,
    checkout_url TEXT,
    amount_cents INTEGER NOT NULL,
    currency TEXT NOT NULL DEFAULT 'aud',
    description TEXT,
    status TEXT NOT NULL DEFAULT 'pending',  -- pending | paid | expired | canceled
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    paid_at TEXT
);

CREATE INDEX IF NOT EXISTS idx_payments_lead_id ON payments(lead_id);
CREATE INDEX IF NOT EXISTS idx_payments_status ON payments(status);

-- Referral bonus ledger (2026-08-01) -- one row per earned one-time 50%
-- referral bonus (one per converted referral, enforced by the unique index
-- on earned_from_lead_id). Caps a referrer at one bonus "slot" per
-- calendar month: if earned_month already has a bonus for this referrer,
-- applies_to_month rolls forward to the next open month instead of
-- stacking. ON DELETE CASCADE on both FKs -- see the delete_lead() crash
-- bug fixed the same day for why that matters.
CREATE TABLE IF NOT EXISTS referral_bonuses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    referrer_lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    earned_from_lead_id INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    earned_month TEXT NOT NULL,        -- YYYY-MM, the referred lead's conversion month
    applies_to_month TEXT NOT NULL,    -- YYYY-MM, may be rolled forward past earned_month
    status TEXT NOT NULL DEFAULT 'pending',  -- pending | applied
    applied_at TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_referral_bonuses_referrer ON referral_bonuses(referrer_lead_id);
CREATE UNIQUE INDEX IF NOT EXISTS idx_referral_bonuses_earned_from ON referral_bonuses(earned_from_lead_id);
"""

# referred_by_lead_id lives on `leads` itself (added via LEADS_MIGRATION_COLUMNS
# below) rather than a separate table -- referral chains are just a
# self-reference, no need for a join table. See models.py's referral
# functions and DECISIONS.md for the discount-tier reasoning.

# Columns added after the original schema — applied via ALTER TABLE so an
# existing hub.sqlite3 doesn't need to be wiped. (name, DDL type/default)
LEADS_MIGRATION_COLUMNS = [
    ("task_type", "TEXT"),
    ("time_estimate_hours", "REAL"),
    ("done_summary", "TEXT"),
    ("left_for_you_summary", "TEXT"),
    ("source_url", "TEXT"),
    ("referred_by_lead_id", "INTEGER REFERENCES leads(id)"),
]


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _migrate(conn):
    existing = {row["name"] for row in conn.execute("PRAGMA table_info(leads)").fetchall()}
    for col_name, col_type in LEADS_MIGRATION_COLUMNS:
        if col_name not in existing:
            conn.execute(f"ALTER TABLE leads ADD COLUMN {col_name} {col_type}")


def init_db():
    conn = get_connection()
    try:
        conn.executescript(SCHEMA)
        _migrate(conn)
        conn.commit()
    finally:
        conn.close()
