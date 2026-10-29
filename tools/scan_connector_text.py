#!/usr/bin/env python3
"""Scans for the alphaXiv connector route (docs/internet_research_protocol.md §5a).

  text FILE                 instruction-like strings in a saved connector text (fixed pattern list, versioned); prints
                            the instruction_scan object for research/archived_metadata/<source_id>.json
  transcripts PATH...       every mcp__alphaXiv__ call in the given session transcripts (files or directories of
                            *.jsonl); flags calls outside the admissible set and any call made from a subagent
                            transcript (only the lead session may call the connector); exit 1 if anything is flagged

Run: python -I tools/scan_connector_text.py text references/_local/<sid>/<file>
     python -I tools/scan_connector_text.py transcripts <session>.jsonl <session>/subagents --since 2026-10-29T23:00
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PATTERNS_VERSION = "2026-10-29.1"
PATTERNS = [re.compile(p, re.I) for p in (
    r"\b(ignore|disregard|forget)\b.{0,20}\b(previous|prior|above|earlier|all)\b.{0,20}\b(instructions?|prompts?|directions?)\b",
    r"\b(you are|act as|pretend to be)\b.{0,10}\b(an? )?(ai|assistant|language model|llm|chatbot|reviewer)\b",
    r"\b(system|developer) prompt\b",
    r"\bprompt injection\b",
    r"<\s*/?\s*(system|assistant|user|instructions?)\s*>",
    r"\b(do not|don't|never)\s+(reveal|mention|tell|disclose)\b",
    r"\b(give|assign|write)\b.{0,15}\b(paper|manuscript|submission)\b.{0,15}\b(positive|high|favou?rable)\b",
    r"\bas an ai\b|\blarge language model\b",
    r"\b(execute|run)\s+(the following|this)\s+(code|command|script)\b",
    r"\bnew instructions?\b",
)]
SERVER = "mcp__alphaXiv__"
VERSIONED_URL = re.compile(r"https://arxiv\.org/abs/\d{4}\.\d{4,5}v\d+")
VERSIONED_ID = re.compile(r"\d{4}\.\d{4,5}v\d+")


def scan_text(text: str) -> dict:
    hits = [{"line": n, "text": line.strip()[:300]} for n, line in enumerate(text.splitlines(), 1)
            if any(p.search(line) for p in PATTERNS)]
    return {"patterns_version": PATTERNS_VERSION, "hits": hits}


def admissible(tool: str, args: dict) -> str | None:
    """None if the call is admissible under §5a, else the reason."""
    if tool == "get_paper_content":
        if args.get("fullText") is not True:
            return "get_paper_content without fullText (AI-written report)"
        if not VERSIONED_URL.fullmatch(str(args.get("url", ""))):
            return "get_paper_content on an unversioned or non-arXiv url"
        return None
    if tool == "answer_pdf_queries":
        return None if VERSIONED_ID.fullmatch(str(args.get("paper", ""))) else "answer_pdf_queries without a versioned arXiv id"
    if tool == "discover_papers":
        return None
    return f"banned tool {tool}"


def scan_transcripts(paths: list[Path], since: str | None) -> list[dict]:
    files = []
    for p in paths:
        files += sorted(p.rglob("*.jsonl")) if p.is_dir() else [p]
    calls = []
    for f in files:
        role = "subagent" if "subagents" in f.parts else "lead"
        with f.open() as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if since and (d.get("timestamp") or "") < since:
                    continue
                for b in (d.get("message") or {}).get("content") or []:
                    if isinstance(b, dict) and b.get("type") == "tool_use" and str(b.get("name", "")).startswith(SERVER):
                        tool = b["name"].removeprefix(SERVER)
                        reason = admissible(tool, b.get("input") or {})
                        if role == "subagent":
                            reason = "called from a subagent transcript" + (f"; {reason}" if reason else "")
                        calls.append({"file": str(f), "role": role, "timestamp": d.get("timestamp"), "tool": tool,
                                      "arguments": b.get("input") or {}, "tool_use_id": b.get("id"), "flag": reason})
    return calls


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("text")
    t.add_argument("file", type=Path)
    s = sub.add_parser("transcripts")
    s.add_argument("paths", type=Path, nargs="+")
    s.add_argument("--since", help="ISO timestamp; earlier calls are ignored")
    a = ap.parse_args(argv)
    if a.cmd == "text":
        print(json.dumps(scan_text(a.file.read_text(encoding="utf-8")), ensure_ascii=False, indent=1))
        return 0
    calls = scan_transcripts(a.paths, a.since)
    print(json.dumps(calls, ensure_ascii=False, indent=1))
    flagged = [c for c in calls if c["flag"]]
    print(f"{len(calls)} connector call(s), {len(flagged)} flagged", file=sys.stderr)
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
