#!/usr/bin/env python3
"""Set `parameters_extracted` of every source in research/source_registry.yaml to the sorted list of parameter ids
whose provenance cites that source (the convention of the Phase 0 entries).

    uv run python tools/sync_parameters_extracted.py           # rewrite the registry
    uv run python tools/sync_parameters_extracted.py --check   # exit 1 if any list is out of sync
"""
from __future__ import annotations

import argparse
import collections
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lhmuc import REPO_ROOT  # noqa: E402

REG = REPO_ROOT / "research" / "source_registry.yaml"


def citing_records(root: Path = REPO_ROOT) -> dict[str, list[str]]:
    cite: dict[str, set[str]] = collections.defaultdict(set)
    for path in sorted((root / "parameters").rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text()) or {}
        for r in doc.get("parameters") or []:
            sid = ((r.get("provenance") or {}).get("source") or {}).get("source_id")
            if sid:
                cite[sid].add(r["parameter_id"])
    return {k: sorted(v) for k, v in cite.items()}


def out_of_sync(reg: dict, cite: dict[str, list[str]]) -> list[str]:
    return [s["source_id"] for s in reg["sources"] if sorted(s.get("parameters_extracted") or []) != cite.get(s["source_id"], [])]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    text = REG.read_text()
    header = "".join(line for line in text.splitlines(keepends=True) if line.startswith("#"))
    reg = yaml.safe_load(text)
    cite = citing_records()
    stale = out_of_sync(reg, cite)
    if args.check:
        for sid in stale:
            print(f"OUT OF SYNC: {sid}")
        return 1 if stale else 0
    for s in reg["sources"]:
        s["parameters_extracted"] = cite.get(s["source_id"], [])
    REG.write_text(header + yaml.safe_dump(reg, sort_keys=False, allow_unicode=True, width=120))
    print(f"parameters_extracted synced for {len(stale)} source(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
