#!/usr/bin/env python

# LEGAL NOTE:
# ZigZag(R) is a registered trademark of Project Xanadu(R).
# This implementation is covered by US Patent 262736B1! Until it expires, do not use it without permission from Ted Nelson.

from ZZCell import *
import kaukatcr
import sys

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

		
operationMark=None
markedCell=None

dims=[]
for i in range(0, 9):
	dims.append("d."+str(i))
dims.extend(["d.exec", "d.branch", "d.comment", "d.stack", "d.funcs"])
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
		if(accursed==0):
			self.accursed=cells[accursed]
		self.hlColor=hlColor
		self.other=None
		self.dimX=0
		self.dimY=1
		self.canvas=Tkinter.Canvas(parent, width=paneWidth, height=paneHeight)
		self.dimYLabel=None; self.dimXLabel=None
		self.prevCells=[]; self.prevCellCenters=[]
		self.editMode=False
	def pack(self, *args):
		self.canvas.pack(*args)
	def drawCompass(self, full=False):
		if(full):
			self.canvas.create_line(gap, gap, gap*2, gap, arrow="last")
			self.canvas.create_line(gap, gap, gap, gap*2, arrow="last")
		if(self.dimYLabel):
			self.canvas.delete(self.dimYLabel)
		self.dimYLabel=self.canvas.create_text((gap, gap*3), text=dims[self.dimY])
		if(self.dimXLabel):
			self.canvas.delete(self.dimXLabel)
		self.dimXLabel=self.canvas.create_text((gap*3, gap), text=dims[self.dimX])
	def drawLinkToAlreadyVisibleCell(self, accursed, x, y, prevCoord, push):
		target=self.prevCellCenters[self.prevCells.index(accursed)]
		middle1=[x+push[0]*gap*2, y+push[1]*gap*2]
		middle3=[target[0]-push[0]*gap*2, target[1]-push[1]*gap*2]
		middle2=[(x+target[0])/2, (y+target[1])/2]
		if x==target[0]:
			middle2[0]+=2*gap
		if y==target[1]:
			middle2[1]+=2*gap
		self.canvas.tag_lower(self.canvas.create_line(x, y, middle1[0], middle1[1], middle2[0], middle2[1], middle3[0], middle3[1], target[0], target[1], smooth="bezier", arrow="last"))
	def drawCell(self, accursed, x, y, push, prevCoord, fillColor):
		if accursed.cloneHead() in self.prevCells:
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
		if(accursed.cloneHead() in self.prevCells):
			print(accursed.cloneHead())
			target=self.prevCellCenters[self.prevCells.index(accursed.cloneHead())]
			middle=[x+target[0]/2, y+target[1]/2]
			if x>=target[0]:
				middle[0]+=200
			else:
				middle[0]-=200
			if y>=target[1]:
				middle[1]+=200
			else:
				middle[1]-=200
			self.canvas.tag_lower(self.canvas.create_line(x, y, middle[0], middle[1], target[0], target[1], smooth="bezier", dash=[2, 1], fill=cloneColor, outline=cloneColor))
		if(fillColor==cellColor and accursed==self.other.accursed):
			fillColor=self.other.hlColor
		self.canvas.create_rectangle(bbox, fill=fillColor)
		if(accursed==self.accursed and accursed==self.other.accursed):
			bbox2=(bbox[0]+((bbox[2]-bbox[0])/2), bbox[1], bbox[2], bbox[3])
			self.canvas.create_rectangle(bbox2, fill=self.other.hlColor)
		self.canvas.tag_raise(cellText)
		return (x, y)
	def drawVisibleCells(self, accursed=None, ttl=10, x=paneWidth/2, y=paneHeight/2, push=None, prevCoord=None, drawn=[]):
		fillColor=cellColor
		if accursed==None:
			accursed=self.accursed
			fillColor=self.hlColor
		if accursed in drawn:
			return
		print(self.prevCells)
		print(accursed in self.prevCells)
		if accursed in self.prevCells:
			return self.drawLinkToAlreadyVisibleCell(accursed, x, y, prevCoord, push)
		else:
			(x, y)=self.drawCell(accursed, x, y, push, prevCoord, fillColor)
			self.prevCells+=[accursed]
			self.prevCellCenters+=[(x, y)]
			if(accursed.getNext(dims[self.dimX])):
				self.drawVisibleCells(accursed.getNext(dims[self.dimX], True), ttl-1, x+gap, y, (1,0), (x, y), drawn+[accursed])
			if(accursed.getNext(dims[self.dimX], False)):
				self.drawVisibleCells(accursed.getNext(dims[self.dimX], False), ttl-1, x-gap, y, (-1,0), (x, y), drawn+[accursed])
			if(accursed.getNext(dims[self.dimY])):
				self.drawVisibleCells(accursed.getNext(dims[self.dimY], True), ttl-1, x, y+gap, (0,1), (x, y), drawn+[accursed])
			if(accursed.getNext(dims[self.dimY], False)):
				self.drawVisibleCells(accursed.getNext(dims[self.dimY], False), ttl-1, x, y-gap, (0,-1), (x, y), drawn+[accursed])
		if(prevCoord):
			self.canvas.tag_lower(self.canvas.create_line(prevCoord[0], prevCoord[1], x, y))
	def clear(self):
		for item in self.canvas.find_all():
			self.canvas.delete(item)
		self.canvas.delete(ALL)
	def _refresh(self):
		self.clear()
		self.drawCompass(True)
		self.prevCells=[]
		self.prevCellCenters=[]
		self.toDraw=[]
		self.drawVisibleCells()
	def refresh(self):
		print("Cells")
		for cell in cells:
			print(str(cell.compressedRep()))
		self._refresh()
		self.other._refresh()
	def nav(self, dim, pos=True):
		if self.editMode:
			return
		global operationMark
		if(operationMark):
			if(operationMark=="break"):
				self.accursed.breakConnection(dim, pos)
			elif(operationMark=="insert"):
				self.accursed.insert(dim, markedCell, pos)
			elif(operationMark=="new"):
				self.accursed.insert(dim, ZZCell(""), pos)
			elif(operationMark=="hop"):
				self.accursed.hop(dim, pos)
			self.refresh()
			operationMark=None
			return
		if(self.accursed.getNext(dim, pos)):
			print(self.accursed.getNext(dim, pos))
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
		if self.editMode:
			return
		self.dimX+=1
		if(self.dimX>len(dims)):
			self.dimX=0
		self.refresh()
	def nextDimY(self, *args, **kw_args):
		if self.editMode:
			return
		self.dimY+=1
		if(self.dimY>len(dims)):
			self.dimY=0
		self.refresh()
	def prevDimX(self, *args, **kw_args):
		if self.editMode:
			return
		self.dimX-=1
		if(self.dimX<0):
			self.dimX=len(dims)-1
		self.refresh()
	def prevDimY(self, *args, **kw_args):
		if self.editMode:
			return
		self.dimY-=1
		if(self.dimY<0):
			self.dimY=len(dims)-1
		self.refresh()
	def markAccursed(self, *arg, **kw_args):
		if self.editMode:
			return
		global markedCell
		markedCell=self.accursed
		print("Marked: "+str(markedCell))
		self.refresh()
	def toggleEdit(self, *arg, **kw_args):
		if(self.editMode):
			self.accursed.cloneHead().value=self.editBox.get("0.0", END)
			self.canvas.refresh()
		else:
			self.editBox=Tkinter.Text(self.canvas)
			self.editBox.delete("0.0", END)
			self.editBox.insert("0.0", self.accursed.getValue())
			self.canvas.create_window((paneWidth/2, paneHeight/2), window=editBox)
		self.editMode=not self.editMode
def setupTK():
	global top, left, right
	try:
		top=Tkinter.tk()
	except:
		top=Tkinter.Tk()
	zzFrame=Tkinter.Frame(top)
	left=ZZPane(zzFrame, hlColor=leftHLColor)
	right=ZZPane(zzFrame, hlColor=rightHLColor)
	left.other=right
	right.other=left
	left.canvas.pack(side="left")
	right.canvas.pack(side="right")
	top.bind("<Key-s>", left.navNegX)
	top.bind("<Key-f>", left.navPosX)
	top.bind("<Key-e>", left.navNegY)
	top.bind("<Key-c>", left.navPosY)
	top.bind("<Key-j>", right.navNegX)
	top.bind("<Key-l>", right.navPosX)
	top.bind("<Key-i>", right.navNegY)
	top.bind("<Key-comma>", right.navPosY)
	top.bind("<Key-x>", left.nextDimX)
	top.bind("<Key-X>", left.prevDimX)
	top.bind("<Key-y>", left.nextDimY)
	top.bind("<Key-Y>", left.prevDimY)
	top.bind("<Control-Key-x>", right.nextDimX)
	top.bind("<Control-Key-X>", right.prevDimX)
	top.bind("<Control-Key-y>", right.nextDimY)
	top.bind("<Control-Key-Y>", right.prevDimY)
	def opMarkHelper(mark, *arg, **argv):
		if left.editMode:
			return
		global operationMark
		print("Mark: "+mark)
		sys.stdout.flush()
		operationMark=mark
	def opBreak(*arg, **argv):
		opMarkHelper("break", *arg, **argv)
	def opNew(*arg, **argv):
		opMarkHelper("new", *arg, **argv)
	def opHop(*arg, **argv):
		opMarkHelper("hop", *arg, **argv)
	def opLink(*arg, **argv):
		opMarkHelper("insert", *arg, **argv)
	top.bind("<Key-b>", opBreak)
	top.bind("<Key-exclam>", opBreak)
	top.bind("<Key-n>", opNew)
	top.bind("<Key-h>", opHop)
	top.bind("<Key-bar>", opLink)
	top.bind("<Key-m>", left.markAccursed)
	top.bind("<Key-M>", right.markAccursed)
	def execHelper(*arg, **argv):
		kaukatcr.execute(left.accursed)
		left.refresh()
	top.bind("<Key-Return>", execHelper)
	top.bind("<Key-Tab>", left.toggleEdit)
	zzFrame.pack()
def main():
	home=ZZCell("Home")
	setupTK()
	left.refresh()
	top.mainloop()

if __name__=="__main__":
	main()
