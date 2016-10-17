#!/usr/bin/env zsh
sed 's/^      / <br> /;s/^	/ <br> /;s/^$/ <br> /;s/^  *//;s/  *$//' | 
	tr '\n.' ' \n' | sed 's/^  *//' | 		# Remove most fmt-style formatting in favor of one sentence (defined by terminating period) per line, with paragraph breaks substituted with '<br>'
	./phrasechain.py "$@" | 
	tr '\n' '.' | sed 's/<br> */\n\n/g;s/\./. /g' |	# replace newlines with periods again and turn paragraph breaks into newlines
	grep -v '^\.$'					# remove empty lines

