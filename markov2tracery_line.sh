#!/usr/bin/env zsh

echo "{}" > .ax
while read x ; do
	./traceryCombine.py <(echo "$x" | ./markov2tracery.py) .ax .ax2
	mv .ax{2,}
done
cat .ax
rm .ax

