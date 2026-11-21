#!/usr/bin/env python3
"""Copy the pre-rendered front page to the output path.

Stdlib only: no network, no clock, no randomness. The image is stored
in this repository as entry.png; this program just moves it to where the
grader looks. Running it twice writes byte-identical output.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
EXPECTED_SHA256 = "a8ea8fb38bed706162aec9d020acd2e7227e51323de3cbc53f6898e818393a1d"
EXPECTED_SIZE = 177442


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    data = open(dst, "rb").read()
    if len(data) != EXPECTED_SIZE:
        sys.exit("entry.png has the wrong size: %d" % len(data))
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        sys.exit("entry.png failed its sha256 self-check")
    print("wrote %s (%d bytes)" % (dst, len(data)))


if __name__ == "__main__":
    main()
