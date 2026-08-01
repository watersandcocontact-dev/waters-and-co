# ROADMAP.md — the plan of attack, from here to fully operational

Everything below reflects the full build as of 2026-08-01: 21 business lines,
the ops hub (daily queue, expansion budget, tax tracking, Stripe payments,
referral & loyalty program), the public website, and daily opportunity
scanning + monthly competitive monitoring. Milestone-based, not a calendar —
go at whatever pace makes sense. Update this as you go; it's a plan, not a
contract with yourself.

**If you read nothing else, read Phase 0 and Phase 1.** Everything past
that is sequencing for later, once real client work is actually flowing.

---

## Phase 0 — Kick it off (things to do this week, in order)

1. **Click "Run now" once on the `daily-opportunity-scan` scheduled task**
   (Scheduled sidebar). This is a one-time approval — without it, the
   automatic daily runs will stall waiting on a permission prompt you're
   not there to answer. After this one click, it's fully hands-off.
2. **Confirm Stripe is fully live-activated** (payment processing — see
   accounts table below). ✅ Account created (`acct_1TzJCBRq9KZRjLbM`),
   payments feature built and tested in the hub (per-lead payment
   requests → Stripe Checkout → webhook confirms paid), test-mode keys
   configured and auto-starting with the hub. **Remaining:** check the
   Dashboard's Test/Live toggle — if it stops you with a business-details/
   identity/bank-account checklist, that's Stripe's activation flow and
   needs completing before a real (live-mode) payment can be taken or
   paid out. Swap the test key in `ops-hub/.stripe_env` for a live one
   once that's done — no code changes needed.
3. **Set up a business Gmail** — free, don't wait on a custom domain.
4. **Review every draft template once, for real** — GBP outreach scripts,
   the land tax objection letter, review-request templates, the ARO
   letter, the website's auto-drafted email replies. They're solid
   drafts, not vetted for your voice or final use.
5. **Log your day-job pay periods as they land, in the hub's Tax page**
   (`/tax`). It's seeded with your 19 July payslip; every pay period after
   that needs entering by hand for the tax/income picture to stay real.
6. **Confirm remote access still works** — `http://m-hp.tail28a65e.ts.net:5000`
   from your phone, HUB_PASSWORD-gated. Already done, just verify before
   relying on it day-to-day.

Don't wait on the phone platform or review-tool signups (steps in Phase 1)
to start any of the above — those gate specific services, not the whole
launch.

---

## Accounts you'll need (with my top pick and cost, where there's a choice)

| Account | Cost | Needed for | My top pick | Why |
|---|---|---|---|---|
| **Payment processing** | $0/mo, ~1.75%+$0.30 per transaction | Getting paid by clients | **🔶 Built, test mode** — Stripe (`acct_1TzJCBRq9KZRjLbM`). Payments feature live in the hub (per-lead payment requests, Checkout, webhook confirmation). Live-mode activation status unconfirmed — check the Dashboard's Test/Live toggle. | Lowest friction to set up solo, handles one-off + recurring (monthly retainers) cleanly, no physical hardware needed since everything here is remote. Square is the alternative if you ever want in-person card tap (e.g. collecting payment on a Downsizing job site). |
| **Business email** | $0 (Gmail) | Everything | **✅ Done** — `watersandco.contact@gmail.com` | Set up. Upgrade to Google Workspace later once you have a domain and it's worth the professional address. |
| **Business name registration** | **~$44 AUD (1yr) / ~$102 AUD (3yr) via ASIC** — approximate, indexed periodically, confirm at asic.gov.au before registering | Only needed if trading as "Waters & Co" (or any name other than your own legal name) | — | Required by law if you invoice/advertise under a business name that isn't your personal name. Doesn't apply if you trade under your own name. |
| **Domain name** | ~$15-40 AUD/year | Website, professional email | — | Cheap and low-risk to grab early even if the website itself waits — secures the name before someone else does. |
| **Website hosting** | **$0/mo (Netlify or Vercel free tier)** for the marketing pages; a small always-on host (~$5-7/mo, e.g. Fly.io/Railway free-to-low tier, or a $5/mo VPS) once the contact-form backend needs to be live 24/7 | The website | **Netlify/Vercel for static pages + a small backend host for the form** | The site now has a real Flask backend behind the contact form (writes to the hub, drafts replies) — that needs *some* always-on process, not just static hosting. Cheapest real option is a small always-on host; revisit exact choice when you're ready to actually go public. |
| **AI phone platform** | $29-349/mo (Dialzara tiers) | MissedCall service | **Dialzara** | The only one of the four researched with sourced, confirmed AU number support. Test Smith.ai's free tier (25 calls/mo, $0) first if you want a no-cost quality check before committing. Full comparison: `wave1/missedcall/platform_research.md`. |
| **Review-automation tool** | $75-125/mo + $199 one-time setup | ReviewGen service | **NiceJob** | Lowest cost of entry, 14-day trial with no card required, no lock-in, strongest public API/webhook docs of the three researched. Full comparison: `wave1/reviewgen/tool_research.md`. |
| **Xero or QuickBooks Online** | $0 to you normally (client's subscription) | Bookkeeping service (Wave 2) | **Xero** | Slightly better bank-rule tooling and a genuine partner-pricing path; QBO's accountant-access model is looser if you hit friction with Xero's signup. See `wave2/bookkeeping/bank_feed_research.md`. |
| **Facebook/Meta Business Suite** | $0 account, ~$300-800/mo ad spend if used | Meta ads (if you go that route) | *(only if/when you run ads, and only once `BUDGET_PHASE` is "on" — see Phase 2)* | Skip until you've validated services with direct outreach. |
| **Google Ads** | $0 account, ~$500-1,000/mo ad spend if used | Search ads (if you go that route) | *(same gating as above)* | Search Ads work better than Meta for land tax/GBP specifically (real search intent), but neither is needed to launch. |
| **GitHub** | $0 | Cloud backup of this project, and a free path to host the website's static pages | *(optional but dual-purpose)* | You have working local git already. |

---

## Phase 1 — Launch sequence (Wave 1, one business at a time)

Recommended order, based on what's most ready-to-go and what compounds:

### 1. GBP / Local SEO — start here
Most "ready" business: 10 real Perth targets already identified
(`wave1/gbp/target_businesses_perth.md`), audit tool built and tested, 3
outreach scripts written, pricing set. **First concrete action:**
re-verify 2-3 of those target businesses' profiles are still thin
(checked 29-30 Jul 2026, profiles change), then run the phone or
text/email script this week.

### 2. Review Generation — bundle in immediately after
No new client acquisition needed — pitch as an add-on to whoever says yes
to GBP. Needs the NiceJob signup first (`wave1/reviewgen/tool_research.md`).

### 3. AI Missed-Call Reception — once you've got 2-3 clients going
Bigger setup lift per client (2-3 hrs) and needs a platform decision +
signup first (`wave1/missedcall/platform_research.md`). Don't let this
block starting GBP.

### 4. Land Tax Objection — opportunistic, not a volume play
Highest $/hr but slow (60-90 day resolution) and infrequent. Keep an ear
out for anyone mentioning a land valuation they think is too high, use
the objection letter + your state's docs (you're in WA — `wave1/landtax/state_WA.md`).

### 5. AI Tools for Business — pitch alongside GBP/MissedCall
Same client base (trades/SME) as GBP — genuinely a same-conversation
upsell ("while I'm auditing your Google listing, want me to also set you
up with an AI assistant for X?"). Competitive-discretion note baked into
the scope doc: `wave3-unscoped/ai_tools_business/service_scope.md`.

### 6. Crypto IT/Literacy — standalone push, different audience
Different client base (crypto-curious individuals, not trades/SME) —
treat as its own outreach lane. Hard boundary: education/setup only,
never investment advice — the guardrail is baked into
`wave3-unscoped/crypto_literacy/service_scope.md`, keep it that way in
every real conversation.

### 7. Odd Jobs / gig marketplace — run in parallel, all the time, lightweight
Not a launch step, an ongoing habit: check Airtasker/Marketplace/Gumtree
for $0-entry one-off jobs that match your skills
(`wave3-unscoped/opportunity_scan/gig_marketplace_scan.md`), log them
under the OddJobs line in the hub as they come in. No dedicated marketing
needed — this is meant to fill gaps, not be advertised as its own
business. If the same *kind* of job repeats 2-3 times, that's a signal to
graduate it into a real line (score it against
`wave3-unscoped/opportunity_scan/scoring_rubric.md`).

**Why this order:** ranked by fastest-to-first-dollar plus lowest setup
friction — GBP needs nothing more from you to start today; everything
after needs either a tool signup or patience for the right lead.

---

## Phase 2 — Stabilize & systemize (once you have ~3-5 active clients)

- [ ] **Actually use the Daily Queue daily** — log real hours against real
      cases so $/hr stops being a rate-card estimate and starts being
      your actual number (`ops-hub`, home page).
- [ ] **Re-price based on real data** — every pricing sheet says "revisit
      after 5-10 clients once real time-per-client is known." That point
      is now.
- [ ] **Set up the weekly monitoring habit** — either `new_case_check.py`
      on a cron, or just ask me to check the hub when you open a session.
- [ ] **Decide if the AI missed-call webhook is worth activating** —
      requires the platform API key from Phase 1 step 3
      (`ops-hub/app/webhook.py`).
- [ ] **Check the day-job-vs-business $/hr comparison on `/tax`** — once
      you have a few weeks of real logged business hours, this page will
      show your actual business $/hr against your $45/hr day-job rate.
      When business $/hr durably clears day-job $/hr *and* you can still
      cover the mortgage-serviceability numbers you and your wife need,
      that's the trigger to consider dropping the day job to 4 then 3
      days — not before, and not on a single good week. Let it run a
      full month or two of real data before acting on it.
- [ ] **Decide whether to flip `BUDGET_PHASE` to "on"** in
      `ops-hub/app/config.py` (currently "off", $0 spend). Only worth
      doing once you have a business line that's proven itself organically
      and you want to accelerate it with paid spend — the expansion
      budget module (`/expansion`) will then track cost-per-outcome
      against your best-performing line's real $/hr and flag
      keep/adjust/kill automatically per spend type.

---

## Phase 3 — Wave 2 rollout (bookkeeping → concessions → grant-finder → pension)

Bookkeeping is the most similar skill-set to what you're already doing
(ongoing client management); the other three are more navigation/advocacy
work with seniors and small businesses.

- [ ] **Bookkeeping** — pick Xero or QBO (`wave2/bookkeeping/bank_feed_research.md`),
      use the onboarding + reconciliation checklists already built. No
      BAS lodgement — explicitly out of scope.
- [ ] **Concession/rebate navigation** — the eligibility matrix
      (`wave2/concessions/eligibility_matrix.md`) is solid but every
      dollar figure needs re-confirming before you quote a real senior
      client — these are indexed annually.
- [ ] **SME grant-finder** — `wave2/grantfinder/` has the screening
      checklist and application template; business.gov.au has no alert
      feature, so this one only works with periodic manual checks (or a
      scraper later — flagged as unverified whether that's allowed under
      their terms).
- [ ] **Age Pension/Centrelink assistance** — document checklist + ARO
      letter template ready (`wave2/pension/`). The 13-week point is
      about backdating arrears, not a hard deadline to request review.

Don't launch all four at once — layer them in as Wave 1 stabilizes and
you have spare capacity.

---

## Phase 4 — Wave 3 fill-ins (built, not part of the core launch push)

- **Lost Super/TPD Navigation** — near-zero effort to layer into *any*
  other client conversation (just ask about past employers), referral-fee
  only. Read the compliance note in
  `wave3-unscoped/lost_super/service_scope.md` before taking a single
  referral fee.
- **Senior Tech Concierge** — natural cross-sell once you're doing
  Concession/Pension work with seniors — same client base.
- **Video/Podcast Repurposing** — standalone, different client base
  (content creators). Lowest $/hr in the portfolio, a "fill the gaps"
  business, not a priority.
- **Senior Downsizing/Cleanout** — local-only, physical, most
  time-intensive — fill gaps rather than prioritize.

---

## Phase 5 — Gated / needs a real decision first (not roadmap-able yet)

- **Airbnb Co-Hosting** — talk to a property/real estate lawyer about the
  WA licensing question (`wave3-unscoped/airbnb_cohost/regulatory_research.md`).
  If blocked, this phase doesn't happen.
- **NDIS Plan Navigation / NDIS Provider Compliance** — needs you to
  confirm what registration/worker-screening you'd actually need before
  I'd build client-facing material.
- **Deceased-Estate Admin** — needs a clear line drawn between
  "organizing documents" (fine) and "advising on executor legal
  obligations" (not fine without a legal qualification).
- **Grant Writing (nonprofit)** — needs a portfolio first, not viable
  cold-start; revisit once SME grant-finder gives you grant-adjacent
  runway.

---

## Phase 6 — Ongoing, no end state (runs forever in the background)

- **Daily opportunity scan** — runs automatically every morning once
  you've done the Phase 0 "Run now" click. Most days it'll find nothing
  and say so; when it does find something scoring 25+ with no regulatory
  complexity, it'll draft a full service scope + pricing sheet in
  `wave3-unscoped/<name>/` for you to review — it will never wire a new
  line into the live hub without you confirming.
- **Gig marketplace scanning** — the lightweight OddJobs habit from Phase
  1 step 7, indefinitely.
- **Tax tracking** — log pay periods and deductible expenses as they
  happen, all year, every year. Re-verify the unconfirmed ATO figures
  (currently just the WFH fixed rate — see
  `wave3-unscoped/tax_tracking/ato_figures_verification.md`) each new
  financial year, since caps/rates/thresholds move annually. This is an
  organisation tool, not tax advice — still get an accountant for actual
  lodgement, the `/tax/export` view is built to hand straight to one.

---

## How to use this

Check items off as you go, or just tell me what you've done and I'll keep
`PROGRESS.md`/`DECISIONS.md` in sync. This file is the "what's next and
why," those two are the "what's actually true right now" — if they ever
disagree, trust `PROGRESS.md`.
