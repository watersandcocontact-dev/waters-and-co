"""Public marketing site. Run with: python3 run.py
Opens at http://127.0.0.1:5050 by default (separate port from the internal
ops hub, which runs on 5000 — the two are meant to run side by side).
"""
import os

from webapp import create_app

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("SITE_HOST", "127.0.0.1")
    port = int(os.environ.get("SITE_PORT", "5050"))
    app.run(host=host, port=port, debug=False)
