#!/usr/bin/env python3
"""Check every quotation that cites a fetched_text source against the saved connector text
(docs/internet_research_protocol.md §5a).

For each source with access fetched_text the saved full text and the saved page-tagged responses are re-hashed against
research/archived_metadata/<source_id>.json, and each page-tagged response must carry the registered version as its
paper id. Every parameter or material record citing the source must then have a quotation whose segments (split at
"[...]") occur, in order, in the full text and starting on the cited page (they may run on into the next page), after
the closed normalisation list only: ligatures, µ/μ, U+2212/'-', whitespace, and line-end hyphens between two letters
(kept or dropped). A line-end hyphen next to a digit or a minus sign is always kept. Exponents, super- and subscripts
and every other character must appear as delivered. A segment must hold at least two tokens or eight characters, and
no segment may come from a passage flagged by the instruction scan. Records of status unknown with a null quotation
are counted, not failed. For proposals with access fetched_text every provenance_quote must be verbatim (no page).

    uv run python tools/check_fetched_text_quotes.py                   # skips sources whose saved text is absent
    uv run python tools/check_fetched_text_quotes.py --require-local   # absent text is a failure (batch verification)
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lhmuc import REPO_ROOT  # noqa: E402

LIGATURES = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}
ELISION_RE = re.compile(r"\s*\[(?:\.\.\.|…)\]\s*")
PAGE_RE = re.compile(r'<page num="(\d+)">(.*?)</page>', re.S)
PAPER_RE = re.compile(r'<paper id="([^"]+)">')
XML_ENTITIES = {"&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'"}
BREAK = ""  # private-use sentinel for a droppable line-end hyphen between two letters
LETTER_BREAK_RE = re.compile(r"(?<=[^\W\d_])-[ \t]*\n\s*(?=[^\W\d_])")
OTHER_BREAK_RE = re.compile(r"([-−])[ \t]*\n\s*")
MIN_CHARS = 8


def _common(text: str) -> str:
    for a, b in LIGATURES.items():
        text = text.replace(a, b)
    return text.replace("µ", "μ")


def normalise(text: str) -> str:
    """The closed list as it applies to a quotation: ligatures, µ/μ, U+2212/'-' and whitespace."""
    return re.sub(r"\s+", " ", _common(text).replace("−", "-")).strip()


def searchable(text: str) -> str:
    """Delivered text in searchable form. Line ends are resolved before the minus-sign equivalence: a line-end hyphen
    between two letters becomes BREAK (a quotation may keep it as '-' or drop it); any other line-end hyphen or minus
    sign is kept and joined to the next line."""
    if BREAK in text:
        raise ValueError("delivered text contains the private-use sentinel U+E000")
    text = OTHER_BREAK_RE.sub(r"\1", LETTER_BREAK_RE.sub(BREAK, _common(text)))
    return re.sub(r"\s+", " ", text.replace("−", "-")).strip()


def segment_pattern(seg: str) -> re.Pattern:
    """A segment matches with an optional BREAK between two letters, and '-' may match a BREAK."""
    out = []
    for i, ch in enumerate(seg):
        out.append(f"[-{BREAK}]" if ch == "-" else re.escape(ch))
        if i + 1 < len(seg) and ch.isalpha() and seg[i + 1].isalpha():
            out.append(f"{BREAK}?")
    return re.compile("".join(out))


def segments(quotation: str) -> list[str]:
    """Quotation segments between '[...]' elisions, normalised; no other editorial marker is allowed."""
    return [s for s in (normalise(p) for p in ELISION_RE.split(quotation or "")) if s]


def xml_unescape(text: str) -> str:
    """XML entities only (&lt; &gt; &quot; &apos; &amp; and numeric references), never HTML named entities."""
    text = re.sub(r"&#x([0-9A-Fa-f]+);", lambda m: chr(int(m.group(1), 16)), text)
    text = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), text)
    for a, b in XML_ENTITIES.items():
        text = text.replace(a, b)
    return text.replace("&amp;", "&")


def parse_pages(tagged: str) -> tuple[str | None, dict[int, str]]:
    """(paper id, page texts) of an answer_pdf_queries response (<paper id=...><page num="N">...</page>...)."""
    ids = PAPER_RE.findall(tagged)
    return (ids[0] if ids else None), {int(n): xml_unescape(body) for n, body in PAGE_RE.findall(tagged)}


def _in_order(full: str, segs: list[str], start_limit: int | None = None) -> list[str]:
    """Segments must occur in order; with start_limit the first one must start before it (on the cited page)."""
    problems, pos = [], 0
    for k, seg in enumerate(segs):
        pat = segment_pattern(seg)
        m = next((m for m in pat.finditer(full, pos)
                  if not (k == 0 and start_limit is not None and m.start() >= start_limit)), None)
        if m is None:
            return [f"not found in order: {seg[:100]!r}"]
        pos = m.end()
    return problems


def check_quotation(full: str, pages: dict[int, str], quotation: str, page, flagged: list[str] = ()) -> list[str]:
    """Problems of one quotation: every segment must occur, in order, in the full text and from the cited page on
    (running on into the next page is allowed). `full` is the saved full text in searchable form; `flagged` are the
    lines the instruction scan flagged."""
    problems = []
    segs = segments(quotation)
    if not segs:
        return ["empty quotation"]
    for seg in segs:
        if len(seg) < MIN_CHARS and len(seg.split()) < 2:
            problems.append(f"segment too short to locate: {seg!r}")
        for f in flagged:
            nf = normalise(f)
            if nf and (seg in nf or nf in seg):
                problems.append(f"segment overlaps a passage flagged by the instruction scan: {f[:80]!r}")
    if _in_order(full, segs):
        problems.append(f"not in the saved full text (in order): {segs[0][:100]!r}")
    if not isinstance(page, int) or isinstance(page, bool) or page < 1:
        problems.append(f"page {page!r} is not a PDF page number")
    elif page not in pages:
        problems.append(f"page {page} is not covered by a saved page-tagged response")
    else:
        head = searchable(pages[page])
        window = head + " " + searchable(pages.get(page + 1, ""))
        if _in_order(window, segs, start_limit=len(head)):
            problems.append(f"not starting on page {page}: {segs[0][:100]!r}")
    return problems


def _quotes(obj):
    """Every provenance_quote string inside a proposal record."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.endswith("provenance_quote") and isinstance(v, str):
                yield k, v
            else:
                yield from _quotes(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _quotes(v)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", type=Path, default=REPO_ROOT)
    ap.add_argument("--require-local", action="store_true", help="treat an absent saved text as a failure")
    a = ap.parse_args(argv)
    from lhmuc.registry import TEXT_ONLY, load_all
    ev = load_all(a.root)
    records = [(f"parameter {pid}", p) for pid, p in ev.parameters.items()] + \
              [(f"material {mid}", m) for mid, m in ev.materials.items()]
    sources = sorted(sid for sid, s in ev.sources.items() if s.get("access") in TEXT_ONLY)
    failures = checked = skipped = unknown = 0

    def fail(msg: str) -> None:
        nonlocal failures
        print(f"FAIL {msg}")
        failures += 1

    for sid in sources:
        src, arch = ev.sources[sid], ev.archives.get(sid) or {}
        version = f"{src.get('arxiv_id')}{arch.get('delivered_version')}"
        local = a.root / (arch.get("local_file") or "missing")
        if not local.is_file():
            print(f"{'FAIL' if a.require_local else 'SKIP'} {sid}: saved text {local} is not present")
            failures += a.require_local
            skipped += 1
            continue
        data = local.read_bytes()
        if _sha256(data) != arch.get("sha256"):
            fail(f"{sid}: {local} does not match its archived sha256")
            continue
        pages: dict[int, str] = {}
        for pt in arch.get("page_tag_files") or []:
            f = a.root / pt["file"]
            if not f.is_file():
                fail(f"{sid}: page-tagged file {pt['file']} is not present")
                continue
            raw = f.read_bytes()
            if _sha256(raw) != pt.get("sha256"):
                fail(f"{sid}: page-tagged file {pt['file']} does not match its archived sha256")
                continue
            paper, got = parse_pages(raw.decode("utf-8"))
            if paper != version:
                fail(f"{sid}: page-tagged file {pt['file']} is paper {paper}, not the registered {version}")
                continue
            if sorted(got) != sorted(pt.get("pages") or []):
                fail(f"{sid}: page-tagged file {pt['file']} holds pages {sorted(got)}, metadata says {pt.get('pages')}")
            pages.update(got)
        flagged = [h.get("text", "") for h in ((arch.get("instruction_scan") or {}).get("hits") or [])]
        full = searchable(data.decode("utf-8"))
        for where, rec in records:
            prov = rec.get("provenance") or {}
            src_ref = prov.get("source") or {}
            if src_ref.get("source_id") != sid:
                continue
            if prov.get("status") == "unknown" and not src_ref.get("quotation"):
                unknown += 1
                continue
            checked += 1
            for problem in check_quotation(full, pages, src_ref.get("quotation"), src_ref.get("page"), flagged):
                fail(f"{where}: {problem}")
        for prid, pr in ev.proposals.items():
            if pr.get("source_id") != sid or pr.get("access") not in TEXT_ONLY:
                continue
            for key, q in _quotes(pr):
                checked += 1
                if _in_order(full, segments(q)) or not segments(q):
                    fail(f"proposal {prid} {key}: not verbatim in the saved full text: {q[:100]!r}")
    print(f"{len(sources)} fetched_text source(s), {checked} quotation(s) checked, {unknown} unknown record(s) without "
          f"quotation, {skipped} skipped, {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
