# Marketing Agents Masterclass (GROW your startup)

## Metadata

- **Title:** Marketing Agents Masterclass (GROW your startup)
- **Channel / Speakers:** Greg Isenberg podcast; guest Cody Schneider (co-founder of Graft / graft.com, formerly known for Swell AI and other growth ventures)
- **Length:** 43:59
- **URL:** https://youtu.be/mD7JpNHLT70
- **Date analyzed:** 2026-08-08

## One-paragraph thesis

Marketing agents are to customer acquisition what coding agents are to software: a way to run a full go-to-market motion on autopilot. The episode teaches two concrete, end-to-end agent builds — (1) a signal-based cold-outbound machine that monitors LinkedIn influencer posts, extracts everyone who engages, enriches those profiles into emails and phone numbers via a "waterfall," and then sends and manages cold email plus LinkedIn DM campaigns; and (2) an organic content engine that mines real human conversations (interviews, sales calls, internal comms) for insights, writes and schedules LinkedIn posts across many accounts, and feeds performance data back into the next writing cycle. The underlying philosophy: an "agent" is just custom software (code + a live data stream + an occasional LLM thinking loop) that replicates what a skilled human operator would do — build it once with a coding agent (Claude Code / Codex), deploy it to a cheap always-on server on a cron cadence, and stop paying per-token for actions that plain code can perform.

## Core concepts & frameworks

- **Signal-based (hand-raiser) targeting.** Traditional outbound targets firmographics/demographics/psychographics — who someone *is*. This system targets behavior: a person liking or commenting on niche content is a "hand raise" signaling active interest in that topic right now. Because cold channels are saturated with AI-generated slop and reply rates are collapsing everywhere, intent signals are the differentiator that makes outreach land.

- **The outlier-monitoring principle (80% coverage from a handful of sources).** In any niche, a small number of creator/company accounts produce the outlier posts everyone engages with. Monitoring roughly 10–20 accounts captures ~80% of the industry's engaged audience; chasing complete coverage has sharply diminishing returns. The same principle applies to ad creative: track ~10 human creators, spot their outlier content, and remix it to escape the "agent generates the same ideas in a loop" entropy problem.

- **Waterfall enrichment.** To turn a social profile into contact details, chain enrichment providers from cheapest/most-accurate to most expensive: query provider A for the whole list, send only the misses to provider B, send B's misses to provider C, and so on. This yields ~80% find rates at minimum cost. Aggregators exist that run the waterfall for you from a single profile URL.

- **"An agent is code + a thinking loop + a live data stream."** Don't mystify agents. The job-to-be-done framing: something that finds leads, reaches out, and responds is an agent regardless of framework. Most builds need no agent framework at all — frameworks are usually bloat for these finite problems.

- **Don't put "God in a box."** Giving a general LLM raw access to (say) an ad account fails. Instead, decompose what the skilled human actually did (research angles → make creative → test → prune losers, promote winners) and build purpose-specific software that runs that exact process, invoking the LLM only at the judgment steps.

- **Pay for software creation, not per-action inference.** Use the LLM/coding agent once to *write* the software; run the software on cheap compute. Burning tokens on every repeated action is wasteful and more fragile. Only use inference where genuine thinking is required (ICP-fit judgment, copywriting, inbox replies).

- **Local-first, then deploy.** If a process works in Claude Code / Codex on your machine, it can be deployed to a server and run on an hourly/daily cron. The build path is: prove the script locally → push to cloud → schedule → attach webhooks/data streams.

- **Domain separation for email deliverability.** Never send cold email from your core business domain. Maintain four separated email estates: (1) burner domains for cold outbound, (2) domains for email marketing/newsletters, (3) transactional email (product-triggered, e.g. password resets), (4) the core business domain your team actually works from. Cold volume on the core domain destroys its deliverability.

- **Content mining beats content inventing ("prospect for ideas").** "Write good LinkedIn content" prompts produce mid, flaggable AI slop. Original ideas live in real human conversation — interviews, sales calls, Slack/Notion/Gong transcripts, podcasts. Source material first, then have the LLM write. The best operators don't invent; they identify what the market already engages with and remix it with their own angle — a top post can be reposted roughly every 90 days indefinitely.

- **Market-first product thinking (transferred to content).** Amateurs try to make the market want their idea; pros ask what the market already wants to buy, then build and sell that. Content works identically: mine what has already gone viral, then apply your own spin.

- **Earned media as free ad spend.** LinkedIn impressions cost ~$22 CPM if bought. Every organic post that gets 1,000 impressions is ~$20 of equivalent ad value — and platforms like YouTube actually pay you to build your lead pipeline.

- **Personal brand not required — theme pages.** If nobody on the team wants a personal brand, run topic-based or meme pages (e.g. a "Growth Tactics" account rather than a company-named account) that aggregate value for a niche audience and route attention to your product.

- **The social media manager role is being replaced by the social media *agent* manager.** The new leverage skill is one person orchestrating content creation and management across 10–100 accounts/channels via agents.

## Step-by-step playbooks

### Playbook 1 — LinkedIn engagement-signal cold outbound (the "SDR in a box")

**Phase A: Source the signal accounts (manual, one-time)**
1. Define the target customer and the topic they consume (e.g. "AI marketing" rather than an off-target niche — test that the content surfaced is genuinely what your buyer engages with; a bad topic gives bad signal).
2. On LinkedIn, use search and especially the For You feed (the algorithm surfaces what's relevant to your niche) to find creators AND company/business accounts (e.g. a tooling vendor's page) posting daily about that topic.
3. Build a spreadsheet of 10–20 such accounts. This is enough — outliers within the niche give ~80% audience coverage. The company you're doing this for usually already knows who its customers follow.

**Phase B: Extract engagers (automated)**
4. Get an Apify API key. Apify is a scraping-API marketplace: one key gives access to many maintained scrapers ("actors") for LinkedIn, Twitter/X, etc. Pick a well-maintained LinkedIn actor set (the one recommended is by the developer "API Maestro", which exposes many LinkedIn endpoints).
5. In a coding agent (Claude Code or Codex), with the Apify key stored locally in your working directory, have the agent read the actor's docs and write a script that: takes a post URL → calls the **post reactions** and **post comments** endpoints → returns every engager's LinkedIn profile URL, deduplicated (a single post yielded ~63 raw profiles in the demo).
6. Also wire the **profile posts** scraper: for each tracked account, pull net-new post URLs.
7. Deploy this code to a cloud server and schedule a **daily cron**: check each tracked account for new posts → for each new post, extract all engagers → append profiles to your lead store. (Exact wiring: cron → profile-post scraper → new post URLs → reactions+comments scrapers → deduped LinkedIn profile URLs.)

**Phase C: (Optional but recommended) ICP-fit filter — the thinking loop**
8. Before spending enrichment credits, have an LLM step research each profile and their company (headcount, role, industry, etc.) and judge fit against your ICP definition. Only fits proceed to enrichment; non-fits are discarded.

**Phase D: Waterfall enrichment (profile → email → phone)**
9. Send the full list of LinkedIn profile URLs to **GetLeads (getleads.io)** via API — a B2B contact database; cheapest/most-accurate first. (Illustrative: 50 profiles → ~32 emails found.)
10. Send only the misses (the remaining ~18) to **Apollo** via API (→ maybe 10 more found).
11. Send remaining misses to a third-tier tool — **Origami**, **Prospeo**, or similar. Chain as many tiers as budget allows; ~80% total find rate is achievable. Alternatively, use an aggregator (Origami) that runs the whole waterfall from a single profile URL.
12. For mobile phone numbers specifically, use **LeadMagic** with the same waterfall strategy.
13. **Validate every email** with **MillionVerifier** before sending — classify good / risky (catch-all) / bad, and send cold email only to valid addresses. Provider-supplied emails (GetLeads, Apollo) need this second verification; sending to invalid addresses wrecks deliverability.

**Phase E: Sending infrastructure**
14. Buy burner domains + hosted inboxes for cold email — never your core domain. Providers: **InboxKit**, **Instantly's pre-built inboxes**, or **Hypertide** (the speaker's partner). Cost benchmark: ~10,000 cold emails/month for ~$100/month of inbox infrastructure.
15. Use **Instantly** (from ~$97/month) as the sending platform for cold email campaigns.
16. For LinkedIn DMs, use **HeyReach** or **Botdog** (both have APIs) to run DM campaigns from connected accounts; LinkedIn InMail is also reportedly working very well right now.

**Phase F: Copywriting + inbox-managing agent**
17. Have the agent write per-recipient copy/variables outside the platform (personalized per person, informed by the post they engaged with) and push campaigns into Instantly via its API — the API allows full account monitoring and management.
18. Configure Instantly **webhooks**: on a positive reply, fire a webhook to your cloud-hosted agent.
19. Give that agent a base prompt: full business context + goal ("get people to book a demo at <scheduling link>"). It answers questions, handles objections, and pushes replies toward booking.
20. Connect the agent to your scheduler (**Calendly** or **Cal.com**) so it can verify whether a contact actually booked the discovery call (the optimization target).
21. Program long-horizon follow-ups: e.g. automatically re-engage contacts that went cold every ~6 months. Result: a self-running SDR — finds people by engagement signal, judges fit, enriches, writes, sends, replies, books, and re-warms.

**Phase G: Deployment**
22. Host everything on a simple always-on server — **Railway** or equivalent. At production scale the reference architecture is: data pipeline + warehouse (e.g. **ClickHouse**, open source) feeding live data streams, plus a server the agents deploy onto. No agent framework needed; plain code + LLM calls suffices.

### Playbook 2 — Organic LinkedIn content engine at team scale

1. **Collect source material on a cadence.** Options (any/all):
   - A recurring weekly ~1:1 recorded interview per team member: "tell me everything you learned this week" — no structure needed; works for sales, technical, and any role.
   - Existing recorded sales calls (e.g. Gong transcripts).
   - Internal comms: query Notion, Slack channels (e.g. the sales channel), the codebase — great content is trapped there (e.g. the exact reason a prospect didn't buy becomes a strong post).
   - Podcasts/long-form content — your own or others' (extract insights from any transcript).
2. **Extract insights** from the transcripts/text — the discrete, original ideas grounded in real human conversation. (Never prompt "write good LinkedIn content" from nothing; it yields generic slop and LinkedIn now actively flags AI-generated content.)
3. **Write posts via an LLM API call** using the extracted insights as the substance. A mid-tier model (e.g. Claude Sonnet) is good enough for the writing step.
4. **Schedule via Ordinal** (API and MCP available): connect multiple team LinkedIn accounts; posts are auto-scheduled to each individual's account. Connected accounts can also interact with each other's posts for extra reach.
5. **Close the analytics loop.** Ordinal pulls per-post, per-account LinkedIn analytics. Feed that data stream back to the agent so each writing cycle knows which topics/formats got impressions and "snowballs"/"remixes" the winners (use those words in the prompt) — the LLM thinks on top of the performance data to steer the next round.
6. **Run the proven-winner cadence.** Once a post proves viral, re-run it (with variation) roughly every 90 days. Build a recurring calendar out of proven winners rather than perpetually inventing.
7. **Pair with Playbook 1:** the same engine that makes your team post daily also generates the influencer-post surface area whose engagers you can harvest for outbound — the two motions compound.
8. **No personal brand? Run theme pages.** Create topic-based accounts (e.g. "@GrowthTactics" instead of "@YourAgency") or meme pages that aggregate value for the niche and funnel attention to your product.

### Mini-playbook — Ad-creative entropy loop (mentioned in passing)

1. Track ~10 human creators on Instagram in your niche.
2. Monitor their published content for outliers (new hook formats, new topics).
3. Pull and remix the outliers into your own ad creative, replicating the top-media-buyer loop: research angles → produce creative → test → prune losers, promote winners.

## Tools & stack

| Tool | Used for in the video | Cost / notes |
|---|---|---|
| Claude Code / Codex | Coding agent that writes all the automation scripts and glue code | The harness for everything; "the only agent is a coding agent" |
| Apify | Scraping-API marketplace; LinkedIn post/profile/reactions/comments scrapers (recommended actor author: "API Maestro"), also Twitter/X etc. | One API key across many scrapers; pick actively maintained actors |
| GetLeads (getleads.io) | First-tier waterfall enrichment: LinkedIn profile → email/phone from aggregated B2B database | Cheapest, most accurate first tier |
| Apollo | Second-tier email enrichment for misses | — |
| Origami | Third-tier enrichment; also aggregates the whole waterfall from one profile URL | Team praised as doing excellent work |
| Prospeo | Alternative third-tier enrichment | — |
| LeadMagic | Mobile phone number enrichment | Used heavily by the speaker for phones |
| MillionVerifier | Email validation (good / risky-catchall / bad) before sending | Second verification even after enrichment tools |
| InboxKit | Buying burner domains + hosted cold-email inboxes | Similar pricing to Hypertide; runs frequent sales |
| Instantly | Cold-email sending platform; API for campaign management; webhooks on replies; also sells pre-built inboxes | From ~$97/month |
| Hypertide | Speaker's partner for inbox infrastructure | ~10,000 cold emails/month for ~$100/month infra |
| HeyReach | LinkedIn DM campaign platform (has API) | — |
| Botdog | Alternative LinkedIn DM campaign platform (has API) | — |
| Calendly / Cal.com | Scheduling; agent checks whether contact actually booked | — |
| Ordinal | Multi-account LinkedIn post scheduling (API + MCP) + per-post analytics fed back to the agent | Partner of the speaker; accounts can interact with each other |
| Claude Sonnet (API) | Writing the LinkedIn posts from extracted insights | "Probably good enough" for the writing step |
| Railway (or any server) | Always-on cloud server to deploy the agents/cron jobs | "A server is just a computer that's on all the time somewhere else" |
| ClickHouse | Open-source data pipeline/warehouse for the live data streams agents decide on | Referenced from the prior episode |
| Graft (graft.com) | The guest's company: platform + forward-deployed engineers implementing these exact agents | Pitch at end; best fit fast-growing companies |

## Tactics & heuristics

- Every marketing channel's performance is degrading as AI slop floods each one; behavioral intent signals are the current way to stand out.
- Engagement (like/comment) on niche content is a stronger targeting criterion than any firmographic filter — it is a live hand-raise.
- 10–20 monitored accounts ≈ 80% coverage of an engaged niche; don't over-invest in exhaustive source lists.
- Business/company pages count as signal sources, not just personal creators.
- Use your own For You feed as a research tool — the algorithm has already ranked your niche.
- Waterfall order = cheapest/most-accurate first; only misses cascade down; aggregators can run the waterfall for you.
- Always second-verify emails before sending, even ones from paid enrichment tools.
- Never send cold email from the core domain; keep cold / marketing / transactional / business email on separate domains.
- Personalize copy per recipient via the agent, pushed into the sender by API — not the platform's generic templates.
- Webhook on positive reply → agent replies, answers questions, drives to the booking link, and confirms bookings via the scheduler's API.
- Schedule automated re-outreach to cold leads every ~6 months.
- Buying contact data from data brokers is legal (US); what you *do* with it triggers compliance (CAN-SPAM checklist in the US; EU/GDPR is much stricter) — do your own research, this is not legal advice.
- Skip agent frameworks for finite problems — plain scripts + LLM calls are less bloat and less breakage.
- Reserve LLM inference for judgment steps (ICP fit, copy, replies); use plain code for everything repeatable.
- If it runs locally under a coding agent, it can be deployed to a server on a cron — that's the promotion path.
- Content: source material from real human conversation beats generated ideas; LinkedIn now flags AI-slop content.
- Extract post ideas from sales calls, internal Slack/Notion, Gong transcripts, podcasts — including other people's podcasts.
- Remix proven-viral posts every ~90 days; prospect for winning ideas, then reuse winners as often as the cadence allows.
- Organic LinkedIn ≈ $22 CPM of earned media; even a 500-follower account earning 1,000 impressions/post banks ~$20 of ad value per post.
- Platforms (YouTube etc.) literally pay you to build your lead pipeline — organic can be revenue-positive before any lead converts.
- Don't want a personal brand? Ship theme/topic/meme pages that aggregate niche value and route attention to your product.
- Learn to manage content at scale across many accounts with agents — that's the emerging meta; the classic social-media-manager role is dying.
- Product strategy analog: don't invent what you want the market to buy; find what the market already buys/engages with and build/remix that.

## Metrics & benchmarks

- **~63** engager profiles pulled from a single LinkedIn post (deduplicated) in the live demo.
- **10–20** monitored accounts ≈ **~80%** surface-area coverage of a niche's engaged audience.
- Waterfall illustration: 50 profiles → **~32** emails from tier 1 (GetLeads) → 18 misses to Apollo → **~10** more → remaining 8 to tier 3. Target overall find rate **~80%**.
- Cold email infrastructure: **~10,000 emails/month for ~$100/month** (Hypertide; InboxKit similar).
- Instantly sending platform: from **~$97/month**.
- Total startup cost for the outbound stack: **~$200/month** (inboxes + sending software).
- LinkedIn paid CPM: **~$22 per 1,000 impressions** — the earned-media value benchmark for organic posts.
- A 500-follower account can plausibly earn **~1,000 impressions/post** ≈ ~$20 of equivalent ad value.
- Re-post proven viral content every **~90 days**.
- Automated re-outreach to cold leads every **~6 months**.
- Context: cold-email reply rates are broadly declining across all channels (no specific number given).

## Prerequisites & warnings

**Prerequisites**
- A coding agent (Claude Code or Codex) and basic comfort letting it write/run scripts; a local working directory with API keys saved.
- API accounts: Apify, at least two enrichment providers (GetLeads + Apollo minimum), MillionVerifier, a sending platform (Instantly), and a DM tool if doing LinkedIn DMs.
- Budget: roughly $200/month minimum for sending infra, plus enrichment credits.
- Burner domains and hosted inboxes — set up *before* any sending; these need to exist separately from the core domain.
- A clearly defined ICP and a validated list of 10–20 signal accounts whose audience really is your buyer.
- A cloud server (Railway etc.) for deployment; at scale, a data pipeline/warehouse (ClickHouse) feeding the agents.
- A scheduling link (Calendly/Cal.com) as the conversion endpoint.
- For the content engine: a recurring source-material ritual (weekly interviews, or access to sales-call/Slack/Notion transcripts) and an Ordinal-type multi-account scheduler.

**Failure modes the speakers call out**
- **Wrong signal source = garbage leads.** If the monitored topic isn't what your actual buyer engages with (the "AI for WordPress" example was discarded mid-demo), the whole pipeline outputs noise. Validate the content-audience fit first.
- **Sending to unverified emails nukes deliverability** — always validate, even post-enrichment.
- **Cold email from the core domain destroys the business domain's reputation** — potentially catastrophic and hard to reverse.
- **Compliance is real and jurisdiction-dependent.** US cold email is legal with a CAN-SPAM checklist; the EU is far stricter. The speaker explicitly disclaims legal expertise — do your own research.
- **"God in a box" fails.** Handing an LLM raw account access (e.g. Facebook ads) risks it nuking the account; encode the human process instead.
- **Generated-from-nothing content is slop.** It wastes readers' time and now gets flagged by LinkedIn's AI-content detection; always ground in real source material.
- **Agent-generated creative converges** (entropy problem) without a fresh outside data stream (human creators to mine).
- **Token-maxing is waste.** Paying inference per action is expensive and fragile versus running plain code; frameworks add bloat for simple jobs.
- **Diminishing returns past the outliers** — chasing 100% niche coverage isn't worth it.

## Generic action checklist

- [ ] Define your ICP and the specific topic/content your target buyer actively engages with.
- [ ] Build a spreadsheet of 10–20 LinkedIn creators and company pages posting daily on that topic (use search + your For You feed); sanity-check that their engagers really match your ICP.
- [ ] Get an Apify API key and pick maintained LinkedIn actors for profile posts, post reactions, and post comments.
- [ ] Use a coding agent to write a script: post URL → deduplicated list of engager LinkedIn profile URLs.
- [ ] Extend it to a daily cron: detect net-new posts from tracked accounts → auto-extract all engagers → append to a lead store.
- [ ] Add an LLM ICP-fit filter that researches each profile/company and discards non-fits before enrichment.
- [ ] Set up waterfall enrichment (GetLeads → Apollo → Origami/Prospeo; LeadMagic for phones), cascading only misses down tiers.
- [ ] Validate all emails with MillionVerifier; send only to "good" addresses.
- [ ] Buy burner domains and hosted inboxes (InboxKit / Instantly / Hypertide); keep cold, marketing, transactional, and business email on separate domains.
- [ ] Set up Instantly (or equivalent) and have your agent write personalized per-recipient copy pushed in via API.
- [ ] Set up a LinkedIn DM channel (HeyReach / Botdog) in parallel; consider InMail.
- [ ] Wire reply webhooks to a cloud-hosted inbox agent with a base prompt (context + "book a demo at <link>" goal), connected to Calendly/Cal.com to confirm bookings.
- [ ] Schedule automated re-outreach to cold leads every ~6 months.
- [ ] Deploy everything to an always-on server (Railway etc.); add a data warehouse (ClickHouse) when volume justifies it.
- [ ] Stand up a source-material ritual: weekly recorded interviews with team members, plus mining of sales calls, Slack, Notion, and podcast transcripts.
- [ ] Build the pipeline: transcript → insight extraction → LLM-written posts → auto-scheduled to multiple accounts (Ordinal or similar).
- [ ] Feed post analytics back into the writing loop; instruct the agent to "snowball" and "remix" winning topics.
- [ ] Re-run proven viral posts every ~90 days as a recurring calendar.
- [ ] If personal brands are off the table, launch a topic/theme page for the niche instead.
- [ ] Verify jurisdiction-specific compliance (CAN-SPAM, GDPR, local anti-spam law) before any sending.

## Best suited for

**Maps well to:**
- B2B products and services with an identifiable buyer who consumes niche content on LinkedIn — SaaS, agencies, consultancies, dev tools, professional services.
- Fast-growing companies with a demo/discovery-call sales motion (the whole pipeline optimizes toward a booked call).
- Teams of any size wanting daily multi-account LinkedIn presence without hiring social media managers — including sales teams (e.g. a 7-person team posting daily).
- Solo founders / "software factory" operators comfortable using a coding agent to build and deploy small custom tools.
- US-market outbound, where cold email is legal with CAN-SPAM compliance.
- Anyone with rich internal conversation data (sales calls, support threads, Slack/Notion) sitting unused as content raw material.

**Maps poorly to:**
- B2C businesses whose customers aren't identifiable via professional-network engagement signals (the whole signal layer is LinkedIn-centric).
- EU-focused outbound or other strict-privacy jurisdictions — GDPR makes the cold-email leg largely non-viable as described; the organic content engine still applies.
- Regulated industries where unsolicited contact or data-broker-sourced contact data creates compliance exposure (health, finance) without legal review first.
- Businesses selling via physical presence/local walk-in demand rather than booked calls (though the theme-page organic tactic can still apply).
- Anyone unwilling to maintain deliverability hygiene and separate domain infrastructure — half-doing the cold-email leg actively damages the core domain.
- Teams expecting a no-code turnkey product: this approach assumes you (or a coding agent you drive) build and host custom scripts.
