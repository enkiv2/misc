#!/usr/bin/env python

MAX_RESULT_LENGTH=400	# IRC limits total message length to 510 characters, including hostname and user. Hostname limits to 63 characters. If user maxes out at 9 chars, this leaves an upper limit of 405 characters.
MAX_MARKOV_LEVEL=5

replyrate=100
replyrate=0

wordTotal=0
wordFrequencies={}
lineList={}		# first level idx is source
lineScores={}		# first level idx is source; parallel with lineList
nextLines={}		# first level idx is one of ["first", "last", "min", "max", "avg", "avg2"]
nextPhrases={}		# first level idx is one of ["first", "last", "min", "max", "avg", "avg2"]
nextWords=[]		# index n is (n-1) order markov model

from random import Random
random=Random()
import sys, os, string, json
try:
	import cPickle
	pickle=cPickle
except:
	sys.stderr.write("Could not import cPickle; falling back to pickle.\n")
	import pickle

from eliza import elizaResponse

def initialize():
	global nextLines, nextPhrases, nextWords
	if(len(nextWords)<MAX_MARKOV_LEVEL):
		for i in range(len(nextWords), MAX_MARKOV_LEVEL):
			nextWords.append({})
	for i in ["first", "last", "min", "max", "avg", "avg2"]:
		if not (i in nextLines):
			nextLines[i]={}
			nextLines[i][""]=[""]
		if not (i in nextPhrases):
			nextPhrases[i]={}
			nextPhrases[i][""]=[""]

def save():
	state={}
	state["wordTotal"]=wordTotal
	state["wordFrequencies"]=wordFrequencies
	state["lineList"]=lineList
	state["nextWords"]=nextWords
	# We do not load or save nextLines or nextPhrases because we should regenerate these on reload
	f=open("yabot_state.pickle.part", "w")
	pickle.dump(state, f)
	f.close()
	os.rename("yabot_state.pickle.part", "yabot_state.pickle")
	regenerateLineHandling()

def load():
	global wordTotal, wordFrequencies, lineList, nextWords
	try:
		f=open("yabot_state.pickle", "r")
		state=pickle.load(f)
		wordTotal=state["wordTotal"]
		wordFrequencies=state["wordFrequencies"]
		lineList=state["lineList"]
		nextWords=state["nextWords"]
	except:
		sys.stderr.write("Could not load 'yabot_state.pickle'. Initializing it...")
		save()
		sys.stderr.write(" done!\n")
	initialize()
	regenerateLineHandling()

def processWords(phrase):
	global wordFrequencies, nextWords, wordTotal
	phraseWords=phrase.lower().split()
	wordTotal+=len(phraseWords)
	if(len(nextWords)<MAX_MARKOV_LEVEL):
		for i in range(len(nextWords)-1, MAX_MARKOV_LEVEL):
			nextWords.append({})
	oldW=[""]*MAX_MARKOV_LEVEL
	phraseWords.append("")
	for w in phraseWords:
		if not (w in wordFrequencies):
			wordFrequencies[w]=1
		else:
			wordFrequencies[w]+=1
		for i in range(0, MAX_MARKOV_LEVEL):
			old=oldW[i]
			if not (old in nextWords[i]):
				nextWords[i][old]={}
			if not (w in nextWords[i][old]):
				nextWords[i][old][w]=1
			else:
				nextWords[i][old][w]+=1
		oldW.append(w)
		oldW.pop(0)

def score(mode, phrase):
	phraseWords=phrase.lower().split()
	if(len(phraseWords)<1):
		return ""
	if mode=="first":
		return phraseWords[0]
	elif mode=="last":
		return phraseWords[-1]
	elif mode=="avg2":
		avg=(1.0*wordTotal)/len(wordFrequencies)
		minI=pow(2, 9); minW=""
		for w in phraseWords:
			count=0
			if(w in wordFrequencies):
				count=wordFrequencies[w]
			delta=abs(count-avg)
			if(delta<minI):
				minI=delta; minW=w
		return minW
	else:
		minI=pow(2,9); minW=""
		maxI=0       ; maxW=""
		ax=0
		for w in phraseWords:
			count=0
			if(w in wordFrequencies):
				count=wordFrequencies[w]
			if(count<minI):
				minI=count; minW=w
			if(count>maxI):
				maxI=count; maxW=w
			ax+=count
		if(mode=="min"):
			return minW
		elif(mode=="max"):
			return maxW
		ax=(1.0*ax)/len(phraseWords)
		minI=pow(2, 9); minW=""
		for w in phraseWords:
			count=0
			if(w in wordFrequencies):
				count=wordFrequencies[w]
			delta=abs(count-ax)
			if(minI<delta):
				minI=delta; minW=w
		return minW

def scoreMulti(phrase):
	state={}
	state["first"]=""; state["last"]=""; state["avg2"]=""
	state["min"]=""; state["max"]=""; state["avg"]=""
	phraseWords=phrase.lower().split()
	if(len(phraseWords)<1):
		return state
	state["first"]=phraseWords[0]
	state["last"]=phraseWords[-1]
	
	ax=0
	avg=(1.0*wordTotal)/len(wordFrequencies)
	minI=pow(2,9);  minW=""
	maxI=0;         maxW=""
	deltaG=pow(2,9);deltaGW=""
	deltaL=pow(2,9);deltaLW=""
	for w in phraseWords:
		count=0
		if(w in wordFrequencies):
			count=wordFrequencies[w]
		ax+=count
		delta=abs(count-avg)
		if(delta<deltaG):
			deltaG=delta
			deltaGW=w
		if(minI<count):
			minI=count
			minW=w
		if(maxI>count):
			maxI=count
			maxW=w
	ax=(1.0*ax)/len(phraseWords)
	state["avg2"]=deltaGW
	state["min"]=minW
	state["max"]=maxW
	for w in phraseWords:
		count=0
		if(w in wordFrequencies):
			count=wordFrequencies[w]
		delta=abs(count-ax)
		if(delta<deltaL):
			deltaL=delta
			deltaLW=w
	state["avg"]=deltaLW
	return state

def processLine(source, line, regen=False):
	global lineList, nextLines, lineScores, nextPhrases
	if(not regen):
		processWords(line)
	if not (source in lineList) or not (source in lineScores):
		lineScores[source]=[scoreMulti("")]
		lineList[source]=[""]
	lineScore=scoreMulti(line)
	lineList[source].append(line)
	lineScores[source].append(lineScore)
	phrases=line.split(".")
	phraseScores=[scoreMulti("")]
	for phrase in phrases:
		phraseScores.append(scoreMulti(phrase+"."))
	for mode in ["first", "last", "avg2", "min", "max", "avg"]:
		lineClass=""
		if(len(lineScores)>1):
			lineClass=lineScores[-2][mode]
		if not (lineClass in nextLines[mode]):
			nextLines[mode][lineClass]=[line]
		else:
			nextLines[mode][lineClass].append(line)
		for i in range(0, len(phrases)):
			if not (phraseScores[i][mode] in nextPhrases[mode]):
				nextPhrases[mode][phraseScores[i][mode]]=[phrases[i]]
			else:
				nextPhrases[mode][phraseScores[i][mode]].append(phrases[i])

def regenerateLineHandlingForSrc(source):
	global lineList, lineScores
	lines=[]
	if source in lineList:
		lines=lineList[source]
	lineList[source]=[]
	lineScores[source]=[]
	for line in lines:
		processLine(source, line, True)
def regenerateLineHandling():
	sources=lineList.keys()
	nextLines={}
	nextPhrases={}
	initialize()
	for source in sources:
		regenerateLineHandlingForSrc(source)
	

def traverseMarkov(seed, level):
	ret=[]
	if(level>MAX_MARKOV_LEVEL):
		level=MAX_MARKOV_LEVEL
	if(level>len(nextWords)):
		level=len(nextWords)
	if not (seed in nextWords[level-1]):
		seed=""
	if(seed==""):
		return ""	# hard mode
	old=([""]*(level-1))
	old.append(seed)
	if(len(old)>1):
		old.pop(0)
	done=False
	while not done:
		candidates=[]
		for i in range(0, level):
			if old[-i] in nextWords[i]:
				for j in range(0, level-i):
					candidates.extend(nextWords[i][old[-i]])
		if(len(candidates)==0):
			done=True
			choice=""
		else:
			choice=random.choice(candidates)
		if(choice==""):
			done=True
		else:
			ret.append(choice)
			old.append(choice)
			old.pop(0)
			if(len(" ".join(ret))>MAX_RESULT_LENGTH):
				return " ".join(ret[:-1])+"..."
	return " ".join(ret)

def traversePhrases(seed, mode):
	ret=[]
	if not seed in nextPhrases[mode]:
		seed=""
	if(seed==""):
		return ""	# hard mode
	done=False
	while not done:
		choice=random.choice(nextPhrases[mode][seed])
		seed=score(mode, choice)
		if not (seed in nextPhrases[mode]):
			ret.append("..")
			done=True
		if(choice==""):
			done=True
		else:
			ret.append(choice)
			if(len(". ".join(ret))>MAX_RESULT_LENGTH):
				if(len(ret)==1):
					return ""
				else:
					return ". ".join(ret[:-1])+"..."
	return ". ".join(ret)

def traverseLines(seed, mode):
	if not seed in nextLines[mode]:
		seed=""
	if(seed==""):
		return ""	# hard mode
	return random.choice(nextLines[mode][seed])

def respondLine(line):
	sys.stderr.write("\n\nInput: \""+line+"\"\n")
	candidates=[]
	candidates.append(elizaResponse(line))
	markovCandidates2=[]
	for mode in ["min", "max", "first", "last", "avg", "avg2"]:
		lineClass=score(mode, line)
		markovCandidates=[]
		for level in range(0, MAX_MARKOV_LEVEL):
			seed=score("first", traverseLines(lineClass, mode))
			if not seed:
				seed=lineClass
			markovCandidates.append(traverseMarkov(seed, level+1))
		sys.stderr.write("Markov candidates: \""+("\",\"".join(markovCandidates))+"\"\n")
		markovCandidates2.append(random.choice(markovCandidates))
		candidates.append(traversePhrases(lineClass, mode))
		candidates.append(traverseLines(lineClass, mode))
	candidates.append(random.choice(markovCandidates2))
	sys.stderr.write("\nCandidates: \""+("\",\"".join(candidates))+"\"\n\n\n")
	return random.choice(candidates)

def handleCmd(source, line):
	chunks=line.split()
	if(chunks[0]=="!save"):
		save()
		return "Saved."
	return ""

def handleLine(source, line):
	if(len(line)>0):
		if(line[0]=="!"):
			return handleCmd(source, line)
		else:
			processLine(source, line)
			if(replyrate and random.choice(range(0, replyrate))==0):
				return respondLine(line)
			return ""

def main():
	load()
	initialize()
	try:
		line=raw_input("> ")
		while(line!="!quit"):
			resp=handleLine("stdin", line)
			if(resp):
				print(resp)
			line=raw_input("> ")
	except EOFError:
		pass
	save()
if __name__=="__main__":
	main()

