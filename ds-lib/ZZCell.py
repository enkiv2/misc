#!/usr/bin/env python

cellCount=0

class ZZCell:
	def __init__(self, value=None):
		global cellCount
		self.cid=cellCount
		cellCount+=1
		self.value=value
		self.connections={}
		self.connections[True]={}
		self.connections[False]={}
	def getNext(self, dim, pos=True):
		if dim in self.connections[pos]:
			return self.connections[pos]
		return None
	def setNext(self, dim, val, pos=True):
		self.connections[pos][dim]=val
		val.connections[not pos][dim]=self
	def insert(self, dim, val, pos=True):
		""" like setNext, except it will repair exactly one connection """
		if(dim in self.connections[pos]):
			temp=self.connections[pos][dim]
			self.setNext(dim, val, pos)
			val.setNext(temp, val, pos)
		else:
			self.setNext(dim, val, pos)
	def interpolate(self, dim, val, pos=True):
		""" interpolate two ranks """
		if(dim in self.connections[pos]):
			temp=self.connections[pos][dim]
			self.setNext(dim, val, pos)
			val.interpolate(temp, val, pos)
		else:
			self.setNext(dim, val, pos)
	def breakConnection(self, dim, pos=True):
		if self.getNext(dim, pos):
			temp=self.connections[pos][dim]
			temp.connections[not pos][dim]=None
			self.connections[pos][dim]=None
	def hop(self, dim, pos=True):
		""" hop this cell over the next one in the rank, if it exists """
		temp=self.getNext(dim, pos)
		if(temp):
			self.breakConnection(dim, pos)
			temp.interpolate(dim, self, not pos)
	def rankHead(self, dim, pos=False):
		""" Get the head (or tail) of a rank """
		curr=self
		n=curr.getNext(dim, pos)
		while(n):
			curr=n
			n=curr.getNext(dim, pos)
		return curr
	def cloneHead(self):
		return self.rankHead("d.clone")
	def getValue(self):
		""" get cell's value. Use this, rather than the value attribute, unless you specifically don't want to handle clones """
		return self.cloneHead().value
	def clone(self):
		""" create a clone """
		c=ZZCell()
		self.rankHead("d.clone", True).setNext("d.clone", c)
		return c
	def getDims(self):
		return list(set(self.connections[True].keys() + self.connections[False].keys()))

