# Review Generation & Reputation Management Tools — Research Notes

**Context:** Researching SMS/review-automation SaaS tools for a solo AU entrepreneur setting up a review-generation & reputation-management service for trade businesses (plumbers, electricians, etc.) in Australia. Goal: automate review requests (SMS/email) and monitor/respond to Google, Facebook, etc. reviews, with an eye toward later API integration with a custom lead-tracking system.

**Research date:** 29 July 2026. Pricing and plan names for these tools change often and different sources (review-aggregator sites, vendor pages) sometimes disagree — treat all $ figures below as indicative, not contractual, and re-verify directly with the vendor before committing.

**IMPORTANT — no accounts were created.** All research below was done by browsing public marketing/pricing/docs pages only. Signing up for any of these tools, starting a trial, or entering any payment/billing details must be done personally by the business owner — that step was not and could not be performed on their behalf.

---

## 1. NiceJob

**What it does:** Reputation-marketing platform aimed squarely at local/home-service businesses. Core loop: automatically request reviews from customers after a job (via SMS + a short email sequence), monitor reviews across Google/Facebook/etc. in one dashboard, use AI to draft review replies, and turn good reviews into social-proof widgets for the business's website. The Pro tier adds referral campaigns, booking/repeat-business reminders, gifting automation, and competitor SEO insights.

**Pricing (USD, as displayed on nicejob.com pricing page):**
- **Reviews plan:** $75/month
- **Pro plan:** $125/month (marketed as most popular; adds AI review replies, referral campaigns, booking campaigns, competitor insights)
- **Sites add-on** (website builder): $99/month + a one-off $199 setup fee
- Some review sites list an older/legacy "customer-count based" tier structure (e.g., "Grow" $75/mo) — pricing model appears to have been restructured recently, so confirm current tier names directly on nicejob.com before quoting to a client.
- **Free trial:** 14 days, and the pricing page explicitly states "no credit card up front," no contract required.

**SMS support:** Yes — review request campaigns are built around "1 SMS + a 3-email sequence." Marketing copy references "SMS and email" review invitations generally, but no page found specifies international/Australian number support explicitly. Given NiceJob has active Australian customers and reviews on AU Trustpilot (24+ AU reviews found), it appears to work for AU businesses in practice, but this should be confirmed directly with sales/support before relying on it (ask specifically: "do you support Australian mobile numbers for SMS review requests, and is there any extra AU carrier fee?").

**Signup requirements:** Email + account creation to start the 14-day trial; no credit card needed to start the trial (per their own pricing page). A credit card would be needed to convert to paid.

**Integration/API:** Strongest of the three researched here for a developer building a custom system:
- Public REST API (docs at api.nicejob.com/docs/reference/rest) using OAuth2 client-credentials auth, JSON in/out.
- Native **webhooks** — a single webhook endpoint tied to the developer account (not per-company), with subscribable entities including Person, Job, Invoice, Conversation, Story, Photo, Campaign, CampaignEnrollment, Employee, Review, Case, Payment.
- Official **Zapier** integration ("if you integrate with Zapier, you already integrate with NiceJob") plus a marketplace ("connect to 1000s of business apps").
- Requires agreeing to a developer agreement to get API access.

**AU-specific notes:** No AU-specific pricing (USD only) or AU legal entity found. However it has a visible AU customer base and reviews, suggesting it's usable in Australia today. No explicit statement about Spam Act 2003 / AU telco compliance was found — worth asking about directly since Australia has its own spam/consent rules for commercial SMS.

Sources: [NiceJob Pricing](https://get.nicejob.com/pricing), [NiceJob Reviews product page](https://get.nicejob.com/product/reviews), [NiceJob Developers](https://get.nicejob.com/partners/developers), [NiceJob REST API docs](https://api.nicejob.com/docs/reference/rest/index.html), [NiceJob on Zapier](https://zapier.com/apps/nicejob/integrations), [NiceJob Trustpilot (AU)](https://au.trustpilot.com/review/get.nicejob.co), [Capterra AU listing](https://www.capterra.com.au/software/142037/nicejob)

---

## 2. Podium

**What it does:** A much broader "customer communication" platform where reviews are one module among many: a unified inbox (SMS, webchat, Facebook Messenger, Google Business Messages), automated review request workflows triggered after a job/appointment, a review-monitoring dashboard pulling in Google/Facebook/etc., text marketing/bulk messaging, payments, and lead capture. Explicitly markets to home-services trades (plumbing, electrical, HVAC, pest control are named on the AU site).

**Pricing (USD, sources conflict somewhat — reflects how often Podium repackages tiers and that much of it is sales-quote-gated):**
- Multiple recent sources cite different current tier names/prices: e.g. "Core $399/mo, Pro $599/mo, Enterprise $999+/mo" (scaling with number of locations) from one source, vs. "Essentials $289/mo, Standard $449/mo, Professional $649/mo" from another. Podium's own pricing page does not list numbers publicly — it says "talk to our sales team."
- Real-world total cost commonly cited around **$500–$800+/month** once add-ons (extra users, SMS overages, a ~$99/month AI-reply module) are included.
- **Annual contracts are standard** — this is a recurring complaint in third-party reviews and is a meaningful downside versus month-to-month tools.
- No public free trial found; likely a sales-demo-gated signup.

**SMS support:** Yes, SMS/text marketing is core to the product, and Podium has a dedicated Australian marketing site (podium.com.au) explicitly targeting AU home-services trades. However: one comparison source noted "no international calling on Podium Phones," and a competitor comparison (Monster SMS, an AU-based competitor) characterizes Podium as "US-focused, AU compliance manual" regarding the Australian Spam Act 2003 — i.e., Podium doesn't appear to have AU spam-consent rules built in the way a local-built tool would, and AU support/billing runs through a US entity (Podium Corp Inc.) with USD pricing (~$615+ AUD/month equivalent for the cited $399 tier).

**Signup requirements:** No public self-serve signup found — the funnel is "book a demo / talk to sales," which typically means a sales call, business verification, and a signed (often annual) contract with payment details before account activation.

**Integration/API:** Podium references "automations that hook up to 200+ integrations" and a Developer Platform at developer.podium.com, but the developer portal's public page returned no usable documentation content during this research (title only, no visible API reference) — meaning API access likely requires being a customer/partner to get into real docs. Cannot confirm webhook support or API scope from public pages; would need to ask a sales rep directly, ideally before signing an annual contract.

**AU-specific notes:** Podium has genuinely localized marketing (podium.com.au, AU-based support staff mentioned) and explicitly targets AU trades — more AU market presence than NiceJob or GatherUp on paper. But it's still a USD-priced, US-headquartered product, requires an annual contract, and a competitor's comparison page raises a specific (self-interested, so treat with some skepticism) claim that AU Spam Act compliance is "manual" rather than built-in. This is the priciest of the three by a wide margin.

Sources: [Podium.com.au Messaging Platform](https://www.podium.com.au/messaging-platform), [Podium.com.au FAQ](https://www.podium.com.au/article/messaging-platform-faqs), [Podium Pricing (global)](https://www.podium.com/pricing/), [SocialPilot: Podium Pricing Breakdown 2026](https://www.socialpilot.co/reviews/blogs/podium-pricing), [Monster SMS vs Podium comparison](https://monstersms.ai/vs/podium), [SmartCompany: Podium launches in Australia](https://www.smartcompany.com.au/technology/podium-australia-sme/), [Podium Developer Portal](https://developer.podium.com/)

---

## 3. GatherUp

**What it does:** Review-generation and reputation-management platform (also does NPS surveys, review monitoring across 100+ sites, AI-assisted review replies via "SmartReply"/"AutoReply," social sharing of reviews, and reporting with AI topic-tagging). SMS is a first-class, metered feature (not just an add-on).

**Pricing (USD, per gatherup.com/pricing):**
- **Single location:** $99/month
- **Multi-location (2–10 locations):** $60/month per location (further volume tiers for 11+ locations, contact sales)
- **Agency/white-label:** custom quote
- Annual billing saves ~20% vs monthly.
- Every plan includes **3,000 email credits + 300 SMS credits per location/month** baked into the base price — a clearer inclusion than either competitor.
- Optional add-on: promotional SMS marketing campaigns at $10/month per location for an extra 1,000 messages, $0.02/message beyond that.
- **Free trial:** 14 days. A credit card is **not** required to start the trial, but **is required to activate/continue** the account once the trial ends (add card in Admin > Payment Information).

**SMS support:** Yes, SMS is a core, clearly-metered feature ("2-Way SMS Messaging," automated and manual SMS review requests). GatherUp's compliance messaging centers on the US TCPA (Telephone Consumer Protection Act) and double opt-in — no mention of Australia, AU phone numbers, or AU Spam Act 2003 compliance was found anywhere in their public marketing or solutions pages. This is the biggest open question for GatherUp and should be confirmed directly with their support (support@gatherup.com) before relying on it for AU SMS — it's plausible their SMS provider (likely a US aggregator) doesn't support AU mobile numbers at all, or does so without local compliance framing.

**Signup requirements:** Self-serve 14-day trial via app.gatherup.com/trial, no card needed to start; card required to keep the account active after trial.

**Integration/API:** Best-documented "developer-friendly" claims of the three for a lightweight custom integration: pricing/marketing pages explicitly state support for **"API, Zapier and Webhooks,"** plus one-click CRM/POS integrations. Detailed API reference documentation was not directly accessed in this research pass (would need a GatherUp account/API key to see full docs) — but the explicit mention of all three integration primitives (REST API, Zapier, webhooks) on public pages is a good sign for later connecting it to a custom lead-tracking system.

**AU-specific notes:** No AU pricing, no AU entity, no AU compliance mentions found — of the three, this is the one with the least evidence either way about Australian SMS support. Worth a direct pre-sales question before evaluating further: "Can GatherUp send/receive SMS to Australian (+61) mobile numbers, and is AU Spam Act 2003 consent handling supported?"

Sources: [GatherUp Pricing](https://gatherup.com/pricing), [GatherUp SMS solutions page](https://gatherup.com/solutions/sms/), [GatherUp FAQ](https://gatherup.com/faq/), [GatherUp free trial](https://app.gatherup.com/trial), [Capterra: GatherUp](https://www.capterra.com/p/239159/GatherUp/)

---

## Comparison & Recommendation

| | NiceJob | Podium | GatherUp |
|---|---|---|---|
| Entry price (USD/mo) | $75 | ~$289–$399+ (quote-gated, conflicting sources) | $99 (1 location) |
| SMS included | Yes, core to review campaigns | Yes, core product | Yes, 300 SMS credits/location/mo included |
| Confirmed AU presence | AU customers/reviews exist; no AU pricing/entity | Dedicated podium.com.au site, AU-targeted marketing, AU support staff | No AU-specific evidence found |
| AU compliance (Spam Act) evidence | Not found — ask directly | A competitor claims it's "manual," not built-in | Not found — ask directly; only US TCPA referenced |
| Contract | No contract, cancel anytime (per pricing page) | Annual contract standard | Monthly or annual (20% discount annual) |
| Free trial, no card | Yes, 14 days | Not found (sales-demo gated) | Yes, 14 days (card needed only to continue) |
| API / webhooks / Zapier | Strongest: public REST API + OAuth2, webhooks, Zapier, dev agreement required | Claims 200+ integrations + developer.podium.com, but public docs not accessible without being a customer | Claims API + Zapier + webhooks, but public reference docs not directly viewed |
| Best fit | Solo/small trade businesses wanting an affordable, self-serve, review-focused tool with real API access | Businesses wanting an all-in-one comms/lead/payments platform and willing to pay more + sign an annual contract | Businesses wanting more generous built-in SMS volume per dollar and multi-location scaling |

**Recommendation for this use case (solo AU entrepreneur reselling review-generation to trade businesses):**

- **Start with NiceJob** as the primary candidate to trial personally: lowest cost of entry, no-card 14-day trial, no contract lock-in, and — importantly for later building a custom lead-tracking system — the most concrete public API + webhook documentation of the three. It's purpose-built for exactly this trade-business review-generation use case. The main unknown to verify directly with NiceJob before committing is confirmed AU SMS deliverability/pricing and any AU compliance guarantees.
- **GatherUp is a reasonable second option to trial in parallel**, mainly because its SMS credits are clearly bundled into the base price (300/location/month) rather than opaque, and it also claims API+webhooks+Zapier — but its total lack of any visible AU-specific information means the very first step should be an email to their support confirming AU (+61) SMS actually works before spending trial time on it.
- **Podium is likely overkill and overpriced for a solo operator's early-stage service** — it's a genuinely more full-featured platform (unified inbox, payments, lead capture) and does have real AU market presence/support, but the annual contract, sales-gated pricing, and cost (likely $400–$800+ AUD-equivalent/month) make it a poor fit until/unless the business has multiple paying clients and needs the extra channels (webchat, payments) beyond review generation. Worth revisiting later as an upsell option for larger trade-business clients, not as the starting tool.

**A note on a possible fourth option not deep-dived here:** the AU-based "Monster SMS" (monstersms.ai) surfaced in this research as a locally-built, AUD-priced, Spam-Act-compliant SMS platform explicitly positioned against Podium for the Australian market. It appears to be SMS/marketing-focused rather than a full review-generation+monitoring suite, so it wasn't treated as a like-for-like candidate here, but it may be worth a quick look separately if AU-native compliance and local support turn out to be dealbreakers for the three tools above.

## Reminder on account creation

None of NiceJob, Podium, or GatherUp were signed up for as part of this research — only public marketing, pricing, and documentation pages were reviewed. The business owner will need to personally create any trial/paid account and enter their own payment details for whichever tool(s) they choose to move forward with; that step cannot be done on their behalf.
