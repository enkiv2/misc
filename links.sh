#!/usr/bin/env zsh
[[ -e ~/.linkit ]] || touch ~/.linkit

function linkit() {
	nopost=""
	if [[ "$1" == "-s" ]] ; then
		nopost="-s"
		shift
	fi
	if [[ $# -gt 1 ]] ; then
		for item in "$@" ; do
			linkit $nopost "$item"
		done
	else
		[ -z "$1" ] || (
			url="$(echo $1 | sed 's/\([&?]\)\(utm\|mc\)_.*$//;s/\([&?]\)curator=.*$//')"
			grep -a -n -- "$url" ~/.linkit || (
				(which mass_archive 2>&1 > /dev/null && mass_archive "$url")
				export LC_ALL=en_US.UTF-8
				echo -e "$url\t$(date)\t$(getTitle "$url")" >> ~/.linkit
				post="$(export LC_ALL=en_US.UTF-8 ; tail -n 1 ~/.linkit | awk 'BEGIN{FS="\t"} {url=$1 ; title=$3 ; if(url!=title && title!=""&&title!=" ") {if(length(url)+length(title)>=280) {delta=(length(url)+length(title))-280; delta+=4; if(delta<length(title)) { title=substr(title, 0, length(title)-delta) "..." ; print title " " url } } else print title " " url } }' | grep -a . | head -n 1 | hxunent | recode -f UTF8)"
				[[ -n "$post" ]] && [[ -z "$nopost" ]] && post "$post"
				stty sane 
		) )
	fi
}
function getTitle() {
	curl -m 2 "$1"| grep -a -i "<title>" | head -n 1 | sed 's/^.*<[tT][iI][tT][lL][eE]>//;s/<\/[tT][iI][tT][lL][eE]>.*//' | 
		sed 's/&#039\;/'"'"'/g;s/&#39\;/'"'"'/g;s/&quot\;/"/g' | 
		tr '\221\222\223\224\226\227' '\047\047""--'
}
function fmtlinks() {
	echo "<html>"
	echo '<head><title>Links</title><link rel="stylesheet" type="text/css" href="vt240.css"></head>'
	echo "<body>"
	echo "<table>"
	echo "<tr><th>Link</th><th>Date</th></tr>"
	tac ~/.linkit| awk 'BEGIN{FS="\t"} {title=$1; if($3 != "" && $3 != "\n" && $3 != "\r") title=$3; print "<tr><td><a href=\"" $1 "\">" title "</a></td><td>" $2 "</td></tr>"}'
	echo "</table>"
	echo "<center><a href=\"https://github.com/enkiv2/misc/blob/master/links.sh\">Generated with links.sh</a></center>"
	echo "</body>"
	echo "</html>"
}
function fmtlinksrss() {
	tac ~/.linkit | iconv -c |  
		awk '
			BEGIN{
				IFS=OFS=FS="\t"; 
				print "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>"
				print "<rss version=\"2.0\">"
				print "<channel>"
				print "<title>The Redundant Daily Redundant</title>"
				print "<link>http://www.lord-enki.net/links.html</link>"
				print "<lastBuildDate>" strftime() "</lastBuildDate>"
				print "<pubDate>" strftime() "</pubDate>"
				print "<ttl>18000</ttl>"
			} { 
				datecmd = "date +\"%a, %d %B %Y\" -d \"" $2 "\""
				datecmd | getline date
				close(datecmd)
				date2cmd = "date -d \"" date "\" +\"%Y%m%d%H%M%S\""
				date2cmd | getline date2
				close(date2cmd)
				linkcmd = "echo \"" $1 "\" | recode utf8..html"
				linkcmd | getline link
				close(linkcmd)
				title=$3
				if(title=="") {
					title=link
				}
				print "<item>"
				print "<title>" title "</title>"
				print "<description>" title "</description>"
				print "<link>" link "</link>"
				print "<guid isPermaLink=\"true\">https://web.archive.org/web/" date2 "/" link "</guid>"
				print "<pubDate>" date "</pubDate>"
				print "</item>\n"
			} END{ 
				print "</channel>"
				print "</rss>"
			}
		'
}
function uploadBandNames() {
	(
	echo '<html>'
	echo '<head><title>Band Names</title><link rel="stylesheet" type="text/css" href="vt240.css"></head>'
	echo '<body><table><tr><th>Date</th><th>Band name</th></tr>'
	grep '	Band name of the day: ' ~/code/misc/lordenki/twtxt.txt | 
		sed 's/^/<tr><td>/;s/	Band name of the day: /<\/td><td>/;s/$/<\/td><\/tr>/' | 
		tac 
	echo "</table></body></html>") > ~/bandnames.html
	scp ~/bandnames.html $1
}
function uploadBadIdeas() {
	(
	echo '<html>'
	echo '<head><title>Ideas</title><link rel="stylesheet" type="text/css" href="vt240.css"></head>'
	echo '<body><table><tr><th>Date</th><th>Idea</th></tr>'
	grep '	Bad idea of the day: ' ~/code/misc/lordenki/twtxt.txt | 
		sed 's/^/<tr><td>/;s/	Bad idea of the day: /<\/td><td>/;s/$/<\/td><\/tr>/' | 
		tac 
	echo "</table></body></html>") > ~/ideas.html
	scp ~/ideas.html $1
}
function uploadlinks() {
	fmtlinks > ~/index.html
	fmtlinksrss > ~/feed.rss
	scp ~/index.html $1
	scp ~/feed.rss $(echo $1 | sed 's/\/[^\/]*$//')
}

