#!/usr/bin/env python

from PIL import Image, ImageFont, ImageStat, ImageFile, ImageOps, ImageDraw, ImageChops

import sys

imageFilename=sys.argv[1]
fontName=sys.argv[2]
wordFilename="/usr/share/dict/words"
if(len(sys.argv)>3):
	wordFilename=sys.argv[3]
widthChars=80
heightChars=25

img=Image.open(imageFilename).convert("L")
(width, height)=img.size
print("Image is "+str(width)+"x"+str(height))
#font=ImageFont.truetype(fontName, width/80)
font=ImageFont.truetype(fontName, 7)

def invertMask(pixel):
	return abs(pixel-255)
def avg(l):
	ax=0
	for i in l:
		ax+=i
	return ax/len(l)

print("Pre-rendering words...")

maxH=0
words=[]
wordImages=[]
wordMasks=[]
wordMasksI=[]
wordSizes=[]
for w in open(wordFilename, 'r').readlines():
	word=" "+w.replace("\n", "").replace("\r", "")
	words.append(word)
words.append(" ")

for word in words:
	wordSizes.append(font.getsize(word))
	if wordSizes[-1][1]>maxH:
		maxH=wordSizes[-1][1]
	
	temp=Image.new("L", wordSizes[-1], "#fff")
	tempDraw=ImageDraw.Draw(temp)
	tempDraw.text((0, 0), word, font=font)
	wordImages.append(temp)
	wordMasks.append(temp)
	wordMasksI.append(Image.eval(temp, invertMask))


print("Rendered")
print(words)

outImg=Image.new(img.mode, (width, height))

for rownum in range(0, height/maxH):
	y=rownum*maxH
	x=0
	while x<width:
		delta=width-x
		candidates=[]
		for i in range(0, len(words)):
			if(wordSizes[i][0]<delta):
				candidates.append(i)
		if(len(candidates)==0):
			break
		candidateScores={}
		for i in range(0, len(candidates)):
			c=candidates[i]
			bbox=(x, y, x+wordSizes[c][0], y+maxH)
			chunk=img.crop(bbox)
			stat1=ImageStat.Stat(ImageChops.multiply(chunk.convert("L"), wordMasks[c].convert("L")))
			stat2=ImageStat.Stat(ImageChops.multiply(chunk.convert("L"), wordMasksI[c].convert("L")))
			#score=(avg(stat1.rms)+(255-avg(stat2.rms)))/2
			score=(avg(stat1.mean)+(255-avg(stat2.mean)))/2
			if(score in candidateScores):
				candidateScores[score].append(i)
			else:
				candidateScores[score]=[i]
		scores=candidateScores.keys()
		scores.sort()
		b=candidateScores[scores[-1]]
		minW=wordSizes[b[0]]
		minB=0
		for i in b:
			if(wordSizes[i][0]<minW):
				minW=wordSizes[i][0]
				minB=i
		best=minB
		bbox=(x, y, x+wordSizes[best][0], y+wordSizes[best][1])
		outImg.paste(wordMasks[best].convert(outImg.mode), bbox)
		x+=wordSizes[best][0]
		sys.stdout.write(words[best])
	sys.stdout.write("\n")

outImg.save("output.png")
