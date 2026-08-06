# Deploying the public website — the full picture

## The problem this solves

The website used to only work with the ops hub running **on the same
machine** — it imported the hub's Python code directly and wrote straight
into the same local SQLite file. That's fine for local development, but it
silently breaks the moment the website is deployed somewhere else (like
Render): the deployed site would have no access to the hub's code or
database, and every contact-form submission would fail or vanish.

**Fixed 2026-08-06.** The website now has two modes, switched by one
environment variable:

- **`HUB_MODE=local`** (default) — direct import, exactly as before. Use
  this for local development (`python3 run.py`).
- **`HUB_MODE=remote`** — the website calls a new authenticated webhook on
  the hub (`POST /webhook/website-lead`) over HTTPS instead. This is what
  Render uses.

The hub itself **keeps running on your own machine**, exactly as it already
does day-to-day — nothing about your daily workflow changes. Only one new
thing is exposed to the public internet: a single webhook endpoint, secured
with its own shared secret, path-scoped so the rest of the hub (your
password-gated dashboard, real client data) stays private on your tailnet
only.

Tested end-to-end against a throwaway database copy before being written
here — both modes create identical-looking lead records (same fields, same
drafted-reply-attached-to-notes behaviour). The real hub database was
never touched during testing.

---

## Setup — three things, in order

### 1. Expose just the webhook endpoint via Tailscale Funnel

You already have Tailscale set up (`docs/remote_access.md`). Funnel is a
Tailscale feature that exposes **one path** of a local service to the
public internet over HTTPS — not the whole hub. Run this on the machine
that runs the hub:

```bash
# Set a secret first — pick something long and random, same idea as HUB_PASSWORD
export WEBSITE_WEBHOOK_SECRET="pick-something-long-and-random"

# Start the hub as usual (in another terminal or backgrounded)
cd ops-hub && python3 run.py

# Expose ONLY /webhook/website-lead publicly — everything else on the hub
# (dashboard, login) stays private, tailnet-only, exactly as it is today
tailscale funnel --bg --https=443 --set-path=/webhook/website-lead localhost:5000
```

This prints your public Funnel URL, something like
`https://your-machine.your-tailnet.ts.net`. That's your `HUB_WEBHOOK_URL`
for the next step (the code appends `/webhook/website-lead` itself, so just
give it the base URL). `--bg` keeps it running in the background; it
persists across hub restarts, but if the machine itself reboots you'll want
to confirm `tailscaled` is set to start on boot so Funnel comes back too.

### 2. Deploy the website to Render

`render.yaml` (repo root) is ready — Render reads it automatically once you
connect the repo:

1. Push this repo to GitHub (ask me if you want help wiring up the remote).
2. On [render.com](https://render.com), sign up (free), **New → Blueprint**,
   connect the repo. Render finds `render.yaml` and configures itself.
3. In Render's dashboard, set the two secret env vars it'll ask for
   (marked `sync: false` in `render.yaml` so they're never committed):
   - `HUB_WEBHOOK_URL` — the Funnel URL from step 1
   - `HUB_WEBHOOK_SECRET` — the same value as `WEBSITE_WEBHOOK_SECRET` you
     set on the hub machine (**must match exactly**, both sides check it)
4. Deploy. Render gives you a `*.onrender.com` URL immediately — test the
   contact form there before pointing your real domain at it.

### 3. Point your domain at Render (once purchased)

Once you've bought your domain — **watersandco.info**, confirmed 2026-08-06:

1. In Render's dashboard → your service → **Settings → Custom Domain** →
   add the domain.
2. Render gives you the exact DNS records to add (usually a `CNAME` for
   `www` and an `A`/`ALIAS` record for the bare domain).
3. Add those records wherever you bought the domain (e.g. Cloudflare's DNS
   panel, since Cloudflare Registrar manages DNS in the same dashboard).
4. Wait for DNS to propagate (usually minutes, sometimes up to a few
   hours) — Render auto-provisions a free HTTPS certificate once it
   verifies the domain.

---

## Testing checklist before calling it live

- [ ] Visit the Render `*.onrender.com` URL directly — landing page loads,
      background/wordmark render correctly.
- [ ] Submit a real test enquiry through a service contact form — confirm
      it appears as a new lead in the hub (check `/all` or the relevant
      `/line/<key>` view), tagged to the right business line, with the
      drafted reply attached in Notes.
- [ ] Submit through the general `/enquire` catch-all too — same check.
- [ ] Confirm the custom domain loads once DNS is pointed (may take a
      while to propagate — don't panic if it's not instant).
- [ ] Confirm `https://` (not `http://`) works on the custom domain —
      Render's auto-cert should handle this once DNS is verified.

## What this does NOT change

- The hub itself is unaffected — same password gate, same local database,
  same Tailscale access from your phone as always.
- Local development is unaffected — `HUB_MODE` defaults to `local`, so
  `python3 run.py` in both `ops-hub/` and `website/` on your own machine
  behaves exactly as it always has.
- No client data leaves your own machine's database — Render only ever
  holds the stateless website code; every lead still lands in the same
  SQLite file on your machine, the same "single source of truth" every
  other business line already uses.
