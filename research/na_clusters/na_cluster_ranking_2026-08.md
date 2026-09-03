# North America DX Cluster Server Ranking — 2026-08-30

Ranking of North America-hosted telnet DX cluster / RBN-aggregator
nodes, combining the original corroboration-based research
(`cluster_research_methodology.md`, full citations in the appendix)
with **live-verification results** (`live_verification_2026-08-30.md`
and `live_verification_remaining5_2026-08-30.md`) for **all 10**
originally-ranked candidates, tested by direct telnet connection under
callsign N6YU. Composite = sum of 4 corroboration axes (Reachability,
Feed richness, Capability, Community), each 0–3 — see the methodology
doc for scoring rules. **VE7CC-1 has been removed from consideration
entirely** — confirmed offline with no expectation of return (see
below); it no longer appears anywhere in this file except as a note.
**W9PA is confirmed non-functional** and shown separately, not in the
ranked table, pending possible retest.

| # | Node | Host:Port | Software | Composite | Live status | Strength | Risk / Flag |
|---|------|-----------|----------|:---:|---|----------|----------|
| 1 | **NC7J** | dxc.nc7j.com:7373 | AR-Cluster V6 | **10** | **LIVE — confirmed, 3 spots/5.4s** | Only node with directly-tested filter-grammar depth (this project's own ADR work) | No independent third-party sentiment found |
| 2 | **WA9PIE-2** | dxc.wa9pie.net:8000 (= hrd.wa9pie.net:8000, confirmed same backend) | DXSpider (cloud-hosted) | 8 | **LIVE — confirmed, 3 spots/34.3s** | Direct N1MM Logger Plus tie-in; hostname conflict fully resolved by live test | Not usable as a spot_filt backup yet — DXSpider grammar is stubbed out in `spot_filter.py` |
| 3 | W3LPL | w3lpl.net:7373 | **DXSpider** (corrected — see below) | 8 | **LIVE — confirmed, 3 spots/5.8s after `set/skimmer`** | 20d 11h uptime, 398 connected users at test time; capabilities `ve7cc rbn` | **Not AR-Cluster V6 as previously recorded** — not a zero-code-change spot_filt backup after all, same DXSpider-grammar gap as VE7CC/WA9PIE-2 |
| 4 | W4MYA | dxc.w4mya.us:7373 | CC-Cluster v3.397 (confirmed) | 6 | **LIVE — confirmed, 3 spots/23.9s after `set/skimmer`** | Explicit FT4/FT8 + Skimmer mode coverage; 80 nodes/537 total users on its network per live stats | Uptime only 4d 9h at test time (vs. W3LPL's 20d) — shorter but not concerning on its own |
| 5 | WB3FFV | dxc.wb3ffv.us:7300 | DXSpider (confirmed) | 5 | **LIVE — confirmed, 3 spots/49.3s** | Explicit IPv4/IPv6 dual-stack — real differentiator | None remaining — fully live-confirmed |
| 6 | **K1TTT** | k1ttt.net:7373 | **AR-Cluster V6.1.5061 (confirmed)** | 5 | **ALIVE, marginal — 2 spots/60s** (below 3-spot bar) | **Confirmed AR-Cluster V6 — genuine zero-code-change backup for spot_filt**, same grammar family/major version as NC7J | Live spot volume modest in the one test window; version confirmed by account owner (K1TTT sysop info), not independently re-verified via HELP output |
| 7 | N2WQ | cluster.n2wq.com:7373 | CC-Cluster (confirmed) | 5 | **LIVE — confirmed, 3 spots/33.0s** | Meets NG3K's own "reliable and consistent" curation bar | None remaining — fully live-confirmed |
| 8 | VE6DXC | dx.middlebrook.ca:8000 | DXSpider (confirmed) | 4 | **ALIVE, weak — 1 spot/60s** | Canadian geographic/software diversity (NA-wide scope) | Low live spot volume — weakest live signal of the alive nodes |

No password-required telnet login found on any of the above (inherited
largely from NG3K's own exclusion of password-gated nodes).

## Removed from consideration

**VE7CC-1** (`ve7cc.net:7373`, `dxc.ve7cc.net:23`) — **offline, not
expected to return.** Confirmed by four independent, dated signals
(silent TCP port even after a nudge, DXHeat's stale activity dates, a
first-hand dated groups.io report, and multiple community thread
titles) — see `live_verification_2026-08-30.md` for the full evidence
trail. Was previously ranked #2 (composite 9) on corroboration alone.
Dropped from the ranked table and from active tracking; not expected to
be retested in future rounds absent new information.

## Confirmed non-functional — pulled from the ranking

**W9PA** (`dxc.w9pa.net:7373`) — **DEAD.** TCP connection itself timed
out on two independent test runs this session. Previously ranked #5
(composite 7). Local network/firewall false-negative can't be fully
ruled out without testing from a second network, but two consistent
failures is a real signal, not a fluke.

## Recommendation for spot_filt

**Keep NC7J as primary.** It ranks #1, is now live-confirmed (not just
corroborated), and is the only node with directly verified
filter-grammar depth via this project's own live-tested ADR work.

**W3LPL is fully live-confirmed (3 spots in 5.8s after `set/skimmer`)
but is NOT a zero-code-change backup after all.** A retest surfaced
that NG3K's directory (and this ranking, copied from it) had the wrong
software family: W3LPL's live banner identifies it as
`"W3LPL-Beta DX-Spider Telnet Server," running DXSpider V1.57` — not
AR-Cluster V6. Same DXSpider-grammar gap as VE7CC and WA9PIE-2 applies.
This was a real error in the sourced data, not just staleness — worth
remembering that NG3K's software-family field isn't fully reliable and
should be live-checked before being load-bearing for a recommendation.

**WA9PIE-2 is live-confirmed and its hostname conflict is fully
resolved, but it's also DXSpider** — not a drop-in backup either, for
the same reason.

**K1TTT is the confirmed backup: AR-Cluster V6.1.5061, same major
version family as NC7J.** Of all 10 candidates tested live, it's the
only other node running AR-Cluster — and its version (V6.1.5061,
confirmed) matches the V6 generation this project's ADR work
(`../../adr/nc7j_filter_adr.md`) already documents the filter grammar for. Live
spot volume was modest in the one test window (2 spots/60s) — not
disqualifying, but worth a longer retest before relying on it
operationally.

**W4MYA, WB3FFV, and N2WQ are all now fully live-confirmed**
(3/23.9s, 3/49.3s, and 3/33.0s respectively, W4MYA needing
`set/skimmer` like W3LPL did) but all remain gated behind their
CC-Cluster/DXSpider grammar not being implemented in `spot_filter.py`
— same status as W3LPL and WA9PIE-2. W4MYA's sysop also mentioned a
new node in testing, `dxc.w4mya.us:8300` ("Go-Cluster"), not previously
in any source checked this session — noted for a future research round,
not evaluated here.

## Updated spot_filt configuration recommendation

**Primary: NC7J** (`dxc.nc7j.com:7373`) — unchanged, live-confirmed,
deepest tested grammar coverage.
**Backup: K1TTT** (`k1ttt.net:7373`) — AR-Cluster V6.1.5061, confirmed
live, same grammar family as NC7J, usable with zero code changes to
`spot_filter.py`. This replaces the earlier (incorrect) W3LPL backup
recommendation, which was based on a wrong software-family listing in
NG3K's directory.
