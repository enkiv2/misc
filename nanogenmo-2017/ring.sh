#!/usr/bin/env zsh
./ring.py | ./annotate.py > _
while [[ `wc -w < _` -lt 50000 ]] ; do
	./annotate.py < _ > __
	mv __ _
done
cat _
rm _

