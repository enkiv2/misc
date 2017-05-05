#!/usr/bin/env python

import hashlib
import time
from multiprocessing import Pool
import copy

class PageOutException(Exception):
	"""failure in paging out"""
class HashCollisionException(Exception):
	"""hash collision"""

class ChordNode:
	""" Implementation of chord routing, for distributed content-addressible object storage over arbitrary protocol
	Chord routing takes advantage of the fact that, given a fully connected network, any arbitrary stable ordering of nodes &
	objects is sufficient to create a stable route.
	So, we store objects in nodes whose names have similar hashes to those of our objects. We fall back to less well-matched nodes
	in case of failure, but push objects further up the list, while replicating on each node.
	So long as there is some route between any two nodes, this is guaranteed to find objects on it, even with partial peer lists.
	Caching & pushing up the list minimizes the number of hops.
	"""
	def __init__(self, name, sendReq, sendObj, timeout=5, algo=None):
		self.peers=[]
		self.peersByHash={}
		self.name=name		# node ID
		self.sendReq=sendReq	# function to send request
					# three args: peer ID, source ID, hash
		self.sendObj=sendObj	# function to send object
					# three args: peer ID, source ID, object
					# both sendReq and sendObj should return True if successful & False if unsuccessful
		self.timeout=timeout	# default request timeout (seconds)
		if(algo):		# hash algorithm: should produce hex digest
			self.algo=algo
		else:
			def simpleHexSha256(data):
				return hashlib.sha256(data).hexdigest()
			self.algo=simpleHexSha256
		self.mailbox=[]		# requests from other nodes
		self.store={}		# objects keyed by hash
		self.storeRequests={}	# hashes vs requests

	def addPeer(self, peerName):
		if peerName in self.peers:
			return
		self.peers.append(peerName)
		peerHash=self.algo(peerName)
		if(peerHash in self.peersByHash):
			raise HashCollisionException("Hash collison: "+peerHash+" matches both \""+peerName+"\" and \""+self.peersByHash[peerHash]+"\"")
		self.peersByHash[peerHash]=peerName
	def addObj(self, obj):
		key=self.algo(obj)
		if key in self.store:
			if self.store[key]!=obj:
				raise HashCollisionException("Hash collision in store: key="+key)
			return
		self.store[key]=obj
	
	def hashDistance(self, a, b):
		return int(a, 16) - int(b, 16)
	
	def sortByHashSimilarity(self, needle, haystack):
		chunks={}
		for item in haystack:
			delta=self.hashDistance(needle, item)
			if(delta in chunks):
				chunks[delta].append(item)
			else:
				chunks[delta]=[item]
		res=[]
		ck=chunks.keys()
		ck.sort()
		for key in ck:
			res.extend(ck[key])
		return res
	def sendMyObj(self, peer, key):
		return self.sendObj(peer, self.name, self.store[key])
	def sendMyReq(self, peer, key):
		return self.sendReq(peer, self.name, key)
	def incCache(self, key):
		if key in self.storeRequests:
			self.storeRequests[key]+=1
		else:
			self.storeRequests[key]=1
	
	def processRequest(self, source, key):
		returnValue=False
		self.incCache(key)
		if key in self.store:
			self.sendMyObj(source, key)
			returnValue=True
		else:
			peerHashes=self.sortByHashSimilarity(key, self.peersByHash.keys())
			for h in peerHashes:
				peerName=self.peersByHash[h]
				if(peerName==source):
					next
				startTime=time.time()
				if(self.sendMyReq(peerName, key)):
					while not (key in self.store) and (time.time()-startTime < self.timeout):
						yield None
				if(key in self.store):
					self.sendMyObj(source, key)
					for h2 in peerHashes:
						if(h2==h): 
							returnValue=True
							break
						peerName=self.peersByHash[h]
						self.sendMyObj(peerName, key)
					returnValue=True
					break
		yield returnValue

	def processRequests(self, poolsize=5):
		mailbox=copy.deepcopy(self.mailbox)
		self.mailbox=self.mailbox[:len(mailbox)]
		p=Pool(poolsize)
		def handleReq(x):
			req=self.processRequest(*x)
			ret=req.next()
			while(ret==None):
				ret=req.next()
			if(ret==False):
				return x
			else:
				return False
		resume=p.map(handleReq, mailbox)
		for i in range(0, len(resume)):
			if(i):
				# retry failures
				self.mailbox.append(i)
		

	def pageOut(self, key, replications):
		peerHashes=self.sortByHashSimilarity(key, self.peersByHash.keys())
		ret=True
		i=0
		for h in peerHashes:
			if not ret:
				return False
			if(i>replications):
				break
			ret=self.sendMyObj(peerName, key)
			if(ret):
				i+=1
		if(ret):
			del self.store[key]
			if key in self.storeRequests:
				del self.storeRequests[key]
		return ret
		
	def goOffline(self, replications=3):
		failure=False
		for key in self.store.keys():
			if not(self.pageOut(key, replications)):
				failure=True
		if(failure):
			raise PageOutException("Could not page out: peers unreachable")

	def collectGarbage(self, maxItems, minCount=0, replications=3):
		if(maxItems):
			if(len(self.store.keys())<maxItems):
				return True
		else:
			maxItems=len(self.store.keys())+1
		itemsByCount={}
		for key in self.store.keys():
			if(key in self.storeRequests):
				count=self.storeRequests[key]
				if(count>=minCount):
					if count in itemsByCount:
						itemsByCount[count].append(key)
					else:
						itemsByCount[count]=[key]
			else:
				if(minCount==0):
					if(0 in itemsByCount):
						itemsByCount[0].append(key)
					else:
						itemsByCount[0]=[key]
		counts=itemsByCount.keys()
		counts.sort(reverse=True)
		i=0
		for c in counts:
			if(i>maxItems):
				break
			chunk=itemsByCount[c]
			i+=len(chunk)
			if(i>maxItems):
				chunk=chunk[:len(chunk)-(i-maxItems)]
			for key in chunk:
				if not(self.pageOut(key, replications)):
					i-=1
		
