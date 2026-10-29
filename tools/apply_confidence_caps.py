#!/usr/bin/env python3
"""Lower parameter confidences to the caps of research/source_quality_policy.md §4.

Only the `confidence:` line of each affected record is edited, so file formatting is preserved; values,
quotations and every other field are left untouched (checked by re-parsing). Each change is appended to a CSV log.

    uv run python tools/apply_confidence_caps.py --log research/_fragments/confidence_caps_applied.csv FILE...
    uv run python tools/apply_confidence_caps.py --check FILE...     # report only, exit 1 if anything exceeds a cap
"""
from __future__ import annotations

import argparse
import copy
import csv
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lhmuc import REPO_ROOT  # noqa: E402
from lhmuc.registry import CONFIDENCE_RANK, confidence_cap  # noqa: E402

ID_RE = re.compile(r"^\s*-\s+parameter_id:\s*['\"]?([A-Za-z0-9_]+)['\"]?\s*$")
CONF_RE = re.compile(r"^(\s*)confidence:\s*['\"]?(high|medium|low|none)['\"]?\s*$")


def load_sources() -> dict:
    doc = yaml.safe_load((REPO_ROOT / "research" / "source_registry.yaml").read_text()) or {}
    return {s["source_id"]: s for s in doc.get("sources", [])}


def process(path: Path, sources: dict, check: bool, log_rows: list) -> int:
    text = path.read_text()
    doc = yaml.safe_load(text) or {}
    records = doc.get("parameters") or []
    target = {}
    for r in records:
        prov = r.get("provenance") or {}
        src = prov.get("source") or {}
        cap, why = confidence_cap(prov, sources.get(src.get("source_id")))
        conf = prov.get("confidence")
        if cap is not None and CONFIDENCE_RANK.get(conf, 0) > CONFIDENCE_RANK[cap]:
            target[r["parameter_id"]] = (conf, cap, why)
    if check or not target:
        for pid, (conf, cap, why) in target.items():
            print(f"{path}: {pid}: {conf} > {cap} ({why})")
        return len(target)
    lines = text.splitlines(keepends=True)
    current, done = None, set()
    for i, line in enumerate(lines):
        m = ID_RE.match(line)
        if m:
            current = m.group(1)
            continue
        m = CONF_RE.match(line)
        if m and current in target and current not in done:
            lines[i] = f"{m.group(1)}confidence: {target[current][1]}\n"
            done.add(current)
    missing = set(target) - done
    if missing:
        raise SystemExit(f"{path}: could not locate the confidence line of {sorted(missing)[:5]}")
    new_text = "".join(lines)
    new_doc = yaml.safe_load(new_text)
    expected = copy.deepcopy(doc)
    for r in expected["parameters"]:
        if r["parameter_id"] in target:
            r["provenance"]["confidence"] = target[r["parameter_id"]][1]
    if new_doc != expected:
        raise SystemExit(f"{path}: edit changed more than the confidence fields; aborted")
    path.write_text(new_text)
    rel = path.resolve().relative_to(REPO_ROOT)
    for pid, (conf, cap, why) in target.items():
        log_rows.append({"parameter_id": pid, "file": str(rel), "before": conf, "after": cap, "rule": why})
    return len(target)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--log", type=Path)
    args = ap.parse_args()
    sources = load_sources()
    rows: list = []
    n = 0
    for f in args.files:
        if f.suffix == ".yaml" and "parameters" in (yaml.safe_load(f.read_text()) or {}):
            n += process(f, sources, args.check, rows)
    if args.check:
        print(f"{n} record(s) exceed a §4 cap")
        return 1 if n else 0
    if rows and args.log:
        new = not args.log.exists()
        with args.log.open("a", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["parameter_id", "file", "before", "after", "rule"], lineterminator="\n")
            if new:
                w.writeheader()
            w.writerows(rows)
    print(f"lowered {n} confidence value(s)" + (f"; logged to {args.log}" if args.log else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
