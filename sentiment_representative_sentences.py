#!/usr/bin/env python
# -*- coding: utf-8
from textblob import TextBlob
import sys, os

SORT_BY_DELTA=True

lines=[]
linesByPolarity={}
sentimentByLine={}
pax=0
sax=0
i=0

for line in sys.stdin.readlines():
	blob=TextBlob(line)
	lines.append(line)
	polarity=blob.sentiment.polarity
	if(polarity in linesByPolarity):
		linesByPolarity[polarity].append(line)
	else:
		linesByPolarity[polarity]=[line]
	sentimentByLine[line]=blob.sentiment
	pax+=polarity
	sax=blob.sentiment.subjectivity
	i+=1

if(i==0):
	os.exit()

pax=(1.0*pax)/i
sax=(1.0*sax)/i

minDelta=1000
maxDelta=0
minI=lines[0]
maxI=lines[0]

if(SORT_BY_DELTA):
	lines_by_delta={}
	for line in lines:
		delta=abs(pax-sentimentByLine[line].polarity)
		if(delta in lines_by_delta):
			lines_by_delta[delta].append(line)
		else:
			lines_by_delta[delta]=[line]
	deltas=lines_by_delta.keys()
	deltas.sort()
	for delta in deltas:
		for line in lines_by_delta[delta]:
			sys.stdout.write(line)
		sys.stdout.flush()
else:
	for line in lines:
		delta=abs(pax-sentimentByLine[line].polarity)
		if(delta>maxDelta):
			maxDelta=delta
			maxI=line
		if(delta<minDelta):
			minDelta=delta
			minI=line

	print("Average polarity: "+str(pax))
	print("Average subjectivity: "+str(sax))
	print("Most representative: "+str(minDelta)+"\t"+minI)
	print("Least representative: "+str(maxDelta)+"\t"+maxI)

