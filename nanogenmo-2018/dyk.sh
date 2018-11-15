#!/usr/bin/env zsh

echo "# Did you know..." > dyk.md
echo >> dyk.md

while [[ `wc -w < dyk.md` -lt 50000 ]] ; do
	echo '```' >> dyk.md
	fortune dyk | ./wcwize.py >> dyk.md
	echo '```' >> dyk.md	
	echo -e "\n" >> dyk.md
done

