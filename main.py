"""Copy entry.txt byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No temp files: the bytes are read from the entry.txt next to
this script and written straight to the output path, mode 0644.
"""

import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ["MAKEFUN_OUTPUT_DIR"], "entry.txt")

try:
    with open(SRC, "rb") as f:
        data = f.read()
except OSError as exc:
    raise SystemExit("cannot read entry.txt: %s" % exc)

if not data.strip():
    raise SystemExit("entry.txt is empty")

try:
    with open(OUT, "wb") as f:
        f.write(data)
    os.chmod(OUT, 0o644)
except OSError as exc:
    raise SystemExit("cannot write output: %s" % exc)
