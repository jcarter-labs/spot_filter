# spot_filter

DX cluster filter configuration for contest band monitoring on the NC7J AR-Cluster node (`dxc.nc7j.com:7373`).

## Environment

| | |
|---|---|
| **Machine** | Lenovo ThinkCentre M70s |
| **OS** | Windows 11 Pro |
| **Python** | 3.14.2 |
| **Project path** | `C:\Users\johnn\Radio\Projects\spot_filt\` |

## spot_filter.py — Filter String Generator

Generates a one-line `SET DX FILTER` command string that you paste into N1MM's cluster command window (or any telnet client connected to an AR-Cluster V6 node). The script does not connect to the cluster itself — it only builds the command string.

CC Cluster and DX Spider grammars are stubbed out but not yet implemented. Selecting `--cluster cc` or `--cluster dxspider` will return an error.

### How to run

From anywhere (if installed to PATH) or from the `spot_filt` directory:

```
python spot_filter.py --bands <band_list> [--spotters <tier>] [--cluster <type>] [--state <ST> | --cont <CODE> | --call-prefix <PREFIX>]
```

### Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `--bands` | No | `40,20,15` | Comma-separated band list in meters (e.g. `40,20,15,10`). Valid bands: 160, 80, 60, 40, 30, 20, 17, 15, 12, 10, 6. A warning is printed if 160 or 80 is included (station has no capability on those bands per ADR-11). |
| `--spotters` | No | `local` | Spotter tier. `local` = 3 skimmers within 50 mi (W6YX, AK6RI-1, N6TV). `regional` = 13 skimmers within ~1000 mi (includes local + ND7K, KW7MM, etc.). |
| `--cluster` | No | `ar6` | Cluster grammar type. `ar6` = AR-Cluster V6 (fully implemented). `cc` and `dxspider` = not yet implemented. |
| `--state` | No | — | Filter spotted stations by US state (e.g. `WV`, `CA`). Mutually exclusive with `--cont` and `--call-prefix`. |
| `--cont` | No | — | Filter spotted stations by continent (`AF`, `AN`, `AS`, `EU`, `NA`, `OC`, `SA`). Mutually exclusive with `--state` and `--call-prefix`. |
| `--call-prefix` | No | — | Filter spotted stations by callsign prefix (e.g. `JA`, `VK`, `G`). Mutually exclusive with `--state` and `--cont`. |

### Examples

```
python spot_filter.py
python spot_filter.py --bands 40,20,15,10
python spot_filter.py --bands 40,20,15,10 --spotters regional --cont AS
python spot_filter.py --state WV
python spot_filter.py --bands 40,20,17,15,12,10 --spotters regional --call-prefix JA
```

### Data flow

```
                        INPUTS                          PROCESSING                    OUTPUT
 ┌─────────────────────────────────┐
 │  --bands       40,20,15        │
 │  --spotters    local/regional  │         ┌──────────────────────┐
 │  --cluster     ar6             │────────▶│  Filter Spec         │
 │  --state       WV              │         │  (dataclass)         │        ┌──────────────────────┐
 │  --cont        AS              │         │                      │        │                      │
 │  --call-prefix JA              │         │  bands: [40,20,15]   │        │  SET DX FILTER       │
 └─────────────────────────────────┘         │  spotters: [W6YX..]  │───────▶│  Skimmer AND NOT     │
                                            │  mode: CW            │        │  SkimBusted AND ...  │
              Hardcoded defaults:           │  state/cont/prefix   │        │                      │
 ┌─────────────────────────────────┐         └──────────────────────┘        │  One-line string     │
 │  Mode       = CW  (always)     │                    │                    │  ready to paste      │
 │  Skimmer    = on  (always)     │                    ▼                    │  into N1MM           │
 │  SkimBusted = off (always)     │         ┌──────────────────────┐        └──────────────────────┘
 └─────────────────────────────────┘         │  Grammar Renderer    │
                                            │                      │
                                            │  ar6 ──▶ implemented │
                                            │  cc  ──▶ stub        │
                                            │  dxspider ──▶ stub   │
                                            └──────────────────────┘
```

## Other files

- **nc7j_filter_adr.md** — Architecture Decision Record documenting the iterative discovery of AR-Cluster V6 filter syntax, confirmed field lists, boolean/grouping grammar, and live-tested filter strings for contest use. Includes standing filters for general CW contest operation (ADR-8) and All Asia DX CW (ADR-10).
- **nc7j_spotter_groups.md** — Vetted spotter/skimmer callsign lists for local and regional tiers, with distance, volume, dupe rate, and skew data from W3RGA and SM7IUN.
- **rbn_reference_sites.md** — Reference list of RBN node status and skimmer quality data sources.
- **qrz-lookup.skill** — Claude Code skill package for looking up amateur radio callsigns against the QRZ.com XML API.

## Filter reference

The AR-Cluster V6 `HELP` text on NC7J points to `www.ab5k.net`, which is dead (parked domain). Use these instead:

- [AR-Cluster Filter Commands (K3LR mirror)](https://www.k3lr.com/w9zrx/AR-Cluster%20Filter%20Commands.pdf)
- [AR-Cluster V6 Filter Commands (RBN mirror)](https://cms.reversebeacon.net/sites/cms.reversebeacon.net/files/2018/04/26/AR-ClusterV6%20Filter%20Commands.pdf)
- [N5PA worked examples & contest filter templates](https://www.n5pa.com/ham.arcluster.php)
