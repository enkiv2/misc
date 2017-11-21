#!/usr/bin/env zsh
cat *.rpy | 
	sed 's/^  *//g' | 
	egrep '^(label|jump)' | 
	tr -d ':\r' | 
	grep -v 'label _' | awk '
		/^label / { 
			curr_label=$2
		} 
		/^jump/ { 
			print curr_label " -> " $2 ";" 
		}' | awk '
			
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
