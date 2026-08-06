# Photo & Memory Digitisation Concierge — Pricing Sheet

A coordination/concierge layer on top of existing bulk-scanning bureaus —
pickup/drop-off logistics, sorting/labelling, curating a "best of"
selection, delivering an organised digital archive. **Not** in-house bulk
scanning.

## Pricing model (confirmed 2026-08-06)

**Coordination fee on top of the bureau's pass-through cost, disclosed as
such** — e.g. "Includes [Bureau]'s scanning at their published rate, plus
our $X pickup/sort/deliver/curate fee." Do not attempt to mark up or beat
the bureaus on their own per-item rate — see reasoning below.

| Component | Rate |
|---|---|
| Bureau scanning cost | Pass through at cost (bureau's own rate — see table below) |
| Coordination/curation fee | **~$55/hr**, or a flat per-visit fee |

## Bulk-scanning market (verified 2026-08-06, live pricing pages — confirms this layer is commoditised)

| Provider | Service | Price |
|---|---|---|
| Memories 2 Digital | Bulk photo scan | 30c/photo (600dpi) |
| RetroMedia (Brisbane) | ShoeBox Scan | 49c/photo (200-3,000), 29c/photo (3,001+) |
| Scan My Photo (Qld) | Bulk 6x4" scan | 24c/photo |
| Kelly's Photo Scan & Archive (Adelaide) | Slide scanning | $1.00/slide (1000+), down to $3/slide |
| Tapes to Digital (national) | VHS→USB | $35/tape, down to $24/tape at 30+ |

Full sourcing: memories2digital.com.au, retromedia.com.au,
scanmyphoto.com.au, photoscanarchive.com.au, tapestodigital.com.au — all
fetched directly 2026-08-06.

## Honest assessment

**The bulk-scanning layer is thoroughly commoditised — a solo operator
cannot and should not try to beat these bureaus on the raw per-item rate.**
At least 7 independent providers publish tight, competing rate cards
(25-70c/photo, 75c-$2/slide, $24-35/tape). The real, defensible margin is
in the coordination/curation labour these bureaus mostly don't offer:
physical pickup/drop-off for irreplaceable originals, sorting/dating loose
photos before they go to the bureau, curating rather than digitising
indiscriminately, and assembling an organised archive rather than a flat
file dump.

**Do not build this as its own priced menu item.** Offer it bundled with
Tech Concierge/Downsizing visits, where the sorting conversation is already
happening.

## Status

**CONFIRMED 2026-08-06** — pricing figures pulled from live provider pages;
the "commoditised, coordination-fee-only" conclusion is itself the key
finding. `PRICING.md` row 27 (new) and `ops-hub/app/config.py` (new
`PhotoDigitisation` business_line key) added. Perth-specific bureau pricing
not independently checked — most sourced providers are Sydney/Melbourne/
Brisbane/Adelaide-based.
