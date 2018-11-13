#!/usr/bin/env zsh
sbot publish --type post --text "$(
	tac ~/.linkit | head -n 23 | 
	awk '
	BEGIN {
		FS="\t"
		print "The Redundant Daily Redundant: a daily digest of 23 links you (should) have already seen\n"
	} { 
		title=$3
		if (title=="")
			title=$1 
		print "* [" title "](" $1 ")"; 
	} END { 
		print "\n[archive](http://www.lord-enki.net/links.html)"
	}')"

