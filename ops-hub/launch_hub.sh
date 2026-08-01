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

# Stripe payments (optional) -- if you've set up .stripe_env (see
# README.md "Taking payments (Stripe)"), pick up the keys automatically so
# payment links + live webhook confirmation just work, no manual export.
STRIPE_ENV_FILE=".stripe_env"
if [ -f "$STRIPE_ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  source "$STRIPE_ENV_FILE"
  set +a
fi

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

# Stripe webhook listener -- only if a key is configured (via
# .stripe_env), and only one running instance at a time (pidfile, since
# matching "stripe listen" by process name alone isn't reliable across
# restarts). Forwards to whatever host:port the hub actually answered on
# above, so this works the same over Tailscale or localhost.
if [ -n "${STRIPE_SECRET_KEY:-}" ]; then
  if ! command -v stripe >/dev/null 2>&1; then
    for d in "$HOME/.nvm/versions/node"/*/bin; do
      [ -x "$d/stripe" ] && export PATH="$d:$PATH" && break
    done
  fi
  LISTEN_PIDFILE=".stripe_listen.pid"
  LISTEN_RUNNING=0
  if [ -f "$LISTEN_PIDFILE" ] && kill -0 "$(cat "$LISTEN_PIDFILE")" 2>/dev/null; then
    LISTEN_RUNNING=1
  fi
  if [ "$LISTEN_RUNNING" = 0 ] && command -v stripe >/dev/null 2>&1; then
    HOST_PORT="${RUNNING_URL#http://}"
    HOST_PORT="${HOST_PORT%/}"
    setsid nohup stripe listen --forward-to "${HOST_PORT}/webhook/stripe" \
      --api-key "$STRIPE_SECRET_KEY" >> stripe_listen.log 2>&1 < /dev/null &
    echo $! > "$LISTEN_PIDFILE"
  fi
fi

xdg-open "$RUNNING_URL" >/dev/null 2>&1 &
