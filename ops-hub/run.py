"""Entry point. Run with: python3 run.py
Dashboard opens at http://127.0.0.1:5000 by default.

For Tailscale/remote access, set HUB_HOST to this machine's Tailscale IP
(find it with `tailscale ip -4`) so the app listens there specifically —
not on the whole LAN/internet, just the private Tailscale network:

    export HUB_HOST=$(tailscale ip -4)
    export HUB_PASSWORD="something-long-and-random"
    python3 run.py
"""
import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    host = os.environ.get("HUB_HOST", "127.0.0.1")
    app.run(host=host, port=5000, debug=False)
