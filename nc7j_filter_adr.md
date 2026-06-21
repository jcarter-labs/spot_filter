# Architecture Decision Record: NC7J DX Cluster Filter Configuration

**Date:** 2026-06-20
**Status:** Filter syntax confirmed active on live session; semantic validation pending
**Context:** DX cluster filter configuration for contest band monitoring, spot-density proxy display project

---

## ADR-1: Cluster node selection — NC7J (AR-Cluster 6.1, +RBN)

- **Decision:** Connect to NC7J (`dxc.nc7j.com:7373`, Syracuse, UT) as primary cluster node for contest filtering, despite node location being geographically unrelated to West Coast QTH.
- **Rationale:** Cluster node geography does not determine spot propagation fidelity — **spotter geography does**. NC7J is RBN-enabled and supports the AR-Cluster V6 filter grammar required for spotter-level filtering. Already established in prior sessions as a principle: "spotter geography, not cluster node geography, determines propagation fidelity."
- **Note:** NC7J-5 (port 7374) defaults to FT-mode RBN spots from NA origin — different default filter scope than NC7J primary (7373). Primary (7373) used for this filter.

## ADR-2: Filter command grammar — AR-Cluster `SET DX FILTER`, not DX Spider `set/filter`

- **Decision:** Use `SET DX FILTER <expression>` as the base command.
- **Rejected:** `set/filter spot Field=Value` (DX Spider syntax) — confirmed via live `Unknown command` error on NC7J.
- **Discovery path:** `HELP` → `HELP DX` → `HELP SET DX` → `HELP SET DX FILTER` (iterative, required live verification at each step; no working syntax found via documentation guesswork alone).
- **Failure mode flagged:** AR-Cluster, DX Spider, and CC Cluster implement materially different filter command grammars. Do not assume cross-compatibility between cluster software families when porting filter strings.

## ADR-3: Filter field reference — ab5k.net is dead; use AR-Cluster V6 Telnet User Manual instead

- **Decision:** `HELP` text on NC7J points to `www.ab5k.net` for extended filter documentation. **This domain is squatted/parked (generic WordPress site, no relevant content) as of 2026-06-20.**
- **Replacement reference:** AR-Cluster V6 Telnet User Manual, archived copies at:
  - `https://www.k3lr.com/w9zrx/AR-Cluster%20Filter%20Commands.pdf`
  - `https://cms.reversebeacon.net/sites/cms.reversebeacon.net/files/2018/04/26/AR-ClusterV6%20Filter%20Commands.pdf`
  - `https://www.n5pa.com/ham.arcluster.php` (worked examples, incl. contest filter templates)
- **Action item:** Update any internal documentation or onboarding notes that reference ab5k.net.

## ADR-4: Confirmed full filter field list (AR-Cluster V6)

```
Call, Cty, State, County, ArrlSection, Cont, CqZone, ItuZone, Band, Mode,
Spotter, SpotterNode, SpotterCty, SpotterState, SpotterCont, Grid, Name,
SpotterCqZone, SpotterItuZone
```

- Spotted-station fields (no prefix) and spotter fields (`Spotter*` prefix) are **independent filter dimensions** — do not conflate spotted-DX-location filtering with spotter-receive-location filtering. This was an early error in this session (attempting `State=WV` while intending spotter-side logic, and vice versa) and is the most likely recurring mistake for this project.
- `Spotter` (not `SpotterCall`) is the correct field for filtering by spotter callsign. Corrected from an earlier incorrect guess (`SpotterCall=`) made mid-session.

## ADR-5: Boolean/grouping syntax confirmed

- `AND`, `OR`, `NOT` operators are valid and combinable with parentheses for grouping.
- Bracket shorthand `Field=[v1,v2,v3]` expands to `Field=v1 OR Field=v2 OR Field=v3` — confirmed both in documentation and via live echo from NC7J (`SHow Dx Options` round-trip).
- `-#` suffix on a callsign acts as an SSID wildcard (matches base call and all `-N` SSID variants), e.g. `KW7MM-#` matches `KW7MM`, `KW7MM-1`, `KW7MM-2`, etc.
- `NOT <field>` and `<field>=0` are equivalent for boolean filter terms — confirmed via live echo: submitted `NOT SkimBusted`, cluster echoed back `SkimBusted=0`. This is parser normalization, not an error.

## ADR-6: `SkimCQ` is redundant for RBN-sourced spots

- **Finding:** `SkimCQ` filters for "skimmer spot of a station calling CQ" — unnecessary when the spot source is RBN or an RBN-bridging cluster, since RBN only propagates spots of CQ-calling stations by design.
- **Decision:** `SkimCQ` may be included or omitted with no functional difference for NC7J (RBN-fed). Left in the active filter for this session; safe to remove in future revisions for clarity.

## ADR-7: State-based filtering reliability

- `State=` (spotted-station side) is **confirmed supported** on this AR-Cluster build via live `SHow Dx Options` echo (`Filter: state = wv`).
- **Open risk, not yet resolved:** semantic correctness of state-to-prefix mapping was not validated against a known live WV spot in this session. The 8th call district (W8/K8/N8/etc.) spans WV, OH, and MI — prefix-based inference is inherently ambiguous; cluster's internal DXCC/state lookup table is assumed authoritative but unverified.
- **Action item:** Validate `State=WV` against a confirmed live WV station spot before relying on it operationally.

## ADR-8: Active contest filter (confirmed live, syntax-valid)

Submitted and echoed back successfully by NC7J:

```
SET DX FILTER Skimmer AND SkimCQ AND NOT SkimBusted AND Mode=CW AND
(Band=40 OR Band=20 OR Band=15 OR Band=10) AND
(Spotter=[KW7MM-#,KW7MM-2-#,VE6JY-#,W6YX-#,ND7K-#,VE6WZ-#,N6TV-#,VE7CC-#,KH6LC-#])
```

Cluster echo (`SHow Dx Options`), normalized form:

```
skimmer and skimcq and skimbusted=0 and mode = cw and
(band = 40 or band = 20 or band = 15 or band = 10) and
(spotter = kw7mm-# or spotter = kw7mm-2-# or spotter = ve6jy-# or
 spotter = w6yx-# or spotter = nd7k-# or spotter = ve6wz-# or
 spotter = n6tv-# or spotter = ve7cc-# or spotter = kh6lc-#)
```

- **Status:** Syntactically valid and active on NC7J as of this session. **Semantic validation pending** — not yet confirmed against live contest traffic that spots are (a) arriving at all from the listed spotters, and (b) correctly restricted to CW/40-20-15-10.
- **Known risk:** If none of the nine listed spotters are online/skimming at test time, filter will silently return zero spots — indistinguishable from a broken filter. Check `SHow/Skimmer` to confirm spotter availability before troubleshooting filter logic.

## ADR-9: WV QSOP — DX-side state filtering workflow

- **Finding:** `State=WV` (spotted-station side) is a wholesale-replace operation, same as any other `SET DX FILTER` call — confirmed no partial/incremental term removal exists on this cluster (no `unset`/`remove-term` command; see AR-Cluster V6 manual, "Set DX Filter" section). Testing a one-off location filter like `State=WV` overwrites the standing ADR-8 contest filter entirely; it is not additive.
- **Decision:** Treat any one-off `State=`/`Cty=`/`Cont=` diagnostic check as a full filter swap requiring explicit restoration afterward, not a toggle. After testing, resubmit the full standing filter string from scratch (e.g. ADR-8) rather than assuming a partial undo is possible.
- **Procedure for testing a DX-side state filter without losing the standing filter:**
  1. `show/dx/options` — confirm current filter before changing anything.
  2. Submit the one-off test filter (e.g. `SET DX FILTER State=WV`).
  3. `SET DX MODE DEBUG` if live +/- validation is wanted; otherwise leave in `FILTER` mode.
  4. Test/observe.
  5. Resubmit the full standing filter string (ADR-8 or current contest variant) verbatim.
  6. `SET DX MODE FILTER` — confirm debug mode is turned back off if it was enabled in step 3.
  7. `show/dx/options` — verify restoration before resuming contest operation.
- **Known risk:** Forgetting step 5 leaves the cluster scoped to the one-off test filter indefinitely (e.g. `State=WV` with no spotter/band/mode restriction) — this is silent; nothing alerts you that the standing filter was dropped.
- **Open risk, carried from ADR-7:** semantic correctness of state-to-prefix mapping for the 8th call district (W8/K8/N8 spans WV/OH/MI) remains unvalidated against a confirmed live WV spot.

## ADR-11: Station band capability — 40m through 10m only

- **Decision:** Station has no 160m or 80m transmit/receive capability. All future filter constructions exclude `Band=160` and `Band=80` regardless of what bands a given contest permits.
- **Scope:** Standing constraint, not contest-specific — applies to ADR-8, ADR-10, and any filter built after this point. Default band set going forward is `(Band=40 OR Band=20 OR Band=15 OR Band=10)` unless a future contest's rules further restrict bands (e.g. single-band entries), in which case narrow further from this set, never widen into 160/80.
- **Rationale:** No antenna/amplifier/tuner capability on those bands — spots there are operationally useless regardless of cluster/skimmer coverage quality.

## ADR-10: All Asia DX Contest, CW (JARL) filter

- **Decision:** Add `Cont=AS` to scope spotted DX to the Asian continent — the relevant filter dimension for this contest, since as a non-Asian station every countable QSO is against an Asian entity.
- **Filter:**

```
SET DX FILTER Skimmer AND NOT SkimBusted AND Mode=CW AND Cont=AS AND
(Band=40 OR Band=20 OR Band=15 OR Band=10) AND
(Spotter=[KW7MM-#,KW7MM-2-#,VE6JY-#,W6YX-#,ND7K-#,VE6WZ-#,N6TV-#,VE7CC-#,KH6LC-#])

SET DX MODE FILTER
```

- **Rationale for field choice:** `Cont` (spotted-station side, not `SpotterCont`) per the ADR-4 field table — independent dimension from spotter-side geography, same distinction flagged as the most likely recurring error in this project.
- **Differences from ADR-8 standing filter:**
  - `Cont=AS` added (new — not present in ADR-8).
  - `SkimCQ` dropped per ADR-6 (confirmed redundant for RBN-sourced spots).
  - Band set: 40/20/15/10, same as ADR-8 default. JARL rule permits 160m and 80m for this contest as well, but station has no 160/80m capability — those bands intentionally excluded. See ADR-11 for the standing station-capability constraint this follows from.
  - Spotter list unchanged from ADR-8.
- **Rule constraint, not a filter concern but operationally relevant:** All Asian DX Contest rules (most recently confirmed in the 60th-edition rule text, status for current running not re-verified this session) prohibit self-spotting and asking for spots on packet cluster. This doesn't affect *receiving* spots via this filter, but flag before assuming any self-spot workflow is permitted under this contest's rules.
- **Known risk, same pattern as ADR-8:** if none of the nine listed spotters are actively skimming Asian-path signals at test time, filter returns zero spots silently. Check `SHow/Skimmer` before troubleshooting filter logic.
- **Status:** Syntactically derived from confirmed AR-Cluster field grammar (ADR-4); not yet live-tested against actual contest traffic.

---

## Outstanding action items

1. ~~Validate `State=WV` semantics against a live confirmed WV spot.~~ — **Confirmed (2026-06-20).**
2. ~~Run live validation of ADR-8 filter during active CW contest traffic; confirm spot count and spotter-of-origin distribution match expectation.~~ — **Confirmed OK (2026-06-20).**
3. ~~Confirm whether multiple sequential `SET DX FILTER` commands on this cluster replace the prior filter outright or require explicit clearing~~ — **Resolved (ADR-9): confirmed wholesale-replace, no append/partial-clear mechanism exists.**
4. Update internal docs/onboarding to remove ab5k.net as a reference; point to k3lr.com/reversebeacon.net archived PDFs instead. **— Open: needs disposition (see below).**
5. ~~Decide whether `SkimCQ` should be dropped from the standing filter for clarity, given it is a no-op for this RBN-fed source.~~ — **Decided: drop.** ADR-8 and ADR-10 filter strings should both omit `SkimCQ` going forward (ADR-10 already omits it per ADR-6; ADR-8's live string still includes it as of last submission — drop on next resubmission).
6. Live-test ADR-10 (All Asia DX CW) filter against actual contest traffic; confirm `Cont=AS` correctly scopes to Asian entities. Skimmer-coverage risk note for 160/80m removed per ADR-11 (station has no capability on those bands; moot).
7. ~~Re-verify current-year All Asia DX Contest rules for the self-spotting/cluster-spot-request prohibition~~ — **Ignore: operator will not self-spot regardless of rule specifics, so this verification has no operational consequence.**
8. Resubmit ADR-8 standing filter without `SkimCQ` (per item 5) — confirm via `show/dx/options` after resubmission.
