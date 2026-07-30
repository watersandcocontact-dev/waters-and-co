# AI Missed-Call Reception Platforms — Research for AU Reseller/Multi-Client Use

**Research date:** 2026-07-29
**Context:** Evaluating platforms to resell/manage as an "AI missed-call reception" service for Australian trade businesses (plumbers, electricians, etc.) — AI answers/texts back missed calls, qualifies the lead, and can book jobs. Business owner is a solo operator managing this for multiple small-business clients and has a custom lead-tracking webhook ready to receive intake/call data.

**Important note up front:** No accounts were created and no payment details were entered anywhere during this research. All pricing/feature details below come from vendor websites and third-party review sites via web search on 2026-07-29 and should be re-verified at signup, since these products change pricing and features frequently. Where a detail could not be confirmed, it is flagged explicitly rather than guessed. **The business owner must personally create any account, agree to terms, and enter payment details — this is required for the "explicit permission" / "prohibited action" rules Claude operates under (creating accounts and entering payment credentials cannot be done on the user's behalf).**

---

## How "missed-call" setup actually works (applies to all platforms below)

None of these require full number porting in the traditional sense to get started. The standard model is **conditional call forwarding**: the tradie keeps their existing AU mobile/landline number and sets carrier-level "forward on no-answer/busy" to a number the AI platform gives them (usually a US number unless the vendor issues a local AU number). Full Twilio-based number porting (moving the AU number's carrier record entirely) is a heavier, optional step mainly relevant to the Retell-style DIY stack. This distinction matters for AU because forwarding an AU number to an overseas (US) number can incur international forwarding charges from the client's own telco — worth checking with each client's carrier.

---

## 1. Smith.ai (AI Receptionist product)

**What it does:** Originally a human virtual-receptionist company, Smith.ai now offers a standalone "AI Receptionist" product (separate from its human "Virtual Receptionist" service) that answers calls, has natural conversations, captures lead/intake info, can transfer or text back, and includes call recording, transcription, and summaries on all tiers. It also offers live-chat/web chat AI.

**Pricing (AI Receptionist, per smith.ai/pricing/ai-receptionist):**
- **Free plan:** $0/month, 25 calls included, $3.00/call overage — genuinely usable as a free trial to test the product.
- **Pro plan:** $150/month, 75–300 calls (tiered), ~$2.00–$1.67 per call, overage ~$2.50–$2.17/call.
- **Enterprise plan:** $500/month, 300–1000+ calls (tiered), ~$1.67–$1.50 per call, overage ~$2.17–$2.10/call.
- No setup fee found. 30-day money-back guarantee; month-to-month, no long-term contract.
- Note: search results also surfaced older/different figures for Smith.ai's separate hybrid human "Virtual Receptionist" product (from ~$300/mo) — don't confuse the two products when comparing prices.

**Setup complexity:** DIY dashboard, no coding required. Call forwarding setup on the client's existing number. Positioned as fairly quick to configure relative to the developer-first platforms.

**Transcription/tagging + webhook/API:** Recording, transcription, and summaries are included across all tiers. A "Developer API" is referenced, plus Zapier integration is confirmed (5,000+ app connections) for pushing lead data into external systems — this should be able to feed the owner's custom webhook via Zapier, or potentially more directly via the API (exact webhook-push documentation wasn't independently confirmed — verify in docs.smith.ai before committing).

**Reseller/white-label/multi-client support:** This is Smith.ai's strongest point for this use case. It has three separate formal partner tracks: a **Referral/Affiliate program**, an **Agency Reseller program** (earn commission on resold accounts, with a dedicated **Partner Portal** — "one account to manage your clients" — giving access to settings, management tools, data, and invoices across all resold client accounts), and a **Wholesale program** for bulk/agency-rate pricing. This multi-client partner portal is exactly the "manage this for multiple client businesses" pattern the owner needs.

**AU-specific caveats:** Smith.ai is a US company; search results describe it as offering AU businesses "local number options" and 24/7 coverage, but this could not be independently confirmed against an official AU numbers/coverage page — verify directly whether they issue genuine Australian local numbers or only forward to a US-based system. Its (separate) human-staffed receptionist coverage is North America-based, not AU-based, which is irrelevant to the pure-AI product but worth knowing if ever upgrading a client to hybrid AI+human.

---

## 2. My AI Front Desk (MyAIFrontDesk)

**What it does:** AI phone receptionist plus SMS/chatbot follow-up, built-in CRM, and (on higher tiers) multilingual support. Positions itself explicitly for agencies reselling to small-business clients.

**Pricing (myaifrontdesk.com/pricing):**
- **Basic:** $20/mo ($16/mo billed annually) — 0 voice minutes included, 40 SMS/mo, 10 chatbot conversations/mo (essentially a chat/SMS-only entry tier, not useful alone for phone answering).
- **Business-in-a-Box:** $99/mo ($79/mo annually) — 200 voice minutes/mo, 400 SMS/mo, 100 chatbot conversations/mo. Overage ~25 credits/min (1 credit = $0.01, i.e. ~$0.25/min).
- **Partner/Enterprise:** custom pricing, lower per-minute overage (as low as 7 credits/min ≈ $0.07/min).
- **7-day free trial**, no credit card required to start.
- **Reseller/wholesale pricing:** separate from retail — resellers reportedly buy at a flat **$54.99/receptionist wholesale** (plus $0.12/min over plan limits) and set their own client-facing price; multiple sources describe agencies reselling at $250–$500+/month per client for 70–90% gross margin. Reseller minimum commitment reported as low as 5 accounts.

**Setup complexity:** DIY, no-code dashboard ("zero code" deployment per their white-label page). Standard conditional call-forwarding setup (QR-code "instant setup" or manual carrier-specific instructions).

**Transcription/tagging + webhook/API:** Transcription was not explicitly confirmed on the pricing page fetched. **API access is restricted to Partner/Enterprise plans only** — Basic and Business-in-a-Box do not get API access, which matters a lot for pushing data into the owner's custom webhook; a Partner-tier account would likely be required to get proper integration access.

**Reseller/white-label/multi-client support:** This is a core, explicitly marketed feature ("Frontdesk Partner" white-label program): full branding (logo, colors, custom domain), a dedicated reseller dashboard to manage unlimited client sub-accounts plus separate client-facing dashboards ("two dashboards, one platform"), Stripe rebilling built in for automated client billing/subscriptions, and partner support/sales materials. This is arguably the most turnkey reseller/agency package of the group.

**AU-specific caveats:** Described in its own marketing as a "US-based service." Whether it issues or supports genuine Australian local numbers, or only supports forwarding, could not be confirmed from available pages — this needs direct confirmation from MyAIFrontDesk before onboarding AU clients. No AU-specific compliance information was found.

---

## 3. Dialzara

**What it does:** AI phone answering/receptionist with conditional call forwarding, SMS follow-up agent, and an optional website chatbot; White Glove onboarding with a "prompt engineer" on every paid plan.

**Pricing (dialzara.com/pricing):**
- **Lite:** $29/mo — 60 minutes included, $0.48/min overage.
- **Pro:** $99/mo — 220 minutes, $0.45/min overage.
- **Plus:** $199/mo — 500 minutes, $0.40/min overage.
- **Elite:** $349/mo — 1,000 minutes, $0.35/min overage.
- Add-ons: SMS Agent $19/mo + $0.05/AI message; standalone website chatbot $39/mo (or bundled cheaper/free with a voice plan).
- **7-day free trial** on inbound voice plans, no setup fees.
- **White Label/Partner Program:** listed with custom pricing, multi-tenant dashboards, and dynamic (per-client) branding — exact price not published, requires contacting sales.

**Setup complexity:** DIY, described as "live in about 15 minutes" — onboarding Q&A, import website/docs for AI knowledge, test via chat/phone, then forward the number. Free number porting offered for US/Canada numbers (not clear this extends to AU numbers — see caveat below); otherwise standard conditional forwarding of the client's existing number.

**Transcription/tagging + webhook/API:** Native connectors for popular CRMs plus Google Calendar/Outlook sync are confirmed; everything else goes through **Zapier, Make, or webhooks** — this is a direct, explicit fit for pushing structured call/lead data into the owner's custom webhook. Call-tagging specifics weren't confirmed in the pages reviewed — verify during trial.

**Reseller/white-label/multi-client support:** Confirmed as an explicit product (White Label / Partner Program) aimed at agencies and answering-service operators, with multi-tenant dashboards and per-client branding, but pricing is not public — needs a sales conversation.

**AU-specific caveats:** This is the one platform in this set with an **explicit, sourced claim of Australian number support**: "Dialzara supports US, UK, Canada, and Australian phone numbers... international numbers (UK, AU, NZ) are available on request" — i.e., AU numbers aren't self-serve in the dashboard but can be requested through support. Worth confirming pricing/turnaround for AU numbers directly before committing a client.

---

## 4. Retell AI + Twilio (developer/DIY stack)

**What it does:** Retell AI is a voice-AI infrastructure/API platform (not a finished consumer product) — you build the conversational agent and pair it with a telephony layer, normally Twilio, to get a real phone number. This is the "usable via Twilio number porting" option in the brief: genuinely full control over call flow, data capture, and where data gets sent, at the cost of needing technical setup.

**Pricing:**
- Pay-as-you-go, no platform/subscription fee: **$0.07–$0.31/minute all-in** depending on voice engine, LLM, and telephony choice (rough breakdown: Retell voice infra ~$0.055/min, TTS ~$0.015/min, LLM $0.003–$0.16/min depending on model, telephony ~$0.015/min if using Retell-managed Twilio, or $0/min in the telephony line if you bring your own Twilio/SIP account and pay Twilio directly).
- **$10 in free credits** on signup (functions as a free trial), no contracts/minimums.
- 20 concurrent calls free; extra concurrency $8/month each.
- International calls to/from Australia are supported via Retell's own numbers but billed at country-specific international rates ($0.03–$0.80/min) — using an **AU-local Twilio number** (confirmed available for purchase directly in the Twilio console, subject to standard AU regulatory/address requirements for certain number types) avoids that international surcharge and gives the client a genuine local AU number.

**Setup complexity:** Highest of the four — this is a DIY technical build (Retell agent config + Twilio number provisioning + call-flow/webhook logic), not a plug-and-play SaaS dashboard. Well suited to a technically inclined solo operator who wants precise control, less suited if the owner wants to avoid any technical setup.

**Transcription/tagging + webhook/API:** This is the platform's core strength — it's an API/webhook-native product built for exactly this kind of integration (inbound call webhooks, SMS integration referenced in docs), meaning it's the most flexible for wiring straight into the owner's custom lead-tracking webhook with no vendor-imposed data format. Exact tagging capabilities weren't independently confirmed and would need checking in Retell's docs.

**Reseller/white-label/multi-client support:** **Retell itself does not ship native multi-tenant/white-label/reseller functionality** — no sub-accounts, no client billing, no branded portal out of the box. Agencies wanting that layer typically bolt on a third-party wrapper (e.g., VoiceAIWrapper, Voicerr.ai, or "Retell Certified Partners" like Awaz) that adds branding, client portals, sub-account isolation, and billing on top of the Retell API — or the owner builds a lightweight version of this themselves (e.g., one Retell account, per-client agent configs, and a simple internal spreadsheet/dashboard). For a solo operator managing a handful of trade-business clients, running everything under one Retell account without a fancy branded portal is a realistic option, but it's meaningfully less "resale-ready out of the box" than Smith.ai, MyAIFrontDesk, or Dialzara.

**AU-specific caveats:** Twilio confirmed to sell local Australian phone numbers (voice + SMS-capable mobile-type numbers) directly through its console, subject to Australian regulatory bundle/address requirements for certain number types (e.g., toll-free numbers need a local AU address on file). This is the cleanest path to a genuinely AU-local number among the four platforms, but it also means the owner is directly responsible for Twilio's AU regulatory compliance steps rather than a vendor handling it invisibly.

---

## Comparison Table

| Platform | Price from | Setup complexity | Webhook/API support | Reseller-friendly |
|---|---|---|---|---|
| **Smith.ai (AI Receptionist)** | Free (25 calls/mo); $150/mo Pro | DIY dashboard, no code | Zapier confirmed; API referenced but not fully verified | Yes — formal Reseller + Wholesale programs with a dedicated multi-client Partner Portal |
| **MyAIFrontDesk** | $20–$99/mo retail; ~$54.99/mo wholesale for resellers | DIY dashboard, no code, QR/carrier-guided forwarding | Zapier/CRM-style, but **native API gated to Partner/Enterprise tier only** | Yes — explicit white-label program: branded dashboards, unlimited client sub-accounts, built-in Stripe rebilling |
| **Dialzara** | $29/mo (60 min) | DIY dashboard, ~15 min setup | Native CRM connectors + Zapier/Make/webhooks (best documented "webhook" language of the no-code options) | Yes, but partner-tier pricing not public — requires a sales call |
| **Retell AI + Twilio** | ~$0.07–$0.31/min, $10 free credit, no subscription fee | High — developer/API build, own Twilio provisioning | Best-in-class — API/webhook-native by design | No native reseller layer — needs a third-party white-label wrapper or a self-built lightweight multi-client process |

*(All prices in USD as published by vendors; convert to AUD and add margin when pricing clients. None confirmed to bill natively in AUD.)*

---

## Recommendation

For a solo AU entrepreneur who wants to manage this across several trade-business clients without a heavy dev build, **start with MyAIFrontDesk or Smith.ai as the primary candidate to trial**, in that order of priority:

- **MyAIFrontDesk** has the most complete, cheapest, and most explicitly "reseller-ready" package (branded multi-client dashboards, sub-accounts, built-in billing, ~$55/mo wholesale cost against $250–$500+/client retail pricing others report) — but the free trial only covers the retail plans, and full API/webhook access requires stepping up to a Partner/Enterprise tier, so budget for that before assuming the custom webhook will connect cleanly. AU number support is unconfirmed and must be checked directly with them first.
- **Smith.ai** is the safer, more established choice with a genuine no-cost tier to test call quality and transcription before spending anything, plus a real Partner Portal for multi-client account management — worth trialling in parallel, especially if call-quality/reliability matters more than rock-bottom cost.
- **Dialzara** is worth a look specifically because it's the only platform here with an explicitly sourced claim of native Australian number support and clean webhook language, but its white-label/partner pricing isn't public, so it needs a direct sales conversation before it can be compared apples-to-apples on cost.
- **Retell AI + Twilio** should be kept as a fallback/upgrade path rather than the starting point: it gives the most control and the cleanest AU-local-number story via Twilio, and the cheapest raw usage cost, but there's no out-of-the-box reseller layer, so it only makes sense once the owner either wants to invest in building that layer (or pay for a wrapper like VoiceAIWrapper/Voicerr) or is comfortable running a handful of clients manually under one account.

Practical next step: sign up for Smith.ai's free tier and MyAIFrontDesk's 7-day trial personally (using the owner's own email/payment details — this cannot be done on the user's behalf), run one or two real AU trade-business call scenarios through each, and check concretely (a) whether transcripts/lead data can reach the custom webhook without a paid tier upgrade, and (b) whether an AU caller number can actually be provisioned or whether forwarding a client's existing AU number is the only option.

**Reminder:** all pricing above is current only as of the 2026-07-29 web search and is USD unless noted; verify AUD pricing, GST treatment, and current trial terms directly with each vendor before quoting clients.
