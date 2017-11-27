#!/usr/bin/env zsh
try:
    import Tkinter
except:
    import tkinter as Tkinter

import os, sys
import json

def ipfsGet(h):
    (stdin, stdout) = os.popen2(["ipfs", "cat", h])
    return stdout

def rcSpan2str(row, col, dRows, dCols, content):
    lines=content.split("\n")
    if(dRows==0):
        return content[row][col:col+dCols]
    ret=[]
    ret.append(lines[row][col:])
    for r in range(1, dRows-1):
        ret.append(lines[row+r])
    ret.append(lines[row+dRows][:dCols]
    return "\n".join(ret)

def edl2concatext(edl):
    concatext=[]

