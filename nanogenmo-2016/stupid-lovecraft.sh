#!/usr/bin/env zsh
./lovecraft-to-paras.sh | shuf -n 5000 > temp.md
cat temp.md | grep '"' | sed 's/"/\n"/g' | grep '^"' | awk '{if((++i)%2) { print } }' | grep '[A-Za-z]' | sed 's/^"//' | sort | uniq > quotes.md
paste quotes.md <(cat handey-quotes.txt dril-quotes.txt | shuf -n $(cat quotes.md | wc -l)) > quoteConv.tsv
cat quoteConv.tsv| sed 's/\//\\\//g;s/\./\\./g;s/\?/\\?/g;s/^/s\/\"/;s/\t/\"\/\"/;s/$/\"\/g\;/' > quoteConv.sed
cat temp.md | sed -f quoteConv.sed | sed 's/$/\n/'

