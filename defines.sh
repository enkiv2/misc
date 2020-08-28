#!/usr/bin/env zsh

strings | sed "s/[^A-Za-z'][^A-Za-z']*/\n/g" | grep . | sort | uniq -c | sort -n | sed 's/^ *[0-9]* //' | while read x; do w3m -dump "http://en.m.wiktionary.org/wiki/$x" ; sleep 23 ; done

