#!/usr/bin/env python

MIN_LINES=1000 # modify this if you want a higher or lower max output; without this default we often get zero-length output

from random import Random
random=Random()

import sys, os

global lines, words, world, mode, wAX
lines=[]
words={}
world={}
mode="first"
wAX=0

def accumulate():
	global lines, words, wAX
	for line in sys.stdin.readlines():
		line=line.strip()
		lines.append(line)
		for word in line.split():
			word=word.lower()
			if not (word in words):
				words[word]=1
			else:
				words[word]+=1
	if(mode=="avg2"):
		ax=0; c=0
		for w in words:
			c+=1
			ax+=words[w]
		wAX=((1.0*ax)/c)

def score(line):
	if(line==""):
		return ""
	wordl=line.split()
	if(mode=="first"):
		return wordl[0].lower()
	if(mode=="last"):
		return wordl[-1].lower()
	max=0; maxw=wordl[0]
	min=2**18; minw=wordl[0]
	ax=0
	for w in wordl:
		w=w.lower()
		if(words[w]>max):
			maxw=w; max=words[w]
		if(words[w]<min):
			minw=w; min=words[w]
		ax+=words[w]
	ax=ax/(1.0*len(wordl))
	if(mode=="max"):
		return maxw
	if(mode=="min"):
		return minw
	if(mode=="avg"):
		minD=max; minDw=wordl[0]
		for w in wordl:
			w=w.lower()
			if(abs(words[w]-ax)<minD):
				minD=abs(words[w]-ax)
				mindDw=w
		return minDw
	if(mode=="avg2"):
		minD=max; minDw=wordl[0]
		for w in wordl:
			w=w.lower()
			if(abs(words[w]-wAX)<minD):
				minD=abs(words[w]-wAX)
				mindDw=w
		return minDw
	
	return ""

def aggregate():
	global world
	lastS=""
	for line in lines:
		if not (lastS in world):
			world[lastS]=[]
		world[lastS].append(line)
		lastS=score(line)
	if not (lastS in world):
		world[lastS]=[]
	world[lastS].append("")

def follow(seed):
	if not (seed in world):
		sys.stderr.write("Seed \""+seed+"\" does not exist in training data; falling back to \"\".\n")
		seed=""
	line=random.choice(world[seed])
	seed=score(line)
	print(line)
	count=1
	while(count<MIN_LINES or seed!=""):
		line=random.choice(world[seed])
		seed=score(line)
		print(line)
		count+=1

if(__name__=="__main__"):
	seed=""
	if(len(sys.argv)>1):
		if(sys.argv[1] in ["first", "last", "min", "max", "avg", "avg2"]):
			mode=sys.argv[1]
		else:
			seed=sys.argv[1]
	if(len(sys.argv)>2):
		if(seed!=""):
			sys.stderr.write("Usage:\n\tphrasechain [mode] [seed]\nWhere mode is one of: first, last, min, max, avg, avg2\n")
			sys.exit(1)
		else:
			seed=sys.argv[2]
	accumulate()
	aggregate()
	follow(seed)

	
