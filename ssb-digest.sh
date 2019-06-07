#!/usr/bin/env zsh
sbot publish --type post --text "$(
	grep -a "$(date | sed 's/[0-9][0-9]*:.*$//')" ~/.linkit | 
	awk '
	BEGIN {
		FS="\t"
		print "# The Redundant Daily Redundant\n\n## a daily digest of what I'"'"'ve been reading\n"
	} { 
		title=$3
		if (title=="")
			title=$1 
		print "* [" title "](" $1 ")"; 
	} END { 
		print "\n[archive](http://www.lord-enki.net/links.html)"
	}')"

