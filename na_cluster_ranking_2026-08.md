# North America DX Cluster Server Ranking — 2026-08-30

Corroboration-based ranking of 10 North America-hosted telnet DX cluster /
RBN-aggregator nodes. **Not live-verified** — scores derive from published
directories, this project's own prior live testing of NC7J, structured
third-party activity data, and community sentiment found this session
(full citations in the companion appendix). Composite = sum of 4 axes
(Reachability, Feed richness, Capability, Community), each 0–3; see
`cluster_research_methodology.md` for the scoring rules, including how
conflicting or absent evidence is flagged rather than hidden.

| # | Node | Host:Port | Software | Composite | Strength | Risk / Flag |
|---|------|-----------|----------|:---:|----------|----------|
| 1 | **NC7J** | dxc.nc7j.com:7373 | AR-Cluster V6 | **10** | Only node with directly-tested filter-grammar depth (this project's own ADR work) | No independent third-party sentiment found |
| 2 | VE7CC-1 | ve7cc.net | CC-Cluster (reference impl.) | 9 | Unique combined RBN+manual feed; engine adopted by other nodes on this list | **Contested** — praise vs. an undated groups.io "cluster down" thread |
| 3 | W3LPL | w3lpl.net:7373 | AR-Cluster V6 | 8 | Active through Aug 2026 (dated); Skimmer-enabled | Community score capped — reputation is background knowledge, not a dated citation |
| 4 | WA9PIE-2 | hrd.wa9pie.net:8000 (NG3K lists dxc.wa9pie.net) | DXSpider (cloud-hosted) | 8 | Direct N1MM Logger Plus tie-in — most relevant to this project's own logging stack | **Contested** — hostname conflict between sources; core evidence is a 2016 article, not current-year |
| 5 | W9PA | dxc.w9pa.net:7373 | AR-Cluster V6 | 7 | CW Skimmer; part of core relay group with NC7J/W3LPL/VE7CC | Latest confirmed activity 29-Mar-2026 — stale relative to report date |
| 6 | W4MYA | dxc.w4mya.us:7373 | CC-Cluster | 6 | Explicit FT4/FT8 + Skimmer mode coverage | Single-source (NG3K only) corroboration |
| 7 | WB3FFV | dxc.wb3ffv.us:7300 | DXSpider | 5 | Explicit IPv4/IPv6 dual-stack — real differentiator | Single-source corroboration |
| 8 | K1TTT | k1ttt.net:7373 | AR-Cluster | 5 | Long-established grammar support | **Insufficient data** — no 2026 corroboration found either direction |
| 9 | N2WQ | cluster.n2wq.com:7373 | CC-Cluster | 5 | Meets NG3K's own "reliable and consistent" curation bar | Single-source corroboration |
| 10 | VE6DXC | dx.middlebrook.ca:8000 | DXSpider | 4 | Canadian geographic/software diversity (NA-wide scope) | Single-source corroboration; weakest evidence base of the 10 |

No password-required telnet login found on any of the 10 (inherited
largely from NG3K's own exclusion of password-gated nodes).

## Recommendation for spot_filt

**Keep NC7J as primary.** It ranks #1 and is the only node with directly
verified filter-grammar depth — this project's own live-tested ADR work
(`nc7j_filter_adr.md`) is stronger evidence than anything corroboration
alone can provide for the other 9.

**Add W3LPL (#3) as backup, not VE7CC (#2) despite its higher score.**
`spot_filter.py` currently only implements AR-Cluster V6 grammar — CC-Cluster
and DXSpider are stubbed out (README). W3LPL shares NC7J's exact grammar
family, so it's usable as a backup with zero code changes. VE7CC's higher
composite reflects real strengths (unique combined feed, engine adoption)
but is gated behind implementing the currently-stubbed CC-Cluster grammar
first — worth revisiting once/if that work happens.

**Do not act on WA9PIE-2's ranking yet.** Its position rests on
contested/stale evidence (see flags above); the next live smoke-test phase
(deferred, not run this session) should resolve the hostname conflict
before it's considered further.
