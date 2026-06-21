# NC7J Spotter Groups — Local / Regional

Derived from the 27-call candidate list (+ AK6RI-1), vetted against three independent sources: live NC7J `SHow/Skimmer`, the W3RGA daily dupe report (`qsl.net/w3rga/top-spotter/dupe_report.csv`), and the SM7IUN skew/calibration report. Distance computed from grid square (dxwatch.com node detail list) to home QTH CM87vk via great-circle (haversine) calculation. See `nc7j_filter_adr.md` for full ADR history and `rbn_reference_sites.md` for source documentation.

**Exclusions applied:** W6DVN omitted — no grid, no W3RGA entry, no skew entry; unverifiable across all three sources. VE6WZ family, VE6JY, WX7V/5, K7EK, KH6LC, WB6BEE, NH6HI, WZ7I, VK6ANC excluded as >1000 mi (see distance table in prior session turn for full figures).

---

## Group 1 — Local Spotters (≤ 50 mi from CM87vk)

| Call | Grid | Distance (mi) | TotSpots (24h) | Dupe% | Skew (ppm) |
|---|---|---|---|---|---|
| W6YX | CM87VJ | 2.9 | 6,328 | 0.2 | +0.7 |
| AK6RI-1 | CM87XI | 10.8 | N/A (no W3RGA entry) | N/A | -0.1 |
| N6TV | CM97CF | 27.0 | 4,360 | 0.3 | +0.5 |

**3 spotters.** Closest-proximity tier; best candidates for any logic specifically modeling near-field/local propagation characteristics. Note AK6RI-1 has no W3RGA volume data — confirm live activity via `SHow/Skimmer` before relying on it operationally.

```
Spotter=[W6YX-#,AK6RI-1-#,N6TV-#]
```

---

## Group 2 — Regional Spotters (50–1000 mi from CM87vk, plus undated KW7MM family)

| Call | Grid | Distance (mi) | TotSpots (24h) | Dupe% | Skew (ppm) | Notes |
|---|---|---|---|---|---|---|
| K6FOD | DM04WC | 324.7 | 1,466 | 0.3 | +0.4 | |
| WA7LNW | DM37GD | 481.2 | 5,961 | 0.4 | -4.9 | Elevated skew; within tolerance but highest in this group |
| ND7K | DM34OB | 576.9 | 5,188 | 0.5 | -0.3 | |
| K7CO | DN40BN | 594.9 | 3,318 | 0.5 | +1.3 | |
| NG7M | DN31XB | 598.4 | 2,207 | 0.0 | -0.0 | Co-located with NC7J cluster node (Syracuse, UT) |
| N7VVX | DN40BW | 603.4 | 1,789 | 0.3 | -0.0 | |
| N7TUG | CN87TQ | 708.3 | 792 | 0.1 | +1.2 | Lower volume than others in group |
| KD7EFG | — | — | 5,058 | 1.0 | +0.3 | Not in dxwatch node list; distance unknown, included per instruction (KW7MM family + all ≤1000mi) |
| KW7MM | — | — | 7,432 | 0.4 | +0.4 | Not in dxwatch node list; distance unknown, included per explicit instruction |
| KW7MM-2 | — | — | 6,286 | 0.4 | +0.6 | Not in dxwatch node list; distance unknown, included per explicit instruction |

**10 spotters.**

```
Spotter=[K6FOD-#,WA7LNW-#,ND7K-#,K7CO-#,NG7M-#,N7VVX-#,N7TUG-#,KD7EFG-#,KW7MM-#,KW7MM-2-#]
```

**Open item — KD7EFG, KW7MM, KW7MM-2 have no confirmed distance.** They were not found in the `skimmer.dxwatch.com` node detail list fetched this session, so their grid squares and therefore actual mileage from CM87vk are unverified. They are included here per explicit instruction ("KW7MM and all other stations within 1000 mi, except W6DVN"), not because their distance was confirmed ≤1000 mi. Recommend a follow-up grid lookup (QRZ skill, Claude Code) before treating this as geographically validated.

**Quality note — KW7MM-3 deliberately excluded from both groups.** Despite sharing the KW7MM callsign family, it showed a 50.3% dupe rate in the W3RGA report — the second-worst in the entire 27-call dataset. Not included in Group 2 even though KW7MM and KW7MM-2 are, per the quality findings from this session.

---

## Combined filter (Groups 1 + 2, 13 spotters)

```
SET DX FILTER Skimmer AND NOT SkimBusted AND Mode=CW AND
(Band=40 OR Band=20 OR Band=15 OR Band=10) AND
(Spotter=[W6YX-#,AK6RI-1-#,N6TV-#,K6FOD-#,WA7LNW-#,ND7K-#,K7CO-#,NG7M-#,N7VVX-#,N7TUG-#,KD7EFG-#,KW7MM-#,KW7MM-2-#])
```

Not yet tested live against NC7J — verify via `SET DX FILTER` + `SHow Dx Options` round-trip before committing as the standing contest filter.
