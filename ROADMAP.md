# ROADMAP.md — from here to launch, and beyond

My recommended sequencing, based on what's actually built and ready vs. what
still needs a decision from you. Not a fixed calendar — milestone-based, go
at whatever pace makes sense. Update this as you go; it's a plan, not a
contract with yourself.

---

## Accounts you'll need (with my top pick and cost, where there's a choice)

| Account | Cost | Needed for | My top pick | Why |
|---|---|---|---|---|
| **Payment processing** | $0/mo, ~1.75%+$0.30 per transaction | Getting paid by clients | **Stripe** | Lowest friction to set up solo, handles one-off + recurring (monthly retainers) cleanly, no physical hardware needed since everything here is remote. Square is the alternative if you ever want in-person card tap (e.g. collecting payment on a Downsizing job site). |
| **Business email** | $0 (Gmail) | Everything | **Gmail (free)**, upgrade to Google Workspace later | Don't pay for Workspace until you have a domain and it's worth the professional address — free Gmail is genuinely fine for outreach right now. |
| **Business name registration** | **~$44 AUD (1yr) / ~$102 AUD (3yr) via ASIC** — approximate, indexed periodically, confirm at asic.gov.au before registering | Only needed if trading as "Waters & Co" (or any name other than your own legal name) | — | Required by law if you invoice/advertise under a business name that isn't your personal name — this is a legal registration step, not optional once you pick a trading name. Doesn't apply if you just trade under your own name. |
| **Domain name** | ~$15-40 AUD/year | Website, professional email | — | Cheap and low-risk to grab early even if the website itself waits — secures the name before someone else does. |
| **Website hosting** | **$0/mo (Netlify or Vercel free tier)** for a simple multi-page site like the segregated-landing-pages plan; ~$5-20/mo if you want a paid host | The website (once built) | **Netlify or Vercel (free tier)** | A simple marketing site with one page per service doesn't need paid hosting — both offer a genuinely free tier that's more than enough, and both deploy straight from a git repo (you already have one). Only upgrade if you outgrow the free tier's limits, which is unlikely for a site this size. |
| **AI phone platform** | $29-349/mo (Dialzara tiers) | MissedCall service | **Dialzara** | The only one of the four researched with sourced, confirmed AU number support — that matters more than price for a service literally about answering Australian trade businesses' calls. Test Smith.ai's free tier (25 calls/mo, $0) first if you want a no-cost quality check before committing, but Dialzara is what I'd actually run the business on. Full comparison: `wave1/missedcall/platform_research.md`. |
| **Review-automation tool** | $75-125/mo + $199 one-time setup | ReviewGen service | **NiceJob** | Lowest cost of entry, 14-day trial with no card required, no lock-in contract, and the strongest public API/webhook docs of the three researched — matters later if you want it feeding into the ops hub. Full comparison: `wave1/reviewgen/tool_research.md`. |
| **Xero or QuickBooks Online** | $0 to you normally (client's subscription) | Bookkeeping service (Wave 2) | **Xero** | Slightly better bank-rule tooling and a genuine (if unverified-for-solo-operators) partner-pricing path; QBO's accountant-access model is looser/easier if you hit friction with Xero's practice-oriented signup. Either works — see `wave2/bookkeeping/bank_feed_research.md` for the full tradeoffs. |
| **Facebook/Meta Business Suite** | $0 account, ~$300-800/mo ad spend if used | Meta ads (if you go that route) | *(only if/when you run ads)* | Skip until you've validated the service with direct outreach — ties to the ad-spend estimate from earlier in this conversation. |
| **Google Ads** | $0 account, ~$500-1,000/mo ad spend if used | Search ads (if you go that route) | *(only if/when you run ads)* | Same — Search Ads work better than Meta for land tax/GBP specifically (real search intent), but neither is needed to launch. |
| **GitHub** | $0 | Cloud backup of this project (and now, hosting the website if you go the Netlify/Vercel route above) | *(optional but now dual-purpose)* | You have working local git already. Free tier covers both a backup and feeding a free website host. |

**On the segregated-landing-pages website specifically:** built (2026-07-31) — `website/`, one page per live service under 3 segments, each ready for an ad to link straight to it. Runs locally for now; still needs a domain + hosting decision before it's actually live for ads to point to (see `website/README.md`).

---

## Phase 0 — Pre-launch (before you take a single real client)

- [ ] **Set up payment processing** (Stripe recommended — see the accounts
      table above). This is the one genuine blocker with nothing to fall
      back on.
- [ ] **Business email** — Gmail is fine to start. Don't wait on a custom
      domain to begin outreach.
- [ ] **Review every draft template once, for real** — the GBP outreach
      scripts, the land tax objection letter, the review-request templates,
      the ARO letter. They're solid drafts, not vetted for your voice/final
      use.
- [ ] **HUB_PASSWORD + Tailscale** — ✅ already done.

Don't wait on the phone platform or review tool signups to start — those
gate specific services (D and C below), not the whole launch.

---

## Phase 1 — Launch sequence (Wave 1, one business at a time)

Recommended order, based on what's most ready-to-go and what compounds:

### 1. GBP / Local SEO — start here
This is the most "ready" business: 10 real Perth targets already identified
(`wave1/gbp/target_businesses_perth.md`), audit tool built and tested, 3
outreach scripts written, pricing set. **First concrete action:** re-verify
2-3 of those target businesses' profiles are still thin (they were checked
29-30 Jul 2026, profiles change), then run the phone or text/email script
on them this week.

### 2. Review Generation — bundle in immediately after
No new client acquisition needed — pitch it as an add-on to whoever says
yes to GBP. Needs a tool signup first (`wave1/reviewgen/tool_research.md` —
NiceJob recommended, 14-day no-card trial, so low-risk to start even before
your first client confirms).

### 3. AI Missed-Call Reception — once you've got 2-3 clients going
Bigger setup lift per client (2-3 hrs) and needs a platform decision +
signup first (`wave1/missedcall/platform_research.md`). Don't let this
block starting GBP — layer it in once you have some cash flow and a
rhythm.

### 4. Land Tax Objection — opportunistic, not a volume play
Highest $/hr but slow (60-90 day resolution) and infrequent — this fills
background time, it's not what you build a weekly routine around. Keep an
ear out for anyone mentioning a land valuation they think is too high
(existing GBP/other clients are a natural source) and use the objection
letter template + your state's docs (all 8 built, but you're in WA —
`wave1/landtax/state_WA.md`) when it comes up.

**Why this order and not another:** it's ranked by "fastest to first
dollar" combined with "lowest setup friction" — GBP needs nothing more
from you to start today, everything after it needs either a tool signup or
patience for the right lead to show up.

---

## Phase 2 — Stabilize & systemize (once you have ~3-5 active clients)

- [ ] **Actually use the Daily Queue daily** — log real hours against real
      cases so $/hr stops being a rate-card estimate and starts being your
      actual number (`ops-hub`, home page).
- [ ] **Re-price based on real data** — every pricing sheet says "revisit
      after 5-10 clients once real time-per-client is known." That point is
      now.
- [ ] **Set up the weekly monitoring habit** — either `new_case_check.py`
      on a cron, or just ask me to check the hub when you open a session.
- [ ] **Decide if the AI missed-call webhook is worth activating** —
      requires the platform API key from Phase 1 step 3
      (`ops-hub/app/webhook.py`).

---

## Phase 3 — Wave 2 rollout (bookkeeping → concessions → grant-finder → pension)

This is the order from your original build spec, and it still makes sense:
bookkeeping is the most similar skill-set to what you're already doing
(ongoing client management), the other three are more navigation/advocacy
work with seniors and small businesses.

- [ ] **Bookkeeping** — pick Xero or QBO (`wave2/bookkeeping/bank_feed_research.md`),
      use the onboarding + reconciliation checklists already built. Remember:
      no BAS lodgement, that's explicitly out of scope.
- [ ] **Concession/rebate navigation** — the eligibility matrix
      (`wave2/concessions/eligibility_matrix.md`) is solid but every dollar
      figure needs re-confirming before you quote a real senior client —
      these are indexed annually and several were already caught out of
      date once.
- [ ] **SME grant-finder** — `wave2/grantfinder/` has the screening
      checklist and application template; business.gov.au itself has no
      alert feature, so this one only works if you're willing to manually
      check periodically (or build a scraper later — flagged as unverified
      whether that's even allowed under their terms).
- [ ] **Age Pension/Centrelink assistance** — document checklist + ARO
      letter template ready (`wave2/pension/`). Remember the 13-week point
      is about backdating arrears, not a hard deadline to request review.

Don't launch all four at once — each is a genuinely different client base
and skill. Layer them in as Wave 1 stabilizes and you have spare capacity.

---

## Phase 4 — Wave 3 (the 4 businesses built from your pricing table)

These exist and are ready (`wave3-unscoped/`), just never part of the
original wave plan — fold them in opportunistically rather than as a
dedicated launch push:

- **Lost Super/TPD Navigation** — near-zero effort to layer into *any*
  other client conversation (just ask about past employers), referral-fee
  only. Start mentioning it as soon as you have a referral partner lined up
  (see the compliance note in `wave3-unscoped/lost_super/service_scope.md`
  before taking a single referral fee).
- **Senior Tech Concierge** — natural cross-sell once you're doing
  Concession/Pension work with seniors — same client base.
- **Video/Podcast Repurposing** — standalone, different client base
  (content creators, not trades/seniors) — treat as a separate small
  push whenever you have spare capacity, lowest $/hr in the portfolio so
  it's a "fill the gaps" business, not a priority.
- **Senior Downsizing/Cleanout** — local-only, physical, most
  time-intensive — same logic, fill gaps rather than prioritize.

---

## Phase 5 — Gated / needs a real decision first (not "roadmap," a checkpoint)

Don't schedule these — they need a specific unblocking action before
they're even roadmap-able:

- **Airbnb Co-Hosting** — talk to a property/real estate lawyer about the
  WA licensing question (`wave3-unscoped/airbnb_cohost/regulatory_research.md`).
  If blocked, this phase doesn't happen.
- **NDIS Plan Navigation / NDIS Provider Compliance** — needs you to
  confirm what registration/worker-screening you'd actually need before
  I'd build client-facing material for either.
- **Deceased-Estate Admin** — needs a clear line drawn between "organizing
  documents" (fine) and "advising on executor legal obligations" (not fine
  without a legal qualification) before this is buildable.
- **Grant Writing (nonprofit)** — your own pricing note says it "needs a
  portfolio first." Not viable as a cold-start business; revisit once
  you've got other grant-adjacent work (SME grant-finder) to point to.

---

## How to use this

Check items off as you go, or just tell me what you've done and I'll keep
`PROGRESS.md`/`DECISIONS.md` in sync. This file is the "what's next and
why," those two are the "what's actually true right now" — if they ever
disagree, trust `PROGRESS.md`.
