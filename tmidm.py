#!/usr/bin/env python3

# Term Markov Inverse Document Markov

import sys
from random import Random
random=Random()

def train(files):
    docs=[]
    background={}
    composite={}
    occurrence={}

    for doc in files:
        docModel={}
        corpus=" ".join(open(doc, 'r').readlines())
        corpus.lower()
        words=corpus.split()
        words.append("")
        lastWord=""
        for word in words:
            if not (lastWord in docModel):
                docModel[lastWord]={}
            if not (word in docModel[lastWord]):
                docModel[lastWord][word]=0
            if not (lastWord in background):
                background[lastWord]={}
            if not (word in background[lastWord]):
                background[lastWord][word]=0
            docModel[lastWord][word]+=1
            background[lastWord][word]+=1
            lastWord=word
        docs.append(docModel)
        sys.stderr.write(".")
    sys.stderr.write("\n")
    for doc in docs:
        for word1 in doc.keys():
            for word2 in doc[word1].keys():
                doc[word1][word2]=(len(docs)*100.0*doc[word1][word2])/(background[word1][word2])
                if not (word1 in composite):
                    composite[word1]={}
                if not (word2 in composite[word1]):
                    composite[word1][word2]=0
                if not (word1 in occurrence):
                    occurrence[word1]={}
                if not (word2 in occurrence[word1]):
                    occurrence[word1][word2]=0
                composite[word1][word2]+=doc[word1][word2]
                occurrence[word1][word2]+=1
        sys.stderr.write(".")
    sys.stderr.write("\n")
    del docs
    del background
    for word1 in composite.keys():
        for word2 in composite[word1].keys():
            composite[word1][word2]/=(1.0*occurrence[word1][word2])
    del occurrence
    return composite

def chainNext(composite, start):
    options=composite[start]
    opts=list(options.keys())
    item=random.choices(opts, map(lambda x: options[x], opts))[0]
    return item

def chain(composite, start):
    ret=[]
    sys.stdout.write(start)
    sys.stdout.write(" ")
    item=chainNext(composite, start)
    while(item!=""):
        sys.stdout.write(item)
        sys.stdout.write(" ")
        sys.stdout.flush()
        item=chainNext(composite, item)

def main():
    composite=train(sys.argv[1:])
    chain(composite, "")

if __name__=="__main__":
    main()

