#!/usr/bin/env python
# -*- coding: utf-8
import os, sys, re

import nltk
from nltk.corpus import wordnet
from nltk.corpus import cmudict

from random import Random

global rhymes, rhyme_chunks, random, rhymelevel, antonyms, synonyms, hypernyms, hyponyms

random=Random()

antonyms={}
synonyms={}
hypernyms={}
hyponyms={}
rhymes={}
rhyme_chunks={}
rhymelevel=2


# from http://kashthealien.wordpress.com/2013/06/15/213/
def rhyme(inp, level):
	global rhyme_chunks
	if(not inp.isalpha()):
		return []
	inp=inp.lower()
	key=""
	entries=cmudict.entries()
	syllables = [(word, syl) for word, syl in entries if word == inp]
	if(len(syllables)>0):
		key=repr(syllables[0][1][-level:])
		if(key in rhyme_chunks):
			#print("Skipping because "+inp+" has a memoized rhyme")
			return rhyme_chunks[key]
	else:
		#print("Skipping because "+inp+" has no rhymes")
		return []
	myRhymes = []
	for (word, syllable) in syllables:
		myRhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
	if(len(syllables)>0): 
		rhyme_chunks[key]=list(set(myRhymes))
	return list(set(myRhymes))

def randomRhyme(w):
	global rhymes, random, rhymelevel
	w=w.lower()
	if not (w in rhymes):
		rhymes[w]=rhyme(w, rhymelevel)
		rhymes[w].append(w)
	if len(rhymes[w])==0: return w
	return random.choice(rhymes[w])

def multiWordRhymesOnly(w):
	global rhymes
	w=w.lower()
	if not (w in rhymes):
		rhymes1=rhyme(w, rhymelevel)
		rhymes1.append(w)
		rhymes[w]=[]
		for piece in rhymes1:
			if(piece.find("_")>0):
				rhymes[w].append(piece.replace("_", " "))
	if len(rhymes[w])==0: return w
	return random.choice(rhymes[w])
	

def main():
	i=0
	rhymeDict={}
	for line in sys.stdin.readlines():
		for word in re.split(r'([A-Za-z0-9]+|[^A-Za-z0-9]+)', line):
			rhym=multiWordRhymesOnly(word)
			if(rhym!=word):
				rhymeDict[rhym]=word
				i+=1
				if(i>25000): 
					break
		if(i>25000): 
			break
	skip=[]
	k=rhymeDict.keys()
	k.sort()
	for w in k:
		w2=multiWordRhymesOnly(w.split()[0]).replace("_", " ")
		if(w.find(w2)!=0 and w2 not in k and w2 not in skip):
			print(w2.upper()+": "+rhymeDict[w]+" (via "+w+")\n")
			skip.append(w2)
		else:
			print(w.upper()+": "+rhymeDict[w]+"\n")
	
if __name__=="__main__": main()
