import argparse
import sys
from dataclasses import dataclass

SPOTTER_TIERS = {
    "local": [
        "W6YX-#", "AK6RI-1-#", "N6TV-#",
    ],
    "regional": [
        "W6YX-#", "AK6RI-1-#", "N6TV-#",
        "K6FOD-#", "WA7LNW-#", "ND7K-#", "K7CO-#", "NG7M-#",
        "N7VVX-#", "N7TUG-#", "KD7EFG-#", "KW7MM-#", "KW7MM-2-#",
    ],
}

NO_CAPABILITY_BANDS = {160, 80}

VALID_BANDS = {160, 80, 60, 40, 30, 20, 17, 15, 12, 10, 6}

VALID_CONTINENTS = {"AF", "AN", "AS", "EU", "NA", "OC", "SA"}


@dataclass
class FilterSpec:
    bands: list[int]
    spotters: list[str]
    mode: str = "CW"
    skimmer: bool = True
    skim_busted: bool = False
    state: list[str] | None = None
    cont: str | None = None
    call_prefix: str | None = None


def render_ar6(spec: FilterSpec) -> str:
    parts = ["Skimmer", "NOT SkimBusted", f"Mode={spec.mode}"]

    if spec.state:
        if len(spec.state) == 1:
            parts.append(f"State={spec.state[0]}")
        else:
            parts.append(f"State=[{','.join(spec.state)}]")
    if spec.cont:
        parts.append(f"Cont={spec.cont}")
    if spec.call_prefix:
        parts.append(f"Call={spec.call_prefix}*")

    band_expr = " OR ".join(f"Band={b}" for b in spec.bands)
    parts.append(f"({band_expr})")

    spotter_list = ",".join(spec.spotters)
    parts.append(f"(Spotter=[{spotter_list}])")

    return "SET DX FILTER " + " AND ".join(parts)


def render_cc(spec: FilterSpec) -> str:
    raise NotImplementedError("CC Cluster grammar not yet implemented")


def render_dxspider(spec: FilterSpec) -> str:
    raise NotImplementedError("DX Spider grammar not yet implemented")


RENDERERS = {
    "ar6": render_ar6,
    "cc": render_cc,
    "dxspider": render_dxspider,
}


def parse_bands(band_str: str) -> list[int]:
    bands = []
    for b in band_str.split(","):
        val = int(b.strip())
        if val not in VALID_BANDS:
            print(f"Error: {val} is not a valid band.", file=sys.stderr)
            sys.exit(1)
        bands.append(val)
    return bands


def warn_no_capability(bands: list[int]):
    flagged = [b for b in bands if b in NO_CAPABILITY_BANDS]
    if flagged:
        label = ", ".join(f"{b}m" for b in flagged)
        print(
            f"Warning: station has no {label} capability (ADR-11). "
            f"Spots on {'these bands' if len(flagged) > 1 else 'this band'} "
            f"are operationally useless.",
            file=sys.stderr,
        )


def main():
    parser = argparse.ArgumentParser(
        description="Generate a DX cluster filter command string for N1MM paste.",
        epilog="Examples:\n"
               "  spot_filter.py\n"
               "  spot_filter.py --bands 40,20,15,10\n"
               "  spot_filter.py --bands 40,20,15,10 --spotters regional --cont AS\n"
               "  spot_filter.py --state WV\n"
               "  spot_filter.py --bands 40,20,17,15,12,10 --spotters regional --call-prefix JA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--bands", default="40,20,15",
        help="Comma-separated band list in meters (default: 40,20,15)"
    )
    parser.add_argument(
        "--spotters", choices=SPOTTER_TIERS.keys(), default="local",
        help="Spotter tier: local (<=50mi) or regional (<=1000mi). Default: local"
    )
    parser.add_argument(
        "--cluster", choices=RENDERERS.keys(), default="ar6",
        help="Cluster type: ar6, cc, dxspider. Default: ar6"
    )

    dx_group = parser.add_mutually_exclusive_group()
    dx_group.add_argument(
        "--state",
        help="Filter spotted stations by US state or Canadian province/territory, comma-separated (e.g. WV or BC,AB,ON)"
    )
    dx_group.add_argument(
        "--cont",
        help="Filter spotted stations by continent (AF, AN, AS, EU, NA, OC, SA)"
    )
    dx_group.add_argument(
        "--call-prefix",
        help="Filter spotted stations by callsign prefix (e.g. JA, VK, G)"
    )

    args = parser.parse_args()

    bands = parse_bands(args.bands)
    warn_no_capability(bands)

    if args.cont and args.cont.upper() not in VALID_CONTINENTS:
        print(
            f"Error: '{args.cont}' is not a valid continent. "
            f"Use one of: {', '.join(sorted(VALID_CONTINENTS))}",
            file=sys.stderr,
        )
        sys.exit(1)

    spec = FilterSpec(
        bands=bands,
        spotters=SPOTTER_TIERS[args.spotters],
        state=[s.strip().upper() for s in args.state.split(",")] if args.state else None,
        cont=args.cont.upper() if args.cont else None,
        call_prefix=args.call_prefix.upper() if args.call_prefix else None,
    )

    renderer = RENDERERS[args.cluster]
    try:
        print(renderer(spec))
    except NotImplementedError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
