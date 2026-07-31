#!/usr/bin/env bash
# Double-click launcher for the ops hub — starts the server if it isn't
# already running, then opens it in the default browser. Safe to run
# repeatedly (won't spawn a second server if one's already up).
set -uo pipefail
cd "$(dirname "$0")"

PW_FILE=".hub_password"
if [ ! -f "$PW_FILE" ]; then
  python3 -c "import secrets; print(secrets.token_urlsafe(12))" > "$PW_FILE"
  chmod 600 "$PW_FILE"
fi
export HUB_PASSWORD
HUB_PASSWORD="$(cat "$PW_FILE")"

TAILSCALE_IP=""
if command -v tailscale >/dev/null 2>&1; then
  TAILSCALE_IP="$(tailscale ip -4 2>/dev/null || true)"
fi

# Reuse whichever address is already serving, if any.
RUNNING_URL=""
for candidate in "$TAILSCALE_IP" "127.0.0.1"; do
  [ -z "$candidate" ] && continue
  if curl -s -o /dev/null -m 1 "http://${candidate}:5000/"; then
    RUNNING_URL="http://${candidate}:5000/"
    break
  fi
done

if [ -z "$RUNNING_URL" ]; then
  export HUB_HOST="${TAILSCALE_IP:-127.0.0.1}"
  setsid nohup python3 run.py >> hub.log 2>&1 < /dev/null &
  URL="http://${HUB_HOST}:5000/"
  for _ in $(seq 1 30); do
    curl -s -o /dev/null -m 1 "$URL" && { RUNNING_URL="$URL"; break; }
    sleep 0.3
  done
fi

if [ -z "$RUNNING_URL" ]; then
  echo "Hub didn't come up — check hub.log" >&2
  exit 1
fi

xdg-open "$RUNNING_URL" >/dev/null 2>&1 &
