#!/usr/bin/env python

from pyquery import PyQuery
import json

global res
res=[]

def grabber(i=0):
    global res
    base_url = "http://principiadiscordia.com/memebombs/"
    url = base_url + "kwotes.pl?action=list&m=501&so=reverse&o=rating&s=" + str(i)
    PQ = PyQuery(url)
    BQ = PQ("blockquote")
    for x in BQ:
        try:
           text=x.text
           text=text.replace("\r", "").strip()
           res.append(text)
        except:
            error = 1
            #this is not error handling... it's error ignoring.

    if len(BQ):
        grabber(i+500)

grabber()
print(json.dumps({"memebombs":res, "origin":["#memebombs# \\#memebomb"]}))

