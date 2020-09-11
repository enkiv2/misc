#!/usr/bin/env zsh

feeds=()

if [ $# -lt 1 ] ; then 
	if [ -e ~/.stupidrss ] ; then
		. ~/.stupidrss
	fi
fi

for item in "$@" ; do 
	feeds+="$item"
done

for feed in $feeds ; do
	curl $feed | grep '<link>' | sed 's/</\n</g;s/>/>\n/g' | grep http | sed 's/^.*"//;s/".*$//' | grep . | while read x ; do w3m -dump "$x" ; done
	sleep 4
done
