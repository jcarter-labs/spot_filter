# Appendix: Per-Candidate Citations — NA Cluster Ranking (2026-08-30)

Full evidentiary backing for `na_cluster_ranking_2026-08.md`. Each claim
is tagged `[source class, date, sentiment]`. "Background knowledge" is
called out explicitly wherever a claim is not a dated, session-sourced
citation — these are given the lowest evidentiary weight in scoring.

## 1. NC7J — dxc.nc7j.com:7373 — AR-Cluster V6

- Live-tested filter grammar, bracket-expansion syntax, and field list
  (State=, SkimCQ, etc.), confirmed via direct echo-back from the node
  itself. `[first-party project ADR, 2026-06-20 to 2026-07-01, positive]`
  — source: `nc7j_filter_adr.md` ADR-1 through ADR-11 (this repo).
- Listed as active RBN-enabled AR-Cluster node. `[curated directory,
  2026-07-31 (NG3K page last-updated date), neutral]`
- No outage or negative-sentiment reports found in web/forum search this
  session. `[absence of evidence — not treated as positive signal, per
  the insufficient-data rule; scored via the ADR evidence above instead]`

## 2. VE7CC-1 — ve7cc.net — CC-Cluster (reference implementation)

- "VE7CC is a very reliable cluster, and there is no trouble connecting."
  `[web/forum search snippet, undated, positive]`
- Thread title "VE7CC-1 Cluster Down ... WX problems?" found on
  CC-User@groups.io. `[groups.io, undated — direct fetch returned HTTP
  402, negative]` — **contested against the item above; date could not
  be resolved.**
- CC-Cluster is the engine underlying other candidates on this list
  (N2WQ, W4MYA both run "CC-Cluster"). `[curated directory cross-
  reference, 2026-07-31, neutral — used as a community/adoption signal]`

## 3. W3LPL — w3lpl.net:7373 — AR-Cluster V6

- "Received DX spots through July 30, 2026... sent latest spots as of
  August 7, 2026." `[structured third-party site, DXHeat.com, dated
  2026-08-07, neutral]`
- "Skimmer cluster that functions well, though it generates a large
  volume of spots." `[web search snippet, undated, positive]`
- Reputation as a major multi-multi contest station: **background
  knowledge, not independently re-sourced with a dated citation this
  session** — Community axis capped at Moderate rather than High to
  reflect this.

## 4. WA9PIE-2 — hrd.wa9pie.net:8000 — DXSpider (cloud-hosted)

- NG3K lists this node as `dxc.wa9pie.net:8000`, Prosper, TX. `[curated
  directory, 2026-07-31, neutral]`
- ARRL article: rebuilt on Google Cloud at `hrd.wa9pie.net:8000` after a
  disk failure; claims "80 percent of the world's DX spots" peering and
  ~6,000 concurrent users; scales with Google Cloud compute. **Publish
  date confirmed via direct fetch: 2016** — initially misread from a
  search snippet as current-year; corrected after fetching the source
  directly. `[news/press, ARRL, 2016 — background/archival, not current-
  year evidence, positive]`
- Direct integration with N1MM Logger Plus (the logging software this
  project's own README targets). `[project documentation cross-
  reference, undated, neutral — used for Community/relevance axis]`
- **Contested**: no current-year source reconciles the `dxc.wa9pie.net`
  vs. `hrd.wa9pie.net` hostname discrepancy.

## 5. W9PA — dxc.w9pa.net:7373 — AR-Cluster V6

- "W9PA/4 sent its latest DX spot on 29-Mar-2026." `[structured third-
  party site, DXHeat.com, dated 2026-03-29, neutral]`
- "A server designed for distributing information to clusters such as
  NC7J, W9PA, VE7CC and W3LPL... all... operating as expected." `[web
  search snippet, undated, positive]`
- CW Skimmer-enabled. `[curated directory, 2026-07-31, neutral]`

## 6. W4MYA — dxc.w4mya.us:7373 — CC-Cluster

- Listed with explicit "Skimmer/FT4/FT8 capable" notation. `[curated
  directory, 2026-07-31, neutral]` — no independent forum/news
  corroboration found this session.

## 7. WB3FFV — dxc.wb3ffv.us:7300 — DXSpider

- Listed with explicit "IPv4/v6 capable" notation. `[curated directory,
  2026-07-31, neutral]` — no independent forum/news corroboration found
  this session.

## 8. K1TTT — k1ttt.net:7373 — AR-Cluster

- Listed as an active AR-Cluster node. `[curated directory, 2026-07-31,
  neutral]`
- Targeted searches for 2026 status/outage/reliability discussion
  returned no relevant results. `[search attempted, no results —
  scored as insufficient data per the explicit rule, not as either
  robust or weak]`
- Long-standing reputation as a major multi-multi contest station:
  **background knowledge, not independently re-sourced this session.**

## 9. N2WQ — cluster.n2wq.com:7373 — CC-Cluster

- Included in NG3K's curated list, whose own stated criterion is "a
  representative selection of normally reliable and consistent nodes."
  `[curated directory, 2026-07-31, positive — inherits NG3K's own
  editorial vetting]` — no independent forum/news corroboration found
  this session.

## 10. VE6DXC — dx.middlebrook.ca:8000 — DXSpider

- Listed in NG3K's directory. `[curated directory, 2026-07-31, neutral]`
  — no independent forum/news corroboration found this session; weakest
  evidence base of the 10, included primarily for NA-wide geographic and
  software-family diversity per the widened scope decision.

## Excluded from the top 10

- **telnet.reversebeacon.net:7000/7001** — RBN's own master relay.
  Explicitly documented as having "no filtering features," which fails
  the Capability axis outright for a filter-driven use case like
  `spot_filt`. `[first-party site content, undated, neutral]`
- Remaining NG3K-listed US nodes not shortlisted (K4ZR, W6CUA, KM6HBH-1,
  W6RFU, N6WS-6, N7OD, W9AEK, NX9G, AI9T, K0WL) and Canadian nodes
  (VE9SC, VE9EMO, VY2CC) — single-source (NG3K-only) corroboration with
  no differentiating capability/community signal found this session;
  omitted in favor of the 10 with either stronger or more distinctive
  evidence. Available for a future research pass if the top 10 need
  expansion.
- No Mexican (XE) node was identified in any source checked this
  session.

## Access limitations encountered this session

- groups.io: direct fetch of at least one thread
  (`groups.io/g/N1MMLoggerPlus/topic/working_dx_cluster_list/37494303`)
  returned HTTP 402 Payment Required. All groups.io evidence above comes
  from search-engine snippets only, which are lower-fidelity and
  sometimes undated.
- W3RGA's spot-volume CSV (`w3rga.ddns.net:73/w3rga/top-spotter/...`)
  could not be retrieved — the redirect target serves plain HTTP on a
  non-standard port, and this session's fetch tooling auto-upgrades to
  HTTPS, which that port doesn't support. This is why DXHeat.com
  "latest spot" dates were used as the feed-richness/reachability proxy
  instead of W3RGA's objective volume numbers.
