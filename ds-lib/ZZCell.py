#!/usr/bin/env python

# LEGAL NOTE:
# While I have written ZigZag implementations officially for Project Xanadu(tm), 
# this implementation shares no code with those. This code contains no material
# under trade secret protection related to Project Xanadu(tm).
#
# Please refer to a collection of these objects as a ZZStructure, rather than
# ZigZag(tm).
#
# It is the opinion of the author that this does not replicate any features of
# ZigZag(tm) that are under patent protection or covered by patent applications
# still in the pipeline.

cellCount=0

class ZZCell:
	"""
	A ZZStructure is a group of "cells" connected along "dimensions".
	
	Each cell has an optional value.
	
	A cell can be connected to another cell along a given dimension 
	in either the negward or posward direction. A cell can have 
	a maximum of one connection with a given dimension & direction.
	If cell A is connected poswardly on dimension d.foo to cell B,
	then cell B is connected negwardly on dimension d.foo to cell A.
	
	Dimensions are arbitrary strings. By convention, they have two
	parts separated by a dot: a namespace followed by a name. The
	default namespace is 'd'.
	
	A rank is the set of all cells connected along a given dimension.
	(A ring-rank is a rank that is a circle.)
	
	Cells can be cloned. A clone's value is the same as the original,
	but its connections may be different. A clone has its original
	as the first item in its rank along dimension 'd.clone'
	"""
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
	def interpolate(self, dim, val, pos=True, ttl=1000):
		""" interpolate two ranks """
		if(ttl==0):
			return		# ring ranks may cause infinite recursion
		if(dim in self.connections[pos]):
			temp=self.connections[pos][dim]
			self.setNext(dim, val, pos)
			val.interpolate(temp, val, pos, ttl-1)
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
			if(n==self):
				break	# handle ringranks
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

