"""Template-based draft-reply generator.

Deterministic, not an AI call — no API key/account needed, costs nothing to
run. Produces a ready-to-edit email referencing the specific service and
real pricing. Stored on the lead for a human (you, or Claude in a session)
to review and actually send — nothing here sends anything.
"""
from .config import SERVICES


def _pricing_lines(service):
    return "\n".join(f"- {p['label']}: {p['price']}" for p in service["pricing"])


def draft_for_service(service_slug, name):
    service = SERVICES.get(service_slug)
    first_name = (name or "there").split(" ")[0]
    if not service:
        return draft_general(name)

    subject = f"Re: your enquiry about {service['name']}"
    body = f"""Hi {first_name},

Thanks for reaching out about {service['name'].lower()}.

{service['summary']}

Current pricing:
{_pricing_lines(service)}

Happy to answer any questions or get started whenever suits — just reply
to this email.

[Your name]
Waters & Co
"""
    return {"subject": subject, "body": body}


def draft_general(name, message=None):
    first_name = (name or "there").split(" ")[0]
    subject = "Re: your enquiry"
    body = f"""Hi {first_name},

Thanks for getting in touch. I'll take a look at what you've described{
' below' if message else ''} and come back to you shortly with whether
this is something we can help with, and what that would look like.

[Your name]
Waters & Co
"""
    return {"subject": subject, "body": body}
