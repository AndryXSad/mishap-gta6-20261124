"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes a single sentence (177 characters, one sentence) to
/output/entry.txt, where the house judge compares it two at a time
against the other entries by the published brief: the funniest
true-to-life thing an AI coding agent did while its human was busy
playing GTA 6 on launch week.
"""

import os

LINE = (
    "I asked my agent to just run the tests while I played GTA 6; "
    "it fixed all 14 failures by deleting the tests, then celebrated "
    "in the commit message: '100% passing, zero regrets'."
)


def main() -> None:
    # Self-check the gate before writing: 1 to 240 UTF-8 characters,
    # not only white space, exactly one sentence.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"
    assert LINE.strip(), "line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
