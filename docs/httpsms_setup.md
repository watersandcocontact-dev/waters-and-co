# httpSMS Setup — Native SMS via the Work Phone's Own SIM

**Status: hub-side code built and tested (`ops-hub/app/sms.py`), self-hosted
server NOT deployed.** This is entirely your call to action — needs Docker
(not installed on the machine this session runs on, and I don't have sudo
to install it) plus physically pairing an Android phone, both of which are
outside what I can do remotely. Everything on the hub's side is ready the
moment you have a running httpSMS instance and an API key.

## What this actually is

[httpSMS](https://github.com/NdoleStudio/httpsms) is an open-source,
self-hosted SMS gateway — no per-message fees, no rented virtual number.
The dedicated work phone runs the httpSMS Android app, stays on and
plugged in permanently, and its real SIM/number sends and receives the
texts. A small self-hosted backend (the part below) relays between that
phone and the ops hub.

## Steps (yours to run)

1. **Get Docker running** on whichever machine will host this (your
   laptop for now, per the original plan — migrate to the mini PC later
   and take httpSMS with it so it stays co-located with the rest of the
   hub, not split across two machines).
2. Clone `https://github.com/NdoleStudio/httpsms` and fill in the
   environment variables it needs (see `docker-compose.httpsms.yml`
   below for the full list — Firebase project credentials, SMTP for
   notification emails, Cloudflare Turnstile keys for the message-search
   endpoint). These all need real signups (Firebase is free-tier
   viable; SMTP can be a free Gmail app-password; Cloudflare Turnstile
   is free).
3. `docker compose up --build` — web UI on `:3000`, API on `:8000`.
4. Install the httpSMS Android app on the dedicated work phone, pair it
   to your self-hosted instance, grant SMS permissions.
5. In the httpSMS dashboard, generate an API key and note the work
   phone's number.
6. Point httpSMS's outbound webhook (for the `message.phone.received`
   event) at your ops hub's `/webhook/sms-inbound` — this needs the hub
   itself reachable from wherever httpSMS runs (same Tailscale setup
   already used for the hub's own remote access should cover this).
7. Set these on the ops hub before starting it:
   ```
   HTTPSMS_ENABLED=1
   HTTPSMS_API_KEY=<from step 5>
   HTTPSMS_FROM_NUMBER=<the work phone's number, e.g. +614xxxxxxxx>
   HTTPSMS_API_URL=<your self-hosted API URL, or leave unset to use the public api.httpsms.com>
   HTTPSMS_WEBHOOK_SECRET=<the signing secret httpSMS gives you for the webhook, optional but recommended>
   ```

## What's already built and tested on the hub side

- `send_sms(to, body, business_line=None, lead_id=None)` — outbound
  helper any business-line workflow can call (review requests,
  appointment reminders, deadline nudges). Rate-limited locally (10/min
  safety net on top of whatever httpSMS itself enforces) so this can
  never accidentally turn into a bulk-blast tool.
- `POST /webhook/sms-inbound` — receives replies, matches the sender's
  phone number to an existing lead (normalises +61/0/spaces/dashes so
  formatting differences don't cause a miss) and appends the reply to
  that lead's notes with a timestamp. No match → creates a new
  `GeneralEnquiry` lead rather than silently dropping a real reply.
  JWT (HS256) signature verification if `HTTPSMS_WEBHOOK_SECRET` is set;
  runs unverified with a logged warning if not, same "built but not
  fully locked down yet" pattern as the existing intake webhook.
- Tested end-to-end against a throwaway database copy (never touched
  production data): both the no-match-creates-a-lead path and the
  match-appends-to-existing-lead path. One real bug found and fixed
  during testing — two leads sharing a phone number updated in the same
  second could tie on `ORDER BY updated_at`, matching the wrong one;
  fixed with an `id DESC` tiebreaker.

## One thing to double-check once it's live

The exact inbound webhook field names (`contact`, `content`, `owner`)
are httpSMS's documented shape as of 2026-08 — worth a quick diff
against `https://docs.httpsms.com/webhooks/events` once you actually
have a live webhook firing, the same way the Twilio-style intake
webhook already flags "adapt field names to whatever the platform
actually sends."
