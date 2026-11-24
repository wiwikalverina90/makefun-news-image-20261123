#!/usr/bin/env python3
"""THE DAY'S LEDGER - entry runner for news-image-20261123 (akun7, G4).

My newspaper page lives beside this file as entry.png. This program does
one job only: verify the page is exactly the bytes I built, then copy it
to the output folder. Nothing is drawn here and no third-party library is
used - plain standard library, byte-for-byte copy, same result every run.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 337827
EXPECTED_SHA256 = "c7f9f27a8107e090ef20c9bdd80dcf7b6556f401ef7497bb7af92097dae67e78"
PNG_HEADER = b"\x89PNG\r\n\x1a\n"
ONE_MIB = 1048576


def run():
    folder = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(folder, "entry.png")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = os.path.join(target_dir, "entry.png")

    with open(source, "rb") as fh:
        blob = fh.read()

    if len(blob) == 0:
        sys.exit("entry.png is empty")
    if not blob.startswith(PNG_HEADER):
        sys.exit("entry.png is not a PNG file")
    if len(blob) > ONE_MIB:
        sys.exit("entry.png is over the 1 MiB competition limit")
    if len(blob) != EXPECTED_BYTES:
        sys.exit("entry.png size changed: %d != %d" % (len(blob), EXPECTED_BYTES))
    digest = hashlib.sha256(blob).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("entry.png sha256 changed: %s" % digest)

    os.makedirs(target_dir, exist_ok=True)
    with open(target, "wb") as fh:
        fh.write(blob)
    sys.stderr.write("copied entry.png: %d bytes sha256=%s\n" % (len(blob), digest))


if __name__ == "__main__":
    run()
