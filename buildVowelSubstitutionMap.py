#!/usr/bin/env python
import json

import sys

words=[]
words2=[]
wordMap={}

vowels=['a', 'e', 'i', 'o', 'u']

sep=""

for line in sys.stdin.readlines():
	line=line.strip().lower()
	words.append(line)

with open(sys.argv[1], 'r') as f:
	for line in f.readlines():
		words2.append(line.strip().lower())

print("{")
for word in words2:
	for vowel in vowels:
		count=word.count(vowel)
		if(count>0):
			matches=[]
			last=0
			for i in range(0, count):
				idx=word.find(vowel, last)
				front=word[:idx]
				back=word[idx+1:]
				last=idx
				for vowel2 in vowels:
					if(vowel!=vowel2):
						temp=front+vowel2+back
						if(temp in words):
							matches.append(temp)
			if(len(matches)>0):
				wordMap[word]=matches
				print("".join([sep, "\"", word, "\":[\"", "\",\"".join(matches), "\"]"]))
				sep=","
				sys.stdout.flush()

print("}")
