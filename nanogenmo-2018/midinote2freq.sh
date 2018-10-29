#!/usr/bin/env zsh
midicsv | 
	egrep '(Note_on_c|End_track)' | sed 's/^.*End_track.*$//' | 
	cut -d\, -f 5 | 
	awk '{
		if(/[0-9]/){
			print 440*(2^(($1-69)/12))
		} else {print}
	}'
