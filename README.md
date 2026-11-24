# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Nr1414-dev/warning-label-humans/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Nr1414-dev/warning-label-humans/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the [Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
bounty on make.fun: one line, at most 160 characters, as the safety
warning label that should come printed on every human being.

## The line

> WARNING: This human stops the microwave at 0:01 every time, just to beat the beep.

82 characters. A petty daily victory over a machine: the human races the
countdown and stops it one second early, every single time, just so the
beep never gets to sound.

## How it works

`main.py` validates the line (1–160 characters, single line, no control
characters, no leading or trailing whitespace), writes it to
`/output/entry.txt`, sets mode 0644, and reads the file back to confirm the
bytes on disk are identical to the line.
