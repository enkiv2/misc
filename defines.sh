#!/usr/bin/env zsh

strings | tr '.' ' ' | sed "s/[^A-Za-z'][^A-Za-z']*/\n/g" | grep . | sort | uniq -c | sort -n | sed 's/^ *[0-9]* //' | while read x; do 
	(cd ~/code/misc ; ./stupidLocalSearch.py search "$x" | head -n 10 | cut -d'	' -f 1 | while read y ; do grep -C5 "$x" "$y" ; done)
	torify w3m -dump "http://en.m.wiktionary.org/wiki/$x"
	torify w3m -dump "https://www.urbandictionary.com/define.php?term=$x"
	torify w3m -dump "https://www.etymonline.com/search?q=$x"
	torify w3m -dump "https://en.m.wikipedia.org/wiki/$x"
	torify w3m -dump "http://simple.m.wikipedia.org/wiki/$x" 
	torify w3m -dump "https://everything2.com/?node=$x"
	torify w3m -dump "https://www.gematrix.org/?word=$x&view_rude=on"
	grep -i "$x" ~/stories/ebooks/gutenberg/* | head -n 10
	sleep 23
done

