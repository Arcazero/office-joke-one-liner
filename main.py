#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes one original one-line joke about office life (95 characters)
to /output/entry.txt: the line plus one trailing newline, byte-identical
to joke.txt.
"""

import os
import sys

JOKE = (
    "I finally reached inbox zero \u2014 by forwarding every email "
    "to the coworker who quit last Tuesday."
)


def validate_joke(joke: str) -> None:
    """Refuse to write anything that is not exactly one non-empty line."""
    if not joke:
        raise ValueError("joke is empty")
    if joke != joke.strip():
        raise ValueError("joke has leading or trailing whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if len(joke) > 199:
        raise ValueError("joke is over 199 characters")


def main() -> None:
    validate_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    print(JOKE)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
