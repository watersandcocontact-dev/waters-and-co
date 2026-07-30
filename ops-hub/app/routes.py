from flask import Blueprint, redirect, render_template, request, url_for

from . import models
from .config import AU_STATES, BUSINESS_LINES, EXTRA_FIELDS, STATUSES

bp = Blueprint("main", __name__)


@bp.app_template_filter("line_label")
def line_label(key):
    return dict(BUSINESS_LINES).get(key, key)


@bp.route("/")
def dashboard():
    business_line = request.args.get("business_line") or None
    status = request.args.get("status") or None
    order_by = request.args.get("order_by") or "deadline"

    leads = models.list_leads(business_line=business_line, status=status, order_by=order_by)
    alerts = models.deadline_alert_buckets()
    counts = models.counts_by_line()

    return render_template(
        "dashboard.html",
        leads=leads,
        alerts=alerts,
        counts=counts,
        business_lines=BUSINESS_LINES,
        statuses=STATUSES,
        selected_line=business_line,
        selected_status=status,
        order_by=order_by,
    )


@bp.route("/due-this-week")
def due_this_week():
    leads = models.due_within(7)
    return render_template("due_this_week.html", leads=leads)


@bp.route("/leads/new", methods=["GET", "POST"])
def new_lead():
    if request.method == "POST":
        data = _form_to_data(request.form)
        lead_id = models.create_lead(data)
        return redirect(url_for("main.lead_detail", lead_id=lead_id))
    return render_template(
        "lead_form.html",
        lead=None,
        business_lines=BUSINESS_LINES,
        statuses=STATUSES,
        au_states=AU_STATES,
        extra_fields=EXTRA_FIELDS,
        selected_line=request.args.get("business_line") or BUSINESS_LINES[0][0],
    )


@bp.route("/leads/<int:lead_id>", methods=["GET", "POST"])
def lead_detail(lead_id):
    lead = models.get_lead(lead_id)
    if lead is None:
        return "Lead not found", 404
    if request.method == "POST":
        data = _form_to_data(request.form)
        models.update_lead(lead_id, data)
        return redirect(url_for("main.lead_detail", lead_id=lead_id))
    return render_template(
        "lead_form.html",
        lead=lead,
        business_lines=BUSINESS_LINES,
        statuses=STATUSES,
        au_states=AU_STATES,
        extra_fields=EXTRA_FIELDS,
        selected_line=lead["business_line"],
    )


@bp.route("/leads/<int:lead_id>/delete", methods=["POST"])
def delete_lead(lead_id):
    models.delete_lead(lead_id)
    return redirect(url_for("main.dashboard"))


def _form_to_data(form):
    business_line = form.get("business_line")
    extra_field_defs = EXTRA_FIELDS.get(business_line, [])
    extra = {key: form.get(f"extra__{key}", "") for key, _ in extra_field_defs}
    return {
        "name": form.get("name", "").strip(),
        "business_line": business_line,
        "status": form.get("status"),
        "next_action": form.get("next_action"),
        "deadline": form.get("deadline") or None,
        "estimated_value": form.get("estimated_value") or None,
        "notes": form.get("notes"),
        "contact_name": form.get("contact_name"),
        "contact_phone": form.get("contact_phone"),
        "contact_email": form.get("contact_email"),
        "au_state": form.get("au_state") or None,
        "extra": extra,
    }
