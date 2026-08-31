# Live Verification — Phase 1b (W3LPL retest + remaining 5) — 2026-08-30

Continuation of `live_verification_2026-08-30.md`: a W3LPL retest with
`set/skimmer` enabled, plus the remaining 5 of the original top-10 NA
ranking (W4MYA, WB3FFV, K1TTT, N2WQ, VE6DXC), all under callsign
**N6YU**.

## W3LPL retest (with `set/skimmer`)

Original test got 0 spots in 60s because W3LPL's CW skimmer defaults
off. This retest logged in, sent `set/skimmer`, then collected:

- Login response: *"Hello N6YU, this is W3LPL in Glenwood,MD running
  DXSpider V1.57 build 686. Capabilities: ve7cc rbn"*
- Node stats: `Nodes: 5/398 Users [Loc/Clr]: 134/3988 Max: 213/6693 —
  Uptime: 20d 11h 36m`
- After `set/skimmer`: **3 spots in 5.8s**

**Correction to prior records**: W3LPL's software family was recorded
as "AR-Cluster V6" in `na_cluster_ranking_2026-08.md`, copied from
NG3K's directory. The live banner is unambiguous: `"Welcome to the
W3LPL-Beta DX-Spider Telnet Server"`, running DXSpider. This is a real
error in the sourced data (NG3K's listing), not staleness — the
directory entry is simply wrong for this host:port as of this session.
`na_cluster_ranking_2026-08.md` has been corrected accordingly, which
also reverses the earlier "zero-code-change backup" recommendation for
W3LPL (`spot_filter.py` doesn't implement DXSpider grammar).

## Remaining 5

Method: TCP connect (15s timeout) → detect login prompt → send
callsign → collect for up to 60s or until 3 `DX de` lines, whichever
first — same method as the original top-5 test.

| Node | Host:Port | Result | Software (live-confirmed) | Notes |
|---|---|---|---|---|
| **WB3FFV** | dxc.wb3ffv.us:7300 | **PASS — 3 spots/49.3s** | DXSpider | Fully confirmed, no caveats |
| **N2WQ** | cluster.n2wq.com:7373 | **PASS — 3 spots/33.0s** | CC-Cluster v3.397 | Fully confirmed, no caveats |
| **K1TTT** | k1ttt.net:7373 | Marginal — 2 spots/60s | **AR-Cluster** (banner: *"Welcome to the K1TTT AR-Cluster Telnet Server"*) | Only other AR-Cluster-family node confirmed besides NC7J — real backup candidate, but version unconfirmed and volume was below the 3-spot bar |
| **W4MYA** | dxc.w4mya.us:7373 | 0 spots/60s | CC-Cluster v3.397 (banner confirms) | Banner explicitly states skimmer defaults off (`set/skimmer` to enable) — same pattern as W3LPL, needs a skimmer-enabled retest before drawing a conclusion |
| **VE6DXC** | dx.middlebrook.ca:8000 | Weak — 1 spot/60s | DXSpider (per NG3K; banner was minimal, just `login:`) | Lowest live spot volume of any alive node tested |

## Open follow-ups

1. **K1TTT AR-Cluster version check** — confirm via `HELP` output or
   version banner whether it runs AR-Cluster V6 specifically (matching
   NC7J and this project's ADR-documented filter grammar) or an older
   version with different syntax, before recommending it as a backup.
2. **W4MYA skimmer-enabled retest** — same treatment as W3LPL's
   successful retest, to get a real spot-volume reading instead of the
   skimmer-off default result.
3. VE6DXC's weak 1-spot result could be re-tested with a longer window
   or at a different time of day before concluding it's genuinely
   low-volume rather than just unlucky timing.
