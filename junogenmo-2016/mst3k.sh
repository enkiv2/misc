#!/usr/bin/env zsh

while read x ; do
	echo "$x"
	if [[ $((RANDOM%100)) -lt 20 ]] ; then
		echo
		egrep -i "$(echo $x | sed 's/[^A-Za-z'"'"']/|/g;s/||/|/g;s/|$//')" mst3k_snarks.txt  | shuf -n 1
		fortune oblique ObliqueStrategies phoenix-checklist metacog-reading scamper
		echo
	fi
done

