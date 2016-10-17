#!/usr/bin/env zsh
sed 's/^      /<br>./;s/^  *//;s/  *$//' | tr '\n.' ' \n' | sed 's/^  *//' | ./phrasechain.py "$@" | tr '\n' '.' | sed 's/<br>\./\n\n/g;s/\./. /g'

