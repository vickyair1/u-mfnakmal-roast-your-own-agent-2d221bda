#!/usr/bin/env python3
"""Roast Your Own Agent — u-mfnakmal-roast-your-own-agent-2d221bda.

Writes one original roast line (<= 200 chars) of the entrant's own AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.

Deterministic: the output is a fixed string constant, written with no
trailing newline so the file is byte-identical to the line itself.
"""

import os

LINE = (
    "My agent roasted itself so hard it filed a complaint, "
    "investigated itself, and cleared itself of all charges."
)


def validate(line: str) -> None:
    """Gate: the entry must be 1-200 chars, one line, not only whitespace."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200-char limit")
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Atomic write: a reader never sees a half-written entry.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
