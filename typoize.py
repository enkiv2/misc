#!/usr/bin/env python

from random import Random
random=Random()

def letterSwap(s, i, j):
	pre=s[:i]
	post=s[j+1:]
	mid=s[i+1:j-1]
	return pre+s[j]+mid+s[i]+post

def typoize(s, rate=5):
	global random
	ret=[]
	words=s.split()
	for w in words:
		word=w
		for i in range(0, len(word)-2):
			if(random.choice(range(0,100))<rate):
				word=letterSwap(word, i, i+1)
		ret.append(word)
	return " ".join(ret)



if __name__=="__main__":
	import sys
	for line in sys.stdin.readlines():
		print(typoize(line, int(sys.argv[1])))

			
