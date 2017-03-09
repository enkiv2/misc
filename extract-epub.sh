#!/usr/bin/env zsh

tempdir=~/.$$
mkdir $tempdir
for i in "$@" ; do
	unzip -d "$tempdir/${i}.d" "$i"
done
find "$tempdir" | egrep '\.(xhtml|html|htm)$' | sort | while read x ; do
	w3m -dump "$x" 
done
rm -rf $tempdir

