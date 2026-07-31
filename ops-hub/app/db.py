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
"""

# Columns added after the original schema — applied via ALTER TABLE so an
# existing hub.sqlite3 doesn't need to be wiped. (name, DDL type/default)
LEADS_MIGRATION_COLUMNS = [
    ("task_type", "TEXT"),
    ("time_estimate_hours", "REAL"),
    ("done_summary", "TEXT"),
    ("left_for_you_summary", "TEXT"),
    ("source_url", "TEXT"),
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
