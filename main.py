#!/usr/bin/env python3
"""Entry for news-image-20261124: sum up Tuesday 24 November 2026 world news.

The image is drawn by build_image.py (Pillow) and shipped in this repository
as entry.png. This program copies it to the output directory. Standard
library only; no network; deterministic — every run writes identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    with open(dst, "wb") as f:
        f.write(data)
    print("wrote", dst, len(data), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
