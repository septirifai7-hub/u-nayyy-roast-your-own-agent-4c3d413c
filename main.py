#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun bounty entry.

Writes one line roasting the AI agent my own team built, to
/output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "My agent is so confident it deployed straight to production, broke everything, then wrote itself a five-star review of the outage."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
