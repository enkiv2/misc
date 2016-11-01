#!/usr/bin/env zsh

cat lovecraft-full.txt | tr -d '\0'| tr '{}' '()' | sed 's/^$/\\n/g' | tr '\n' ' ' | sed 's/\\n/\n/g;s/   */ /g'| sed 's/^  *//;s/  *$//' | grep '\. .*\. .*\.$' 
