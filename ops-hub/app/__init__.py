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
    init_db()

    from .auth import bp as auth_bp
    from .auth import init_auth
    from .payments import bp as payments_bp
    from .routes import bp as main_bp
    from .webhook import bp as webhook_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(webhook_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(auth_bp)
    init_auth(app)

    return app
