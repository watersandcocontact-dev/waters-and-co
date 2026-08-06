import secrets
from pathlib import Path

from flask import Flask

from .db import init_db

ROOT = Path(__file__).resolve().parent.parent
SECRET_KEY_PATH = ROOT / "data" / "secret_key.txt"


def _load_or_create_secret_key():
    SECRET_KEY_PATH.parent.mkdir(parents=True, exist_ok=True)
    if SECRET_KEY_PATH.exists():
        return SECRET_KEY_PATH.read_text().strip()
    key = secrets.token_hex(32)
    SECRET_KEY_PATH.write_text(key)
    return key


def create_app():
    app = Flask(
        __name__,
        template_folder=str(ROOT / "templates"),
        static_folder=str(ROOT / "static"),
    )
    app.secret_key = _load_or_create_secret_key()
    # Defense-in-depth against CSRF on the session cookie: browsers won't
    # attach a Lax cookie to a cross-site POST, which covers every
    # state-changing form in this app (delete_lead, payments, referral
    # bonuses, etc.) without needing per-form CSRF tokens. Not forcing
    # SESSION_COOKIE_SECURE here since the hub is sometimes reached through
    # a reverse proxy (Tailscale Funnel) that terminates HTTPS upstream of
    # this process -- forcing it blind could silently break login there.
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    init_db()

    from .auth import bp as auth_bp
    from .auth import init_auth
    from .payments import bp as payments_bp
    from .routes import bp as main_bp
    from .sms import bp as sms_bp
    from .webhook import bp as webhook_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(sms_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(auth_bp)
    init_auth(app)

    return app
