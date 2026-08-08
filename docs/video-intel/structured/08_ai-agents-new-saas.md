# AI Agents are the new SaaS

## Metadata

- **Title:** AI Agents are the new SaaS
- **Channel / speaker:** Greg Isenberg — The Startup Ideas Podcast
- **Length:** 26:03
- **URL:** https://youtu.be/83fWzQSWB10
- **Date analyzed:** 2026-08-08
- **Transcript source:** docs/video-intel/transcripts/08_ai-agents-new-saas.txt

## One-paragraph thesis

The video argues that AI agents represent a wealth-creation wave comparable to (and larger than) the SaaS era, because agents don't sell software tools — they sell completed work, which means their addressable market is the multi-trillion-dollar labor market rather than the software budget. The core shift is from "here is a tool your team can use" to "here is a job your team no longer has to do." The winning playbook: pick a niche where missed work costs money, find one high-frequency workflow that people already pay a human or agency to do, shadow the human who does it to capture the real workflow detail, build the smallest useful agent (starting as a constrained workflow, not a fully autonomous employee), wrap it in a trust-building SaaS layer (logs, approvals, evals, handoffs), sell pilots priced like labor, productize the repeated patterns, and market it with before/after "workflow teardown" content in one niche until the internet associates you with that workflow.

## Core concepts & frameworks

### 1. "The product is the job" (agent SaaS vs. classic SaaS)

Classic SaaS sells software; agent SaaS sells work. A traditional product positions itself as a tool a team could use; an agent product positions itself as a job the team no longer has to do by hand. The buyer's mental benchmark is not other software but a junior employee, an agency, or added headcount — so the pitch is: handles one annoying job better than a junior employee, faster than an agency, cheaper than hiring. Examples given: an AI "superhost" answering restaurant phones (handles questions, reservations, VIP routing, staff alerts, integrates with OpenTable/Yelp — Slang AI cited as an example), and AI dispatchers/receptionists for home services companies that answer calls 24/7, respond to texts, and book jobs (Sameday cited as an example).

### 2. The five traits of a workflow worth automating ("workflow with a paycheck attached")

Start from work people already pay for (an employee, agency, receptionist, coordinator, dispatcher). A good agent workflow has:

1. **High frequency** — happens all the time; daily is good, hourly is better (every inbound lead, call, ticket, quote request, appointment, order, maintenance request).
2. **A clear finish line** — an unambiguous "done" state (job booked, ticket categorized, refund approved, vendor scheduled, customer got a useful answer).
3. **Touches existing software** — Gmail, Slack, Shopify, HubSpot, Zendesk, Stripe, etc., so the agent has tools to act with and context to read.
4. **Annoying-but-learnable edge cases** — if the work is too basic, plain automation (e.g., Zapier-style zaps) already handles it; if it's pure human judgment, v1 will break. The sweet spot is repetitive work with just enough judgment that AI adds value.
5. **The buyer can feel the loss** — missed calls, slow replies, dropped leads, empty calendar slots, expensive humans doing low-value coordination.

### 3. Shadow the human before building

Before prompting or coding, watch a real person do the job 10–20 times (screen recordings with narration are ideal; you can pay operators for this). Ask: what makes a case easy vs. weird, what do they check before deciding, where do mistakes happen. The point is that the surface-level task hides a deeper real workflow (a restaurant host answering "what time are you open?" actually knows kitchen close times, stroller-friendly tables, patio status, VIP handling, when to route private-dining inquiries). "The detail is the product."

### 4. The seven-part agent spec

Every agent should be specced with: (1) what wakes the agent up (trigger), (2) what context it needs, (3) what tools it can use, (4) what it's allowed to do autonomously, (5) where it needs approval, (6) when it must escalate to a human, and (7) what success looks like. Skipping this produces "agent slop" — impressive demos that don't hold up.

### 5. The Minimal Useful Agent (MUA) and the autonomy ladder

Don't build a fully autonomous employee first — that's how you get Twitter demos that don't work and bad businesses. Four good first versions, in ascending autonomy:

1. **Draft-and-approve agent** — reads context, drafts the reply/quote/summary/next step; a human approves. Best where there is workflow risk, creativity, or approval processes.
2. **Triage agent** — classifies inbound work and routes it (maintenance request vs. billing issue vs. refund).
3. **Coordinator agent** — moves work between systems and people: checks availability, sends reminders, chases missing info, keeps things moving.
4. **Bounded-action agent** — performs one specific action under clear rules (book an appointment, send a follow-up, process a refund under $50 — the Uber Eats automatic-refund pattern).

The ladder: draft → triage → coordinate → act.

### 6. Workflows before agents ("earn autonomy")

Citing Anthropic's agent guidance: many agent problems should start as workflows. A workflow follows a predictable path; an agent decides dynamically. Founders should earn autonomy — start with a predictable path and add judgment only where it creates value. Launch with one workflow and one promise (e.g., "we answer missed calls for roofers and book qualified jobs"). One workflow that works is enough for day one, and it builds confidence in both you and the customer — who is likely buying an agent for the first time and doesn't want everything at once from a non-Microsoft/Salesforce vendor.

### 7. The wrapper is the SaaS; the agent does the work, the wrapper creates the trust

What separates a cool automation from a real agent-first SaaS product is the product wrapper: logs, approvals, controls, handoff rules, a way to test before going live, and visibility into why the agent did what it did. The agent itself lives in the phone system, inbox, Slack channel, or CRM; the customer still needs a "control room" dashboard (can be simple): e.g., call summaries, reservation outcomes, and missed human handoffs for a restaurant phone agent; tickets created, vendor routing, tenant updates, owner approvals for a property maintenance agent.

### 8. Evals as both quality gate and sales asset

Build a test set of ~50 real examples of the job with marked correct answers (50 calls, 50 leads, 50 maintenance requests). Run the agent against them: did it classify correctly, ask for the right missing info, apply the right policy? Re-run this "gym" every time you change the prompt, model, tools, or workflow. It doubles as a sales asset: "We tested this on 50 of your old maintenance requests. It routed 42 correctly, flagged 6 for human review, and made 2 mistakes — here are the mistakes and how we fixed them." That transparency builds trust, especially with owners of unglamorous businesses.

### 9. Sell the pilot like labor, then productize

Fastest path: run pilots where you manually do the work with AI assistance, then productize the repeated parts — "you earn the software by doing the work first." Start with three customers in one niche (same niche, same workflow, same pain), sell the outcome ("we will answer and qualify your missed calls"), charge a setup fee plus a simple monthly fee, and only move to usage/outcome pricing once you understand the value. The speaker believes outcome pricing is the long-term future of agent pricing (customers don't want another seat), but warns against jumping there immediately. The product emerges when every customer in the niche needs the same repeated pattern (every roofer: emergency call script, service-area check, financing questions, estimate follow-up; every med spa: lead scoring, consultation booking, no-show recovery, post-treatment follow-up).

### 10. Distribution via workflow teardowns

The content format working right now: show the painful old way of a process step by step (call comes in, nobody answers, customer calls a competitor — or a CSR juggles five questions, calendar, service area, notes, reminders, and forgets the follow-up), then show the agent way (call answered, right questions asked, service area and urgency checked, appointment booked, CRM updated, confirmation sent, edge cases flagged to a human). Owners feel the pain viscerally — you're selling painkillers, not vitamins. Pick one workflow and make the internet associate you with it: publish the checklist, the benchmark, the teardown, ~50 examples of the workflow. Then put paid ads behind the content formats that prove out. Focus on one platform to start.

## Step-by-step playbooks

### Playbook A: Finding and scoping the agent idea

1. Pick one niche you understand where missed work costs money (examples: roofers, med spas, Shopify brands, restaurants, home services, property management, insurance agencies).
2. Write down 20 jobs people in that niche complain about (roofers: missed calls, financing questions, insurance paperwork, appointment reminders; med spas: lead qualification, no-show recovery, membership upsells; Shopify brands: returns, exchanges, wholesale lead follow-up).
3. Score each job on five dimensions: (a) how often it happens, (b) how expensive the pain is, (c) how easy it is to know when the job is done, (d) what tool/software access it needs, (e) who already owns the budget for it.
4. Choose the job with a paycheck attached — work someone is already paid to do — and validate it against the five workflow traits (frequency, clear finish line, software access, learnable edge cases, felt loss).

### Playbook B: Shadowing and speccing

1. Find a human who currently does the job; watch them do 10–20 real instances (pay them if needed).
2. Have them screen-record and narrate as they work.
3. Interview them: what makes a case easy, what makes a case weird, what do you check before deciding, where do mistakes happen.
4. Document the real workflow, including the hidden context and judgment calls (the detail is the product).
5. Write the seven-part agent spec: trigger, context, tools, allowed autonomous actions, approval points, escalation rules, success definition.

### Playbook C: Building the Minimal Useful Agent

1. Pick the lowest rung of the autonomy ladder that delivers value: draft-and-approve or triage is usually enough for v1.
2. Before writing any software, run the job manually with an AI chat assistant: paste in the context, have the AI draft the output, have a human approve. This tests whether AI helps at all before you build.
3. Build the smallest useful version as a predictable workflow, not a dynamic agent; add judgment only where it creates value.
4. Constrain any autonomous actions with hard rules (e.g., refunds only under a dollar threshold).
5. Create an eval set from 50 real examples with marked correct answers; run the system against it.
6. Re-run the eval set after every change to prompt, model, tools, or workflow; track classification accuracy, correct escalations, and mistakes.

### Playbook D: Wrapping, piloting, and productizing

1. Build the product wrapper around the working workflow: activity logs, approval queues, settings/controls, handoff rules, a pre-live test mode, and explanations of agent decisions.
2. Deploy the agent inside the customer's existing surface (phone system, inbox, Slack, CRM) with a simple control-room dashboard.
3. Sell 2–3 pilots to customers in the same niche with the same workflow and pain; sell the outcome, not the technology.
4. Price simply: setup fee + flat monthly fee for one workflow (illustrative: $1,500 setup + $1,000/month; or $2,000 setup + $30 per qualified appointment; or $3,000/month up to 500 handled tickets). The learning matters more than the exact price.
5. During pilots, find out: what the customer values, where the agent breaks, what needs approval, and — most importantly — what they would miss if you took it away.
6. Identify the pattern repeated across every customer in the niche; build the product around that repeated pattern.
7. Layer in usage- or outcome-based pricing only after you understand the value delivered.

### Playbook E: The 30-day / four-week zero-to-launch plan

1. **Day 1:** Pick a niche where missed work costs money (home services, property management, insurance agencies).
2. **Day 2:** Interview 10 operators; have them screen-share their workflow; record the calls as research (paying them is fine).
3. **Day 3:** Pick one workflow with frequency, pain, software access, and a clear success metric.
4. **Day 4:** Write the agent spec — trigger, context, tools, rules, handoffs, eval criteria.
5. **Day 5:** Run the job manually with an AI assistant (copy/paste context, draft output, human approves) to prove AI helps before building software.
6. **Day 6:** Build the smallest useful version (draft-and-approve or triage).
7. **Day 7:** Create the eval set from 50 real examples.
8. **Week 2:** Sell two pilots in the same niche.
9. **Week 3:** Add the product wrapper — logs, approvals, settings, analytics, handoffs — using AI coding tools to build it fast.
10. **Week 4:** Publish workflow teardowns, turn the pilots into public proof, and double down on the content strategy. (Throughout all four weeks: build an audience continuously.)
11. **Months 2–3:** Identify which content formats work, put paid spend behind winners, measure LTV and channel economics, and keep iterating.

### Playbook F: Distribution / content engine

1. Pick one workflow and commit to making the internet associate you with it.
2. Produce "workflow teardown" content: narrate the old painful way step by step, then the agent way step by step.
3. Poke fun at the old way; make memes; make the buyer (owner/manager/executive) feel the pain.
4. Publish supporting assets: the checklist, the benchmark, and roughly 50 worked examples of the workflow.
5. Focus on one platform first.
6. Identify winning formats, then amplify them with paid ads.
7. Build the audience in parallel with building the product, from day one.

## Tools & stack

| Tool | What it's used for in the video | Cost/notes if stated |
|---|---|---|
| Claude / ChatGPT | Manually running the job with AI before building software (paste context, draft output, human approves) | Not stated |
| Claude (design + coding, "Fable" mentioned if live) | Building the product wrapper software (logs, approvals, settings, analytics) in week 3 | Not stated |
| OpenTable / Yelp | Integration surfaces for a restaurant phone agent (example) | Not stated |
| Gmail, Slack, Shopify, HubSpot, Zendesk, Stripe | Examples of existing software an agent workflow should touch for tools + context | Not stated |
| CRM / phone system / inbox | Where the agent actually "lives"; the SaaS dashboard is the control room on top | Not stated |
| Zapier-style automation ("zaps") | Named as the baseline: if basic automation can do the workflow, it's too simple for an agent business | Not stated |
| Slang AI | Cited example company — AI phone superhost for restaurants (calls, reservations, VIP routing, staff alerts) | Not affiliated; example only |
| Sameday | Cited example company — AI dispatchers/receptionists/sales agents for home services (answer calls, respond to texts, book/reschedule jobs) | Example only |
| Paid ads | Amplifying content formats that have already proven organic traction | Spend only after formats prove out |

## Tactics & heuristics

- Sell work, not software: frame every pitch as a job the customer no longer has to do.
- Benchmark against labor, not software: "better than a junior employee, faster than an agency, cheaper than headcount."
- Start with the paycheck: only automate work someone is already paid to do — that's where the budget exists.
- Daily frequency is good; hourly is better.
- If a zap can do it, it's too simple; if it needs pure human judgment, v1 breaks. Target repetitive-with-judgment.
- Shadow the human 10–20 reps before writing any prompt or code; pay operators for research calls if needed.
- The detail is the product — the hidden checks and context a human uses are your moat.
- Spec every agent with the seven parts: trigger, context, tools, autonomy, approvals, escalation, success.
- Earn autonomy: ship a predictable workflow first; add dynamic judgment only where it creates value.
- One workflow + one promise is enough for launch; customers buying agents for the first time don't want everything at once.
- The wrapper creates the trust: logs, approvals, test mode, and "why it did that" visibility are what customers pay for beyond the automation itself.
- Run the job manually with AI before building software — prove AI helps before you invest in engineering.
- Build a 50-example eval set and re-run it after every prompt/model/tool change; use eval results (including mistakes) transparently as a sales asset.
- Sell three pilots in one tight niche (same workflow, same pain) before generalizing.
- Charge setup + simple flat monthly first; move to usage/outcome pricing only once value is understood. Outcome pricing is the likely long-term model.
- The most important pilot question: what would the customer miss if you took it away?
- Productize only the pattern repeated across every customer in the niche.
- Market with before/after workflow teardowns; sell painkillers, not vitamins.
- Make the checklist, the benchmark, the teardown, and ~50 worked examples; own one workflow publicly.
- One platform first; paid ads only behind organically proven formats.
- Build the audience in parallel with the product from day one.
- Don't chase fully-autonomous "Twitter demo" agents — they don't work and make bad businesses.

## Metrics & benchmarks

- Labor is described as a multi-trillion-dollar market — the reason agents' TAM exceeds SaaS.
- Shadow a human for 10–20 job instances before building.
- Interview 10 operators in the niche (Day 2 of the 30-day plan).
- List 20 complained-about jobs per niche when ideating.
- Eval set size: ~50 real examples with marked answers.
- Example eval sales stat: 50 old maintenance requests → 42 routed correctly, 6 flagged for human review, 2 mistakes (shown transparently with fixes).
- Pilot count: start with 3 customers in one niche; sell 2 pilots in week 2 of the 30-day plan.
- Illustrative pricing models: $1,500 setup + $1,000/month for one workflow; $2,000 setup + $30 per qualified appointment (outcome-based); $3,000/month up to 500 handled tickets (usage-capped). Exact price matters less than the learning.
- Bounded-action example threshold: auto-process refunds under $50.
- Content volume target: ~50 published examples of the chosen workflow.
- Timeline: 30 days / 4 weeks from zero to pilots + content engine; months 2–3 for LTV and channel analysis.

## Prerequisites & warnings

**What you need before this works:**

- A niche you understand (or are willing to research deeply via operator interviews) where missed work demonstrably costs money.
- Access to real operators willing to be shadowed/interviewed (budget to pay them if necessary).
- The workflow must touch existing software (email, CRM, phone, commerce, ticketing) so the agent has both tools and context.
- An existing budget owner: someone already pays a human/agency for this work.
- ~50 real historical examples of the job to build an eval set.
- Willingness to do the work manually with AI during pilots before software exists.
- Willingness to create content consistently — the speaker is explicit that you cannot skip the content game.

**Failure modes called out:**

- Building the fully autonomous employee first: produces flashy demos that don't work in production and bad businesses.
- Skipping the human-shadowing step: you miss the hidden real workflow and build shallow "agent slop."
- Picking workflows that are too simple (basic automation already solves them) or pure-judgment (v1 breaks).
- Selling a bare automation with no wrapper: without logs, approvals, test mode, and explainability, customers can't trust it.
- Jumping straight to outcome/usage pricing before understanding the value delivered — start simple, evolve pricing.
- Trying to sell a broad multi-workflow platform on day one when you aren't Microsoft or Salesforce; first-time agent buyers want one constrained promise.
- Spreading distribution across many platforms/workflows instead of owning one workflow on one platform.
- Seeing the shift but not building — the speaker's closing warning is that most listeners will understand the opportunity and still not participate.

## Generic action checklist

- [ ] Pick one niche where missed or slow work visibly costs money.
- [ ] List 20 jobs operators in that niche complain about.
- [ ] Score each job on frequency, pain cost, clarity of "done," software access, and budget owner.
- [ ] Select one workflow that people already pay a human/agency to perform.
- [ ] Interview ~10 operators; have them screen-share and narrate the workflow (pay them if needed).
- [ ] Document the real workflow including hidden checks, edge cases, and where mistakes happen.
- [ ] Write a seven-part agent spec: trigger, context, tools, allowed actions, approvals, escalation, success metric.
- [ ] Run the job manually using an AI assistant with human approval to prove AI adds value before building anything.
- [ ] Build the smallest useful agent — draft-and-approve or triage first; defer coordination and bounded action.
- [ ] Assemble an eval set of ~50 real examples with correct answers; measure accuracy, escalations, and mistakes.
- [ ] Re-run the eval set after every change to prompts, model, tools, or workflow.
- [ ] Add the trust wrapper: logs, approval queues, settings, handoff rules, pre-live test mode, decision explanations.
- [ ] Deploy the agent inside the customer's existing systems with a simple control-room dashboard.
- [ ] Sell 2–3 pilots in the same niche with an outcome-framed promise and setup-fee + flat-monthly pricing.
- [ ] During pilots, record what customers value, where the agent breaks, what needs approval, and what they'd miss most.
- [ ] Productize the pattern repeated across all pilot customers.
- [ ] Introduce usage- or outcome-based pricing once value per unit of work is understood.
- [ ] Publish workflow teardown content (old way vs. agent way) plus a checklist, benchmark, and ~50 worked examples.
- [ ] Focus on one content platform; put paid ads behind formats that prove out organically.
- [ ] By months 2–3, measure LTV and channel economics and double down on what works.

## Best suited for

**Maps well to:**

- Local/boring service businesses with high call and inquiry volume: home services (plumbing, HVAC, roofing, pest control), restaurants, med spas, property management, insurance agencies.
- E-commerce operations (Shopify-style brands) with repetitive inbound work: returns, exchanges, wholesale lead follow-up.
- Any business with a paid coordination role — receptionists, dispatchers, CSRs, schedulers, triage staff — doing high-frequency, clearly-finishable work inside existing software.
- Solo founders and small teams who can pick one niche, do pilots manually, and build in public via niche content.
- Agencies/consultants wanting to convert service delivery into productized recurring revenue ("earn the software by doing the work first").

**Maps poorly to:**

- Workflows so simple that rules-based automation (zaps) already solves them — no defensible agent business there.
- Work requiring pure human judgment, high creativity, or regulated professional discretion where a v1 agent will break and trust can't be earned incrementally.
- Rare or one-off tasks (low frequency fails the first workflow trait) and jobs with no clear finish line.
- Businesses with no existing software surface (no CRM/phone/email systems for the agent to read from and act in).
- Buyers with no existing budget for the work — if nobody currently pays a human or agency, there's no paycheck to attach to.
- Founders unwilling to do content marketing or to constrain scope to one workflow/one niche — the playbook explicitly depends on both.
