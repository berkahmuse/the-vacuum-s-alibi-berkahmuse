#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters — @berkahmuse entry.

Writes one deadpan excuse from a robot vacuum to /output/entry.txt.
No network, no randomness, no input: every run writes the same bytes.
"""

import os

ENTRY = (
    "I did not miss that spot. The dust there unionized, "
    "and my contract forbids crossing a picket line."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY, "entry must fit on one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
