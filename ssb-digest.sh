#!/usr/bin/env zsh
text="$(
	shuf -n 23 ~/.linkit | 
  sed 's|//medium.com/|//scribe.rip/|g' |
	awk '
	BEGIN {
		FS="\t"
		print "# The Redundant Daily Redundant\n\n## a daily digest of links I once found interesting\n"
	} { 
		title=$3
		if (title=="")
			title=$1 
		print "* [" title "](" $1 ") originally archived on " $2; 
	} END { 
		print "\n[full archive](http://www.lord-enki.net/links.html)"
	}' 
)"

msg='{"jsonrpc": "2.0", "method": "publish", "params": {"type": "post", "text":"'"$(echo "$text" | sed 's/$/\\\\n/' | tr -d '\n')"'"}}' 
echo "$text" | xclip
#echo "$msg"
#echo
#curl -v -H "Content-Type: application/json" -d "$msg" 127.0.0.1:3030
