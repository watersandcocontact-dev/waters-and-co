#!/usr/bin/env bash
# Daily opportunity scan — runs Claude Code non-interactively via your own
# cron, no approval dialog (that's the whole reason this exists instead of
# the in-app scheduled-tasks tool, which needs a one-time approval click
# the app can't get past unattended).
#
# --permission-mode acceptEdits: file writes/edits proceed without a prompt.
# --allowedTools restricts this run to read/write/search only — no Bash,
# so it can't run arbitrary commands even by mistake.
#
# Add this to your crontab yourself (never done automatically — see
# instructions below):
#   crontab -e
#   0 9 * * * /home/m/claude\ code/business\ app/wave3-unscoped/opportunity_scan/run_daily_scan.sh >> /home/m/claude\ code/business\ app/wave3-unscoped/opportunity_scan/scan.log 2>&1

set -euo pipefail
cd "$(dirname "$0")/../.."

PROMPT_FILE="wave3-unscoped/opportunity_scan/daily_scan_prompt.txt"

echo "=== Daily opportunity scan: $(date -Iseconds) ==="
claude -p "$(cat "$PROMPT_FILE")" \
  --permission-mode acceptEdits \
  --allowedTools "Read Write Edit Glob Grep WebSearch WebFetch" \
  --output-format text
echo "=== Done: $(date -Iseconds) ==="
