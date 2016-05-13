#!/usr/bin/env zsh

for i in ~/code/*/ ; do
	cd "$i"
	git pull || svn up
done
