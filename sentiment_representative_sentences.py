#!/usr/bin/env python
# -*- coding: utf-8
from textblob import TextBlob
import sys, os

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

for line in lines:
	delta=abs(pax-sentimentByLine[line].polarity)
	if(delta>maxDelta):
		maxDelta=delta
		maxI=line
	if(delta<minDelta):
		minDelta=delta
		minI=line

print("Most representative: "+minI)
print("Least representative: "+maxI)

