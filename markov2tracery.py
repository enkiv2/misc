#!/usr/bin/env python

import json
import re

def markov2tracery(s):
    grammar={}
    last="origin"
    
    words=s.split()
    for w in words:
        if(w!=""):
            word=re.sub(r"\W+", "", w).lower()
            key=w+" #"+word+"#"
            if not (last in grammar):
                    grammar[last]=[key]
            else:
                    grammar[last].append(key)
            last=word
    if not (last in grammar):
        grammar[last]=[""]
    else:
        grammar[last].append("")
    return json.dumps(grammar)

if __name__=="__main__":
    import sys
    for line in sys.stdin.readlines():
        print(markov2tracery(line.strip()))

