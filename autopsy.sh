#!/usr/bin/env zsh
curl http://autopsy.io | tr '<>' '\n\n' | grep '^a target=\"_blank\" href=' | sed 's/^.*href=\"//;s/".*$//' | shuf -n 5 | while read x ; do links -dump "$x" || w3m -dump "$x"  ; done
