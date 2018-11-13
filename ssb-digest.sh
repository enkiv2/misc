#!/usr/bin/env zsh
sbot publish --type post --text "$(
	tac ~/.linkit | head -n 23 | 
	awk '
	BEGIN {
		FS="\t"
		print "Links digest\n"
	} { 
		title=$3
		if (title=="")
			title=$1 
		print "* [" title "](" $1 ")"; 
	} END { 
		print "\n[Links archive](http://www.lord-enki.net/links.html)"
	}')"

