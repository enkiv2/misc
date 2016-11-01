#!/usr/bin/env zsh

export LC_ALL=C

echo "# $(cat lovecraft-surnames.txt | grep . | shuf -n 1)'s Dictionary of $(cat lovecraft-towns.txt | grep . | shuf -n 1) Rhyming Slang"
echo

cat /usr/share/dict/word.lst | ./rhyme-dict.py | grep . |  sort | uniq | gawk '{nfl=substr($0, 1, 1); if(nfl!=ofl) { print "## " nfl "\n" ; ofl=nfl ; } print $0 ; print "" ; }'

