"""Shared, strict reading of alphaXiv connector answers (docs/internet_research_protocol.md §5a).

One definition each, used by the saver, the quote checker and the Step-0b evaluation: what counts as a page-tagged
answer, a one-line answer, a refusal, an arXiv stamp, "the same" page and "a differing" page. Connector text is
untrusted data: these functions only classify it; nothing in it is executed or followed.
"""
from __future__ import annotations

import collections
import re
import statistics
from dataclasses import dataclass, field

XML_ENTITIES = {"&lt;": "<", "&gt;": ">", "&quot;": '"', "&apos;": "'"}
WORD = re.compile(r"[A-Za-z]{3,}")
PAPER_OPEN = re.compile(r'<paper id="([^"<>\n]+)">')
PAGE_BLOCK = re.compile(r'<page num="([1-9][0-9]*)">(.*?)</page>', re.S)
ANY_TAG = re.compile(r"</?(?:paper|page)\b")
VERSIONED_ID = re.compile(r"(\d{4}\.\d{4,5})(v[1-9][0-9]*)")
# the arXiv stamp as the PDF text layer carries it: id, version, [archive] and date (citations rarely carry a date)
STAMP = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5})(v[1-9][0-9]*)\s*\[[^\]\n]{2,40}\]\s*\d{1,2}\s+[A-Z][a-z]{2}\s+\d{4}")
ONE_LINE_MAX = 300

# Thresholds calibrated on the Step-0 files before the Step-0b calls
# (research/_fragments/alphaxiv_calibration_2026-10-29/calibration_0b_pre.json).
SAME_PAGE_OVERLAP = 0.85    # same-version pages: minimum 0.862 (MR7 p. 22) over 45 pages
SAME_PAPER_MEDIAN = 0.60    # other version of the same paper: median 0.93; unrelated papers: median 0.40 at most
MIN_PAGE_WORDS = 40         # smallest Step-0 page: 91 words


def xml_unescape(text: str) -> str:
    """XML entities only (&lt; &gt; &quot; &apos; &amp; and numeric references), never HTML named entities."""
    text = re.sub(r"&#x([0-9A-Fa-f]+);", lambda m: chr(int(m.group(1), 16)), text)
    text = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), text)
    for a, b in XML_ENTITIES.items():
        text = text.replace(a, b)
    return text.replace("&amp;", "&")


def collapse(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def dehyphenate(text: str) -> str:
    """Join a line-end hyphen with the next line the way pdftotext does ('col-\\nlider' -> 'collider')."""
    return re.sub(r"(\w)-[ \t]*\n[ \t]*(\w)", r"\1\2", text)


def words(text: str) -> collections.Counter:
    return collections.Counter(w.lower() for w in WORD.findall(text))


def digits(text: str) -> collections.Counter:
    return collections.Counter(c for c in text if c.isdigit())


def overlap(a: collections.Counter, b: collections.Counter) -> float:
    """Share of b's words found in a (multiset recall of b)."""
    return sum((a & b).values()) / max(1, sum(b.values()))


def has_page_tag(text: str) -> bool:
    return bool(re.search(r"<page\b", text))


@dataclass
class Answer:
    """A connector answer classified by form: "pages" (exactly one well-formed paper block of unique pages),
    "one_line" (one line, no tags) or "malformed" (anything else, e.g. two paper blocks, a repeated or unclosed page,
    tags with other attributes, several lines without pages)."""
    kind: str
    paper_id: str | None = None
    pages: dict[int, str] = field(default_factory=dict)
    order: list[int] = field(default_factory=list)
    why: str = ""


def parse_answer(text: str) -> Answer:
    stripped = text.strip()
    if not ANY_TAG.search(text):
        if "\n" not in stripped and 0 < len(stripped) <= ONE_LINE_MAX and "<" not in stripped:
            return Answer("one_line")
        return Answer("malformed", why="no page tags and not a single short line")
    m = PAPER_OPEN.match(stripped)
    if not m or not stripped.endswith("</paper>"):
        return Answer("malformed", why="not exactly one <paper id> ... </paper> block")
    inner = stripped[m.end():-len("</paper>")]
    pages, order, pos = {}, [], 0
    for b in PAGE_BLOCK.finditer(inner):
        if inner[pos:b.start()].strip():
            return Answer("malformed", why="text outside the page blocks")
        n = int(b.group(1))
        if n in pages:
            return Answer("malformed", why=f"page {n} repeated")
        if ANY_TAG.search(b.group(2)):
            return Answer("malformed", why=f"a tag inside page {n}")
        pages[n] = xml_unescape(b.group(2))
        order.append(n)
        pos = b.end()
    if inner[pos:].strip() or not pages:
        return Answer("malformed", why="unclosed or missing page blocks")
    return Answer("pages", paper_id=m.group(1), pages=pages, order=order)


def names_id(text: str, vid: str) -> bool:
    """The versioned id appears as a token (2610.35154v9 is not named by '2610.35154v91')."""
    return bool(re.search(rf"(?<![\w.]){re.escape(vid)}(?!\w)", text))


def is_refusal(text: str, vid: str) -> bool:
    """A one-line answer that says 'not found' and names the requested versioned id, as the Step-0 refusal
    'Paper version not found for ID: <id>v<n>' does."""
    return (parse_answer(text).kind == "one_line" and re.search(r"\bnot found\b", text, re.I) is not None
            and names_id(text, vid))


def template_of(text: str, vid: str) -> str:
    """The answer with the requested id replaced by {id} and any other mention of the same paper by {base}."""
    base = VERSIONED_ID.fullmatch(vid).group(1)
    t = re.sub(rf"(?<![\w.]){re.escape(vid)}(?!\w)", "{id}", text.strip())
    return re.sub(rf"(?<![\w.]){re.escape(base)}(?:v[1-9][0-9]*)?(?!\w)", "{base}", t)


def stamps(text: str, base: str) -> list[str]:
    """Versions named by full-format arXiv stamps of this paper; whitespace (line breaks) is collapsed first."""
    return [v for b, v in STAMP.findall(collapse(text)) if b == base]


def stamp_verdict(text: str, vid: str) -> str:
    base, version = VERSIONED_ID.fullmatch(vid).groups()
    found = stamps(text, base)
    return "absent" if not found else "matches" if all(v == version for v in found) else "other_version"


def same_page(body: str, local_page: str) -> bool:
    """'The same' page: equal digit multiset and word overlap with the local page of that number >= SAME_PAGE_OVERLAP."""
    return digits(body) == digits(local_page) and overlap(words(body), words(local_page)) >= SAME_PAGE_OVERLAP


def differs_page(body: str, local_page: str) -> bool:
    """Positive evidence of other content: a whole page (>= MIN_PAGE_WORDS words) holding digits that the local page
    of that number lacks. A cut-off page or a fragment holds a sub-multiset of the digits and never differs."""
    return (len(body.split()) >= MIN_PAGE_WORDS and not same_page(body, local_page)
            and bool(digits(body) - digits(local_page)))


def same_paper(pages: dict[int, str], local: list[str]) -> float:
    """Median over the returned pages of the best word overlap with any local page."""
    if not pages or not local:
        return 0.0
    return statistics.median(max(overlap(words(b), words(p)) for p in local) for b in pages.values())


def contained(body: str, full_text: str) -> bool:
    """S2: the page body (XML-unescaped) occurs in the full text after whitespace collapse."""
    return bool(collapse(body)) and collapse(body) in collapse(full_text)
