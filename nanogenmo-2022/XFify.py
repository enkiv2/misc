#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter
from random import Random
random=Random()

DPI=300
pageSizeIn=(4.5, 7)

pageSizePx=(int(pageSizeIn[0]*DPI), int(pageSizeIn[1]*DPI))
candidates=[]
default_font=ImageFont.truetype("Akira Expanded Demo.ttf", 20)

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
		return Image.new("RGB", pageSizePx, "#ffff")

alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def layoutSectionHeader(headerName, color):
		pages=[newPage()]
		maxHeight=int(pageSizePx[1]/2)
		minHeight=int(pageSizePx[1]/3)
		headerName=headerName.replace(" ", "")

		i=0
		while i<len(headerName):
				chunk=rubicate(pickCandidate(), color, headerName[i], maxHeight)
				height=chunk.size[1]
				while height<minHeight and headerName[i] in alpha:
						chunk=rubicate(pickCandidate(), color, headerName[i], maxHeight)
						height=chunk.size[1]
				print(headerName[i], flush=True)
				i+=1
				pages[-1].paste(chunk, (0, 0, chunk.size[0], chunk.size[1]))
				if i<len(headerName):
						chunk=rubicate(pickCandidate(), color, headerName[i], maxHeight)
						height=chunk.size[1]
						while height<minHeight and headerName[i] in alpha:
								chunk=rubicate(pickCandidate(), color, headerName[i], maxHeight)
								height=chunk.size[1]
						print(headerName[i], flush=True)
						i+=1
						pages[-1].paste(chunk, (0, maxHeight, chunk.size[0], maxHeight+chunk.size[1]))
						if i<len(headerName):
								pages.append(newPage())
		return pages

def wrapLines(para, maxwidth):
		lines=[]
		words=para.split(" ")
		while len(words)>0:
				i=0
				while default_font.getbbox(" ".join(words[:i]))[2]<maxwidth and i<len(words):
						i+=1
				i-=1
				if i>0:
						lines.append(" ".join(words[:i]))
						words=words[i:]
				else:
						print(f"ERROR: could not word wrap word: `{words[0]}`")
						lines.append(words[0])
						words=words[1:]
						# raise Exception
		return lines


def layoutPageRect(paras, bbox):
		img=Image.new("RGB", bbox, "#fff")
		offset=1
		p=0
		while p<len(paras):
				para=paras[p]
				if not para:
						p+=1
				else:
						print(default_font.getbbox(para))
						line_bbox=default_font.getbbox(para)[2:]
						if line_bbox[1]+offset>=bbox[1]:
								print("==== END OF PAGE ====")
								return (img, paras[p:])
						if line_bbox[0]>bbox[0]:
								lines=[]
								try:
										print("Trying to wrap lines", (para, bbox[0]))
										lines=wrapLines(para, bbox[0])
								except:
										print("ERROR: could not wrap", line_bbox, bbox)
										if bbox[0]==pageSizePx[0]:
												raise
										return (img, paras[p:])
								print(">>>> WRAPPING >>>")
								(img2, paras2)=layoutPageRect(lines, (bbox[0]+offset, bbox[1]))
								img.paste(img2, (0, offset, img2.size[0], img2.size[1]+offset))
								offset+=img2.size[1]
								print("<<<< WRAPPING <<<<")
								if paras2:
										paras[p]=" ".join(paras2)
								else:
										p+=1
						else:
							d=ImageDraw.Draw(img)
							d.text((1, offset), para, font=default_font, fill="#000")
							offset+=line_bbox[1]
							p+=1
							print((para, line_bbox, bbox, offset), flush=True)
		return (img, [])




def layoutSectionBody(body, color):
		pages=[newPage()]
		body=body.strip()
		illuminatedLetter=rubicate(pickCandidate(), color, body[0], int(pageSizePx[1]/2))
		while illuminatedLetter.size[0]>pageSizePx[0]:
				illuminatedLetter=rubicate(pickCandidate(), color, body[0], int(pageSizePx[1]/2))
		pages[-1].paste(illuminatedLetter, (0, 0, illuminatedLetter.size[0], illuminatedLetter.size[1]))
		paras=body[1:].split("\n")
		print(body[0])
		(img, remainder)=layoutPageRect(paras, (pageSizePx[0]-illuminatedLetter.size[0], illuminatedLetter.size[1]))
		pages[-1].paste(img, (illuminatedLetter.size[0], 0, illuminatedLetter.size[0]+img.size[0], img.size[1]))
		if remainder:
				(img, remainder)=layoutPageRect(remainder, (pageSizePx[0], pageSizePx[1]-illuminatedLetter.size[1]))
				pages[-1].paste(img, (0, illuminatedLetter.size[1], img.size[0], illuminatedLetter.size[1]+img.size[1]))
				while remainder:
						print("==== NEW PAGE ===")
						pages.append(newPage())
						(img, remainder)=layoutPageRect(remainder, pageSizePx)
						pages[-1].paste(img, (0, 0, img.size[0], img.size[1]))
		return pages

def layoutSection(headerName, body, color):
		print("---- SECTION ----")
		return layoutSectionHeader(headerName, color)+layoutSectionBody(body, color)


def writePages(pages, offset=0):
		for i in range(0, len(pages)):
				p=offset+i
				pages[i].save(f"page{p:05d}.png")
		return offset+len(pages)


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
		return bottom.convert("RGB")

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
		#writePages(layoutSection("SPECTACLE", "The history of civilization is the history of class struggle. The spectacle is not an accumulation of images or a relation between images but a relation between people mediated by images.", (255, 0, 0)))
		#writePages(layoutSectionBody("The history of civilization is the history of class struggle. The spectacle is not an accumulation of images or a relation between images but a relation between people mediated by images.", (255, 0, 0)))
		section=[]
		header=""
		colors=[(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
		i=0
		offset=0
		for line in sys.stdin.readlines():
				if line[0]=="#":
						if section:
								offset=writePages(layoutSection(header, "\n".join(section), colors[i%len(colors)]), offset)
								section=[]
								i+=1
						header=line[2:]
				else:
						section.append(line)
		writePages(layoutSection(header, "\n".join(section), colors[i%len(colors)]), offset)