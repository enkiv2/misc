#!/usr/bin/env zsh

echo "<html>"
echo "<head><title>iNFOCALYPSE</title></head>"
echo "<body>"
echo "<center>"
echo "<table>"


for album in $(ls *.json | sort -nr) ; do
	./album2html.py $album | sed 's/^/<td>/;s/$/<\/td>/'
done | awk 'BEGIN { print("<tr>") } { print ; i++; if(i>3) { i=0 ; print "</tr>" ; print "<tr>" } } END {print "</tr>"}'

echo "</table>"
echo "<table>"
echo "<tr>"
echo "<td><center><a href=\"http://www.patreon.com/user?u=37198\"><img src=\"patreon.png\" alt=\"Infocalypse on Patreon\" width=\"100\" /><br>Infocaypse on Patreon</a></center></td>"
echo "<td><center><a href=\"https://www.jamendo.com/artist/5060/infocalypse\"><img src=\"jamendo.png\" alt=\"Infocalypse on Jamendo\" width=\"100\" /><br>Infocaypse on Jamendo</a></center></td>"
echo "<td><center><a href=\"http://infocalypse.bandcamp.com\"><img src=\"bandcamp.png\" alt=\"Infocalypse on Bandcamp\" width=\"100\" /><br>Infocaypse on Bandcamp</a></center></td>"
echo "</tr>"
echo "</table>"
echo "</center>"
echo "</body>"
echo "</html>"
