#!/usr/bin/env python
import nltk
try:
        from nltk.corpus import wordnet
except:
        nltk.download("wordnet")
try:
        from nltk.corpus import cmudict
except:
        nltk.download("cmudict")

import sys, re
from random import Random
random=Random()

synonyms={}
hyponyms={}
hypernyms={}

def randomSyn(w):
	global random, synonyms
	w=w.lower()
	if not (w in synonyms):
		ret=[]
		for syn in wordnet.synsets(w):
			for l in syn.lemmas():
				ret.append(l.name())
		ret.append(w)
		synonyms[w]=list(set(ret))
	if len(synonyms[w])==0: return w
	return random.choice(synonyms[w])
def randomHyper(w):
	global random, hypernyms
	w=w.lower()
	if not (w in hypernyms):
		ret=[]
		for syn in wordnet.synsets(w):
                            if syn.hypernyms():
                                    ret.append(syn.hypernyms()[0].name())
		ret.append(w)
		hypernyms[w]=list(set(ret))
	if len(hypernyms[w])==0: return w
	return random.choice(hypernyms[w])

def randomHypo(w):
	global random, hyponyms
	w=w.lower()
	if not (w in hyponyms):
		ret=[]
		for syn in wordnet.synsets(w):
			    if syn.hyponyms():
				    ret.append(syn.hyponyms()[0].name())
		ret.append(w)
		hyponyms[w]=list(set(ret))
	if len(hyponyms[w])==0: return w
	return random.choice(hyponyms[w])

for line in sys.stdin.readlines():
    for word in re.split("[^A-Za-z]", line):
        word=word.lower()
        word=word.replace("the", "a")
        if word.find("e")>=0:
            ttl=1000
            w=randomSyn(word)
            while w.find("e")>=0:
                w=randomSyn(word)
                ttl-=1
                if(ttl==0): break
            if(w.find("e")>=0):
                ttl=1000
                w=randomHypo(randomHyper(word))
                while (w.find("e")>=0):
                    w=randomHypo(randomHyper(w))
                    if(w.find("e")>=0):
                        w=randomSyn(w)
                    ttl-=1
                    if(ttl==0): break
            if(w.find("e")>=0):
                w=word.replace("e", "-")
            sys.stdout.write(w.replace("_", " "))
        else:
            sys.stdout.write(word)
        sys.stdout.write(" ")

        
