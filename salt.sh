#!/usr/bin/env zsh
pfx="$HOME/music/talk/salt/"
curl http://longnow.org/projects/seminars/SALT.xml | grep mp3 | sed 's/^[   ]*//;s/[        ]*$//;s/<[^>]*>//g' | grep . |  tee salt.txt | (
	while read url ; do
		basename="$(echo "$url" | sed 's|^.*/||')"
		if [[ -e  "$pfs/$basename" ]] ; then
			echo "Skipping already downloaded file: $basename"
		else
			wget -nc -nd -P "$pfx" "$url"
			sleep 3
		fi
	done
)

