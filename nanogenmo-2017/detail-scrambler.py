#!/usr/bin/env python
# -*- coding: utf-8
import os, sys, re

import nltk
from nltk.corpus import wordnet
from nltk.corpus import cmudict

from random import Random
global random, hypernyms, hyponyms, correspondences
hypernyms={}
hyponyms={}
correspondences={}
random=Random()

def matchCaps(a, b):
    if(a.istitle()):
        return b.title()
    if(a.isupper()):
        return b.upper()
    return b

def getCorrespondence(w):
    global correspondences
    w2=w.lower()
    if(w2 in correspondences):
        return matchCaps(w, correspondences[w2])
    else:
#        hyper=randomHyper(w2)
#        if(hyper==w2):
#            correspondences[w2]=w2
#            return w
#        hypo=randomHypo(hyper)
#        if(hypo==hyper):
#            correspondences[w2]=w2
#            return w
#        if w2==hypo:
#            return w
        #ret=randomHypo(randomHypo(randomHyper(randomHyper(w))))
        ret=randomHypo(randomHyper(w))
        if(len(ret.split('.'))>1):
            ret=ret.split('.')[0]
        if(w2=="."):
            ret=w2
        correspondences[w2]=random.choice(([w2]*9)+[ret])
        return matchCaps(w, ret)

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

def main():
    for line in sys.stdin.readlines():
        outWords=[]
	for w in re.split(r'([A-Za-z0-9]+|[^A-Za-z0-9]+)', line.strip()):
            outWords.append(getCorrespondence(w))
        print("".join(outWords).replace("_", " "))
#    maxhypo=0
#    for item in hyponyms:
#        maxhypo=max(maxhypo, len(hyponyms[item]))
#    maxhyper=0
#    for item in hypernyms:
#        maxhyper=max(maxhyper, len(hypernyms[item]))
#    print ("Max hyponyms: "+str(maxhypo))
#    print ("Max hypernyms: "+str(maxhyper))

main()
