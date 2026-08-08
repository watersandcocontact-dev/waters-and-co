"""Content model for the public website — practices, services, pricing.

Real numbers pulled from wave1/*/pricing_sheet.md, not invented. Keep this
file in sync if pricing sheets change; it's a summary for web copy, not the
source of truth (the pricing sheets remain that).

Restructured 2026-08-07 from 5 flat "segments" to 4 "practices" per
docs/deep_research_growth_seo_ai_blueprint_2026-08-07.md §1/§5.1 — the
site was too broad to market as 16 equal offers; four focused practices
read as expertise, not a catalogue. Every service kept, none dropped or
renamed internally (SERVICES dict keys, business_line values, and hub
routing are all unchanged) — only the grouping/URLs changed. The old
gbp/reviewgen/missedcall cross-listing into the former "business-systems"
segment is dropped: the blueprint's own sitemap doesn't cross-list them
under AI Solutions, and one clear home per service is the whole point of
this restructure.

A practice's "services" is a flat list of service slugs (most practices).
A practice can instead use "groups" — a list of {"heading", "services"} —
for a visual sub-split (currently just small-business: Get Found & Never
Miss a Call / Books & Grants). See practice_groups() below — every
practice normalises to the same group shape either way.

Each service carries:
- "practice": the practice slug it belongs to (exactly one -- no more
  cross-listing, see above)
- "url_slug": the SEO-friendly path segment used in the live URL
  (/<practice-slug>/<url_slug>/) -- deliberately kept separate from the
  SERVICES dict key, which stays a short internal identifier used for
  hub routing, drafted-reply lookups and (via OLD_SERVICE_REDIRECTS) the
  permanent redirect from the old flat /service/<key>/ URL.
- "package": the offer-ladder package name this service maps to from the
  blueprint's §3.3 (optional -- most services aren't part of a named
  package, only the ones the blueprint explicitly bundles).
- optional richer fields (who_for/who_not_for/process/faqs) used by the
  upgraded page template for the five priority services flagged in the
  blueprint's 90-day plan (§11, "Upgrade the five priority service
  pages"): gbp, aitoolsbusiness, missedcall, ai_implementation, reviewgen.
  Absent for the other 11 services -- service.html renders those sections
  only when the data exists, so this is purely additive.
"""

PRACTICES = [
    {
        "slug": "small-business",
        "name": "Local Business Growth",
        "tagline": "Get found, get called, get paid — the everyday work of running a small business, handled properly",
        "groups": [
            {
                "heading": "Get Found & Never Miss a Call",
                "services": ["gbp", "reviewgen", "missedcall"],
            },
            {
                "heading": "Books & Grants",
                "services": ["bookkeeping", "grantfinder"],
            },
        ],
    },
    {
        "slug": "ai-solutions",
        "name": "AI Solutions for Small Business",
        "tagline": "Practical AI, set up properly and actually used — not a subscription gathering dust",
        "services": ["ai_implementation", "aitoolsbusiness", "realestate"],
    },
    {
        "slug": "personal-digital-support",
        "name": "Personal Digital Support",
        "tagline": "Patient, plain-English help — tech, finances, and the paperwork nobody enjoys",
        "services": [
            "pension", "techconcierge", "cryptoliteracy",
            "digitallegacy", "downsizing", "photodigitisation",
        ],
    },
    {
        "slug": "specialist-projects",
        "name": "Specialist Projects",
        "tagline": "Focused, one-off work — a recording repurposed, a valuation challenged",
        "services": ["videorepurpose", "landtax"],
    },
]

# Old (2026-08-07 morning) 5-segment slug -> new practice slug, for
# permanent redirects. property-tax-review and content-repurposing both
# collapse into specialist-projects; business-systems becomes ai-solutions.
OLD_SEGMENT_REDIRECTS = {
    "small-business-support": "small-business",
    "business-systems": "ai-solutions",
    "seniors-support": "personal-digital-support",
    "content-repurposing": "specialist-projects",
    "property-tax-review": "specialist-projects",
}

SERVICES = {
    "gbp": {
        "name": "Google Business Profile Management",
        "practice": "small-business",
        "url_slug": "google-business-profile-management-perth",
        "package": "Get Found / Stay Visible",
        "business_line": "GBP",
        "one_liner": "Your Google listing, actually kept up to date.",
        "summary": (
            "A fully managed Google Business Profile — accurate, current, "
            "and actively kept up, so customers see the right information "
            "and choose you instead of a competitor with a better-looking "
            "listing."
        ),
        "pricing": [
            {"label": "Visibility check and action plan", "price": "$99 fixed"},
            {"label": "Profile cleanup and relaunch", "price": "$249 fixed"},
            {"label": "Ongoing profile management", "price": "$149/mo"},
        ],
        "who_for": [
            "Trades and local service businesses who rely on Google Maps for jobs",
            "Any business whose Google listing has wrong hours, missing photos, or no recent activity",
        ],
        "who_not_for": [
            "Businesses that don't take customers via search or Maps at all",
            "Anyone wanting guaranteed rankings — no one can promise that, and anyone who does is the risk, not us",
        ],
        "process": [
            "Free 10-point visibility check of your current listing",
            "Cleanup: category, hours, service area, photos, description, Q&A",
            "Ongoing: posts, review responses and monitoring on the management tier",
            "Monthly summary of what changed and what it's driving",
        ],
        "faqs": [
            {
                "q": "Can you guarantee a #1 ranking?",
                "a": "No — nobody legitimately can. What a properly maintained profile does is remove the easy reasons Google (and customers) have to rank or trust you less.",
            },
            {
                "q": "Do I need a street address listed?",
                "a": "Only if you have a staffed storefront customers walk into. Service-area businesses should hide the address and set a proper service area instead — we'll set this correctly either way.",
            },
        ],
    },
    "reviewgen": {
        "name": "Review Generation & Reputation Management",
        "practice": "small-business",
        "url_slug": "review-management",
        "package": "Get Found / Stay Visible",
        "business_line": "ReviewGen",
        "one_liner": "More reviews, and a considered reply to every one.",
        "summary": (
            "A steady flow of new reviews from your customers, plus a "
            "considered response to every one that comes in — good or bad. "
            "Most people check reviews before they call, and a thin or "
            "ignored review list quietly costs you the job."
        ),
        "pricing": [
            {"label": "Review-request system setup", "price": "$149 fixed"},
            {"label": "Managed requests and monitoring", "price": "$149/mo"},
            {"label": "Managed requests, responses and reporting", "price": "$249/mo"},
        ],
        "who_for": ["Any business with real, happy customers who just haven't been asked for a review"],
        "who_not_for": ["Anyone wanting reviews written for them, gated, or incentivised — that breaches Google's policies and we won't do it"],
        "process": [
            "Set up a simple, neutral way to ask every customer for feedback",
            "Draft considered replies to every incoming review",
            "Flag anything that needs your direct attention",
        ],
        "faqs": [
            {
                "q": "Will you write fake reviews or pay for them?",
                "a": "No. Ever. That's against Google's terms, it's the fastest way to lose the whole profile, and it's not how this business operates.",
            },
        ],
    },
    "missedcall": {
        "name": "AI Missed-Call Reception",
        "practice": "small-business",
        "url_slug": "ai-missed-call-reception",
        "package": "Never Miss the Job",
        "business_line": "MissedCall",
        "one_liner": "The call you couldn't take still gets handled.",
        "summary": (
            "Every call you can't take still gets a response and the job "
            "still gets captured, reviewed daily so nothing slips through. "
            "A missed call is often a job that goes straight to whichever "
            "competitor picks up instead."
        ),
        "pricing": [
            {"label": "Missed-call text-back setup", "price": "$349 fixed"},
            {"label": "Managed text-back and lead capture", "price": "$199/mo"},
            {"label": "AI reception and managed follow-up", "price": "From $299/mo"},
        ],
        "who_for": ["Trades and appointment-based businesses that lose jobs to voicemail"],
        "who_not_for": ["Businesses that already have full-time reception staff answering every call"],
        "process": [
            "Set up automated text-back or AI reception on your existing number",
            "Every missed call becomes a captured lead, not a lost one",
            "Daily quality review so nothing sits unanswered",
        ],
        "faqs": [
            {
                "q": "Do I need a new phone number?",
                "a": "No — this connects to the number you already advertise. Customers never notice a change except that missed calls now get a response.",
            },
        ],
    },
    "landtax": {
        "name": "Land Tax / Rates Valuation Objection",
        "practice": "specialist-projects",
        "url_slug": "property-valuation-objection",
        "business_line": "LandTax",
        "one_liner": "If the valuation looks wrong, there's a process to challenge it.",
        "summary": (
            "A properly built, evidence-backed case for why your land or "
            "rates valuation is too high, ready for you to lodge (most "
            "states require identity-verified lodgement, so that step "
            "stays with you). Most people who don't challenge an inflated "
            "valuation simply pay more than they should."
        ),
        "pricing": [
            {"label": "Residential evidence and objection pack", "price": "$590 fixed"},
            {"label": "Complex or commercial objection pack", "price": "From $990"},
        ],
    },
    "ai_implementation": {
        "name": "AI Implementation for SMEs",
        "practice": "ai-solutions",
        "url_slug": "ai-automation-perth",
        "package": "AI Efficiency Build",
        "business_line": "AIImplementation",
        "one_liner": "A working custom automation, built and delivered — not a DIY tool.",
        "summary": (
            "A working software system built around a real bottleneck in "
            "your business — tested and ready to use, so the manual, "
            "repetitive part of your day stops eating hours you don't "
            "have. No need to learn to build it yourself or pay "
            "boutique-agency rates to get it done. Larger multi-step "
            "systems available for more complex needs."
        ),
        "pricing": [
            {"label": "Workflow check and implementation plan", "price": "$290 fixed"},
            {"label": "Practical AI workflow pilot", "price": "From $1,290"},
            {"label": "Multi-step small-business system", "price": "From $2,900"},
            {"label": "Optional monitoring and improvements", "price": "$199/mo"},
        ],
        "who_for": ["A business with one clear, repetitive bottleneck eating real hours every week"],
        "who_not_for": ["Anyone wanting a vague 'AI transformation' with no specific process in mind — start narrower, prove it, then expand"],
        "process": [
            "Describe the bottleneck — the task, how often, how long it takes now",
            "We scope one workflow with a written acceptance test",
            "Build, test against real data, hand over with documentation",
            "Optional monthly monitoring so it keeps working as your business changes",
        ],
        "faqs": [
            {
                "q": "What happens to my data?",
                "a": "Nothing goes into a public AI tool without your agreement, and personal or sensitive data is minimised or redacted before any processing. You'll always know what's being used and where.",
            },
            {
                "q": "Do I own what's built?",
                "a": "Yes — the workflow and its documentation are yours, with an export/handover path so you're never locked into us specifically to keep it running.",
            },
        ],
    },
    "realestate": {
        "name": "AI Lead-Response for Real Estate Agents",
        "practice": "ai-solutions",
        "url_slug": "real-estate-lead-response",
        "business_line": "RealEstateLeads",
        "one_liner": "Instant lead response, fully managed — no dashboard for you to run.",
        "summary": (
            "New leads get a response within moments of coming in, your "
            "cold database gets worked back through, and follow-ups keep "
            "happening — entirely hands-off. Leads go cold fast, and the "
            "agent who responds first is usually the one who wins the "
            "listing."
        ),
        "pricing": [
            {"label": "Lead-response workflow setup", "price": "$390 fixed"},
            {"label": "Managed lead response and follow-up", "price": "$179/mo"},
        ],
    },
    "aitoolsbusiness": {
        "name": "AI Tools for Business",
        "practice": "ai-solutions",
        "url_slug": "ai-tools-training-small-business",
        "package": "AI Working Session",
        "business_line": "AIToolsBusiness",
        "one_liner": "Get set up on the AI tool you already pay for, properly.",
        "summary": (
            "Your AI tool set up properly and your whole team trained to "
            "actually use it well — not just installed and left to gather "
            "dust while you keep paying for it. Lighter and cheaper than a "
            "custom automation build (that's our AI Implementation "
            "service)."
        ),
        "pricing": [
            {"label": "One tool setup and training session", "price": "$290 fixed"},
            {"label": "2–3 tools, two sessions and template pack", "price": "$490 fixed"},
            {"label": "Optional ongoing support", "price": "$120/mo"},
        ],
        "who_for": ["A business already paying for an AI tool (or considering one) that isn't confidently used yet"],
        "who_not_for": ["A business wanting a fully custom system built from scratch — that's AI Implementation, one step up"],
        "process": [
            "Confirm which tool(s) and what you want the team doing with them",
            "Configuration and account setup done properly",
            "Hands-on training session(s) with your actual team, using your actual work",
            "A short reference pack so the training sticks after we leave",
        ],
        "faqs": [
            {
                "q": "Which AI tools do you cover?",
                "a": "Whatever you're already using or considering — we work with the mainstream business AI tools rather than pushing one particular product.",
            },
        ],
    },
    "bookkeeping": {
        "name": "Small-Business Bookkeeping",
        "practice": "small-business",
        "url_slug": "bookkeeping",
        "business_line": "Bookkeeping",
        "one_liner": "Bank reconciliation and reporting, at a fixed monthly fee.",
        "summary": (
            "Your books kept accurate and current every month, with "
            "clear reporting you can actually understand — at one "
            "predictable fixed fee, never an open-ended hourly bill. "
            "Falling behind makes tax time stressful and makes it hard to "
            "know if you're actually profitable. BAS lodgement isn't "
            "included (that needs a registered BAS agent) and is referred "
            "out."
        ),
        "pricing": [
            {"label": "Micro — up to 25 transactions/mo", "price": "$169/mo"},
            {"label": "Small — 26–100 transactions/mo", "price": "From $349/mo"},
        ],
    },
    "grantfinder": {
        "name": "SME Grant-Finder",
        "practice": "small-business",
        "url_slug": "grant-finder",
        "business_line": "GrantFinder",
        "one_liner": "A curated shortlist of grants you actually qualify for.",
        "summary": (
            "A shortlist of the grants your business actually qualifies "
            "for, checked and ready to act on — so you're not the one "
            "spending hours working out what applies to you. A one-off "
            "report, not a subscription."
        ),
        "pricing": [
            {"label": "Grant-match shortlist report", "price": "$89 fixed"},
        ],
    },
    "pension": {
        "name": "Age Pension / Centrelink Assistance",
        "practice": "personal-digital-support",
        "url_slug": "age-pension-centrelink-assistance",
        "business_line": "Pension",
        "one_liner": "A flat, disclosed fee — no surprise minimums if you're found ineligible.",
        "summary": (
            "Your Age Pension claim or review handled and lodged "
            "properly — not financial advice. Centrelink's process is "
            "notoriously slow and easy to get wrong, and a mistake can "
            "cost you weeks of back-payments. A flat fee agreed and "
            "disclosed before we start, with no extra charge if the claim "
            "turns out not to be eligible."
        ),
        "pricing": [
            {"label": "New Age Pension claim", "price": "$349 flat"},
            {"label": "ARO appeal/review", "price": "$249 flat"},
        ],
    },
    "techconcierge": {
        "name": "Senior Technology Concierge",
        "practice": "personal-digital-support",
        "url_slug": "senior-technology-concierge",
        "package": "Digital Confidence at Home",
        "business_line": "TechConcierge",
        "one_liner": "Patient, plain-English tech help — teaching, not just fixing.",
        "summary": (
            "Patient, plain-English help with your devices, in-home or "
            "remote, at a fair per-session rate — no one-hour minimums, no "
            "jargon, and an eye kept out for anything that looks like a "
            "scam."
        ),
        "pricing": [
            {"label": "Standard in-person session — up to 1 hour", "price": "$79"},
            {"label": "Standard remote session — up to 1 hour", "price": "$59"},
            {"label": "Extended in-person session — up to 90 minutes", "price": "$119"},
            {"label": "Remote follow-up — up to 30 minutes", "price": "$45"},
        ],
    },
    "cryptoliteracy": {
        "name": "Crypto IT / Literacy Education",
        "practice": "personal-digital-support",
        "url_slug": "crypto-literacy-education",
        "business_line": "CryptoLiteracy",
        "one_liner": "How wallets and exchanges actually work — not investment tips.",
        "summary": (
            "A clear, safe understanding of how crypto actually works, "
            "taught in plain English — enough to protect yourself and "
            "avoid costly mistakes. Education only, never investment or "
            "financial advice."
        ),
        "pricing": [
            {"label": "1:1 session", "price": "$85/hr"},
            {"label": "Public small-group workshop", "price": "$59/person"},
            {"label": "Private workshop — up to 8 people", "price": "$349 fixed"},
        ],
    },
    "digitallegacy": {
        "name": "Digital Legacy / Account Organiser",
        "practice": "personal-digital-support",
        "url_slug": "digital-legacy-account-organiser",
        "business_line": "DigitalLegacy",
        "one_liner": "A password manager set up, your accounts inventoried, written down for your family.",
        "summary": (
            "Your important accounts organised, secured, and properly "
            "documented, with a written handover your family can actually "
            "use — so the people who matter to you aren't left guessing if "
            "something ever happens to you."
        ),
        "pricing": [
            {"label": "Starter account organiser", "price": "$139 fixed"},
            {"label": "Full digital account inventory", "price": "$289 fixed"},
            {"label": "Annual refresh", "price": "$89 fixed"},
        ],
    },
    "downsizing": {
        "name": "Senior Downsizing Support",
        "practice": "personal-digital-support",
        "url_slug": "senior-downsizing-support",
        "business_line": "Downsizing",
        "one_liner": "Coordination for a move, or hands-on help — your choice.",
        "summary": (
            "A move handled for you — coordinated end-to-end, or with "
            "hands-on help packing and sorting, whichever you actually "
            "need. Downsizing alone means more decisions and phone calls "
            "than most people expect. Tell us which you need and we'll "
            "take it from there."
        ),
        "pricing": [
            {"label": "Planning and coordination", "price": "$59/hr"},
            {"label": "Coordinated downsizing package", "price": "From $490"},
            {"label": "Hands-on labour/sorting", "price": "$80/hr flat"},
        ],
    },
    "photodigitisation": {
        "name": "Photo & Memory Digitisation",
        "practice": "personal-digital-support",
        "url_slug": "photo-memory-digitisation",
        "business_line": "PhotoDigitisation",
        "one_liner": "Your photos, slides, and videos, professionally digitised and organised for you.",
        "summary": (
            "Your photos, slides, and home videos collected, "
            "professionally digitised, and delivered back as one "
            "organised, easy-to-browse archive — not just a folder of "
            "files. Physical photos and old tapes degrade a little more "
            "every year they're left as they are."
        ),
        "pricing": [
            {"label": "Photo sorting and project setup", "price": "$149 fixed"},
            {"label": "Additional coordination and curation", "price": "$55/hr"},
            {"label": "Scanning and restoration", "price": "Quoted at supplier cost"},
        ],
    },
    "videorepurpose": {
        "name": "Video/Podcast Repurposing",
        "practice": "specialist-projects",
        "url_slug": "video-podcast-repurposing",
        "business_line": "VideoRepurpose",
        "one_liner": "One episode in, a week's worth of short clips out.",
        "summary": (
            "One recording turned into a full set of ready-to-post short "
            "clips for every platform that matters — polished, on-brand, "
            "and delivered without you touching an editing timeline. More "
            "content from the same effort means more chances to be found, "
            "without recording more."
        ),
        "pricing": [
            {"label": "Per episode (10 clips)", "price": "$249"},
            {"label": "Subscription (4 episodes/mo)", "price": "$199/episode"},
        ],
    },
}

# url_slug -> internal SERVICES key, built once at import time so routes.py
# can resolve /<practice>/<url_slug>/ without a linear scan per request.
SERVICE_KEY_BY_URL_SLUG = {svc["url_slug"]: key for key, svc in SERVICES.items()}

# Old (2026-08-07 morning) flat /service/<key>/ URL -> new nested URL, for
# permanent redirects. Every current SERVICES key redirects; nothing new
# needs adding here unless a service's url_slug changes again later.
OLD_SERVICE_REDIRECTS = {key: (svc["practice"], svc["url_slug"]) for key, svc in SERVICES.items()}


def practice_by_slug(slug):
    return next((p for p in PRACTICES if p["slug"] == slug), None)


def service_by_slug(slug):
    return SERVICES.get(slug)


def service_by_url_slug(practice_slug, url_slug):
    """Resolve a live URL's two path segments back to a service dict, or
    None if either doesn't match (wrong practice, wrong slug, or a
    practice/url_slug pairing that doesn't actually exist -- e.g. a
    service's url_slug requested under the wrong practice)."""
    key = SERVICE_KEY_BY_URL_SLUG.get(url_slug)
    if not key:
        return None
    svc = SERVICES[key]
    if svc["practice"] != practice_slug:
        return None
    return key, svc


def services_in_practice(slug):
    """Flat list of every service in a practice, regardless of whether
    it's defined as a flat list or as groups."""
    practice = practice_by_slug(slug)
    if not practice:
        return []
    if "groups" in practice:
        return [{"slug": s, **SERVICES[s]} for g in practice["groups"] for s in g["services"]]
    return [{"slug": s, **SERVICES[s]} for s in practice["services"]]


def practice_groups(slug):
    """Every practice normalised to the same shape for the template:
    [{"heading": str|None, "services": [service dicts]}, ...]."""
    practice = practice_by_slug(slug)
    if not practice:
        return []
    if "groups" in practice:
        return [
            {"heading": g.get("heading"), "services": [{"slug": s, **SERVICES[s]} for s in g["services"]]}
            for g in practice["groups"]
        ]
    return [{"heading": None, "services": [{"slug": s, **SERVICES[s]} for s in practice["services"]]}]
