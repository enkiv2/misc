#!/usr/bin/env python
import sys

words1=[]
words2=[]
with open(sys.argv[1], 'r') as f:
		words1=("".join(f.readlines())).split()
with open(sys.argv[2], 'r') as f:
		words2=("".join(f.readlines())).split()

while len(words1)>len(words2):
		words2+=words2

i=0
with open(sys.argv[1], 'r') as f:
		for line in f.readlines():
				while i<len(words1) and line.find(words1[i])>=0:
						w1=words1[i]
						w2=words2[i]
						idx=line.find(w1)
						if idx>0:
								sys.stdout.write(line[:idx])
						line=line[idx+len(w1):]
						sys.stdout.write(w1[:int(len(w1)/2.0+0.5)]+w2[int(len(w2)/2.0):])
						i+=1
				sys.stdout.write(line)
				sys.stdout.flush()


