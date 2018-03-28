#!/usr/bin/env zsh

[[ -e ~/.notes ]] || touch ~/.notes

function addnote() {
	read x 
	echo "$x" >> ~/.notes
}
function rnote() {
	if [[ $# -eq 0 ]] ; then
		shuf -n 1 ~/.notes
	else
		egrep "$@" ~/.notes | shuf -n 1
	fi
}
function gnote() {
	egrep "$@" ~/.notes
}
function lnote() {
	if [[ $# -eq 0 ]] ; then
		tail -n 1 ~/.notes
	else
		tail -n "$@" ~/.notes
	fi
}

bnotd () 
{ 
    echo "$@" | addnote;
    post "Band name of the day: $@"
}
biotd () 
{ 
    post "Bad idea of the day: $@"
}
