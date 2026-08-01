from flask import Blueprint, redirect, render_template, request, url_for

from . import models
from .config import (
    AU_STATES,
    BUDGET_PHASE,
    BUSINESS_LINES,
    EVALUATION_WINDOWS_WEEKS,
    EXPENSE_CATEGORIES,
    EXTRA_FIELDS,
    STATUSES,
    TASK_TYPE_LABELS,
    TASK_TYPE_LINES,
    TAX_FIGURES,
    WEEKLY_BUDGET_RANGE,
)

bp = Blueprint("main", __name__)


@bp.app_template_filter("line_label")
def line_label(key):
    return dict(BUSINESS_LINES).get(key, key)


@bp.app_template_filter("money")
def money(value):
    if value is None:
        return "—"
    return f"${value:,.0f}"


@bp.route("/")
def daily_queue():
    """The hub's primary view: today's open, actionable work across every
    business line, sorted highest $/hr first — no other sort order."""
    leads = models.daily_queue()
    alerts = models.deadline_alert_buckets()
    return render_template("daily_queue.html", leads=leads, alerts=alerts)


@bp.route("/all")
def all_leads():
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


@bp.route("/lines")
def lines_index():
    counts = models.counts_by_line()
    return render_template("lines_index.html", business_lines=BUSINESS_LINES, counts=counts)


@bp.route("/line/<key>")
def line_view(key):
    """One business line at a time — kept clearly separated per line rather
    than a single blurred case list, per your guided-mode instruction."""
    valid_keys = dict(BUSINESS_LINES)
    if key not in valid_keys:
        return "Unknown business line", 404
    status = request.args.get("status") or None
    leads = models.list_leads(business_line=key, status=status, order_by="rate")
    return render_template(
        "line_view.html",
        line_key=key,
        line_label=valid_keys[key],
        leads=leads,
        statuses=STATUSES,
        selected_status=status,
        business_lines=BUSINESS_LINES,
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
        task_type_lines=TASK_TYPE_LINES,
        task_type_labels=TASK_TYPE_LABELS,
        selected_line=request.args.get("business_line") or BUSINESS_LINES[0][0],
        all_leads=models.list_leads_basic(),
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
    time_entries = models.get_time_entries(lead_id)
    payments = models.list_payments_for_lead(lead_id)
    return render_template(
        "lead_form.html",
        lead=lead,
        business_lines=BUSINESS_LINES,
        statuses=STATUSES,
        au_states=AU_STATES,
        extra_fields=EXTRA_FIELDS,
        task_type_lines=TASK_TYPE_LINES,
        task_type_labels=TASK_TYPE_LABELS,
        selected_line=lead["business_line"],
        time_entries=time_entries,
        payments=payments,
        payment_error=request.args.get("payment_error"),
        payment_result=request.args.get("payment"),
        all_leads=[l for l in models.list_leads_basic() if l["id"] != lead_id],
        referral=models.referral_summary(lead_id),
    )


@bp.route("/leads/<int:lead_id>/delete", methods=["POST"])
def delete_lead(lead_id):
    models.delete_lead(lead_id)
    return redirect(url_for("main.daily_queue"))


@bp.route("/leads/<int:lead_id>/log-time", methods=["POST"])
def log_time(lead_id):
    hours = request.form.get("hours")
    note = request.form.get("note")
    if hours:
        try:
            models.log_time(lead_id, float(hours), note)
        except ValueError:
            pass
    return redirect(url_for("main.lead_detail", lead_id=lead_id))


@bp.route("/expansion", methods=["GET", "POST"])
def expansion():
    if request.method == "POST":
        models.create_spend(
            {
                "spend_date": request.form.get("spend_date"),
                "business_line": request.form.get("business_line") or None,
                "spend_type": request.form.get("spend_type"),
                "campaign_tag": request.form.get("campaign_tag"),
                "amount": float(request.form.get("amount") or 0),
                "funded_by": request.form.get("funded_by"),
                "notes": request.form.get("notes"),
            }
        )
        return redirect(url_for("main.expansion"))

    report = models.spend_report()
    return render_template(
        "expansion.html",
        spends=report["spends"],
        best_line=report["best_performing_line"],
        business_lines=BUSINESS_LINES,
        budget_phase=BUDGET_PHASE,
        weekly_budget_range=WEEKLY_BUDGET_RANGE,
        evaluation_windows=EVALUATION_WINDOWS_WEEKS,
    )


@bp.route("/expansion/<int:spend_id>/outcome", methods=["POST"])
def spend_outcome(spend_id):
    leads = int(request.form.get("outcome_leads") or 0)
    revenue = float(request.form.get("outcome_revenue") or 0)
    status = request.form.get("status") or None
    models.update_spend_outcome(spend_id, leads, revenue, status)
    return redirect(url_for("main.expansion"))


@bp.route("/referrals")
def referrals_dashboard():
    return render_template("referrals.html", data=models.referral_dashboard())


@bp.route("/referral-bonuses/<int:bonus_id>/apply", methods=["POST"])
def apply_referral_bonus(bonus_id):
    referrer_lead_id = models.mark_bonus_applied(bonus_id)
    if referrer_lead_id is None:
        return "Bonus not found", 404
    return redirect(url_for("main.lead_detail", lead_id=referrer_lead_id))


@bp.route("/tax", methods=["GET"])
def tax_dashboard():
    return render_template(
        "tax.html",
        position=models.combined_tax_position(),
        caps=models.no_receipt_cap_usage(),
        comparison=models.day_job_vs_business_comparison(),
        pay_periods=models.list_pay_periods(),
        day_job_expenses=models.list_expenses(context="day_job"),
        business_expenses=[e for e in models.list_expenses() if e["context"] != "day_job"],
        business_lines=BUSINESS_LINES,
        expense_categories=EXPENSE_CATEGORIES,
        tax_figures=TAX_FIGURES,
    )


@bp.route("/tax/pay-period", methods=["POST"])
def tax_pay_period():
    models.create_pay_period(
        {
            "pay_date": request.form.get("pay_date"),
            "gross": float(request.form.get("gross") or 0),
            "tax_withheld": float(request.form.get("tax_withheld") or 0),
            "net": float(request.form.get("net") or 0),
            "super_amount": float(request.form.get("super_amount")) if request.form.get("super_amount") else None,
            "hours_worked": float(request.form.get("hours_worked")) if request.form.get("hours_worked") else None,
            "notes": request.form.get("notes"),
        }
    )
    return redirect(url_for("main.tax_dashboard"))


@bp.route("/tax/expense", methods=["POST"])
def tax_expense():
    models.create_expense(
        {
            "expense_date": request.form.get("expense_date"),
            "context": request.form.get("context"),
            "category": request.form.get("category"),
            "amount": float(request.form.get("amount") or 0),
            "description": request.form.get("description"),
            "receipt_held": request.form.get("receipt_held"),
            "no_receipt_bucket": request.form.get("no_receipt_bucket") or None,
            "deduction_treatment": request.form.get("deduction_treatment") or None,
            "km_count": float(request.form.get("km_count")) if request.form.get("km_count") else None,
            "hours_count": float(request.form.get("hours_count")) if request.form.get("hours_count") else None,
        }
    )
    return redirect(url_for("main.tax_dashboard"))


@bp.route("/tax/export")
def tax_export():
    return render_template("tax_export.html", data=models.accountant_export_data(), tax_figures=TAX_FIGURES)


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
        "task_type": form.get("task_type") or None,
        "time_estimate_hours": form.get("time_estimate_hours") or None,
        "done_summary": form.get("done_summary"),
        "left_for_you_summary": form.get("left_for_you_summary"),
        "source_url": form.get("source_url"),
        "referred_by_lead_id": form.get("referred_by_lead_id") or None,
        "extra": extra,
    }
