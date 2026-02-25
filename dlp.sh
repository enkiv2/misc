#!/usr/bin/env zsh

for i in "$@" ; do
	yt-dlp "$i"
done

