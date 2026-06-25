# Session Notes — 2026-06-20 through 2026-06-25

## What we built

### spot_filter.py
A Python terminal script that generates a one-line `SET DX FILTER` command string for pasting into N1MM's cluster command window. Does not connect to the cluster — output only.

Built in three spirals:
- **Spiral 1:** Hardcoded spotters, bands as only argument, proved the string assembly matched the known-good ADR-8 format.
- **Spiral 2:** Added argparse (`--bands`, `--spotters`, `--cluster`, `--state`, `--cont`), spotter tiers as a dict, FilterSpec dataclass, AR-Cluster renderer, CC/DX Spider stubs.
- **Spiral 3:** Added `--call-prefix`, band validation, ADR-11 warning for 160/80m, continent validation, clean help text with examples.

**Defaults:** `--bands 40,20,15`, `--spotters local`. Running `spot_filter` with no arguments produces the local-spotter 40/20/15 CW filter.

### System command
`spot_filter` works from any terminal — a `.cmd` wrapper lives in `C:\Users\johnn\bin\` which is on the user PATH.

### QRZ lookup skill
`qrz-lookup.skill` was already in the Projects folder. We extracted it, found and fixed a bug (XML namespace was `http://xml.qrz.com` — should be `http://xmldata.qrz.com`), and repacked the corrected version. Used it to look up N8JMS, K3JT, AB8RL, and W8WVA.

---

## What we discussed

### AR-Cluster filter grammar (nc7j_filter_adr.md)
- Added ADR-9 (WV QSOP state filter workflow — `SET DX FILTER` is a wholesale replace, not additive; 7-step procedure for safe one-off testing without losing the standing filter)
- Added ADR-11 (station has no 160m or 80m capability — standing constraint on all future filters)
- Added ADR-10 (All Asia DX CW filter — `Cont=AS`, drops `SkimCQ` per ADR-6, same spotter list as ADR-8)
- Updated Outstanding action items — marked 1, 2, 3, 5, 7 as resolved; added items 6 and 8

### Spotter tiers (nc7j_spotter_groups.md)
Two tiers derived from a 27-callsign candidate list vetted against live NC7J `SHow/Skimmer`, W3RGA dupe report, and SM7IUN skew/calibration data:
- **Local (≤50 mi):** W6YX-#, AK6RI-1-#, N6TV-#
- **Regional (≤1000 mi):** above + K6FOD-#, WA7LNW-#, ND7K-#, K7CO-#, NG7M-#, N7VVX-#, N7TUG-#, KD7EFG-#, KW7MM-#, KW7MM-2-#
- KW7MM-3 deliberately excluded (50.3% dupe rate)
- KD7EFG, KW7MM, KW7MM-2 have no confirmed grid — distance unverified

### ab5k.net cleanup
Searched the repo for all references. All four instances are in ADR-3 itself as deliberate historical record (documenting that the domain is dead). No other files referenced it — no edits needed.

---

## Repo and tooling setup

- Installed Git for Windows (2.54.0) — was not present at session start
- Initialized git repo, set user `johnn` / `jcfrgmn@gmail.com`
- Created GitHub repo at `https://github.com/jcarter-labs/spot_filter`
- Moved project from `Projects/` root into `Projects/spot_filt/` subdirectory; re-rooted git there and force pushed
- Added SVG data flow diagram (`docs/dx-filter-pipeline.svg`) replacing the ASCII art in the README
- README updated with: environment table (M70s, Win11, Python 3.14.2, project path), usage syntax, parameter table, examples, data flow diagram

---

## Outstanding items (carried from nc7j_filter_adr.md)

1. Live-test ADR-10 (`Cont=AS`) filter against actual All Asia DX CW contest traffic
2. Resubmit ADR-8 without `SkimCQ` (still in the live string as of last submission); confirm via `show/dx/options`
3. Confirm grid squares / distances for KD7EFG, KW7MM, KW7MM-2
4. ab5k.net action item — disposition still open (all references are in ADR-3 historical record; no external docs to update were found)

---

## How to resume

```
cd C:\Users\johnn\Radio\Projects\spot_filt
claude
```

Say "continue working on spot_filter" — memory and files provide full context.
