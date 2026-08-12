#!/usr/bin/env python3
"""Create (or update) a hub lead for a genuine reply to the cold-email campaign.

Why this exists: ops-hub/app/webhook.py only ingests leads from two
places -- the website contact form and the phone/SMS webhook. A reply to
one of the 120 cold-outreach emails has no automated path into the hub at
all (flagged 2026-08-10/11, see ml_training_log event
campaign-reply-pipeline-gap-2026-08-10). This script is the missing third
ingestion path, called by the `campaign-reply-watch` scheduled task once
per genuine reply it finds in Gmail -- not run on a timer itself, and not
a webhook (Gmail access only exists via the connected MCP session inside
an agent turn, so the scheduled task does the Gmail search+read; this
script only does the local DB write, the one part a plain script safely
can).

Repeat senders (added 2026-08-11): the reply-watch scan now detects
individual follow-up MESSAGES rather than whole threads, so the same
person can legitimately arrive here more than once -- Kirrilee replying,
then replying again two days later. When the sender already has a lead,
this appends a timestamped note to that lead instead of creating a
duplicate case record. Without this, the message-level scan fix would
have quietly shredded one conversation across several lead rows.

Usage:
    python3 scripts/create_email_reply_lead.py \\
        --name "Jane Smith" --email jane@example.com.au \\
        --subject "Re: missed calls costing you jobs?" \\
        --snippet "Yeah keen to hear more, give me a call" \\
        --thread-url "https://mail.google.com/mail/u/0/#inbox/<threadId>" \\
        --business-line MissedCall \\
        [--urgent]   # opt-out/unsubscribe request -- Spam Act 2003 gives
                      # a ~5-business-day clock to honour it, see
                      # DECISIONS.md 2026-08-09 entry
        [--json]     # print {"lead_id": N, "action": "created"|"appended"}
                      # instead of the bare ID, so the caller can tell a
                      # new lead from a follow-up on an existing one

Prints the new/updated lead's numeric ID on success (nothing else, unless
--json), non-zero exit and a message on stderr on failure -- easy for the
calling agent turn to check.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.config import BUSINESS_LINE_KEYS  # noqa: E402
from app.models import (  # noqa: E402
    append_note,
    create_lead,
    find_lead_by_email,
    update_lead,
)

VALID_BUSINESS_LINES = set(BUSINESS_LINE_KEYS)  # canonical list, not a hand-copied one -- see app/config.py

URGENT_NEXT_ACTION = "Honour opt-out request (Spam Act 5-business-day clock)"
URGENT_LEFT_FOR_YOU = (
    "Spam Act 2003 requires this be honoured within ~5 business days. Confirm the sender is "
    "removed from all future sends and reply confirming if appropriate."
)


def _append_to_existing(lead, args):
    """Record a follow-up message on a lead that already exists.

    Deliberately conservative about `status`: the Owner's workflow owns
    that column, and silently flipping a Won/Quoted lead back to New on an
    inbound "thanks!" would corrupt the queue. Only the fields that
    describe what to do next get touched.
    """
    already_urgent = bool((lead.get("extra") or {}).get("urgent_optout"))
    changes = {}

    if args.urgent:
        changes = {
            "next_action": URGENT_NEXT_ACTION,
            "left_for_you_summary": URGENT_LEFT_FOR_YOU,
            "extra": {**(lead.get("extra") or {}), "urgent_optout": True},
        }
    elif not already_urgent:
        # Never downgrade a live opt-out obligation because a later,
        # friendlier message arrived on the same address.
        changes = {
            "next_action": "Reply to campaign follow-up",
            "left_for_you_summary": "They've come back again — review the thread and respond.",
        }

    if changes:
        update_lead(lead["id"], {**lead, **changes})

    # Order matters, and not obviously: update_lead is a full-row overwrite
    # that rewrites `notes` from the dict handed to it. `lead` was read
    # before this function ran, so doing the note first and the update
    # second writes the stale pre-append notes back over it and silently
    # loses the new message. Append last.
    label = "Opt-out request" if args.urgent else "Follow-up reply"
    append_note(
        lead["id"],
        f"{label} — subject: {args.subject}\n  “{args.snippet}”\n  {args.thread_url}",
    )

    return lead["id"]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--name", required=True, help="Sender's name (best guess from the email if not signed)")
    p.add_argument("--email", required=True, help="Sender's email address")
    p.add_argument("--subject", required=True)
    p.add_argument("--snippet", required=True, help="Short quote/summary of what they actually said")
    p.add_argument("--thread-url", required=True, help="Gmail web link straight to the thread")
    p.add_argument(
        "--business-line", default="GeneralEnquiry",
        help="Which offer they're replying to, if obvious from the thread. Defaults to GeneralEnquiry "
             "(the same website-catch-all tag) when it's not clear which of the 16 lines it maps to.",
    )
    p.add_argument(
        "--urgent", action="store_true",
        help="Set when the reply is an opt-out/unsubscribe/complaint -- flags the lead so it sorts to "
             "the top of the queue instead of competing on normal $/hr priority.",
    )
    p.add_argument(
        "--json", action="store_true",
        help="Print a JSON object with lead_id and action (created|appended) instead of the bare ID.",
    )
    args = p.parse_args()

    business_line = args.business_line if args.business_line in VALID_BUSINESS_LINES else "GeneralEnquiry"

    existing = find_lead_by_email(args.email)
    if existing:
        lead_id = _append_to_existing(existing, args)
        action = "appended"
    else:
        if args.urgent:
            done_summary = "Opt-out/unsubscribe request received via cold-email reply."
            left_for_you = URGENT_LEFT_FOR_YOU
            next_action = URGENT_NEXT_ACTION
        else:
            done_summary = "Reply received to the cold-email outreach campaign — captured automatically, not yet actioned."
            left_for_you = "Review the reply and respond — response speed matters most here."
            next_action = "Reply to campaign response"

        notes = f"Subject: {args.subject}\n\nWhat they said: “{args.snippet}”\n\nThread: {args.thread_url}"

        lead_id = create_lead({
            "name": args.name,
            "business_line": business_line,
            "status": "New",
            "next_action": next_action,
            "notes": notes,
            "contact_name": args.name,
            "contact_email": args.email,
            "source": "cold_email_reply",
            "source_url": args.thread_url,
            "done_summary": done_summary,
            "left_for_you_summary": left_for_you,
            "extra": {"urgent_optout": True} if args.urgent else {},
        })
        action = "created"

    if args.json:
        print(json.dumps({"lead_id": lead_id, "action": action}))
    else:
        print(lead_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 -- deliberately broad, this is a small CLI tool
        print(f"create_email_reply_lead.py failed: {exc}", file=sys.stderr)
        sys.exit(1)
