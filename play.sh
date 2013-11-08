#!/bin/sh
# Something is wrong with Tom's sound card, so he needed this weirdness.
timidity -Ow $1 && aplay --device=hw:1 $(echo "$1"|cut -d. -f1).wav
