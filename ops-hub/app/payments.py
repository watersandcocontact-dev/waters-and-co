"""Stripe Payments — create per-lead payment requests (Checkout Sessions)
and receive the webhook that confirms them as paid.

Setup (see ops-hub/README.md for the full walkthrough):
  export STRIPE_SECRET_KEY="rk_live_... or sk_test_..."
  export STRIPE_WEBHOOK_SECRET="whsec_..."
  python3 run.py

Until STRIPE_SECRET_KEY is set, "Request payment" on a lead just explains
what to set — same inactive-until-configured pattern as app/webhook.py's
intake webhook.

Payment status only ever moves pending -> paid/expired/canceled via the
webhook below, never from the create route or the success_url redirect —
that's what stops someone marking themselves paid without Stripe actually
confirming the charge.
"""

import os
import secrets
import string

import stripe
from flask import Blueprint, jsonify, redirect, request, url_for

from . import models

bp = Blueprint("payments", __name__)


def _configured():
    return bool(os.environ.get("STRIPE_SECRET_KEY"))


def _integration_tag():
    suffix = "".join(secrets.choice(string.ascii_letters) for _ in range(8))
    return f"opshub_payment_{suffix}"


@bp.route("/leads/<int:lead_id>/payments/create", methods=["POST"])
def create_payment(lead_id):
    lead = models.get_lead(lead_id)
    if lead is None:
        return "Lead not found", 404

    if not _configured():
        return redirect(
            url_for(
                "main.lead_detail",
                lead_id=lead_id,
                payment_error="Stripe isn't set up yet — set STRIPE_SECRET_KEY (see ops-hub/README.md).",
            )
        )

    try:
        amount_dollars = float(request.form.get("amount") or 0)
    except ValueError:
        amount_dollars = 0
    if amount_dollars <= 0:
        return redirect(
            url_for("main.lead_detail", lead_id=lead_id, payment_error="Enter an amount greater than $0.")
        )

    description = (request.form.get("description") or "").strip() or lead["name"]
    amount_cents = round(amount_dollars * 100)

    stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
    try:
        session = stripe.checkout.Session.create(
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "aud",
                        "unit_amount": amount_cents,
                        "product_data": {"name": description},
                    },
                    "quantity": 1,
                }
            ],
            success_url=url_for("main.lead_detail", lead_id=lead_id, payment="success", _external=True),
            cancel_url=url_for("main.lead_detail", lead_id=lead_id, payment="cancelled", _external=True),
            metadata={"lead_id": str(lead_id)},
            integration_identifier=_integration_tag(),
        )
    except stripe.StripeError as e:
        return redirect(
            url_for("main.lead_detail", lead_id=lead_id, payment_error=f"Stripe error: {e.user_message or str(e)}")
        )

    models.create_payment(
        {
            "lead_id": lead_id,
            "checkout_session_id": session.id,
            "checkout_url": session.url,
            "amount_cents": amount_cents,
            "currency": "aud",
            "description": description,
        }
    )
    return redirect(url_for("main.lead_detail", lead_id=lead_id))


@bp.route("/webhook/stripe", methods=["POST"])
def stripe_webhook():
    payload = request.get_data()
    sig_header = request.headers.get("Stripe-Signature")
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET")

    if not webhook_secret:
        return jsonify({"status": "disabled", "message": "STRIPE_WEBHOOK_SECRET not set"}), 503

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except (ValueError, stripe.SignatureVerificationError):
        return jsonify({"status": "error", "message": "invalid signature"}), 400

    event_type = event["type"]
    obj = event["data"]["object"]

    if event_type == "checkout.session.completed":
        payment_intent = obj["payment_intent"] if "payment_intent" in obj else None
        models.mark_payment_paid(obj["id"], payment_intent)
    elif event_type == "checkout.session.expired":
        models.mark_payment_status(obj["id"], "expired")

    return jsonify({"status": "ok"}), 200
