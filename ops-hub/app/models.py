import json
from datetime import date, datetime, timedelta

from .config import AUTO_DEADLINE_RULES, DEADLINE_THRESHOLDS, EVALUATION_WINDOWS_WEEKS, RATE_CARD
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
                 task_type, time_estimate_hours, done_summary, left_for_you_summary, source_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            ),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def update_lead(lead_id, data):
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
                source_url = ?, updated_at = datetime('now')
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
                lead_id,
            ),
        )
        conn.commit()
    finally:
        conn.close()


def delete_lead(lead_id):
    conn = get_connection()
    try:
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
