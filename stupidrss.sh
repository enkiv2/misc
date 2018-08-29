#!/usr/bin/env zsh

feeds=()

if [ -e ~/.stupidrss ] ; then
	. ~/.stupidrss
fi
for item in "$@" ; do 
	feeds+="$item"
done

for feed in $feeds ; do
	curl $feed | grep '<link>' | sed 's/^[ \t]*//;s/<[\/]*link>//g' | while read x ; do w3m -dump "$x" ; done
done
