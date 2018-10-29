#!/usr/bin/env zsh
for i in "$@" ; do 
	echo "# $(echo $i | sed 's/^.*\///;s/\.mid$//')" ; 
	cat $i | ./midinote2freq.sh |./freq2words.sh  ; 
done | sed 's/^$/===/;s/$/\n/'
