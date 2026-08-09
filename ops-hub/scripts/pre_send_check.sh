#!/usr/bin/env bash
# Real end-to-end check: submits an actual test enquiry through the LIVE
# public site (not just localhost) and confirms it lands in the hub
# database. This is the test watchdog.sh deliberately does NOT run every
# 5 minutes (it would create a real lead each time) -- run this by hand
# before anything time-sensitive, e.g. right before a scheduled send.
#
# Usage: ./pre_send_check.sh [production-url, default https://watersandco.info]

set -uo pipefail
cd "$(dirname "$0")/.."
URL="${1:-https://watersandco.info}"
STAMP="$(date +%s)"
NAME="Pre-send Check ${STAMP}"
EMAIL="presend-check-${STAMP}@example.com"

echo "1. Local hub responding?"
if curl -s -o /dev/null -m 5 -w "   -> %{http_code}\n" "http://127.0.0.1:5000/login"; then :; else echo "   -> FAILED (no response)"; fi

echo "2. Tailscale Funnel proxying the webhook route?"
if command -v tailscale >/dev/null 2>&1 && tailscale funnel status 2>&1 | grep -q "webhook/website-lead"; then
  echo "   -> yes"
else
  echo "   -> NO -- fix this before relying on the site"
fi

echo "3. Live site homepage responding?"
curl -s -o /dev/null -m 10 -w "   -> %{http_code}\n" "${URL}/"

echo "4. Real end-to-end enquiry submission via ${URL}/enquire ..."
CODE=$(curl -s -m 15 -o /tmp/presend_check_body.html -w "%{http_code}" -X POST "${URL}/enquire" \
  -d "name=${NAME}" -d "email=${EMAIL}" -d "phone=" -d "interest=Not sure yet" \
  -d "message=Automated pre-send check - safe to delete" -d "website=")
LOCATION=$(curl -s -m 15 -D - -o /dev/null -X POST "${URL}/enquire" \
  -d "name=${NAME}b" -d "email=${EMAIL}.b" -d "phone=" -d "interest=Not sure yet" \
  -d "message=Automated pre-send check - safe to delete" -d "website=" | grep -i "^location" || true)
if echo "$LOCATION" | grep -q "/thanks"; then
  echo "   -> SUCCESS (redirected to /thanks)"
else
  echo "   -> FAILED -- got HTTP $CODE, no /thanks redirect. Check /tmp/presend_check_body.html for the error shown to a real visitor."
fi

echo ""
echo "5. Did the test lead actually land in the hub database?"
python3 - "$NAME" <<'PYEOF'
import sqlite3, sys
name = sys.argv[1]
con = sqlite3.connect("data/hub.sqlite3")
cur = con.cursor()
cur.execute("SELECT id, contact_email, created_at FROM leads WHERE contact_name = ? OR contact_name = ? ORDER BY id DESC", (name, name + "b"))
rows = cur.fetchall()
if rows:
    for r in rows:
        print(f"   -> FOUND lead id={r[0]} email={r[1]} created={r[2]}")
else:
    print("   -> NOT FOUND -- form said success but nothing landed in the database. Investigate before trusting the site.")
PYEOF

echo ""
echo "Done. Test leads above are safe to delete (not real prospects) -- not deleted automatically, per the no-delete-data rule."
