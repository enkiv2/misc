#!/usr/bin/env python
# -*- coding: utf-8
global hyponyms, random
from random import Random
random=Random()

import json
import sys, re


import nltk
from nltk.corpus import wordnet
from nltk.corpus import cmudict

plots=json.load(open("plots_preprocessed.json"))
hyponyms={}
hypernyms={}

def sprint(l):
    print(''.join([i if ord(i)<128 else ' ' for i in l]))

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

def norm(w):
    w=w.replace("_", " ")
    if(len(w.split("."))>1):
        w=w.split(".")[0]
    return w

def hyperAnnotate(w):
    hyper=randomHyper(w)
    if(hyper==w.lower()):
        return None
    return "\t"+random.choice(["A kind of "])+norm(hyper)
def hypoAnnotate(w):
    hypos=[]
    for i in range(0, random.choice(range(1, 5))):
        hypo=norm(randomHypo(w))
        if (not (hypo in hypos)) and hypo!=w.lower():
            hypos.append(hypo)
    if(len(hypos)>0):
        return "\t"+random.choice(["Ex.", "For instance", "Such as"])+", "+(", ".join(hypos))
    return None
def crossRefAnnotate(w):
    if not w.isalpha():
        return None
    for i in range(0, 10):
        title=random.choice(plots.keys())
        if(plots[title].find(w)):
            note="\tMuch as in "+title+", where: \n\t\t"+plots[title].replace("\n", "\n\t\t")
            return note
    return None

def annotate(line):
    words=re.split(r'([A-Za-z0-9]+|[^A-Za-z0-9]+)', line.strip())
    l2=[]
    for word in words:
        l2.append(word)
        if(random.choice(range(0, 100))<10):
            poss=[]
            hypoAnnotation=hypoAnnotate(word)
            if(hypoAnnotation):
                poss+=[hypoAnnotation]
            hyperAnnotation=hyperAnnotate(word)
            if(hyperAnnotation):
                poss+=[hyperAnnotation]
            crossRefAnnotation=crossRefAnnotate(word)
            if(crossRefAnnotation):
                poss+=[crossRefAnnotation]
            if(len(poss)>0):
                l2+=["\n"+random.choice(poss)+"\n"]
    return "".join(l2)

for line in sys.stdin.readlines():
    sprint(annotate(line))
