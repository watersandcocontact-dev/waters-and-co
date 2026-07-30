from flask import Blueprint, abort, redirect, render_template, request, url_for

from . import draft_email
from .config import SEGMENTS, SERVICES, segment_by_slug, service_by_slug, services_in_segment
from .hub_bridge import create_website_lead

bp = Blueprint("main", __name__)


@bp.route("/")
def landing():
    return render_template("landing.html", segments=SEGMENTS)


@bp.route("/segment/<slug>")
def segment(slug):
    seg = segment_by_slug(slug)
    if not seg:
        abort(404)
    return render_template("segment.html", segment=seg, services=services_in_segment(slug))


@bp.route("/service/<slug>")
def service(slug):
    svc = service_by_slug(slug)
    if not svc:
        abort(404)
    return render_template("service.html", service=svc, slug=slug)


@bp.route("/service/<slug>/contact", methods=["POST"])
def service_contact(slug):
    svc = service_by_slug(slug)
    if not svc:
        abort(404)

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "service.html", service=svc, slug=slug, error="Name, email, and a message are required."
        )

    lead_id = create_website_lead(
        name=name,
        email=email,
        phone=phone,
        message=message,
        business_line=svc["business_line"],
        service_name=svc["name"],
    )
    draft = draft_email.draft_for_service(slug, name)
    _attach_draft(lead_id, draft)

    return redirect(url_for("main.thanks"))


@bp.route("/enquire", methods=["GET", "POST"])
def enquire():
    if request.method == "GET":
        return render_template("enquire.html")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template("enquire.html", error="Name, email, and a message are required.")

    lead_id = create_website_lead(
        name=name,
        email=email,
        phone=phone,
        message=message,
        business_line="GeneralEnquiry",
    )
    draft = draft_email.draft_general(name, message)
    _attach_draft(lead_id, draft)

    return redirect(url_for("main.thanks"))


@bp.route("/thanks")
def thanks():
    return render_template("thanks.html")


def _attach_draft(lead_id, draft):
    """Append the drafted reply to the lead's notes so it's visible right on
    the case detail page in the hub — no schema change needed.

    update_lead() overwrites every column from `data`, so this must round-trip
    every field the lead already has (not just the ones this function cares
    about) or it silently nulls out everything else on the row."""
    from .hub_bridge import HUB_ROOT  # noqa: F401 — ensures sys.path is set

    from app.models import get_lead, update_lead

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
