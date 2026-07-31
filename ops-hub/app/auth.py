"""Minimal password gate for remote access.

The hub has no login by default (fine for localhost-only use). The moment
you expose it beyond your own machine (Tailscale, a tunnel, anything), set
the HUB_PASSWORD environment variable before starting the app — every route
except the login page and the Twilio-style webhook (which has its own
shared-secret check, see webhook.py) then requires a session login first.

This is intentionally simple (one shared password, no user accounts) — it's
a personal single-operator tool, not a multi-user system. If HUB_PASSWORD is
not set, auth is skipped entirely (today's default, unchanged).
"""

import os
from functools import wraps

from flask import Blueprint, redirect, render_template_string, request, session, url_for

bp = Blueprint("auth", __name__)

LOGIN_TEMPLATE = """
<!doctype html><html><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>Sign in — Ops Hub</title>
<link rel="stylesheet" href="/static/style.css"></head>
<body style="display:flex; min-height:100vh; align-items:center; justify-content:center; background:var(--bg);">
<main style="max-width:360px; width:100%; padding:0 20px;">
<h1 style="text-align:center; margin-bottom:24px;">Waters <em>&amp;</em> Co <span class="tag">Ops Hub</span></h1>
{% if error %}<p style="color:var(--red); text-align:center;">{{ error }}</p>{% endif %}
<form method="post" class="lead-form">
  <label>Password</label>
  <input type="password" name="password" autofocus>
  <div class="actions"><button class="btn" type="submit">Sign in</button></div>
</form>
</main></body></html>
"""


def _password_required():
    return bool(os.environ.get("HUB_PASSWORD"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    if not _password_required():
        return redirect(url_for("main.daily_queue"))
    error = None
    if request.method == "POST":
        if request.form.get("password") == os.environ.get("HUB_PASSWORD"):
            session["authed"] = True
            return redirect(request.args.get("next") or url_for("main.daily_queue"))
        error = "Wrong password."
    return render_template_string(LOGIN_TEMPLATE, error=error)


@bp.route("/logout", methods=["POST"])
def logout():
    session.pop("authed", None)
    return redirect(url_for("auth.login"))


def init_auth(app):
    @app.before_request
    def require_login():
        if not _password_required():
            return None
        exempt = {"auth.login", "static", "webhook.intake", "payments.stripe_webhook"}
        if request.endpoint in exempt or request.endpoint is None:
            return None
        if not session.get("authed"):
            return redirect(url_for("auth.login", next=request.path))
        return None
