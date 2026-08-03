"""Native SMS via httpSMS (self-hosted) — READY BUT INACTIVE.

Uses the dedicated work phone's own SIM/number for genuine native texting
(not WhatsApp, not a rented virtual number), via a self-hosted httpSMS
backend (https://github.com/NdoleStudio/httpsms) that the work phone's
httpSMS Android app pairs with. This module is the ops hub's side of that
integration — it does not install or run httpSMS itself (see
docs/httpsms_setup.md for the self-hosting steps, which need Docker and
are your call, not something I can do from here).

Reused across every business line that needs outbound texting (review
requests, appointment reminders, deadline nudges, follow-ups) via
send_sms() — one integration, not one per line, same principle as the
Twilio-style intake webhook.

To activate:
  1. Self-host httpSMS (see docs/httpsms_setup.md) and pair the work
     phone's httpSMS Android app to it.
  2. Set HTTPSMS_ENABLED=1, HTTPSMS_API_KEY=<your key>,
     HTTPSMS_FROM_NUMBER=<the work phone's number, e.g. +614xxxxxxxx>,
     and HTTPSMS_API_URL (defaults to the public api.httpsms.com if
     you're not self-hosting the API layer, or your own self-hosted URL)
     as environment variables before starting the app.
  3. In httpSMS's own dashboard, point its outbound webhook for
     "message.phone.received" at:  POST /webhook/sms-inbound
  4. Optionally set HTTPSMS_WEBHOOK_SECRET to the signing secret httpSMS
     gives you for that webhook, so inbound requests are verified
     (JWT HS256) rather than trusted blindly — the webhook still works
     without this, it just skips verification and logs a warning.

Field names below (contact/content/owner for inbound, from/to/content for
outbound) are httpSMS's documented shape as of 2026-08 — worth a quick
diff against https://docs.httpsms.com/webhooks/events once actually
wired up, the same "adapt to what the platform really sends" caveat as
the intake webhook.
"""

import json
import os
import time

import requests
from flask import Blueprint, jsonify, request

from .db import get_connection
from .models import append_note, create_lead, find_lead_by_phone

bp = Blueprint("sms", __name__)

DEFAULT_API_URL = "https://api.httpsms.com"

# Local safety-net rate limit, on top of whatever's configured in httpSMS
# itself -- this is a one-to-one client texting line, never a bulk blast
# tool. Simple in-process counter; fine for a solo operator's send volume,
# not built for multi-process deployment.
_MAX_SENDS_PER_MINUTE = 10
_send_timestamps = []


def _enabled():
    return os.environ.get("HTTPSMS_ENABLED") == "1"


def _api_url():
    return os.environ.get("HTTPSMS_API_URL", DEFAULT_API_URL).rstrip("/")


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


def _rate_limit_ok():
    now = time.time()
    cutoff = now - 60
    while _send_timestamps and _send_timestamps[0] < cutoff:
        _send_timestamps.pop(0)
    if len(_send_timestamps) >= _MAX_SENDS_PER_MINUTE:
        return False
    _send_timestamps.append(now)
    return True


def send_sms(to, body, business_line=None, lead_id=None):
    """Send a text from the work phone's number via httpSMS. Returns a
    dict with 'status': 'sent' | 'disabled' | 'rate_limited' | 'error',
    never raises -- callers (review-request flow, appointment reminders,
    deadline nudges) should treat SMS as best-effort, not block on it.
    """
    payload = {"to": to, "body_preview": (body or "")[:80], "business_line": business_line}

    if not _enabled():
        _log("sms_send", payload, lead_id=lead_id, note="skipped: HTTPSMS_ENABLED not set")
        return {"status": "disabled", "message": "httpSMS not configured yet"}

    if not _rate_limit_ok():
        _log("sms_send", payload, lead_id=lead_id, note="skipped: local rate limit hit")
        return {"status": "rate_limited", "message": "sent too many texts in the last minute"}

    api_key = os.environ.get("HTTPSMS_API_KEY")
    from_number = os.environ.get("HTTPSMS_FROM_NUMBER")
    if not api_key or not from_number:
        _log("sms_send", payload, lead_id=lead_id, note="error: missing API key or from-number")
        return {"status": "error", "message": "HTTPSMS_API_KEY / HTTPSMS_FROM_NUMBER not set"}

    try:
        resp = requests.post(
            f"{_api_url()}/v1/messages/send",
            headers={"x-api-key": api_key, "Content-Type": "application/json"},
            json={"from": from_number, "to": to, "content": body},
            timeout=15,
        )
        ok = resp.ok
        _log(
            "sms_send",
            payload,
            lead_id=lead_id,
            note=f"httpSMS response {resp.status_code}" if ok else f"httpSMS error {resp.status_code}: {resp.text[:200]}",
        )
        return {"status": "sent" if ok else "error", "http_status": resp.status_code}
    except requests.RequestException as exc:
        _log("sms_send", payload, lead_id=lead_id, note=f"exception: {exc}")
        return {"status": "error", "message": str(exc)}


def _verify_webhook(raw_body, headers):
    """Best-effort JWT (HS256) verification of the inbound webhook using
    HTTPSMS_WEBHOOK_SECRET. Returns True if verified, False if the
    signature is present but invalid, None if no secret is configured yet
    (caller should still process the request but log that it went
    unverified, same 'built but not fully wired up yet' pattern as the
    rest of this module)."""
    secret = os.environ.get("HTTPSMS_WEBHOOK_SECRET")
    if not secret:
        return None
    token = headers.get("Authorization", "").removeprefix("Bearer ").strip()
    if not token:
        return False
    try:
        import jwt  # PyJWT -- already available in this environment

        jwt.decode(token, secret, algorithms=["HS256"], options={"verify_aud": False})
        return True
    except Exception:
        return False


@bp.route("/webhook/sms-inbound", methods=["POST"])
def sms_inbound():
    payload = request.get_json(silent=True) or {}

    if not _enabled():
        _log("sms_inbound", payload, note="rejected: SMS module disabled (HTTPSMS_ENABLED not set)")
        return jsonify({"status": "disabled"}), 503

    verified = _verify_webhook(request.get_data(), request.headers)
    note_suffix = ""
    if verified is False:
        _log("sms_inbound", payload, note="rejected: webhook signature failed verification")
        return jsonify({"status": "error", "message": "invalid signature"}), 401
    if verified is None:
        note_suffix = " (unverified -- set HTTPSMS_WEBHOOK_SECRET to verify signatures)"

    if request.headers.get("X-Event-Type") and request.headers["X-Event-Type"] != "message.phone.received":
        _log("sms_inbound", payload, note=f"ignored event type {request.headers.get('X-Event-Type')}")
        return jsonify({"status": "ignored"}), 200

    # httpSMS's documented shape for message.phone.received: the event data
    # carries contact (sender), content (message text), owner (the work
    # phone's own number that received it). Some deployments nest this
    # under a "data" key (CloudEvents-style) -- handle both.
    data = payload.get("data", payload)
    sender = data.get("contact")
    content = data.get("content", "")

    lead = find_lead_by_phone(sender) if sender else None
    if lead:
        append_note(lead["id"], f"SMS reply: {content}")
        _log("sms_inbound", payload, lead_id=lead["id"], note="appended to existing lead" + note_suffix)
        return jsonify({"status": "ok", "lead_id": lead["id"]}), 200

    # No matching lead -- log it as a new, untagged enquiry rather than
    # silently dropping a real reply from a real phone number.
    lead_id = create_lead(
        {
            "name": sender or "Unknown SMS sender",
            "business_line": "GeneralEnquiry",
            "status": "New",
            "next_action": "Identify which case this SMS reply belongs to",
            "notes": f"Inbound SMS with no matching lead: {content}",
            "contact_phone": sender,
            "source": "sms_webhook",
        }
    )
    _log("sms_inbound", payload, lead_id=lead_id, note="created new lead, no phone match" + note_suffix)
    return jsonify({"status": "ok", "lead_id": lead_id, "matched": False}), 201
