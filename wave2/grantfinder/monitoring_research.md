# Grant-Finder & Rebate-Matching Research for Australian SMEs

Research date: 2026-07-29. Grant portals and rules change frequently — re-verify anything load-bearing (eligibility thresholds, dollar amounts, close dates) directly against the source before building a screening tool or advising a real business.

**Legend used throughout:**
- 🟢 **No account/signup required** — publicly browsable/searchable, no login.
- 🔵 **Signup required** — the business owner must create an account / subscribe with their own email. Claude/an automated agent should never do this on the owner's behalf without their explicit action, since it typically requires entering a personal email address and accepting terms of use.
- ⚠️ **Unverified / could not confirm** — flagged explicitly rather than guessed.

---

## 1. business.gov.au Grants and Programs Finder

URL: https://business.gov.au/grants-and-programs

### How it works
It's a guided filter/search tool (not a raw database dump) layered over listings that the Department of Industry, Science and Resources (and other agencies) publish to the site. 🟢 No login is needed to search or view results.

### Filters/search fields observed
- **Free-text name search** — type-ahead search box, filters by grant name as you type.
- **Location** — multi-select by state/territory (ACT, NSW, NT, QLD, SA, TAS, VIC, WA, "other territories"), plus a toggle "Only show regional or rural area opportunities."
- **Industry** — dropdown of ~18 ANZSIC-style categories (e.g. "Accommodation and food services," "Manufacturing," "Retail trade"), plus a checkbox to "Exclude grants for all industries" (i.e. exclude cross-industry/general grants and show only industry-specific ones).
- **Business structure** — Company, Not for profit, Partnership, Sole trader, Trust.
- **Support type** — Advice and mentoring, Funding, Loan, Sponsorship, Subsidies and rebates, Tax benefits.
- **Business objective/purpose** — ~21 categories such as AI, building improvements, community/cultural heritage, R&D, employing, environmental management, equipment/vehicles/tools, importing/exporting, investing in other businesses, manufacturing, natural disasters/emergencies, online and digital, operational costs, organising an event, promoting your business, selling to government, support for women in business, training.
- **Business stage/age** — Less than 2 years, Between 2 and 5 years, More than 5 years.
- **Grant status** — Open, Coming soon, Closed.
- **Indigenous eligibility** — toggle to only show, or exclude, Indigenous-business-specific opportunities.
- **Results pagination** — 10/25/50 per page.

This filter set is itself a strong candidate for the fields a screening/matching tool should capture about a client business (location, ANZSIC industry, legal structure, business age, and purpose/objective).

### Alerts / monitoring features
- **Shortlist + email-yourself-the-list**: 🟢 no account needed. You can star/shortlist individual grants while browsing and enter an email address to have the *shortlisted list* (not a subscription — a one-off send) emailed to you. This is a manual, one-time action, not a recurring alert.
- **General news/opportunities newsletter**: https://business.gov.au/contact-us/subscribe-to-our-news-updates — 🔵 requires entering an email to subscribe (site states "over 30,000 subscribers"). This is a broad business-news digest, not a filtered "new grants matching my profile" feed — it would need manual scanning by the owner or a downstream summarizer.
- **No dedicated "notify me of new grants matching these filters" recurring alert feature was found** on business.gov.au itself. ⚠️ Could not confirm this doesn't exist in some form behind an account (the finder doesn't appear to require or offer account creation at all — it's fully anonymous), but no such feature is documented or visible in the current UI.

### RSS / API / structured data export
- **robots.txt** (https://business.gov.au/robots.txt) only disallows crawling of `/SearchResult?resultsNum=*` and `/*/Result?*` (paginated search-result query strings) and points to a sitemap at `/sitemap.xml`. It does **not** block `/grants-and-programs` pages generally.
- **No RSS feed was found or documented** for the grants finder.
- **No public API was found or documented** for business.gov.au grants data.
- **No downloadable structured export (CSV/JSON) of the grant list was found.**
- Conclusion: 🟢 the tool is technically **scrapeable/parseable** (no login wall, no robots.txt block on the listing/detail pages, individual grant pages appear to be static, crawlable HTML with a sitemap), but there is no sanctioned/structured feed — any monitoring built on it would mean periodically re-fetching and diffing the HTML search-results page or the sitemap, which is fragile to markup changes and should respect reasonable crawl rates and the site's Terms of Use. ⚠️ I could not locate and read business.gov.au's specific Terms of Use text regarding automated access/scraping (a general WebFetch to check was not completed) — this should be checked directly before building any scraper, since general Australian legal guidance is that a site's Terms of Use can still restrict automated reuse of public pages even absent a robots.txt block.

---

## 2. Other free sources for monitoring new Australian grant opportunities

| Source | Scope | Access model | Notes |
|---|---|---|---|
| **GrantConnect** (grants.gov.au) | Commonwealth (federal) grant opportunities — current and forecast — plus Grants Awarded transparency data | 🟢 Browsing/searching is free, no registration required. 🔵 Registration (free, no fee) is required to: download full grant guidelines/documentation, submit applications, and set up **email notifications of all new Commonwealth opportunities matching your interests**, and to be auto-notified of addenda/changes to a specific opportunity once its guidelines are downloaded. | Administered by Dept of Finance. Mandated since 31 Dec 2017 that all Commonwealth grant awards be published within 21 days of the agreement taking effect — useful for market intelligence on who's winning what. |
| **data.gov.au "Grants Awarded Data"** dataset | Historical Commonwealth grants awarded (Dept of Industry, Science and Resources and grants administered on behalf of other agencies) | 🟢 Public dataset, no login (typical for data.gov.au CKAN datasets, downloadable as CSV/API via CKAN's standard interface). | Useful for backward-looking analysis (who tends to win, average grant size) rather than monitoring *new* opportunities, since it's awarded-grants history, not open opportunities. ⚠️ Did not verify exact CKAN API endpoint/format for this specific dataset — check data.gov.au directly. |
| **Business Victoria** — business.vic.gov.au/grants-and-programs | VIC state grants | 🟢 Browsing free. 🔵 "Business Victoria Update" monthly e-newsletter (business.vic.gov.au/about-us/subscribe) covers new programs/funding rounds, latest grant recipients, events — requires email signup. |
| **NSW Grants and Funding Finder** — nsw.gov.au/grants-and-funding (and service.nsw.gov.au/find-grants-and-financial-help) | NSW state + aggregates >500 grant/funding/rebate offerings from 46 separate NSW government websites | 🟢 Free filter by keyword/category/location, no login mentioned. | Positioned as a genuine aggregator across many NSW agencies/councils — potentially a good single scrape/monitoring target for NSW-specific opportunities. |
| **Business Queensland Grants Finder** — grants.services.qld.gov.au (linked from business.qld.gov.au) | QLD state grants, rebates, loans, subsidies, training | 🟢 Free search by industry/category. | Business Queensland also publishes a "Small and family business grants schedule" page listing known upcoming rounds. |
| **South Australia** — business.sa.gov.au/programs/grant-programs | SA state grants (e.g. Powering Business Grants, Research and Innovation Fund) | 🟢 Free browsing. | Smaller, more curated list than NSW/VIC/QLD portals. |
| **WA Small Business Development Corporation (SBDC)** — smallbusiness.wa.gov.au/grants and /finance/business-grants | WA state grants (e.g. Small Business Growth Grants) | 🟢 Free browsing. | SBDC's own site also explicitly points businesses back to the national business.gov.au finder for the full federal/state/local database. |
| **Local councils** (e.g. City of Sydney, City of Melbourne) | Council-level small business/creative-sector grants | 🟢 Browsing free; 🔵 applications typically run through SmartyGrants (see §4), which requires an account to submit. | Easy to miss — many SME-relevant micro-grants ($2k–$20k) sit at council level, not state/federal. Worth enumerating per-LGA if targeting a specific region. |
| **Industry association newsletters** (AiGroup "Manufacturing Matters", AMTIL, Tourism & Transport Forum, Australian Tourism Industry Council, Australian Retailers Association, National Retail Association, AIIA, TechCouncil of Australia, COSBOA, state Chambers of Commerce) | Sector-specific grants and (claimed) advance notice | 🔵 Requires membership/subscription (often paid membership, not just free email signup, depending on the association). | ⚠️ **Flagging as unverified**: one source (australiangrants.org, a commercial grants-consulting content site, not a primary source) claimed industry associations "know about grants 30-60 days before public announcement." This is a plausible-sounding but unsubstantiated marketing claim from a secondary/commercial source — treat as anecdotal, not fact, until corroborated by a primary source (e.g. the association itself or a government media release timeline). |
| **GrantConnect email notifications** vs **business.gov.au** | — | — | Note the asymmetry: GrantConnect is the one with an actual "notify me of all new matching opportunities" subscription feature (🔵 free account required); business.gov.au itself does not appear to have an equivalent recurring-alert feature, only the one-off shortlist emailer and the general newsletter. |

**Practical implication for the product**: no single free, no-login, structured feed of "new SME-relevant grants across all of Australia" exists. A monitoring service will likely need to combine (a) periodic scraping/diffing of business.gov.au and the state finders (🟢 no signup, but fragile/ToS-sensitive), with (b) the owner's own GrantConnect and state-newsletter subscriptions (🔵 owner must sign up themselves) feeding in as a secondary signal, since those give genuine push notifications the tool doesn't have to build itself.

---

## 3. Common eligibility criteria patterns across SME grants

Collated from multiple programs (EMDG, state SME grants, generic small-business grant guides). Treat exact figures as illustrative — they vary by program and must be checked per-grant, but the *pattern* of criteria types is consistent and is a good basis for a screening checklist:

1. **Valid, active ABN (and sometimes ACN)** — must not be cancelled/suspended, must be registered to the applying entity. Very commonly a **minimum tenure** requirement too (frequently ~12 months active ABN; EMDG specifically requires trading under the same ABN for **at least two consecutive years** before applying).
2. **GST registration**, often for a minimum period (commonly ≥12 months) before applying.
3. **Annual turnover thresholds** — very commonly capped at **under $20 million** (this is the standard ATO/legislative definition threshold used by many federal programs, incl. EMDG); some programs use a higher cap (up to $100m) or, conversely, target only micro businesses.
4. **Employee count thresholds** — federal SME-targeted programs often cap around **<200 employees**; some micro/small-business-specific grants target **<20 employees**. Definitions of "small business" vary by program (ATO/ABS/program-specific definitions aren't identical).
5. **Minimum business operating age** — commonly "trading for at least 1–2 years," sometimes tied to the ABN-tenure rule above rather than a separate criterion.
6. **Co-contribution / matching funding requirements** — very common. Often expressed as a ratio (e.g. 1:1 matched funding) or a percentage (commonly around 50% of total project cost must come from the applicant). EMDG frames this differently — as a minimum spend threshold (≥$20,000/year on eligible marketing activity) rather than a strict match ratio.
7. **Business structure eligibility** — many grants restrict eligibility by legal structure (company, sole trader, partnership, trust, not-for-profit) — visible directly as a filter on business.gov.au, confirming this is a first-order screening field.
8. **Location/registration requirements** — registered business address or primary operations within the specific state/territory or LGA offering the grant; some programs have regional/rural-only carve-outs or bonuses.
9. **Industry/sector alignment** — grant tied to a specific ANZSIC industry or a stated "business objective" (R&D, exporting, employing, digital adoption, etc.) — again mirrors the business.gov.au filter taxonomy.
10. **Not currently insolvent / no outstanding tax debt** — common good-standing requirement (ATO compliance, not under external administration).
11. **One-grant-per-round / no-double-dipping rules** — many programs exclude applicants who've received the same or a similar grant recently, or require disclosure of other government funding for the same project/activity.
12. **Insurance in place appropriate to the project** (see §4) is sometimes an eligibility condition, not just an application document.

**Suggested screening checklist fields** for a matching tool, derived from the above: ABN status + activation date, GST registration date, legal structure, ANZSIC industry, state/territory + regional/rural flag, annual turnover, employee headcount, years trading, ability to fund a co-contribution (and roughly how much cash/in-kind is available), sector/purpose tags matching the business.gov.au objective taxonomy, good-standing (no insolvency/tax debt), and whether they've received other grants recently for the same activity.

---

## 4. What a typical grant application requires

Based on business.gov.au general guidance, an EMDG (Austrade) example, and SmartyGrants — the platform underlying most state/council grant applications (e.g. City of Sydney, City of Melbourne, many regional council and state programs) — a typical SME grant application bundle includes:

**Identity/registration documents**
- ABN details (and ACN/certificate of incorporation for companies).
- Proof of business registration/legal structure.

**Financials**
- Recent financial statements (to prove turnover thresholds, and financial capacity to fund the co-contribution).
- A project **budget** — SmartyGrants guidance specifies budgets are typically required **exclusive of GST and in whole dollars**, itemising income and expenditure.
- **Quotes** for equipment/materials/services above a cost threshold — a common concrete example: City of Sydney's Small Business Grant requires **a minimum of two quotes** for any equipment/material item over $1,000.

**Planning/narrative documents**
- A **business plan** (or an excerpt/summary of one) — business.gov.au itself provides a free business plan template/tool partly because so many grant applications expect one.
- For activity-specific grants (e.g. EMDG), a **marketing/export plan** demonstrating genuine market research, target market understanding, entry strategy, measurable objectives and an activity timeline — i.e., a project plan tailored to the specific grant's purpose, not just a generic business plan.
- Project timeline/milestones and how grant funds will be spent.

**Compliance/risk documents**
- **Insurance** — most commonly a **Certificate of Currency for Public Liability Insurance** (City of Sydney's example specifies cover to the value of $10 million for the project). If auspiced by another organisation, written agreement to use that organisation's insurance is sometimes accepted (per SmartyGrants guidance).
- Confirmation of no outstanding tax debt / good standing with the ATO.

**Support/endorsement documents**
- **Letters of support** — frequently requested or "recommended" (not always mandatory) from community partners, project partners, local council, or industry bodies, particularly for community/place-based grants. EMDG's specific documentation requirements around letters of support were **not found/confirmed** in this research — ⚠️ flagged as unverified for that specific program; don't assume EMDG requires one without checking Austrade's guidelines directly.

**Platform-specific note**: because SmartyGrants underlies a large share of state/council grant programs, its "Help Guide for Applicants" (https://applicanthelp.smartygrants.com.au/) and "Preparing a budget" / "Project budgeting" help sheets (smartygrants.com/help-sheets/...) are a reasonably reliable proxy for "typical" document/format requirements across many non-federal SME grants, and could be a good reference to build a generic application-drafting template against — with the caveat that any individual grant's specific guidelines always take precedence.

**Suggested application-drafting template sections**, derived from the above: applicant/entity details (ABN/ACN), eligibility self-declaration against the program's criteria, project description & objectives, itemised budget (GST-exclusive, whole dollars) with ≥2 quotes for line items over $1,000, timeline/milestones, business plan excerpt or link to full plan, insurance certificate of currency, financial capacity evidence for co-contribution, and an optional letters-of-support slot.

---

## Summary — no-signup vs signup-required monitoring methods

**🟢 No account/signup needed (owner or tool can just browse/query):**
- business.gov.au Grants and Programs Finder — full search/filter, plus one-off shortlist emailer.
- GrantConnect — browsing and searching current/forecast Commonwealth opportunities.
- data.gov.au Grants Awarded Data dataset.
- NSW, VIC, QLD, SA, WA state grant finder portals — browsing/searching.
- Council grant listing pages — browsing.

**🔵 Requires the business owner to sign up themselves (do not do this on their behalf without explicit, in-the-moment approval, since it means submitting their email/personal details to a third-party government or association site):**
- business.gov.au general news/opportunities newsletter.
- GrantConnect free registered-user account — needed for full document downloads, application submission, and the actual "notify me of new matching opportunities" email alert feature.
- Business Victoria "Business Victoria Update" monthly e-newsletter.
- Industry association newsletters/memberships (AiGroup, ARA/NRA, AIIA, TechCouncil, COSBOA-affiliated bodies, state Chambers of Commerce) — several of these are paid memberships, not just free email signups; verify per-association.
- SmartyGrants-based application accounts (needed to actually submit an application, on nearly every state/council grant).

**⚠️ Flagged as unverified/unconfirmed during this research (re-check before relying on):**
- Whether business.gov.au's Terms of Use place any additional restriction on automated/scraped access beyond what robots.txt shows.
- Exact API/CKAN access details for the data.gov.au Grants Awarded Data dataset.
- Whether any recurring "email me new grants matching my filters" feature exists on business.gov.au beyond the one-off shortlist emailer and general newsletter (none found, but a hidden/account-gated feature can't be fully ruled out since the finder requires no account at all currently).
- The "industry associations know about grants 30–60 days early" claim (sourced from a commercial grants-consultancy content site, not corroborated elsewhere).
- Whether EMDG specifically requires letters of support as part of its application.
