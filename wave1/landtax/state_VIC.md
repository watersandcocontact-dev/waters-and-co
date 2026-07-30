# VIC — Land Valuation Objection Process

**Researched:** 2026-07-29. **Follow-up verification pass: 2026-07-30.**
**Caveat:** Deadlines, forms, portal URLs, and processing timeframes below were verified against official .gov.au sources (land.vic.gov.au, sro.vic.gov.au, vcat.vic.gov.au) on the research date, but state government processes and forms change periodically. Re-verify all details (especially current deadlines, form versions, and fees) directly against the official sources below before advising any client. **Update (2026-07-30):** the primary land.vic.gov.au objection page, which returned HTTP 403 on direct fetch in the original research, was successfully retrieved on the follow-up pass via a text-extraction proxy (r.jina.ai) — see Escalation Path and confirmation notes below. Direct WebFetch of land.vic.gov.au still returns 403; use a proxy or a real browser if re-verifying manually.

---

## Authority

- **Valuer-General Victoria (VGV)** — the sole statutory valuation authority responsible for annual valuations of all land in Victoria for rating and land tax purposes (councils are no longer the valuing authority, though they issue the combined rates/valuation notice and often act as the initial point of lodgement for rates-related objections).
- **State Revenue Office (SRO) Victoria** — administers land tax; land tax valuation objections are lodged with the SRO, which forwards them to the VGV for determination.
- **Local councils** — issue the annual Valuation and Rates Notice (which includes the VGV-determined value) and receive/forward objections relating to that notice.

## Deadline

- **2 months (60 days)** from the date the Valuation and Rates Notice (council) or land tax assessment notice (SRO) was issued.
- For land tax: "The Commissioner of State Revenue has no discretion to accept late objections" — this appears to be a strict/hard deadline for SRO-administered land tax valuation objections.
- Council/rates valuation objections: council cannot process objections lodged after this window.

## How to Object

- **Council rates valuation objections:**
  - Many (78+) participating councils accept objections electronically via the state **Rating Valuation Objections Portal**: https://ratingvaluationobjections.vic.gov.au/
  - Otherwise, obtain a pro-forma objection form from your council, or use the generic Valuer-General Victoria version if the council cannot supply one.
  - Completed forms and attachments are posted or submitted to the **council** that issued the notice (not directly to VGV).
- **Land tax valuation objections:**
  - Lodge via the **SRO's online Land Valuation Objections Portal**: https://www.e-business.sro.vic.gov.au/objections/login
  - Requires assessment notice number, customer number, detailed reasons, property details, and joint owner information.
  - The SRO forwards the objection to the VGV, who determines it.

## Evidence / Grounds Accepted

- The value itself is incorrect (too high or too low).
- Interests in the land have been incorrectly apportioned.
- Separate parcels have been inappropriately combined into one valuation, or one parcel inappropriately split.
- Property description, dimensions, or area details are incorrect.
- Objectors are expected to support a contention that a valuation is too high or low with **evidence of sales and rents of comparable properties**.

## What Happens After Lodging

- Land tax: SRO forwards the objection to the VGV, who has up to **4 months** to issue a written decision; if the VGV recommends a change, a further **2 months** may be needed to confirm the adjustment. Total process commonly takes **6+ months**.
- Rates/land tax must still be paid by the due date while an objection is pending — interest accrues daily on unpaid amounts; overpayments are refunded with interest if the objection succeeds.

## Escalation Path

- **VCAT (Victorian Civil and Administrative Tribunal) — Land Valuation list**, under **s22(1) of the *Valuation of Land Act 1960***. If, after the valuer/Valuer-General has reviewed the objection, the objector is still dissatisfied, they may apply to VCAT to review the decision.
- **VCAT application deadline — RESOLVED 2026-07-30:** directly fetched from VCAT's own "Review of a decision on valuation of land" page (`https://www.vcat.vic.gov.au/case-types/land-valuation/review-of-a-decision-on-valuation-of-land`): **"You must apply within 30 days of the notice of the decision being given."** This confirms the deadline runs from the **objection decision date** (i.e., the Valuer/Valuer-General's decision on the objection), **not** from the original rates/valuation notice date as the previously-flagged secondary source suggested. The 60-day figure in the old flag was incorrect for the VCAT step specifically — 60 days is the deadline for the *original objection* (to council/SRO), while the *further VCAT application*, once an objection decision has issued, is a separate 30-day window. Process before applying: lodge objection with the valuation authority → receive the objection decision → prepare the VCAT application (proposed correct value, grounds, supporting valuer/comparable sales evidence) → lodge online with VCAT → send a copy to the valuation authority within 7 days of lodging → attend a compulsory conference or hearing.
- Applicants must state what they believe the correct value is and support it with comparable sales/rental evidence.
- **VCAT filing fee — still unverified after a second research pass.** VCAT's fee schedule for the Land Valuation list is only exposed through an interactive JavaScript fee-calculator tool on vcat.vic.gov.au/fees (select case type + concession/standard/corporate rate) — this could not be extracted by any automated method tried (direct fetch, text-extraction proxy, or downloading/parsing the *Victorian Civil and Administrative Tribunal (Fees) Regulations 2026* Regulatory Impact Statement docx, which contains no fee table in extractable form). What was confirmed: VCAT fees changed under the new *Victorian Civil and Administrative Tribunal (Fees) Regulations 2026*, effective **27 June 2026**, with a further annual fee-unit indexation on **1 July 2026** (fee unit rising from $16.81 to $17.27, a 2.75% increase); fee categories are concession (~11% of standard), standard, and corporate (100%) rates. The specific Land Valuation list dollar figure (the ~$200 previously cited) was **not** confirmed or found in either direction — **this needs the VCAT online fee calculator run directly (vcat.vic.gov.au/fees, select "Land valuation") or a phone call to VCAT (1300 01 8228) rather than further web searching**, since the figure lives behind a JS tool that text-based fetching cannot reach.

## Official Links

- Objecting to a rating valuation (Valuer-General Victoria / DEECA land.vic.gov.au): https://www.land.vic.gov.au/valuations/valuations-for-rate-and-land-tax/objecting-to-a-rating-valuation (still returns 403 on direct automated fetch as of 2026-07-30; successfully read via text-extraction proxy on the follow-up pass — content confirmed, see below)
- Object to site or capital improved valuation for land tax (SRO): https://sro.vic.gov.au/owning-property/land-tax/managing-your-land-tax/objections-and-refunds/object-site-or-capital-improved-valuation-your-land
- SRO Land Valuation Objections Portal: https://www.e-business.sro.vic.gov.au/objections/login
- Rating Valuation Objections Portal (councils): https://ratingvaluationobjections.vic.gov.au/
- SRO — Appeals: https://www.sro.vic.gov.au/about-us/objections-and-appeals/appeals
- VCAT — Review of a decision on valuation of land: https://www.vcat.vic.gov.au/case-types/land-valuation/review-of-a-decision-on-valuation-of-land
- VCAT — Land valuation case type overview: https://www.vcat.vic.gov.au/land-valuation

## Unverified / Flag for Follow-up

- **Primary land.vic.gov.au page — RESOLVED 2026-07-30.** Direct WebFetch still returns 403 Forbidden, but the page was successfully retrieved via a text-extraction proxy (r.jina.ai) on the follow-up pass. Confirmed content matches this file: authority (council for rates, SRO for land tax), 2-month/60-day deadline (Valuation of Land Act 1960, referenced generally — the page cites "Section 17: Grounds for objection" and "Section 22: The appeals process" as the relevant statutory sections), written objection requirement, and the two lodgement channels (Objections Portal for 78 participating councils, or paper form to council). No fee is mentioned on the page for lodging the initial objection, consistent with the rest of this file.
- **VCAT deadline basis — RESOLVED 2026-07-30.** Confirmed directly from vcat.vic.gov.au: the 30-day VCAT application window runs from the **objection decision date**, not the original notice date. See Escalation Path above.
- **VCAT filing fee (~$200) — still unconfirmed after a second research pass.** The figure lives behind an interactive JS fee calculator on vcat.vic.gov.au/fees that no automated text-based tool (direct fetch, proxy fetch, or parsing the Fees Regulations RIS docx) could extract. This is a case where the web research approach has been exhausted — resolving it needs either a human to manually run the VCAT fee calculator in a browser, or a phone call to VCAT (1300 01 8228).
