"""CLI: `python -m lhmuc validate` — validate every registry and print a provenance summary."""
from __future__ import annotations

import argparse
import sys

from .registry import load_all, status_counts


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="lhmuc")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="validate schemas, parameters, sources, conflicts, proposals")
    v.add_argument("--warnings", action="store_true", help="print warnings too")
    args = ap.parse_args(argv)
    if args.cmd == "validate":
        ev = load_all()
        counts = status_counts(ev)
        print(f"parameters: {len(ev.parameters)}  sources: {len(ev.sources)}  scenarios: {len(ev.scenarios)}  "
              f"assumptions: {len(ev.assumptions)}  conflicts: {len(ev.conflicts)}  proposals: {len(ev.proposals)}")
        print("provenance status counts:")
        for k, n in counts.items():
            print(f"  {k:20s} {n}")
        unknown = [p for p in ev.parameters.values() if p["provenance"]["status"] == "unknown"]
        synthetic = [p for p in ev.parameters.values() if p["provenance"]["status"] == "synthetic"]
        if unknown:
            print("unknown parameters (value must stay null):")
            for p in unknown:
                print(f"  {p['parameter_id']}")
        if synthetic:
            print("synthetic parameters (range only, see parameters/assumptions):")
            for p in synthetic:
                print(f"  {p['parameter_id']}  <- {p['provenance'].get('assumption_id')}")
        errs = ev.errors
        warns = [i for i in ev.issues if i.severity == "warning"]
        if args.warnings:
            for w in warns:
                print(w)
        for e in errs:
            print(e)
        print(f"{len(errs)} errors, {len(warns)} warnings")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
