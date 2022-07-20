cut -d\  -f 1 access_log | uniq |
	sort | uniq |
	while read x ; do
		geoiplookup $x 
	done | 
		uniq | sort | uniq |
		cut -d: -f 2- | sed 's/^  *//'

