#!/usr/bin/env zsh

( which shuf 2>&1 ) > /dev/null || function shuf() {
	name=.$$
	cat > $name ; len=$(wc -l < $name)
	tail -n $(((RANDOM%len)+1)) < $name | head -n 1
	rm $name
}

for item in "$@" ; do
	echo "$item"
done | shuf -n 1

