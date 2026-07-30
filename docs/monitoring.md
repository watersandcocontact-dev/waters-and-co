# Ongoing Monitoring — how "staying in the loop" actually works

You asked for this to not be a one-time build — that once anything new comes
into the hub, you get a terse what/why + done-vs-left-for-you breakdown
without having to dig for it. Here's how that's actually implemented, and
why it's not a single "set and forget" cloud job.

## Why there's no autonomous cloud monitor

I checked: Claude's scheduled cloud routines run in Anthropic's cloud
infrastructure and **cannot reach a locally-running app, local files, or a
local database at all**. Setting one up to "check the hub" would either fail
outright or silently do nothing — worse than not having it, because it would
look like monitoring is happening when it isn't. I didn't build that.

The only way a cloud job could reach the hub is if the hub were a permanent,
publicly-hosted, always-on service — which is the opposite of the
self-hosted/zero-signup/runs-on-my-machine setup from the very first prompt.
If you ever want that trade-off (e.g. once you're running this as a real
business and want always-on monitoring regardless of whether your laptop is
on), say so explicitly — it's a real infrastructure change, not a config flag.

## What actually works instead

**1. `scripts/new_case_check.py` — local, reliable, no signup.**
Diffs the database against the last check and fires a desktop notification
(and prints to stdout) for every new or updated case, in exactly the format
you asked for:
```
Bob the Builder (LandTax): Comps pulled, objection letter drafted | Left for you: Sign and lodge via SRO portal before deadline — https://www.sro.vic.gov.au
```
That's `{what}: {done_summary} | Left for you: {left_for_you_summary} — {source_url}`
— pulled directly from the fields already on the lead (see the case detail
page), not generated fresh by an AI call each time. That's deliberate: it
means this is fast, free, and works even if you never open Claude again.

Run it manually, or add to cron for an actual periodic check:
```bash
crontab -e
# hourly:
5 * * * * cd "/home/m/claude code/business app/ops-hub" && /usr/bin/python3 scripts/new_case_check.py
```

**Important:** this only surfaces something useful if `done_summary` /
`left_for_you_summary` / `source_url` are actually filled in when a case is
created — right now that's manual (or, once the webhook is live, whatever
the AI phone platform's payload maps to). If you leave those blank, the
notification just says "no summary set yet" — a nudge to fill them in, not a
silent failure.

**2. Ask me directly, in a live session.**
This is the more thorough option — I can read the hub's actual state (not
just what's changed since a timestamp) and give you real analysis, not a
template. Open a session, ask "what's new in the hub" or "check the queue,"
and I'll give you the terse what/why + link + done-vs-left breakdown for
anything worth flagging, same format as the notifications but with actual
judgment behind it.

**3. `/loop` for a bounded active-monitoring session.**
If you want me actively re-checking every few minutes *while you're working*
(not across days), Claude Code's `/loop` skill re-invokes a prompt on an
interval for the life of a session. Useful for "watch this while I'm at my
desk," not for "monitor this while I'm away for a week" — session-bound
schedules (the `CronCreate` tool) explicitly die when the session ends.

## Bottom line

Local + cron = reliable, unattended, forever, but templated.
Me in a live session = smarter, but only when you actually open one.
No cloud auto-pilot — not because I didn't want to build it, but because it
would have been fake.
