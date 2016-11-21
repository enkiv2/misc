#!/usr/bin/env zsh

cat stopwords | tr -d '\r' | awk '{ print "s/ " $1 " / " $1 " \\n/g;" }' > stopwords.sed
cat stopwords | tr -d '\r' | awk '{ print "s/" $1 "\./"$1 " /g;\ns/\." $1 "/ " $1 "/g;" }' > stopwords-reconstruct.sed

sed 's/^      / <br> /;s/^	/ <br> /;s/^$/ <br> /;s/^  *//;s/  *$//' | 
	tr '\n.' ' \n' | sed 's/^  *//' | 		# Remove most fmt-style formatting in favor of one sentence (defined by terminating period) per line, with paragraph breaks substituted with '<br>'
	sed -f stopwords.sed |
	./phrasechain.py "$@" | 
	tr '\n' '.' | sed -f stopwords-reconstruct.sed | sed 's/<br> */\n\n/g;s/\./. /g' |	# replace newlines with periods again and turn paragraph breaks into newlines
	grep -v '^\.$'					# remove empty lines

