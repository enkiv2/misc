#!/usr/bin/env zsh

function dump() {
	torify w3m -dump "$1" || w3m -dump "$1"
}

strings | tr '.' ' ' | sed "s/[^A-Za-z'][^A-Za-z']*/\n/g" | grep . | sort | uniq -c | sort -n | sed 's/^ *[0-9]* //' | while read x; do 
#	(cd ~/code/misc ; ./stupidLocalSearch.py search "$x" | head -n 10 | cut -d'	' -f 1 | while read y ; do grep -C5 "$x" "$y" ; done)
	dump "http://en.m.wiktionary.org/wiki/$x"
	dump "https://www.urbandictionary.com/define.php?term=$x"
	dump "https://www.etymonline.com/search?q=$x"
	dump "https://en.m.wikipedia.org/wiki/$x"
	dump "http://simple.m.wikipedia.org/wiki/$x" 
	dump "https://everything2.com/?node=$x"
	dump "https://www.gematrix.org/?word=$x&view_rude=on"
	dump "https://www.rhymezone.com/r/rhyme.cgi?Word=$x&typeofrhyme=perfect&org1=syl&org2=l&org3=y"
#	find ~/stories/gutenberg -type f | xargs grep -i "$x" | shuf -n 10
#	sleep 23
done

