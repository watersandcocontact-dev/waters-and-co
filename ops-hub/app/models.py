import json
from datetime import date, datetime, timedelta

from .config import (
    AUTO_DEADLINE_RULES,
    DAY_JOB_HOURLY_RATE,
    DEADLINE_THRESHOLDS,
    DISCOUNT_INELIGIBLE_LINES,
    DISCOUNT_MARGIN_FLOOR_FRACTION,
    EVALUATION_WINDOWS_WEEKS,
    LOYALTY_REPEAT_CUSTOMER_PCT,
    RATE_CARD,
    REFERRAL_LOYALTY_STACKED_TIER_PCT,
    REFERRAL_ONE_TIME_BONUS_PCT,
    REFERRAL_RETENTION_CAP_PCT,
    REFERRAL_RETENTION_PCT_PER_ACTIVE,
    TAX_FIGURES,
)
from .db import get_connection


def _row_to_dict(row):
    d = dict(row)
    try:
        d["extra"] = json.loads(d.get("extra_json") or "{}")
    except (json.JSONDecodeError, TypeError):
        d["extra"] = {}
    return d


def list_leads(business_line=None, status=None, order_by="deadline"):
    conn = get_connection()
    try:
        q = """
            SELECT leads.*,
                   (SELECT COALESCE(SUM(hours), 0) FROM time_entries WHERE lead_id = leads.id) AS actual_hours
            FROM leads WHERE 1=1
        """
        params = []
        if business_line:
            q += " AND business_line = ?"
            params.append(business_line)
        if status:
            q += " AND status = ?"
            params.append(status)
        # NULLs (no deadline) sort last regardless of order
        if order_by == "deadline":
            q += " ORDER BY (deadline IS NULL) ASC, deadline ASC, created_at DESC"
        elif order_by == "created":
            q += " ORDER BY created_at DESC"
        elif order_by == "value":
            q += " ORDER BY (estimated_value IS NULL) ASC, estimated_value DESC"
        rows = conn.execute(q, params).fetchall()
        leads = [_row_to_dict(r) for r in rows]
        for lead in leads:
            rate_info = dollar_per_hour(lead)
            lead["dollar_per_hour"] = rate_info["per_hour"]
            lead["dollar_per_hour_source"] = rate_info["source"]
        if order_by == "rate":
            leads.sort(key=lambda lead: lead["dollar_per_hour"] or 0, reverse=True)
        return leads
    finally:
        conn.close()


def get_lead(lead_id):
    conn = get_connection()
    try:
        row = conn.execute(
            """
            SELECT leads.*,
                   (SELECT COALESCE(SUM(hours), 0) FROM time_entries WHERE lead_id = leads.id) AS actual_hours
            FROM leads WHERE id = ?
            """,
            (lead_id,),
        ).fetchone()
        if not row:
            return None
        lead = _row_to_dict(row)
        rate_info = dollar_per_hour(lead)
        lead["dollar_per_hour"] = rate_info["per_hour"]
        lead["dollar_per_hour_source"] = rate_info["source"]
        return lead
    finally:
        conn.close()


def _apply_auto_deadline(business_line, deadline, extra, au_state=None):
    """If a business line has an auto-deadline rule and the user left
    `deadline` blank, derive it from a trigger date in `extra`.

    `days_to_add` in the rule may be a flat int, or a per-state dict (e.g.
    land tax objection windows vary by state — NT is 30 days, others 60)."""
    if deadline:
        return deadline
    rule = AUTO_DEADLINE_RULES.get(business_line)
    if not rule:
        return deadline
    trigger_field, days_rule = rule
    trigger_val = extra.get(trigger_field)
    if not trigger_val:
        return deadline
    if isinstance(days_rule, dict):
        days = days_rule.get(au_state, days_rule.get("_default"))
    else:
        days = days_rule
    if days is None:
        return deadline
    try:
        trigger_date = datetime.strptime(trigger_val, "%Y-%m-%d").date()
        return (trigger_date + timedelta(days=days)).isoformat()
    except ValueError:
        return deadline


def create_lead(data):
    extra = data.get("extra") or {}
    deadline = _apply_auto_deadline(
        data["business_line"], data.get("deadline") or None, extra, au_state=data.get("au_state")
    )
    conn = get_connection()
    try:
        cur = conn.execute(
            """
            INSERT INTO leads
                (name, business_line, status, next_action, deadline, estimated_value,
                 notes, contact_name, contact_phone, contact_email, au_state, source, extra_json,
                 task_type, time_estimate_hours, done_summary, left_for_you_summary, source_url,
                 referred_by_lead_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["name"],
                data["business_line"],
                data.get("status") or "New",
                data.get("next_action"),
                deadline,
                data.get("estimated_value") or None,
                data.get("notes"),
                data.get("contact_name"),
                data.get("contact_phone"),
                data.get("contact_email"),
                data.get("au_state"),
                data.get("source") or "manual",
                json.dumps(extra),
                data.get("task_type") or None,
                data.get("time_estimate_hours") or None,
                data.get("done_summary"),
                data.get("left_for_you_summary"),
                data.get("source_url"),
                data.get("referred_by_lead_id") or None,
            ),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def _normalize_phone(phone):
    """Strip everything but digits, then keep the last 9 (AU mobile/landline
    body without country code or leading 0) so +61..., 0..., and space/dash
    formatted numbers all compare equal."""
    digits = "".join(ch for ch in (phone or "") if ch.isdigit())
    return digits[-9:] if len(digits) >= 9 else digits


def find_lead_by_phone(phone):
    """Best-effort match of an inbound SMS sender to an existing lead, for
    the httpSMS inbound webhook (see app/sms.py). Returns the most recently
    updated matching lead, or None if nothing matches."""
    target = _normalize_phone(phone)
    if not target:
        return None
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT id, contact_phone FROM leads WHERE contact_phone IS NOT NULL "
            "ORDER BY updated_at DESC, id DESC"
        ).fetchall()
    finally:
        conn.close()
    for row in rows:
        if _normalize_phone(row["contact_phone"]) == target:
            return get_lead(row["id"])
    return None


def _normalize_email(email):
    """Lowercase and strip surrounding whitespace/angle brackets so
    'Kirrilee <Info@QueensOfClutter.com.au>' and 'info@queensofclutter.com.au'
    compare equal. Deliberately does NOT strip +tags or dots -- those are
    Gmail-specific conventions, and treating them as equal would wrongly
    merge two genuinely different business addresses."""
    raw = (email or "").strip()
    if "<" in raw and ">" in raw:
        raw = raw[raw.rfind("<") + 1 : raw.rfind(">")]
    return raw.strip().lower()


def find_lead_by_email(email):
    """Best-effort match of an inbound email sender to an existing lead, for
    the campaign-reply-watch ingestion path (see
    scripts/create_email_reply_lead.py). Returns the most recently updated
    matching lead, or None if nothing matches.

    Mirrors find_lead_by_phone deliberately. Once the reply-watch scan
    detects individual follow-up messages rather than whole threads
    (2026-08-11 fix), a second message from someone who already has a lead
    must append to that lead instead of creating a duplicate case record."""
    target = _normalize_email(email)
    if not target:
        return None
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT id, contact_email FROM leads WHERE contact_email IS NOT NULL "
            "ORDER BY updated_at DESC, id DESC"
        ).fetchall()
    finally:
        conn.close()
    for row in rows:
        if _normalize_email(row["contact_email"]) == target:
            return get_lead(row["id"])
    return None


def append_note(lead_id, text):
    """Append a timestamped line to a lead's notes without clobbering
    existing notes -- used by the SMS inbound webhook so a client's reply
    lands in their case record instead of overwriting prior notes."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"[{stamp}] {text}"
    conn = get_connection()
    try:
        existing = conn.execute("SELECT notes FROM leads WHERE id = ?", (lead_id,)).fetchone()
        combined = (existing["notes"] + "\n" + line) if existing and existing["notes"] else line
        conn.execute(
            "UPDATE leads SET notes = ?, updated_at = datetime('now') WHERE id = ?",
            (combined, lead_id),
        )
        conn.commit()
    finally:
        conn.close()


def update_lead(lead_id, data):
    if data.get("referred_by_lead_id") and int(data["referred_by_lead_id"]) == lead_id:
        data = {**data, "referred_by_lead_id": None}
    extra = data.get("extra") or {}
    deadline = _apply_auto_deadline(
        data["business_line"], data.get("deadline") or None, extra, au_state=data.get("au_state")
    )
    conn = get_connection()
    try:
        conn.execute(
            """
            UPDATE leads SET
                name = ?, business_line = ?, status = ?, next_action = ?, deadline = ?,
                estimated_value = ?, notes = ?, contact_name = ?, contact_phone = ?,
                contact_email = ?, au_state = ?, extra_json = ?, task_type = ?,
                time_estimate_hours = ?, done_summary = ?, left_for_you_summary = ?,
                source_url = ?, referred_by_lead_id = ?, updated_at = datetime('now')
            WHERE id = ?
            """,
            (
                data["name"],
                data["business_line"],
                data.get("status") or "New",
                data.get("next_action"),
                deadline,
                data.get("estimated_value") or None,
                data.get("notes"),
                data.get("contact_name"),
                data.get("contact_phone"),
                data.get("contact_email"),
                data.get("au_state"),
                json.dumps(extra),
                data.get("task_type") or None,
                data.get("time_estimate_hours") or None,
                data.get("done_summary"),
                data.get("left_for_you_summary"),
                data.get("source_url"),
                data.get("referred_by_lead_id") or None,
                lead_id,
            ),
        )
        conn.commit()
    finally:
        conn.close()


def delete_lead(lead_id):
    conn = get_connection()
    try:
        # Null out anyone who named this lead as their referrer first --
        # referred_by_lead_id has no ON DELETE clause, and foreign_keys is
        # ON for every connection, so deleting a referenced lead would
        # otherwise throw sqlite3.IntegrityError (uncaught -> 500).
        conn.execute("UPDATE leads SET referred_by_lead_id = NULL WHERE referred_by_lead_id = ?", (lead_id,))
        conn.execute("DELETE FROM leads WHERE id = ?", (lead_id,))
        conn.commit()
    finally:
        conn.close()


def due_within(days, include_overdue=True):
    """Leads with a deadline within `days` from today (optionally including overdue)."""
    conn = get_connection()
    try:
        today = date.today().isoformat()
        cutoff = (date.today() + timedelta(days=days)).isoformat()
        lo = "0000-00-00" if include_overdue else today
        rows = conn.execute(
            """
            SELECT * FROM leads
            WHERE deadline IS NOT NULL AND deadline != '' AND deadline BETWEEN ? AND ?
            ORDER BY deadline ASC
            """,
            (lo, cutoff),
        ).fetchall()
        return [_row_to_dict(r) for r in rows]
    finally:
        conn.close()


def deadline_alert_buckets():
    """Group due/overdue leads into per-line threshold buckets for the dashboard banner."""
    today = date.today()
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM leads WHERE deadline IS NOT NULL AND deadline != '' "
            "AND status NOT IN ('Won','Lost') ORDER BY deadline ASC"
        ).fetchall()
    finally:
        conn.close()

    buckets = {"overdue": [], "due_14": [], "due_30": [], "due_60": []}
    for r in rows:
        d = _row_to_dict(r)
        try:
            dl = datetime.strptime(d["deadline"], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        days_left = (dl - today).days
        thresholds = DEADLINE_THRESHOLDS.get(d["business_line"], DEADLINE_THRESHOLDS["_default"])
        if days_left < 0:
            buckets["overdue"].append(d)
        elif days_left <= thresholds[0]:
            buckets["due_14"].append(d)
        elif days_left <= thresholds[1]:
            buckets["due_30"].append(d)
        elif days_left <= thresholds[2]:
            buckets["due_60"].append(d)
    return buckets


def new_or_updated_since(timestamp_iso):
    """Leads created or updated since the given ISO datetime string — the
    data source for scripts/new_case_check.py's periodic monitoring."""
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM leads WHERE created_at > ? OR updated_at > ? ORDER BY created_at ASC",
            (timestamp_iso, timestamp_iso),
        ).fetchall()
        return [_row_to_dict(r) for r in rows]
    finally:
        conn.close()


def counts_by_line():
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT business_line, COUNT(*) as n FROM leads GROUP BY business_line"
        ).fetchall()
        return {r["business_line"]: r["n"] for r in rows}
    finally:
        conn.close()


def _rate_card_default(business_line, task_type):
    rate = RATE_CARD.get(business_line)
    if isinstance(rate, dict):
        return rate.get(task_type) or rate.get("management") or next(iter(rate.values()), 0)
    return rate if rate is not None else 0


def dollar_per_hour(lead):
    """Compute a lead's $/hr and where the number came from, priority order:
    actual logged hours > the lead's own time estimate > the PRICING.md rate-card
    default for its business line (+ task type for GBP/MissedCall)."""
    estimated_value = lead.get("estimated_value")
    actual_hours = lead.get("actual_hours") or 0
    time_estimate = lead.get("time_estimate_hours")

    if estimated_value:
        if actual_hours and actual_hours > 0:
            return {"per_hour": round(estimated_value / actual_hours, 2), "source": "actual hours logged"}
        if time_estimate and time_estimate > 0:
            return {"per_hour": round(estimated_value / time_estimate, 2), "source": "your time estimate"}

    default_rate = _rate_card_default(lead.get("business_line"), lead.get("task_type"))
    return {"per_hour": default_rate, "source": "rate-card default"}


def log_time(lead_id, hours, note=None):
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO time_entries (lead_id, hours, note) VALUES (?, ?, ?)",
            (lead_id, hours, note),
        )
        conn.execute("UPDATE leads SET updated_at = datetime('now') WHERE id = ?", (lead_id,))
        conn.commit()
    finally:
        conn.close()


def get_time_entries(lead_id):
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM time_entries WHERE lead_id = ? ORDER BY logged_at DESC", (lead_id,)
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def _with_actual_hours_query(where_clause, params):
    conn = get_connection()
    try:
        rows = conn.execute(
            f"""
            SELECT leads.*,
                   (SELECT COALESCE(SUM(hours), 0) FROM time_entries WHERE lead_id = leads.id) AS actual_hours
            FROM leads
            WHERE {where_clause}
            """,
            params,
        ).fetchall()
        return [_row_to_dict(r) for r in rows]
    finally:
        conn.close()


def daily_queue():
    """The hub's primary view: every open, actionable lead (not Won/Lost, has
    a next action set) across ALL business lines, each annotated with its
    computed $/hr, sorted highest $/hr first — no other sort order.

    "Actionable today" = currently open work with something to do next, not
    literally scheduled for today's date (most leads don't have day-level
    scheduling, only an optional deadline) — this is the whole live worklist
    you'd triage each morning."""
    leads = _with_actual_hours_query(
        "status NOT IN ('Won','Lost') AND next_action IS NOT NULL AND next_action != ''", []
    )
    for lead in leads:
        rate_info = dollar_per_hour(lead)
        lead["dollar_per_hour"] = rate_info["per_hour"]
        lead["dollar_per_hour_source"] = rate_info["source"]
    leads.sort(key=lambda lead: lead["dollar_per_hour"] or 0, reverse=True)
    return leads


# --- Expansion budget + kill-switch (2026-07-31) ---
# Phase 1 = $0 budget (see config.BUDGET_PHASE) — these functions exist so
# tracking is ready the moment real spend starts, not retrofitted later.

def create_spend(data):
    spend_type = data["spend_type"]
    window_weeks = EVALUATION_WINDOWS_WEEKS.get(spend_type, EVALUATION_WINDOWS_WEEKS["other"])
    try:
        spend_date = datetime.strptime(data["spend_date"], "%Y-%m-%d").date()
        evaluation_due = (spend_date + timedelta(weeks=window_weeks)).isoformat()
    except (ValueError, KeyError):
        evaluation_due = None

    conn = get_connection()
    try:
        cur = conn.execute(
            """
            INSERT INTO expansion_spend
                (spend_date, business_line, spend_type, campaign_tag, amount,
                 funded_by, notes, evaluation_due)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["spend_date"],
                data.get("business_line") or None,
                spend_type,
                data.get("campaign_tag"),
                data["amount"],
                data.get("funded_by") or "personal_income",
                data.get("notes"),
                evaluation_due,
            ),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def update_spend_outcome(spend_id, outcome_leads, outcome_revenue, status=None):
    conn = get_connection()
    try:
        if status:
            conn.execute(
                "UPDATE expansion_spend SET outcome_leads = ?, outcome_revenue = ?, "
                "status = ?, updated_at = datetime('now') WHERE id = ?",
                (outcome_leads, outcome_revenue, status, spend_id),
            )
        else:
            conn.execute(
                "UPDATE expansion_spend SET outcome_leads = ?, outcome_revenue = ?, "
                "updated_at = datetime('now') WHERE id = ?",
                (outcome_leads, outcome_revenue, spend_id),
            )
        conn.commit()
    finally:
        conn.close()


def list_spend(status=None):
    conn = get_connection()
    try:
        q = "SELECT * FROM expansion_spend WHERE 1=1"
        params = []
        if status:
            q += " AND status = ?"
            params.append(status)
        q += " ORDER BY spend_date DESC"
        rows = conn.execute(q, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def best_performing_line():
    """Rough $/hr leader among Won leads with actual hours logged — used as
    the comparison point for expansion-spend cost-efficiency, per the
    'compare against what the same dollar would do elsewhere' instruction."""
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT leads.business_line, leads.estimated_value,
                   (SELECT COALESCE(SUM(hours), 0) FROM time_entries WHERE lead_id = leads.id) AS actual_hours
            FROM leads WHERE status = 'Won' AND estimated_value IS NOT NULL
            """
        ).fetchall()
    finally:
        conn.close()

    totals = {}
    for r in rows:
        if not r["actual_hours"]:
            continue
        rate = r["estimated_value"] / r["actual_hours"]
        line = r["business_line"]
        totals.setdefault(line, []).append(rate)

    if not totals:
        return None
    averaged = {line: sum(rates) / len(rates) for line, rates in totals.items()}
    best_line = max(averaged, key=averaged.get)
    return {"business_line": best_line, "avg_dollar_per_hour": round(averaged[best_line], 2)}


def spend_report():
    """Weekly-report-ready view: every spend with computed cost-per-lead,
    ROI, and a plain-language flag. Not a fully automated kill decision —
    surfaces the numbers so the call ("keep/adjust/kill") can actually be
    made with real data behind it, per the underperformance-detection spec."""
    today = date.today()
    spends = list_spend()
    best_line = best_performing_line()

    for s in spends:
        s["cost_per_lead"] = round(s["amount"] / s["outcome_leads"], 2) if s["outcome_leads"] else None
        s["roi"] = round((s["outcome_revenue"] - s["amount"]) / s["amount"], 2) if s["amount"] else None

        try:
            due = datetime.strptime(s["evaluation_due"], "%Y-%m-%d").date() if s["evaluation_due"] else None
        except ValueError:
            due = None
        past_due = due is not None and today >= due

        if s["status"] != "active":
            s["flag"] = f"already marked {s['status']}"
        elif not past_due:
            s["flag"] = f"within evaluation window (due {s['evaluation_due']})"
        elif not s["outcome_leads"] and not s["outcome_revenue"]:
            s["flag"] = "NO MEASURABLE RETURN — evaluate now (kill/adjust/pause)"
        elif s["roi"] is not None and s["roi"] < 0:
            s["flag"] = "UNDERPERFORMING — costing more than it's returning, review"
        else:
            s["flag"] = "showing a return — compare against best-performing line below before deciding to scale"

    return {"spends": spends, "best_performing_line": best_line}


# --- Stripe payments (2026-08-01) ---
# One row per payment request against a lead. Client-side code never sets
# status='paid' -- only the Stripe webhook (app/payments.py) does that,
# after verifying the event signature, so a client can't just hit the
# success_url and mark themselves paid without actually paying.

def create_payment(data):
    conn = get_connection()
    try:
        cur = conn.execute(
            """
            INSERT INTO payments
                (lead_id, checkout_session_id, checkout_url, amount_cents,
                 currency, description, status)
            VALUES (?, ?, ?, ?, ?, ?, 'pending')
            """,
            (
                data["lead_id"],
                data["checkout_session_id"],
                data["checkout_url"],
                data["amount_cents"],
                data.get("currency") or "aud",
                data.get("description"),
            ),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def list_payments_for_lead(lead_id):
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM payments WHERE lead_id = ? ORDER BY created_at DESC", (lead_id,)
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def mark_payment_paid(checkout_session_id, payment_intent_id=None):
    """Idempotent -- Stripe can and will redeliver the same webhook event."""
    conn = get_connection()
    try:
        conn.execute(
            """
            UPDATE payments SET status = 'paid', payment_intent_id = ?,
                paid_at = datetime('now')
            WHERE checkout_session_id = ? AND status != 'paid'
            """,
            (payment_intent_id, checkout_session_id),
        )
        conn.commit()
    finally:
        conn.close()


def mark_payment_status(checkout_session_id, status):
    """For non-paid terminal states (expired, canceled) via webhook."""
    conn = get_connection()
    try:
        conn.execute(
            "UPDATE payments SET status = ? WHERE checkout_session_id = ? AND status = 'pending'",
            (status, checkout_session_id),
        )
        conn.commit()
    finally:
        conn.close()


# --- Referral & loyalty program (2026-08-01) ---
# Advisory only -- this computes eligibility/recommended discount %, it
# never touches a Stripe payment amount automatically. You still decide
# the actual number when creating a payment request (app/payments.py);
# these numbers are what to factor in. Config: REFERRAL_* / LOYALTY_* /
# DISCOUNT_* in config.py, reasoning in DECISIONS.md.

def list_leads_basic():
    """id + name for every lead, for the "referred by" picker -- cheap,
    no joins, fine at solo-operator lead volumes."""
    conn = get_connection()
    try:
        rows = conn.execute("SELECT id, name, business_line FROM leads ORDER BY name").fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def _is_repeat_customer(lead, all_won_leads):
    """Same contact (email, falling back to phone) has another Won lead."""
    contact_key = (lead.get("contact_email") or "").strip().lower() or (lead.get("contact_phone") or "").strip()
    if not contact_key:
        return False
    for other in all_won_leads:
        if other["id"] == lead["id"]:
            continue
        other_key = (other.get("contact_email") or "").strip().lower() or (other.get("contact_phone") or "").strip()
        if other_key and other_key == contact_key:
            return True
    return False


def _month_str(dt_str):
    """'2026-07-31 16:44:15' or '2026-07-31' -> '2026-07'."""
    return (dt_str or "")[:7]


def _next_month(month_str):
    year, month = int(month_str[:4]), int(month_str[5:7])
    month += 1
    if month > 12:
        month = 1
        year += 1
    return f"{year:04d}-{month:02d}"


def _sync_referral_bonuses(conn, referrer_lead_id):
    """Materialize a referral_bonuses row for every converted (Won) referral
    that doesn't have one yet -- idempotent (unique index on
    earned_from_lead_id backs this up at the DB level too). Conversion
    month is read off the referred lead's updated_at, same proxy
    business_ytd_income() already uses elsewhere for "when did this
    convert" since there's no dedicated won_at timestamp.

    Caps the referrer at one bonus per calendar month: if earned_month
    already has a bonus for this referrer, rolls applies_to_month forward
    to the next month that doesn't."""
    converted = conn.execute(
        "SELECT id, updated_at FROM leads WHERE referred_by_lead_id = ? AND status = 'Won' ORDER BY updated_at",
        (referrer_lead_id,),
    ).fetchall()
    for row in converted:
        exists = conn.execute(
            "SELECT id FROM referral_bonuses WHERE earned_from_lead_id = ?", (row["id"],)
        ).fetchone()
        if exists:
            continue
        earned_month = _month_str(row["updated_at"])
        applies_to = earned_month
        while conn.execute(
            "SELECT id FROM referral_bonuses WHERE referrer_lead_id = ? AND applies_to_month = ?",
            (referrer_lead_id, applies_to),
        ).fetchone():
            applies_to = _next_month(applies_to)
        conn.execute(
            """INSERT INTO referral_bonuses
                (referrer_lead_id, earned_from_lead_id, earned_month, applies_to_month, status)
               VALUES (?, ?, ?, ?, 'pending')""",
            (referrer_lead_id, row["id"], earned_month, applies_to),
        )


def list_referral_bonuses(lead_id):
    conn = get_connection()
    try:
        _sync_referral_bonuses(conn, lead_id)
        conn.commit()
        rows = conn.execute(
            """
            SELECT referral_bonuses.*, leads.name AS earned_from_name
            FROM referral_bonuses JOIN leads ON leads.id = referral_bonuses.earned_from_lead_id
            WHERE referrer_lead_id = ?
            ORDER BY applies_to_month
            """,
            (lead_id,),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_referral_bonus(bonus_id):
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM referral_bonuses WHERE id = ?", (bonus_id,)).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def mark_bonus_applied(bonus_id):
    """Returns the bonus's referrer_lead_id (its own DB-recorded owner,
    never a client-supplied value) so the caller can redirect correctly
    without trusting form input for ownership -- fixes an IDOR where a
    crafted POST could mark any bonus applied and redirect anywhere."""
    conn = get_connection()
    try:
        row = conn.execute("SELECT referrer_lead_id FROM referral_bonuses WHERE id = ?", (bonus_id,)).fetchone()
        if row is None:
            return None
        conn.execute(
            "UPDATE referral_bonuses SET status = 'applied', applied_at = datetime('now') WHERE id = ? AND status = 'pending'",
            (bonus_id,),
        )
        conn.commit()
        return row["referrer_lead_id"]
    finally:
        conn.close()


def referral_summary(lead_id):
    """Everything needed to show the Referral & Loyalty advisory box on a
    lead's page: who referred them, who they've referred and whether those
    converted, repeat-customer status, the recommended discount tier, and
    a margin-floor flag if that discount would cut too deep into this
    line's usual rate."""
    lead = get_lead(lead_id)
    if lead is None:
        return None

    conn = get_connection()
    try:
        referred_by = None
        if lead.get("referred_by_lead_id"):
            row = conn.execute(
                "SELECT id, name, business_line FROM leads WHERE id = ?", (lead["referred_by_lead_id"],)
            ).fetchone()
            referred_by = dict(row) if row else None

        referred_rows = conn.execute(
            "SELECT id, name, business_line, status FROM leads WHERE referred_by_lead_id = ? ORDER BY created_at",
            (lead_id,),
        ).fetchall()
        referrals_made = [dict(r) for r in referred_rows]

        all_won = [dict(r) for r in conn.execute(
            "SELECT id, contact_email, contact_phone FROM leads WHERE status = 'Won'"
        ).fetchall()]
    finally:
        conn.close()

    pending_bonuses = [b for b in list_referral_bonuses(lead_id) if b["status"] == "pending"]

    converted_referrals = [r for r in referrals_made if r["status"] == "Won"]
    # "active" = currently an engaged client, not lost -- Won or any open
    # in-progress status counts, only Lost drops out.
    active_referred = [r for r in referrals_made if r["status"] != "Lost"]

    is_repeat = _is_repeat_customer(lead, all_won)
    is_active_referrer = len(active_referred) > 0

    retention_pct = min(
        len(active_referred) * REFERRAL_RETENTION_PCT_PER_ACTIVE,
        REFERRAL_RETENTION_CAP_PCT,
    ) if is_active_referrer else 0

    if is_repeat and is_active_referrer:
        tier = "stacked"
        recommended_pct = REFERRAL_LOYALTY_STACKED_TIER_PCT
    elif is_repeat:
        tier = "loyalty"
        recommended_pct = LOYALTY_REPEAT_CUSTOMER_PCT
    elif is_active_referrer:
        tier = "referrer_retention"
        recommended_pct = retention_pct
    else:
        tier = "none"
        recommended_pct = 0

    line = lead.get("business_line")
    eligible = line not in DISCOUNT_INELIGIBLE_LINES
    rate_default = _rate_card_default(line, lead.get("task_type"))
    margin_floor_flag = False
    if eligible and recommended_pct and rate_default:
        effective_rate = rate_default * (1 - recommended_pct / 100)
        if effective_rate < rate_default * DISCOUNT_MARGIN_FLOOR_FRACTION:
            margin_floor_flag = True

    return {
        "referred_by": referred_by,
        "referrals_made": referrals_made,
        "converted_referrals_count": len(converted_referrals),
        "active_referred_count": len(active_referred),
        "is_repeat_customer": is_repeat,
        "pending_bonuses": pending_bonuses,
        "one_time_bonus_pct": REFERRAL_ONE_TIME_BONUS_PCT,
        "tier": tier,
        "recommended_discount_pct": recommended_pct if eligible else 0,
        "loyalty_ineligible_line": not eligible,
        "margin_floor_flag": margin_floor_flag,
    }


def referral_dashboard():
    """Portfolio-wide view: every lead currently sitting in a referral/
    loyalty tier, with a rough estimated monthly discount cost (rate-card
    default or the lead's own estimated_value, whichever's known -- this is
    a proxy, not a real recurring-billing figure, since the hub doesn't
    bill on a subscription model) and any margin-floor flags."""
    conn = get_connection()
    try:
        rows = conn.execute("SELECT id FROM leads WHERE status NOT IN ('Lost')").fetchall()
    finally:
        conn.close()

    entries = []
    total_estimated_monthly_cost = 0.0
    flagged = []
    for row in rows:
        summary = referral_summary(row["id"])
        if not summary or summary["tier"] == "none":
            continue
        lead = get_lead(row["id"])
        rate_default = _rate_card_default(lead.get("business_line"), lead.get("task_type"))
        base_value = lead.get("estimated_value") or rate_default or 0
        estimated_cost = round(base_value * summary["recommended_discount_pct"] / 100, 2)
        total_estimated_monthly_cost += estimated_cost
        entry = {
            "lead": lead,
            "summary": summary,
            "estimated_monthly_cost": estimated_cost,
        }
        entries.append(entry)
        if summary["margin_floor_flag"]:
            flagged.append(entry)

    return {
        "entries": entries,
        "total_estimated_monthly_cost": round(total_estimated_monthly_cost, 2),
        "flagged": flagged,
    }


# --- Tax tracking (2026-07-31) ---
# Organisation/flagging tool, not tax advice. See config.TAX_FIGURES for
# sourced figures and wave3-unscoped/tax_tracking/ato_figures_verification.md
# for the research behind them.

def _current_fy_start():
    """1 July of the current Australian financial year."""
    today = date.today()
    year = today.year if today.month >= 7 else today.year - 1
    return date(year, 7, 1)


def create_pay_period(data):
    conn = get_connection()
    try:
        cur = conn.execute(
            """
            INSERT INTO day_job_pay_periods
                (pay_date, gross, tax_withheld, net, super_amount, hours_worked, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["pay_date"],
                data["gross"],
                data["tax_withheld"],
                data["net"],
                data.get("super_amount"),
                data.get("hours_worked"),
                data.get("notes"),
            ),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def list_pay_periods():
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT * FROM day_job_pay_periods ORDER BY pay_date DESC"
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def day_job_ytd():
    fy_start = _current_fy_start().isoformat()
    conn = get_connection()
    try:
        row = conn.execute(
            """
            SELECT COALESCE(SUM(gross), 0) AS gross,
                   COALESCE(SUM(tax_withheld), 0) AS tax_withheld,
                   COALESCE(SUM(net), 0) AS net,
                   COALESCE(SUM(super_amount), 0) AS super_amount,
                   COALESCE(SUM(hours_worked), 0) AS hours_worked,
                   COUNT(*) AS pay_periods
            FROM day_job_pay_periods WHERE pay_date >= ?
            """,
            (fy_start,),
        ).fetchone()
        return dict(row)
    finally:
        conn.close()


def create_expense(data):
    conn = get_connection()
    try:
        cur = conn.execute(
            """
            INSERT INTO deductible_expenses
                (expense_date, context, category, amount, description,
                 receipt_held, no_receipt_bucket, deduction_treatment, km_count, hours_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["expense_date"],
                data["context"],
                data["category"],
                data["amount"],
                data.get("description"),
                data.get("receipt_held") or "yes",
                data.get("no_receipt_bucket"),
                data.get("deduction_treatment"),
                data.get("km_count"),
                data.get("hours_count"),
            ),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def list_expenses(context=None, since=None):
    conn = get_connection()
    try:
        q = "SELECT * FROM deductible_expenses WHERE 1=1"
        params = []
        if context:
            q += " AND context = ?"
            params.append(context)
        if since:
            q += " AND expense_date >= ?"
            params.append(since)
        q += " ORDER BY expense_date DESC"
        rows = conn.execute(q, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def no_receipt_cap_usage():
    """Sum of no-receipt-exception spend against each cap, YTD, flagged if
    a cap is exceeded. Caps and bucket meanings: config.TAX_FIGURES."""
    fy_start = _current_fy_start().isoformat()
    expenses = list_expenses(since=fy_start)
    buckets = {
        "combined_300": {"used": 0.0, "cap": TAX_FIGURES["no_receipt_combined_cap"]},
        "laundry_150": {"used": 0.0, "cap": TAX_FIGURES["no_receipt_laundry_cap"]},
        "small_expense_200": {"used": 0.0, "cap": TAX_FIGURES["no_receipt_small_expense_cap"]},
        "phone_internet_50": {"used": 0.0, "cap": TAX_FIGURES["no_record_phone_internet_threshold"]},
    }
    for e in expenses:
        bucket = e.get("no_receipt_bucket")
        if bucket in buckets:
            buckets[bucket]["used"] += e["amount"]
            # laundry counts inside combined_300 too, not additional
            if bucket == "laundry_150":
                buckets["combined_300"]["used"] += e["amount"]
    for b in buckets.values():
        b["remaining"] = round(b["cap"] - b["used"], 2)
        b["over"] = b["used"] > b["cap"]
    return buckets


def business_ytd_income(business_line=None):
    """Won leads' estimated_value since 1 July, the closest proxy this hub
    has for realised business income (not cash-received timing)."""
    fy_start = _current_fy_start().isoformat()
    conn = get_connection()
    try:
        q = (
            "SELECT business_line, COALESCE(SUM(estimated_value), 0) AS total "
            "FROM leads WHERE status = 'Won' AND updated_at >= ?"
        )
        params = [fy_start]
        if business_line:
            q += " AND business_line = ?"
            params.append(business_line)
        q += " GROUP BY business_line"
        rows = conn.execute(q, params).fetchall()
        by_line = {r["business_line"]: r["total"] for r in rows}
        return {"by_line": by_line, "total": sum(by_line.values())}
    finally:
        conn.close()


def business_ytd_expenses():
    fy_start = _current_fy_start().isoformat()
    expenses = [e for e in list_expenses(since=fy_start) if e["context"] != "day_job"]
    return round(sum(e["amount"] for e in expenses), 2)


def _marginal_rate_for(income):
    for bracket in TAX_FIGURES["tax_brackets"]:
        ceiling = bracket["ceiling"]
        if ceiling is None or income < ceiling:
            return bracket["rate"]
    return TAX_FIGURES["tax_brackets"][-1]["rate"]


def combined_tax_position():
    """Day-job YTD gross + business YTD profit (income - business expenses),
    combined for a real (not planning-estimate) marginal-rate and
    threshold position. Not advice — numbers for you and your accountant."""
    day_job = day_job_ytd()
    biz_income = business_ytd_income()
    biz_expenses = business_ytd_expenses()
    biz_profit = biz_income["total"] - biz_expenses

    combined_income = day_job["gross"] + biz_profit
    marginal_rate = _marginal_rate_for(combined_income)

    concessional_used = day_job["super_amount"]  # employer SG YTD; personal contributions not tracked separately yet
    concessional_headroom = round(TAX_FIGURES["concessional_super_cap"] - concessional_used, 2)

    gst_progress = round((biz_income["total"] / TAX_FIGURES["gst_registration_threshold"]) * 100, 1) if TAX_FIGURES["gst_registration_threshold"] else 0

    thresholds_crossed = []
    for t in (18200, 45000, 135000, 190000):
        if combined_income >= t:
            thresholds_crossed.append(t)

    return {
        "day_job_ytd": day_job,
        "business_ytd_income": biz_income,
        "business_ytd_expenses": biz_expenses,
        "business_ytd_profit": round(biz_profit, 2),
        "combined_income": round(combined_income, 2),
        "marginal_rate": marginal_rate,
        "concessional_super_used": concessional_used,
        "concessional_super_headroom": concessional_headroom,
        "gst_threshold_progress_pct": gst_progress,
        "gst_threshold_flag": biz_income["total"] >= TAX_FIGURES["gst_registration_threshold"],
        "division_293_flag": combined_income >= TAX_FIGURES["division_293_threshold"],
        "thresholds_crossed": thresholds_crossed,
    }


def day_job_vs_business_comparison():
    """Day-job $/hr (fixed rate, or computed from the latest pay period if
    hours are logged) vs business $/hr (best-performing line). Surfaces a
    signal, not a decision — see docs/day_job_vs_business.md for why this
    stays a signal rather than an automated 'go part-time' call (mortgage
    serviceability and income consistency both matter and aren't tracked
    here)."""
    pay_periods = list_pay_periods()
    day_job_rate = DAY_JOB_HOURLY_RATE
    if pay_periods and pay_periods[0].get("hours_worked"):
        latest = pay_periods[0]
        day_job_rate = round(latest["gross"] / latest["hours_worked"], 2)

    best_line = best_performing_line()
    business_rate = best_line["avg_dollar_per_hour"] if best_line else None

    won_with_hours = 0
    conn = get_connection()
    try:
        won_with_hours = conn.execute(
            """
            SELECT COUNT(*) AS n FROM leads
            WHERE status = 'Won'
              AND (SELECT COALESCE(SUM(hours),0) FROM time_entries WHERE lead_id = leads.id) > 0
            """
        ).fetchone()["n"]
    finally:
        conn.close()

    if won_with_hours < 8:
        signal = (
            f"Not enough data yet ({won_with_hours} completed jobs with logged hours) — "
            "need consistent volume before this comparison means anything. "
            "Keep logging time on every job."
        )
    elif business_rate and business_rate > day_job_rate:
        signal = (
            f"Business $/hr (${business_rate}) has been exceeding day-job $/hr (${day_job_rate}) "
            f"across {won_with_hours} completed jobs. Worth a real conversation about reducing "
            "day-job days — but check mortgage/lending implications first (see notes)."
        )
    else:
        signal = f"Day-job $/hr (${day_job_rate}) still at or above business average (${business_rate or 0}) — keep both going."

    return {
        "day_job_hourly_rate": day_job_rate,
        "business_hourly_rate": business_rate,
        "best_performing_line": best_line,
        "won_jobs_with_hours": won_with_hours,
        "signal": signal,
        "lending_note": (
            "Reducing PAYG hours can affect mortgage serviceability — lenders "
            "typically discount or fully exclude sole-trader income until ~2 years "
            "of tax returns exist. Worth raising with your mortgage broker/lender "
            "before changing day-job days, not just comparing $/hr."
        ),
    }


def accountant_export_data():
    """Everything for the one-document accountant handoff: day-job +
    business deductions separated, no-receipt cap usage, combined income
    position, and the speak-to-your-accountant discussion points with real
    numbers. Not lodgement, not advice — an organised handoff."""
    fy_start = _current_fy_start().isoformat()
    all_expenses = list_expenses(since=fy_start)
    day_job_expenses = [e for e in all_expenses if e["context"] == "day_job"]
    business_expenses = [e for e in all_expenses if e["context"] != "day_job"]

    position = combined_tax_position()
    caps = no_receipt_cap_usage()

    concessional_headroom = position["concessional_super_headroom"]
    marginal_rate = position["marginal_rate"]
    # Rough tax-saving estimate: headroom taxed at 15% inside super vs marginal rate outside
    super_saving_estimate = round(concessional_headroom * max(marginal_rate - 0.15, 0), 2)

    return {
        "financial_year": TAX_FIGURES["financial_year"],
        "generated": date.today().isoformat(),
        "day_job_expenses": day_job_expenses,
        "business_expenses": business_expenses,
        "no_receipt_caps": caps,
        "position": position,
        "speak_to_accountant": {
            "concessional_super_headroom": concessional_headroom,
            "estimated_tax_saving_if_fully_used": super_saving_estimate,
            "carry_forward_note": (
                "5-year carry-forward available if total super balance was under "
                f"${TAX_FIGURES['carry_forward_eligible_tsb_threshold']:,} at last 30 June. "
                "FY2021-22 unused space expires 30 June 2027 (confirm exact remaining "
                "amount with accountant — this tool only tracks employer SG, not any "
                "prior years' unused cap)."
            ),
            "gst_threshold_progress_pct": position["gst_threshold_progress_pct"],
            "gst_flag": position["gst_threshold_flag"],
            "division_293_flag": position["division_293_flag"],
            "logbook_vs_cents_per_km_note": (
                "Worth a real comparison once a few months of vehicle-use data exist — "
                "cents/km is capped at "
                f"{TAX_FIGURES['cents_per_km_max_km']:,}km/car/year at "
                f"${TAX_FIGURES['cents_per_km_rate']}/km "
                f"(= ${TAX_FIGURES['cents_per_km_max_km'] * TAX_FIGURES['cents_per_km_rate']:,.0f} max); "
                "logbook method has no cap but needs a 12-week logbook plus ongoing records."
            ),
        },
        "unconfirmed_figures": TAX_FIGURES["unconfirmed_for_this_fy"],
    }
