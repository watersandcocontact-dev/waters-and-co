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

    @app.after_request
    def add_delivery_headers(response):
        """Cache immutable public assets and provide conservative browser
        protections without changing form or page behaviour."""
        if response.status_code == 200 and response.mimetype in {
            "text/css", "application/javascript", "font/woff2",
            "image/jpeg", "image/png", "image/x-icon",
        }:
            response.headers["Cache-Control"] = "public, max-age=604800, stale-while-revalidate=86400"
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        return response

    return app
