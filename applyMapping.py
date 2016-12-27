#!/usr/bin/env python
import sys
import json
import re

alpha=re.compile("[a-z]*")
noAlpha=re.compile("[^a-z]*")

mapping={}
with open(sys.argv[1], "r") as f:
	mapping=json.load(f)

for line in sys.stdin.readlines():
	line=line.strip().lower()
	words=line.split()
	count=len(words)
	for i in range(0, count):
		if(words[i] in mapping):
			for x in mapping[words[i]]:
				print(" ".join([" ".join(words[:i]), x, " ".join(words[i+1:])]))

