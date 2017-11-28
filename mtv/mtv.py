#!/usr/bin/env python

""" mtv - minimal transliterature viewer
    (c) 2017 John Ohno
    This software is not associated with Project Xanadu (tm)!

    Requirements: python, tkinter, ipfs command line tools
"""

try:
    import Tkinter
    from Tkinter import *
    import tkFileDialog
    import tkSimpleDialog
except:
    import tkinter as Tkinter
    from tkinter import *
    from tkinter import filedialog
    tkFileDialog=filedialog
    import tkSimpleDialog

import os, sys, subprocess
import json
import urllib, urllib2
import tempfile
from random import Random

import cStringIO

global clipboard, url2hash, odl, recentDocs
clipboard=None
url2hash={}
windows=[]
odl=[]
recentDocs=[]

def genHLColor(obj):
    gen=Random(obj)
    red     = gen.randint(0, 128)+128
    green   = gen.randint(0, 128)+128
    blue    = gen.randint(0, 128)+128
    return "#%02X%02X%02X" % (red-1, green-1, blue-1)

def ipfsPutFile(path):
    #return os.popen("ipfs add -q --pin "+ path).read()
     return subprocess.check_output(["ipfs", "add", "-q", "--pin", path]).strip()
def ipfsPutStr(content):
    temp=tempfile.NamedTemporaryFile(delete=False)
    temp.write(content)
    temp.flush()
    temp.close()
    h=ipfsPutFile(temp.name)
    os.unlink(temp.name)
    return h
def urlGet(url):
    global url2hash
    if url in url2hash:
        h=url2hash[url]
    else:
        h=ipfsPutStr(urllib2.urlopen(url).read())
        url2hash[url]=h
    return ipfsGet(h)
def ipfsGet(h):
    h=h.strip()
    return cStringIO.StringIO(subprocess.check_output(["ipfs", "cat", h]))
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
    line=""
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
        concatext.append(rcSpan2str(clip["row"], clip["col"], clip["dRows"], clip["dCols"], get(clip["path"])))
    return concatext

def concatext2str(concatext):
    return "".join(concatext)

def spawnTranslitEditor(edl):
    global url2hash, recentDocs
    for item in windows:
        if(edl in [item.ed.currentEDLHash, item.ed.path]):
            item.master.master.deiconify()
            item.lift()
            return item
    if edl in recentDocs:
        recentDocs.remove(edl)
    recentDocs.insert(0, edl)

    top=TranslitEditorFrame(Toplevel())
    top.pack()
    windows.append(top)
    try:
        top.ed.openEDL(edl)
    except:
        top.ed.openTextAsEDL(edl)
    top.title()
    top.ed.addLinks(odl)
    json.dump(url2hash, open("url2hash.json", "w"))
    json.dump(recentDocs, open("recent.json", "w"))
    return top

def addLinksToODL(links):
    odl.extend(links)
    for win in windows:
        win.ed.addlinks(odl)

class TranslitEditor(Text):
    def __init__(self, *args, **kw_args):
        Text.__init__(self, *args, **kw_args)
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
        self.lastInsertionCursorPosition="0.0"
        def _on_change(self, event):
            if(self.index("insert")!=self.lastInsertionCursorPosition):
                self.lastInsertionCursorPosition=self.index("insert")
                self.showLinkTarget()
        self.bind("<<Change>>", _on_change)
    def idxDelta(self, idx, idx2):
        idx=idx.split(".")
        idx2=idx2.split(".")
        return (int(idx2[0])-int(idx[0]), int(idx2[1])-int(idx[1]))
    def renderTransclusionColor(self, clipNum):
        tagname="CLIP"+str(clipNum)
        h=self.clipLookup[clipNum]["path"]
        if(h=="orphan"):
            self.tag_config(tagname, background="#ffffff")
            return
        if(h in url2hash):
            h=url2hash[h]
        self.tag_config(tagname, background=genHLColor(h))
    def renderTransclusionColors(self):
        for i in range(0, len(self.clipLookup)):
            self.renderTransclusionColor(i)
    def showLinkTarget(self):
        target=self.index("insert")
        tags=self.tag_names(target)
        for tag in tags:
            if tag.find("LINK")==0:
                linkID=int(tag[4:])
                link=self.linkLookup[linkID]
                if(link["type"]!="format"):
                    for endpoint in link["endpoints"]:
                        win=spawnTranslitEditor(endpoint["path"])
                        win.ed.addLink(link)
                        win.ed.see(".".join([str(endpoint["row"]), str(endpoint["col"])]))
    def renderLink(self, linkNum):
        if(self.linkLookup[i]["type"]=="format"):
            self.tag_config("LINK"+str(linkNum), **self.linkLookup[i]["attributes"])
            return
        if(self.showLinkColors):
            endpoints=[]
            for item in self.linkLookup[linkNum][1]["endpoints"]:
                endpoints.append(item["path"])
            color=genHLColor(" ".join(endpoints))
            self.tag_config("LINK"+str(linkNum), background=color)
    def renderLinks(self):
        for i in range(0, len(self.linkLookup)):
            self.renderLink(i)
    def recolor(self):
        self.renderTransclusionColors()
        self.renderLinks()
    def addLink(self, link):
        if(link in self.odl):
            return
        found=False
        tags=[]
        endpoints=[]
        for endpoint in link:
            endpoints.append(endpoint["path"])
            if endpoint["path"] in [self.path, self.currentEDLHash]:
                tagname="LINK"+str(len(linkLookup))
                linkLookup.append((endpoint, link))
                found=True
                tags.append(tagname)
            elif endpoint["path"] in self.clipPaths:
                for i in range(0, len(self.clipLookup)):
                    clip=self.clipLookup[i]
                    if(clip["path"]==endpoint["path"]):
                        if(endpoint["row"]>=clip["row"] and endpoint["row"]<=clip["row"]+clip["dRows"]):
                            startRow=endpoint["row"]
                        # XXX finish calculating overlap
        if(found):
            self.odl.append(link)
    def addLinks(self, links):
        for link in links:
            self.addLink(link)
        self.recolor()
    def insertTextAsEDL(self, path):
        text=get(path).read()
        lines=text.split("\n")
        if path in url2hash:
            path=url2hash[path]
        return self.insertEDL(ipfsPutStr(json.dumps([{"path":path, "row":0, "col":0, "dRows":len(lines), "dCols":0}])))
    def insertEDL(self, path):
        edl=json.load(get(path))
        concatext=edl2concatext(edl)
        for i in range(0, len(edl)):
            self.clipPaths.append(edl[i]["path"])
            if(edl[i]["path"] in url2hash):
                self.clipPaths.append(url2hash[edl[i]["path"]])
            tagname="CLIP"+str(len(self.clipLookup))
            self.clipLookup.append(edl[i])
            self.insert("insert", concatext[i], tagname)
        if(self.showTransclusionColors):
            self.renderTransclusionColors()
        self.clipPaths=list(set(self.clipPaths))
        self.recalculateClips()
        self.recolor()
        return (edl, concatext)
    def openTextAsEDL(self, path):
        self.path=path
        self.delete("0.0", "end")
        (self.edl, self.concatext) = self.insertTextAsEDL(path)
        if path in url2hash:
            path=url2hash[path]
        self.currentEDLHash=path
    def openEDL(self, path):
        self.path=path
        self.delete("0.0", "end")
        (self.edl, self.concatext) = self.insertEDL(path)
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
                currTags.append(value)
                lastTag=index
            elif(key=="tagoff" and value.find("CLIP")==0):
                d=self.idxDelta(lastTag, index)
                clipNum=int(value[4:])
                dRows=self.clipLookup[clipNum]["dRows"]
                dCols=self.clipLookup[clipNum]["dCols"]
                if(d[0]!=dRows or d[1]!=dCols):
                    row=self.clipLookup[clipNum]["row"]
                    col=self.clipLookup[clipNum]["col"]
                    path=self.clipLookup[clipNum]["path"]
                    clipsToRemove.append((value, lastTag, index))
                    clipsToAdd.append( ( (path, (row, col), (d[0], d[1])),          (lastTag, index) ) )
                    if(d[0]!=dRows):
                        self.clipLookup[clipNum]["dRows"] -= d[0]
                        self.clipLookup[clipNum]["row"] += d[0]
                        self.clipLookup[clipNum]["col"] = d[1]
                    else:
                        self.clipLookup[clipNum]["dCols"]-=d[1]
                        self.clipLookup[clipNum]["cols"]+=d[1]
                currTags.remove(value)
                lastTag=index
        self.flushOrphan()
        for item in clipsToRemove:
            self.tag_remove(item[0], item[1], item[2])
        for item in clipsToAdd:
            tagname="CLIP"+str(len(self.clipLookup))
            clipInfo=item[0]
            self.clipLookup.append({"path":clipInfo[0], "row":clipInfo[1][0], "col":clipInfo[1][1], "dRows":clipInfo[2][0], "dCols":clipInfo[2][1]})
            self.tag_add(tagname, item[1][0], item[1][1])
    def publishOrphan(self):
        self.orphanFile.close()
        h=ipfsPutFile(self.orphanFile.name)
        os.unlink(self.orphanFile.name)
        self.orphan=[]
        self.orphanFile=tempfile.NamedTemporaryFile(delete=False)
        for i in range(0, len(self.clipLookup)):
            if self.clipLookup[i]["path"]=="orphan":
                self.clipLookup[i]["path"]=h
    def calculateEDLClip(self, start, end):
        edl=[]
        print("EDL clip")
        last=[]
        for item in self.dump(start, end, all=True):
            (key, value, index)=item
            if(key=="tagon" and value.find("CLIP")==0):
                clipNum=int(value[4:])
                edl.append(self.clipLookup[clipNum])
            elif(key=="text"):
                last.append(index)
        if(len(edl)==0):
            tags=self.tag_names(last[0])
            clip=None
            for item in tags:
                if(item.find("CLIP")==0):
                        clip=item
                        continue
            try:
                clipObj=self.clipLookup[int(clip[4:])]
                start_idx=self.index(clip+".first")
                offsetRow=int(start_idx.split(".")[0])-int(last[0].split(".")[0])
                dRow=int(last[-1].split(".")[0])-int(last[0].split(".")[0])
                dCol=int(last[-1].split(".")[1])
                edl.append({"path":clipObj["path"], "row":clipObj["row"]+offsetRow, "col":int(start_idx.split(".")[1]), "dRows":dRow, "dCols":dCol})
            except Exception as e:
                print e
        print(edl)
        return edl
    def calculateEDL(self):
        self.edl=self.calculateEDLClip("0.0", "end")
    def selectionAsClip(self):
        return self.calculateEDLClip("sel.first", "sel.last")
    def saveEDL(self, path=None):
        global url2hash
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
        json.dump(url2hash, open("url2hash.json", "w"))

class TranslitEditorFrame(Frame):
    def __init__(self, *args, **kw_args):
        Frame.__init__(self, *args, **kw_args)
        self.fr=Frame(self)
        self.cmdpanel=Frame(self.fr)
        self.ed=TranslitEditor(self.fr)
        self.utilpanel=Frame(self.cmdpanel)
        def openURLHelper(*args):
            url=tkSimpleDialog.askstring("Open URL or hash", "URL or hash", parent=self, initialvalue=self.clipboard_get())
            if(url):
                spawnTranslitEditor(url)
        def openFileHelper(*args):
            url=tkFileDialog.askopenfilename(title="Open EDL or text file", filetypes=[("EDL", "*.edl"), ("Plain text", "*.txt"), ("JSON", "*.json")], parent=self)
            if(url):
                spawnTranslitEditor("file://"+url)
        self.openfilebtn=Button(self.utilpanel, text="Open from filesystem", command=openFileHelper)
        self.openipfsbtn=Button(self.utilpanel, text="Open from URL", command=openURLHelper)
        def exportHelper(*args):
            self.ed.saveEDL()
        def exportFileHelper(*args):
            url=tkFileDialog.asksavefilename(title="Save EDL as", filetypes=[("EDL", "*.edl"), ("JSON", "*.json")], parent=self)
            if(url):
                self.ed.saveEDL(url)
        self.export=Button(self.utilpanel, text="Export", command=exportHelper)
        self.exportfile=Button(self.utilpanel, text="Export to file")
        self.openfilebtn.pack(side="left")
        self.openipfsbtn.pack(side="left")
        self.export.pack(side="left")
        self.exportfile.pack(side="right")
        self.utilpanel.pack()
        self.clippanel=Frame(self.cmdpanel)
        def copyHelper(*args):
            global clipboard
            self.ed.recalculateClips()
            try:
                clipboard=self.ed.selectionAsClip()
                print("Copied: ")
                print(clipboard)
            except Exception as e:
                print("Tried to copy but no selection!")
                print(e)
        def pasteHelper(*args):
            self.ed.recalculateClips()
            print("Pasting: ")
            print(clipboard)
            if(clipboard):
                self.ed.insertEDL(ipfsPutStr(json.dumps(clipboard)))
                self.ed.recalculateClips()
        self.copybtn=Button(self.clippanel, text="Copy clip", command=copyHelper)
        self.pastebtn=Button(self.clippanel, text="Paste clip", command=pasteHelper)
        self.copybtn.pack(side="left")
        self.pastebtn.pack()
        self.linkpanel=Frame(self.cmdpanel)
        self.linkbtn=Button(self.linkpanel, text="Link")
        self.fmtbtn=Button(self.linkpanel, text="Format")
        self.linkbtn.pack(side="left")
        self.fmtbtn.pack()
        self.clippanel.pack()
        self.linkpanel.pack()
        self.cmdpanel.pack()
        self.ed.pack()
        self.fr.pack()
        self.title()
        self.bind("<Enter>", self.title)
        def handleAutoSave(*args):
            self.ed.saveEDL()
            self.master.destroy()
        self.master.protocol("WM_DELETE_WINDOW", handleAutoSave)
    def title(self, *args):
        self.master.wm_title(str(self.ed.path)+" ("+str(self.ed.currentEDLHash)+") - mtv")

def main():
    global url2hash, recentDocs
    try:
        url2hash=json.load(open("url2hash.json", "r"))
        recentDocs=json.load(open("recent.json", "r"))
    except Exception as e:
        print(e)
        json.dump(url2hash, open("url2hash.json", "w"))
        json.dump(recentDocs, open("recent.json", "w"))
    tk=Tk()
    top=TranslitEditorFrame(tk)
    top.pack()
    windows.append(top)
    if len(sys.argv)>1:
        for target in sys.argv[1:]:
            print("Target: "+target)
            spawnTranslitEditor(target)
    def handleAutoSave(*args):
        for win in windows:
            win.ed.saveEDL()
        tk.destroy()
    tk.protocol("WM_DELETE_WINDOW", handleAutoSave)
    tk.mainloop()

if __name__=="__main__":
    main()
