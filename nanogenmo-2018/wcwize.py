#!/usr/bin/env python

import sys
from random import Random
random=Random()

for line in sys.stdin.readlines():
    words=line.split()
    while (len(words)>0):
        if(len(words)>1):
            chunked=False
            while not chunked:
                try:
                    chunkLen=random.randint(1, min(3, len(words)-1))
                    chunked=True
                except:
                    pass
            chunk=words[:chunkLen]
            words=words[chunkLen:]
            if len(chunk)==1:
                chunk=chunk[0]
        else:
            chunk=words[0]
            words=[]
        pfx=" "*(random.randint(0, 3)*5)
        print(pfx+((" "*(random.randint(1, 3))).join(chunk)))

