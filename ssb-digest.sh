#!/usr/bin/env zsh
sbot publish --type post --text "$(
	shuf -n 23 ~/.linkit | 
	awk '
	BEGIN {
		FS="\t"
		print "# The Redundant Daily Redundant\n\n## a daily digest of links I once found interesting\n"
	} { 
		title=$3
		if (title=="")
			title=$1 
		print "* [" title "](" $1 ") originally archived on " $2; 
	} END { 
		print "\n[full archive](http://www.lord-enki.net/links.html)"
	}')"

