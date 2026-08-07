import datetime
import json
from pathlib import Path

from flask import Blueprint, abort, redirect, render_template, request, url_for

from .config import SEGMENTS, SERVICES, segment_by_slug, segment_groups, service_by_slug
from .hub_bridge import HubUnreachableError, create_website_lead_with_draft

bp = Blueprint("main", __name__)

# Fallback capture for the rare case the hub genuinely can't be reached --
# a real submission must never just vanish with nothing for the Owner to
# see, the way it silently did before this file existed. This is a plain
# append-only local file (not the hub DB, since the hub is exactly what's
# unreachable) -- check it if a visitor says they got an error message.
FAILED_SUBMISSIONS_LOG = Path(__file__).resolve().parent.parent / "failed_submissions.log"
SUPPORT_FALLBACK_EMAIL = "watersandco.contact@gmail.com"


def _log_lost_submission(*, name, email, phone, message, business_line, error):
    entry = {
        "ts": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "name": name,
        "email": email,
        "phone": phone,
        "message": message,
        "business_line": business_line,
        "error": str(error),
    }
    try:
        with FAILED_SUBMISSIONS_LOG.open("a") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError:
        # Even the fallback log failed (disk full, permissions, etc.) --
        # nothing more we can do server-side; the visitor-facing error
        # message is still the honest fallback (email us directly).
        pass


ERROR_MESSAGE = (
    "Something went wrong sending that through -- your message wasn't lost, "
    f"but to be safe, please email {SUPPORT_FALLBACK_EMAIL} directly and we'll "
    "get back to you."
)


@bp.route("/")
def landing():
    return render_template("landing.html", segments=SEGMENTS)


@bp.route("/segment/<slug>")
def segment(slug):
    seg = segment_by_slug(slug)
    if not seg:
        abort(404)
    return render_template("segment.html", segment=seg, groups=segment_groups(slug))


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

    try:
        create_website_lead_with_draft(
            name=name,
            email=email,
            phone=phone,
            message=message,
            business_line=svc["business_line"],
            service_slug=slug,
            service_name=svc["name"],
        )
    except HubUnreachableError as exc:
        _log_lost_submission(
            name=name, email=email, phone=phone, message=message,
            business_line=svc["business_line"], error=exc,
        )
        return render_template("service.html", service=svc, slug=slug, error=ERROR_MESSAGE), 502

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

    try:
        create_website_lead_with_draft(
            name=name,
            email=email,
            phone=phone,
            message=message,
            business_line="GeneralEnquiry",
        )
    except HubUnreachableError as exc:
        _log_lost_submission(
            name=name, email=email, phone=phone, message=message,
            business_line="GeneralEnquiry", error=exc,
        )
        return render_template("enquire.html", error=ERROR_MESSAGE), 502

    return redirect(url_for("main.thanks"))


@bp.route("/thanks")
def thanks():
    return render_template("thanks.html")
