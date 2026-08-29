#!/usr/bin/env python3
"""Validate structural invariants of a math-textbook corpus Markdown file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ID_RE = re.compile(r"^#{1,6}\s+((?:DEF|FIG|THM|PRF)-P\d{3,5}-[A-Za-z0-9]+)\b", re.MULTILINE)
FIG_RE = re.compile(r"^#{1,6}\s+(FIG-P\d{3,5}-[A-Za-z0-9]+)\b", re.MULTILINE)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)


def section_after(text: str, start: int) -> str:
    next_heading = HEADING_RE.search(text, start)
    return text[start : next_heading.start() if next_heading else len(text)]


def validate(markdown: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not markdown.is_file():
        return [f"Markdown file not found: {markdown}"], warnings

    text = markdown.read_text(encoding="utf-8")
    ids = ID_RE.findall(text)
    duplicates = sorted({item_id for item_id in ids if ids.count(item_id) > 1})
    if duplicates:
        errors.append("Duplicate permanent IDs: " + ", ".join(duplicates))

    if text.count("$$") % 2:
        errors.append("Unbalanced display-math delimiter: odd number of '$$' markers")

    for match in IMAGE_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if target.startswith(("http://", "https://", "data:", "sandbox:")):
            continue
        image_path = (markdown.parent / target).resolve()
        if not image_path.is_file():
            errors.append(f"Missing figure asset: {target}")

    for match in FIG_RE.finditer(text):
        section = section_after(text, match.end())
        if not IMAGE_RE.search(section):
            errors.append(f"Figure heading has no image before the next heading: {match.group(1)}")

    legacy_figures = re.findall(r"^#{1,6}\s+Figure\s+\d+\b", text, re.MULTILINE | re.IGNORECASE)
    if legacy_figures:
        warnings.append(f"Found {len(legacy_figures)} unnumbered legacy figure heading(s)")

    if "[uncertain:" in text.lower():
        warnings.append("Corpus contains explicitly uncertain transcription; review before finalizing")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path, help="Corpus Markdown file")
    args = parser.parse_args()

    errors, warnings = validate(args.markdown)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
