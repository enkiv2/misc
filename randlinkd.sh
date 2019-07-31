(while : ; do 
	post "$(item="$(shuf -n 1 ~/.linkit)"; date="$(echo "$item" | cut -f 2)"; date2=$(date -d "$date" +"%Y%m%d%H%M%S"); url="$(echo "$item" | cut -f 1)"; echo "Random link from the archives: https://web.archive.org/web/$date2/$url originally posted $date/")" 
	sleep 4h
done 2>&1) > /dev/null 

