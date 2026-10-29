"""The fetched_text rules of lhmuc.registry (owner decision 2026-10-29, docs/internet_research_protocol.md §5a):
connector-delivered text read in full is capped at medium, says it was not checked against page images, cites an
integer PDF page, is never a figure read, and is backed by connector_text metadata that matches what was requested
(get_paper_content with fullText on the versioned URL); caps pass to derived records."""
import json

import yaml

from lhmuc.registry import FETCHED_TEXT_NOTE, Evidence, cross_check, load_all

SID = "SRC_ARXIV_1234_56789"
URL = "https://arxiv.org/abs/1234.56789v2"
NOTE = "Read from connector-delivered text (access fetched_text); not checked against page images."
HASH = "0" * 64


def _archive() -> dict:
    return {"source_id": SID, "content_kind": "connector_text", "sha256": HASH, "delivered_version": "v2",
            "local_file": f"references/_local/{SID}/fulltext.txt",
            "connector_calls": [
                {"tool": "get_paper_content", "arguments": {"url": URL, "fullText": True}, "tool_use_id": "t1", "called_on": "x"},
                {"tool": "answer_pdf_queries", "arguments": {"paper": "1234.56789v2", "queries": ["q"]}, "tool_use_id": "t2",
                 "called_on": "x"}],
            "page_tag_files": [{"file": f"references/_local/{SID}/pages.xml", "sha256": "1" * 64, "pages": [3],
                                "tool_use_id": "t2"}]}


def _ev(category: str = "PEER_REVIEWED", status: str = "imported_related", confidence: str = "medium",
        method: str = "manual_text_read", notes: str | None = NOTE, page=3, archive: bool = True) -> Evidence:
    ev = Evidence()
    ev.sources[SID] = {"source_id": SID, "access": "fetched_text", "category": category, "source_type": "arxiv_preprint",
                       "version": "v2 (requested and stated by the page-tagged response)", "sha256": HASH,
                       "arxiv_id": "1234.56789", "archived_file": f"references/_local/{SID}/fulltext.txt (git-ignored)"}
    if archive:
        ev.archives[SID] = _archive()
    ev.parameters["TEST_X"] = {"parameter_id": "TEST_X", "unit": "dimensionless", "value": 1.0, "notes": notes,
                               "provenance": {"status": status, "extraction_method": method, "confidence": confidence,
                                              "source": {"source_id": SID, "page": page, "quotation": "x = 1"},
                                              "applicability": {"category": "analogous", "explanation": "t"}},
                               "validation": {"level": "P0"}}
    return ev


def _messages(ev: Evidence) -> str:
    ev.issues.clear()
    cross_check(ev)
    return "\n".join(str(i) for i in ev.errors)


def _derived(pid: str, deps: list, derivation: str, confidence: str = "high", notes=None) -> dict:
    return {"parameter_id": pid, "unit": "dimensionless", "value": 2.0, "notes": notes, "dependencies": deps,
            "provenance": {"status": "analytical_estimate", "extraction_method": "computed_from_registry",
                           "confidence": confidence, "source": None, "derivation": derivation,
                           "applicability": {"category": "analogous", "explanation": "t"}},
            "validation": {"level": "P0"}}


def test_compliant_fetched_text_record_passes():
    assert _messages(_ev()) == ""
    assert _messages(_ev(category="PRIMARY_LHMUC", status="reported_lhmuc")) == ""


def test_fetched_text_confidence_above_medium_is_rejected():
    assert "exceeds the 'medium' cap" in _messages(_ev(confidence="high"))


def test_figure_read_from_fetched_text_is_rejected():
    assert "no figure reads" in _messages(_ev(method="manual_figure_read"))


def test_fetched_text_record_without_page_image_note_is_rejected():
    assert "in its notes" in _messages(_ev(notes="read from the connector"))


def test_fetched_text_record_needs_a_pdf_page_number():
    for page in ("§3.2", None, 0):
        assert "integer PDF page" in _messages(_ev(page=page)), page


def test_fetched_text_source_requires_connector_text_metadata():
    assert "content_kind connector_text" in _messages(_ev(archive=False))
    cases = [("sha256", "1" * 64, "differs"),
             ("local_file", "references/_local/SRC_OTHER/fulltext.txt", "must be saved under"),
             ("delivered_version", "v3", "delivered version")]
    for key, value, msg in cases:
        ev = _ev()
        ev.archives[SID][key] = value
        assert msg in _messages(ev), key


def test_archive_must_match_what_was_requested():
    calls = _archive()["connector_calls"]
    variants = {
        "no fullText": [{**calls[0], "arguments": {"url": URL}}, calls[1]],
        "other version": [{**calls[0], "arguments": {"url": "https://arxiv.org/abs/1234.56789v1", "fullText": True}}, calls[1]],
        "banned tool": calls + [{"tool": "get_paper_notes", "arguments": {}, "tool_use_id": "t3", "called_on": "x"}],
        "unversioned pages": [calls[0], {**calls[1], "arguments": {"paper": "1234.56789"}}],
    }
    for name, value in variants.items():
        ev = _ev()
        ev.archives[SID]["connector_calls"] = value
        assert _messages(ev), name
    ev = _ev()
    ev.archives[SID]["page_tag_files"][0]["file"] = "research/_fragments/pages.xml"
    assert "page-tagged file" in _messages(ev)
    ev = _ev()
    ev.sources[SID]["version"] = "v12"
    assert "delivered version" in _messages(ev)
    ev = _ev()
    ev.sources[SID]["arxiv_id"] = "2506.15445"
    assert "SRC_ARXIV_<id>" in _messages(ev)


def test_connector_text_metadata_on_another_source_is_rejected():
    ev = _ev()
    ev.sources[SID]["access"] = "uploaded"
    assert "connector_text archive on a source" in _messages(ev)


def test_note_kept_after_an_upload_replaces_the_connector_text_warns():
    ev = _ev()
    ev.sources[SID]["access"] = "uploaded"
    del ev.archives[SID]
    cross_check(ev)
    assert any("re-verify" in i.message for i in ev.issues if i.severity == "warning")


def test_reported_lhmuc_requires_a_source_read_in_full():
    ev = _ev(category="PRIMARY_LHMUC", status="reported_lhmuc")
    ev.sources[SID]["access"] = "snippet_only"
    del ev.archives[SID]
    assert "read in full" in _messages(ev)


def test_unverified_source_backs_no_status():
    assert "UNVERIFIED" in _messages(_ev(category="UNVERIFIED"))


def test_material_citing_fetched_text_is_checked():
    ev = _ev()
    ev.materials["MAT_TEST"] = {"material_id": "MAT_TEST", "notes": None,
                                "provenance": {**ev.parameters["TEST_X"]["provenance"], "confidence": "high"}}
    ev.issues.clear()
    cross_check(ev)
    mine = [i.message for i in ev.errors if i.where == "material MAT_TEST"]
    assert any("in its notes" in m for m in mine) and any("exceeds the 'medium' cap" in m for m in mine)
    ev.materials["MAT_TEST"].update(notes=NOTE)
    ev.materials["MAT_TEST"]["provenance"]["confidence"] = "medium"
    ev.issues.clear()
    cross_check(ev)
    assert not [i for i in ev.errors if i.where == "material MAT_TEST"]


def test_derived_records_inherit_the_fetched_text_cap_and_note():
    ev = _ev()
    ev.parameters["TEST_C"] = _derived("TEST_C", ["TEST_X"], "TEST_X + 1", confidence="medium", notes=NOTE)
    ev.parameters["TEST_D"] = _derived("TEST_D", ["TEST_C"], "2 × TEST_C")             # transitive
    ev.parameters["TEST_E"] = _derived("TEST_E", [], "3 × TEST_X (derivation text only)")  # derivation only
    msgs = _messages(ev)
    for pid in ("TEST_D", "TEST_E"):
        assert f"{pid}: confidence 'high' exceeds the 'medium' cap inherited" in msgs, pid
        assert f"{pid}: derived from fetched_text input" in msgs, pid
    assert "TEST_C:" not in msgs  # compliant: medium and the note


def test_proposal_access_must_match_a_registry_read_in_full_both_ways():
    ev = _ev()
    ev.proposals["PROP_TEST"] = {"proposal_id": "PROP_TEST", "source_id": SID, "access": "pending_fetch"}
    assert "differs from the registry access" in _messages(ev)
    ev = _ev()
    ev.sources[SID]["access"] = "blocked"
    del ev.archives[SID]
    ev.parameters.clear()
    ev.proposals["PROP_TEST"] = {"proposal_id": "PROP_TEST", "source_id": SID, "access": "fetched_text"}
    assert "differs from the registry access" in _messages(ev)
    ev.proposals["PROP_TEST"]["access"] = "pending_fetch"
    assert _messages(ev) == ""


def test_conflict_value_from_fetched_text_must_say_so():
    ev = _ev()
    ev.conflicts["CONF_TEST"] = {"conflict_id": "CONF_TEST", "affected_parameters": ["TEST_X"],
                                 "competing_values": [{"source_id": SID, "context": "p. 3"}]}
    assert "must say 'fetched_text'" in _messages(ev)


def _tmp_repo(tmp_path, archives: dict) -> None:
    (tmp_path / "research" / "archived_metadata").mkdir(parents=True)
    (tmp_path / "parameters").mkdir()
    src = {"source_id": "SRC_TEST_UPLOAD", "title": "t", "source_type": "journal_article", "category": "PEER_REVIEWED",
           "url": None, "access_date": "2026-10-29", "access": "uploaded", "relevance": "r", "sha256": "a" * 64}
    (tmp_path / "research" / "source_registry.yaml").write_text(yaml.safe_dump({"sources": [src]}))
    for name, text in archives.items():
        (tmp_path / "research" / "archived_metadata" / name).write_text(text)


def _pdf_archive(sid: str) -> dict:
    return {"source_id": sid, "local_file": "references/_local/x.pdf", "committed_copy": None, "title": "t", "authors": "a",
            "venue": "v", "identifier": None, "category": "PEER_REVIEWED", "licence": "l", "redistribution": "r", "pages": 1,
            "size_bytes": 1, "sha256": "a" * 64, "upload_name": "x.pdf", "archived_on": "2026-10-29", "archive_method": "m",
            "read_status": "read in full"}


def test_archive_files_on_disk_are_checked(tmp_path):
    _tmp_repo(tmp_path, {"SRC_TEST_UPLOAD.json": json.dumps(_pdf_archive("SRC_TEST_UPLOAD")),
                         "SRC_TEST_ORPHAN.json": json.dumps(_pdf_archive("SRC_TEST_ORPHAN")),
                         "SRC_TEST_RENAMED.json": json.dumps(_pdf_archive("SRC_TEST_UPLOAD")),
                         "SRC_TEST_BROKEN.json": "{not json"})
    msgs = "\n".join(str(i) for i in load_all(tmp_path).errors)
    assert "no source SRC_TEST_ORPHAN" in msgs
    assert "does not match its source_id" in msgs
    assert "invalid JSON" in msgs
    assert "SRC_TEST_UPLOAD.json" not in msgs  # the consistent archive passes
