#!/usr/bin/env python3
"""THE DAY'S LEDGER — delivery guard for akun7, news-image-20261123 G4.

My newspaper page is finished and stored beside this file as entry.png.
This runner does no drawing at all. Its single job is to prove the page
on disk is exactly the page I signed off on — PNG signature, the 1 MiB
competition ceiling, the precise byte count and the sha256 fingerprint
recorded below — and only then copy those bytes, untouched, into the
output directory. Standard library only.
"""

import hashlib
import os
import sys

EXPECTED_BYTES = 235372
EXPECTED_SHA256 = "452cc943bedf3a2de82049c83754e1b60ba83d3f0be4930f5be85200f2032199"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
ONE_MIB = 1048576


def deliver():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = os.path.join(target_dir, "entry.png")

    with open(source, "rb") as fh:
        page = fh.read()
    # Revision note: the G4 slim re-render (posterised flat palette,
    # 235,372 bytes) replaced the first 337,827-byte render; the two
    # constants above record the slim page, and the checks below guard
    # exactly that page.

    if not page:
        sys.exit("entry.png is empty; refusing to deliver nothing")
    if page[:8] != PNG_MAGIC:
        sys.exit("entry.png lacks the PNG signature; refusing to deliver")
    if len(page) > ONE_MIB:
        sys.exit("entry.png is over the 1 MiB ceiling: %d bytes" % len(page))
    if len(page) != EXPECTED_BYTES:
        sys.exit(
            "entry.png has %d bytes; the signed-off page has %d"
            % (len(page), EXPECTED_BYTES)
        )
    digest = hashlib.sha256(page).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit("entry.png sha256 %s is not the signed-off digest" % digest)

    os.makedirs(target_dir, exist_ok=True)
    with open(target, "wb") as fh:
        fh.write(page)
    sys.stderr.write("delivered entry.png: %d bytes sha256=%s\n" % (len(page), digest))


if __name__ == "__main__":
    deliver()
