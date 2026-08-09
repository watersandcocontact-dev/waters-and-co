#!/usr/bin/env bash
# Watchdog: catches the exact failure mode from 2026-08-09/10 -- ops-hub's
# process died silently, which meant every real contact-form lead on
# watersandco.info was failing (Funnel proxies to localhost:5000, nothing
# was listening, visitors got a 502/graceful-error page). Nobody noticed
# until the next session manually checked before a launch.
#
# What this checks, every run:
#   1. Is the hub actually responding on 127.0.0.1:5000? (not just "is a
#      process running" -- a hung process that's not accepting connections
#      would pass a ps-based check and still be broken)
#   2. Is Tailscale Funnel still proxying the two webhook routes it should?
# If either check fails: attempt self-heal via launch_hub.sh (the same
# launcher a human would run), then log the outcome either way.
#
# Deliberately does NOT hit the live watersandco.info /enquire endpoint on
# every run -- that would create a real test lead in the database every
# 5 minutes. Use pre_send_check.sh for the real end-to-end test, run that
# manually before something time-sensitive (like a launch).
#
# Setup (one-time): add to crontab --
#   */5 * * * * "/home/m/claude code/business app/ops-hub/scripts/watchdog.sh" >> "/home/m/claude code/business app/ops-hub/data/watchdog.log" 2>&1
#   @reboot sleep 60 && "/home/m/claude code/business app/ops-hub/scripts/watchdog.sh" >> "/home/m/claude code/business app/ops-hub/data/watchdog.log" 2>&1

set -uo pipefail
cd "$(dirname "$0")/.."
LOGDIR="data"
mkdir -p "$LOGDIR"
ALERT_FILE="$LOGDIR/watchdog_alert.txt"
TS="$(date '+%Y-%m-%d %H:%M:%S %Z')"

hub_ok() {
  curl -s -o /dev/null -m 5 -w "%{http_code}" "http://127.0.0.1:5000/login" 2>/dev/null | grep -q "^200$"
}

funnel_ok() {
  command -v tailscale >/dev/null 2>&1 || return 1
  local status
  status="$(tailscale funnel status 2>&1)"
  echo "$status" | grep -q "webhook/website-lead"
}

PROBLEMS=()

if hub_ok; then
  echo "[$TS] hub: OK"
else
  echo "[$TS] hub: DOWN -- attempting restart via launch_hub.sh"
  ./launch_hub.sh >/dev/null 2>&1 &
  sleep 8
  if hub_ok; then
    echo "[$TS] hub: RECOVERED after restart"
  else
    echo "[$TS] hub: STILL DOWN after restart attempt"
    PROBLEMS+=("ops-hub is not responding on 127.0.0.1:5000, even after an automatic restart attempt. Check ops-hub/hub.log directly.")
  fi
fi

if funnel_ok; then
  echo "[$TS] funnel: OK"
else
  echo "[$TS] funnel: NOT proxying /webhook/website-lead -- this needs a human (Tailscale Funnel config, not something this script can fix)"
  PROBLEMS+=("Tailscale Funnel is not proxying /webhook/website-lead. Real leads on watersandco.info will fail even though the hub itself may be fine. Needs manual check: 'tailscale funnel status'.")
fi

if [ "${#PROBLEMS[@]}" -gt 0 ]; then
  {
    echo "WATCHDOG ALERT -- $TS"
    echo ""
    printf '%s\n\n' "${PROBLEMS[@]}"
    echo "This file is overwritten each run problems persist; deleted automatically once everything checks out clean again."
  } > "$ALERT_FILE"
else
  rm -f "$ALERT_FILE"
fi
