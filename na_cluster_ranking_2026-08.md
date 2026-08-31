# North America DX Cluster Server Ranking — 2026-08-30

Ranking of North America-hosted telnet DX cluster / RBN-aggregator
nodes, combining the original corroboration-based research
(`cluster_research_methodology.md`, full citations in the appendix)
with **Phase 1 live-verification results** (`live_verification_2026-08-30.md`)
for the top 5 candidates, tested by direct telnet connection under
callsign N6YU. Composite = sum of 4 corroboration axes (Reachability,
Feed richness, Capability, Community), each 0–3 — see the methodology
doc for scoring rules. **Two nodes confirmed non-functional by live
testing have been pulled out of the ranked table below** rather than
left in with a stale score; see that section.

| # | Node | Host:Port | Software | Composite | Live status | Strength | Risk / Flag |
|---|------|-----------|----------|:---:|---|----------|----------|
| 1 | **NC7J** | dxc.nc7j.com:7373 | AR-Cluster V6 | **10** | **LIVE — confirmed, 3 spots/5.4s** | Only node with directly-tested filter-grammar depth (this project's own ADR work) | No independent third-party sentiment found |
| 2 | **WA9PIE-2** | dxc.wa9pie.net:8000 (= hrd.wa9pie.net:8000, confirmed same backend) | DXSpider (cloud-hosted) | 8 | **LIVE — confirmed, 3 spots/34.3s** | Direct N1MM Logger Plus tie-in; hostname conflict fully resolved by live test | Not usable as a spot_filt backup yet — DXSpider grammar is stubbed out in `spot_filter.py` |
| 3 | W3LPL | w3lpl.net:7373 | AR-Cluster V6 | 8 | **LIVE — reachable**, full banner + login prompt confirmed | Active through Aug 2026 (dated); same grammar family as NC7J | Spot-volume untested live — banner confirms CW skimmer is off by default (`set/skimmer` needed for a real volume read) |
| 4 | W4MYA | dxc.w4mya.us:7373 | CC-Cluster | 6 | Not yet live-tested | Explicit FT4/FT8 + Skimmer mode coverage | Single-source (NG3K only) corroboration |
| 5 | WB3FFV | dxc.wb3ffv.us:7300 | DXSpider | 5 | Not yet live-tested | Explicit IPv4/IPv6 dual-stack — real differentiator | Single-source corroboration |
| 6 | K1TTT | k1ttt.net:7373 | AR-Cluster | 5 | Not yet live-tested | Long-established grammar support | **Insufficient data** — no 2026 corroboration found either direction |
| 7 | N2WQ | cluster.n2wq.com:7373 | CC-Cluster | 5 | Not yet live-tested | Meets NG3K's own "reliable and consistent" curation bar | Single-source corroboration |
| 8 | VE6DXC | dx.middlebrook.ca:8000 | DXSpider | 4 | Not yet live-tested | Canadian geographic/software diversity (NA-wide scope) | Single-source corroboration; weakest evidence base |

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

**Keep W3LPL as backup — now on stronger footing.** It's live-confirmed
reachable (full banner, login prompt) and shares NC7J's exact
AR-Cluster V6 grammar, so it remains usable with zero code changes to
`spot_filter.py`. Its spot-volume claim is still unconfirmed live
(skimmer defaults off), but that's a config detail, not a reachability
question — the earlier "not down" hunch was right.

**WA9PIE-2 is now live-confirmed and its hostname conflict is fully
resolved, but it's still not a drop-in backup.** `spot_filter.py` only
implements AR-Cluster V6 grammar; WA9PIE-2 runs DXSpider, same gap that
applied to VE7CC. Worth keeping in mind as a second-tier option if
DXSpider grammar support is ever added — not actionable today.

**VE7CC-1's #2 corroboration-based rank should be treated as void.**
Live evidence is unambiguous: it's down, not just contested.
