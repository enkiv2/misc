#!/usr/bin/env zsh
. ../links.sh
(echo "<html><head><title>Resources for A Survey Of Alternatives</title><link rel="stylesheet" type="text/css" href="vt240.css"></head><body><ul>" ; cat resources-survey-of-alternatives.txt | while read x ; do if echo "$x" | grep -q '://' ; then echo "<li><a href=\"$x\">$(y=$(getTitle "$x") ; [ -z "$y" ] && echo $x || echo $y )</a></li>" ; else echo "</ul>$x<ul>" ; fi ; done ; echo "</ul></body></html>") | tee resources-survey-of-alternatives.html
scp resources-survey-of-alternatives.html accela_lordenki@ssh.phx.nearlyfreespeech.net:/home/public

