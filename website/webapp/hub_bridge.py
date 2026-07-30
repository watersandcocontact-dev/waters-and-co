"""Bridge into the ops hub's lead database — the website writes leads
directly via the hub's own models.create_lead(), the same "file" every
other business line already writes to. No HTTP call, no webhook gate:
just a direct Python import of the hub's package, since both apps run on
the same machine and share the same SQLite file.
"""
import sys
from pathlib import Path

HUB_ROOT = Path(__file__).resolve().parent.parent.parent / "ops-hub"
if str(HUB_ROOT) not in sys.path:
    sys.path.insert(0, str(HUB_ROOT))

from app.models import create_lead  # noqa: E402


def create_website_lead(*, name, email, phone, message, business_line, service_name=None):
    next_action = "Respond to website enquiry"
    if service_name:
        next_action = f"Respond re: {service_name} enquiry"

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
    return lead_id
