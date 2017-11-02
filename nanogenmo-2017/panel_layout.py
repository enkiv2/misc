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
    if(width<=bordersize*2 or height<=bordersize*2):
        return []
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
    if(targetWidth<=bordersize*2):
        targetWidth=width
    if(targetHeight<=bordersize*2):
        targetHeight=height
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
    topBoundaries=[]
    bottomBoundaries=[]
    leftovers=[(0, 0, page.size[0], page.size[1])]
    while(len(leftovers)>0):
        chunk=leftovers.pop()
        topBoundaries.append((chunk[0], chunk[1]))
        bottomBoundaries.append((chunk[0], chunk[3]))
        leftovers.extend(layoutRect(chunk, page, bordersize, colorize, sketchOnly))
    return (page, topBoundaries, bottomBoundaries)

def generateBox(line,colorize=True,  maxwidth=720):
    size=font.getsize(line)
    if(size[0]>maxwidth):
        boxes=[]
        words=line.split()
        i=1
        while font.getsize(" ".join(words[:-i]))[0]>maxwidth and i<len(words):
            i+=1
        boxes.append(generateBox(" ".join(words[:-i]), colorize, maxwidth))
        boxes.append(generateBox(" ".join(words[-i:]), colorize, maxwidth))
        scratch=Image.new("RGBA", (max(boxes[0].size[0], boxes[1].size[0]), boxes[0].size[1]+boxes[1].size[1]), "#ffffcc")
        scratch.paste(boxes[0], (0, 0))
        scratch.paste(boxes[1], (0, boxes[0].size[1]))
        return scratch
    if(colorize):
        color="#ffffcc"
    else:
        color="#ffffff"
    box=Image.new("RGB", (size[0]+10, size[1]+10), color=color)
    ImageDraw.Draw(box).text((5, 5), line, font=font, fill="#000000")
    return box.convert("RGBA")

def genPage(lines, bordersize=5, colorize=True, sketchOnly=False):
    (page, topBoundaries, bottomBoundaries)=layoutPage(bordersize, colorize, sketchOnly)
    i=0
    for line in lines:
        i+=1
        if(random.choice([True, False])):
            # Align to the top of the frame
            position=random.choice(topBoundaries)
            topBoundaries.remove(position)
            page.paste(generateBox(line, colorize, maxwidth=720-position[0]), (position[0]+2*bordersize, position[1]+2*bordersize))
        else:
            # Align to the bottom of the frame
            position=random.choice(topBoundaries)
            topBoundaries.remove(position)
            box=generateBox(line, colorize, maxwidth=720-position[0])
            page.paste(box, (position[0]+2*bordersize, position[1]-(2*bordersize+box.size[1])))
        if(len(topBoundaries)==0 or len(bottomBoundaries)==0):
            return (page, lines[i:])
        if(i>5):
            return (page, lines[i:])
    return (page, [])


def genPages(lines, pfx, bordersize=5, colorize=True, sketchOnly=False):
    pages=[]
    while len(lines)>0:
        try:
            if(len(pages)==24):
                colorize=False
            if(len(pages)==94):
                sketchOnly=True
            if(len(pages)==101):
                return
            (page, lines2)=genPage(lines, bordersize, colorize, sketchOnly)
            pages.append(page)
            pages[-1].save(pfx+"-"+str(len(pages))+".png")
            print("Page successful")
            lines=lines2
        except Exception as e:
            print(e)
lines=list(sys.stdin.readlines())
genPages(lines, "comic")

