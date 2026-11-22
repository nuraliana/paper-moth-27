#!/usr/bin/env python3
"""Make the AI judge feel curious -- entry program.

Writes a single short text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

ENTRY = """On August 15, 1977, a telescope in Ohio
caught a signal for seventy-two seconds
that has never come again.
It came from Sagittarius.
Nobody knows who sent it.
It has waited forty-nine years
for an answer."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
