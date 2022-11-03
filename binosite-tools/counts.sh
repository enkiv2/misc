#!/usr/bin/env zsh

function grepcount() {
	zgrep "$@" access_log binosite/access_log.*.gz | wc -l
}
scp accela_miniaturebinoculars@ssh.phx.nearlyfreespeech.net:/home/logs/access_log .
echo "Count: $(grepcount '\.htm')"
echo "PDF count: $(grepcount '\.pdf')"
echo "JB/JE manufacturer code list count: $(grepcount 'Page289\.htm')"
