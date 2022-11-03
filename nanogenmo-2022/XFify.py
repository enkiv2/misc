#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter
from random import Random
random=Random()

DPI=300
pageSizeIn=(4.5, 7)

pageSizePx=(int(pageSizeIn[0]*DPI), int(pageSizeIn[1]*DPI))
candidates=[]

def pickCandidate():
		random.shuffle(candidates)
		bg=None
		for item in candidates:
				try:
						bg=Image.open(item).convert("RGB")
						if bg.size:
								return bg
				except:
						pass
		return bg

def newPage():
		return Image.new("RGBA", pageSizePx, "#ffff")

def layoutSectionHeader(headerName, color):
		pages=[newPage()]
		maxHeight=int(pageSizePx[1]/2)
		minHeight=int(pageSizePx[1]/3)

		i=0
		while i<len(headerName):
				height=0
				while height<minHeight:
						chunk=rubicate(pickCandidate(), color, headerName[i], maxHeight)
						height=chunk.size[1]
				i+=1
				pages[-1].paste(chunk, (0, 0, chunk.size[0], chunk.size[1]))
				if i<len(headerName):
						height=0
						while height<minHeight:
								chunk=rubicate(pickCandidate(), color, headerName[i], maxHeight)
								height=chunk.size[1]
						i+=1
						pages[-1].paste(chunk, (0, maxHeight, chunk.size[0], maxHeight+chunk.size[1]))
						if i<len(headerName):
								pages.append(newPage())
		return pages

def writePages(pages):
		for i in range(0, len(pages)):
				pages[i].save(f"page{i:05d}.png")


# Mimic the risograph-like monochrome style of the illustrations in the XF
def risoify(sourceImage, color=None, invert=False):
		sourceImage=ImageOps.grayscale(sourceImage).convert("RGBA")
		if not color:
				return sourceImage
		overlay=Image.new("RGBA", sourceImage.size, color=color)
		if invert:
				sourceImage=ImageChops.invert(sourceImage)
				overlay=ImageChops.invert(overlay)
		merged=ImageChops.multiply(sourceImage, overlay)
		if invert:
				merged=ImageChops.invert(merged)
		return merged

def rubicate(sourceImage, color, string, maxHeight=None):
		font=ImageFont.truetype("Akira Expanded Demo.ttf", sourceImage.size[1])
		mask=Image.new("1", sourceImage.size, color=1)
		ImageDraw.Draw(mask).text((0, 0), string, font=font)
		top=risoify(sourceImage, color, True)
		bottom=risoify(sourceImage, color, False)
		bottom.paste(top, mask=mask)
		bottom=bottom.crop(font.getbbox(string))
		if maxHeight and bottom.size[1]>maxHeight:
				ratio=(1.0*maxHeight)/bottom.size[1]
				bottom=bottom.resize((int(bottom.size[0]*ratio), maxHeight))
		return bottom

if __name__=="__main__":
		for path in sys.argv[1:]:
				if(os.path.isdir(path)):
						stuff=os.walk(path)
						for entry in stuff:
								pfx=entry[0]
								for sfx in entry[2]:
										candidates.append(pfx+"/"+sfx)
				else:
						candidates.append(path)
		writePages(layoutSectionHeader("SPECTACLE", (255, 0, 0)))
