#!/usr/bin/env python

from PIL import Image, ImageFont, ImageStat, ImageFile, ImageOps, ImageDraw, ImageChops

from multiprocessing import Pool
import multiprocessing
from random import Random
random=Random()

import sys, os, math, gc
poolSize=10
pad=0
fmt=""
##############################################################################
# From: https://stackoverflow.com/a/16071616/1966871
def fun(f, q_in, q_out):
    while True:
        i, x = q_in.get()
        if i is None:
            break
        q_out.put((i, f(x)))


def parmap(f, X, nprocs=multiprocessing.cpu_count()):
    q_in = multiprocessing.Queue(1)
    q_out = multiprocessing.Queue()

    proc = [multiprocessing.Process(target=fun, args=(f, q_in, q_out))
            for _ in range(nprocs)]
    for p in proc:
        p.daemon = True
        p.start()

    sent = [q_in.put((i, x)) for i, x in enumerate(X)]
    [q_in.put((None, None)) for _ in range(nprocs)]
    res = [q_out.get() for _ in range(len(sent))]

    [p.join() for p in proc]

    return [x for i, x in sorted(res)]
###############################################################################

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
cacheMaxItems=750
cache={}
def deCache(framenum, outdir):
    while(len(cache.keys())>=cacheMaxItems):
        del cache[random.choice(cache.keys())]
        gc.collect()
    num=str(framenum)
    if(not(num in cache)):
        try:
            cache[num]=(Image.open(outdir+"/"+fmt.format(framenum)+".jpg")).convert("RGB")
        except:
            return None
    return cache[num]
def imgDelta(a, b):
    if(a==None or b==None):
        return 2**64
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
    def fileIfExists(x):
        path=outdir+"/"+fmt.format(x)+".jpg"
        if(os.path.exists(path)):
            return "\"mf://"+path+"\""
        else: return ""
    os.system("mencoder -oac copy -ovc lavc -mf fps="+str(fps)+
        " -o \""+vidfile+"\" "+
        " ".join(map(fileIfExists, framenums)))
    os.system("mencoder -oac copy -ovc copy " +
        " -audiofile \""+outdir+"/"+audiofile+"\" "+
        "-o \"new_"+vidfile+"\" \""+vidfile+"\"")
    os.system("mv \"new_"+vidfile+"\" \""+vidfile+"\"")
def frame2audio(outdir, duration, idx, outfile):
    os.system("sox \""+outdir+"/audio.wav\" \""+outdir+"/"+outfile+"\" trim "+str(duration*idx)+" "+str(duration*(idx+1)))
def frames2audio(outdir, fps, framenums):
    spf=1.0/fps
    frame2audio(outdir, spf, framenums[0], "ax.wav")
    for frame in framenums[1:]:
        frame2audio(outdir, spf, frame, "item.wav")
        os.system("sox \""+outdir+"/ax.wav\" \""+outdir+"/item.wav\" ax2.wav")
        os.system("mv ax2.wav \""+outdir+"/ax.wav\"")
    os.system("mv \""+outdir+"/ax.wav\" \""+outdir+"/processed_audio.wav\"")

def findBestMatchFrame(needle, haystack, outdir):
    global pool
    if(len(haystack)==1):
        return haystack[0]
    sys.stdout.write("|")
    needleF=deCache(needle, outdir)
    sys.stdout.write("\b-")
    sys.stdout.flush()
    def deltaDecache(x):
        sys.stdout.write("\b"+random.choice(["|", "/", "-", "\\"]))
        sys.stdout.flush()
        return imgDelta(needleF, deCache(x, outdir))
    deltas=parmap(deltaDecache, haystack)
    sys.stdout.write("\b")
    sys.stdout.flush()
    return mindex(deltas)[1]
    #return mindex2(pool.map(lambda y: pool.map(lambda x: imgDelta(needleF, deCache(x, outdir)), y), chunkDivide(haystack, poolSize)))

def findMatchChain(initialFrame, frames, outdir):
    numFrames=len(frames)
    print("Caching frames...")
    framesToCache=frames
    if(len(framesToCache)>cacheMaxItems):
        framesToCache=frames[:cacheMaxItems]
    parmap(lambda x: deCache(x, outdir), framesToCache)
    print("Starting frame path identification...")
    outFrames=[initialFrame]
    try:
        frames.remove(0)
    except:
        pass
    try:
        del frames[initialFrame]
    except:
        pass
    plugged=False
    while(len(frames)>0):
	sys.stdout.write(".")
        percent=(len(frames)*100)/numFrames
        if(percent%10 == 0):
            if(not plugged):
                sys.stdout.write(str(percent)+"%")
                plugged=True
        else:
            plugged=False
        frameSample=frames
        if(len(frames)>1000):
            frameSample=random.sample(frames, 1000)
        match=findBestMatchFrame(outFrames[-1], frameSample, outdir)
        try:
            del cache[str(outFrames[-1])]
        except:
            pass
        try:
            del frames[match]
        except:
            outFrames.append(match)
            outFrames.extend(frames)
            return outFrames
        outFrames.append(match)
        gc.collect()
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
