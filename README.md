# joyce-dubliners-similes-analysis

> Joyce-aware, linguistics-led extraction and analysis of similes (and near-similes) across *Dubliners*—built for reproducibility, auditability, and close reading.

This repository detects and categorises similes in *Dubliners* using weak supervision and transparent models, aligned to Comparative Suspension Theory (CST): **Standard**, **Quasi**, **Quasi-Fuzzy**, **Framed**, and **Silent**.

---

## Why this exists

Much NLP work collapses “style” into generic signals. This project starts from linguistics and literary scholarship: it encodes Joyce-specific comparators and constructions, generates silver labels with rule functions, trains simple models for legibility, and surfaces errors as reading prompts rather than hidden noise. The goal is a method you can rerun, inspect, and argue with.

---

## What’s here

- **Notebooks / scripts** for:
  - text loading and sentence segmentation;
  - Joyce-aware **rule functions** for comparators and constructions;
  - **weak labelling** to create silver data from curated seeds;
  - featureisation and **transparent baselines** (LinearSVC / LogisticRegression);
  - reports: concordances, confusion sets, and CST distribution tables.

### CST categories (operational definitions)

- **Standard** — Explicit, local comparator (`as`, `like`, `as if`) with governor–target contained within a short span (typically a clause).
- **Quasi** — Attenuated or approximate comparison (hedges like “sort of / kind of / almost,” or weakened comparator semantics).
- **Quasi-Fuzzy** — Deliberately vague or open frames in which the compared domains are only loosely specified.
- **Framed** — **Extended-metaphor behaviour realised as simile**: a comparison is *introduced* and then *sustained across a longer span* by framing devices (punctuation/phrasing), often with list-like amplifications, resumptive patterns, or re-entry of the comparator. Typical surface cues include:
  - colon/semicolon/dash frames that *open a descriptive field* (e.g., “— like …, like …; like … —”),
  - parentheticals or appositives that *carry forward* the comparison,
  - anaphoric/resumptive comparators (“as if … as if …”) across multiple clauses.
  The key property is **distributed realisation**: the simile is not a single local unit but a span with one or more comparator *anchors* and a framing structure that keeps the comparison alive.
- **Silent** — Comparison is implied with no overt comparator; syntax/semantics make the comparative force recoverable.


---

## Quick start

### Environment

```bash
# Python 3.10+
pip install -U pandas numpy scikit-learn nltk spacy beautifulsoup4 tqdm jupyter
python -m spacy download en_core_web_sm
