#!/usr/bin/env python
import sys

stype="text"
ssource="notes"
stitle="[no title]"
scontent=[]
stags=[]

sf=open(sys.argv[1])
for line in sf.readlines():
		if line.find("Type: "==0):
				stype=line[6:].strip()
		elif line.find("Source: "==0):
				ssource=line[8:].strip()
		elif line.find("Title: "==0):
				stitle=line[7:].strip()
		elif line.find("* "==0):
				stags.append(line[2:].strip())
		else:
				scontent.append(line.strip())


