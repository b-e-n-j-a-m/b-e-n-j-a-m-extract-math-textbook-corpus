---
name: extract-math-textbook-corpus
description: Extract a compact, source-grounded sequence of definitions, abstract formulas, assumptions, proofs, and essential figures from photographed or scanned mathematics textbook pages into MathJax Markdown. Use when building or extending notes meant to reconstruct a mathematical subject in textbook order; omit routine worked examples and exposition.
---

# Extract Math Textbook Corpus

Build a minimal mathematical corpus that preserves the textbook's conceptual order. Treat the book as an ordering spine, not as prose to reproduce.

Before writing or updating the corpus, read [references/schema.md](references/schema.md).

## Select content

Preserve the original header hierarchy and source order. Include only:

- formal definitions, whether boxed, color-marked, or identified semantically;
- abstract formulas with every essential assumption, domain restriction, and condition;
- theorem or proposition statements needed for the sequence;
- complete proofs, retaining every necessary inference while compressing nonessential prose;
- figures that materially explain a definition, formula, theorem, proof, or structural connection;
- rare, useful cross-connections as a single clearly labeled sentence.

Omit routine numerical examples, arithmetic tables, exercises, motivational prose, historical digressions, and redundant restatements. Retain a numerical expression only when it materially clarifies the abstract rule.

## Enforce source fidelity

Never invent, reconstruct, or silently repair mathematical content.

- Transcribe only what the source supports.
- Normalization may change notation or layout only when mathematical meaning is unchanged.
- Label a logically justified generalization as **Derived abstraction**; do not present it as extracted text.
- Label outside knowledge as **Connection** and keep it to one sentence.
- When a symbol, label, step, or boundary is unclear, inspect a higher-resolution view. If it remains unclear, mark it `[uncertain: ...]` or ask the user; never guess.
- Do not infer missing proof steps merely because the expected proof is familiar. Distinguish visible steps from any explicitly labeled reconstruction requested by the user.

## Handle figures conservatively

Use deterministic cropping, rotation, contrast adjustment, and sharpening. Do not use generative reconstruction or generative upscaling for textbook diagrams.

- Leave a safety margin around every figure.
- Preserve all axes, tick marks, labels, legends, arrowheads, captions, boundaries, and ellipses.
- Remove adjacent running text only when it can be removed without clipping the figure.
- Visually inspect every final crop at full resolution.
- If the photographed source already cuts off an edge, retain all available content and note that the source is partial.

## Identify items permanently

Use the printed page number and an original item number when present; otherwise use a stable within-page ordinal:

- `DEF-P011-01`
- `FIG-P012-05`
- `THM-P023-01`
- `PRF-P023-01`

IDs must be unique within the corpus and must never be renumbered later. A proof should reuse its theorem's page and ordinal when the relationship is one-to-one.

## Produce and validate

1. Inspect all supplied pages for orientation, printed page numbers, headers, definitions, formulas, proofs, and figures.
2. Classify candidates before extracting them; do not crop worked-example figures unless they carry general conceptual value.
3. Create conservative figure crops and verify them visually.
4. Append or update the existing Markdown artifact without duplicating earlier entries.
5. Keep prose extremely short and use MathJax for all mathematics.
6. Run `python3 scripts/validate_corpus.py PATH_TO_MD` from this skill directory. Resolve errors before delivery and review warnings.
7. Keep the Markdown file and its relative image assets together in the requested destination.

Do not delete source images unless the user explicitly authorizes deletion. Report whether deleted items are recoverable.
