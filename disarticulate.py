#!/usr/bin/env python

from typoize import typoize
import tracery
import json

from random import Random
random=Random()

grammar=tracery.Grammar(json.load(open("verbal_inarticulations.json", "r")))

def disarticulate(s, rate=15):
	global grammar
	ret=[]
	words=s.split()
	for word in words:
		ret.append(word)
		if(random.choice(range(0, 100))<rate):
			ret.append(grammar.flatten("#origin#"))
	return typoize(" ".join(ret))

if __name__=="__main__":
	import sys
	for line in sys.stdin.readlines():
		print(disarticulate(line, int(sys.argv[1])))

