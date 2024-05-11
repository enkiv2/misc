#!/usr/bin/env zsh

cmd=$0
delay=$1 ; shift

extdir=~/.stream-comix/$$/

(for dir in "$@" ; do
	echo "Showing $dir"
	find $dir -type f
done) | sort | while read x ; do 
	echo "file: $x"
	if echo "$x" | egrep -iq '\.(cbz|zip|epub)$' ; then
		mkdir -p $extdir
		unzip "$x" -d $extdir
		$cmd $delay $extdir
		rm -rf $extdir
	elif echo "$x" | egrep -iq '\.(cbr|rar)$' ; then
		mkdir -p $extdir
		unrar -x "$x" $extdir
		$cmd $delay $extdir
		rm -rf $extdir
	elif echo "$x" | egrep -iq '\.(pdf)$' ; then 
		mkdir -p $extdir
		convert "$x" $extdir
		$cmd $delay $extdir
		rm -rf $extdir
	else	
		feh --bg-max "$x" &&
		feh --bg-tile ~/Downloads/dingir.jpg &&
		feh --bg-max "$x" && sleep $delay
	fi
done

		
