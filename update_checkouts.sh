#!/usr/bin/env zsh

for i in ~/code/*/ ; do
	echo
	echo "$i"
	cd "$i"
	git pull || svn up
	echo
done
