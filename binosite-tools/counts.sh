#!/usr/bin/env zsh

function grepcount() {
	zgrep "$@" access_log binosite/access_log.*.gz | wc -l
}
scp accela_miniaturebinoculars@ssh.nyc1.nearlyfreespeech.net:/home/logs/access_log .
echo "Count: $(grepcount 'GET .*\.htm')"
echo "PDF count: $(grepcount 'GET [^\"]*\.pdf')"
echo "JB/JE manufacturer code list count: $(grepcount 'GET [^\"]*Page289\.htm')"
echo "Other binoculars count: $(for i in 21222 2762 3047 3260 3540 3595 4610 3090 4508 290 705 1014 4487 563 1959 2326 2616 2860 ; do grepcount 'GET [^"]*Page'"${i}"'.htm' ; done | awk '{x+=$0} END{print(x)}')"

