#!/usr/bin/env python3
"""The Internet in One Word.

The whole internet, summed up in a single word: feral.

Why feral: the internet is wild, untamed, unpredictable, and
self-organising — a place where memes, arguments, cat videos and
conspiracy theories roam free with no keeper in charge. It is funny
on its own, true of the internet as a whole rather than one app or
mood, and it is not the first obvious word anyone reaches for.
"""

import os

WORD = "feral"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
