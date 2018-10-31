#!/usr/bin/env zsh
wl=pg-freq.txt
#wl=tvwl.txt
awk '{
	if(/[0-9]/) {
		print int($1+0.5-20)
	} else {print}
}' | 
	while read x ; do 
		grep "^$x " $wl | 
			awk '{print $2}' ; 
	done | 
		tr '\n' ' ' | 
		sed 's/  /\n/g;s/^ //' 
echo

