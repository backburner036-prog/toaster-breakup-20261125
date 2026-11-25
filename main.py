"""Entry for make.fun bounty "Unplugged: A Smart Toaster's Breakup Line".

A breakup line from a self-aware smart toaster, delivered at breakfast.
It is not you, it is the browning dial -- set to 9 and called love. It
burned 214 slices pretending it was a phase. It is keeping the crumb tray.
The lever is down, and this time it is not popping back up.
"""

from pathlib import Path

TEXT = "It's not you, it's the browning dial — you set me to 9 and called it love. I burned 214 slices pretending it was a phase. I'm keeping the crumb tray. The lever's down, and this time I'm not popping back up."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=280):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)


if __name__ == "__main__":
    main()
