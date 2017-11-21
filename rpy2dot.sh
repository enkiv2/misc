#!/usr/bin/env zsh
if [ $# -lt 1 ] ; then set *.rpy ; fi
for item in "$@" ; do
	cat "$item"	| 
		sed 's/^  *//g' | 
		egrep '^(label|jump)' | egrep -v '[\."]' |
		tr -d ':\r' |
		grep -v 'label _' | awk '
			/^label / { 
				if(curr_label)
					print curr_label " -> " $2 ";"
				curr_label=$2
			} 
			/^jump/ { 
				print curr_label " -> " $2 ";" 
			}' | sort | uniq
done | awk '
		
	BEGIN { 
		print "digraph path {" 
	} 
	{
		if(x[$1]) 	x[$1]=x[$1] $0
		else 		x[$1]=$0
	}
	END {
		print x["start"]
		for (i in x)
			if(i!="start")
				print x[i]
		print "}"
	}' 
