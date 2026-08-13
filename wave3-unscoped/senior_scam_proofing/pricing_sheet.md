# Scam & Online Safety Check — Pricing Sheet

Priced **inside the Tech Concierge rate card** ($85/hr blended; $99
in-person / $69 remote / $145 extended / $49 follow-up), not as a new line.
See `service_scope.md` for why there is no separable product here.

## Pricing (drafted 2026-08-13, unvalidated — no client has paid this yet)

| Package | Price | Time | Effective $/hr |
|---|---|---|---|
| **Scam & Online Safety Check** — the full visit: accounts, devices, call screening, fridge card, family note | **$145** | ~90min | $97/hr — the existing extended-session price, unchanged |
| Same check, remote/screen-share (no device clean-up) | **$99** | ~1hr | $99/hr |
| Bolt-on to a standard Tech Concierge session already booked | **+$49** | ~30min | best margin — no second trip |
| 3-month re-check (settings still on, nothing new installed) | **$49** | ~30min | uses the existing follow-up slot |
| Second person, same household, same visit | **+$49** | ~30min | partner/spouse |

**Nothing here is a new price.** Every row is an existing Tech Concierge
rate with a name attached. That is deliberate: the value of this work is
that it gives the existing session a reason to be booked, and inventing a
premium for it would invite the obvious comparison with the free
government-funded option.

## Why not price it higher

The instinct is to charge more because the downside being prevented is
five figures — remote-access scams average ~$17,943 per victim. Resist it.
Two reasons, both structural:

1. **The free tier is the price anchor.** WA ScamNet, IDCARE and Be
   Connected all deliver a version of this for $0, and ID Support NSW is
   now running free one-on-one sessions as a government service. A
   $300–500 "audit" invites the family to search, find the free option,
   and conclude the paid one was opportunistic. At $145 it reads as an
   hour and a half of a technician's time, which is what it is.
2. **Fear-priced services aimed at seniors age badly.** The reputational
   floor matters more than the margin here — see the fourth boundary in
   `service_scope.md`. The service already resembles the fraud it prevents;
   pricing it off the fear makes that worse.

## Competitor evidence (checked 2026-08-13)

| Who | What | Price found |
|---|---|---|
| WA ScamNet / Consumer Protection WA | Scam presentations to seniors'/community groups on request | **Free** |
| IDCARE | Cyber Resilience Outreach Clinics in WA; victim case management | **Free** (gov-funded) |
| eSafety — Be Connected | National program, in-person help via community partners | **Free** |
| ID Support NSW | Face-to-face scam support roadshow, one-on-one, from March 2026 | **Free** (NSW) |
| **Geeks Perth** | "Tech Help for Seniors" 1–2hr in-home; scam email/phishing/passwords explicitly included | **Not published** — booking by phone/online only |
| The Original PC Doctor | In-room aged-care-facility tech help, family update after visit | Not published |
| Geeks2U / IT 4 Retirees (from the Tech Concierge sheet, 2026-08-09) | General in-home senior IT | $158/hr; $162/hr + $73/hr travel |

No Australian operator was found selling a standalone paid scam/online-
safety audit to seniors at a published price. The absence of a comparable
is not evidence of an opening — read alongside the free tier, it is
evidence that the willingness to pay separately hasn't been demonstrated.

Sources: geeksperth.com.au/tech-help-for-seniors fetched directly
2026-08-13 (no pricing on page); scamnet.wa.gov.au, IDCARE WA clinics and
the ID Support NSW program page from search results and one direct fetch of
the NSW page; loss figures are secondary industry/press summaries of ACCC /
National Anti-Scam Centre data, **not the primary report** — re-verify
before quoting to a client.

## Status

Drafted 2026-08-13 by the daily opportunity scan. Not wired into
`ops-hub/app/config.py` — no `BUSINESS_LINES` entry, no `RATE_CARD` entry,
no `TASK_TYPE_LINES` change. If the Owner adopts it, the change is a
`TechConcierge` task type and a line of website copy, nothing more.
