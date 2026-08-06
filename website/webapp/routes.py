from flask import Blueprint, abort, redirect, render_template, request, url_for

from .config import SEGMENTS, SERVICES, segment_by_slug, segment_groups, service_by_slug
from .hub_bridge import create_website_lead_with_draft

bp = Blueprint("main", __name__)


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

    create_website_lead_with_draft(
        name=name,
        email=email,
        phone=phone,
        message=message,
        business_line=svc["business_line"],
        service_slug=slug,
        service_name=svc["name"],
    )

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

    create_website_lead_with_draft(
        name=name,
        email=email,
        phone=phone,
        message=message,
        business_line="GeneralEnquiry",
    )

    return redirect(url_for("main.thanks"))


@bp.route("/thanks")
def thanks():
    return render_template("thanks.html")
