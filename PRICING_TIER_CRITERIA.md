# Pricing Tier Criteria — "Which number do I actually quote?"

**Answers a real gap found 2026-08-06:** every price on the website is a
range (e.g. "$400–800"), but most of those ranges never had a rule for
where a specific job lands — only 4 rows on the whole site had one before
today (GBP cleanup, GBP management, ReviewGen management, MissedCall
management — all below, unchanged, just collected here for one place to
check). Everything else is new judgement-call criteria, same status as any
other pricing assumption in this repo: a defensible starting rule, not
gospel — refine once you've quoted a few real jobs and see where they
actually land.

**How to use this:** before quoting, find the service below, check the
factor that drives the price, quote accordingly. Default to the low end
when genuinely unsure — cheaper-than-expected builds trust faster than a
walked-back high quote does.

---

## Local Presence & Never Miss a Call

### GBP — One-off cleanup ($150–300) — *already tiered*
Use the 10-point audit score: **sub-40 → $300** (near-full rebuild), **40–60 → $200–250**, **60+ → $150** (light touch-up only).

### GBP — Ongoing management ($100–200/mo) — *already tiered*
**Basic $100** (2 posts/mo, photo refresh, no review replies) / **Standard $150** (4 posts/mo, review responses, quarterly re-audit) / **Growth $200** (weekly posts, full review management, monthly report). Let the client pick, default-recommend Standard.

### ReviewGen — One-off setup ($100–200)
**$100** — one platform (Google only), client's existing templates/branding, no custom tone work. **$150–200** — multiple platforms (Google + Facebook), custom response-tone tuning for their trade, or an existing messy review backlog to clean up first.

### ReviewGen — Ongoing management ($100–300/mo) — *already tiered*
**Basic $100–150** (automated requests + monitoring only, no responses) / **Managed $200–300** (Basic + drafted responses to every review, sentiment summary). Managed is the one to lead with — it's the actual differentiator vs the Starworks-style self-serve tools.

### AI Missed-Call Reception — Setup ($300–600)
**$300** — single service line, simple FAQ script, client keeps their existing number (forwarding only). **$450** — a couple of service lines or pricing rules to configure. **$600** — multiple services/staff routing, number porting coordination, or a client who needs several rounds of script revision before go-live.

### AI Missed-Call Reception — Monthly management ($150–400/mo) — *already tiered*
**Basic $150** (daily log review, monthly summary) / **Standard $250** (+ weekly recording sampling, lead push, urgent-call flagging) / **Premium $400** (+ calendar/booking integration, monthly refresh call, priority support). Underlying per-call platform usage cost is *always* itemised separately, never buried in this fee.

### Bookkeeping — Micro, 0–25 tx/mo ($149–179/mo)
Scale roughly linearly with transaction count: **≤10 tx/mo → $149**, **10–18 → $164**, **18–25 → $179**. Same logic one tier up.

### Bookkeeping — Small, 25–100 tx/mo ($299–449/mo)
**25–50 tx/mo → $299–349**, **50–75 → $350–399**, **75–100 → $400–449**. Multiple bank accounts or inventory tracking pushes toward the top of whichever band.

### SME Grant-Finder — Shortlist report ($79–99 flat)
**$79** — client already knows roughly what they're after, just wants it confirmed/shortlisted. **$99** — genuinely open-ended ("what am I even eligible for"), needing a fuller sweep across federal + state + local programs.

---

## AI Systems for Business

### AI Implementation — Single automation build ($990–1,490 fixed)
**$990** — one data source, one trigger, one action (e.g. "form submission → CRM entry + confirmation email"). **$1,490** — multiple steps/conditions, or integrating 2+ existing tools that don't talk to each other natively.

### AI Implementation — Small business system, multi-step ($2,500–4,000 fixed)
**$2,500** — 2 of the 3 core components (e.g. lead capture + CRM, no invoicing yet). **$4,000** — all of lead capture + CRM + invoicing/payments + reporting, or genuinely messy existing data to migrate/clean first.

### AI Implementation — Optional monitoring ($150–250/mo)
**$150** — a single simple workflow, low change-frequency. **$250** — a multi-integration system where "what's new" check-ins and tweaks genuinely take real time each month.

### AI Tools for Business — Basic ($200–350 one-off)
**$200** — one tool, one person, standard use case (no custom prompt/template work needed). **$350** — one tool but genuinely trade-specific template/prompt pack built from scratch.

### AI Tools for Business — Standard ($400–600 one-off)
**$400** — 2 tools, 2 people. **$600** — 3 tools, a full team, or a business with unusual/complex workflows needing more tailoring.

### AI Tools for Business — Ongoing support ($80–150/mo)
**$80** — occasional light troubleshooting only. **$150** — a client who wants a standing monthly check-in call plus template refreshes as tools update.

---

## Seniors & Family Support

### Senior Tech Concierge — sessions
Kept as real ranges, not flattened, since travel time is the actual swing factor:
- In-person standard (~1hr): **$70** close/no-travel, **$85** further out or awkward timing.
- Remote standard (~1hr): **$55** simple, **$65** more devices/complexity within the hour.
- Extended (~1.5hr): **$105–125** same logic, scaled up.
- Follow-up (~30min): **$40–50**, mostly travel-driven again.

### Crypto IT/Literacy — sessions
1:1 stays flat **$85/hr** (no range to resolve). Group workshop: **$59/head** for 4+ people, **$349 flat** once it's effectively a private booking (≤6 people) — quote flat once headcount makes per-head math work out close to or above $349 anyway.

### Digital Legacy — Starter ($120–150)
**$120** — under ~10 accounts, straightforward. **$150** — closer to the upper end of "top ~10 accounts," or the client needs extra hand-holding setting up the password manager itself.

### Digital Legacy — Full inventory ($250–320)
**$250** — a fairly organised client, most accounts already known. **$320** — genuine full sweep needed (forgotten accounts, old email addresses to check, subscription audit turns up a lot).

### Digital Legacy — Annual refresh ($80–100)
**$80** — quick confirm-nothing's-changed. **$100** — a few new accounts/subscriptions to add since last time.

### Senior Downsizing — Coordination only ($45–65/hr, or $400–1,200 packaged)
Hourly: **$45** — one or two vendors to liaise with (e.g. just a removalist). **$65** — juggling several (removalist + charity pickup + agent + cleaner) or a tight/urgent timeline. Packaged flat quote scales the same way: **$400–600** simple single-vendor moves, **$800–1,200** full multi-vendor coordination.

### Senior Downsizing — Hands-on labour/sorting
**Set to a flat $80/hr (2026-08-06, Owner's call)** — no longer a range. `PRICING.md`, `ops-hub/app/config.py`, and the website have all been updated to match.

### Photo & Memory Digitisation — Coordination/curation fee (~$55/hr)
Flat rate, not a range — the variable cost is the bureau's own per-item pricing (passed through separately, see the service's own pricing sheet), not this fee.

---

## Content Repurposing

### Video/Podcast Repurposing
**Per episode ($249)** and **subscription ($199/episode)** are both already flat, no range to resolve.

---

## Property & Tax Review

### Land Tax / Rates Objection — Standard residential ($400–800 flat)
**$400–500** — a clear-cut case: obvious comparable sales nearby, straightforward valuation error, minimal research needed. **$600–700** — a typical case, some real comparable-sales digging required. **$800** — genuinely contested valuation, thin comparable-sales evidence nearby, or a property with unusual features (zoning overlay, recent unique renovation) that takes real extra research time to build a solid case for.

---

## Status

Built 2026-08-06 in response to a direct question before launch: "do we
already have pre-determined prices in these ranges?" — answer was mostly
no, so this exists now. Every rule here is a reasoned starting point, not
tested against real client jobs yet — revisit after the first several real
quotes in each line to see whether the actual factors driving price match
what's assumed here, and tighten/loosen the bands accordingly.
