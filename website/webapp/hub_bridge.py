"""Bridge into the ops hub's lead database — two modes, switched by the
HUB_MODE environment variable:

- HUB_MODE=local (default) — a direct Python import of the hub's own
  models.create_lead()/get_lead()/update_lead(), the same "file" every
  other business line already writes to. No HTTP call, no webhook gate.
  Only works when both apps run on the same machine and share the same
  SQLite file — i.e. local development, or running both apps together on
  one host.
- HUB_MODE=remote — an authenticated HTTPS POST to the hub's
  /webhook/website-lead endpoint (ops-hub/app/webhook.py). Use this once
  the website is deployed somewhere other than the hub's own machine (e.g.
  Render) — see docs/website_deployment.md for the full setup (the hub
  stays running locally/on your own machine as it already does, exposed
  only via Tailscale Funnel, not a direct network-level connection).

Either way, the caller (routes.py) gets one function —
create_website_lead_with_draft() — that creates the lead AND attaches the
drafted reply in one call, so the two modes produce identical-looking lead
records in the hub.
"""
import os
import sys
from pathlib import Path

from . import draft_email

HUB_ROOT = Path(__file__).resolve().parent.parent.parent / "ops-hub"


def _mode():
    return os.environ.get("HUB_MODE", "local").strip().lower()


def _draft_for(service_slug, name, message=None):
    if service_slug:
        return draft_email.draft_for_service(service_slug, name)
    return draft_email.draft_general(name, message)


def _create_local(*, name, email, phone, message, business_line, next_action):
    if str(HUB_ROOT) not in sys.path:
        sys.path.insert(0, str(HUB_ROOT))
    from app.models import create_lead, get_lead, update_lead  # noqa: E402

    lead_id = create_lead(
        {
            "name": name,
            "business_line": business_line,
            "status": "New",
            "next_action": next_action,
            "notes": message,
            "contact_name": name,
            "contact_phone": phone or None,
            "contact_email": email,
            "source": "website",
            "done_summary": "Submitted via the website contact form.",
            "left_for_you_summary": "Review the drafted email reply and send it (or edit first).",
        }
    )
    return lead_id, get_lead, update_lead


def _attach_draft_local(lead_id, draft, get_lead, update_lead):
    lead = get_lead(lead_id)
    if not lead:
        return
    draft_block = f"\n\n---\nDRAFTED REPLY (review before sending)\nSubject: {draft['subject']}\n\n{draft['body']}"
    data = {k: lead.get(k) for k in (
        "name", "business_line", "status", "next_action", "deadline", "estimated_value",
        "contact_name", "contact_phone", "contact_email", "au_state",
        "task_type", "time_estimate_hours", "done_summary", "left_for_you_summary", "source_url",
    )}
    data["extra"] = lead.get("extra") or {}
    data["notes"] = (lead.get("notes") or "") + draft_block
    update_lead(lead_id, data)


def _create_remote(*, name, email, phone, message, business_line, next_action, draft):
    import requests

    url = os.environ.get("HUB_WEBHOOK_URL")
    secret = os.environ.get("HUB_WEBHOOK_SECRET")
    if not url or not secret:
        raise RuntimeError(
            "HUB_MODE=remote requires HUB_WEBHOOK_URL and HUB_WEBHOOK_SECRET to be set "
            "(see docs/website_deployment.md)."
        )
    resp = requests.post(
        url.rstrip("/") + "/webhook/website-lead",
        headers={"X-Website-Secret": secret, "Content-Type": "application/json"},
        json={
            "name": name,
            "email": email,
            "phone": phone,
            "message": message,
            "business_line": business_line,
            "next_action": next_action,
            "draft_subject": draft["subject"],
            "draft_body": draft["body"],
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()["lead_id"]


def create_website_lead_with_draft(*, name, email, phone, message, business_line, service_slug=None, service_name=None):
    """Create a lead (tagged to the right business line) and attach a
    template-based drafted reply to it, in one call, in whichever mode
    HUB_MODE selects. Returns the new lead_id."""
    next_action = f"Respond re: {service_name} enquiry" if service_name else "Respond to website enquiry"
    draft = _draft_for(service_slug, name, message)

    if _mode() == "remote":
        return _create_remote(
            name=name, email=email, phone=phone, message=message,
            business_line=business_line, next_action=next_action, draft=draft,
        )

    lead_id, get_lead, update_lead = _create_local(
        name=name, email=email, phone=phone, message=message,
        business_line=business_line, next_action=next_action,
    )
    _attach_draft_local(lead_id, draft, get_lead, update_lead)
    return lead_id
