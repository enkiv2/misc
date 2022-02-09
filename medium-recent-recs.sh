#!/usr/bin/env zsh
cat medium-export/claps/*.html 				| 
	sed 's/</\n</g' 										| 
	grep '^<a class="h-cite u-like-of' 	| 
	sed 's/^<a.*href="//;s/".*$//'			|
	tac
