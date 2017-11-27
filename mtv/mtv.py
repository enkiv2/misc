#!/usr/bin/env zsh

""" mtv - minimal transliterature viewer
    (c) 2017 John Ohno
    This software is not associated with Project Xanadu (tm)!

    Requirements: python, tkinter, ipfs command line tools
"""

try:
    import Tkinter
except:
    import tkinter as Tkinter

import os, sys
import json
import urllib, urllib2
import tempfile
from random import Random

url2hash={}

def genHLColor(obj):
    gen=Random(obj)
    red     = gen.randint(0, 128)+128
    green   = gen.randint(0, 128)+128
    blue    = gen.randint(0, 128)+128
    return "#%02x%02x%02x" % (red, green, blue)

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

class TranslitEditor(Tkinter.Text):
    def __init__(self, *args, **kw_args):
        Tkinter.Text(self, *args, **kw_args)
        self.edl=[]
        self.currentEDLHash=None
        self.clipPaths=[]
        self.clipLookup=[]
        self.linkLookup=[]
        self.concatext=[]
        self.odl=[]
        self.path=None
        self.orphanFile=tempfile.NamedTemporaryFile(delete=False)
        self.orphan=[]
        self.showTransclusionColors=True
        self.showLinkColors=True
    def idxDelta(self, idx, idx2):
        idx=idx.split(".")
        idx2=idx2.split(".")
        return (int(idx2[0])-int(idx[0]), int(idx2[1])-int(idx[1]))
    def renderTransclusionColor(self, clipNum):
        tagname="CLIP"+str(clipNum)
        h=clipLookup[clipNum].path
        if(h=="orphan"):
            self.tag_config(tagname, background="#ffffff")
            return
        if(h in url2hash):
            h=url2hash[h]
        self.tag_config(tagname, background=genHLColor(h))
    def renderTransclusionColors(self):
        for i in range(0, len(self.clipLookup)):
            renderTransclusionColor(i)
    def renderLink(self, linkNum):
        if(self.showLinkColors):
            endpoints=[]
            for item in self.linkLookup[linkNum][1].endpoints:
                endpoints.append(item.path)
            color=genHLColor(" ".join(lendpoints))
            self.tag_config("LINK"+str(linkNum), color)
    def renderLinks(self):
        for i in range(0, len(self.linkLookup)):
            self.renderLink(i)
    def addLink(self, link):
        found=False
        tags=[]
        endpoints=[]
        for endpoint in link:
            endpoints.append(endpoint.path)
            if endpoint.path in [self.path, self.currentEDLHash]:
                tagname="LINK"+str(len(linkLookup))
                linkLookup.append((endpoint, link))
                found=True
                tags.append(tagname)
            elif endpoint.path in self.clipPaths:
                for i in range(0, len(self.clipLookup)):
                    clip=self.clipLookup[i]
                    if(clip.path==endpoint.path):
                        if(endpoint.row>=clip.row and endpoint.row<=clip.row+clip.dRows):
                            startRow=endpoint.row
                        # XXX finish calculating overlap
        if(found):
            self.odl.append(link)

    def insertEDL(self, path):
        edl=json.load(get(path))
        concatext=edl2concatext(edl)
        for i in range(0, len(edl)):
            self.clipPaths.append(edl[i].path)
            if(edl[i].path in url2hash):
                self.clipPaths.append(url2hash[edl[i].path])
            tagname="CLIP"+str(len(self.clipLookup))
            self.clipLookup.append(edl[i])
            self.insert("insert", concatext[i], [tagname])
        if(self.showTransclusionColors):
            self.renderTransclusionColors()
        self.clipPaths=list(set(self.clipPaths))
        return (edl, concatext)
    def openEDL(self, path):
        self.path=path
        self.delete("0.0", "end")
        (self.edl, self.concatext) = insertEDL(path)
        if path in url2hash:
            path=url2hash[path]
        self.currentEDLHash=path
    def flushOrphan(self):
        newOrphan=[[]]*len(self.orphan)
        for line in self.orphan:
            if(len(line)>0):
                self.orphanFile.write(line+"\n")
        self.orphan=newOrphan
        self.orphanFile.flush()
    def recalculateClips(self):
        currTags=[]
        clipsToAdd=[]
        clipsToRemove=[]
        lastTag="0.0"
        for item in self.dump("0.0", "end", tag=True):
            (key, value, index)=item
            if(key=="tagon" and value.find("CLIP")==0):
                if(len(currTags)==0):
                    chunk=self.get(lastTag, index)
                    if(len(chunk)>0):
                        chunkLines=chunk.split("\n")
                        clipsToAdd.append((("orphan", (len(self.orphan), 0), (len(chunkLines), 0)), (lastTag, index)))
                        self.orphan.extend(chunkLines)
                currtags.append(value)
                lastTag=index
            elif(key=="tagoff" and value.find("CLIP")==0):
                d=idxDelta(lastTag, index)
                clipNum=int(value[4:])
                dRows=self.clipLookup[clipNum].dRows
                dCols=self.clipLookup[clipNum].dCols
                if(d[0]!=dRows or d[1]!=dCols):
                    row=self.clipLookup[clipNum].row
                    col=self.clipLookup[clipNum].col
                    path=self.clipLookup[clipNum].path
                    clipsToRemove.append((value, lastTag, index))
                    clipsToAdd((path, (row, col), (d[0], d[1])), (lastTag, index))
                    if(d[0]!=dRows):
                        clipLookup[clipNum].dRows-=d[0]
                        clipLookup[clipNum].rows+=d[0]
                        clipLookup[clipNum].cols=d[1]
                    else:
                        clipLookup[clipNum].dCols-=d[1]
                        clipLookup[clipNum].cols+=d[1]
                currtags.remove(value)
                lastTag=index
        self.flushOrphan()
        for item in clipsToRemove:
            self.tag_remove(item[0], item[1], item[2])
        for item in clipsToAdd:
            tagname="CLIP"+str(len(self.clipLookup))
            clipInfo=item[0]
            self.clipLookup.append({path=clipInfo[1], row=clipInfo[1][0], col=clipInfo[1][1], dRows=clipInfo[2][0], dCols=clipInfo[2][1]})
            self.tag_add(tagname, item[1], item[2])
    def publishOrphan(self):
        self.orphanFile.close()
        h=ipfsPutFile(self.orphanFile.name)
        os.unlink(self.orphanFile.name)
        self.orphan=[]
        self.orphanFile=tempfile.NamedTemporaryFile(delete=False)
        for i in range(0, len(self.clipLookup)):
            if self.clipLookup[i].path=="orphan":
                self.clipLookup[i].path=h
    def calculateEDLClip(self, start, end):
        edl=[]
        for item in self.dump(start, end, tag=True):
            (key, value, index)=item
            if(key=="tagon" and value.find("CLIP")==0):
                clipNum=int(value[4:])
                edl.append(self.clipLookup[clipNum])
        return edl
    def calculateEDL(self):
        self.edl=calculateEDLClip("0.0", "end")
    def saveEDL(self, path=None):
        self.recalculateClips()
        self.publishOrphan()
        self.renderTransclusionColors()
        self.calculateEDL()
        self.currentEDLHash=ipfsPutStr(json.dumps(self.edl))
        if(path):
            self.path=path
            f=open(path, "w")
            f.write(ipfsGet(self.currentEDLHash).read())
            f.flush()
            f.close()
