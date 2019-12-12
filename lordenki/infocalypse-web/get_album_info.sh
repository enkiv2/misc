#!/usr/bin/env zsh
cat urls.txt| grep . | cut -d/ -f 5 | 
#	head -n 1 |  
	while read x ; do 
		wget -nc -O ${x}.json "https://api.jamendo.com/v3.0/albums/musicinfo/?client_id=$1&imagesize=400&id=$x&format=jsonpretty" 
		sleep 1
		[ -e ${x}.jpg ] || (
			wget $(cat ${x}.json | grep '"image"' | cut -d\" -f 4 | sed 's/\\\//\//g')
			mv 1.400.jpg ${x}.jpg
			sleep 1
		)
	done

