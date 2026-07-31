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
    # Website contact-form catch-all (2026-07-30) — "don't see what you need?"
    # enquiries that don't match a listed service.
    ("GeneralEnquiry", "General Enquiry (via website)"),
    # 2026-07-31 additions — explicitly designed to reuse Tech Concierge's
    # client base/booking infra rather than needing anything built from
    # scratch. See DECISIONS.md for the "reuse-what-exists" filter this
    # came from.
    ("CryptoLiteracy", "Crypto IT / Literacy"),
    ("AIToolsBusiness", "AI Tools for Business"),
    # Lightweight catch-all for one-off gig/marketplace jobs (Airtasker,
    # Marketplace, etc.) that don't warrant a dedicated business line unless
    # the same kind of job starts repeating — see
    # wave3-unscoped/opportunity_scan/gig_marketplace_scan.md
    ("OddJobs", "Odd Jobs / Gig Marketplace"),
]
BUSINESS_LINE_KEYS = [k for k, _ in BUSINESS_LINES]

# Business lines where a single lead might be a "setup" task or an "ongoing
# management" task with very different $/hr (see PRICING.md rows 3-6) — the
# lead form shows a task-type selector for these; everything else has one
# flat default rate.
TASK_TYPE_LINES = {
    "GBP": ["setup", "management"],
    "MissedCall": ["setup", "management"],
    # session = live 1:1/workshop delivery, course = the pre-recorded product
    # (near-zero marginal delivery cost once built, very different $/hr)
    "CryptoLiteracy": ["session", "course"],
}
TASK_TYPE_LABELS = {
    "setup": "Setup",
    "management": "Ongoing management",
    "session": "Live session",
    "course": "Pre-recorded course",
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
    "CryptoLiteracy": {"session": 100, "course": 300},
    "AIToolsBusiness": 85,
    "OddJobs": 50,  # rough default — every job varies, override per-lead with real quoted price/time
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
    "CryptoLiteracy": [
        ("format", "Format (1:1 / workshop / course sale)"),
        ("investment_boundary_held", "Investment-question boundary held? (y/n + note if redirected)"),
    ],
    "AIToolsBusiness": [
        ("tools_setup", "Tool(s) being set up"),
        ("existing_client", "Reused from existing GBP/ReviewGen/MissedCall client? (y/n)"),
    ],
    "OddJobs": [
        ("platform", "Platform (Airtasker/Marketplace/Gumtree/etc.)"),
        ("repeat_pattern_flag", "Is this the 2nd+ similar job recently? (y/n — signal to consider a real business line)"),
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

# --- Expansion budget + kill-switch (2026-07-31) ---

# Phase 1 = $0 budget, no spend allowed until you explicitly flip this.
# This is a code-level switch, not a UI toggle, deliberately — flipping it
# means editing this file, which matches "I decide when the budget phase
# starts, don't assume it."
BUDGET_PHASE = "off"  # "off" | "on"
WEEKLY_BUDGET_RANGE = (25, 50)  # scales to 100 only once methods show results

# Evaluation window (weeks) before a spend-type needs a real keep/adjust/kill
# call. Reasoning (logged in DECISIONS.md 2026-07-31): search ads show
# statistically usable signal fastest since click-through intent is
# immediate; social/meta ads need longer for audience-based targeting to
# leave its learning phase; organic content is slowest since indexing and
# audience compounding both take real time; tool subscriptions aren't really
# "killable" the same way, they get a monthly cost-review instead; referral
# partnerships are relationship-based and slower to generate volume.
EVALUATION_WINDOWS_WEEKS = {
    "search_ads": 3,
    "meta_ads": 4,
    "content": 10,
    "tool_subscription": 4,
    "referral_partnership": 6,
    "other": 4,
}

# --- Tax tracking (2026-07-31) ---
# Figures verified 31 July 2026 against ato.gov.au —
# see wave3-unscoped/tax_tracking/ato_figures_verification.md for sources
# and nuance. This is an organisation/flagging tool, NOT tax advice — every
# figure here should be re-checked before relying on it, and a qualified
# accountant should sign off before any of this is acted on. Two figures
# are marked unconfirmed-for-this-year below; the rest were confirmed
# directly against official ATO pages.
TAX_FIGURES = {
    "financial_year": "2026-27",
    "instant_deduction_threshold": 300,       # individual work-related items <= this = immediate deduction
    "no_receipt_combined_cap": 300,            # total work-related claims w/o receipts (excl. car/travel/meal allowances)
    "no_receipt_laundry_cap": 150,             # inside the combined 300, not additional
    "no_receipt_small_expense_cap": 200,       # separate provision, not inside the 300
    "no_receipt_small_expense_per_item_max": 10,
    "no_record_phone_internet_threshold": 50,  # above this needs a 4-week diary
    "cents_per_km_rate": 0.91,
    "cents_per_km_max_km": 5000,
    "home_office_fixed_rate": 0.70,            # CONFIRMED for FY24-25/FY25-26 only — see UNCONFIRMED note below
    "concessional_super_cap": 32500,
    "non_concessional_super_cap": 130000,
    "non_concessional_bring_forward_cap": 390000,
    "gst_registration_threshold": 75000,
    "gst_registration_window_days": 21,
    "division_293_threshold": 250000,
    # Bracket thresholds unchanged FY25-26 -> FY26-27; the second-bracket
    # rate drops 16% -> 15% from 1 July 2026 ("now law" per ATO). Medicare
    # levy (2%) is separate, not included in these marginal rates.
    "tax_brackets": [
        {"floor": 0, "ceiling": 18200, "rate": 0.0},
        {"floor": 18200, "ceiling": 45000, "rate": 0.15},
        {"floor": 45000, "ceiling": 135000, "rate": 0.30},
        {"floor": 135000, "ceiling": 190000, "rate": 0.37},
        {"floor": 190000, "ceiling": None, "rate": 0.45},
    ],
    # Concessional-cap carry-forward: 5-year window, eligible if total super
    # balance was under $500,000 at the prior 30 June. FY2021-22 unused
    # space expires 30 June 2027 (verification corrected your original
    # "30 June 2026" claim by one year — it's still usable this FY).
    "carry_forward_eligible_tsb_threshold": 500000,
    "carry_forward_years": [
        {"fy": "2021-22", "expires": "2027-06-30"},
        {"fy": "2022-23", "expires": "2028-06-30"},
        {"fy": "2023-24", "expires": "2029-06-30"},
        {"fy": "2024-25", "expires": "2030-06-30"},
        {"fy": "2025-26", "expires": "2031-06-30"},
    ],
    "unconfirmed_for_this_fy": [
        "home_office_fixed_rate — confirmed for FY24-25/FY25-26 at 70c, "
        "ATO had not published an explicit FY26-27 figure as of 31 Jul 2026 "
        "research date; treated as the likely default, flagged in the UI",
    ],
}

# Day-job hourly rate — from your payslip data (gross/hours). Used for the
# day-job-vs-business $/hr comparison. Update if your rate changes.
DAY_JOB_HOURLY_RATE = 45.0

# Expense categories, tagged by where they can apply. "day_job" = Carpentry
# TA specific; "business" = any of the 19 business lines; "both" = either.
EXPENSE_CATEGORIES = {
    "tools_equipment": {"label": "Tools & equipment", "context": "both"},
    "ppe_laundry": {"label": "PPE / protective clothing / laundry", "context": "day_job"},
    "car_travel": {"label": "Car/travel (multi-site or bulky tools)", "context": "day_job"},
    "self_education": {"label": "Self-education (current role only)", "context": "day_job"},
    "union_fees": {"label": "Union/professional association fees", "context": "day_job"},
    "home_office": {"label": "Home office running costs (fixed-rate hours)", "context": "business"},
    "software_subscriptions": {"label": "Software/subscriptions", "context": "business"},
    "insurance": {"label": "Professional indemnity/business insurance", "context": "business"},
    "asic_fees": {"label": "ASIC fees (business name renewal, etc.)", "context": "business"},
    "accounting_fees": {"label": "Accounting/bookkeeping fees, bank fees", "context": "business"},
    "marketing": {"label": "Marketing/advertising (feeds expansion_spend too)", "context": "business"},
    "vehicle_km": {"label": "Vehicle use, client-facing (cents/km)", "context": "business"},
    "equipment_depreciation": {"label": "Equipment/depreciation", "context": "business"},
    "education_business": {"label": "Education/courses for running the business", "context": "business"},
}
