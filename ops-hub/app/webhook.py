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
    if secret and request.headers.get("X-Intake-Secret") != secret:
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
