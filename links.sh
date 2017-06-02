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
	echo "<th><td>Link</td><td>Date</td></th>"
	tac ~/.linkit| awk 'BEGIN{FS="\t"} {print "<tr><td><a href=\"" $1 "\">" $1 "</a></td><td>" $2 "</td></tr>"}'
	echo "</table>"
	echo "</body>"
}
function uploadlinks() {
	fmtlinks > ~/index.html
	scp ~/index.html $1
}

