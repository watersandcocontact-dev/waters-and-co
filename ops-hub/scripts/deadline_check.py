#!/usr/bin/env python3
"""Optional daily deadline check — desktop notification, no signup required.

The dashboard banner (see app/routes.py) already shows deadline alerts whenever
you open the hub. This script is for an OS-level nudge even when the dashboard
isn't open, via `notify-send` (Linux desktop notifications — already available
on this machine, no account needed).

Run manually:
    python3 scripts/deadline_check.py

Or add to your crontab for a daily 8am check:
    crontab -e
    # then add:
    0 8 * * * cd "/home/m/claude code/business app/ops-hub" && /usr/bin/python3 scripts/deadline_check.py
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.models import deadline_alert_buckets  # noqa: E402


def notify(title, message, urgency="normal"):
    try:
        subprocess.run(["notify-send", "-u", urgency, title, message], check=False)
    except FileNotFoundError:
        print(f"[notify-send not available] {title}: {message}")


def main():
    buckets = deadline_alert_buckets()
    overdue = buckets["overdue"]
    due_14 = buckets["due_14"]
    due_30 = buckets["due_30"]

    if overdue:
        names = ", ".join(f"{d['name']} ({d['business_line']})" for d in overdue[:5])
        notify("Ops Hub: OVERDUE deadlines", f"{len(overdue)} overdue: {names}", urgency="critical")

    if due_14:
        names = ", ".join(f"{d['name']} ({d['business_line']})" for d in due_14[:5])
        notify("Ops Hub: due within 14 days", f"{len(due_14)} items: {names}", urgency="normal")

    if due_30:
        names = ", ".join(f"{d['name']} ({d['business_line']})" for d in due_30[:5])
        notify("Ops Hub: due within 30 days", f"{len(due_30)} items: {names}", urgency="low")

    if not (overdue or due_14 or due_30):
        print("Nothing due within 30 days.")


if __name__ == "__main__":
    main()
