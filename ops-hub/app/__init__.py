from pathlib import Path

from flask import Flask

from .db import init_db

ROOT = Path(__file__).resolve().parent.parent


def create_app():
    app = Flask(
        __name__,
        template_folder=str(ROOT / "templates"),
        static_folder=str(ROOT / "static"),
    )
    init_db()

    from .routes import bp as main_bp
    from .webhook import bp as webhook_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(webhook_bp)

    return app
