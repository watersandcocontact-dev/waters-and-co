"""Intake webhook receiver — READY BUT INACTIVE.

This is built ahead of time so that once you sign up for an AI phone /
missed-call platform (e.g. Twilio + an AI answering layer, or an
all-in-one AU reception platform) and get an API key / shared secret,
turning this on is a config change, not a rewrite.

To activate:
  1. Set INTAKE_WEBHOOK_ENABLED=1 and INTAKE_WEBHOOK_SECRET=<your secret>
     as environment variables before starting the app (see ops-hub/README.md).
  2. Point your phone platform's webhook at:  POST /webhook/intake
  3. Send the shared secret as header  X-Intake-Secret: <your secret>

Expected JSON body (adapt field names to whatever your chosen platform
actually sends — Twilio, Smith.ai-style, or an AU reseller platform will
all differ slightly; this is a reasonable common shape):
{
  "caller_name": "Jane Smith",
  "caller_phone": "+61...",
  "caller_email": "optional@example.com",
  "call_summary": "Caller wants a quote for...",
  "transcript_url": "https://...",
  "business_line": "MissedCall"   // optional, defaults to MissedCall
}

Every call to this endpoint is logged to webhook_log regardless of
whether it creates a lead, so nothing is silently dropped while you're
still wiring things up.
"""

import json
import hmac
import os

from flask import Blueprint, jsonify, request

from .db import get_connection
from .models import create_lead

bp = Blueprint("webhook", __name__)


def _enabled():
    return os.environ.get("INTAKE_WEBHOOK_ENABLED") == "1"


def _log(source, payload, lead_id=None, note=None):
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO webhook_log (source, payload_json, lead_id, note) VALUES (?, ?, ?, ?)",
            (source, json.dumps(payload), lead_id, note),
        )
        conn.commit()
    finally:
        conn.close()


@bp.route("/webhook/intake", methods=["POST"])
def intake():
    payload = request.get_json(silent=True) or {}

    if not _enabled():
        _log("intake", payload, note="rejected: webhook disabled (no API key configured yet)")
        return (
            jsonify(
                {
                    "status": "disabled",
                    "message": (
                        "Intake webhook is built but inactive. Set INTAKE_WEBHOOK_ENABLED=1 "
                        "and INTAKE_WEBHOOK_SECRET once you've signed up for a phone platform."
                    ),
                }
            ),
            503,
        )

    secret = os.environ.get("INTAKE_WEBHOOK_SECRET")
    if not secret:
        # Fail closed, same pattern as /webhook/website-lead below -- an
        # enabled-but-unconfigured webhook must never silently accept
        # unauthenticated leads.
        _log("intake", payload, note="rejected: INTAKE_WEBHOOK_ENABLED=1 but INTAKE_WEBHOOK_SECRET not set")
        return (
            jsonify({"status": "error", "message": "INTAKE_WEBHOOK_SECRET not configured on the hub"}),
            503,
        )
    if not hmac.compare_digest(request.headers.get("X-Intake-Secret", ""), secret):
        _log("intake", payload, note="rejected: bad/missing secret")
        return jsonify({"status": "error", "message": "invalid secret"}), 401

    name = payload.get("caller_name") or "Unknown caller"
    lead_id = create_lead(
        {
            "name": name,
            "business_line": payload.get("business_line") or "MissedCall",
            "status": "New",
            "next_action": "Review call / call back",
            "notes": payload.get("call_summary") or payload.get("transcript_url") or "",
            "contact_phone": payload.get("caller_phone"),
            "contact_email": payload.get("caller_email"),
            "source": "webhook",
            "extra": {"raw_payload": payload},
        }
    )
    _log("intake", payload, lead_id=lead_id, note="created lead")
    return jsonify({"status": "ok", "lead_id": lead_id}), 201


@bp.route("/webhook/website-lead", methods=["POST"])
def website_lead():
    """Receiver for the PUBLIC website's contact-form leads, once the
    website is deployed somewhere other than this machine (e.g. Render)
    and can no longer reach the hub via a direct Python import/shared
    SQLite file — see docs/website_deployment.md for the full picture.

    Unlike /webhook/intake (gated behind INTAKE_WEBHOOK_ENABLED, which
    stays off until a phone platform is chosen), this endpoint is always
    reachable but ALWAYS requires WEBSITE_WEBHOOK_SECRET to be set and
    matched — fails closed, same "refuse to run insecurely" pattern as
    scripts/start_remote.sh. Uses its own secret (not INTAKE_WEBHOOK_SECRET)
    so configuring one webhook source never silently grants access to the
    other.

    Does both steps the local direct-import path used to do in one call:
    creates the lead, then immediately appends the pre-generated draft
    reply to its notes (mirrors website/webapp/routes.py's old
    _attach_draft helper exactly, so lead records look identical either
    way the website is deployed).
    """
    payload = request.get_json(silent=True) or {}

    secret = os.environ.get("WEBSITE_WEBHOOK_SECRET")
    if not secret:
        _log("website-lead", payload, note="rejected: WEBSITE_WEBHOOK_SECRET not configured")
        return (
            jsonify({"status": "error", "message": "WEBSITE_WEBHOOK_SECRET not configured on the hub"}),
            503,
        )
    if not hmac.compare_digest(request.headers.get("X-Website-Secret", ""), secret):
        _log("website-lead", payload, note="rejected: bad/missing secret")
        return jsonify({"status": "error", "message": "invalid secret"}), 401

    name = payload.get("name") or "Unknown"
    business_line = payload.get("business_line") or "GeneralEnquiry"
    next_action = payload.get("next_action") or "Respond to website enquiry"

    lead_id = create_lead(
        {
            "name": name,
            "business_line": business_line,
            "status": "New",
            "next_action": next_action,
            "notes": payload.get("message") or "",
            "contact_name": name,
            "contact_phone": payload.get("phone") or None,
            "contact_email": payload.get("email"),
            "source": "website",
            "done_summary": "Submitted via the website contact form.",
            "left_for_you_summary": "Review the drafted email reply and send it (or edit first).",
        }
    )

    draft_subject = payload.get("draft_subject")
    draft_body = payload.get("draft_body")
    if draft_subject and draft_body:
        from .models import get_lead, update_lead

        lead = get_lead(lead_id)
        if lead:
            draft_block = f"\n\n---\nDRAFTED REPLY (review before sending)\nSubject: {draft_subject}\n\n{draft_body}"
            data = {k: lead.get(k) for k in (
                "name", "business_line", "status", "next_action", "deadline", "estimated_value",
                "contact_name", "contact_phone", "contact_email", "au_state",
                "task_type", "time_estimate_hours", "done_summary", "left_for_you_summary", "source_url",
            )}
            data["extra"] = lead.get("extra") or {}
            data["notes"] = (lead.get("notes") or "") + draft_block
            update_lead(lead_id, data)

    _log("website-lead", payload, lead_id=lead_id, note="created lead + draft")
    return jsonify({"status": "ok", "lead_id": lead_id}), 201
