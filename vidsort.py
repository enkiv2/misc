#!/usr/bin/env python

from PIL import Image, ImageFont, ImageStat, ImageFile, ImageOps, ImageDraw, ImageChops

import sys, os, math
pad=0
fmt=""
def invertMask(pixel):
    return abs(pixel-255)
def avg(l):
    ax=0
    for i in l:
    	ax+=i
    return ax/len(l)
def imgDelta(a, b):
    merge=ImageChops.difference(a.convert("RGB"), b.convert("RGB")).convert("L")
    return avg(ImageStat.Stat(merge).mean)

def vid2frames(vidfile, fps, outdir):
    global pad, fmt
    cmd=("mplayer -vo jpeg"+
        ":outdir="+outdir+
        " -fps "+str(fps)+
        " -ao pcm:file=\""+outdir+
        "/audio.wav\" \""+vidfile+"\"")
    print(cmd)
    os.system(cmd)
    framecount=0
    for item in os.listdir(outdir):
        if item.find(".jpg")>0:
            pad=len(item)-4
            framecount+=1
    fmt="{0:0>"+str(pad)+"}"
    return framecount
def frames2vid(vidfile, fps, framenums, outdir, audiofile):
    os.system("mencoder -oac copy -ovc lavc -mf fps="+str(fps)+
        " -audiofile \""+outdir+"/"+audiofile+"\" "+
        " -o \""+vidfile+"\" "+
        " ".join(map(lambda x: "\"mf://"+outdir+"/"+fmt.format(x)+".jpg\"", framenums)))
def frame2audio(outdir, duration, idx, outfile):
    os.system("sox \""+outdir+"/audio.wav\" \""+outdir+"/"+outfile+"\" trim "+str(duration*idx)+" "+str(duration*(idx+1)))
def frames2audio(outdir, fps, framenums):
    spf=1.0/fps
    frame2audio(outdir, spf, framenums[0], "ax.wav")
    for frame in framenums[1:]:
        frame2audio(outdir, spf, frame, "item.wav")
        os.system("sox \""+outdir+"/ax.wav\" \""+outdir+"/item.wav\" ax2.wav")
        os.system("mv ax2.wav \""+outdir+"/ax.wav")
    os.system("mv \""+outdir+"/ax.wav\" \""+outdir+"/processed_audio.wav\"")

def findBestMatchFrame(needle, haystack, outdir):
    if(len(haystack)==1):
        return haystack[0]
    needleF=Image.open(outdir+"/"+fmt.format(needle)+".jpg")
    best=math.pow(2, 32)
    bestI=needle
    for item in haystack:
        delta=imgDelta(needleF, Image.open(outdir+"/"+fmt.format(item)+".jpg"))
        if(best>delta):
            best=delta
            bestI=item
    return item
def findMatchChain(initialFrame, frames, outdir):
    outFrames=[initialFrame]
    try:
        frames.remove(initialFrame)
    except:
        pass
    while(len(frames)>0):
        match=findBestMatchFrame(outFrames[-1], frames, outdir)
        frames.remove(match)
        outFrames.append(match)
    return outFrames

def main():
    os.system("rm -rf ~/.vidsort")
    os.system("mkdir ~/.vidsort")
    outdir=os.getenv("HOME")+"/.vidsort"
    frameCount=vid2frames(sys.argv[1], 25, outdir)
    frames=findMatchChain(1, range(1, frameCount), outdir)
    frames2audio(outdir, 25, frames)
    frames2vid("out.avi", 25, frames, outdir, "processed_audio.wav")

if(__name__=="__main__"):
    main()
