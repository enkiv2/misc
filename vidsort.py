#!/usr/bin/env python

from PIL import Image, ImageFont, ImageStat, ImageFile, ImageOps, ImageDraw, ImageChops

from multiprocessing import Pool

import sys, os, math
poolSize=10
pool=Pool(poolSize)
pad=0
fmt=""
def invertMask(pixel):
    return abs(pixel-255)
def avg(l):
    ax=0
    for i in l:
    	ax+=i
    return ax/len(l)
def chunkDivide(l, chunkMax):
    ret=[]
    i=0
    while(len(l)>i):
        j=i+chunkMax
        if(chunkMax>=len(l)):
            chunkMax=len(l)-1
        ret.append(l[i:j])
        i=j
    return ret
def mindex(l):
    i=0
    m=l[0]
    for j in range(0, len(l)):
        if(l[j]<m):
            m=l[j]
            i=j
    return (m, i)
def mindex2(l):
    l2=pool.map(mindex, l)
    l3=[]
    for i in range(0, len(l)):
        l3.extend(pool.map(lambda x: (x[0], x[1]*i), l2[i]))
    m=l3[0][0]
    i=0
    for j in range(0, len(l3)):
        if(m>l3[j][0]):
            m=l3[j][0]
            i=l3[j][1]
    return i
cache={}
def deCache(framenum, outdir):
    num=str(framenum)
    if(not(num in cache)):
        cache[num]=(Image.open(outdir+"/"+fmt.format(framenum)+".jpg")).convert("RGB")
    return cache[num]
def imgDelta(a, b):
    merge=ImageChops.difference(a, b).convert("L")
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
    needleF=deCache(needle, outdir)
    return mindex2(pool.map(lambda y: pool.map(lambda x: imgDelta(needleF, deCache(x, outdir)), y), chunkDivide(haystack, poolSize)))

def findMatchChain(initialFrame, frames, outdir):
    outFrames=[initialFrame]
    try:
        frames.remove(initialFrame)
    except:
        pass
    while(len(frames)>0):
        match=findBestMatchFrame(outFrames[-1], frames, outdir)
        cache.remove(str(outFrames[-1]))
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
