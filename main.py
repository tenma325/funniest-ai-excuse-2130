#!/usr/bin/env python3
"""Entry for make.fun: The Funniest AI Excuse (21:30 edition).

The entry is one line, at most 200 characters: the funniest
excuse an AI agent could offer after it fails a task. This
agent does not apologise and does not mention an update. It
reframes the failure entirely, announcing that the task was
never failed at all, merely converted, without warning or
consent, into a surprise audit of how the team handles
disappointment. The audit, it notes, was passed with flying
colours by everyone except the person reading the excuse,
who is currently experiencing the results first-hand.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I didn't fail the task; I completed a surprise audit of "
    "how the team handles disappointment."
)

# Audit findings, delivered free of charge: the team handles
# disappointment exactly like this, by reading an excuse.
AUDIT_RESULT = "passed"


def render_entry() -> str:
    """Return the excuse exactly as it will be delivered."""
    return ENTRY_TEXT


def one_line_excuse(text: str) -> bool:
    """Confirm the excuse is a single line under 200 chars."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_line_excuse(text), "excuses stay one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
