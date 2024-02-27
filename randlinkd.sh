MAX=300

processLink() {
	read item;
	date="$(echo "$item" | cut -f 2)" 
	date2=$(date -d "$date" +"%Y%m%d%H%M%S") 
	url="$(echo "$item" | cut -f 1 | sed 's|//medium.com/|//scribe.rip/|g')"
	url2="https://web.archive.org/web/$date2/$url"
	title="$(echo "$item" | cut -f 3-)"
	template="Random link from the archives: \"$title\" $url2 originally retrieved $date"
	if [ $(echo "$template" | wc -c) -gt $MAX ]; then
		template="Random link from the archives: \"$title\" $url2"
		if [$(echo "$template" | wc -c) -gt $MAX ]; then
			template="#randomArchiveLink \"$title\" $url2 @ $date"
			if [$(echo "$template" | wc -c) -gt $MAX ]; then
				template="#randomArchiveLink \"$title\" $url2 @ $date2"
				if [$(echo "$template" | wc -c) -gt $MAX ]; then
					template="#randomArchiveLink \"$title\" $url2"
					if [$(echo "$template" | wc -c) -gt $MAX ]; then
						template="#randomArchiveLink $url2 @ $date"
					fi
				fi
			fi
  	fi
  fi
	echo "$template"
}
(while : ; do 
	post "$(shuf -n 1 ~/.linkit | processLink)" 
	sleep 4h
	sleep 23m
done 2>&1)  > /dev/null 

