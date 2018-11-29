#!/usr/bin/env zsh
[[ -e ~/.linkit ]] || touch ~/.linkit

function linkit() {
	[ -z "$1" ] || (
		grep -n -- "$1" ~/.linkit || (
			(which mass_archive 2>&1 > /dev/null && mass_archive "$1")
			export LC_ALL=en_US.UTF-8
			echo -e "$1\t$(date)\t$(getTitle "$1")" >> ~/.linkit
			post="$(export LC_ALL=en_US.UTF-8 ; tail -n 1 ~/.linkit | awk 'BEGIN{FS="\t"} {url=$1 ; title=$3 ; if(url!=title && title!=""&&title!=" ") {if(length(url)+length(title)>=280) {delta=(length(url)+length(title))-280; delta+=4; if(delta<length(title)) { title=substr(title, 0, length(title)-delta) "..." ; print title " " url } } else print title " " url } }' | grep -a . | head -n 1 | hxunent | recode -f UTF8)"
			[[ -n "$post" ]] && post "$post"
			stty sane 
	) )
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
function uploadlinks() {
	fmtlinks > ~/index.html
	scp ~/index.html $1
}

