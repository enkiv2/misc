#!/usr/bin/env python

class TumblerAddressException(Exception):
	"""invalid tumbler address"""

class Enfilade:
	def __init__(self):
		self.children={}
		self.vals={}
	def getRange(self, start=0, end=-1):
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
		keySequence=tumbler.split('.')
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
		keySequence=tumbler.split('.')
		current=self
		for key in keySequence[:-1]:
			current=current.children
			if not (key in current):
				current[key]=Enfilade()
			current=current[key]
		current.vals[keySequence[-1]]=value
