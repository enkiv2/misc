#!/usr/bin/env zsh
for i in intro.txt chapter*.txt ; do 
	(echo "<html><body>" ; cat $i | sed 's/^$/<p \/>/' ; echo "</body></html>") > ${i}.html
done

(echo "<html><body><h1>Glossary</h1><p/>" ; cat gloss.txt | sort | sed 's/$/<br \/>/' ; echo "</body></html>") > gloss.txt.html

