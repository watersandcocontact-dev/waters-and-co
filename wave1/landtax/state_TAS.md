# Tasmania (TAS) — Land Valuation Objection Process

*Researched: 2026-07-29. Government processes, forms, and deadlines can change — re-verify all details against official sources before using this for client advice.*

## Authority

- **Valuations are issued by the Office of the Valuer-General (OVG)**, part of the Department of Natural Resources and Environment Tasmania (NRE Tas — formerly DPIPWE). The OVG determines statutory **Land Value**, **Capital Value**, and **Assessed Annual Value (AAV)** for all rateable/taxable land in Tasmania under the *Valuation of Land Act 2001* (Tas).
- **Objections to a valuation are also handled by the OVG** (not by councils and not by the State Revenue Office). This is confirmed on the State Revenue Office Tasmania (SRO) site: "Land values used for land tax notices of assessment are obtained from the Office of the Valuer-General (OVG), and only the OVG has the authority to determine land values and consider objections about valuations. The Commissioner of State Revenue does not set the valuation of land." (sro.tas.gov.au)
- **Land tax** itself is administered separately by the **State Revenue Office Tasmania (SRO)**, based on the OVG's land value multiplied by an adjustment factor. If a client disputes the *land tax assessment* (e.g., adjustment factors, exemptions, calculation), that objection goes to the SRO. If they dispute the *underlying valuation figure*, that objection must go to the OVG. This distinction matters for client-facing service design — the two objection pathways are different.
- Council rates and the Fire Service Levy also use OVG-issued values (Capital Value / AAV and an Adjusted Fire Service Value derived from AAV) as their base, but again, any dispute about the value itself is lodged with the OVG, not the council or Tasmania Fire Service.
- I could not find an official OVG page that separately defines "Adjusted Fire Service Value" (AFSV) as a distinct statutory value type alongside Land Value/Capital Value/AAV — flagged below in Notes.

## Deadline

- **60 days after receipt of the Notice of Valuation** (or after provision of a valuation certificate under s.44), per **s.28(1) of the Valuation of Land Act 2001 (Tas)**: an owner dissatisfied with a valuation may, "within 60 days after receipt of a notice under section 27 [or] the provision of that certificate," lodge an objection with the Valuer-General stating fully and in detail the grounds relied on.
- **Exceptions/extensions:** The Act (ss. 28(5) and 30(8)) allows a court to extend this time limit in certain circumstances — i.e., a late objection is not automatically barred, but extension is a matter for the Land Valuation Court, not an administrative discretion of the OVG. Exact grounds for extension were not fully extractable from the legislation text in this research pass — flagged in Notes.
- Note: the OVG's own web page on objections (nre.tas.gov.au) directs readers to the Act for the specific time limit rather than restating the 60-day figure explicitly on the page itself, so the deadline should be sourced to the Act (confirmed above) and cross-checked against the notice itself, which should state the response-by date.

## How to Object

Two lodgement channels, both referenced on the official OVG page "Objecting to a Statutory Valuation" (nre.tas.gov.au):

1. **Online — OVG Valuation Portal (VISTAS):**
   `https://valuation.dpipwe.tas.gov.au/VISTAS/portal/form/objection`
2. **Paper form — "Objection to Valuation Form"** (Word doc), downloadable from the OVG site, returned by:
   - **Email:** ovg@nre.tas.gov.au
   - **Post:** Office of the Valuer-General, GPO Box 44, Hobart TAS 7001
   - **Phone (general enquiries):** 03 6165 4444

An "Owner's Guide" PDF ("Objection-to-Valuation.pdf") is also linked from the OVG page and appears to walk owners through the process, though its content could not be extracted as readable text during this research (binary/PDF stream issue) — worth a follow-up manual check before building client-facing copy from it.

The objection must "state fully and in detail" the grounds relied on (Act s.28(1)), i.e., a bare assertion that the value is "too high" without detail/evidence is not sufficient.

## Evidence / Grounds

The *Valuation of Land Act 2001* (s.29) and the OVG's own page both state the objection **"may be made on any one or more of the following grounds, but on no other ground"** — i.e., this is an exhaustive/closed list:

1. That the **land value, capital value, or assessed annual value** assigned to the land is **too high or too low**.
2. That the **apportionment of the valuation among the interests** of two or more owners of the land is not correct.
3. That the **apportionment of the valuation** (generally) is not correct.
4. That **lands that should be included in one valuation have been valued separately**.
5. That **lands that should be valued separately have been included in one valuation**.
6. That the **person named in the Notice of Valuation is not the owner** of the land to which the notice relates.
7. That the **area, dimensions, or particulars of the land are not correctly described**.

The OVG page explicitly warns: **"No other basis for an objection can be accepted, for example an owner cannot object about their land tax or local council rates."** This is an important client-facing caveat — objections to the *tax/rates bill amount* itself (as opposed to the underlying valuation) are out of scope and must be redirected to SRO or the council.

**Evidence to support an objection** (per the OVG page): "comparable sales/lease evidence, details of other parties with a property interest etc." — i.e., comparable sales/lease evidence is the primary accepted evidence type for the "value too high/low" ground; ownership documents for the "not correctly named owner" ground; survey/title particulars for the "incorrectly described" ground.

## Escalation Path

1. **Lodge objection with the OVG** within 60 days of receiving the Notice of Valuation (s.28).
2. **OVG assesses and decides the objection.** The OVG page states: **"It can take up to 6 months to finalise objections, depending on the complexity of the issues."**
3. **If dissatisfied with the OVG's decision**, the objector may require the Valuer-General to refer the matter for independent determination (Act s.30(3)–(4)), within a further statutory window (30 days, per this research — flagged for confirmation), to either:
   - The **Land Valuation Court** (for any valuation amount), or
   - The **Supreme Court of Tasmania** (where the valuation exceeds a prescribed monetary threshold set in the regulations).
   - Arbitration may also be available if agreed by the parties.
4. **Further appeal:** Decisions of the Land Valuation Court may be appealed to the **Supreme Court of Tasmania by way of rehearing** (Act s.40(1)). Except where otherwise provided, the Land Valuation Court's decision is otherwise final.
5. I found **no evidence of a body called the "Valuation of Land Appeal Board"** operating in Tasmania (that naming convention appears to be used in other states, e.g. Victoria's Land Valuation tribunals). Tasmania's own statutory appeal body under this Act is the **Land Valuation Court**, not a "Valuation of Land Appeal Board" — flagged as a correction to the initial research brief's assumption.
6. The **Magistrates Court of Tasmania** does not appear to be the hearing body for these valuation objections/appeals based on the Act text reviewed — the Act directs matters to the **Land Valuation Court** and **Supreme Court**. (It's possible the "Land Valuation Court" sits administratively within or alongside the Magistrates Court system, similar to how some specialist jurisdictions are constituted in Tasmania, but this could not be confirmed from the sources fetched — flagged in Notes.)

## Official Links

- Objecting to a Statutory Valuation (OVG overview page): https://nre.tas.gov.au/land-tasmania/office-of-the-valuer-general/objecting-to-a-statutory-valuation
- Online objection portal (OVG VISTAS Valuation Portal): https://valuation.dpipwe.tas.gov.au/VISTAS/portal/form/objection
- Owner's Guide to objecting (PDF, linked from the OVG page): https://nre.tas.gov.au/Documents/Objection-to-Valuation.pdf
- Paper "Objection to Valuation Form" (Word doc, linked from the OVG page): https://nre.tas.gov.au/Documents/Objection%20to%20Valuation%20Form.docx
- Valuation of Land Act 2001 (Tas) — current in-force version: https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2001-102
- Property Valuation Adjustment Factors (OVG): https://nre.tas.gov.au/land-tasmania/office-of-the-valuer-general/property-valuation-adjustment-factors
- State Revenue Office Tasmania — Land Tax overview: https://www.sro.tas.gov.au/land-tax
- State Revenue Office Tasmania — Complaints and objections (land tax assessment objections, distinct from valuation objections): https://www.sro.tas.gov.au/about-us/complaints
- Service Tasmania — "Lodge an objection to a notice of valuation" (directory listing page, returned HTTP 403 on automated fetch during this research; should be checked manually): https://www.service.tas.gov.au/services/housing-and-property/owning-or-leasing-land/lodge-an-objection-to-a-notice-of-valuation/
- OVG contact: ovg@nre.tas.gov.au / 03 6165 4444 / GPO Box 44, Hobart TAS 7001

## Notes / Unverified Items

- **"Land Valuation Court" vs "Valuation of Land Appeal Board":** The research brief assumed a "Valuation of Land Appeal Board (Tasmania)" as the appeal body. No evidence of this body was found. The Act instead establishes a **Land Valuation Court** as the first-tier referral/appeal body, with further appeal to the **Supreme Court of Tasmania**. This should be treated as a correction, but I recommend a manual double-check of the current Act (Part 5, ss. 30–40 region) or a call to the OVG to confirm the Land Valuation Court's current operating status/registry (e.g., whether it's a standing court or convened as needed, and where objectors actually file referral paperwork).
- **Whether the Land Valuation Court is administratively linked to the Magistrates Court of Tasmania** could not be confirmed — flag for manual verification before publishing client-facing material.
- **The 30-day window to require referral to the Land Valuation Court/Supreme Court after the OVG's decision** (Act s.30(3)-(4)) was extracted via an AI-summarized fetch of the legislation site rather than a direct read of the statutory text, so the exact figure (30 days) and the precise wording of s.30 should be independently re-verified against the primary legislation before being used in client deadline calculators.
- **Grounds for extension of the 60-day objection deadline** under ss.28(5)/30(8) — the specific circumstances a court will accept for a late objection could not be extracted in this pass; needs a direct read of those subsections.
- **"Adjusted Fire Service Value" (AFSV):** referenced in the original research brief as one of the value types, but no official OVG page was found in this research that names AFSV as a distinct OVG-issued statutory value alongside Land Value/Capital Value/AAV. It appears the Fire Service Levy is instead calculated by the Tasmania Fire Service off the Assessed Annual Value with adjustment factors, rather than the OVG issuing a separately-branded "Adjusted Fire Service Value." Flag for confirmation — do not assume AFSV is independently objectable via the same 7-ground process without checking the Fire Service levy legislation.
- **The Objection-to-Valuation.pdf "Owner's Guide"** could not be read as text during this research (PDF extraction failed/returned binary) — should be opened manually before relying on its procedural detail for client-facing collateral.
- **The SRO "Objections, reviews and appeals guideline" PDF** likewise could not be extracted as readable text — recommend a manual read to precisely delineate the SRO land-tax-assessment objection process from the OVG valuation-objection process, since a client-facing service should route users to the correct one.
- **Service Tasmania's objection lodgement page** returned an HTTP 403 to the automated fetch tool and was not able to be verified directly in this session — content described in search snippets only.
- Whether there is any lodgement/objection fee was not identified from any official source found — treated as unconfirmed (likely nil, but not verified).
