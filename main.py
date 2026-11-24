#!/usr/bin/env python3
"""Entry for make.fun bounty: The Worst App Idea Ever Pitched.

Writes one sentence (<= 240 characters) pitching the worst, most
useless app idea imaginable to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic, stdlib only, no network.
"""
import os

ENTRY = (
    "ParkPal uses AI to find and reserve the farthest parking spot from "
    "every entrance, so your 10,000 steps start before you even leave "
    "the car \u2014 walking is the feature, convenience was the bug."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
