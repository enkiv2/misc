cat ~/stories/ebooks/holmes/* | tr 'A-Z' 'a-z' | sed 's/[^a-z][^a-z]*/\n/g' | grep . | sort | uniq > holmes.vocabulary
cat holmes.vocabulary |  while read x ; do grep -q "$x" /usr/share/dict/words || echo "$x" ; done > names.candidates

