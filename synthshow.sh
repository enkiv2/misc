#!/usr/bin/env zsh

(osdsh 2>&1)> /dev/null

sed 's/ /\n/g' | while read x ; do
	clear
	(osdctl -s "$x" 2>&1) > /dev/null &
	echo "$x" | toilet &
	(echo "$x" | festival --tts  2>&1 )> /dev/null &
	sleep 0.23 
done

