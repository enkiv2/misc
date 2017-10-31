#!/usr/bin/env python
# -*- coding: utf-8
from random import Random
random=Random()

import json
import sys, re

def sprint(l):
    print(''.join([i if ord(i)<128 else ' ' for i in l]))

plots=json.load(open("plots_preprocessed.json"))


def iterateLine(title, line, seenLines=[]):
    lines=plots[title].split("\n")
    if(len(seenLines)>=len(lines)):
        return
    linePool=range(0, len(lines))
    availableLines=[]
    for item in linePool:
        if not (item in seenLines):
            availableLines.append(item)
    target=random.choice(availableLines)
    if(line>target):
        sys.stdout.write(random.choice(["Earlier", "Before", "Long before", "Not long before", "Not much earlier", "Before that"])+", ")
    else:
        sys.stdout.write(random.choice(["After", "Afterward", "After that", "Much later", "Not much later", "Later"])+", ")
    sprint(lines[target])
    iterateLine(title, target, seenLines+[target])

def iterateLines(title):
    lines=plots[title].split("\n")
    line=random.choice(range(0, len(lines)))
    sprint(lines[line])
    iterateLine(title, line, [line])

title=random.choice(plots.keys())
sprint(title)
print("")
iterateLines(title)

