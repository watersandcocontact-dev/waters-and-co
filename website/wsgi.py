"""Gunicorn entrypoint for production (Render). Local dev keeps using
`python3 run.py` — this file is only what Render's start command targets.

    gunicorn wsgi:app
"""
from webapp import create_app

app = create_app()
