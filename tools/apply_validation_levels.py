#!/usr/bin/env python3
"""Lower P1 validation labels that name no existing test to P0 (docs/validation_plan.md, P1 entry criterion).

Only the `level: P1` token of each affected record's validation block is edited (block or inline style), so file
formatting is preserved; the arithmetic described in validation.methods stays as a candidate check. The file is
re-parsed and the edit aborted if anything but validation.level changed. Each change is appended to a CSV log.

    uv run python tools/apply_validation_levels.py --log research/_fragments/validation_levels_lowered.csv FILE...
    uv run python tools/apply_validation_levels.py --check FILE...
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
from lhmuc.registry import p1_test_references, registered_test_names  # noqa: E402

ID_RE = re.compile(r"^\s*-\s+parameter_id:\s*['\"]?([A-Za-z0-9_]+)['\"]?\s*$")
VAL_RE = re.compile(r"^\s*validation:")
LEVEL_RE = re.compile(r"level:\s*P1\b")


def process(path: Path, tests: set, check: bool, rows: list) -> int:
    text = path.read_text()
    doc = yaml.safe_load(text) or {}
    target = []
    for r in doc.get("parameters") or []:
        v = r.get("validation") or {}
        if v.get("level") == "P1" and not (p1_test_references(v) & tests):
            target.append(r["parameter_id"])
    if check or not target:
        for pid in target:
            print(f"{path}: {pid}: P1 without a test")
        return len(target)
    lines = text.splitlines(keepends=True)
    want, current, done = set(target), None, set()
    i = 0
    while i < len(lines):
        m = ID_RE.match(lines[i])
        if m:
            current = m.group(1)
        elif current in want and current not in done and VAL_RE.match(lines[i]):
            for j in range(i, min(i + 3, len(lines))):
                if LEVEL_RE.search(lines[j]):
                    lines[j] = LEVEL_RE.sub("level: P0", lines[j], count=1)
                    done.add(current)
                    break
        i += 1
    missing = want - done
    if missing:
        raise SystemExit(f"{path}: could not locate the level token of {sorted(missing)[:5]}")
    new_text = "".join(lines)
    expected = copy.deepcopy(doc)
    for r in expected["parameters"]:
        if r["parameter_id"] in want:
            r["validation"]["level"] = "P0"
    if yaml.safe_load(new_text) != expected:
        raise SystemExit(f"{path}: edit changed more than validation.level; aborted")
    path.write_text(new_text)
    rel = path.resolve().relative_to(REPO_ROOT)
    for pid in target:
        rows.append({"parameter_id": pid, "file": str(rel), "before": "P1", "after": "P0",
                     "rule": "P1 names no existing test function (docs/validation_plan.md)"})
    return len(target)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--log", type=Path)
    args = ap.parse_args()
    tests = registered_test_names(REPO_ROOT)
    rows: list = []
    n = 0
    for f in args.files:
        if f.suffix == ".yaml" and "parameters" in (yaml.safe_load(f.read_text()) or {}):
            n += process(f, tests, args.check, rows)
    if args.check:
        print(f"{n} P1 record(s) name no existing test")
        return 1 if n else 0
    if rows and args.log:
        new = not args.log.exists()
        with args.log.open("a", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["parameter_id", "file", "before", "after", "rule"], lineterminator="\n")
            if new:
                w.writeheader()
            w.writerows(rows)
    print(f"lowered {n} P1 label(s)" + (f"; logged to {args.log}" if args.log else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
