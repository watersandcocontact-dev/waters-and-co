#!/usr/bin/env python3
"""Periodic monitoring — desktop notification, no cloud/signup required.

Why this exists instead of a scheduled cloud agent: cloud-scheduled routines
run in Anthropic's cloud and cannot reach a locally-running app or its
database at all — they'd need the hub permanently, publicly hosted, which
contradicts the self-hosted/zero-signup setup. This script is the reliable
local equivalent: it runs on this machine (via cron, see below), diffs
against the last check, and surfaces new/changed cases in the same
what/why + done-vs-left-for-you format you'd want from an assistant checking
in on you — pulled straight from each lead's own `done_summary` /
`left_for_you_summary` / `source_url` fields rather than generated fresh
each time, so it's fast and doesn't need an AI call to run.

Run manually:
    python3 scripts/new_case_check.py

Or add to crontab for an hourly check:
    crontab -e
    # then add:
    5 * * * * cd "/home/m/claude code/business app/ops-hub" && /usr/bin/python3 scripts/new_case_check.py

For the terse "what/why + done-vs-left" narration when you're actually in a
Claude Code session, just ask — reading the hub and giving you that
breakdown directly is more thorough than a templated notification and
doesn't need this script at all. This script is for when no session is open.
"""
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.models import new_or_updated_since  # noqa: E402

STATE_FILE = ROOT / "data" / "last_check.txt"


def notify(title, message, urgency="normal"):
    try:
        subprocess.run(["notify-send", "-u", urgency, title, message], check=False)
    except FileNotFoundError:
        print(f"[notify-send not available] {title}: {message}")


def main():
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    last_check = STATE_FILE.read_text().strip() if STATE_FILE.exists() else "1970-01-01 00:00:00"

    leads = new_or_updated_since(last_check)
    if not leads:
        print("Nothing new since last check.")
    else:
        for lead in leads:
            what = f"{lead['name']} ({lead['business_line']})"
            why = lead.get("done_summary") or "no summary set yet — fill in done_summary/left_for_you_summary"
            left = lead.get("left_for_you_summary") or lead.get("next_action") or "review it"
            link = f" — {lead['source_url']}" if lead.get("source_url") else ""
            notify(what, f"{why} | Left for you: {left}{link}", urgency="normal")
            print(f"{what}: {why} | Left for you: {left}{link}")

    STATE_FILE.write_text(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()
