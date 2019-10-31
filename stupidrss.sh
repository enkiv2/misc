#!/usr/bin/env zsh

feeds=()

if [ -e ~/.stupidrss ] ; then
	. ~/.stupidrss
fi
for item in "$@" ; do 
	feeds+="$item"
done

for feed in $feeds ; do
	curl $feed | grep '<link>' | sed 's/</\n</g;s/>/>\n/g' | grep http | sed 's/^.*"//;s/".*$//' | while read x ; do w3m -dump "$x" ; done
done
