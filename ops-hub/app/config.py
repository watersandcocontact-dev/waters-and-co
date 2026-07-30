"""Static config: business lines, statuses, and per-line extra-field schemas.

Wave 2 business lines are included now (per instructions) even though
Wave 2 isn't launched yet, so the hub is ready to receive leads for them
without a later migration.
"""

BUSINESS_LINES = [
    # Wave 1 — fully built (hub + templates/research/pricing)
    ("GBP", "GBP / Local SEO"),
    ("ReviewGen", "Review Generation"),
    ("MissedCall", "AI Missed-Call Reception"),
    ("LandTax", "Land Tax / Rates Objection"),
    # Wave 2 (prep) — checklists/research built, not launched
    ("Bookkeeping", "Bookkeeping (non-BAS)"),
    ("Concession", "Energy/Concession Navigation"),
    ("GrantFinder", "SME Grant Finder"),
    ("Pension", "Age Pension / Centrelink Assistance"),
    # Introduced via PRICING.md (2026-07-30). Built out on 2026-07-30 for the
    # low-regulatory-risk ones (service scope + pricing in wave3-unscoped/).
    # Still-held ones stay tagged "(unscoped)" — see DECISIONS.md for why.
    ("LostSuper", "Lost Super / TPD Navigation (referral model)"),
    ("DeceasedEstate", "Deceased-Estate Admin (unscoped — holding, see DECISIONS.md)"),
    ("TechConcierge", "Senior Tech Concierge"),
    ("GrantWriting", "Grant Writing — Nonprofit (unscoped — needs portfolio first)"),
    ("NDISNav", "NDIS Plan Navigation (unscoped — holding, see DECISIONS.md)"),
    ("NDISCompliance", "NDIS Provider Compliance/Audit-Prep (unscoped — holding, see DECISIONS.md)"),
    ("VideoRepurpose", "Video/Podcast Repurposing"),
    ("Downsizing", "Senior Downsizing/Cleanout"),
    ("AirbnbCohost", "Airbnb Co-Hosting (unscoped — likely needs a real estate licence, see DECISIONS.md)"),
]
BUSINESS_LINE_KEYS = [k for k, _ in BUSINESS_LINES]

# Business lines where a single lead might be a "setup" task or an "ongoing
# management" task with very different $/hr (see PRICING.md rows 3-6) — the
# lead form shows a task-type selector for these; everything else has one
# flat default rate.
TASK_TYPE_LINES = {
    "GBP": ["setup", "management"],
    "MissedCall": ["setup", "management"],
}

# Default $/hr per business line (midpoint of the range in PRICING.md),
# used to rank the Daily Queue until a lead has its own time-estimate
# override or actual logged hours. See models.dollar_per_hour().
RATE_CARD = {
    "GBP": {"setup": 80, "management": 225},
    "ReviewGen": 300,
    "MissedCall": {"setup": 70, "management": 300},
    "LandTax": 280,
    "Bookkeeping": 95,
    "Concession": 140,
    "GrantFinder": 325,
    "Pension": 138,
    "LostSuper": 635,
    "DeceasedEstate": 65,
    "TechConcierge": 80,
    "GrantWriting": 315,
    "NDISNav": 75,
    "NDISCompliance": 95,
    "VideoRepurpose": 80,
    "Downsizing": 65,
    "AirbnbCohost": 45,
}

STATUSES = [
    "New",
    "Contacted",
    "Qualified",
    "Proposal Sent",
    "Active",
    "On Hold",
    "Won",
    "Lost",
]

AU_STATES = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "ACT", "NT"]

# Default deadline-alert thresholds (days) per business line.
# LandTax and Pension/GrantFinder have hard statutory/program deadlines,
# so they get flagged earliest.
DEADLINE_THRESHOLDS = {
    "LandTax": [14, 30, 60],
    "Pension": [14, 30, 60],
    "GrantFinder": [14, 30, 60],
    "Concession": [14, 30, 60],
    "GBP": [14, 30, 60],
    "ReviewGen": [14, 30, 60],
    "MissedCall": [14, 30, 60],
    "Bookkeeping": [14, 30, 60],
    "_default": [14, 30, 60],
}

# Extra, business-line-specific fields. Rendered as simple text inputs in the
# lead form and stored as JSON in leads.extra_json — avoids a schema migration
# every time a new business line needs a new field.
EXTRA_FIELDS = {
    "GBP": [
        ("google_profile_url", "Google Business Profile URL"),
        ("website", "Website"),
        ("current_review_count", "Current review count"),
    ],
    "ReviewGen": [
        ("platform_used", "Review platform(s) in use"),
        ("monthly_review_target", "Monthly review target"),
    ],
    "MissedCall": [
        ("phone_platform", "AI phone platform"),
        ("call_volume_estimate", "Estimated monthly call volume"),
    ],
    "LandTax": [
        ("property_address", "Property address"),
        ("council_lga", "Council / LGA"),
        ("valuation_notice_date", "Valuation notice date (YYYY-MM-DD)"),
        ("current_valuation", "Current (disputed) valuation"),
        ("target_valuation", "Target/evidence-based valuation"),
    ],
    "Bookkeeping": [
        ("accounting_software", "Accounting software (Xero/QBO/other)"),
        ("monthly_tx_volume", "Approx. monthly transaction volume"),
    ],
    "Concession": [
        ("concession_type", "Concession/rebate type"),
        ("household_situation", "Household situation (pensioner/low-income/etc.)"),
    ],
    "GrantFinder": [
        ("grant_program", "Grant program name"),
        ("application_window", "Application window / round"),
    ],
    "Pension": [
        ("claim_type", "Claim type (new claim / ARO review / other)"),
        ("centrelink_ref", "Centrelink reference (if any)"),
    ],
    "TechConcierge": [
        ("session_type", "Session type (setup/scam check/troubleshooting/etc.)"),
        ("device", "Device(s) involved"),
    ],
    "VideoRepurpose": [
        ("platform_targets", "Target platforms (TikTok/Reels/Shorts/LinkedIn)"),
        ("episode_link", "Episode file/link"),
    ],
    "Downsizing": [
        ("property_address", "Property address"),
        ("job_type", "Job type (declutter/full clearout/move-prep)"),
    ],
    "LostSuper": [
        ("referral_partner", "Referral partner (TPD lawyer/AFSL adviser)"),
        ("referral_fee_agreed", "Referral fee agreed ($)"),
    ],
}

# Business lines with a hard statutory/program deadline that should
# auto-populate from a notice/trigger date if the user doesn't set one.
# `days_to_add` can be an int (flat rule) or a dict of {au_state: days} with
# a "_default" fallback — objection windows vary by state (confirmed via
# wave1/landtax/state_*.md research: NT is 30 days, all other states/territories
# are 60 days as of 2026-07).
AUTO_DEADLINE_RULES = {
    # (extra_field_holding_trigger_date, days_to_add)  -> writes into `deadline`
    "LandTax": (
        "valuation_notice_date",
        {"NT": 30, "_default": 60},
    ),
}
