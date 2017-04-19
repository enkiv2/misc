#!/usr/bin/env python

class TumblerAddressException(Exception):
	"""invalid tumbler address"""

class Enfilade:
	""" 
	A model-T style enfilade, supporting tumbler addressing (http://en.wikipedia.org/wiki/Tumbler_(Project_Xanadu)

	A tumbler address is a period-separated sequence of positive integers. Each child and/or value stored in an enfilade 
	is keyed by a single positive integer, so a tumbler address represents a path through the rope in the form of a 
	sequence of indices (or dsps).
	"""
	def __init__(self):
		self.children={}
		self.vals={}
	def getRange(self, start=0, end=-1):
		""" walk all nodes within the range (defaulting to everything), flattening the results """
		childKeys=self.children.keys()
		valKeys=self.vals.keys()
		keys=childKeys+valKeys
		keys.sort()
		if(end<0):
			end=keys[-1]
		ret=[]
		for key in keys:
			if(key>=start and key<=end):
				ret.extend(self.get(key))
		return ret
	def get(self, key):
		ret=[]
		if(key in self.vals):
			ret.extend(self.vals[key])
		if(key in self.children):
			ret.extend(self.children[key].getRange())
		return ret
	def getByTumbler(self, tumbler):
		""" resolve a tumbler address to a flat list of values """
		keySequence=map(int, tumbler.split('.'))
		ret=[]
		i=0
		current=self
		for key in keySequence[:-1]:
			i+=1
			current=current.children
			if(key in current):
				current=current[key]
			else:
				raise TumblerAddressException("No item at tumbler address "+tumbler+"; enfilades run out at "+(".".join(keySequence[:i])))
		return current.get(keySequence[-1])
	def putValue(self, tumbler, value):
		""" set the value at a particular tumbler address, creating intermediate nodes if necessary """
		keySequence=map(int, tumbler.split('.'))
		current=self
		for key in keySequence[:-1]:
			current=current.children
			if not (key in current):
				current[key]=Enfilade()
			current=current[key]
		current.vals[keySequence[-1]]=value
