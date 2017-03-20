#!/usr/bin/env python
import gensim
from gensim.models import word2vec

from nltk.corpus import webtext
import sys

try:
	open("text8.wv", 'r')
	model=gensim.models.Word2Vec.load("text8.wv")
except:
	sys.stderr.write("Corpus not found; training...")
	sys.stderr.flush()
	sentences=[]
	for s in webtext.paras():
		for j in s:
			sentences.append(j)
	model=gensim.models.Word2Vec(sentences)
	model.save("text8.wv")
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

