# Ops Hub

Self-contained local CRM/lead-tracker for all business lines (Wave 1 + Wave 2 prep).
Zero external accounts required — SQLite file on disk, Flask dev server, runs entirely
on this machine.

## Run it

```bash
cd ops-hub
python3 run.py
```

Open http://127.0.0.1:5000

The database is created automatically at `ops-hub/data/hub.sqlite3` on first run.

## What's here

- `app/config.py` — business lines, statuses, per-line extra fields, deadline thresholds
- `app/db.py` — SQLite schema (`leads`, `webhook_log`)
- `app/models.py` — CRUD + deadline-alert logic (incl. auto 60-day land-tax deadline)
- `app/routes.py` — dashboard, due-this-week, lead form (create/edit/delete)
- `app/webhook.py` — intake webhook receiver, **inactive until you set env vars**
- `templates/`, `static/` — UI

## Activating the phone-platform webhook (later, once you've signed up for one)

```bash
export INTAKE_WEBHOOK_ENABLED=1
export INTAKE_WEBHOOK_SECRET="choose-a-long-random-string"
python3 run.py
```

Point your AI phone platform's webhook at `POST http://<your-host>:5000/webhook/intake`
with header `X-Intake-Secret: <same secret>`. See `app/webhook.py` for the expected
JSON shape — adjust field names to match whatever platform you pick.

## Notes

- No email notifications (would require a mail-account signup); deadline alerts are
  dashboard-only, shown as a banner at 14/60/30-day thresholds plus overdue.
- Dependency: Flask, installed to the user site-packages with
  `python3 -m pip install --user --break-system-packages flask` (this machine's
  Debian/Ubuntu Python blocks plain global pip installs and `venv` needs a missing
  `python3-venv` apt package this session couldn't install without sudo).
- Not hardened for the public internet — this is a local ops tool. If you ever expose
  it beyond localhost, put it behind auth first.
