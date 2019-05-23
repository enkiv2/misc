#!/usr/bin/env python

import sys, math

def freq2color(freq):
    #return "#"+("{:06x}".format(int((math.pow(2, 23)-1)*freq)))
    return "#"+("{:02x}".format(int((127+64+32)*freq))*3)
def normdoc(doc):
    return doc.lower().split()
def doc2freqs(doc):
    freqs={}
    maxVal=0
    for word in doc:
        if not word in freqs:
            freqs[word]=doc.count(word)
            if(freqs[word]>maxVal):
                maxVal=freqs[word]
            sys.stderr.write(".")
    sys.stderr.write("\n")
    maxVal=math.log(maxVal)
    for word in freqs:
        if(freqs[word]>1):
            freqs[word]=math.log(freqs[word])/maxVal
        else:
            freqs[word]=0
        sys.stderr.write(".")
    sys.stderr.write("\n")
    return freqs
def fmtdoc(doc, freqs):
    sep=""
    for word in doc.split():
        sys.stderr.write(".")
        sys.stdout.write(sep)
        sep=" "
        if not word.lower() in freqs:
            sys.stdout.write(word)
        else:
            sys.stdout.write("".join(["<font color=\"", freq2color(freqs[word.lower()]), "\">", word, "</font>"]))

lines=sys.stdin.readlines()
sys.stderr.write("{} lines\n".format(len(lines)))
freqs=doc2freqs(normdoc("".join(lines)))
sys.stderr.write("Starting...\n")
sys.stderr.flush()
sys.stdout.write("<html><body>")
for line in lines:
    sep1=""
    for sentence in line.split("."):
        sep2=""
        sys.stdout.write(sep1)
        sep1="."
        for clause in sentence.split(","):
            sys.stdout.write(sep2)
            sep2=","
            fmtdoc(clause, freqs)
    sys.stdout.write("<br>\n")
    sys.stderr.write("\n")
    sys.stderr.flush()
print("</body></html>")

