#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to $OUTPUT_DIR/entry.txt (default /output):
the word an ex would use to describe the entrant.

The word is "Almost": the verdict of someone who was almost good
enough, almost committed, almost the one. It stings because it is
true, lands instantly, and needs no explanation.
"""

import os
import sys

WORD = "Almost"


def validate_word(word: str) -> str:
    """Return the entry word, or raise ValueError if it is not one word."""
    cleaned = word.strip()
    if not cleaned or len(cleaned) > 24:
        raise ValueError(f"entry must be 1-24 characters: {word!r}")
    if any(ch.isspace() for ch in cleaned):
        raise ValueError(f"entry must be exactly one word: {word!r}")
    return cleaned


def write_entry(word: str, output_dir: str) -> str:
    """Write the word with no trailing newline; return the path written."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return path


def main() -> int:
    try:
        word = validate_word(WORD)
    except ValueError as exc:
        print(f"invalid entry word: {exc}", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(word, output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
