#!/usr/bin/env zsh

if [[ "$1" == "-h" ]] ; then
	echo -e "RBG: random background image\nUsage: $0 delay directory [directory ...]" >&2
	exit 1
fi

delay=$1 ; shift

while : ; do
	(for dir in "$@" ; do
		find $dir -type f
	done) | shuf | while read x ; do
		feh --bg-max "$x" &&
sleep $delay
#		(
#			feh --bg-$(echo -e "tile\nmax\nfill" | shuf -n 1) "$(find ~/Downloads/eyes -type f | shuf | head -n 1)"
#			feh --bg-tile  ~/Downloads/dingir.jpg 
#			feh --bg-max "$x" && sleep $delay
#		)
	done
done

