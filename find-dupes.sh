#!/usr/bin/env zsh
if [[ $# -gt 0 ]] ; then
	for dir in $@ ; do 
		find "$dir" -type f 
	done
else
	find . -type f
fi	 										|
	while read x ; do 
		md5sum -- "$x" 
	done  								| 
	awk '
		{
			hash=$1
			$1=""
			if(found[hash]) { 
				dupes[$0]++
			}
				found[hash]++
		} END { 
			for(name in dupes) { 
				print name 
			}
		}' | sed 's/^ //'

