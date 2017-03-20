#!/usr/bin/env python
from gensim import Word2Vec
from gensim.models import word2vec

import sys

try:
	open("text8.wv", 'r')
	model=Word2Vec.load("text8.wv")
except:
	sys.stderr.write("Corpus not found; training...")
	sys.stderr.flush()
	sentences = word2vec.Text8Corpus('text8')
	model=Word2Vec(sentences)
	model.save("text8.wv")
	sys.stderr.write("\ttrained!\n")
	sys.stderr.flush()

def doubleSplit(fname):
	ret=[]
	f=open(fname, 'r')
	for line in f.readlines():
		ret.push(line.split())
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
			w2=w%len(corpus2[l2])
		sys.stdout.write(model.wv.most_similar(positive=[ corpus1[l][w], corpus2[l2][w2] ])[0][0])
		sys.stdout.write(" ")
		sys.stdout.flush()
	sys.stdout.write("\n")

