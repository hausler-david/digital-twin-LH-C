#!/usr/bin/env python3
"""Lower scenario validation labels to the minimum over their role records (docs/validation_plan.md §1 rule 3).

Only the `validation_level:` token of each affected scenario is edited, so file formatting is preserved. The file is
re-parsed and the edit aborted if anything but validation_level changed. Each change is appended to a CSV log.

    uv run python tools/apply_scenario_levels.py --log research/_fragments/scenario_levels_lowered.csv FILE...
    uv run python tools/apply_scenario_levels.py --check FILE...
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
from lhmuc.registry import LEVEL_ORDER, load_all, scenario_level_cap  # noqa: E402

ID_RE = re.compile(r"^\s*-\s+scenario_id:\s*['\"]?([A-Za-z0-9-]+)['\"]?\s*$")
LEVEL_RE = re.compile(r"^(\s*validation_level:\s*)['\"]?(P[0-5])['\"]?(\s*)$")


def process(path: Path, ev, check: bool, rows: list) -> int:
    text = path.read_text()
    doc = yaml.safe_load(text) or {}
    target = {}
    for s in doc.get("scenarios") or []:
        cap = scenario_level_cap(ev, s)
        lvl = s.get("validation_level", "P0")
        if LEVEL_ORDER.index(lvl) > LEVEL_ORDER.index(cap):
            target[s["scenario_id"]] = (lvl, cap, s)
    if check or not target:
        for sid, (lvl, cap, _) in target.items():
            print(f"{path}: {sid}: {lvl} exceeds {cap}, the minimum over its role records")
        return len(target)
    lines = text.splitlines(keepends=True)
    current, done = None, set()
    for i, line in enumerate(lines):
        m = ID_RE.match(line)
        if m:
            current = m.group(1)
            continue
        m = LEVEL_RE.match(line.rstrip("\n"))
        if m and current in target and current not in done:
            lines[i] = f"{m.group(1)}{target[current][1]}{m.group(3)}\n"
            done.add(current)
    missing = set(target) - done
    if missing:
        raise SystemExit(f"{path}: could not locate validation_level of {sorted(missing)[:5]}")
    new_text = "".join(lines)
    expected = copy.deepcopy(doc)
    for s in expected["scenarios"]:
        if s["scenario_id"] in target:
            s["validation_level"] = target[s["scenario_id"]][1]
    if yaml.safe_load(new_text) != expected:
        raise SystemExit(f"{path}: edit changed more than validation_level; aborted")
    path.write_text(new_text)
    rel = path.resolve().relative_to(REPO_ROOT)
    for sid, (lvl, cap, s) in target.items():
        roles = [pid for pid in (s.get("parameters") or {}).values() if pid in ev.parameters]
        n_p1 = sum(1 for pid in roles if (ev.parameters[pid].get("validation") or {}).get("level") == "P1")
        rows.append({"scenario_id": sid, "file": str(rel), "before": lvl, "after": cap,
                     "roles_with_records": len(roles), "roles_at_p1": n_p1,
                     "rule": "label exceeds the minimum over its role records (docs/validation_plan.md §1 rule 3)"})
    return len(target)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--log", type=Path)
    args = ap.parse_args()
    ev = load_all(REPO_ROOT)
    rows: list = []
    n = 0
    for f in args.files:
        if f.suffix == ".yaml" and "scenarios" in (yaml.safe_load(f.read_text()) or {}):
            n += process(f, ev, args.check, rows)
    if args.check:
        print(f"{n} scenario label(s) exceed the minimum over their role records")
        return 1 if n else 0
    if rows and args.log:
        new = not args.log.exists()
        with args.log.open("a", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["scenario_id", "file", "before", "after", "roles_with_records",
                                               "roles_at_p1", "rule"], lineterminator="\n")
            if new:
                w.writeheader()
            w.writerows(rows)
    print(f"lowered {n} scenario label(s)" + (f"; logged to {args.log}" if args.log else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
