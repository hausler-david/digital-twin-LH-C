"""Load, validate and cross-check the evidence registries.

Single source of truth: YAML files under parameters/ (parameter records, scenarios, assumptions,
materials), research/source_registry.yaml and research/source_conflicts.yaml. CSV registries in
registries/ are *generated* from these by tools/build_registries.py and must stay in sync.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from . import REPO_ROOT
from .units import parse_unit

SCHEMA_DIR = REPO_ROOT / "schemas"
PARAM_DIR = REPO_ROOT / "parameters"
RESEARCH_DIR = REPO_ROOT / "research"
BENCH_DIR = REPO_ROOT / "theory" / "benchmarks"


def _schema_registry() -> Registry:
    reg = Registry()
    for path in SCHEMA_DIR.glob("*.schema.json"):
        doc = json.loads(path.read_text())
        res = Resource.from_contents(doc)
        reg = reg.with_resource(doc["$id"], res)
        reg = reg.with_resource(path.name, res)  # allow relative "$ref": "provenance.schema.json#/..."
    return reg


def validator(name: str) -> Draft202012Validator:
    path = SCHEMA_DIR / f"{name}.schema.json"
    doc = json.loads(path.read_text())
    return Draft202012Validator(doc, registry=_schema_registry())


def load_yaml(path: Path) -> Any:
    with path.open() as fh:
        return yaml.safe_load(fh)


@dataclass
class Issue:
    severity: str  # "error" | "warning"
    where: str
    message: str

    def __str__(self) -> str:
        return f"[{self.severity}] {self.where}: {self.message}"


@dataclass
class Evidence:
    parameters: dict[str, dict] = field(default_factory=dict)
    parameter_files: dict[str, Path] = field(default_factory=dict)
    scenarios: dict[str, dict] = field(default_factory=dict)
    assumptions: dict[str, dict] = field(default_factory=dict)
    materials: dict[str, dict] = field(default_factory=dict)
    sources: dict[str, dict] = field(default_factory=dict)
    conflicts: dict[str, dict] = field(default_factory=dict)
    proposals: dict[str, dict] = field(default_factory=dict)
    issues: list[Issue] = field(default_factory=list)

    # ------------------------------------------------------------------ helpers
    def error(self, where: str, msg: str) -> None:
        self.issues.append(Issue("error", where, msg))

    def warn(self, where: str, msg: str) -> None:
        self.issues.append(Issue("warning", where, msg))

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "error"]


def _validate_doc(ev: Evidence, name: str, doc: Any, where: str) -> bool:
    ok = True
    for err in sorted(validator(name).iter_errors(doc), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path)
        ev.error(f"{where}:{loc}", err.message[:300])
        ok = False
    return ok


def load_all(root: Path = REPO_ROOT) -> Evidence:
    ev = Evidence()
    # ---- sources
    src_path = root / "research" / "source_registry.yaml"
    if src_path.exists():
        doc = load_yaml(src_path) or {"sources": []}
        _validate_doc(ev, "source", doc, str(src_path.relative_to(root)))
        for s in doc.get("sources", []):
            sid = s.get("source_id")
            if sid in ev.sources:
                ev.error(src_path.name, f"duplicate source_id {sid}")
            ev.sources[sid] = s
    else:
        ev.warn("research/source_registry.yaml", "missing")
    # ---- parameters (every yaml under parameters/ except assumptions, materials, scenarios)
    for path in sorted((root / "parameters").rglob("*.yaml")):
        rel = str(path.relative_to(root))
        doc = load_yaml(path)
        if doc is None:
            ev.warn(rel, "empty file")
            continue
        if "assumptions" in doc:
            _validate_doc(ev, "assumption", doc, rel)
            for a in doc["assumptions"]:
                aid = a.get("assumption_id")
                if aid in ev.assumptions:
                    ev.error(rel, f"duplicate assumption_id {aid}")
                ev.assumptions[aid] = a
        elif "materials" in doc:
            _validate_doc(ev, "material", doc, rel)
            for m in doc["materials"]:
                ev.materials[m.get("material_id")] = m
        elif "scenarios" in doc:
            _validate_doc(ev, "machine", doc, rel)
            for s in doc["scenarios"]:
                sid = s.get("scenario_id")
                if sid in ev.scenarios:
                    ev.error(rel, f"duplicate scenario_id {sid}")
                ev.scenarios[sid] = s
        elif "parameters" in doc:
            _validate_doc(ev, "provenance", doc, rel)
            for p in doc["parameters"]:
                pid = p.get("parameter_id")
                if pid in ev.parameters:
                    ev.error(rel, f"duplicate parameter_id {pid} (also in {ev.parameter_files[pid]})")
                ev.parameters[pid] = p
                ev.parameter_files[pid] = path.relative_to(root)
        else:
            ev.error(rel, "unknown document type (expected parameters/assumptions/materials/scenarios)")
    # ---- conflicts
    conf_path = root / "research" / "source_conflicts.yaml"
    if conf_path.exists():
        doc = load_yaml(conf_path) or {"conflicts": []}
        _validate_doc(ev, "conflict", doc, "research/source_conflicts.yaml")
        for c in doc.get("conflicts", []):
            ev.conflicts[c.get("conflict_id")] = c
    # ---- proposals
    for path in sorted((root / "theory" / "benchmarks").glob("*/proposal.yaml")):
        rel = str(path.relative_to(root))
        doc = load_yaml(path)
        _validate_doc(ev, "proposal", doc, rel)
        ev.proposals[doc.get("proposal_id")] = doc
    cross_check(ev)
    return ev


def cross_check(ev: Evidence) -> None:
    """Referential integrity and the null-vs-zero / provenance rules."""
    for pid, p in ev.parameters.items():
        where = f"{ev.parameter_files.get(pid)}:{pid}"
        prov = p.get("provenance", {})
        status = prov.get("status")
        value = p.get("value")
        # units
        try:
            parse_unit(p.get("unit", ""))
        except ValueError as exc:
            ev.error(where, str(exc))
        # null vs zero
        if status == "unknown" and value is not None:
            ev.error(where, "status 'unknown' requires value null")
        if status != "unknown" and status != "scan_variable" and value is None:
            ev.error(where, f"value null but status is {status!r} (use 'unknown' or give a value)")
        if value == 0 and not p.get("notes"):
            ev.warn(where, "value 0 without a note explaining that zero is a physical value, not 'unknown'")
        # sources
        src = prov.get("source")
        if src and src.get("source_id") and src["source_id"] not in ev.sources:
            ev.error(where, f"unknown source_id {src['source_id']}")
        if status in ("reported_lhmuc", "imported_related", "analogous") and not (src and src.get("quotation")):
            ev.error(where, f"status {status} requires a source quotation")
        if status == "reported_lhmuc" and src and src.get("source_id") in ev.sources:
            if ev.sources[src["source_id"]].get("category") != "PRIMARY_LHMUC":
                ev.error(where, "reported_lhmuc requires a PRIMARY_LHMUC source")
        if status in ("derived_lhmuc", "analytical_estimate") and not prov.get("derivation"):
            ev.error(where, f"status {status} requires a derivation")
        # assumptions
        if status == "synthetic":
            aid = prov.get("assumption_id")
            if aid not in ev.assumptions:
                ev.error(where, f"synthetic parameter without assumption record ({aid})")
            elif not p.get("allowed_range"):
                ev.error(where, "synthetic parameter must carry an allowed_range (no bare point values)")
        # dependencies
        for dep in p.get("dependencies", []):
            if dep not in ev.parameters:
                ev.error(where, f"unknown dependency {dep}")
        # scenario
        sc = p.get("scenario")
        if sc and sc not in ev.scenarios:
            ev.error(where, f"unknown scenario {sc}")
    for aid, a in ev.assumptions.items():
        if a.get("parameter_id") not in ev.parameters:
            ev.warn(f"assumption {aid}", f"parameter_id {a.get('parameter_id')} has no parameter record")
    for sid, s in ev.scenarios.items():
        for role, pid in s.get("parameters", {}).items():
            if pid not in ev.parameters:
                ev.error(f"scenario {sid}", f"role {role} references unknown parameter {pid}")
        for src in s.get("primary_source_ids", []):
            if src not in ev.sources:
                ev.error(f"scenario {sid}", f"unknown source {src}")
    for cid, c in ev.conflicts.items():
        for pid in c.get("affected_parameters", []):
            if pid not in ev.parameters:
                ev.warn(f"conflict {cid}", f"affected parameter {pid} has no record")
        for v in c.get("competing_values", []):
            if v.get("source_id") not in ev.sources:
                ev.error(f"conflict {cid}", f"unknown source {v.get('source_id')}")
    for prid, pr in ev.proposals.items():
        if pr.get("source_id") not in ev.sources:
            ev.error(f"proposal {prid}", f"unknown source {pr.get('source_id')}")


def status_counts(ev: Evidence) -> dict[str, int]:
    out: dict[str, int] = {}
    for p in ev.parameters.values():
        s = p["provenance"]["status"]
        out[s] = out.get(s, 0) + 1
    return dict(sorted(out.items()))
