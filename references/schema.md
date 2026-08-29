# Corpus schema

Use only the blocks that the source page actually contains. Preserve their source order beneath the original chapter and section headers.

## Identifiers

`TYPE-PAGE-ITEM`

- `TYPE`: `DEF`, `FIG`, `THM`, or `PRF`.
- `PAGE`: zero-padded printed page number, normally three digits.
- `ITEM`: original figure/theorem number when present; otherwise a two-digit within-page ordinal.

Examples: `DEF-P011-01`, `FIG-P012-05`, `THM-P023-01`, `PRF-P023-01`.

## Markdown blocks

### Definition

```markdown
### DEF-P011-01 — Function

A function $f$ assigns each $x\in D$ exactly one value $f(x)\in E$.

$$
f:D\to E,\qquad x\mapsto f(x)
$$
```

Do not add an equivalent symbolic formulation unless it is visible in the source or is labeled **Derived abstraction**.

### Abstract formula

Place an unnumbered formula directly beneath its governing header or item. State necessary conditions immediately before it.

```markdown
For $h\ne0$,

$$
\frac{f(a+h)-f(a)}{h}
$$
```

### Theorem and proof

```markdown
### THM-P023-01 — Theorem title

**Assumptions:** ...

**Statement:** ...

### PRF-P023-01 — Proof

1. ...
2. ...
3. Therefore, ...
```

Retain every logically necessary step. Algebra may be compacted only when the omitted manipulation is genuinely mechanical and the implication remains auditable.

### Figure

```markdown
### FIG-P012-05 — Domain and Range

![Domain and range shown on the coordinate axes](fig-p012-05.png)
```

Use a filename derived from the permanent ID. Keep the original textbook caption or figure number in the heading when useful.

### Derived content

```markdown
> **Derived abstraction:** ...

> **Connection:** ...
```

Never blend derived or external content into source transcription.

## Compactness

- Prefer formulas to explanatory restatement.
- Use one sentence for a definition when precision permits.
- Do not summarize a proof so aggressively that its logical mechanism disappears.
- Do not create empty headings or categories.
