#!/usr/bin/env python
from sketchify import *

import os, sys
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter
from random import Random
random=Random()

try:
    font=ImageFont.truetype("arialbi.ttf", 64)
except:
    try:
        font=ImageFont.truetype("arial.ttf", 64)
    except:
        font=ImageFont.load_default()

candidates=[]
def walk_helper(arg, dirname, fnames):
    for item in fnames:
        fullpath=os.path.join(dirname, item)
        if not (os.path.isdir(fullpath)):
            candidates.append(fullpath)
for path in sys.argv[1:]:
    if(os.path.isdir(path)):
        os.path.walk(path, walk_helper, None)
    else:
        candidates.append(path)

def pickCandidate():
    random.shuffle(candidates)
    bg=None
    for item in candidates:
        try:
            bg=Image.open(item).convert("RGB")
            return bg
        except:
            pass
    return bg

def newPage():
    return Image.new("RGBA", (10*72, 15*72), "#ffff")

def layoutRect(bbox, page, bordersize=5, colorize=True, sketchOnly=False):
    width=bbox[2]-bbox[0]
    height=bbox[3]-bbox[1]
    ok=False
    while not ok:
        try:
            img=pickCandidate()
            panel=panelify(img, (img.size[0]-bordersize*2, img.size[1]-bordersize*2))
            ok=True
            print("Panel successful")
        except Exception as e:
            print(e)
            print("Could not panelify")
            pass
    if(img.size[0]>width):
        img=img.resize((width, int(img.size[1]*(1.0*width/img.size[0]))))
    if(img.size[1]>height):
        img=img.resize((int(img.size[0]*(1.0*height/img.size[1])), height))
    targetWidth=width
    if(abs(width-(1.0*img.size[0]))/width>0.2):
        if abs(width-img.size[0])>bordersize*2:
            targetWidth=img.size[0]
    targetHeight=height
    if(abs(height-(1.0*img.size[1]))/height>0.2):
        if abs(height-img.size[1])>bordersize*2:
            targetHeight=img.size[1]
    panel=panelify(img, (targetWidth, targetHeight), bordersize, colorize, sketchOnly)
    page.paste(panel, (bbox[0], bbox[1]))
    leftovers=[]
    dWidth=width-targetWidth
    dHeight=height-targetHeight
    if targetWidth<width:
        if targetHeight<height:
            leftovers.append((bbox[2]-dWidth, bbox[1], bbox[2], bbox[3]-dHeight))
            leftovers.append((bbox[2]-dWidth, bbox[3]-dHeight, bbox[2], bbox[3]))
            leftovers.append((bbox[0], bbox[3]-dHeight, bbox[2]-dWidth, bbox[3]))
        else:
            leftovers.append((bbox[2]-dWidth, bbox[1], bbox[2], bbox[3]))
    else:
        if targetHeight<height:
            leftovers.append((bbox[0], bbox[3]-dHeight, bbox[2], bbox[3]))
    return leftovers

def layoutPage(bordersize=5, colorize=True, sketchOnly=False):
    page=newPage()
    leftovers=[(0, 0, page.size[0], page.size[1])]
    while(len(leftovers)>0):
        chunk=leftovers.pop()
        leftovers.extend(layoutRect(chunk, page, bordersize, colorize, sketchOnly))
    return page


pages=[]

page=layoutPage()
page.save("page.png")

