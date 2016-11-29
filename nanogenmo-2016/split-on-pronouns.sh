#!/usr/bin/env zsh

./lovecraft-to-paras.sh | egrep ' ([Hh]e|[Ss]he|[Ii]t|I) ' | sed 's/$/<BR>/' | tr -d '\n' |
	sed 's/\( [Hh]e \)/\1\n/g' | shuf | tr -d '\n' |
	sed 's/\( [Ss]he \)/\1\n/g' | shuf | tr -d '\n' |
	sed 's/\( [Ii]t \)/\1\n/g' | shuf | tr -d '\n' |
	sed 's/\( I \)/\1\n/g' | shuf | tr -d '\n' |
	sed 's/<BR>/\n/g' | grep '^[A-Z]' | sed 's/$/\n/'
