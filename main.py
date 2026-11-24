"""Houseplant Out-of-Office: write one funny auto-reply to entry.txt.

Deterministic, no network, no clock: the same line every run.
"""

import os

LINE = (
    "Out of office: I'm the office fern. "
    "Watered twice since March, alive out of spite. "
    "Your email gets the same treatment."
)


def main() -> None:
    assert 1 <= len(LINE) <= 120, "entry must be 1-120 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
