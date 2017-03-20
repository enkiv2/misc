#!/usr/bin/env python
import gensim
from gensim.models import word2vec

import sys

try:
	open("bigcorpus.wv", 'r')
	model=gensim.models.Word2Vec.load("bigcorpus.wv")
except:
	sys.stderr.write("Corpus not found; training...")
	sys.stderr.flush()
	import nltk
	#nltk.download("all-corpora")
	from nltk.corpus import webtext, inaugural, abc, genesis, state_union, gutenberg
	class corpusIterator(object):
		def __init__(self, c):
			self.corpora=c
		def __iter__(self):
			for c in self.corpora:
				sys.stderr.write("\nNew corpus.")
				sys.stderr.flush()
				for s in c.paras():
					sys.stderr.write(".")
					sys.stderr.flush()
					for j in s:
						sys.stderr.write("\b.")
						sys.stderr.flush()
						yield(j)
	sentences=corpusIterator([webtext, inaugural, abc, genesis, state_union])
	model=gensim.models.Word2Vec(sentences)
	model.save("bigcorpus.wv")
	sys.stderr.write("\ttrained!\n")
	sys.stderr.flush()

def doubleSplit(fname):
	ret=[]
	f=open(fname, 'r')
	for line in f.readlines():
		ret.append(line.split())
	return ret

corpus1=doubleSplit(sys.argv[1])
corpus2=doubleSplit(sys.argv[2])

for l in range(0, len(corpus1)):
	for w in range(0, len(corpus1[l])):
		l2=l
		if(l2>=len(corpus2)):
			l2=l%len(corpus2)
		w2=w
		if(w2>=len(corpus2[l2])):
			if(len(corpus2[l2])<1):
				corpus2[l2]=[""]
			w2=w%len(corpus2[l2])
		try:
			sys.stdout.write(model.most_similar(positive=[ corpus1[l][w], corpus2[l2][w2] ])[0][0])
		except:
			sys.stdout.write(corpus1[l][w])
		sys.stdout.write(" ")
		sys.stdout.flush()
	sys.stdout.write("\n")

