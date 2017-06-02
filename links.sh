#!/usr/bin/env zsh
[[ -e ~/.linkit ]] || touch ~/.linkit

function linkit() {
	echo "$1\t$(date)" >> ~/.linkit
}
function fmtlinks() {
	echo "<html>"
	echo "<head><title>Links</title></head>"
	echo "<body>"
	echo "<table>"
	echo "<tr><th>Link</th><th>Date</th></tr>"
	tac ~/.linkit| awk 'BEGIN{FS="\t"} {print "<tr><td><a href=\"" $1 "\">" $1 "</a></td><td>" $2 "</td></tr>"}'
	echo "</table>"
	echo "<center><a href=\"https://github.com/enkiv2/misc/blob/master/links.sh\">Generated with links.sh</a></center>"
	echo "</body>"
	echo "</html>"
}
function uploadlinks() {
	fmtlinks > ~/index.html
	scp ~/index.html $1
}

