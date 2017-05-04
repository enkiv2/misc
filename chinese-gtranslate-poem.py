#!/usr/bin/env python
# -*- coding: utf-8

# Automates the generation of the original text side of 
# google translate poems like the ones in this thread:
#  https://twitter.com/metasynthie/status/859743651282509824 
# Uses chinese rather than japanese because random kanji
# should have more interesting meaning than random kana.
# However, it's straightforward to replace the range list
# with character ranges for kana.
# We omit extensions past A because unichr() doesn't like
# unicode characters higher than 0x10k

import codecs
import sys

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

from random import Random
random=Random()

def randCharInRange(start, end):
	rangeLen=end-start
	codePoint=start+random.choice(range(0, rangeLen))
	if(codePoint<255):
		return chr(codePoint)
	return unichr(codePoint)

ranges=[]
ranges.append((0x4e00,0x9fff)) 		# CJK Unified Ideographs 		- common
ranges.append((0x3400,0x4dbf)) 		# CJK Unified Ideographs Extension A 	- rare
#ranges.append((0x20000,0x2a6df)) 	# CJK Unified Ideographs Extension B 	- rare, historic
#ranges.append((0x2a700,0x2b73f)) 	# CJK Unified Ideographs Extension C 	- rare, historic

ax=""
for i in range(0, 10):
	candidates=[]
	for r in ranges:
		candidates.append(randCharInRange(r[0], r[1]))
	ax+=random.choice(candidates)
	print(ax)

