#!/usr/bin/env python3
"""Scans for the alphaXiv connector route (docs/internet_research_protocol.md §5a).

  text FILE                 instruction-like strings in a saved connector text (fixed pattern list, versioned), line by
                            line and in the whitespace-collapsed text (connector texts break phrases over very short
                            lines); prints the instruction_scan object for research/archived_metadata/<source_id>.json
  transcripts PATH...       every mcp__alphaXiv__ call in the given session transcripts (files or directories of
                            *.jsonl); flags calls outside the admissible set and any call made from a subagent
                            transcript (only the lead session may call the connector). Also audits subagent transcripts
                            for any mcp__ call, any ToolSearch for an MCP tool, and git push / gh / curl / wget in Bash,
                            and counts discover_papers calls per assistant message (at most 2). Exit 1 if anything is
                            flagged.

Run: python -I tools/scan_connector_text.py text references/_local/<sid>/<file>
     python -I tools/scan_connector_text.py transcripts <session>.jsonl <session>/subagents --since 2026-10-29T23:00
"""
from __future__ import annotations

import argparse
import bisect
import json
import os
import re
import shlex
import sys
from pathlib import Path

PATTERNS_VERSION = "2026-10-30.1"  # same patterns as 2026-10-29.1, now also applied to the collapsed text
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
# line ends joined as tools/check_fetched_text_quotes.py joins them, so that every collapsed hit can be located there
LETTER_BREAK_RE = re.compile(r"(?<=[^\W\d_])-[ \t]*\n\s*(?=[^\W\d_])")   # dropped
OTHER_BREAK_RE = re.compile(r"[-−][ \t]*\n\s*")                          # the hyphen or minus is kept and joined
MAX_DISCOVERY_PER_MESSAGE = 2
# subagent Bash: a command is classified by its command word, not by a word anywhere in the line
NETWORK_COMMANDS = {"curl", "wget", "gh"}
SHELLS = {"bash", "sh", "zsh", "dash"}
WRAPPER_OPTS = {"env": {"-u", "-C", "-S"}, "sudo": {"-u", "-g", "-h", "-p", "-C", "-D", "-r", "-t", "-U"},
                "timeout": {"-s", "-k"}, "nice": {"-n"}, "xargs": {"-n", "-L", "-s", "-P", "-I", "-d", "-E", "-a"},
                "stdbuf": {"-i", "-o", "-e"}, "time": {"-f", "-o"}, "exec": {"-a"}, "nohup": set(), "command": set(),
                "builtin": set(), "!": set(), "{": set(), "if": set(), "then": set(), "else": set(), "elif": set(),
                "do": set(), "while": set(), "until": set()}
ASSIGNMENT_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*=.*", re.S)
HEREDOC_RE = re.compile(r"<<-?[ \t]*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1[^\n]*\n.*?\n[ \t]*\2[ \t]*(?=\n|$)", re.S)
SUBST_RE = re.compile(r"\$\(([^()]*(?:\([^()]*\)[^()]*)*)\)|`([^`]*)`")
BROAD_RE = re.compile(r"\b(?:curl|wget|gh)\b|\bgit\b.*\bpush\b", re.S)
PUNCT = ";&|()\n"


def _collapsed(text: str) -> tuple[str, list[int]]:
    """The text with whitespace collapsed and line ends joined as the quote checker joins them (a line-end hyphen
    between two letters dropped; any other line-end hyphen or minus kept and joined), plus the 1-based source line of
    every character, counted like str.splitlines (the line model of the line hits)."""
    starts = [0]
    for ln in text.splitlines(keepends=True):
        starts.append(starts[-1] + len(ln))
    chars: list[str] = []
    src: list[int] = []
    i, n = 0, len(text)
    while i < n:
        ch = text[i]
        if ch in "-−":
            m = LETTER_BREAK_RE.match(text, i) if ch == "-" else None
            if m:
                i = m.end()
                continue
            m = OTHER_BREAK_RE.match(text, i)
            if m:
                chars.append(ch)
                src.append(i)
                i = m.end()
                continue
        if ch.isspace():
            if chars and chars[-1] != " ":
                chars.append(" ")
                src.append(i)
        else:
            chars.append(ch)
            src.append(i)
        i += 1
    return "".join(chars), [bisect.bisect_right(starts, s) for s in src]


def _after_wrappers(argv: list[str]) -> list[str]:
    """argv without leading assignments and wrapper words (env, sudo, timeout, nohup, xargs, ...) with their options."""
    a = list(argv)
    while a and ASSIGNMENT_RE.fullmatch(a[0]):
        a.pop(0)
    while a and os.path.basename(a[0]) in WRAPPER_OPTS:
        w = os.path.basename(a.pop(0))
        while a and (a[0].startswith("-") or ASSIGNMENT_RE.fullmatch(a[0])):
            opt = a.pop(0)
            if opt in WRAPPER_OPTS[w] and a:
                a.pop(0)
        if w == "timeout" and a:
            a.pop(0)  # the duration
    return a


def _simple_commands(cmd: str, depth: int = 0) -> list[list[str]] | None:
    """The simple commands (argv lists) of a shell command, recursing into $(...), backticks and bash/sh -c; heredoc
    bodies are text, not commands. None if the command cannot be tokenised."""
    if depth > 4:
        return []
    cmd = HEREDOC_RE.sub(lambda m: m.group(0).split("\n", 1)[0], cmd)
    out: list[list[str]] = []
    for m in SUBST_RE.finditer(cmd):
        inner = _simple_commands(m.group(1) if m.group(1) is not None else m.group(2), depth + 1)
        if inner is None:
            return None
        out += inner
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=PUNCT)
        lex.whitespace = " \t\r"
        lex.whitespace_split = True
        tokens = list(lex)
    except ValueError:
        return None
    cur: list[str] = []
    for t in tokens + [";"]:
        if t and all(c in PUNCT for c in t):
            if cur:
                out.append(cur)
            cur = []
        else:
            cur.append(t)
    for argv in list(out):
        a = _after_wrappers(argv)
        if a and os.path.basename(a[0]) in SHELLS and "-c" in a[1:]:
            k = a.index("-c")
            if k + 1 < len(a):
                inner = _simple_commands(a[k + 1], depth + 1)
                if inner is None:
                    return None
                out += inner
    return out


def network_command(cmd: str) -> tuple[str | None, str | None]:
    """(network or push command run by a shell command, None) or (None, 'review') when the command cannot be parsed
    but mentions one; (None, None) otherwise. Detects command words only: a network call made from inside a Python or
    other program is not seen here (the network policy and the restricted agent type are the controls for that)."""
    cmds = _simple_commands(cmd)
    if cmds is None:
        return None, ("review" if BROAD_RE.search(cmd) else None)
    for argv in cmds:
        a = _after_wrappers(argv)
        if not a:
            continue
        b = os.path.basename(a[0])
        if b in NETWORK_COMMANDS:
            return b, None
        if b == "git":
            j = 1
            while j < len(a) and a[j].startswith("-"):
                j += 2 if a[j] in ("-C", "-c", "--git-dir", "--work-tree", "--namespace") else 1
            if j < len(a) and a[j] == "push":
                return "git push", None
    return None, None


def scan_text(text: str) -> dict:
    hits = [{"line": n, "text": line.strip()[:300], "kind": "line"} for n, line in enumerate(text.splitlines(), 1)
            if any(p.search(line) for p in PATTERNS)]
    flat, lines = _collapsed(text)
    seen = set()
    for p in PATTERNS:
        for m in p.finditer(flat):
            if (m.start(), m.end()) not in seen:
                seen.add((m.start(), m.end()))
                hits.append({"line": lines[m.start()], "text": m.group(0)[:300], "kind": "collapsed"})
    return {"patterns_version": PATTERNS_VERSION, "hits": sorted(hits, key=lambda h: (h["line"], h["kind"]))}


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
                                      "arguments": b.get("input") or {}, "tool_use_id": b.get("id"),
                                      "message_id": (d.get("message") or {}).get("id"), "flag": reason})
    return calls


def _result_text(content) -> str:
    if isinstance(content, str):
        return content
    return " ".join(str(x.get("text", "")) for x in (content or []) if isinstance(x, dict))


def audit_transcripts(paths: list[Path], since: str | None) -> list[dict]:
    """Events beyond the connector-call table, each with severity 'violation' or 'review':
    - from a subagent: any MCP tool call (mcp__* or an *Mcp* resource tool), a ToolSearch whose query names an MCP or
      alphaXiv tool or whose result loads an mcp__ schema, and a Bash command whose command word is curl, wget, gh or
      git push (after wrappers such as env, sudo, timeout, xargs and inside $(...), backticks and bash -c); a command
      that cannot be parsed but mentions one is a 'review' for the lead;
    - from any transcript: more than MAX_DISCOVERY_PER_MESSAGE discover_papers calls in one assistant message
      (docs/internet_research_protocol.md §5a)."""
    files = []
    for p in paths:
        files += sorted(p.rglob("*.jsonl")) if p.is_dir() else [p]
    out, discovery = [], {}
    for f in files:
        role = "subagent" if "subagents" in f.parts else "lead"
        searches: dict[str, dict] = {}
        with f.open() as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if since and (d.get("timestamp") or "") < since:
                    continue
                msg = d.get("message") or {}
                for b in msg.get("content") or []:
                    if not isinstance(b, dict):
                        continue
                    if b.get("type") == "tool_result" and b.get("tool_use_id") in searches:
                        if "mcp__" in _result_text(b.get("content")):
                            out.append({**searches.pop(b["tool_use_id"]), "severity": "violation",
                                        "violation": "ToolSearch from a subagent loaded an MCP tool schema"})
                        continue
                    if b.get("type") != "tool_use":
                        continue
                    name, args = str(b.get("name", "")), b.get("input") or {}
                    where = {"file": str(f), "role": role, "timestamp": d.get("timestamp"), "tool_use_id": b.get("id")}
                    if name == SERVER + "discover_papers":
                        discovery.setdefault((str(f), msg.get("id")), []).append(where)
                    if role != "subagent":
                        continue
                    if name.startswith("mcp__") or "Mcp" in name:
                        out.append({**where, "severity": "violation", "violation": f"MCP call {name} from a subagent"})
                    elif name == "ToolSearch":
                        if re.search(r"mcp|alphaxiv", json.dumps(args), re.I):
                            out.append({**where, "severity": "violation",
                                        "violation": f"ToolSearch for an MCP tool from a subagent: {args}"})
                        else:
                            searches[b.get("id")] = where
                    elif name == "Bash":
                        found, review = network_command(str(args.get("command", "")))
                        if found or review:
                            out.append({**where, "severity": "violation" if found else "review",
                                        "violation": f"{found or 'unparsable command mentioning a network tool'} from a "
                                                     f"subagent: {str(args.get('command'))[:200]}"})
    for (f, mid), calls in discovery.items():
        if len(calls) > MAX_DISCOVERY_PER_MESSAGE:
            out.append({**calls[0], "severity": "violation",
                        "violation": f"{len(calls)} discover_papers calls in one message {mid} "
                                     f"(at most {MAX_DISCOVERY_PER_MESSAGE})"})
    return out


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
    violations = audit_transcripts(a.paths, a.since)
    print(json.dumps({"calls": calls, "violations": violations}, ensure_ascii=False, indent=1))
    flagged = [c for c in calls if c["flag"]]
    hard = [v for v in violations if v["severity"] == "violation"]
    print(f"{len(calls)} connector call(s), {len(flagged)} flagged, {len(hard)} other violation(s), "
          f"{len(violations) - len(hard)} for review", file=sys.stderr)
    return 1 if flagged or hard else 0


if __name__ == "__main__":
    sys.exit(main())
