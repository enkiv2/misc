#!/usr/bin/env zsh
for i in medium-export/*.html ; do w3m -dump "$i" ; done  | sed 's/^$/\\r/g' | tr '\n' ' ' | sed 's/\\r/\n/g' | sed 's/^  *//' | egrep -v '^(View original|Canonical link|By A pig|Exported from Medium on|Tagged in)' | egrep -v '(━━━━|…)' | sed 's/\([\t ]\)[\t ]*/\1/g' | sed 's/[ \t]*$//' | grep . |  uniq

