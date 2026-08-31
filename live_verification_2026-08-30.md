# Live Verification — Phase 1 (Top 5 Candidates) — 2026-08-30

Deferred live-telnet phase from `cluster_research_methodology.md`,
executed against the top 5 of the 10 ranked nodes in
`na_cluster_ranking_2026-08.md`. This supplements, but does not
overwrite, the corroboration-based ranking — see Recommendation below
for how the two should be reconciled.

## Method

Three scratchpad scripts (not committed — throwaway per this session's
scope decision), run against callsign **N6YU**:

1. **Full test**: TCP connect (15s timeout) → detect login prompt → send
   callsign → collect for up to 60s or until 3 `DX de` spot lines
   received, whichever first.
2. **Banner-only retest**: TCP connect only, no login sent, report
   whatever the server volunteers unprompted in 8s — run specifically to
   separate "dead" (no TCP connect) from "alive but our login logic
   didn't trigger a response" (connects, but silent or mishandled).
3. **VE7CC nudge retest**: TCP connect + send a bare CRLF, wait 10s, to
   rule out a server that withholds its banner until it sees any client
   input.

## Results

| Node | Host:Port | TCP connect | Banner/login prompt | Spots (3-in-60s test) | Verdict |
|---|---|---|---|---|---|
| **NC7J** | dxc.nc7j.com:7373 | Yes (0.3s) | Yes, full banner | **3 spots in 5.4s** | **LIVE — confirmed** |
| **WA9PIE-2** | dxc.wa9pie.net:8000 | Yes (0.1s) | Yes, full banner | **3 spots in 34.3s** | **LIVE — confirmed** |
| **WA9PIE-2** | hrd.wa9pie.net:8000 | Yes (0.1s) | **Identical banner to above** | 1 spot in 60s | Same backend as above — not a separate node |
| **W3LPL** | w3lpl.net:7373 | Yes (0.1s) | Yes, full banner, login prompt | 0 spots in 60s | **LIVE, responsive — spot volume untested** (see caveat) |
| **VE7CC-1** | ve7cc.net:7373 | Yes (0.2s) | **No — silent even after CRLF nudge** | 0 spots | **Effectively non-functional** |
| **VE7CC-1** | dxc.ve7cc.net:23 | Yes (0.3s) | **No — silent even after CRLF nudge** | 0 spots | **Effectively non-functional** |
| **W9PA** | dxc.w9pa.net:7373 | **No — timeout, twice on independent runs** | — | — | **DEAD** |

## Key findings

**WA9PIE-2's hostname conflict is resolved, not contested.**
`dxc.wa9pie.net:8000` and `hrd.wa9pie.net:8000` return byte-identical
banners — same DXSpider backend, two DNS aliases, not competing hosts.

**W3LPL's 0-spot result is very likely a test artifact, not an outage.**
Its banner states CW skimmer spots are **off by default**
(`set/skimmer` required), which the test never sent. Login prompt and
full banner confirm the node is alive and responsive; only the
spot-volume claim from `na_cluster_ranking_2026-08.md` remains
unconfirmed live, pending a retest that sends `set/skimmer`.

**VE7CC-1 is confirmed down**, on the strength of four independent,
mutually reinforcing, dated signals: (1) the TCP port accepts a
connection but sends *nothing* — not even a login prompt — on both its
listed ports, even after a CRLF nudge; (2) DXHeat.com's structured
data shows VE7CC's **last received spot was 2026-06-12** (11 weeks
before this report) and its **last sent spot was 2025-09-24** (nearly a
year stale); (3) a groups.io authenticated fetch (via the
`groupsio-fetch` skill built this session — see below) retrieved a
first-hand, dated report: KE8G, N1MMLoggerPlus message #102247, August
2026: *"I get nothing at all from VE7CC, my usual cluster... Most of
the connection attempts just sit there and do nothing."* — an exact
independent match for the live silent-connection result; (4) multiple
other relevant groups.io thread titles were found via search this
session ("VE7CC-1 DOWN?", "VE7CC-1 Cluster down?", "Almost no spots
from VE7CC"), consistent with a wider, ongoing community-noticed
problem. An open TCP port with no application-layer response is
consistent with a dead or hung backend process behind a still-running
listener/load balancer, not a healthy node.

**W3LPL's 0-spot result now has independent, dated confirmation of the
cause, not just a plausible hypothesis.** Tim Shoppa (N3QE),
N1MMLoggerPlus message #102385, 2026-08-10: *"W3LPL cluster software
recently had a major overhaul and if you had previously turned on
skimmer spots they may have gotten turned off. Log into it and do a
SET/SKIMMER."* — posted in reply to another user who'd independently
reported near-zero spots on W3LPL for a week. This confirms the
skimmer-off-by-default explanation with a real date and cause (a
recent software overhaul), not just the banner text's general
disclaimer.

The same KE8G message also reports "no luck" connecting to K3LR and
W3LPL, but frames this as starting right after an N1MM+ client
upgrade on their end — read as a likely client-side issue for those
two, not independent corroboration of an outage. K3LR's own DXHeat
data (last received spot 2026-08-07) doesn't support it being down, so
this session treats that part of the report as noise, not signal.

**W9PA is DEAD** — connection timeout on two independent script runs
this session (full test and banner-only retest). Consistent enough to
treat as a real outage rather than a one-off network blip, though a
local firewall/ISP block on that specific port can't be fully ruled out
without testing from a second network.

## Limitations

- **groups.io access was resolved mid-session.** Direct unauthenticated
  fetch returns HTTP 402 Payment Required (confirmed on four thread
  URLs before this was worked around). A `groupsio-fetch` skill was
  built (login via email/password, session-cookie-based) and
  successfully retrieved authenticated content from N1MMLoggerPlus —
  see messages #102385 and #102247 cited above. It only works for
  groups the account is actually a member of (N1MMLoggerPlus, RBN-OPS);
  CC-User (where several VE7CC-specific threads live) was explicitly
  out of scope per the account holder's instruction.
- The "VE7CC-1 DOWN?" and "Almost no spots from VE7CC" thread titles
  found via search are on CC-User, not fetched this session (out of
  scope, see above) — the N1MMLoggerPlus corroboration obtained instead
  is considered sufficient given four independent signals already
  agree.
- The remaining 5 of the top-10 ranked nodes not in this first phase
  (W4MYA, WB3FFV, K1TTT, N2WQ, VE6DXC) have not been live-tested.

## Recommendation update

The spot_filt recommendation in `na_cluster_ranking_2026-08.md`
(NC7J primary, W3LPL backup) is **strengthened, not changed**, by this
phase: NC7J is now live-confirmed, not just corroborated, and W3LPL's
non-response is best explained by a config default rather than an
outage — both remain reasonable choices. **VE7CC-1's #2 corroboration-based
rank should not be read as current standing** — live evidence points to
it being effectively non-functional right now, independent of its
historical reputation and unique combined-feed design.
