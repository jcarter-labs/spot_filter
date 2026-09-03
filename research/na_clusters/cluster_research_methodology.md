# Methodology: NA DX Cluster Server Research

Documented agentic workflow used to produce `na_cluster_ranking_2026-08.md`
and its appendix. This is a methodology record, not a runnable tool — the
steps below were executed manually (via WebSearch/WebFetch and direct
research) in a single session on 2026-08-30.

## Scope

North America-hosted telnet DX cluster nodes (US, Canada, Mexico), plus
RBN-affiliated aggregator nodes (e.g. VE7CC's combined feed). Widened from
an initial US-only scope specifically to avoid a candidate pool that
collapses to 5-6 well-known names padded out to 10 — a risk an independent
review of the draft plan flagged directly (see "External validation"
below). No Mexican (XE) node was identified in the sources checked this
session; the report notes this rather than forcing a placeholder entry.

## Steps

1. **Seed candidate list** — pulled from `rbn_reference_sites.md`'s
   already-vetted directories (NG3K's telnet cluster/skimmer list,
   skimmer.dxwatch.com), expanded via open web search for
   dxcluster.info's telnet directory and VE7CC-family nodes (Canadian).
   NG3K's full node table (36 entries, last updated 2026-07-31) was the
   primary seed; filtered to NA-hosted only.
2. **Evidence gathering per candidate**, across source classes: curated
   directories (NG3K, dxcluster.info), first-party project evidence (this
   repo's own live-tested `../../adr/nc7j_filter_adr.md`, dated 2026-06-20 through
   2026-07-01), structured third-party activity data (DXHeat.com
   per-node "latest spot" timestamps, used as a dated, non-forum
   reachability proxy — the W3RGA spot-volume CSV that was originally
   planned as the feed-richness input was **not** accessible this
   session, see Limitations), news/press (ARRL, eHam), and groups.io
   threads (accessed only via search-result snippets — direct fetch
   returned HTTP 402/paywalled, see Limitations). Each finding was tagged
   with source class, publish date, and a sentiment tag
   (positive/negative/neutral) rather than just counted.
3. **Corroboration + recency + sentiment scoring** — claims were weighted
   by source-class diversity, recency (this-year weighted highest), and
   sentiment, so a complaint thread and a praise thread are not treated
   as equal-strength "the node exists" signal. One finding was caught and
   corrected by this step: a search snippet implied "as of August 9"
   activity for WA9PIE-2's Google Cloud migration read as current-year;
   fetching the source (ARRL article) directly showed a publish date of
   **2016**, not 2026. It was rescored as archival background, not
   current-year evidence — a direct illustration of why source dates were
   independently verified rather than trusted from search snippets alone.
4. **Reflection checkpoint 1 (conflict surfacing)** — applied explicit
   rules rather than averaging silently:
   - VE7CC: general positive sentiment found ("very reliable... no
     trouble connecting") conflicts with a groups.io thread titled
     "VE7CC-1 Cluster Down ... WX problems?" whose date could not be
     confirmed (groups.io access blocked). Marked **contested** rather
     than resolved either way.
   - WA9PIE-2: NG3K's 2026-07-31 listing shows host `dxc.wa9pie.net:8000`
     (Prosper, TX); the (2016) ARRL article names `hrd.wa9pie.net:8000`
     (Google Cloud). No current-year source reconciles which hostname is
     live. Marked **contested**.
   - K1TTT: no current-year corroboration found in either direction
     despite searching directly. Marked **insufficient data** rather than
     scored as robust-by-silence or weak-by-silence.
5. **Composite scoring** — four axes, each scored 0 (insufficient) to 3
   (high): **Reachability** (corroboration+sentiment-derived recency
   signal — explicitly not live-probed), **Feed richness** (RBN
   integration / mode coverage / volume claims — DXHeat "latest spot"
   date used as the available structured proxy, see Limitations),
   **Capability** (filter grammar family *and* feature depth within it —
   NC7J's SpotterState/SpotterCont fields, directly confirmed via this
   project's own live echo-test in `../../adr/nc7j_filter_adr.md`, count for more
   than a bare grammar-family listing), and **Community/support**
   (independent sentiment and node-to-node adoption, e.g. other nodes
   running VE7CC's own CC-Cluster engine). General ham-community
   reputation not backed by a dated, session-sourced citation (e.g. "W3LPL
   is a well-known superstation") was capped at Moderate rather than High
   on the Community axis, to keep the score honest about evidence
   quality — see the appendix for which claims are dated citations vs.
   background knowledge.
6. **Reflection checkpoint 2 (sanity check)** — cross-checked the
   emerging top-10 against NC7J's own documented AR-Cluster V6 support
   and NG3K's curation bar. 10 genuinely distinguishable candidates were
   available across three grammar families (AR-Cluster, CC-Cluster,
   DXSpider) and two countries (US, Canada) without padding.
7. **Report generation** — one-page summary table with confidence/
   contested flags, plus a separate appendix carrying every claim's
   source class, date, and sentiment tag.

## Password/access gate

Per NG3K's own stated exclusion criterion ("no longer list[s] nodes
requiring passwords"), telnet-login password requirements were tracked as
a **flagged caveat**, not a hard exclusion, per this session's
requirements — none of the shortlisted 10 were found to require a login
password beyond callsign, largely because the candidate pool draws heavily
from NG3K's own already-filtered list.

## Limitations (explicit, not glossed over)

- **No live telnet verification was performed.** All reachability/status
  signal is corroboration-based. This is a known limitation, not an
  oversight — see "Deferred next phase" below.
- **groups.io threads could not be fetched directly** (HTTP 402 on at
  least one thread tested) — evidence from groups.io is limited to
  search-engine snippet text, which is lower-fidelity and sometimes
  undated. This mirrors a limitation already documented in
  `rbn_reference_sites.md` for reversebeacon.net's robots.txt block.
- **W3RGA's spot-volume CSV was inaccessible this session** — the
  redirect target uses plain HTTP on a non-standard port that this
  session's fetch tooling could not reach (auto-upgrades to HTTPS, which
  the server doesn't support on that port). DXHeat.com's per-node
  "latest spot" date was used as a substitute structured, dated
  reachability signal, but it does not give volume/throughput numbers.
  A future session with direct HTTP/curl access could retrieve the CSV
  and re-score the feed-richness axis with real volume data.
- **General ham-community reputation** (e.g., a station's decades-long
  standing as a major contest superstation) was drawn on for a few
  entries but is explicitly *not* a dated, session-sourced citation —
  flagged as such everywhere it's used, and capped at Moderate rather
  than High confidence to avoid overstating rigor.

## Deferred next phase (not executed this session)

A future live smoke test — real telnet login + a short spot-capture
window — against the top-10 shortlist only, to validate this
corroboration-based ranking against ground truth (actual reachability,
latency, and spot flow, none of which corroboration can measure
directly). This is explicitly out of scope for this session per the
user's decision to keep research and live verification as separate
phases.

## External validation performed on the draft plan

Before this methodology was finalized, the draft was checked two ways:
an independent cold-read critique by a fresh agent with no session
context (surfaced the popularity-vs-robustness scoring risk, addressed by
sentiment-tagging and the insufficient-data rule; underspecified
conflict-handling, addressed by the explicit tie-break rules above; and
axis redundancy, addressed by sourcing Community-axis evidence from
mentions not already counted toward Reachability); and a cross-check
against how sources already used in this project (NG3K, W3RGA) define
quality themselves, which surfaced the password-exclusion criterion and
the objective-volume-metric idea (only partially usable this session, per
Limitations above).
