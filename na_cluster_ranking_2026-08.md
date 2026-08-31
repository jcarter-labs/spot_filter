# North America DX Cluster Server Ranking — 2026-08-30

Ranking of North America-hosted telnet DX cluster / RBN-aggregator
nodes, combining the original corroboration-based research
(`cluster_research_methodology.md`, full citations in the appendix)
with **live-verification results** (`live_verification_2026-08-30.md`
and `live_verification_remaining5_2026-08-30.md`) for **all 10**
originally-ranked candidates, tested by direct telnet connection under
callsign N6YU. Composite = sum of 4 corroboration axes (Reachability,
Feed richness, Capability, Community), each 0–3 — see the methodology
doc for scoring rules. **Two nodes confirmed non-functional by live
testing have been pulled out of the ranked table below** rather than
left in with a stale score; see that section.

| # | Node | Host:Port | Software | Composite | Live status | Strength | Risk / Flag |
|---|------|-----------|----------|:---:|---|----------|----------|
| 1 | **NC7J** | dxc.nc7j.com:7373 | AR-Cluster V6 | **10** | **LIVE — confirmed, 3 spots/5.4s** | Only node with directly-tested filter-grammar depth (this project's own ADR work) | No independent third-party sentiment found |
| 2 | **WA9PIE-2** | dxc.wa9pie.net:8000 (= hrd.wa9pie.net:8000, confirmed same backend) | DXSpider (cloud-hosted) | 8 | **LIVE — confirmed, 3 spots/34.3s** | Direct N1MM Logger Plus tie-in; hostname conflict fully resolved by live test | Not usable as a spot_filt backup yet — DXSpider grammar is stubbed out in `spot_filter.py` |
| 3 | W3LPL | w3lpl.net:7373 | **DXSpider** (corrected — see below) | 8 | **LIVE — confirmed, 3 spots/5.8s after `set/skimmer`** | 20d 11h uptime, 398 connected users at test time; capabilities `ve7cc rbn` | **Not AR-Cluster V6 as previously recorded** — not a zero-code-change spot_filt backup after all, same DXSpider-grammar gap as VE7CC/WA9PIE-2 |
| 4 | W4MYA | dxc.w4mya.us:7373 | CC-Cluster (confirmed) | 6 | **ALIVE, 0 spots/60s** — banner confirms skimmer off by default (`set/skimmer` needed), same pattern as W3LPL | Explicit FT4/FT8 + Skimmer mode coverage | Untested with skimmer enabled — likely fine, not confirmed |
| 5 | WB3FFV | dxc.wb3ffv.us:7300 | DXSpider (confirmed) | 5 | **LIVE — confirmed, 3 spots/49.3s** | Explicit IPv4/IPv6 dual-stack — real differentiator | None remaining — fully live-confirmed |
| 6 | **K1TTT** | k1ttt.net:7373 | **AR-Cluster (confirmed live — version unconfirmed)** | 5 | **ALIVE, marginal — 2 spots/60s** (below 3-spot bar) | **Only other AR-Cluster-family node confirmed besides NC7J** — real zero-code-change backup candidate if version matches V6 | Version not yet confirmed as V6 specifically; spot volume modest |
| 7 | N2WQ | cluster.n2wq.com:7373 | CC-Cluster (confirmed) | 5 | **LIVE — confirmed, 3 spots/33.0s** | Meets NG3K's own "reliable and consistent" curation bar | None remaining — fully live-confirmed |
| 8 | VE6DXC | dx.middlebrook.ca:8000 | DXSpider (confirmed) | 4 | **ALIVE, weak — 1 spot/60s** | Canadian geographic/software diversity (NA-wide scope) | Low live spot volume — weakest live signal of the alive nodes |

No password-required telnet login found on any of the above (inherited
largely from NG3K's own exclusion of password-gated nodes).

## Confirmed non-functional — pulled from the ranking

**VE7CC-1** (`ve7cc.net:7373`, `dxc.ve7cc.net:23`) — **DOWN.** Live
telnet connections succeed at the TCP level but the server sends
nothing at all — not even a login prompt — on either port, even after
a CRLF nudge, tested twice. Corroborated by DXHeat.com's structured
data: last *received* spot 2026-06-12 (11 weeks stale as of this
report), last *sent* spot 2025-09-24 (~11 months stale). This was
previously ranked #2 (composite 9) on corroboration alone — full
history and evidence in `live_verification_2026-08-30.md`.

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

**K1TTT is the real zero-code-change backup candidate — pending one
more check.** Of all 10 candidates tested live, it's the only other
node confirmed running actual AR-Cluster software (banner: *"Welcome
to the K1TTT AR-Cluster Telnet Server"*), the same family NC7J runs and
the only family `spot_filter.py` implements. Its live spot volume was
marginal (2 spots in 60s, just under the 3-spot bar) and its exact
AR-Cluster **version** hasn't been confirmed — the ADR-documented filter
grammar in this project is specific to V6, and older AR-Cluster
versions may differ. Recommend a follow-up check of K1TTT's version
banner/`HELP` output before promoting it to backup status.

**WB3FFV and N2WQ are both fully live-confirmed** (3/49.3s and
3/33.0s respectively) but remain gated behind their DXSpider/CC-Cluster
grammar not being implemented in `spot_filter.py` — same status as
W3LPL and WA9PIE-2.

**VE7CC-1's #2 corroboration-based rank should be treated as void.**
Live evidence is unambiguous: it's down, not just contested.
