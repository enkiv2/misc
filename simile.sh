#!/usr/bin/env zsh
curl -s  http://www.bartleby.com/161/$(( (RANDOM%3186 )+ 1)).html | awk '/<!-- BEGIN CHAPTER -->/ { show=1 } /<!-- END CHAPTER -->/ { show=0 } /<TD>/ { if(show) print } {}' | sed 's/&#151\;/ --/g;s/<BR>/\n/g;s/&[^;]*\;//g;s/<[^>]*>//g'

