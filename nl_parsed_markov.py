#!/usr/bin/env python

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.parse.pchart import LongestChartParser
from nltk.tree.tree import Tree
from nltk.corpus import treebank
from soundex import Soundex
from random import Random

soundex=Soundex().soundex
random=Random()

#parser=LongestChartParser()
def tokens2parsetrees(tokens, max_trees=-1):
		ret=[]
		i=0
		for pt in parser.parse(tokens):
				if max_trees >= 0 and i >= max_trees:
						continue
				ret.append(pt)
		return ret

def sentence2parsetrees(sentence, max_trees=-1):
		return tokens2parsetrees(word_tokenize(sentence), max_trees)

brain={}
soundex_lookup={}
serialization_lookup={}
class myParseTree:
		def __init__(self, pos=None, children=[], nextItem=None, lastItem=None, probability=1, pt=None):
				if lastItem:
						lastItem.setNext(self)
				self.children=children
				self.soundexes=[]
				self.soundex_processed = False
				self.pos=pos
				self.next=nextItem
				self.last=lastItem
				self.probability=1
				if pt:
						self.convertFromNLTKParseTree(pt)
		def setNext(self, nextItem):
				self.next=nextItem
		def convertFromNLTKParseTree(self, pt):
				self.pos=pt.label()
				self.children=[]
				last=None
				for child in pt:
						if isinstance(child, Tree):
								self.children.append(myParseTree(pt=child, lastItem=last, probability=self.probability))
						else:
								self.children.append(child)
						last=self.children[-1]
				if self.children and isinstance(self.children[0], myParseTree):
						self.children[0].last=self

		def lint_soundex_lookup(self):
				keys=list(soundex_lookup.keys())
				for k in keys:
						l=soundex_lookup[k]
						lkeys=list(l.keys())
						for kk in lkeys:
								if l[kk]<=0:
										del l[kk]
						if len(l)==0:
								del soundex_lookup[k]

		def unprocess_soundex(self):
				if not self.soundex_processed:
						return
				i=0
				for child in self.children:
						if isinstance(child, myParseTree):
								child.unprocess_soundex()
						else:
								ch=str(child)
								sx=self.soundexes[i]
								soundex_lookup[sx][ch]-=self.probability
				self.soundexes=[]
				self.soundex_processed=False

		def process_soundex(self):
				if self.soundex_processed:
						return
				self.soundexes=[]
				i=0
				for child in self.children:
						if isinstance(child, myParseTree):
								child.process_soundex()
								self.soundexes.append(None)
						else:
								ch=str(child)
								sx=soundex(ch)
								soundex_lookup[sx]=soundex_lookup.get(sx, {})
								soundex_lookup[sx][ch]=soundex_lookup[sx].get(ch, 0)+self.probability
								self.soundexes.append(sx)
						i+=1
				self.soundex_processed=True
		def process_serialization_lookup(self):
				r=repr(self)
				s=self.serialize(True)
				serialization_lookup[r]=serialization_lookup.get(r, {})
				serialization_lookup[r][s]=serialization_lookup[r].get(s, 0)+self.probability
				for child in self.children:
						if isinstance(child, myParseTree):
								child.process_serialization_lookup()
				

		def _repr(self, pretty=False):
				sep=" "
				if pretty:
						sep="\n\t"
				child_reps=[]
				i=0
				for child in self.children:
						if isinstance(child, myParseTree):
								child_reps.append(repr(child))
						else:
								child_reps.append(self.soundexes[i])
						i+=1
				return f"({self.pos} {sep.join(child_reps)})"
		def __repr__(self):
				return self._repr()
		def __str__(self):
				return self._repr(True)
		def reprs(self, flatten=False):
				ret=[repr(self)]
				for child in self.children:
						if isinstance(child, myParseTree):
								ret.extend(child.reprs())
				return ret
		def serialize(self, toplevel=False):
				items=[]
				for child in self.children:
						if isinstance(child, myParseTree):
								items.extend(child.serialize())
						else:
								items.append(child)
				if toplevel:
						items=' '.join(items)
				return items

		def clean_children(self):
				ret=[]
				for child in self.children:
						if isinstance(child, myParseTree):
								ret.append(child)
				return ret

		def firsts(self):
				ret=[]
				children=self.clean_children()
				if children:
						ret.append(children[0])
						ret.extend(children[0].firsts())
				return ret

		def lasts(self):
				ret=[]
				children=self.clean_children()
				if children:
						ret.append(children[-1])
						ret.extend(children[-1].lasts())
				return ret
		def update_brain(self, p, q):
				brain[p]=brain.get(p, {})
				brain[p][q]=brain[p].get(q, 0)+self.probability
		def markov_ingest(self):
				q=''
				if self.next:
						q=repr(self.next)
				self.update_brain(repr(self), q)
				for child in self.lasts():
						self.update_brain(repr(child), q)
						if self.next:
								for q in self.next.firsts():
										self.update_brain(repr(child), repr(q))
				q=''
				if self.last:
						q=repr(self.last)
				self.update_brain(q, repr(self))
				for child in self.firsts():
						self.update_brain(q, repr(child))
						if self.last:
								for q in self.last.lasts():
										self.update_brain(repr(q), repr(child))
						

def weighted_random(structure):
		total=0
		for k, v in structure.items():
				total+=v
		target=random.uniform(0, total)
		ax=0
		for k, v in structure.items():
				ax+=v
				if ax>=target:
						return k


def markov_next(s):
		candidates=brain.get(s, {})
		selected=weighted_random(candidates)
		return selected

def markov_chain(s=''):
		n=markov_next(s)
		if n:
				return [n]+markov_chain(n)
		return []

def reconstruct_chain(chain):
		ret=[]
		for c in chain:
				ret.append(weighted_random(serialization_lookup[c]))
		return ' '.join(ret)


last=None
trees=[]
for t in treebank.parsed_sents():
	pt=myParseTree(pt=t)
	pt.process_soundex()
	pt.process_serialization_lookup()
	pt.markov_ingest()

	pt=myParseTree(pt=t, lastItem=last)
	pt.process_soundex()
	pt.markov_ingest()
	last=pt
	trees.append(pt)
#	print(pt.serialize(True))
pt=myParseTree(children=trees)
pt.process_soundex()
pt.process_serialization_lookup()
pt.markov_ingest()
print()
print(reconstruct_chain(markov_chain()))
print(reconstruct_chain(markov_chain()))
print(reconstruct_chain(markov_chain()))

