#!/usr/bin/env python3
"""Office joke entry for make.fun.

Writes a single office joke, one line under 200 characters, to
/output/entry.txt. The grader reads that file.
"""

import os

JOKE = (
    "My boss told me to dress for the job I want, so today I came in "
    "as the office printer: jammed, out of toner, and somehow still essential."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

OFFICE_WORDS = ("boss", "office", "printer", "meeting", "email", "desk")


def check_office_flavour(text: str) -> None:
    """Make sure the line is actually about office life and has a turn.

    A one-line office joke needs a setup and a payoff: here the colon
    separates the setup (dress for the job you want) from the payoff
    (being the printer). It also has to name something from the office.
    """
    assert ":" in text, "the joke needs a colon turn between setup and payoff"
    lowered = text.lower()
    assert any(word in lowered for word in OFFICE_WORDS), (
        "the joke must mention something from office life"
    )


def main() -> None:
    lines = JOKE.splitlines()
    assert len(lines) == 1, "the joke must be exactly one line"
    assert len(JOKE) < MAX_CHARS, f"joke is {len(JOKE)} chars, limit is {MAX_CHARS}"
    assert JOKE.strip(), "the joke must not be blank"
    check_office_flavour(JOKE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")

    print(f"wrote {len(JOKE)}-character joke to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
