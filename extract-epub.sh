#!/usr/bin/env zsh


if [[ $# -gt 1 ]] ; then
	for i in "$@" ; do
		$0 "$i"
	done
else
	tempdir=~/.$$
	mkdir "$tempdir"
	unzip -d "$tempdir" "$1"
	find "$tempdir" | egrep '\.(xhtml|html|htm)$' | sort | while read x ; do
		w3m -dump "$x" 
	done
	rm -rf $tempdir
fi

