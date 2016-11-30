#!/usr/bin/env zsh
cat lovecraft-full.txt| tr 'A-Z' 'a-z' | sed 's/[^A-Za-z]/\n/g'| grep . | sort | uniq -c | sort -nr | sed 's/^  *//;s/ /\t/' > lovecraft-freq.tsv
cat lovecraft-freq.tsv | cut -f 2 | while read x ; do grep -iq "^$x\$" /usr/share/dict/word.lst && echo "$x" ; done > lovecraft-freq-onlyrealwords.tsv
paste <( cat lovecraft-freq-onlyrealwords.tsv  ) <( tac lovecraft-freq-onlyrealwords.tsv ) | sed 's|^|s/ |;s|\t| / |;s|$| /g;|' > invert-freq.sed
cat lovecraft-full.txt|  sed -e "$(head -n 5000  invert-freq.sed)" | tee lovecraft-freq-inverted.md

