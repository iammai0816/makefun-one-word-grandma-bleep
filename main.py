#!/usr/bin/env python3
"""Write the one word grandma would text about AI.

The program is deterministic: it always emits the same single word,
the word itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

WORD = "Bleep"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
