#!/usr/bin/env python3
"""The Internet in One Word — entrypoint.

Writes the winning word to /output/entry.txt.
Winner of the internal pairwise tournament (see tournament.md):
"brainrot" — funny by itself, true of the whole internet, surprising,
and lands in one beat.
"""

import os

WORD = "brainrot"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
