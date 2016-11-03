#!/usr/bin/env python
# -*- coding: utf-8
import os, sys, re

import pronouncing

from random import Random

global rhymes

random=Random()

rhymes={}



def randomRhyme(w):
	global rhymes, random, rhymelevel
	w=w.lower()
	if not (w in rhymes):
		rhymes[w]=pronouncing.rhymes(w)
		rhymes[w].append(w)
	if len(rhymes[w])==0: return w
	return random.choice(rhymes[w])

def multiWordRhymesOnly(w):
	global rhymes
	w=w.lower()
	if not (w in rhymes):
		rhymes1=pronouncing.rhymes(w)
		rhymes1.append(w)
		rhymes[w]=[]
		for piece in rhymes1:
			if(piece.find("_")>0):
				rhymes[w].append(piece.replace("_", " "))
	if len(rhymes[w])==0: return w
	return random.choice(rhymes[w])
	

def main():
	i=0
	skip=[]
	rhymeDict={}
	for line in sys.stdin.readlines():
		for word in re.split(r'([A-Za-z0-9]+|[^A-Za-z0-9]+)', line):
			rhym=multiWordRhymesOnly(word)
			if(rhym!=word):
				rhymeDict[rhym]=word
				w2=multiWordRhymesOnly(rhym.split()[0]).replace("_", " ")
				if(rhym.find(w2)!=0 and w2 not in rhymeDict and w2 not in skip):
					print(w2.upper()+": "+rhymeDict[rhym]+" (via "+rhym+")\n")
					skip.append(w2)
					i+=1
				elif(rhym not in skip):
					print(rhym.upper()+": "+rhymeDict[rhym]+"\n")
					skip.append(rhym)
					i+=1
				if(i>25000): 
					break
		if(i>25000): 
			break
	
if __name__=="__main__": main()
