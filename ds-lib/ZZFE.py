#!/usr/bin/env python

# LEGAL NOTE:
# ZigZag(R) is a registered trademark of Project Xanadu(R).
# This implementation is covered by US Patent 262736B1! Until it expires, do not use it without permission from Ted Nelson.

from ZZCell import *

try:
	import Tkinter
	from Tkinter import *
	import tkFileDialog
	import tkSimpleDialog
except:
	import tkinter as Tkinter
	from tkinter import *
	from tkinter import filedialog
	tkFileDialog=filedialog
	from tkinter import simpledialog
	tkSimpleDialog=simpledialog

cellColor='#aaffff'
cloneColor='#ffff00'
leftHLColor='#aaaaff'
rightHLColor='#aaffaa'
paneWidth=600
paneHeight=600
gap=20
maxLineWidth=150
minCellWidth=20
minCellHeight=50

dims=[]
for i in range(0, 9):
	dims.append("d."+str(i))
dims.append("d.clone")

def refreshDimList():
	usedDims=[]
	for cell in cells:
		usedDims.extend(cell.getDims())
		usedDims=list(set(usedDims))
	for dim in usedDims:
		if not (dim in dims):
			dims.append(dim)

class ZZPane:
	def __init__(self, parent, accursed=0, hlColor='#aaaaff'):
		self.accursed=accursed
		if(type(accursed)==type(0)):
			self.accursed=cells(accursed)
		self.hlColor=hlColor
		self.other=None
		self.dimX=0
		self.dimY=1
		self.canvas=Canvas(parent, width=paneWidth, height=paneHeight)
		self.dimYLabel=None; self.dimXLabel=None
		self.operationMark=None
	def pack(self, *args):
		self.canvas.pack(*args)
	def drawCompass(self, full=False):
		if(full):
			self.canvas.create_line(gap, gap, gap*2, gap, arrow="last")
			self.canvas.create_line(gap, gap, gap, gap*2, arrow="last")
		if(self.dimYLabel):
			self.canvas.delete(self.dimYLabel)
		self.dimYLabel=self.canvas.create_text((0, gap*3), text=dims[self.dimY])
		if(self.dimXLabel):
			self.canvas.delete(self.dimXLabel)
		self.dimXLabel=self.canvas.create_text((gap*3, gap), text=dims[self.dimX])
	def drawVisibleCells(self, accursed=None, ttl=10, x=paneWidth/2, y=paneHeight/2, push=None, prevCoord=None, prevCells=[], prevCellCenters=[]):
		fillColor=cellColor
		if accursed==None:
			accursed=self.accursed
			fillColor=self.hlColor
		if accursed in prevCells:
			target=prevCellCenters[prevCells.index(accursed)]
			middle=[x+target[0]/2, y+target[1]/2]
			if x>=target[0]:
				middle[0]+=200
			else:
				middle[0]-=200
			if y>=target[1]:
				middle[1]+=200
			else:
				middle[1]-=200
			self.canvas.tag_lower(self.canvas.create_line(x, y, middle[0], middle[1], target[0], target[1], smooth="bezier"))  
		else:
			if accursed.cloneHead() in prevCells:
				fillColor=cloneColor
			cellText=self.canvas.create_text((x, y), text=accursed.getValue(), width=maxLineWidth)
			bbox=self.canvas.bbox(cellText)
			if(bbox[2]-bbox[0]<minCellWidth):
				delta=(minCellWidth-(bbox[2]-bbox[0]))/2
				bbox=(bbox[0]-delta, bbox[1], bbox[2]+delta, bbox[3])
			if(bbox[3]-bbox[1]<minCellHeight):
				delta=(minCellHeight-(bbox[3]-bbox[1]))/2
				bbox=(bbox[0], bbox[1]-delta, bbox[2], bbox[3]+delta)
			if(push):
				deltaX=int(push[0]*(bbox[2]-bbox[0]))
				deltaY=int(push[1]*(bbox[3]-bbox[1]))
				bbox=(bbox[0]+deltaX, bbox[1]+deltaY, bbox[2]+deltaX, bbox[3]+deltaY)
				self.canvas.move(cellText, deltaX, deltaY)
				x+=deltaX
				y+=deltaY
			if(fillColor==cloneColor):
				target=prevCellCenters[prevCells.index(accursed.cloneHead())]
				middle=[x+target[0]/2, y+target[1]/2]
				if x>=target[0]:
					middle[0]+=200
				else:
					middle[0]-=200
				if y>=target[1]:
					middle[1]+=200
				else:
					middle[1]-=200
				self.canvas.tag_lower(self.canvas.create_line(x, y, middle[0], middle[1], target[0], target[1], smooth="bezier", dash=[2, 1], fill=cloneColor))
			if(fillColor==cellColor and accursed==self.other.accursed):
				fillColor=self.other.hlColor
			self.canvas.create_rectangle(bbox, fill=fillColor)
			if(fillColor!=cellColor and accursed==self.other.accursed):
				bbox2=(bbox[0]+(bbox[2]-bbox[0]/2), bbox[1], bbox[2], bbox[3])
				self.canvas.create_rectangle(bbox2, fill=self.other.hlColor)
			self.canvas.tag_raise(cellText)
			if(accursed.getNext(dims[self.dimX])):
				self.drawVisibleCells(accursed.getNext(dims[self.dimX], True), ttl-1, x+gap, y, (1,0), (x, y), prevCells+[accursed], prevCellCenters+[(x, y)])
			if(accursed.getNext(dims[self.dimX], False)):
				self.drawVisibleCells(accursed.getNext(dims[self.dimX], False), ttl-1, x-gap, y, (-1,0), (x, y), prevCells+[accursed], prevCellCenters+[(x, y)])
			if(accursed.getNext(dims[self.dimY])):
				self.drawVisibleCells(accursed.getNext(dims[self.dimY], True), ttl-1, x, y+gap, (0,1), (x, y), prevCells+[accursed], prevCellCenters+[(x, y)])
			if(accursed.getNext(dims[self.dimY], False)):
				self.drawVisibleCells(accursed.getNext(dims[self.dimY], False), ttl-1, x, y-gap, (0,-1), (x, y), prevCells+[accursed], prevCellCenters+[(x, y)])
		if(prevCoord):
			self.canvas.tag_lower(self.canvas.create_line(prevCoord[0], prevCoord[1], x, y))
	def clear(self):
		for item in self.canvas.find_all():
			self.canvas.delete(item)
	def refresh(self):
		self.clear()
		self.drawCompass()
		self.drawVisibleCells()
	def nav(self, dim, pos=True):
		if(self.operationMark):
			if(self.operationMark=="break"):
				self.accursed.breakConnection(dim, pos)
			elif(self.operationMark=="insert"):
				self.accursed.insert(dim, self.markedCell, pos)
			elif(self.operationMark=="new"):
				self.accursed.insert(dim, ZZCell(), pos)
			elif(self.operationMark=="hop"):
				self.accursed.hop(dim, pos)
			self.operationMark=None
		if(self.accursed.getNext(dim, pos)):
			self.accursed=self.accursed.getNext(dim, pos)
			self.refresh()
	def navPosX(self, *args, **kw_args):
		self.nav(dims[self.dimX], True)
	def navPosY(self, *args, **kw_args):
		self.nav(dims[self.dimY], True)
	def navNegX(self, *args, **kw_args):
		self.nav(dims[self.dimX], False)
	def navNegY(self, *args, **kw_args):
		self.nav(dims[self.dimY], False)
	def nextDimX(self, *args, **kw_args):
		self.dimX+=1
		if(self.dimX>len(dims)):
			self.dimX=0
		self.refresh()
	def nextDimY(self, *args, **kw_args):
		self.dimY+=1
		if(self.dimY>len(dims)):
			self.dimY=0
		self.refresh()
	def prevDimX(self, *args, **kw_args):
		self.dimX-=1
		if(self.dimX<0):
			self.dimX=len(dims)-1
		self.refresh()
	def prevDimY(self, *args, **kw_args):
		self.dimY-=1
		if(self.dimY<0):
			self.dimY=len(dims)-1
		self.refresh()
def main():
	top=tk()
	zzFrame=Frame(top)
	left=zzPane(zzFrame, hlColor=leftHLColor)
	right=zzPane(zzFrame, hlColor=rightHLColor)
	left.other=right
	right.other=left
	left.pack(side="left")
	right.pack(side="right")
	zzFrame.bind("<Key-s>", left.navNegX)
	zzFrame.bind("<Key-f>", left.navPosX)
	zzFrame.bind("<Key-e>", left.navNegY)
	zzFrame.bind("<Key-c>", left.navPosY)
	zzFrame.bind("<Key-j>", right.navNegX)
	zzFrame.bind("<Key-l>", right.navPosX)
	zzFrame.bind("<Key-i>", right.navNegY)
	zzFrame.bind("<Key-comma>", right.navPosY)
	zzFrame.bind("<Key-x>", left.nextDimX)
	zzFrame.bind("<Key-X>", left.prevDimX)
	zzFrame.bind("<Key-y>", left.nextDimY)
	zzFrame.bind("<Key-Y>", left.prevDimY)
	zzFrame.bind("<Key-Control-x>", right.nextDimX)
	zzFrame.bind("<Key-Control-X>", right.prevDimX)
	zzFrame.bind("<Key-Control-y>", right.nextDimY)
	zzFrame.bind("<Key-Control-Y>", right.prevDimY)
	zzFrame.pack()
