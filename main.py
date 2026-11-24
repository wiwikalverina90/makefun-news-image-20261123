#!/usr/bin/env python3
"""Runner for THE DAY'S LEDGER (news-image-20261123, akun7 G4).

The finished newspaper page sits next to this script as entry.png. The
script's whole responsibility is guarding that page: it checks the PNG
signature, the 1 MiB ceiling, the exact byte count and the sha256 I
recorded at build time, and only then copies the file, untouched, into
the output directory. Standard library only; no drawing happens here.
"""

import hashlib
import os
import sys

SIZE_I_RECORDED = 337827
SHA_I_RECORDED = "c7f9f27a8107e090ef20c9bdd80dcf7b6556f401ef7497bb7af92097dae67e78"
SIGNATURE = b"\x89PNG\r\n\x1a\n"
LIMIT = 1048576


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    page_path = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = os.path.join(out_dir, "entry.png")

    with open(page_path, "rb") as fh:
        page = fh.read()

    if len(page) == 0:
        sys.exit("entry.png is empty - nothing to deliver")
    if page[:8] != SIGNATURE:
        sys.exit("entry.png does not start with the PNG signature")
    if len(page) > LIMIT:
        sys.exit("entry.png exceeds 1 MiB: %d bytes" % len(page))
    if len(page) != SIZE_I_RECORDED:
        sys.exit("entry.png is %d bytes, expected %d" % (len(page), SIZE_I_RECORDED))
    if hashlib.sha256(page).hexdigest() != SHA_I_RECORDED:
        sys.exit("entry.png sha256 does not match the recorded digest")

    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(page)
    sys.stderr.write(
        "entry.png delivered: %d bytes sha256=%s\n"
        % (len(page), hashlib.sha256(page).hexdigest())
    )


if __name__ == "__main__":
    main()
