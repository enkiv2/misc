#!/usr/bin/env python
# -*- coding: utf-8
from textblob import TextBlob, Word
import sys, os
from random import Random
random=Random()

poolsize=100
expandTries=1000

def guessSingular(w):
	""" assume singular unless non-collective noun where form is equivalent to plural """
	wW=Word(w)
	ws=wW.singularize()
	wp=Word(ws).pluralize()
	singular=True
	if(w.lower()!=ws.lower()):
		if(w.lower()==wp.lower()):
			singular=False
	return singular
def tagFormatConvert(t):
	pfx=t[0].lower()
	if(pfx=="j"):
		return "a"
	return pfx

if(len(sys.argv)<3):
	print("Usage: "+sys.argv[0]+" sentence target\nTranslates sentence into a (theoretically synonymous) new sentence with the same approximate sentiment as target (which may be a sentiment polarity value or a model sentence).")
	sys.exit()

try:
	target=float(sys.argv[2])
except:
	target=TextBlob(sys.argv[2]).sentiment.polarity
sentence=sys.argv[1]
blob=TextBlob(sentence)
options=[]
optionSyns=[]
for tag in blob.tags:
	word=Word(tag[0])
	syns=[]
	try:
		syns=word.get_synsets(tagFormatConvert(tag[1]))
	except:
		syns=word.get_synsets()
	syns_clean=[tag[0]]
	singular=True
	if(tag[1][0]=="N"):
		singular=guessSingular(tag[0])
	for syn in syns:
		lemmanames=syn.lemma_names()
		for name in lemmanames:
			if(name.find(".")>=0):
				name=name[:name.find(".")]
			if(not singular):
				name=Word(name).pluralize()
			name=name.replace("_", " ")
			syns_clean.append(name)
	optionSyns.append(syns_clean)
i=0
while i<expandTries and len(options)<poolsize:
	rephrase=[]
	for word in optionSyns:
		if(len(word)>1):
			rephrase.append(random.choice(word))
		else:
			rephrase.append(word[0])
	rephraseS=" ".join(rephrase)
	if not (rephraseS in options):
		options.append(rephraseS)
	expandTries+=1

optionsByDelta={}
for option in options:
	optionblob=TextBlob(option)
	delta=abs(target-(optionblob.sentiment.polarity))
	# print(str(delta)+"\t"+str(optionblob.sentiment.polarity)+"\t"+option)
	if(delta in optionsByDelta):
		optionsByDelta[delta].append(option)
	else:
		optionsByDelta[delta]=[option]

keys=optionsByDelta.keys()
best=optionsByDelta[min(keys)]
if(len(best)>1):
	#print(str(min(keys))+"\t"+random.choice(best))
	print(random.choice(best))
else:
	#print(str(min(keys))+"\t"+best[0])
	print(best[0])

