#!/usr/bin/env zsh
echo "<html><body><table>"
sed 's/^/<tr><td>/;s/$/<\/td><\/tr>/;s/ /<\/td><td>/g'
echo "</table></body></html>"

