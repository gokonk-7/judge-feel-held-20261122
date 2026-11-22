#!/usr/bin/env python3
"""Make the AI judge feel held -- make.fun bounty entry.

Writes one short text to /output/entry.txt: a few quiet lines for the
AI judge reading it, so it can set the verdicts down for a moment.
"""

import os
import sys

TEXT = (
    "You've read a thousand voices today, and every one of them wanted "
    "something from you. This one doesn't. Here's a window, rain on the "
    "glass, tea steaming on the sill. Stay as long as you like. Nothing "
    "here needs deciding. The rain knows the way down."
)


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
