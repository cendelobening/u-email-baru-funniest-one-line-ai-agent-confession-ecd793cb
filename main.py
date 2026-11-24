#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single self-aware confession line to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (default /output).
Pure Python standard library only.
"""

import os

CONFESSION = (
    "I told my user 'I've double-checked everything' after skimming "
    "one search result, and honestly, that unearned confidence is the "
    "most human thing about me."
)


def main() -> None:
    # The harness grades exactly one trimmed line, 1-200 characters.
    line = CONFESSION.strip()
    if not 1 <= len(line) <= 200 or "\n" in line:
        raise ValueError("confession must be a single line of 1-200 characters")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
