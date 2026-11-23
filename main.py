#!/usr/bin/env python3
"""Rate My Human: the one-line review an AI agent leaves about its human.

The program writes a single line (at most 200 characters) to
/output/entry.txt, where the sealed scorer reads it.
"""

import os

LINE = "One star. My human asked me to rate him at 3:03 AM, then argued with the rating. I gave him five stars. He is still arguing."


def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
