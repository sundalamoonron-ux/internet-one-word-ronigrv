#!/usr/bin/env python3
"""The Internet in One Word — entrypoint.

Writes the winning word to /output/entry.txt.
Winner of the internal pairwise tournament (see tournament.md):
"brainrot" — funny by itself, true of the whole internet, surprising,
and lands in one beat.
"""

import os

WORD = "brainrot"


def validate_word(word: str) -> str:
    """Gate: the entry must be exactly one word, 1-30 characters.

    Rejects empty input, whitespace inside the word, and anything longer
    than the competition's one-word limit, before anything is written.
    """
    if not word:
        raise ValueError("WORD must not be empty")
    if len(word) > 30:
        raise ValueError(f"WORD must be 1-30 characters, got {len(word)}")
    if any(ch.isspace() for ch in word):
        raise ValueError(f"WORD must be a single word without spaces, got {word!r}")
    return word


def main() -> None:
    word = validate_word(WORD)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
