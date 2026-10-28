#!/usr/bin/env python3
"""Generate registries/*.csv from the YAML single source of truth.

parameter_registry.csv  <- parameters/**/*.yaml (parameter records)
assumption_registry.csv <- parameters/assumptions/*.yaml
Other registries (missing_evidence, validation, risk) are authored CSVs and are only checked.
Run:  uv run python tools/build_registries.py [--check]
"""
from __future__ import annotations

import csv
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lhmuc import REPO_ROOT  # noqa: E402
from lhmuc.registry import load_all  # noqa: E402

PARAM_COLS = ["parameter_id", "name", "subsystem", "scenario", "symbol", "value", "unit", "uncertainty",
              "allowed_range", "provenance_status", "confidence", "applicability", "source_id", "source_title",
              "page", "table_figure_or_equation", "extraction_method", "validation_level", "dependencies",
              "assumption_id", "date_added", "responsible_module", "file"]
ASM_COLS = ["assumption_id", "parameter_id", "status", "superseded_by", "superseded_on", "distribution", "minimum", "maximum", "unit",
            "reason_required", "reason_authoritative_value_missing", "affected_outputs", "replacement_evidence",
            "sensitivity_analysis", "date_added"]


def _fmt_unc(u):
    if not u:
        return ""
    if u.get("type") == "interval":
        return f"interval[{u.get('lower')},{u.get('upper')}] {u.get('unit') or ''}".strip()
    if u.get("type") == "not_stated":
        return "not_stated"
    return f"{u.get('type')}={u.get('value')} {u.get('unit') or ''}".strip()


def _fmt_range(r):
    if not r:
        return ""
    return f"[{r.get('min')},{r.get('max')}] {r.get('unit')}"


def render(ev) -> dict[str, str]:
    out = {}
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=PARAM_COLS, lineterminator="\n")
    w.writeheader()
    for pid in sorted(ev.parameters):
        p = ev.parameters[pid]
        pr = p["provenance"]
        src = pr.get("source") or {}
        w.writerow({
            "parameter_id": pid, "name": p["name"], "subsystem": p["subsystem"], "scenario": p.get("scenario") or "",
            "symbol": p.get("symbol") or "", "value": "" if p["value"] is None else p["value"], "unit": p["unit"],
            "uncertainty": _fmt_unc(p.get("uncertainty")), "allowed_range": _fmt_range(p.get("allowed_range")),
            "provenance_status": pr["status"], "confidence": pr["confidence"],
            "applicability": pr["applicability"]["category"], "source_id": src.get("source_id") or "",
            "source_title": src.get("title") or "", "page": src.get("page") if src.get("page") is not None else "",
            "table_figure_or_equation": src.get("table_figure_or_equation") or "",
            "extraction_method": pr["extraction_method"], "validation_level": p["validation"]["level"],
            "dependencies": ";".join(p.get("dependencies", [])), "assumption_id": pr.get("assumption_id") or "",
            "date_added": p["date_added"], "responsible_module": p["responsible_module"],
            "file": str(ev.parameter_files[pid]),
        })
    out["parameter_registry.csv"] = buf.getvalue()
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=ASM_COLS, lineterminator="\n")
    w.writeheader()
    for aid in sorted(ev.assumptions):
        a = ev.assumptions[aid]
        sm = a["synthetic_model"]
        w.writerow({
            "assumption_id": aid, "parameter_id": a["parameter_id"], "status": a["status"],
            "superseded_by": ";".join(a.get("superseded_by") or []), "superseded_on": a.get("superseded_on") or "",
            "distribution": sm["distribution"], "minimum": sm.get("minimum", ""), "maximum": sm.get("maximum", ""),
            "unit": sm["unit"], "reason_required": a["reason_required"],
            "reason_authoritative_value_missing": a["reason_authoritative_value_missing"],
            "affected_outputs": ";".join(a["affected_outputs"]), "replacement_evidence": a["replacement_evidence"],
            "sensitivity_analysis": a["sensitivity_analysis"], "date_added": a["date_added"],
        })
    out["assumption_registry.csv"] = buf.getvalue()
    return out


def main(argv: list[str]) -> int:
    check = "--check" in argv
    ev = load_all()
    if ev.errors:
        for e in ev.errors:
            print(e)
        print(f"{len(ev.errors)} validation errors; registries not written")
        return 1
    reg_dir = REPO_ROOT / "registries"
    reg_dir.mkdir(exist_ok=True)
    rc = 0
    for name, text in render(ev).items():
        path = reg_dir / name
        if check:
            if not path.exists() or path.read_text() != text:
                print(f"OUT OF SYNC: {path.relative_to(REPO_ROOT)} (run tools/build_registries.py)")
                rc = 1
        else:
            path.write_text(text)
            print(f"wrote {path.relative_to(REPO_ROOT)} ({text.count(chr(10)) - 1} rows)")
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
