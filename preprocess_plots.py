#!/usr/bin/env python

import json

plots={}
titleStream=open("titles")
plotStream=open("plots")

for title in titleStream.readlines():
    ax=[]
    line=plotStream.readline().strip()
    while(line!="<EOS>"):
        ax.append(line)
        line=plotStream.readline().strip()
    plots[title.strip()]="\n".join(ax)

print(json.dumps(plots))

