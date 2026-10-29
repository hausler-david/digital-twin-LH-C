"""Load, validate and cross-check the evidence registries.

Single source of truth: YAML files under parameters/ (parameter records, scenarios, assumptions,
materials), research/source_registry.yaml and research/source_conflicts.yaml. CSV registries in
registries/ are *generated* from these by tools/build_registries.py and must stay in sync.
"""
from __future__ import annotations

import json
import re
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
    archives: dict[str, dict] = field(default_factory=dict)  # research/archived_metadata/<source_id>.json
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
    # ---- archived-file metadata (docs/internet_research_protocol.md §5a, §6)
    arch_dir = root / "research" / "archived_metadata"
    for path in sorted(arch_dir.glob("*.json")) if arch_dir.is_dir() else []:
        rel = str(path.relative_to(root))
        try:
            doc = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            ev.error(rel, f"invalid JSON: {exc}")
            continue
        if _validate_doc(ev, "archived_metadata", doc, rel) and doc.get("source_id") != path.stem:
            ev.error(rel, f"file name does not match its source_id {doc.get('source_id')}")
        ev.archives[path.stem] = doc
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
    cross_check(ev, root)
    return ev


TEST_NAME_RE = re.compile(r"(test_\w+)")


def registered_test_names(root: Path = REPO_ROOT) -> set[str]:
    """Names of all pytest functions under tests/ (used by the P1 rule of docs/validation_plan.md)."""
    names: set[str] = set()
    for f in (root / "tests").rglob("test_*.py"):
        names |= set(re.findall(r"^def (test_\w+)", f.read_text(), re.M))
    return names


def p1_test_references(validation: dict) -> set[str]:
    """test_* names cited in validation.methods and validation.check_ids."""
    text = " ".join(map(str, (validation.get("methods") or []) + (validation.get("check_ids") or [])))
    return set(TEST_NAME_RE.findall(text))


CONFIDENCE_RANK = {"none": 0, "low": 1, "medium": 2, "high": 3}

# Access modes (schemas/provenance.schema.json $defs/access_mode). Only a document read in full from its own file (a PDF
# or slides with page images) is uncapped; fetched_text is read in full but only as connector-delivered text
# (owner decision 2026-10-29, docs/internet_research_protocol.md §5a).
FULL_PAGE_READ = ("uploaded", "fetched")
TEXT_ONLY = ("fetched_text",)
READ_IN_FULL = FULL_PAGE_READ + TEXT_ONLY
NOT_READ_IN_FULL = ("snippet_only", "blocked", "pending_fetch")
FETCHED_TEXT_NOTE = "not checked against page images"
SOURCE_BACKED = ("reported_lhmuc", "imported_related", "analogous")


def confidence_cap(prov: dict, source: dict | None) -> tuple[str | None, str]:
    """Lowest applicable confidence cap of research/source_quality_policy.md §4.

    Only the mechanical rules are applied here: synthetic values, status analogous, imported_related from a
    design_variant, sources not read in full with page images (fail closed: any access other than uploaded or fetched,
    including fetched_text), and unrefereed slides. The conflict rule (low while a conflict has no decided treatment)
    is applied by hand when a conflict record is written; the cap a derived record inherits from its inputs is applied
    by cross_check (capped_inputs).
    Returns (cap, reason) or (None, "") when no cap applies.
    """
    caps: list[tuple[str, str]] = []
    status = prov.get("status")
    if status == "synthetic":
        caps.append(("low", "synthetic value"))
    if status == "analogous":
        caps.append(("medium", "status analogous"))
    if status == "imported_related" and (prov.get("applicability") or {}).get("category") == "design_variant":
        caps.append(("medium", "imported_related from a design_variant"))
    if source:
        access = source.get("access")
        if access in TEXT_ONLY:
            caps.append(("medium", f"source access {access} (connector-delivered text, {FETCHED_TEXT_NOTE})"))
        elif access not in FULL_PAGE_READ:
            caps.append(("medium", f"source access {access}"))
        if source.get("source_type") == "workshop_talk":
            caps.append(("medium", "unrefereed slides"))
    if not caps:
        return None, ""
    return min(caps, key=lambda c: CONFIDENCE_RANK[c[0]])


LEVEL_ORDER = ("P0", "P1", "P2", "P3", "P4", "P5")


def scenario_level_cap(ev: Evidence, scenario: dict) -> str:
    """docs/validation_plan.md §1 rule 3: the label of a composite is the minimum over its inputs. A scenario's inputs
    are the records its roles point to; a scenario without any role record is capped at P0."""
    levels = [(ev.parameters[pid].get("validation") or {}).get("level", "P0")
              for pid in (scenario.get("parameters") or {}).values() if pid in ev.parameters]
    return min(levels, key=LEVEL_ORDER.index) if levels else "P0"


PARAM_ID_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")


def capped_inputs(ev: Evidence, pid: str) -> list[tuple[str, str]]:
    """Inputs of a record (its dependencies, transitively, and the parameter or material ids named in its derivation)
    whose cited source was not read in full with page images. A derived_lhmuc or analytical_estimate record inherits
    their 'medium' cap (research/source_quality_policy.md §4), so a number read from connector text or a snippet cannot
    gain confidence by passing through a formula. An id that a derivation merely mentions counts as an input too: this
    over-caps, which is the safe direction."""
    out: list[tuple[str, str]] = []
    seen, todo = {pid}, [pid]
    while todo:
        rec = ev.parameters.get(todo.pop())
        if rec is None:
            continue
        nxt = list(rec.get("dependencies") or [])
        nxt += [t for t in PARAM_ID_RE.findall((rec.get("provenance") or {}).get("derivation") or "")
                if t in ev.parameters or t in ev.materials]
        for q in nxt:
            if q in seen:
                continue
            seen.add(q)
            todo.append(q)
            inp = ev.parameters.get(q) or ev.materials.get(q) or {}
            sid = ((inp.get("provenance") or {}).get("source") or {}).get("source_id")
            access = (ev.sources.get(sid) or {}).get("access") if sid else None
            if access is not None and access not in FULL_PAGE_READ:
                out.append((q, access))
    return out


def _check_provenance(ev: Evidence, where: str, prov: dict, notes: str | None, cap_hint: str) -> None:
    """Provenance rules shared by parameter and material records (research/source_quality_policy.md §3-§4,
    docs/internet_research_protocol.md §5-§5a)."""
    status = prov.get("status")
    src = prov.get("source") or {}
    sid = src.get("source_id")
    source = ev.sources.get(sid) if sid else None
    if sid and source is None:
        ev.error(where, f"unknown source_id {sid}")
    if status in SOURCE_BACKED and not src.get("quotation"):
        ev.error(where, f"status {status} requires a source quotation")
    if source is not None:
        access = source.get("access")
        if status == "reported_lhmuc":
            if source.get("category") != "PRIMARY_LHMUC":
                ev.error(where, "reported_lhmuc requires a PRIMARY_LHMUC source")
            if access not in READ_IN_FULL:
                ev.error(where, f"reported_lhmuc requires a source read in full (access {', '.join(READ_IN_FULL)}); "
                                f"{sid} is {access}")
        if status in SOURCE_BACKED and source.get("category") == "UNVERIFIED":
            ev.error(where, f"status {status} cites UNVERIFIED source {sid}, which backs no status "
                            "(research/source_quality_policy.md §3)")
        has_note = FETCHED_TEXT_NOTE in (notes or "").lower()
        if access in TEXT_ONLY:
            if prov.get("extraction_method") == "manual_figure_read":
                ev.error(where, f"{sid} is fetched_text (connector-delivered text, no page images): no figure reads")
            if not has_note:
                ev.error(where, f"a record citing the fetched_text source {sid} must say '{FETCHED_TEXT_NOTE}' in its notes")
            page = src.get("page")
            if not isinstance(page, int) or isinstance(page, bool) or page < 1:
                ev.error(where, f"page must be the integer PDF page of the saved page-tagged text of {sid} "
                                "(docs/internet_research_protocol.md §5a)")
        elif has_note:
            ev.warn(where, f"notes say '{FETCHED_TEXT_NOTE}' but {sid} now has access {access}: re-verify the record "
                           "against page images, then update the note")
    # confidence caps (research/source_quality_policy.md §4)
    cap, why = confidence_cap(prov, source)
    conf = prov.get("confidence")
    if cap is not None and CONFIDENCE_RANK.get(conf, 0) > CONFIDENCE_RANK[cap]:
        ev.error(where, f"confidence {conf!r} exceeds the {cap!r} cap of research/source_quality_policy.md §4 ({why}); {cap_hint}")


def cross_check(ev: Evidence, root: Path = REPO_ROOT) -> None:
    """Referential integrity and the null-vs-zero / provenance rules."""
    tests = registered_test_names(root)
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
        # sources, status admissibility and confidence caps
        _check_provenance(ev, where, prov, p.get("notes"), "lower it, e.g. with tools/apply_confidence_caps.py")
        if status in ("derived_lhmuc", "analytical_estimate"):
            if not prov.get("derivation"):
                ev.error(where, f"status {status} requires a derivation")
            inputs = capped_inputs(ev, pid)
            if inputs and CONFIDENCE_RANK.get(prov.get("confidence"), 0) > CONFIDENCE_RANK["medium"]:
                ev.error(where, f"confidence {prov.get('confidence')!r} exceeds the 'medium' cap inherited from input "
                                f"{inputs[0][0]} (source access {inputs[0][1]}; research/source_quality_policy.md §4); lower it "
                                "by hand (tools/apply_confidence_caps.py does not compute inherited caps)")
            text_inputs = [q for q, acc in inputs if acc in TEXT_ONLY]
            if text_inputs and FETCHED_TEXT_NOTE not in (p.get("notes") or "").lower():
                ev.error(where, f"derived from fetched_text input(s) {', '.join(text_inputs)}: notes must say '{FETCHED_TEXT_NOTE}'")
        # P1 needs a registered test (docs/validation_plan.md, P1 entry criterion)
        val = p.get("validation") or {}
        if val.get("level") == "P1" and not (p1_test_references(val) & tests):
            ev.error(where, "validation level P1 requires validation.methods or check_ids to name an existing test function "
                            "under tests/ (docs/validation_plan.md); add the test or lower the level with "
                            "tools/apply_validation_levels.py")
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
    for mid, m in ev.materials.items():
        _check_provenance(ev, f"material {mid}", m.get("provenance") or {}, m.get("notes"),
                          "lower it by hand (tools/apply_confidence_caps.py processes parameter files only)")
    for aid, a in ev.assumptions.items():
        if a.get("parameter_id") not in ev.parameters:
            ev.warn(f"assumption {aid}", f"parameter_id {a.get('parameter_id')} has no parameter record")
        if a.get("status") == "superseded_by_evidence":
            sup = a.get("superseded_by") or []
            if not sup:
                ev.error(f"assumption {aid}", "status superseded_by_evidence requires a non-empty superseded_by list")
            for pid in sup:
                if pid not in ev.parameters:
                    ev.error(f"assumption {aid}", f"superseded_by references unknown parameter {pid}")
                elif ev.parameters[pid]["provenance"]["status"] in ("synthetic", "unknown", "scan_variable"):
                    ev.error(f"assumption {aid}", f"superseded_by {pid} is not an evidence-backed record")
            if not a.get("superseded_on"):
                ev.error(f"assumption {aid}", "superseded_by_evidence requires superseded_on")
    for sid, s in ev.scenarios.items():
        for role, pid in s.get("parameters", {}).items():
            if pid not in ev.parameters:
                ev.error(f"scenario {sid}", f"role {role} references unknown parameter {pid}")
        # a scenario is a composite of its role records (docs/validation_plan.md §1 rule 3)
        cap = scenario_level_cap(ev, s)
        lvl = s.get("validation_level", "P0")
        if lvl in LEVEL_ORDER and LEVEL_ORDER.index(lvl) > LEVEL_ORDER.index(cap):
            ev.error(f"scenario {sid}", f"validation_level {lvl} exceeds {cap}, the minimum over its role records "
                                        "(docs/validation_plan.md §1 rule 3); lower it with tools/apply_scenario_levels.py")
        for src in s.get("primary_source_ids", []):
            if src not in ev.sources:
                ev.error(f"scenario {sid}", f"unknown source {src}")
        for role, pid in s.get("parameters", {}).items():
            p = ev.parameters.get(pid)
            if p and p["provenance"]["status"] == "synthetic":
                a = ev.assumptions.get(p["provenance"].get("assumption_id"))
                if a and a.get("status") == "superseded_by_evidence":
                    ev.error(f"scenario {sid}", f"role {role} points to synthetic {pid} whose assumption is superseded; use {a.get('superseded_by')}")
    for cid, c in ev.conflicts.items():
        for pid in c.get("affected_parameters", []):
            if pid not in ev.parameters:
                ev.warn(f"conflict {cid}", f"affected parameter {pid} has no record")
        for v in c.get("competing_values", []):
            src = ev.sources.get(v.get("source_id"))
            if src is None:
                ev.error(f"conflict {cid}", f"unknown source {v.get('source_id')}")
            elif src.get("access") in TEXT_ONLY and "fetched_text" not in (v.get("context") or ""):
                ev.error(f"conflict {cid}", f"competing value from {v.get('source_id')} must say 'fetched_text' in its context")
    for prid, pr in ev.proposals.items():
        src = ev.sources.get(pr.get("source_id"))
        if src is None:
            ev.error(f"proposal {prid}", f"unknown source {pr.get('source_id')}")
        elif (pr.get("access") in READ_IN_FULL or src.get("access") in READ_IN_FULL) and pr.get("access") != src.get("access"):
            ev.error(f"proposal {prid}", f"access {pr.get('access')} differs from the registry access {src.get('access')} "
                                         f"of {pr.get('source_id')}")
    # archived-file metadata and connector texts (docs/internet_research_protocol.md §5a, §6)
    for sid, a in ev.archives.items():
        s = ev.sources.get(sid)
        if s is None:
            ev.error(f"research/archived_metadata/{sid}.json", f"no source {sid} in research/source_registry.yaml")
            continue
        if a.get("sha256") != s.get("sha256"):
            ev.error(f"source {sid}", f"registry sha256 {s.get('sha256')} differs from research/archived_metadata/{sid}.json "
                                      f"({a.get('sha256')})")
        if a.get("content_kind") == "connector_text" and s.get("access") not in TEXT_ONLY:
            ev.error(f"source {sid}", f"connector_text archive on a source with access {s.get('access')}")
    for sid, s in ev.sources.items():
        if s.get("access") not in TEXT_ONLY:
            continue
        a = ev.archives.get(sid)
        if a is None or a.get("content_kind") != "connector_text":
            ev.error(f"source {sid}", "access fetched_text requires research/archived_metadata/<source_id>.json with "
                                      "content_kind connector_text")
            continue
        local = a.get("local_file") or ""
        if not local.startswith(f"references/_local/{sid}/"):
            ev.error(f"source {sid}", f"connector text must be saved under references/_local/{sid}/ (is {local})")
        if (s.get("archived_file") or "").split(" ")[0] != local:
            ev.error(f"source {sid}", "archived_file must begin with the local_file of its archived metadata")
        # what was requested and what came back (docs/internet_research_protocol.md §5a)
        arxiv_id, v = s.get("arxiv_id") or "", a.get("delivered_version") or ""
        if not re.search(rf"(?<![0-9A-Za-z]){re.escape(v)}(?!\d)", s.get("version") or "") or not v:
            ev.error(f"source {sid}", f"registry version must name the delivered version {v or None}")
        if not sid.startswith("SRC_ARXIV_" + arxiv_id.replace(".", "_")):
            ev.error(f"source {sid}", f"a fetched_text source id must be SRC_ARXIV_<id> of its arxiv_id {arxiv_id}")
        calls = a.get("connector_calls") or []
        url = f"https://arxiv.org/abs/{arxiv_id}{v}"
        if not any(c.get("tool") == "get_paper_content" and (c.get("arguments") or {}).get("fullText") is True
                   and (c.get("arguments") or {}).get("url") == url for c in calls):
            ev.error(f"source {sid}", f"archived metadata needs a get_paper_content call with fullText true on {url}")
        for c in calls:
            if c.get("tool") not in ("get_paper_content", "answer_pdf_queries"):
                ev.error(f"source {sid}", f"connector call {c.get('tool')} cannot back a fetched_text source")
            elif c.get("tool") == "answer_pdf_queries" and (c.get("arguments") or {}).get("paper") != f"{arxiv_id}{v}":
                ev.error(f"source {sid}", f"answer_pdf_queries must name the delivered version {arxiv_id}{v}")
        for pt in a.get("page_tag_files") or []:
            if not str(pt.get("file", "")).startswith(f"references/_local/{sid}/"):
                ev.error(f"source {sid}", f"page-tagged file {pt.get('file')} must be saved under references/_local/{sid}/")


def status_counts(ev: Evidence) -> dict[str, int]:
    out: dict[str, int] = {}
    for p in ev.parameters.values():
        s = p["provenance"]["status"]
        out[s] = out.get(s, 0) + 1
    return dict(sorted(out.items()))
