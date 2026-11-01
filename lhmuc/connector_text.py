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
PAGE_BLOCK = re.compile(r'<page num="([1-9][0-9]{0,5})">(.*?)</page>', re.S)  # longer page numbers are malformed
CHAR_REF = re.compile(r"&#(x[0-9A-Fa-f]+|[0-9]+);")
ANY_TAG = re.compile(r"</?(?:paper|page)\b")
VERSIONED_ID = re.compile(r"(\d{4}\.\d{4,5})(v[1-9][0-9]*)")
# the arXiv stamp as the PDF text layer carries it: id, version, [archive] and date (citations rarely carry a date)
STAMP = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5})(v[1-9][0-9]*)\s*\[[^\]\n]{2,40}\]\s*\d{1,2}\s+[A-Z][a-z]{2}\s+\d{4}")
ONE_LINE_MAX = 300

# Thresholds calibrated on the Step-0 files and the uploaded PDFs before the Step-0b calls; the values they rest on
# are in research/_fragments/alphaxiv_calibration_2026-10-29/calibration_0b_pre.json.
SAME_PAGE_OVERLAP = 0.85    # same-version pages: minimum 0.862 (MR7 p. 22) over 45 pages
SAME_PAPER_MEDIAN = 0.80    # median page window share: same paper 0.991 at least, unrelated papers 0.683 at most
SAME_PAPER_CHUNKS = 0.80    # whole-text chunk score: same paper 1.000, unrelated papers 0.714 at most (both maxima:
                            # Kaya against the muLHC upload, two papers on the same subject)
MIN_PAGE_WORDS = 40         # a page below this is "short": no evidence either way (Step-0 pages: 91 words at least)
CHUNK_WORDS = 150


def _char(n: int, ref: str) -> str:
    return chr(n) if n <= 0x10FFFF else ref  # an out-of-range reference stays as written


def xml_unescape(text: str) -> str:
    """XML entities only (&lt; &gt; &quot; &apos; &amp; and numeric references), never HTML named entities."""
    text = re.sub(r"&#x([0-9A-Fa-f]{1,7});", lambda m: _char(int(m.group(1), 16), m.group(0)), text)
    text = re.sub(r"&#(\d{1,7});", lambda m: _char(int(m.group(1)), m.group(0)), text)  # longer: kept as written
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
        if any(not _valid_ref(r) for r in CHAR_REF.findall(b.group(2))):
            return Answer("malformed", why=f"an out-of-range character reference in page {n}")
        pages[n] = xml_unescape(b.group(2))
        order.append(n)
        pos = b.end()
    if inner[pos:].strip() or not pages:
        return Answer("malformed", why="unclosed or missing page blocks")
    return Answer("pages", paper_id=m.group(1), pages=pages, order=order)


def _valid_ref(ref: str) -> bool:
    """A numeric character reference that names a Unicode code point (at most 7 digits, at most U+10FFFF)."""
    digits_ = ref[1:] if ref.startswith("x") else ref
    if len(digits_) > 7:
        return False
    return int(digits_, 16 if ref.startswith("x") else 10) <= 0x10FFFF


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


def other_paper_stamps(text: str, base: str) -> list[str]:
    """Full-format arXiv stamps of other papers (a page carrying one is a page of another paper)."""
    return [b + v for b, v in STAMP.findall(collapse(text)) if b != base]


def strip_stamps(text: str) -> str:
    """The text without its full-format arXiv stamps (whitespace collapsed)."""
    return STAMP.sub(" ", collapse(text))


def stamp_verdict(text: str, vid: str) -> str:
    base, version = VERSIONED_ID.fullmatch(vid).groups()
    found = stamps(text, base)
    return "absent" if not found else "matches" if all(v == version for v in found) else "other_version"


def short(body: str) -> bool:
    """A page below MIN_PAGE_WORDS words: no evidence either way (listed, never compared)."""
    return len(body.split()) < MIN_PAGE_WORDS


def same_page(body: str, local_page: str) -> bool:
    """'The same' page: equal digit multiset and word overlap with the local page of that number >= SAME_PAGE_OVERLAP."""
    return digits(body) == digits(local_page) and overlap(words(body), words(local_page)) >= SAME_PAGE_OVERLAP


def windows(local: list[str] | tuple[str, ...], n: int | None = None) -> list[str]:
    """Single pages and pairs of consecutive local pages; with n, only those around page n (n-1 to n+1)."""
    idx = range(len(local)) if n is None else [i for i in (n - 2, n - 1, n) if 0 <= i < len(local)]
    out = [local[i] for i in idx]
    out += [local[i] + "\n" + local[i + 1] for i in idx if i + 1 < len(local) and (n is None or i + 1 <= n)]
    return out


def same_as_any(body: str, local: list[str] | tuple[str, ...]) -> bool:
    return any(same_page(body, p) for p in local)


def differs_page(body: str, local: list[str] | tuple[str, ...], n: int) -> bool:
    """Positive evidence of other content at page n: a page of at least MIN_PAGE_WORDS words that is the same as no
    local page and holds digits that no local window around page n (pages n-1 to n+1, singly or as consecutive pairs)
    contains. A cut-off page, a fragment or a page shifted by one is never counted as differing."""
    if short(body) or same_as_any(body, local):
        return False
    d = digits(body)
    return all(d - digits(w) for w in windows(local, n)) if windows(local, n) else bool(d)


def window_share(unit: str, local: list[str] | tuple[str, ...]) -> float:
    """Share of the unit's words found in the best window of one or two consecutive local pages."""
    u = words(unit)
    total = sum(u.values())
    if not total or not local:
        return 0.0
    return max(sum((u & words(w)).values()) for w in windows(local)) / total


def same_paper(pages: dict[int, str], local: list[str] | tuple[str, ...]) -> float | None:
    """Median over the returned pages of at least MIN_PAGE_WORDS words of window_share; None when no page qualifies."""
    scores = [window_share(b, local) for b in pages.values() if not short(b)]
    return statistics.median(scores) if scores else None


def chunk_score(text: str, local: list[str] | tuple[str, ...]) -> float:
    """Whole-text same-paper score: median window_share of consecutive CHUNK_WORDS-word chunks of the text. Unlike a
    whole-text recall it does not depend on the lengths of the two versions."""
    ws = text.split()
    chunks = [" ".join(ws[i:i + CHUNK_WORDS]) for i in range(0, len(ws), CHUNK_WORDS)]
    chunks = [c for c in chunks if len(c.split()) >= MIN_PAGE_WORDS] or chunks
    return statistics.median(window_share(c, local) for c in chunks) if chunks else 0.0


def contained(body: str, full_text: str) -> bool:
    """S2: the page body (XML-unescaped) occurs in the full text after whitespace collapse."""
    return bool(collapse(body)) and collapse(body) in collapse(full_text)
