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
		feh --bg-tile ~/Downloads/dingir.jpg &&
		(find ~/Downloads/eyes -type f | shuf | head -n 5 |
			while read y ; do 
				feh --bg-tile "$x" &&
				feh --bg-tile "$y" && 
				feh --bg-max "$x" &&
				feh --bg-tile ~/Downloads/dingir.jpg &&
				feh --bg-max "$x" &&
				feh --bg-max "$y" && 
				feh --bg-max "$x" &&
				feh --bg-tile ~/Downloads/dingir.jpg &&
				feh --bg-max "$x" &&
				feh --bg-max ~/Downloads/dingir.jpg &&
				feh --bg-max "$x" &&
				feh --bg-fill "$y" && 
				feh --bg-fill ~/Downloads/dingir.jpg &&
				feh --bg-fill "$x" &&
				feh --bg-tile ~/Downloads/dingir.jpg 
		; done ) &&
		feh --bg-max "$x" && sleep $delay
	done
done

