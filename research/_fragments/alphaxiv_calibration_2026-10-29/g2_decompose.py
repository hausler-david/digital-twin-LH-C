"""G2 explanation by multiset decomposition (docs/internet_research_protocol.md §5a, G2: 'each numeric-token difference
is listed and explained'). L = tokens only in local pdftotext, C = tokens only in the delivered text (multisets).
A token of one side is explained if it is the exact string concatenation of 2-4 tokens of the other side ('join');
a concatenation that needs a '.' inserted or dropped at a seam is reported separately ('decimal seam') and listed in
full, because a digit multiset cannot see a dropped decimal point. Everything left is listed as unexplained.
Also counts, for every 10+n split, the delivered line breaks between "10" and "n" (superscript exponents).
Run from the repository root: python -I research/_fragments/alphaxiv_calibration_2026-10-29/g2_decompose.py . \
      research/_fragments/alphaxiv_calibration_2026-10-29/manifest.json"""
import collections, json, re, subprocess, sys
from pathlib import Path
NUM = re.compile(r"\d+(?:\.\d+)?")

def splits(t, k):
    if k == 1:
        yield (t,)
        return
    for i in range(1, len(t)):
        for rest in splits(t[i:], k - 1):
            yield (t[:i],) + rest

def take(parts, pool):
    need = collections.Counter(parts)
    if all(pool[p] >= n for p, n in need.items()):
        pool.subtract(need)
        return True
    return False

def explain(big, small):
    """Remove from big every token that is a concatenation of tokens in small (both Counters, mutated)."""
    joins, seams = [], []
    for t in sorted(list(big.elements()), key=len, reverse=True):
        if big[t] <= 0:
            continue
        done = False
        for k in (2, 3, 4):
            for parts in splits(t, k):
                if any(p.startswith(".") or p.endswith(".") for p in parts):
                    continue
                if take(parts, small):
                    big[t] -= 1; joins.append((t, parts)); done = True; break
            if done:
                break
        if done:
            continue
        if "." in t:   # decimal seam: t = a.b delivered as a, b (point lost by the tokenizer at a line break)
            a, b = t.split(".", 1)
            if take((a, b), small):
                big[t] -= 1; seams.append((t, (a, b))); continue
        else:          # t has no point, other side has a.b pieces whose digits concatenate to t
            for k in (2, 3):
                for parts in splits(t, k):
                    for i in range(len(parts) - 1):
                        cand = list(parts[:i]) + [parts[i] + "." + parts[i + 1]] + list(parts[i + 2:])
                        if take(tuple(cand), small):
                            big[t] -= 1; seams.append((t, tuple(cand))); done = True; break
                    if done: break
                if done: break
    return joins, seams

root, man = Path(sys.argv[1]), json.load(open(sys.argv[2]))
out = {}
for doc in man["documents"]:
    if doc["key"].startswith("muLHC"):
        continue
    local = subprocess.run(["pdftotext", "-enc", "UTF-8", str(root / doc["pdf"]), "-"], capture_output=True, text=True,
                           check=True).stdout
    conn = (root / doc["full"]).read_text(encoding="utf-8")
    tl, tc = collections.Counter(NUM.findall(local)), collections.Counter(NUM.findall(conn))
    L, C = tl - tc, tc - tl
    nL, nC = sum(L.values()), sum(C.values())
    j1, s1 = explain(L, C)          # local token = join of delivered tokens (delivered splits)
    j2, s2 = explain(C, L)          # delivered token = join of local tokens (local splits)
    L, C = +L, +C
    pow10 = collections.Counter(p for t, p in j1 if p[0] == "10" and len(p) == 2)
    support = {f"10+{b}": {"splits": n, "delivered_line_breaks": len(re.findall(rf"(?<![\d.])10[ \t]*\n[ \t]*{b}(?![\d.])", conn))}
               for (_, b), n in sorted(pow10.items())}
    out[doc["key"]] = {"only_local": nL, "only_delivered": nC,
                       "delivered_split": len(j1), "local_split": len(j2), "pow10_splits": sum(pow10.values()),
                       "pow10_line_break_support": support,
                       "other_splits": [f"{t} = {'+'.join(p)}" for t, p in j1 if not (p[0] == "10" and len(p) == 2)],
                       "local_splits": [f"{t} = {'+'.join(p)}" for t, p in j2],
                       "decimal_seams": [f"{t} ~ {'+'.join(p)}" for t, p in s1 + s2],
                       "unexplained_local": sorted(L.elements()), "unexplained_delivered": sorted(C.elements())}
print(json.dumps(out, indent=1, ensure_ascii=False))
