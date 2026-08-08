# Waters & Co — Video Intel Implementation Plan

Written 2026-08-08. Applies the eight videos in `structured/` to Waters & Co
specifically. Read alongside `PROGRESS.md`, `PRICING.md`, `DECISIONS.md`.

The videos repeat each other a lot (as expected). Section 1 is the deduped
strategy; Section 2 is the per-video plan of attack; Section 3 is the sequenced
roadmap; Section 4 is what we're deliberately NOT adopting.

---

## 1. Cross-cutting themes → what they mean for W&C

Seven themes appear in 3+ videos each. These are the actual lessons; the
per-video sections show where each came from.

### T1. Sell work, not software — benchmark against labor (videos 1, 6, 8)
Every offer should be framed as "a job you no longer have to do," priced
against what a person costs, not against other software. W&C's `$/hr`-sorted
queue already thinks this way internally; the **pitch** now has to say it.
Missed-Call SMS = "your after-hours receptionist." AI Tools = "your admin
assistant that never sleeps." Rewrite offer copy accordingly.

### T2. The audit is the front-end product (videos 6, 8)
Don't lead with "we build automations." Lead with a paid (or initially free)
**AI Opportunity Sprint**: shadow the real workflow, map where time and money
leak, deliver an operating map + ROI matrix ranked by revenue / risk / cost.
The sprint is cheap to deliver (it's what W&C's competitive-analysis muscle
already does), de-risks the client's decision, and every sprint produces the
spec for a build engagement. This slots in as a new productized entry point
for the AI Tools line.

### T3. Deterministic core + LLM judgment + human gate + evals (videos 1, 6, 7, 8)
The architecture all four "agent" videos converge on is exactly the W&C house
pattern already in force (confirm-before-send): plain software for the
predictable 90%, LLM only at genuine decision points, human approval on
anything outward-facing, and a small **golden dataset of test cases re-run
after every change**. Two upgrades to adopt: (a) formal eval sets for anything
we deploy for clients — "42 of 50 handled correctly, here's how we fixed the
rest" is a *sales asset*, not just QA; (b) full audit trails as a stated
feature in proposals.

### T4. Owned audience: everything funnels to an email list (videos 1, 4, 5)
W&C has zero owned audience. Social is rented; the 117-lead cold campaign is
one-shot. Start the list now: lead magnet on watersandco.info (a genuinely
good checklist/template from the existing template library), email-gate the
best content, and a short weekly/fortnightly email for Perth/AU small
businesses ("what AI can quietly do for a trade/clinic/shop this week").
Benchmarks to steer by: 40%+ open = excellent, <30% = fix subject lines.
The list compounds; every later theme (content, teardowns, re-warms) feeds it.

### T5. Content = trust minutes; teardowns are the format (videos 4, 5, 8)
Buyers need cumulative watch/read minutes before they trust you. W&C plays
the **B2B/services game**: dollars-per-view, not virality — a post seen by
300 Perth business owners beats 50k random views. The proven format for agent
services is the **workflow teardown**: "how [business type] handles missed
calls today vs. with an agent — costs, steps, failure points." One platform,
one recognizable one-of-one story ("solo operator running an 18-line business
with AI agents, alongside a day job" — that story is genuinely rare),
iterate one piece at a time, every piece embeds the lead magnet.

### T6. Focus + premium positioning: flagship lines, anchor client (videos 3, 8)
"One product to $10M" translated to W&C scale: **two flagship lines** (AI
Tools/automation + Missed-Call SMS — already the two live campaigns) get the
content, the sprints, and the iteration reps; the other lines stay on the
menu but don't get growth investment until a flagship works. Premium is
positioning, not price: keep prices in the expected band, but make every
touchpoint (site, invoice, proposal, brand kit) signal premium — already
mostly true. Land **one anchor client** per flagship — a respected local
business whose name/logo/result carries the next ten sales — with the Owner
personally closing it. Measure **sell-through** (conversion per lead source,
response SLA held), not sell-in (emails sent, leads listed).

### T7. The Owner is an agent manager; the ops must watch themselves (videos 2, 6, 7)
The constraint isn't agent capacity, it's **Owner decision latency** around a
day job. Adopt: (a) a **daily watchdog digest** — one message covering site
up/form works/Stripe events/queue movement/campaign replies — so the Owner
reads one thing; (b) a **pinned decision queue** — every pending
confirm-before-send item in one numbered list, batched for when the Owner
surfaces (the new `next-decision` skill drills these one at a time); (c) a
**scheduled critical-journey test** of watersandco.info's contact form —
we've already shipped one silent lead-loss bug; this makes that class of bug
a 24-hour discovery instead of a lucky catch; (d) the **graduated trust
ladder** — visible → efficient → automatic → delegated — as the explicit
policy for expanding what the PA/GM does without confirmation (nothing
outward-facing ever climbs past the gate).

---

## 2. Plan of attack, per video

### Video 1 — Marketing Agents Masterclass (Cody Schneider)
[structured/01_marketing-agents-masterclass.md](structured/01_marketing-agents-masterclass.md)

**Teaches:** signal-based outbound (scrape engagers of niche LinkedIn
influencers = live hand-raises), waterfall enrichment, separate sending
domains, inbox agent driving to a booking link, 6-month re-warms, agent =
code + data stream + occasional LLM on a cron.

**W&C adoption:**
1. **Signal-based targeting for wave 2 outreach.** Before sourcing more raw
   leads, mine hand-raises: AU businesses posting/commenting about missed
   calls, admin overload, AI curiosity — LinkedIn, local FB groups, GBP
   review patterns. Score existing 117+26 leads for signals; signal-positive
   leads get priority and a tailored first line.
2. **Never send volume from the core identity.** Current campaign (117 Gmail
   drafts, Owner-sent) is fine at this scale. Before any scaled sending:
   separate sending domain + verification pass, per the video's warning that
   bad sending burns the real domain.
3. **Reply-handling agent (draft-only).** Wire campaign replies into the hub:
   classify (interested / question / not-now / never), draft the response,
   queue for Owner confirm. Not-now leads get an automatic 6-month re-warm
   date in the hub.
4. **⚠ Compliance gate:** the video assumes US CAN-SPAM. Australia's **Spam
   Act 2003 requires consent** (express or inferred — e.g. published business
   address relevant to the offer), working unsubscribe, and sender identity.
   Verify current ACMA guidance against the live source before any send wave,
   per the triple-check rule. LinkedIn-engager scraping also sits against
   LinkedIn ToS + Privacy Act — do the *signal-watching* manually/lightly
   rather than industrial scraping.

### Video 2 — 4 AI Agents To Automate 99% Of Your Life (Sandeep Swadia)
[structured/02_4-ai-agents-automate-life.md](structured/02_4-ai-agents-automate-life.md)

**Teaches:** Four C's (Coordination, Creativity, Clarity, Coaching), 5-part
agent prompt skeleton (job/tool/categories/output/boundary), graduated trust
ladder, contract-microscope table, multi-model advisory board.

**W&C adoption:**
1. Rewrite the PA/GM's recurring jobs (queue triage, brief prep, template
   work) as 5-part skeletons with the **boundary line explicit** in each —
   makes the existing house rules machine-checkable and reusable as client
   deliverables.
2. **Contract microscope as a client-facing micro-service:** the 5-column
   plain-English contract table (says / means / matters / risk / questions)
   is exactly the kind of fixed-price, boundary-safe doc product W&C can sell
   to trades (subcontracts, supplier T&Cs) — *navigation, not legal advice*;
   state that on the deliverable.
3. **Coaching mode for pre-job briefings:** before Owner calls/visits, add an
   optional rehearsal — likely objections, tough questions, a one-page prep
   card. Extends the existing pre-job briefing duty (CLAUDE.md #4).
4. Trust ladder → adopted as T7(d) policy.

### Video 3 — Premium Isn't About Price (Open Residency)
[structured/03_premium-positioning.md](structured/03_premium-positioning.md)

**Teaches:** premium at scale (signal premium, price in-band), design for the
shelf, sell-through > sell-in, know the intermediary math, founder closes the
anchor customer, one product to $10M, stage-gate launches, speed as the
small-team edge.

**W&C adoption:**
1. **Flagship focus (T6):** AI Tools + Missed-Call SMS get the investment;
   other 16-19 lines stay listed but unpushed. Revisit quarterly.
2. **Anchor client per flagship**, Owner-closed, with a written case study +
   permission to name. Target: one respected Perth trade/allied-health
   business each.
3. **Sell-through dashboard in the hub:** per lead-source conversion, time-
   to-first-response, retention — not vanity counts. 30-day adjust cycle.
4. **"Never stock out" = response SLA.** A missed inbound lead is a stockout.
   The watchdog (T7a) enforces it.
5. **Shelf design:** proposal/invoice/site polish is the "packaging tripled
   sales" lesson — mostly done via brand kit; audit the proposal template
   next, since that's the shelf a prospect actually inspects.
6. **Buy pattern recognition:** occasional paid advisory calls with someone
   who has scaled an AU service business beat guessing; log takeaways to
   DECISIONS.md.

### Video 4 — Newsletters Are the Easiest Business (Open Residency)
[structured/04_newsletters-easiest-business.md](structured/04_newsletters-easiest-business.md)

**Teaches:** owned list beats rented reach, tactic-stacking growth (waitlist,
email gates, repurposing cycle, referral rewards from zero-cost assets,
recommendations, paid boosts), layered monetization, 40-45% open benchmark,
survey-driven premium tiers, investor-update pattern.

**W&C adoption:**
1. **Launch the W&C email list (T4).** Fortnightly to start (sustainable next
   to a day job): one practical "AI for your business" tip, one teardown or
   client story, one soft CTA. Platform: whatever's cheapest with data
   portability; the list is the asset.
2. **Lead magnets from existing IP:** the template/checklist library is
   already built — package one per flagship (e.g. "Missed-call cost
   calculator", "10 admin jobs an agent can do for a trade business").
3. **Referral rewards from zero-cost digital assets:** the referral/loyalty
   program (already operating) adds digital rewards — templates, a free
   mini-audit — instead of only discounts.
4. **Survey the list** once it exists; premium offerings (sprints, retainers)
   get designed from survey data, not guesses.
5. **Monthly update email** to warm contacts/clients (the investor-update
   pattern): what shipped, results, one ask. Compounds referrals and
   makes W&C look bigger than one operator.

### Video 5 — Content Masterclass (Open Residency)
[structured/05_content-masterclass.md](structured/05_content-masterclass.md)

**Teaches:** five content games (W&C = B2B/services), dollars-per-view over
virality, Seven Lego Bricks iteration, comprehension as master KPI, content
minutes → trust, long-form as trust engine, native lead magnets, AI-proof
moats (one-of-one story, niche term ownership).

**W&C adoption:**
1. **One platform, one story.** LinkedIn (where AU SME owners are; pairs with
   video 1's signal-watching). The one-of-one story: *day-job operator
   running an 18-line business solo with AI agents* — build-in-public
   with real numbers where safe.
2. **Cadence:** 2 posts/week, iterated one at a time using the Lego Bricks
   method (hold proven topic/angle/structure, vary one brick). The PA/GM
   drafts; Owner confirms each post (house rule). Target the first 100 reps
   before judging.
3. **Dollars-per-view discipline:** measure inquiries and email signups per
   post, not impressions. On-target views only.
4. **Own a term.** Candidate: something like "quiet automation" for SMEs —
   pick one, use it relentlessly, own the niche vocabulary in AU search.
5. Every post embeds the lead magnet → list (T4). Teardown format (T5) is
   the default content type.

### Video 6 — FDE: The $1M/Year AI Job (Verity Agents)
[structured/06_fde-forward-deployed-engineer.md](structured/06_fde-forward-deployed-engineer.md)

**Teaches:** intelligence is commoditized, deployment is the moat; audit
first (shadow the real workflow — the real process is never the documented
one); audit itself is sellable (call it a "sprint"); deterministic + LLM +
human gate; evals/golden datasets; shadow-mode rollout on the client's
existing stack; measure revenue/risk/cost; 95% of pilots fail from
token-maxing.

**W&C adoption:**
1. **Productize the AI Opportunity Sprint (T2)** as the AI Tools line's front
   door. Fixed price, fixed deliverable (operating map + ranked ROI matrix +
   one quick win implemented). First 2-3 free/cheap for case studies, then
   priced per PRICING.md tier logic.
2. **Sprint methodology doc:** what to shadow, what to ask, how to extract
   the unwritten exception rules, the ROI matrix template. Build once, reuse
   every engagement.
3. **Never force migrations:** deploy on whatever the client already uses
   (their phone system, their calendar, their spreadsheet). This is why SMEs
   will buy from W&C and not an enterprise vendor.
4. **Rollout ladder for client builds:** shadow mode → suggestions → gated
   autonomy, with an eval set from day one. The 95%-pilot-failure stat and
   "we measure in revenue, risk, cost" framing go straight into proposals.
5. W&C **is** an FDE shop at SME price points — that's the positioning
   sentence for the AI Tools line.

### Video 7 — Managing AI Agents (Ryan Carson)
[structured/07_managing-ai-agents.md](structured/07_managing-ai-agents.md)

**Teaches:** everyone becomes an agent manager; cloud parallelism; scheduled
browser-testing of the critical journey; daily production watchdog digest;
daily self-improvement loop; decision latency is the bottleneck; phone-first;
no standing prod credentials for agents.

**W&C adoption:**
1. **Critical-journey test (T7c):** scheduled end-to-end test of the
   watersandco.info contact form → hub webhook → lead record, with a daily
   pass/fail line in the digest. Direct answer to the 2026-08-07 silent
   lead-loss incident class.
2. **Daily watchdog digest (T7a):** one morning message — site health, form
   test result, Stripe events, new leads/replies, queue top-3, pending
   decisions count. Fits the Owner's day-job rhythm.
3. **Decision queue (T7b):** numbered, pinned, drained via `next-decision`.
   Track decision latency; if items sit >48h, the queue is too noisy —
   prune what's being escalated.
4. **Self-improvement loop, weekly not daily:** one scheduled pass over the
   hub/site/templates proposing 1-3 concrete fixes as prepared diffs for
   Owner review. Scaled to W&C budget (Carson spends ~$15/day; we start
   weekly).
5. **Credential hygiene** (no standing secrets in agent reach) — already
   house practice; keep it explicit in any client-facing agent build too.

### Video 8 — AI Agents are the new SaaS (Greg Isenberg)
[structured/08_ai-agents-new-saas.md](structured/08_ai-agents-new-saas.md)

**Teaches:** sell the job, not the software; 5-trait workflow score
(frequency, clear finish line, touches existing software, learnable edge
cases, felt loss); shadow 10-20 reps; 7-part agent spec (trigger, context,
tools, autonomy, approvals, escalation, success); autonomy ladder; Minimal
Useful Agent; evals as sales asset; pilot pricing (setup + flat monthly);
teardown marketing; 30-day launch plan.

**W&C adoption:**
1. **Score every W&C service line against the 5 traits.** Missed-Call SMS
   scores near-perfect (hourly frequency, clear finish, touches phone stack,
   learnable edge cases, viscerally felt loss) — confirming flagship choice.
   Use the score to pick flagship #3 later.
2. **7-part spec template** goes into the sprint methodology (video 6) — the
   sprint's output IS a 7-part spec the client can see and approve.
3. **Pilot pricing formalized:** setup fee + flat monthly, matching existing
   $150-300/mo tiers; 2-3 pilots per niche, then productize the repeatable
   version. Outcome pricing only after eval data exists.
4. **Same-niche pilots:** don't take 3 pilots in 3 industries; take 3 in one
   (e.g. Perth trades), so edge cases learned once resell forever.
5. **Teardown marketing (T5)** is this video's GTM verbatim — old-way vs
   agent-way, published on LinkedIn, feeding the list.

---

## 3. Sequenced roadmap

**Phase 1 — this fortnight (mostly PA/GM prep, Owner confirms):**
1. Send the already-drafted 117-lead campaign per schedule — after the Spam
   Act check (V1.4) is verified against live ACMA guidance.
2. Stand up the daily watchdog digest + scheduled contact-form journey test
   (V7.1-2).
3. Decision queue live in the hub; drain via `next-decision` (V7.3).
4. Package lead magnet #1 from existing templates; add email capture to
   watersandco.info (V4.2).
5. Draft the AI Opportunity Sprint one-pager + methodology skeleton (V6.1-2).

**Phase 2 — this month:**
6. Reply-handling agent (draft-only) + 6-month re-warm dates (V1.3).
7. First LinkedIn posts: 2/week teardown cadence, Owner-confirmed (V5.2, V8.5).
8. Newsletter issue #1 to whatever list exists; monthly update email to warm
   contacts (V4.1, V4.5).
9. Sell-through dashboard fields in the hub (V3.3).
10. Proposal template audit — evals/audit-trail/revenue-risk-cost framing
    added (V3.5, V6.4).

**Phase 3 — this quarter:**
11. Close anchor client #1 per flagship (Owner-led; PA/GM preps everything)
    (V3.2).
12. Run first 2-3 sprints in ONE niche; publish case studies; formalize pilot
    pricing (V6.1, V8.3-4).
13. Weekly self-improvement loop on hub/site (V7.4).
14. Survey the list; design the first premium tier from the answers (V4.4).
15. Quarterly flagship review: 5-trait scores + sell-through data decide
    whether a third line gets promoted (V8.1).

---

## 4. Explicitly NOT adopting (and why)

- **Industrial LinkedIn engager scraping / waterfall enrichment stack**
  (V1): US-legal-context playbook; Privacy Act + LinkedIn ToS + cost don't
  fit a solo AU operator. We take the *signal* principle, done manually.
- **10k/month cold-email infrastructure** (V1): scale mismatch and Spam Act
  risk. W&C stays low-volume, high-relevance, Owner-sent.
- **Paid ads / paid subscriber boosts** (V4, V5): not before organic + list
  show conversion. Revisit when a flagship has an anchor case study.
- **$5k/month token budgets, per-session cloud VM fleets** (V7): right
  shape, wrong scale. We adopt the automations, sized to hobby-budget crons.
- **Mass-retail mechanics** (V3): distributor/broker math doesn't apply to
  services — only the translated principles (sell-through, anchor, focus).
- **Anything crossing the standing regulatory lines** (all videos): no
  playbook overrides the NDIS/TPB/ASIC/legal-practice boundaries or
  confirm-before-send.
