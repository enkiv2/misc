#!/usr/bin/env zsh
try:
    import Tkinter
except:
    import tkinter as Tkinter

import os, sys
import json

def ipfsGet(h):
    (stdin, stdout) = os.popen2(["ipfs", "cat", h])
    stdin.close()
    return stdout

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

