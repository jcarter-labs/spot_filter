# RBN Skimmer / Spotter Reference Sites

Reference list of websites providing RBN node, skimmer status, or spotter-quality data — compiled for the spot-density proxy and contact logger projects. Verify each live before depending on it operationally; uptime and feature sets are not guaranteed.

## Originally supplied (this session)

| Site | Purpose | Data type |
|---|---|---|
| [reversebeacon.net/nodes/detail.php](https://www.reversebeacon.net/nodes/detail.php) | Official RBN node/skimmer detail list | Live node roster — **blocked by robots.txt for automated fetch**; browser access only |
| [dxcluster.ha8tks.hu](https://dxcluster.ha8tks.hu/) | HA8TKS real-time CW skimmer comparison | Compare a node's spots against its 10 closest skimmer neighbors over the last 15 min |
| [sm7iun.se/rbn/analytics](https://sm7iun.se/rbn/analytics/) | SM7IUN RBN analytics | Daily skew/calibration data (ppm drift), feeds into W3RGA's ranking |
| [qsl.net/w3rga/top-spotter](https://www.qsl.net/w3rga/top-spotter/index.html) | W3RGA Top-Spotter Page | Ranks RBN nodes by daily CW/RTTY spot volume; raw CSV at `.../dupe_report.csv` — **best machine-readable source found this session** |

## Additional sites identified

| Site | Purpose | Data type |
|---|---|---|
| [reversebeacon.net/main.php](https://www.reversebeacon.net/main.php) | RBN main live spot map | Real-time spot map; red dots = active nodes (replaces the old static skimmer list), blue = spotted stations |
| [reversebeacon.net/analysis](https://www.reversebeacon.net/analysis/) | RBN Propagation Dashboard (beta) | Per-callsign SNR heatmap and historical propagation charts by band/region — under active rebuild as of this session |
| [skimmer.dxwatch.com](https://skimmer.dxwatch.com/index.php) | dxwatch.com node detail list | Source of the detailed node roster used this session (grid squares, band coverage, agg version, last-seen). Same operator (PY1NB) as reversebeacon.net |
| [ng3k.com/misc/cluster.html](https://www.ng3k.com/misc/cluster.html) | NG3K curated telnet cluster/skimmer list | Manually curated (not automated), representative selection of reliable open-telnet nodes — useful as a sanity cross-check, not a primary source |

## Notes

- **reversebeacon.net** and **dxwatch.com/skimmer.dxwatch.com** are both hosted/maintained by the same person (Felipe Ceglia, PY1NB) — expect overlapping but not identical data.
- **ab5k.net**, referenced in NC7J's own `HELP` output as the AR-Cluster filter documentation source, is now a dead/squatted domain (confirmed this session). Do not use; see ADR-3 in `nc7j_filter_adr.md` for the working replacement references (k3lr.com, reversebeacon.net archived PDFs).
- The W3RGA dupe-report CSV and the SM7IUN skew-analytics report are complementary, not redundant: dupe% measures spot-quality (duplicate/busted rate), skew (ppm) measures the skimmer's frequency calibration accuracy. Both were used this session to evaluate the 27-callsign filter list.
- robots.txt blocks automated fetching of `reversebeacon.net/skimmers/detail.php` and `main.php` — any future automated/scripted pull of RBN data should target the CSV/raw endpoints (e.g., W3RGA's dupe_report.csv) or skimmer.dxwatch.com instead, which permitted fetch this session.
