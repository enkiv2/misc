#!/usr/bin/env python

from datetime import date
import re, os, os.path, sys

import tkinter, tkinter.ttk

def dprint(s):
		sys.stderr.write(s+"\n")
		sys.stderr.flush()
try:
		import cPickle as pickle
except:
		dprint("cPickle does not exist; falling back to pickle")
		import pickle

nonLowerPat=re.compile("[^a-z]+")
HOME=os.path.expanduser("~")+"/.stak/"
if not os.path.exists(HOME):
		os.makedirs(HOME)

class card:
		def __init__(self, cid, note="", tags=[]):
				self.note=note
				self.tags=[]
				self.cid=cid
				self.date=date.now()

class stack:
		def __init__(self):
				self.maxCid=0
				self.cards=[]
				self.cardsByTag={}
				self.cardsByTerm={}
				self.termFrequencies={}
				self.lastFetched=[]
				self.maxResident=100
				self.dirty={}
		def searchByTag(self, tag):
				ret=list(set(self.cardsByTag.get(tag, [])))
				ret.sort()
				return ret
		def searchByTerms(self, terms):
				tf={}
				df={}
				for term in terms:
						for card in self.cardsByTerm.get(term,[])+self.cardsByTag.get(term,[]):
								tf[card]=tf.get(card,0)+self.termFrequencies.get(term, 0)
								df[card]=df.get(card,0)+1
				tfidfs={}
				for card in tf:
						tfidf=int((10000.0*tf[card])/df[card])
						tfidfs[tfidf]=tfidfs.get(tfidf, [])+[card]
				tfidf_keys=list(tfidfs.keys())
				tfidf_keys.sort()
				ret=[]
				for k in tfidf_keys:
						ret+=tfidfs[k]
				return ret
		def normalizeNoteForIndexing(self, note):
				return re.sub(nonLowerPat, " ", note.lower()).split()
		def registerCard(self, card):
				cid=card.cid
				for tag in card.tags:
						self.cardsByTag[tag]=self.cardsByTag.get(tag, [])+[cid]
						self.cardsByTerm[tag]=self.cardsByTerm.get(tag, [])+[cid]
						self.termFrequencies[tag]=self.termFrequencies.get(tag, 0)+1
				for term in self.normalizeNoteForIndexing(card.note):
						self.cardsByTag[term]=self.cardsByTag.get(term, [])+[cid]
						self.cardsByTerm[term]=self.cardsByTerm.get(term, [])+[cid]
						self.termFrequencies[term]=self.termFrequencies.get(term, 0)+1
		def addCard(self, note, tags):
				c=card(len(self.cards), note, tags)
				self.cards.append(c) ; self.maxCid=len(self.cards)
				self.registerCard[c]
				self.dirty[c.cid]=True
		def loadCard(self, cid):
				cidName=str(cid)
				cidPath=HOME+"cards/"+(cidName[-1])+"/"+cidName+".pickle"
				with open(cidPath) as f:
						self.cards[cid]=pickle.load(f)
						self.dirty[cid]=False
		def saveCard(self, cid):
				cidName=str(cid)
				cidPath=HOME+"cards/"+(cidName[-1])+"/"
				os.makedirs(cidPath)
				cidPath+=cidName+".pickle"
				with open(cidPath, "w") as f:
						pickle.dump(self.cards[cid], f)
						self.dirty[cid]=False
		def gcCard(self, cid):
				if self.cards[cid]!=None:
						if self.dirty[cid]:
								self.saveCard(cid)
						self.cards[cid]=None
		def stackGc(self):
				if len(self.lastFetched)>self.maxResident:
						self.lastFetched=self.lastFetched[-self.maxResident:]
				keep=list(set(self.lastFetched))
				for cid in range(0, len(self.cards)):
						if not cid in keep:
								gcCard(cid)
		def makeCardsResident(self, cids):
				for cid in cids:
						if None==self.cards[cid]:
								self.loadCard(cid)
		def getCards(self, cids):
				self.lastFetched.extend(cids)
				if len(self.lastFetched)>self.maxResident:
						self.lastFetched=self.lastFetched[-self.maxResident:]
				self.makeCardsResident(cids)
				ret=[]
				for cid in cids:
						ret.append(self.cards[cid])
				return ret
		def reindex(self):
				self.cardsByTag={}
				self.cardsByTerm={}
				self.termFrequencies={}
				self.makeCardsResident(range(0, len(self.cards)))
				for card in self.cards:
						self.registerCard(card)
				self.saveIndex()
		def loadIndex(self):
				idxPath=HOME+"/idx.pickle"
				with open(idxPath) as f:
						(self.maxCid, self.cardsByTag, self.cardsByTerm, self.termFrequencies)=pickle.load(f)
		def saveIndex(self):
				idxPath=HOME+"/idx.pickle"
				with open(idxPath, "w") as f:
						pickle.dump((self.maxCid, self.cardsByTag, self.cardsByTerm, self.termFrequencies), f)
		def saveState(self):
				self.saveIndex()
				tmp=self.lastFetched
				self.lastFetched=[]
				self.stackGc()
				self.lastFetched=tmp
				self.makeCardsResident(list(set(tmp)))


myStack=stack()
try:
		myStack.loadIndex()
except:
		myStack.saveState()

