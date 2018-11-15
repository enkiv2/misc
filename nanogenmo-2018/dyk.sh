#!/usr/bin/env zsh

echo "# Did you know..." > dyk2.md
echo >> dyk2.md

fortune dyk | ./wcwize.py | sed 's/^/    /g;s/$/\n\n/g' >> dyk2.md
while [[ `wc -w < dyk2.md` -lt 50000 ]] ; do
	(echo "or" ; fortune dyk) | ./wcwize.py | sed 's/^/    /g;s/$/\n\n/g' >> dyk2.md
	(echo "and" ; fortune dyk) | ./wcwize.py | sed 's/^/    /g;s/$/\n\n/g' >> dyk2.md
	echo -e "\n" >> dyk2.md
	(fortune dyk) | ./wcwize.py | sed 's/^/    /g;s/$/\n\n/g' >> dyk2.md
done

