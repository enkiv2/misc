#!/usr/bin/env zsh
try:
    import Tkinter
except:
    import tkinter as Tkinter

import os, sys
import json
import urllib, urllib2
import tempfile

url2hash={}

def ipfsPutFile(path):
    return os.popen(["ipfs", "put", "-Q", "--pin", path]).read()
def ipfsPutStr(content):
    temp=tempfile.NamedTemporaryFile(delete=False)
    temp.write(content)
    temp.close()
    h=ipfsPutFile(f.name)
    os.unlink(f.name)
    return h
def urlGet(url):
    if url in urlhash:
        h=urlhash[url]
    else:
        h=ipfsPutStr(urllib2.urlopen(url).read())
        urlhash[url]=h
    return ipfsGet(h)
def ipfsGet(h):
    (stdin, stdout) = os.popen2(["ipfs", "cat", h])
    stdin.close()
    return stdout
def get(path):
    if path[0]=="/":
        path="file://"+path
    protocol=path.split(":")[0]
    if(len(protocol)==1): # Windows
        protocol="file"
        path="file://"+path
    if(path.find(":")==-1 or protocol in ["ipfs", "ipns"]):
        return ipfsGet(path)
    else:
        return urlGet(path)

def rcSpan2str(row, col, dRows, dCols, contentStream):
    ret=[]
    for i in range(0, row):
        line=contentStream.readline()
    ret.append(line[col:])
    for i in range(0, dRows-1):
        ret.append(contentStream.readline())
    ret.append(contentStream.readline()[:dCols])
    contentStream.close()
    return "\n".join(ret)

def edl2concatext(edl):
    concatext=[]
    for clip in edl:
        concatext.append(rcSpan2str(clip.row, clip.col, clip.dRows, clip.dCols, get(clip.path)))
    return concatext

def concatext2str(concatext):
    return "".join(concatext)


