#!/usr/bin/env zsh

nye=1451624400
daySec=$((24*60*60))

for day in {0..365}; do
	echo "# $(date -d "@$((nye+(day*daySec)))")"
	echo
	for entry in {0..10} ; do
		./tinyTarotStory.py
		echo
	done
	echo
done

