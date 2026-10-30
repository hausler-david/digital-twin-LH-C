#!/usr/bin/env python3
"""Save one alphaXiv connector result byte for byte for a fetched_text source (docs/internet_research_protocol.md §5a).

Only two calls are accepted: get_paper_content with fullText true on a versioned arXiv URL (saved as .txt) and
answer_pdf_queries on a versioned arXiv id (page-tagged text, saved as .xml). The text is taken from the session
transcript (the tool_result of the given tool_use_id) or, when the harness persisted a large result, from that file,
read as bytes; a "<persisted-output>" preview is never saved, nor an error result or a result that is not exactly one
text block. The file goes to references/_local/<source_id>/<name> (git-ignored, mode 600) and must not exist yet:
archived files are never edited (§6). The tool prints the connector_call object and, for page-tagged text, the
page_tag_file object of schemas/archived_metadata.schema.json, plus the SHA-256 and size of the saved file.

The result text is untrusted (CLAUDE.md §5): a harness pointer is followed only when the result *starts* with the
harness's own notice, and only to a file directly inside <transcript dir>/<transcript stem>/tool-results/ (no symlinks;
an oversize file must be named mcp-alphaXiv-<tool>-*). A notice anywhere else is delivered text and is saved as such.
A one-line "not found" refusal is never saved as a delivered text; --probe saves the answer of a later-version probe
(answer_pdf_queries on <id>v<n+1>, docs/internet_research_protocol.md §5a) as probe_*.txt, error results included, and
prints the later_version_probe object.

Run: python -I tools/save_connector_text.py --transcript <session.jsonl> --tool-use-id <id> --source-id SRC_... --name <file>
     python -I tools/save_connector_text.py --probe --transcript <session.jsonl> --tool-use-id <id> --source-id SRC_... \
         --name probe_<id>v<k>.txt
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREVIEW_MARK = "<persisted-output>"
# the harness's own notices, matched only at the start of a result (anywhere else they are delivered text)
PERSISTED_RE = re.compile(r"<persisted-output>\nOutput too large \([^)\n]*\)\. Full output saved to: (\S+)\n")
OVERSIZE_RE = re.compile(r"Error: result \(([\d,]+) characters across ([\d,]+) lines\) exceeds maximum allowed tokens\. "
                         r"Output has been saved to (\S+?)\.?(?:\n|$)")
# a one-line refusal ("Paper version not found for ID: 2506.15445v2"): never a delivered text
NOT_FOUND_RE = re.compile(r"\s*[^\n<]{0,120}\bnot found\b[^\n<]{0,120}\s*", re.I)
PAGE_RE = re.compile(r'<page num="(\d+)">')
PAPER_RE = re.compile(r'<paper id="([^"]+)">')
VERSIONED_URL = re.compile(r"https://arxiv\.org/abs/\d{4}\.\d{4,5}v\d+")
VERSIONED_ID = re.compile(r"\d{4}\.\d{4,5}v\d+")


def _one_text_block(content) -> str:
    if isinstance(content, str):
        return content
    blocks = list(content or [])
    if len(blocks) != 1 or not isinstance(blocks[0], dict) or blocks[0].get("type") != "text":
        raise SystemExit(f"result is not exactly one text block ({len(blocks)} block(s)): refusing to save")
    return blocks[0].get("text", "")


def find_call(transcript: Path, tool_use_id: str) -> tuple[dict, dict, str | None]:
    """Return (tool_use block, tool_result block, timestamp of the tool_use line) from a session transcript."""
    use = result = stamp = None
    with transcript.open() as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            content = (d.get("message") or {}).get("content")
            if not isinstance(content, list):
                continue
            for b in content:
                if b.get("type") == "tool_use" and b.get("id") == tool_use_id:
                    use, stamp = b, d.get("timestamp")
                elif b.get("type") == "tool_result" and b.get("tool_use_id") == tool_use_id:
                    result = b
    if use is None or result is None:
        raise SystemExit(f"tool_use_id {tool_use_id} or its result not found in {transcript}")
    return use, result, stamp


def check_call(use: dict, name: str, probe: bool = False) -> str:
    """The tool name without the server prefix, if the call is one of the two admissible calls."""
    tool = str(use.get("name", "")).removeprefix("mcp__alphaXiv__")
    args = use.get("input") or {}
    if probe:
        if tool != "answer_pdf_queries" or not VERSIONED_ID.fullmatch(str(args.get("paper", ""))):
            raise SystemExit("--probe saves only answer_pdf_queries on a versioned arXiv id <id>v<n>")
        if not (name.startswith(f"probe_{args['paper']}") and name.endswith(".txt")):
            raise SystemExit(f"a probe answer is saved as probe_{args['paper']}[_suffix].txt")
        return tool
    if name.startswith("probe_"):
        raise SystemExit("probe_* names are reserved for --probe")
    if tool == "get_paper_content":
        if args.get("fullText") is not True or not VERSIONED_URL.fullmatch(str(args.get("url", ""))):
            raise SystemExit("get_paper_content must have fullText true and a versioned https://arxiv.org/abs/<id>v<n> url")
        if not name.endswith(".txt"):
            raise SystemExit("the full text is saved as .txt")
    elif tool == "answer_pdf_queries":
        if not VERSIONED_ID.fullmatch(str(args.get("paper", ""))):
            raise SystemExit("answer_pdf_queries must name a versioned arXiv id <id>v<n>")
        if not name.endswith(".xml"):
            raise SystemExit("page-tagged text is saved as .xml")
    else:
        raise SystemExit(f"{use.get('name')} is not an admissible connector call (docs/internet_research_protocol.md §5a)")
    return tool


def _confined(path: str, tool_results: Path, prefix: str | None = None) -> Path:
    """A harness file named by a pointer: an absolute path, not itself a symlink, whose real location is directly
    inside the real tool_results directory (symlinked ancestor directories are allowed; the target is what counts)."""
    p = Path(path)
    if not p.is_absolute() or os.path.islink(p):
        raise SystemExit(f"pointer {path} is not an absolute path to a regular file: refusing to follow it")
    real = Path(os.path.realpath(p))
    if real.parent != Path(os.path.realpath(tool_results)):
        raise SystemExit(f"pointer {path} is outside {tool_results}: refusing to follow it")
    if prefix and not real.name.startswith(prefix):
        raise SystemExit(f"pointer {path} does not name a harness file {prefix}*: refusing to follow it")
    return p


MIN_TEXT_BYTES, MIN_TEXT_LINES = 2048, 50  # smallest calibration full text: 16,610 bytes, 913 lines


def check_structure(data: bytes, name: str) -> None:
    """A delivered text must look like one: page-tagged XML with a paper id and at least one page, or a multi-line
    full text above a floor. Anything else (an empty answer, a refusal in other words, an error page) is refused."""
    text = data.decode("utf-8", errors="replace")
    if name.endswith(".xml"):
        if not PAPER_RE.search(text) or not PAGE_RE.search(text):
            raise SystemExit("the answer has no <paper id> and <page num> blocks: not page-tagged text (refusing)")
    elif len(data) < MIN_TEXT_BYTES or len(text.splitlines()) < MIN_TEXT_LINES:
        raise SystemExit(f"the answer has {len(data)} bytes and {len(text.splitlines())} lines: too small for a full text "
                         f"(at least {MIN_TEXT_BYTES} bytes and {MIN_TEXT_LINES} lines); refusals are saved with --probe")


def resolve_bytes(result: dict, tool_results: Path, tool: str = "", probe: bool = False) -> tuple[bytes, bool]:
    """The result as bytes; follows the harness pointer when the result starts with the harness's own notice."""
    if result.get("is_error") and not probe:
        raise SystemExit("the tool returned an error: refusing to save")
    text = _one_text_block(result.get("content"))
    big = OVERSIZE_RE.match(text)
    if big:
        raw = _confined(big.group(3), tool_results, f"mcp-alphaXiv-{tool}-").read_bytes()
        n_chars, n_lines = int(big.group(1).replace(",", "")), int(big.group(2).replace(",", ""))
        decoded = raw.decode("utf-8")
        if len(decoded) != n_chars or len(decoded.splitlines()) != n_lines:
            raise SystemExit(f"saved result has {len(decoded)} characters and {len(decoded.splitlines())} lines; the harness "
                             f"reported {n_chars} and {n_lines}: refusing to save an incomplete file")
        return raw, True
    if not text.startswith(PREVIEW_MARK):
        if not probe and NOT_FOUND_RE.fullmatch(text):
            raise SystemExit(f"the result is a refusal, not a delivered text ({text.strip()[:80]!r}); a probe answer is "
                             "saved with --probe")
        return text.encode("utf-8"), False
    m = PERSISTED_RE.match(text)
    if not m:
        raise SystemExit("transcript holds a persisted-output preview without a file path: refusing to save a preview")
    raw = _confined(m.group(1), tool_results).read_bytes()
    try:
        doc = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raw.decode("utf-8")  # must be text
        return raw, True
    if isinstance(doc, list):
        return _one_text_block(doc).encode("utf-8"), True
    raise SystemExit("persisted result has an unknown JSON shape: refusing to save")


def save(data: bytes, target: Path) -> dict:
    if target.exists():
        raise SystemExit(f"{target} exists: archived files are never overwritten (docs/internet_research_protocol.md §6)")
    target.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as fh:
        fh.write(data)
    return {"sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data)}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--transcript", type=Path, required=True)
    ap.add_argument("--tool-use-id", required=True)
    ap.add_argument("--source-id", required=True)
    ap.add_argument("--name", required=True, help="file name inside references/_local/<source_id>/")
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--probe", action="store_true", help="save the answer of a later-version probe (probe_*.txt)")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"SRC_[A-Z0-9_]+", a.source_id) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", a.name):
        raise SystemExit("invalid --source-id or --name")
    use, result, stamp = find_call(a.transcript, a.tool_use_id)
    tool = check_call(use, a.name, a.probe)
    tool_results = a.transcript.parent / a.transcript.stem / "tool-results"
    data, persisted = resolve_bytes(result, tool_results, tool, a.probe)
    if not a.probe:
        check_structure(data, a.name)
    rel = str(Path("references") / "_local" / a.source_id / a.name)
    saved = save(data, a.root / rel)
    call = {"tool": tool, "arguments": use.get("input") or {}, "tool_use_id": a.tool_use_id, "called_on": stamp or ""}
    out = {"file": rel, **saved, "persisted_by_harness": persisted, "connector_call": call}
    if a.probe:
        text = data.decode("utf-8", errors="replace")
        out["is_error"] = bool(result.get("is_error"))
        out["has_pages"] = bool(PAGE_RE.search(text))
        if not out["has_pages"] and len(text) <= 500:
            out["text"] = text
        out["later_version_probe"] = {**call, "file": rel, "sha256": saved["sha256"], "is_error": out["is_error"],
                                      "has_pages": out["has_pages"], "paper_id": (PAPER_RE.findall(text) or [None])[0],
                                      "pages": [int(n) for n in PAGE_RE.findall(text)]}
    elif tool == "answer_pdf_queries":
        text = data.decode("utf-8")
        out["paper_id"] = (PAPER_RE.findall(text) or [None])[0]
        out["page_tag_file"] = {"file": rel, "sha256": saved["sha256"], "size_bytes": saved["size_bytes"],
                                "pages": [int(n) for n in PAGE_RE.findall(text)], "tool_use_id": a.tool_use_id}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
