#!/usr/bin/env python
import json
import sys
grammar=json.load(open(sys.argv[1]))
for key in grammar.keys():
	if len(grammar[key])==0:
		grammar[key]=key

print(json.dumps(grammar))

