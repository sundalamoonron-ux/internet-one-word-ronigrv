#!/usr/bin/env python3
"""The Internet in One Word — entry program.

Writes a single word describing the whole internet to /output/entry.txt.
Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 30
characters, not only white space.
"""

import os

WORD = "doomscroll"


def main() -> None:
    word = WORD.strip()
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word, "word must not be empty"
    assert " " not in word and "\n" not in word, "entry must be a single word"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    # Read-back verification: the file must hold exactly the word, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == word, "entry.txt does not match the word"
    assert 1 <= len(written) <= 30, "entry.txt outside the 1-30 character gate"
    print(f"Wrote {len(written)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
