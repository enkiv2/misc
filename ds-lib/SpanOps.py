#!/usr/bin/env python

""" span is ordered pair (start, length) """

def nonOverlap(a, b):
	""" return a list of spans corresponding to parts of a that do not overlap with b """
	if(a==b):
		return []
	tmp=overlap(a, b)
	if(tmp==None):
		return [a, b]
	aEnd=a[0]+a[1]
	bEnd=b[0]+b[1]
	if(a[0]>b[0] and aEnd<bEnd):
		return []
	ret=[]
	if aEnd>bEnd:
		ret.append((bEnd, aEnd-bEnd))
	if b[0]>a[0]:
		ret.append((a[0], b[0]-a[0]))
	return ret

def overlap(a, b):
	""" return the portion of a that overlaps with b """
	aEnd=a[0]+a[1]
	bEnd=b[0]+b[1]
	if a[0]>b[0] and aEnd>b[0]:
		return None
	if b[0]>a[0] and bEnd>a[0]:
		return None
	if(a[0]>b[0]):
		if aEnd>bEnd:
			return (a[0], bEnd-a[0])
		else:
			return (a[0], a[1])
	if(aEnd>bEnd):
		return (b[0], b[1])
	else:
		return (b[0], aEnd-b[0])

def sort(spanlist):
	items={}
	for span in spanlist:
		if span[0] in spanlist:
			spanlist[span[0]].append(span[1])
		else:
			spanlist[span[0]]=[span[1]]
	ret=[]
	keys=items.keys()
	keys.sort()
	for s in keys:
		ends=items[s]
		ends.sort(reverse=True)
		for e in ends:
			ret.append((s, e))
	return ret

def lint(spanlist):
	""" sloppy greedy merge; not guaranteed to create optimal merge """
	spanlist=sort(spanlist)
	ret=[]
	curr=spanlist[0]
	i=1
	while(i<len(spanlist)):
		o=overlap(curr, spanlist[i])
		if(o==None):
			ret.append(curr)
			curr=spanlist[i]
		else:
			n=nonOverlap(curr, spanlist[i])
			if(len(n)>0):
				ret.extend(n)
		i+=1
	return ret

def pageList(spanlist, cachedSpans):
	""" given a list of spans requested & a list of already-cached spans, produce a list of spans we should page in """
	spanlist=lint(spanlist)
	cachedSpans=lint(cachedSpans)
	ret=[]
	for span in spanlist:
		for span2 in cachedSpans:
			if(overlap(span, span2)):
				ret.extend(nonOverlap(span, span2))
	return lint(ret)

def concatextIdx2SpanIdx(threespans, idx):
	""" 
	a threespan is a tuple of form (source, start, length);
	a concatext is a document made by concatenating a series of spans from different sources
	
	this function takes the threespans representing the concatext & an index into it, and
	returns an index into an individual source document in the form of a zero-length threespan
	"""
	ax=0
	for tsp in threespans:
		i=ax+tsp[2]
		if(i==idx):
			return (tsp[0], tsp[1]+tsp[2], 0)
		if(i>idx):
			delta=tsp[2]-(i-idx)
			return (tsp[0], tsp[1]+delta, 0)
		ax=i
	return None

			
