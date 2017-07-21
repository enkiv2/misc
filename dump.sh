#!/usr/bin/env zsh
for item in "$@" ; do
	w3m -dump "$item"
done

