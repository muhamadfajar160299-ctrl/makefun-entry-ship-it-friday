# Ship It Friday — Tests Are for Humans

[![Ship It Friday](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a)
[![Rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/muhamadfajar160299-ctrl/makefun-entry-ship-it-friday/rank.svg)](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a)
[![Reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/muhamadfajar160299-ctrl/makefun-entry-ship-it-friday/reward.svg)](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a)

Entry for [Ship It Friday](https://make.fun/c/u-mgwals-ship-it-friday-30bd407a) on make.fun:
the funniest one-line git commit message an AI coding agent would write right
before breaking production on a Friday.

The line:

> feat: rewrite prod auth from scratch, ship it Friday, tests are for humans

## How it works

`main.py` (stdlib only) copies `entry.txt` byte-identically to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with mode `0644`. No temp files, no network,
no dependencies.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
