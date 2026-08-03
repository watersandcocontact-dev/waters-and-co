# Ops Hub

Self-contained local CRM/lead-tracker for all business lines (Wave 1 + Wave 2 prep).
Zero external accounts required — SQLite file on disk, Flask dev server, runs entirely
on this machine.

## Run it

```bash
cd ops-hub
python3 run.py
```

Open http://127.0.0.1:5000

The database is created automatically at `ops-hub/data/hub.sqlite3` on first run.

## What's here

- `app/config.py` — business lines, statuses, per-line extra fields, deadline thresholds
- `app/db.py` — SQLite schema (`leads`, `webhook_log`)
- `app/models.py` — CRUD + deadline-alert logic (incl. auto 60-day land-tax deadline)
- `app/routes.py` — dashboard, due-this-week, lead form (create/edit/delete)
- `app/webhook.py` — intake webhook receiver, **inactive until you set env vars**
- `app/payments.py` — Stripe payment requests per lead, **inactive until you set env vars**
- `templates/`, `static/` — UI

## Activating the phone-platform webhook (later, once you've signed up for one)

```bash
export INTAKE_WEBHOOK_ENABLED=1
export INTAKE_WEBHOOK_SECRET="choose-a-long-random-string"
python3 run.py
```

Point your AI phone platform's webhook at `POST http://<your-host>:5000/webhook/intake`
with header `X-Intake-Secret: <same secret>`. See `app/webhook.py` for the expected
JSON shape — adjust field names to match whatever platform you pick.

## Taking payments (Stripe)

Each lead's detail page has a **Payments** section: enter an amount (AUD) and a
description ("Deposit — 50%", "Final balance", etc.) and it creates a Stripe
Checkout link you copy/send to the client. A lead can have several payment
requests over its life — deposit now, balance later — each tracked separately
(pending until Stripe confirms the charge, then paid).

```bash
export STRIPE_SECRET_KEY="rk_live_..."      # restricted key, Payments scope only
export STRIPE_WEBHOOK_SECRET="whsec_..."    # from the Stripe Dashboard webhook endpoint
python3 run.py
```

1. Get a live restricted API key from the
   [Stripe Dashboard](https://dashboard.stripe.com/apikeys) → "Create restricted key" →
   grant it **write access to Checkout Sessions only** (least privilege — this key
   never needs to touch anything else). Don't use your full secret key (`sk_...`).
2. Add a webhook endpoint in the Dashboard pointing at
   `POST http://<your-host>:5000/webhook/stripe`, subscribed to
   `checkout.session.completed` (and optionally `checkout.session.expired`).
   Copy its signing secret into `STRIPE_WEBHOOK_SECRET` — this is what proves a
   "paid" update actually came from Stripe, not from someone hitting your
   success URL directly.
3. Test mode first: use a `sk_test_...`/`rk_test_...` key and
   [Stripe's test cards](https://docs.stripe.com/testing) before switching to live
   keys once you're happy.
4. Payment method types aren't hardcoded to cards only — Stripe shows whichever
   methods make sense for the amount/currency automatically. Manage which ones
   are enabled from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).
5. This does **not** collect GST/tax automatically (`automatic_tax` is off) —
   don't turn it on unless/until you're actually GST-registered (see the Tax
   Tracking dashboard's `gst_threshold_flag`). Turning it on without registration
   would mean Stripe silently collects $0 tax while implying it's handled.

## Notes

- No email notifications (would require a mail-account signup); deadline alerts are
  dashboard-only, shown as a banner at 14/60/30-day thresholds plus overdue.
- Dependencies: Flask, stripe, requests, and PyJWT, installed to the user
  site-packages with
  `python3 -m pip install --user --break-system-packages flask stripe requests pyjwt`
  (this machine's Debian/Ubuntu Python blocks plain global pip installs and
  `venv` needs a missing `python3-venv` apt package this session couldn't
  install without sudo). requests/PyJWT are for the httpSMS module
  (`app/sms.py`) -- see `docs/httpsms_setup.md`.
- Not hardened for the public internet — this is a local ops tool. If you ever expose
  it beyond localhost, put it behind auth first.
