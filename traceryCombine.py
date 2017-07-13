#!/usr/bin/env python
import json
import sys
out=sys.stdout
if(len(sys.argv)<3):
	sys.stderr.write("Usage: "+sys.argv[0]+" jsonfile jsonfile [output]\n")
	sys.exit(1)
if(len(sys.argv)>3):
	out=open(sys.argv[3], 'w')
grammar1=json.load(open(sys.argv[1], 'r'))
grammar2=json.load(open(sys.argv[2], 'r'))
for key in grammar1.keys():
	if key in grammar2:
		grammar2[key].extend(grammar1[key])
	else:
		grammar2[key]=grammar1[key]
json.dump(grammar2, out)

