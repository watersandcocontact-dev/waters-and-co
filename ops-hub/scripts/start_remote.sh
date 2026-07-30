#!/usr/bin/env bash
# Zero-signup remote access: starts the hub + a Cloudflare "quick tunnel"
# (no Cloudflare account needed) and prints the public HTTPS URL.
#
# IMPORTANT CAVEATS — read before using this over a Tailscale-based setup:
# - The URL this prints is PUBLIC on the internet. Anyone who gets it can
#   reach your hub (client names/phones/emails/notes) until you close it.
# - The URL is EPHEMERAL — it changes every time you run this script, so
#   it's fine for "I need remote access right now tonight" but not for a
#   URL you'd bookmark on your phone permanently. For that, see
#   docs/remote_access.md and set up Tailscale instead (free, one signup,
#   private network instead of public internet — the safer long-term option).
# - This script REFUSES to start unless HUB_PASSWORD is set, so the login
#   wall (app/auth.py) is active before anything goes on the public internet.
#
# Usage:
#   export HUB_PASSWORD="something-long-and-random"
#   ./scripts/start_remote.sh

set -euo pipefail
cd "$(dirname "$0")/.."

if [ -z "${HUB_PASSWORD:-}" ]; then
  echo "ERROR: HUB_PASSWORD is not set. Refusing to expose the hub publicly with no login." >&2
  echo "Run:  export HUB_PASSWORD=\"something-long-and-random\"   then re-run this script." >&2
  exit 1
fi

if ! curl -s -o /dev/null http://127.0.0.1:5000/login; then
  echo "Starting the hub on 127.0.0.1:5000 ..."
  nohup python3 run.py > data/hub.log 2>&1 &
  sleep 2
fi

echo "Starting Cloudflare quick tunnel (no account needed, URL is temporary + public)..."
./bin/cloudflared tunnel --url http://127.0.0.1:5000 2>&1 | tee data/tunnel.log &
TUNNEL_PID=$!

for i in $(seq 1 15); do
  URL=$(grep -oE "https://[a-zA-Z0-9-]+\.trycloudflare\.com" data/tunnel.log | head -1 || true)
  if [ -n "$URL" ]; then
    echo ""
    echo "=================================================="
    echo "Public URL (temporary, changes on next restart):"
    echo "  $URL"
    echo "Login with the password you set in HUB_PASSWORD."
    echo "Press Ctrl+C to stop the tunnel."
    echo "=================================================="
    break
  fi
  sleep 1
done

wait "$TUNNEL_PID"
