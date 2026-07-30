# Remote Access — how to reach the hub from your phone/laptop anywhere

Two options, in order of what I'd actually recommend using day-to-day.

## Option A (recommended) — Tailscale. One signup: **you**, free.

**What it is:** a private network (VPN mesh) between only your own devices —
your server and your phone/laptop. The hub is never exposed to the public
internet at all; only devices you've personally signed into your Tailscale
account can reach it.

**Why this over a public tunnel:** the hub stores real client PII (names,
phones, emails, notes) and has only a single shared password, not proper
multi-user auth. A public tunnel + one password is an acceptable stopgap for
one night; it's not something you want as your permanent daily-use URL,
because it's sitting on the open internet where bots constantly probe for
exactly this kind of thing. Tailscale removes that exposure entirely — the
password becomes a second layer, not your only line of defense.

**What you need to do (I can't do this part — account creation):**
1. Go to tailscale.com, sign up free (Google/GitHub/email — your choice).
2. Install Tailscale on this machine: `curl -fsSL https://tailscale.com/install.sh | sh` then `sudo tailscale up` (follow the browser login prompt it gives you).
3. Install the Tailscale app on your phone and laptop, sign into the same account.
4. Once connected, this machine gets a stable private address/hostname (Tailscale calls it MagicDNS, something like `your-machine.your-tailnet.ts.net`).
5. Set `HUB_PASSWORD` (see below) and start the hub normally (`python3 run.py`) — reach it at `http://your-machine.your-tailnet.ts.net:5000` from any of your signed-in devices, from anywhere.

I didn't install or configure Tailscale itself since it requires you to
create the account and complete the browser login — everything else (the
hub, the password gate) is already done and ready the moment you are.

## Option B (zero signup, use tonight) — Cloudflare quick tunnel

Already built and tested — no account needed at all, works right now:

```bash
cd ops-hub
export HUB_PASSWORD="something-long-and-random"
./scripts/start_remote.sh
```

This prints a temporary public HTTPS URL (like
`https://ltd-dear-divorce-exception.trycloudflare.com`) that proxies to your
local hub. Tested end-to-end: the tunnel comes up, and the login wall holds
over the public URL (unauthenticated requests get redirected to `/login`,
confirmed with a live test on 2026-07-30).

**Trade-offs, be aware of these:**
- The URL is **public on the internet** — anyone who gets it can reach your
  login page (they still need the password, but it's one factor, not two).
- The URL **changes every time you restart the script** — not something to
  bookmark permanently on your phone.
- Cloudflare's own terms note account-less tunnels have "no uptime
  guarantee" — fine for occasional/emergency use, not for relying on daily.

The script refuses to start if `HUB_PASSWORD` isn't set, specifically so you
can't accidentally put unauthenticated client data on the public internet.

## The password gate itself (`HUB_PASSWORD`)

Either option needs this. It's one shared password (not per-user accounts —
this is a solo-operator tool), stored as an environment variable, never
committed to git:

```bash
export HUB_PASSWORD="pick-something-long-and-random"
```

Without it set, the hub runs exactly as before — open, no login, intended
for localhost-only use. The moment you set it, every page except the login
form and the (currently-inactive) intake webhook requires signing in first.
Session cookies are signed with a random key generated on first run and
persisted to `ops-hub/data/secret_key.txt` (gitignored) — restarting the
server doesn't log you out.

## My recommendation

Use Option B tonight if you want to check the hub from your phone right
now. Set up Option A (Tailscale) this week for the actual daily-use setup —
it's free, takes about 10 minutes, and is the one that doesn't put client
data on the open internet.
