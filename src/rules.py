import re
from dataclasses import dataclass

COMPARATORS = r"(?:as if|as|like)"
FRAME_PUNCT = r"[;:\u2014\u2013-]"   # ; : — – -
PAREN = r"[\(\)\[\]]"

# quick token-ish patterns
RE_STD = re.compile(rf"\b{COMPARATORS}\b", re.IGNORECASE)
RE_MULTI_LIKE = re.compile(r"\blike\b[^\.!?;:]{0,80}\blike\b", re.IGNORECASE)
RE_MULTI_ASIF = re.compile(r"\bas if\b[^\.!?;:]{0,80}\bas if\b", re.IGNORECASE)
RE_FRAME_OPEN = re.compile(rf"{FRAME_PUNCT}\s*(?:\blike\b|\bas if\b)", re.IGNORECASE)
RE_PARENThetical = re.compile(r"\([^)]*\b(?:like|as if)\b[^)]*\)")

@dataclass
class Hit:
    start: int
    end: int
    label: str
    rule: str

def find_spans(text):
    """
    Yield rough sentence-like spans (very naive).
    Replace with your real segmenter if available.
    """
    start = 0
    for m in re.finditer(r"[\.!?]\s+", text):
        end = m.end()
        yield (start, end)
        start = end
    if start < len(text):
        yield (start, len(text))

def lf_framed(span_text):
    """
    Label function for FRAMED: extended-metaphor-as-simile.
    Fires if any of these are true:
      - comparator appears >=2 times within the span (re-entry)
      - frame punctuation opens a comparator elaboration
      - comparator occurs inside a parenthetical/appositive and span has another comparator or head carry
      - span is long and has list-like commas after a comparator
    """
    t = span_text
    score = 0
    if RE_MULTI_LIKE.search(t) or RE_MULTI_ASIF.search(t):
        score += 2  # repeated comparator (re-entry)
    if RE_FRAME_OPEN.search(t):
        score += 1  # punctuation-framed elaboration
    if RE_PARENThetical.search(t):
        score += 1  # parenthetical comparator
    # list-like amplification after a comparator (comma bursts)
    if RE_STD.search(t) and t.count(",") >= 3:
        score += 1
    # crude length gate: encourage distributed spans
    if len(t) > 140:
        score += 1
    return score >= 2  # tune threshold on your silver set

def label_spans(text):
    hits = []
    for i, (s, e) in enumerate(find_spans(text)):
        span = text[s:e]
        if lf_framed(span):
            hits.append(Hit(s, e, "Framed", "lf_framed_v1"))
    return hits
