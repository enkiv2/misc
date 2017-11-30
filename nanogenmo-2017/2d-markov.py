#!/usr/bin/env python

import sys, os
import re

from random import Random
random = Random()

wordMatrix=[]
maxWordsPerLine=0
for line in sys.stdin.readlines():
    wordMatrix.append(re.split(" ", line.strip()))
    if(len(wordMatrix[-1])>maxWordsPerLine):
        maxWordsPerLine=len(wordMatrix[-1])
for line in range(0, len(wordMatrix)):
    if(len(wordMatrix[line])<maxWordsPerLine):
        wordMatrix[line].extend(['']*(maxWordsPerLine-len(wordMatrix[line])))
try:
    import gensim
    model=gensim.models.Word2Vec(wordMatrix)
    gensimMode=True
except:
    gensimMode=False



markov={}
#markov['']={}
#markov['']["left"]=['']
#markov['']["right"]=['']
#markov['']["up"]=['']
#markov['']["down"]=['']
for lineNum in range(0, len(wordMatrix)):
    for wordNum in range(0, len(wordMatrix[lineNum])):
        left=""
        right=""
        up=""
        down=""
        word=wordMatrix[lineNum][wordNum]
        if wordNum>0:
            left=wordMatrix[lineNum][wordNum-1]
        if wordNum<len(wordMatrix[lineNum])-1:
            right=wordMatrix[lineNum][wordNum+1]
        if lineNum>0:
            if len(wordMatrix[lineNum-1])>wordNum:
                up=wordMatrix[lineNum-1][wordNum]
        if lineNum<len(wordMatrix)-1:
            if len(wordMatrix[lineNum+1])>wordNum:
                down=wordMatrix[lineNum+1][wordNum]
        if word in markov:
            markov[word]["left"].append(left)
            markov[word]["right"].append(right)
            markov[word]["up"].append(up)
            markov[word]["down"].append(down)
        else:
            markov[word]={}
            markov[word]["left"]=[left]
            markov[word]["right"]=[right]
            markov[word]["up"]=[up]
            markov[word]["down"]=[down]

width=maxWordsPerLine
height=len(wordMatrix)
outputWordMatrix=[['']*width]*height


startingLine=height/2
startingCol=width/2
word=wordMatrix[startingLine][startingCol]

def setWord(line, col, options):
    try:
        if line<len(outputWordMatrix)-1:
            if col<len(outputWordMatrix[line])-1:
                if(outputWordMatrix[line][col]):
                    w=random.choice(options)
                    if gensimMode and w:
                        try:
                            options.append(outputWordMatrix[line][col])
                            options=[model.most_similar(positive=options)[0][0]]
                            #options=[model.most_similar(positive=[w, options[-1]])[0][0]]
                        except:
                            options=[w, outputWordMatrix[line][col]]
                    else:
                        options=[w, outputWordMatrix[line][col]]
                outputWordMatrix[line][col]=random.choice(options)
    except:
        pass
def setCross(line, col, word):
    setWord(line, col, [word])
    if(line>0):
        setWord(line-1, col, markov[word]["up"])
    if(line<len(outputWordMatrix)-1):
        setWord(line+1, col, markov[word]["down"])
    if(col>0):
        setWord(line, col-1, markov[word]["left"])
    if(line<maxWordsPerLine-1):
        setWord(line, col+1, markov[word]["right"])

outputWordMatrix=wordMatrix
setCross(startingLine, startingCol, word)

for lineNum in range(0, startingLine):
    for wordNum in range(0, startingCol):
        setCross(startingLine-lineNum, startingCol-wordNum, outputWordMatrix[startingLine-lineNum+1][startingCol-wordNum+1])

for lineNum in range(0, startingLine):
    for wordNum in range(startingCol, width):
        setCross(startingLine-lineNum, wordNum, outputWordMatrix[startingLine-lineNum+1][wordNum])

for lineNum in range(startingLine, height):
    for wordNum in range(startingCol, width):
        setCross(lineNum, wordNum, outputWordMatrix[lineNum-1][wordNum-1])

for lineNum in range(startingLine, height):
    for wordNum in range(0, startingCol):
        setCross(lineNum, startingCol-wordNum, outputWordMatrix[lineNum-1][startingCol-wordNum+1])

for line in outputWordMatrix:
    print(" ".join(line))


