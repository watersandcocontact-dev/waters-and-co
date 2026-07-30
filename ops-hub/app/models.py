import json
from datetime import date, datetime, timedelta

from .config import AUTO_DEADLINE_RULES, DEADLINE_THRESHOLDS
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
        q = "SELECT * FROM leads WHERE 1=1"
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
        return [_row_to_dict(r) for r in rows]
    finally:
        conn.close()


def get_lead(lead_id):
    conn = get_connection()
    try:
        row = conn.execute("SELECT * FROM leads WHERE id = ?", (lead_id,)).fetchone()
        return _row_to_dict(row) if row else None
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
                 notes, contact_name, contact_phone, contact_email, au_state, source, extra_json)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                contact_email = ?, au_state = ?, extra_json = ?, updated_at = datetime('now')
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


def counts_by_line():
    conn = get_connection()
    try:
        rows = conn.execute(
            "SELECT business_line, COUNT(*) as n FROM leads GROUP BY business_line"
        ).fetchall()
        return {r["business_line"]: r["n"] for r in rows}
    finally:
        conn.close()
