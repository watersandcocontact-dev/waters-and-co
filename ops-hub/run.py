"""Entry point. Run with: python3 run.py
Dashboard opens at http://127.0.0.1:5000 by default.

For Tailscale/remote access, set HUB_HOST=1 (or any truthy value) so the
app binds ALL interfaces (0.0.0.0) instead of localhost-only:

    export HUB_HOST=1
    export HUB_PASSWORD="something-long-and-random"
    python3 run.py

REAL BUG FIXED 2026-08-07: this used to accept HUB_HOST=<a specific IP>
(e.g. the Tailscale IP from `tailscale ip -4`) and bind ONLY that one
address. That broke Tailscale Funnel silently: Funnel's own proxy target
is `localhost:5000`, which is a DIFFERENT address than the Tailscale IP --
binding to the Tailscale IP alone meant nothing was listening on
localhost, so every request Funnel tried to forward (including every real
website contact-form lead) got a 502 Bad Gateway with no visible error on
either the hub or website side. Binding 0.0.0.0 listens on localhost, the
Tailscale IP, and the LAN all at once, which is what Funnel/any reverse
proxy actually needs -- safe to do here since every route except the two
secret-protected webhooks still requires the HUB_PASSWORD session gate
(see app/auth.py), so this doesn't newly expose client data to the LAN.
"""
import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    host = "0.0.0.0" if os.environ.get("HUB_HOST") else "127.0.0.1"
    app.run(host=host, port=5000, debug=False)
