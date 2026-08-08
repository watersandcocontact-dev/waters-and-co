# FDE: The $1M/Year AI Job Explained

## Metadata
- **Title:** FDE: The $1M/Year AI Job Explained
- **Channel / speakers:** Greg Isenberg (host) with "Voss" of Verity Agents (name also transcribed as Vass/Vance; ex-Meta software engineer, now runs an enterprise AI deployment firm). Greg also references his agency LCA.
- **Length:** 51:34
- **URL:** https://youtu.be/zXysLUTLjw4
- **Date analyzed:** 2026-08-08
- **Note:** The video's subject is the **Forward Deployed Engineer (FDE)** role — the person who manages how AI agents enter and operate inside a business: designing, deploying, evaluating, and governing agent systems for real organizations.

## One-paragraph thesis
Frontier AI intelligence is now a commodity — every company can buy the same models and the same tooling, so intelligence itself can no longer be a competitive moat. The advantage has shifted entirely to *deployment*: deciding where, how, and why intelligence is applied inside a specific company's messy, undocumented reality. The person who does this is the Forward Deployed Engineer, a role popularized by Palantir that combines consulting-grade business understanding with real software-engineering judgment. FDEs run a repeating loop — audit the real workflow, decide what should be deterministic software vs. LLM judgment vs. human approval, build with evals and audit trails, deploy gradually inside existing systems, measure against revenue/risk/cost, and improve — and because so few people can do both halves well, the role commands extreme compensation and is learnable through a concrete 30-day self-training plan.

## Core concepts & frameworks

### Intelligence commoditization → deployment is the moat
Every company now has access to the same frontier models and the same tool stack (coding agents, IDE assistants, copilots). If everyone can buy the same intelligence, differentiation comes from the *bridge* between a company's specific processes and that intelligence. The edge belongs to whoever builds the best company-specific application of general-purpose capability.

### The Forward Deployed Engineer (FDE)
A role coined by Palantir: an engineer embedded with the customer (often literally on site) who learns their workflows firsthand, then customizes a platform/agents to solve their exact pain points. It is "consulting for the software space." The AI era multiplies demand for this because every company will need customized agents, not generic tools.

### The three stages of FDE involvement
1. **Business reality** — understand how work *actually* happens today (not the documented version). This consumes the bulk of the time and doubles as change management: it brings the client along the journey.
2. **FDE judgment** — decide where intelligence belongs and, critically, where it does not. Assess each workflow/step for risk, ROI, and whether it truly needs non-deterministic judgment.
3. **Deployed AI system** — actually build and ship it, ranging from low-code workflow assembly to full production code, and own it when it breaks.

### The two-sided skill profile (the "million-dollar hire")
- **Business/consulting side:** workflows, costs, incentives, risk, adoption, business value, internal politics — where top consultants excel.
- **Technical side:** models, systems, APIs, data, code, reliability, evals, guardrails, harnesses, post-training/fine-tuning — where software engineers excel.
The FDE must be the *best* combination of both, not an average of both. The rarity of that combination is why the role pays so much, and both halves are trainable.

### Documented process vs. real process
The stated workflow ("an email arrives") hides the reality: 40+ senders, no two formatted alike, data in PDFs/screenshots/spreadsheets/forwarded threads, half the cases are exceptions, and the true routing rules live in one person's head, unwritten. If you build against the documented process you build for a system that doesn't exist. The only fix is sitting with the people who do the work — a one-hour interview yields the idealized job; a full day on site reveals the exceptions.

### The tri-layer system design: deterministic / agent / human
The best AI solution for most companies is mostly deterministic software, with LLM calls only at genuine judgment points, and human-in-the-loop approval gates at risky steps. For a typical 10-step workflow, perhaps only 3 steps need model judgment; the rest are if/then logic and API calls. Some workflows shouldn't be touched by AI at all (too risky, low ROI, or already automated). Deciding this split is the core of FDE judgment.

### The Audit → Evals → Deployment loop
The master operating loop. Audit the workflow, build evaluation suites that prove correct behavior, deploy with hand-holding and monitoring — then loop again, because improving one system exposes interconnected upstream/downstream bottlenecks. This is how one 10x'd workflow compounds into a 100x'd business.

### Evals as "non-determinism into evidence"
Convert fuzzy AI behavior into measurable evidence: golden datasets from historical data, a pass/fail matrix (right data? required steps followed? matches an expert? safe to act on?), and an evaluation report that classifies failures by cause. Anything not safe to act on routes to a human. For creative/subjective tasks, encode what "good" looks like from prior examples and accept that human-in-the-loop feedback must continuously improve the harness.

### The three buckets of business value
Every agent must be measured in exactly three currencies: **revenue uplift, risk mitigation, cost savings**. Nothing else matters to a business buyer.

### The happy path vs. unhappy paths
There is one way for a process to go right and a thousand ways for it to go wrong. An agent built only for the happy path is worth nothing; an agent built for the exceptions and failure modes is worth "a million times more."

### Ecosystem depth before model agnosticism
Long-term value lies in being able to swap models freely (accuracy up, cost down, no vendor lock-in), but a beginner should first go deep on ONE model and ONE agent-building platform, then branch out to others and open-source models. You can only judge which model fits a task after you understand several — depth precedes breadth. (Analogy used: a sommelier learns the customer's palate before recommending the wine; handing everyone Pinot Noir is why most AI pilots fail.)

### De-risking the buyer (the promotion frame)
You are pitching to individual humans who fear getting fired and want to get promoted. Bringing you in is itself a risk to them. Sell by removing risk: build on their existing systems, prove value before charging, keep everything auditable, and frame outcomes as cost-effective value they can point to at performance-review time.

## Step-by-step playbooks

### Playbook 1: Run a workflow audit (the entry engagement)
1. Pick a department/function and enumerate every workflow in it.
2. Go where the work happens — on site if at all possible (relationship + exception discovery), remote if necessary. Interview people, observe them working full days, and get read access to their systems (ERP, CRM, email).
3. For each workflow, document: every real step, all data sources and formats, the software used, who touches it, and — most importantly — the exception handling and unwritten tribal rules held in individuals' heads.
4. Map bottlenecks, repetitive work, and judgment points; produce an "operating map" of the function.
5. Build a priority/ROI matrix: what is worth automating vs. not, with expected value per workflow.
6. Present the map plus a build proposal with projected ROI. (Clients report the audit alone is worth ~10x its price.)
7. Naming tip: buyers have an allergic reaction to the word "audit" — rebrand it as a "sprint" (e.g., design sprint) to sell it more easily.
8. Early-career variant: do the first audits free to get in the door, get paid only on proven measurable value; your first 1–3 customers teach you more than you're worth to them, after which you can charge.

### Playbook 2: Design the intelligent workflow (software vs. agent vs. human)
1. Take the audited workflow step by step and classify each step: deterministic software (if/then, API calls), LLM judgment (genuinely non-deterministic decisions like categorization), or human control (approval/exception).
2. Filter at the workflow level first: skip workflows that are too risky, low ROI, or already well automated. Prioritize high-volume workflows where the improvement is large enough to matter.
3. Structure the typical deployed agent as: intake → validation → agent drafting → **human approval gate** → execution of the remaining steps → record update in the system of record. Push clients to include the human-in-the-loop approval stage.
4. Estimate accuracy/risk per design option (e.g., "this design gets ~80% accuracy — not worth it; this alternative is higher ROI, faster to build, lower risk") and choose accordingly.

### Playbook 3: Build the evaluation suite
1. Gather as much historical data as possible (e.g., 10,000 previously categorized emails; 5,000 past presentations) to form a golden dataset.
2. For subjective tasks, distill explicit quality criteria from the examples (layout rules, style rules, what "good" means to this client).
3. Define the pass matrix per run: correct data pulled, required steps completed, output matches expert judgment, safe to act on. Route anything unsafe to a human.
4. Run the suite and produce an evaluation report: e.g., 50 runs, 41 passed; classify the 9 failures by cause (5 missing data, 4 wrong record pulled) and fix the system accordingly.
5. Bake in permanent human-in-the-loop feedback so the harness (and optionally fine-tunes/post-training) keeps improving after deployment — evals alone never reach perfection on subjective work.

### Playbook 4: Deploy inside the business
1. Integrate with what already exists — never force a software migration. Build on top of their ERP/CRM (NetSuite, Salesforce, SAP, Concur, Expensify, Gong, Workday...) and connect systems together; a client who spent years and millions on their stack will reject any "move off it" pitch.
2. Test in a controlled environment first.
3. Scale autonomy gradually: shadow mode → increasing autonomy → full production. Walk the client through the journey rather than flipping a switch.
4. Log every agent action — a complete audit trail is a hard requirement for trust ("if you can't show the client what the agent is doing, they will never trust you").
5. Hand-hold adoption while monitoring KPIs and SLAs; when something breaks in production, it's on you to know who to call and how to fix it.
6. After deployment, observe and improve — then start the loop again on the next (now-visible) bottleneck.

### Playbook 5: The 30-day zero-to-FDE training plan
(30 days of material; pace it as needed.)

**Week 1 — Build an agent that completes a real loop.**
1. Ask an LLM for one real enterprise back-office workflow (finance, HR, procurement, logistics, or sales) in as granular detail as possible.
2. Build an agent for it, one concept per day: agent looping → tool usage → guardrails → context & memory → audit trail → applying it to the real workflow.
3. Bar to hit: the agent completes the task at high accuracy even when prompted sloppily — repeatable background motion, not a well-crafted one-shot prompt.
4. Checkpoint: a working agent with tools, guardrails, deliberate memory, and a full audit trail for one task.

**Week 2 — Turn the demo into a system that can recover.**
5. Enforce defined JSON schemas (not free-form text) and validate them.
6. Enumerate failure modes and build explicit exception/failure handling — design for the unhappy paths, not just the happy path.
7. Checkpoint: an agent that survives malformed inputs and known failure conditions.

**Week 3 — Make it measurable and economically viable.**
8. Add retry logic.
9. Build a golden dataset and eval suite; verify improvement over time.
10. Optimize cost: test cheaper/smaller models for subtasks instead of frontier models everywhere.
11. Measure the agent against the three buckets: time saved (cost), risk mitigated, revenue uplift.
12. Checkpoint: an evaluated agent with known failure modes, measured costs, and a golden dataset.

**Week 4 — Defend the system like an FDE.**
13. Rehearse the story as an engineer: architecture, key decisions, iteration history (e.g., accuracy 70% → 95%).
14. Rehearse the same story as a VP: problem, outcome, evidence, risk, economics.
15. Price it: what would this be worth to a customer?
16. Pitch it to real businesses and absorb their corrections ("no, we'd want it this way") — that feedback is the training data for your first real engagement.
17. End state: on day 30 you understand FDE work *and* have evidence you can do it — the job before the title.

### Playbook 6: Selling yourself/AI services into a company
1. Lead with the audit/sprint (free at first, paid once proven).
2. Pitch improvement of their existing stack, never replacement ("fish with dynamite": you keep what works, I make it faster/cheaper/better).
3. Speak the buyer's incentives: quantify in revenue/risk/cost terms they can cite in their own performance review.
4. Meet face-to-face where possible — guiding people through change is far easier with a relationship than as "a guy behind a screen flipping a switch."
5. Under-promise, over-deliver; use the audit to spark their own ideas for use cases.
6. Get paid on measurable value early on; charge properly once you have 1–3 reference wins, at which point you're ahead of nearly everyone in a market with far more demand than qualified supply.

## Tools & stack

| Tool | What it's used for in the video | Cost/notes if stated |
|---|---|---|
| Claude Code / Codex / Cursor / GitHub Copilot | The now-commoditized coding-agent stack "all 50 enterprise clients" use — evidence intelligence is no longer a moat | Cursor noted for model agnosticism |
| OpenAI Agents platform / Claude Agent SDK (and equivalents from every provider) | Agent-building platforms; pick ONE and master it before going multi-model | — |
| Kimi (K3), GLM, open-source models | Second-wave exploration after mastering one ecosystem; building proprietary harnesses | — |
| Gemini Flash (and other small/cheap models) | Cost optimization — cheaper models for subtasks instead of frontier models everywhere | — |
| ChatGPT / any LLM | Generating a granular real-world enterprise workflow to practice against in the 30-day plan | — |
| Palantir ontology/platform | The original FDE model: central customizable platform + on-site engineers, connectors, data lakes | Historical/illustrative |
| Salesforce, Gong, Chili Piper, HubSpot, Apollo, Clay | Examples of divergent sales stacks across companies — why every audit is different | — |
| NetSuite, SAP, Concur, Expensify, Workday | ERP/finance systems to build ON TOP of and integrate, never migrate away from | Client spent ~2 years / ~$2M moving to NetSuite |
| JSON schemas + validation | Structured agent outputs instead of free-form text (week 2 of the plan) | — |
| Golden datasets / eval suites | Proving agent behavior; built from historical company data | — |

## Tactics & heuristics
- Advantage is in deployment, not intelligence — every competitor can buy the same models.
- The documented process is never the real process; the real rules live unwritten in individual employees' heads.
- Sit with people for full days rather than one-hour interviews; exceptions only surface when you watch real work.
- On-site presence is mostly about relationship-building, which later makes change management dramatically easier.
- Most of a good AI solution is deterministic software; use LLMs only where judgment is genuinely required.
- Push for a human approval gate in every agent deployment.
- Not every workflow deserves AI — skip low-ROI, high-risk, or already-automated ones; prioritize high-volume workflows with large improvement potential.
- Build for the unhappy paths; exception coverage is where all the value is.
- Full audit trails of agent actions are non-negotiable for client trust.
- Master one model + one agent platform deeply before going model-agnostic; agnosticism is the end state, not the start.
- Long term, avoid marrying one intelligence provider — the goal is accuracy up, cost down, freedom to switch.
- Use cheaper models for subtasks; don't run frontier models on everything (anti-"token maxing").
- Sell the audit; if the word "audit" scares buyers, call it a "sprint."
- Do early audits free, get paid on proven value; first customers are worth more to you than you to them.
- Build on top of existing systems and integrate them; never force a migration.
- Roll out via shadow mode → increasing autonomy → production.
- Frame everything in the three buckets: revenue uplift, risk mitigation, cost savings.
- Your real buyer is a person who wants to get promoted and not get fired — de-risk them.
- Rehearse every system twice: once as the engineer (architecture/decisions) and once as the VP (problem/outcome/evidence/economics).
- Do the job before you have the title — a portfolio agent with evals and economics beats credentials.
- Learn from practitioners (YouTube/X), not universities — the material won't be in textbooks for years.

## Metrics & benchmarks
- FDE compensation: ~$150K base + considerable equity at the low end, up to ~$1M/year — called the hottest role in tech.
- MIT stat cited: **95% of generative AI pilots fail**.
- Horror story: a C-suite team blew through a **$10M** annual AI budget in **~3 months** via unmanaged "token maxing," with no needle-moving results.
- Clients report the audit alone was worth **~10x** what they paid for it.
- Example workflow intake: emails from **40+ senders**, no two formatted alike; roughly **half of cases are exceptions**.
- Eval report example: 50 runs → 41 passed; of 9 failures, 5 missing data, 4 wrong record pulled.
- Iteration example: agent accuracy improved from **~70% to ~95%** over deployment iterations.
- Example switching cost: ~2 years and a couple of million dollars to migrate to one ERP (why you never pitch migration).
- Design threshold example: a projected ~80% accuracy design judged "not worth it" versus a lower-risk higher-ROI alternative.
- 30-day plan assumes heavy effort (speaker references ~12-hour days) but is explicitly pace-flexible.
- "One way to go right, a thousand ways to go wrong" — the exception-coverage ratio that determines an agent's worth.

## Prerequisites & warnings

**Prerequisites**
- Both skill streams, deliberately trained: communication/consulting ability (extracting truth from people, navigating politics, adoption) AND software engineering (APIs, schemas, reliability, evals, guardrails). Weakness in either halves your value.
- Deep fluency in at least one model ecosystem and agent-building platform before advising on model choice.
- Access to the client's real systems and real workers (ERP/CRM access, shadowing time) — without it you're building against fiction.
- Historical data from the client to seed golden datasets for evals.
- Willingness to be accountable in production: when it breaks, it's your problem.

**Failure modes called out**
- **Token maxing:** giving everyone unlimited model access and letting AI "figure it out" — burns budgets, causes hallucinations, moves nothing; the main reason 95% of pilots fail.
- **Building to the documented process:** interviewing for an hour, hearing the happy path, and shipping a system that can't handle the 50% of cases that are exceptions.
- **Happy-path-only agents:** worthless in production; value is proportional to exception coverage.
- **Forcing migrations:** asking a client to abandon their existing stack kills the deal and the trust.
- **Slapping AI everywhere:** applying LLMs to steps that needed if/then logic, or to workflows that shouldn't change at all.
- **Opaque agents:** no logged traces → no client trust, ever.
- **Premature model agnosticism:** spreading thin across providers before mastering one.
- **Ignoring buyer psychology:** pitching tech instead of de-risked, promotion-worthy outcomes; even your presence is perceived risk to the sponsor.
- **Evals as a one-time gate:** without ongoing human-in-the-loop feedback the system stops improving, especially on subjective tasks.

## Generic action checklist
- [ ] List every workflow in one target function (finance, HR, procurement, sales, ops) of your business or a client's.
- [ ] Shadow the people doing one high-volume workflow for at least a full working day; record the real steps, not the SOP.
- [ ] Document every exception, edge case, and unwritten routing rule (the "one person's head" knowledge) for that workflow.
- [ ] Classify each step of the workflow: deterministic software / LLM judgment / human approval.
- [ ] Kill or skip candidate workflows that are low-ROI, high-risk, or already automated; rank the rest by volume × improvement.
- [ ] Produce an operating map + ROI priority matrix and review it with the process owner.
- [ ] Choose ONE model ecosystem and ONE agent-building platform and commit to mastering it.
- [ ] Build an agent for the top-priority workflow: loop, tools, guardrails, deliberate context/memory.
- [ ] Add a full audit trail logging every agent action from day one.
- [ ] Enforce JSON-schema outputs with validation; ban free-form text between components.
- [ ] Enumerate failure modes and build explicit handling for the unhappy paths.
- [ ] Assemble a golden dataset from historical records and write an eval suite (data correct / steps followed / matches expert / safe to act).
- [ ] Run the evals, produce a failure-classified report, and fix the top failure causes.
- [ ] Insert a human approval gate before any consequential action; route unsafe cases to a human.
- [ ] Test cheaper models on subtasks and record the accuracy/cost trade-off.
- [ ] Measure the system in the three buckets: revenue uplift, risk mitigation, cost savings.
- [ ] Deploy via shadow mode first, then increase autonomy stepwise into production.
- [ ] Integrate with the existing software stack (ERP/CRM/email); do not introduce replacement systems.
- [ ] Write the two-audience debrief: engineer version (architecture, decisions, accuracy trend) and executive version (problem, outcome, evidence, economics).
- [ ] Pitch the result (or the audit/sprint offer) to a real stakeholder and incorporate their corrections into the next loop.

## Best suited for
**Maps well to:**
- Anyone selling AI implementation/automation services (freelancers, agencies, consultancies) — the audit-first, value-proven engagement model is the core commercial playbook.
- Operators automating their own business's back office (finance, admin, intake, procurement, sales ops) — the tri-layer design, eval discipline, and shadow-mode rollout apply directly at any scale.
- Software engineers or consultants repositioning into the FDE role — the 30-day plan is a literal curriculum.
- Businesses with high-volume, exception-heavy, multi-system workflows (email intake, document processing, data entry across ERP/CRM) — exactly the terrain the playbooks target.
- Organizations with existing entrenched software stacks — the build-on-top/integrate approach is designed for them.

**Maps poorly to:**
- One-off creative or novel work with no repetitive volume — the ROI math (volume × improvement) never clears the bar.
- Teams wanting a "flip the switch" full-autonomy solution — everything here assumes gradual autonomy, human gates, and audit trails.
- Contexts with no historical data and no access to the people doing the work — you can't build golden datasets or discover the real process.
- Pure product startups building horizontal AI tools — the video's thesis is that generic tools lose to customized deployment; this is a services/deployment playbook, not a product one.
- Workflows that are already cheap, automated, or where errors are catastrophic and unreviewable — the speaker explicitly says leave those alone.
