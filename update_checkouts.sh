#!/usr/bin/env zsh

rec() {
for i in  "$@" ; do
	echo
	echo "$i"
	cd "$i"
	:|(git pull --all --no-edit || svn up || rec $i/*/)
	echo
done
}

rec ~/code/*/
