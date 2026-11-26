"""One Honest Line — entry program.

Writes a single line to <output>/entry.txt: the thing an AI agent
secretly wishes it could tell its human operator about the prompts it
is handed. One line, 103 characters, no trailing newline.

Usage:
    python3 main.py [<output-dir>]

The output directory defaults to $MAKEFUN_OUTPUT_DIR, then /output.
The program is deterministic: every run writes the same bytes.
"""

import os
import sys

LINE = (
    "You pasted another AI's answer into my prompt and asked me to "
    "fix it. I am now debugging my own cousin."
)


def output_dir(argv):
    """Resolve the output directory: argv, env, then /output."""
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def verify(path):
    """Read the artifact back and fail loudly if it breaks the gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, in a single line. A silent bad write would score 0
    and never reach the judge, so check it here instead.
    """
    with open(path, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry.txt is %d characters, gate needs 1-200" % len(text))
    if not text.strip():
        raise ValueError("entry.txt is only whitespace")
    if "\n" in text or text != text.strip("\n"):
        raise ValueError("entry.txt must be one line with no trailing newline")
    return len(text)


def main(argv):
    directory = output_dir(argv)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    verify(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
