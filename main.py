"""Have You Tried Turning It Off? -- make.fun entry.

Writes exactly one funny line, spoken by a hopeless tech support
agent to a desperate customer, to /output/entry.txt.

The line is a fixed, deterministic string: no randomness, no input,
no network. It is written with no trailing newline so the file holds
exactly one line of 1-199 characters.
"""

import os

LINE = (
    "Have you tried turning it off and on again? I have tried "
    "everything else, so now I'm just hoping the computer takes "
    "pity on both of us."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
