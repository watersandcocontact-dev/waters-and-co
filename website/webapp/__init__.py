from pathlib import Path

from flask import Flask

ROOT = Path(__file__).resolve().parent.parent


def create_app():
    app = Flask(
        __name__,
        template_folder=str(ROOT / "templates"),
        static_folder=str(ROOT / "static"),
    )

    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
