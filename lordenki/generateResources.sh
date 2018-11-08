#!/usr/bin/env zsh
. ../links.sh
dot < gui_evolution.dot -Tpng > gui_evolution.png
convert gui_evolution.png -colorspace HSI -channel B -level 100,0%  +channel -colorspace sRGB gui_evolution2.png
scp gui_evolution2.png accela_lordenki@ssh.phx.nearlyfreespeech.net:/home/public/
(echo "<html><head><title>Resources for A Survey Of Alternatives</title><link rel="stylesheet" type="text/css" href="vt240.css"></head><body><ul>" ; cat resources-survey-of-alternatives.txt | while read x ; do if echo "$x" | grep -q '://' ; then echo "<li><a href=\"$x\">$(y=$(getTitle "$x") ; [ -z "$y" ] && echo $x || echo $y )</a></li>" ; else echo "</ul>$x<ul>" ; fi ; done ; echo "<li><a href=\"gui_evolution2.png\">Map of GUI evolution</a></li></ul></body></html>") | tee resources-survey-of-alternatives.html
scp resources-survey-of-alternatives.html accela_lordenki@ssh.phx.nearlyfreespeech.net:/home/public

