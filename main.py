"""Warning Label for Humans: One Line, Big Laugh.

Writes the chosen warning label — one single line, 82 characters — to
/output/entry.txt. The line was picked from 8 candidates scored against
the judge brief's five criteria (23/25) and won the 1v1 rounds against the
next-best candidates; the field sample (1,022 line-like entries) shows no
microwave / 0:01 / beat-the-beep angle anywhere, so it is not a cliche
cluster and not a copy of any sampled field line.

The gate requires UTF-8 text of 1 to 160 characters, not only whitespace,
so the program validates the line before writing, writes it directly with
open() (never tempfile.mkstemp — mkstemp makes mode 0600, which the
grader cannot read as another user), sets mode 0644 explicitly, and reads
the file back to confirm the bytes on disk are identical to the line.
"""

import os

LINE = "WARNING: This human stops the microwave at 0:01 every time, just to beat the beep."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the competition gate: 1-160 chars, one line, real text."""
    if not line or line != line.strip():
        raise ValueError("line must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 160:
        raise ValueError(f"line is {len(line)} chars, over the 160 limit")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("line contains control characters")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("bytes on disk differ from the line")


if __name__ == "__main__":
    main()
