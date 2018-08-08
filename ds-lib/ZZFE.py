#!/usr/bin/env python

# LEGAL NOTE:
# ZigZag(R) is a registered trademark of Project Xanadu(R).

# While I have written ZigZag implementations officially for Project Xanadu, 
# this implementation shares no code with those. This code contains no material
# under trade secret protection related to Project Xanadu.
#
# Please refer to a collection of these objects as a ZZStructure, rather than
# ZigZag(R).
#
# This implementation is covered by US Patent 262736B1.

from ZZCell import *
import kaukatcr
import sys

try:
	import cPickle as pickle
except:
	import pickle

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
paneWidth=1200
paneHeight=1000
gap=20
maxLineWidth=700
minCellWidth=20
minCellHeight=50

sliceFilename="home.zzp"
		
operationMark=None
markedCell=None

dims=[]
for i in range(0, 9):
	dims.append("d."+str(i))
dims.extend(["d.exec", "d.branch", "d.comment", "d.stack", "d.funcs"])
dims.append("d.clone")

def refreshDimList():
	storedDims=[]
	if len(cells)>0:
		if cells[0].getNext("d.dimList"):
			head=cells[0].getNext("d.dimList")
			while head:
				storedDims.append(head.getValue())
				head=head.getNext("d.dimList")
		usedDims=[]
		usedDims.extend(storedDims)
		for cell in cells:
			usedDims.extend(cell.getDims())
			usedDims=list(set(usedDims))
		for dim in usedDims:
			if not (dim in dims):
				dims.append(dim)
		for dim in dims:
			if not (dim in storedDims):
				cells[0].rankHead("d.dimList", True).setNext("d.dimList", ZZCell(dim))

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
		op=operationMark
		if(op==None):
			op="move"
		statusLine="Accursed: "+str(self.accursed.cid)+", Marked: "+str(markedCell)+", Operation: "+str(op)+", Slice: "+sliceFilename+", "+str(len(cells))+" cells resident"
		print(statusLine)
		self.canvas.create_text((paneWidth/2, paneHeight-gap), text=statusLine)
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
	def sizeCell(self, accursed, x, y, push, prevCoord, fillColor):
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
		return (x, y, fillColor, cellText, bbox)
	def drawCell(self, accursed, x, y, fillColor, bbox):
		self.canvas.create_rectangle(bbox, fill=fillColor)
		if(accursed==self.accursed and accursed==self.other.accursed):
			bbox2=(bbox[0]+((bbox[2]-bbox[0])/2), bbox[1], bbox[2], bbox[3])
			self.canvas.create_rectangle(bbox2, fill=self.other.hlColor)
	def drawVisibleCells(self, accursed=None, ttl=10, x=paneWidth/2-250, y=paneHeight/2-250, push=None, prevCoord=None, drawn=[]):
		fillColor=cellColor
		if accursed==None:
			accursed=self.accursed
			fillColor=self.hlColor
		if accursed in drawn:
			return
		if accursed in self.prevCells:
			return self.drawLinkToAlreadyVisibleCell(accursed, x, y, prevCoord, push)
		else:
			(x, y, fillColor, cellText, bbox)=self.sizeCell(accursed, x, y, push, prevCoord, fillColor)
			self.prevCells+=[accursed]
			self.prevCellCenters+=[(x, y)]
			if(accursed.getNext(dims[self.dimX])):
				self.drawVisibleCells(accursed.getNext(dims[self.dimX], True), ttl-1, x+gap, y, (0.75,0), (x, y), drawn+[accursed])
			if(accursed.getNext(dims[self.dimX], False)):
				self.drawVisibleCells(accursed.getNext(dims[self.dimX], False), ttl-1, x-gap, y, (-0.75,0), (x, y), drawn+[accursed])
			if(accursed.getNext(dims[self.dimY])):
				self.drawVisibleCells(accursed.getNext(dims[self.dimY], True), ttl-1, x, y+gap, (0,0.75), (x, y), drawn+[accursed])
			if(accursed.getNext(dims[self.dimY], False)):
				self.drawVisibleCells(accursed.getNext(dims[self.dimY], False), ttl-1, x, y-gap, (0,-0.75), (x, y), drawn+[accursed])
			self.drawCell(accursed, x, y, fillColor, bbox)
			self.canvas.tag_raise(cellText)
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
		self._refresh()
		self.other._refresh()
	def nav(self, dim, pos=True):
		if self.editMode or self.other.editMode:
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
		if self.editMode or self.other.editMode:
			return
		self.dimX+=1
		if(self.dimX>len(dims)):
			self.dimX=0
		self.refresh()
	def nextDimY(self, *args, **kw_args):
		if self.editMode or self.other.editMode:
			return
		self.dimY+=1
		if(self.dimY>len(dims)):
			self.dimY=0
		self.refresh()
	def prevDimX(self, *args, **kw_args):
		if self.editMode or self.other.editMode:
			return
		self.dimX-=1
		if(self.dimX<0):
			self.dimX=len(dims)-1
		self.refresh()
	def prevDimY(self, *args, **kw_args):
		if self.editMode or self.other.editMode:
			return
		self.dimY-=1
		if(self.dimY<0):
			self.dimY=len(dims)-1
		self.refresh()
	def markAccursed(self, *arg, **kw_args):
		if self.editMode or self.other.editMode:
			return
		global markedCell
		markedCell=self.accursed
		self.refresh()
	def enableEdit(self, *arg, **kw_args):
		self.editBox=Tkinter.Text(self.canvas)
		self.editBox.delete("0.0", END)
		self.editBox.insert("0.0", self.accursed.getValue())
		self.canvas.create_window((paneWidth/2, paneHeight/2), window=self.editBox)
		self.editMode=True
	def disableEdit(self, *arg, **kw_args):
		if(self.editMode and self.editBox):
			self.accursed.cloneHead().value=self.editBox.get("0.0", END)
			self.refresh()
		self.editMode=False
def saveSlice(filename):
	refreshDimList()
	with open(filename, 'w') as f:
		pickle.dump(cells, f)
def autoSave(*args, **argv):
	saveSlice(sliceFilename)
def loadSlice(filename):
	global cells
	with open(filename, 'r') as f:
		cells=pickle.load(f)
	refreshDimList()

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
	left.canvas.pack(side="left", fill="both")
	right.canvas.pack(side="right", fill="both")
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
		if left.editMode:
			return
		kaukatcr.execute(left.accursed)
		left.refresh()
	top.bind("<Key-Return>", execHelper)
	top.bind("<Key-Tab>", left.enableEdit)
	top.bind("<Key-Escape>", left.disableEdit)
	top.bind("<Control-Key-s>", autoSave)
	def saveAsHelper(*args, **argv):
		global sliceFilename
		name=tkFileDialog.asksaveasfilename(initialfile=sliceFilename, filetypes=[("ZigZag pickle", "*.zzp")])
		if(name):
			if (name!=sliceFilename):
				try:
					saveSlice(name)
					sliceFilename=name
					left.refresh()
				except:
					pass
	top.bind("<Control-Key-a>", saveAsHelper)
	def openHelper(*args, **argv):
		global sliceFilename
		name=tkFileDialog.askopenfilename(initialfile=sliceFilename, filetypes=[("ZigZag pickle", "*.zzp")])
		if(name):
			if (name!=sliceFilename):
				try:
					loadSlice(name)
					sliceFilename=name
					left.refresh()
				except:
					pass
	top.bind("<Control-Key-o>", openHelper)
	def cloneheadHelper(pane):
		if left.editMode:
			return
		pane.accursed=pane.accursed.cloneHead()
		pane.refresh()
	def cloneheadHelperLeft(*arg, **args):
		cloneheadHelper(left)
	def cloneheadHelperRight(*arg, **args):
		cloneheadHelper(right)
	top.bind("<Key-o>", cloneheadHelperLeft)
	top.bind("<Key-O>", cloneheadHelperLeft)
	def shl(*arg, **args):
		if left.editMode:
			return
		left.accursed=right.accursed
		left.refresh()
	def shr(*arg, **args):
		if left.editMode:
			return
		right.accursed=left.accursed
		left.refresh()
	top.bind("<Key-less>", shl)
	top.bind("<Key-greater>", shr)
	def opClone(pane, *arg, **args):
		if left.editMode:
			return
		global markedCell
		markedCell=pane.accursed.clone()
		opLink(*arg, **args)
	def opCloneLeft(*arg, **args):
		opClone(left, *arg, **args)
	def opCloneRight(*arg, **args):
		opClone(right, *arg, **args)
	top.bind("<Key-t>", opCloneLeft)
	top.bind("<Key-T>", opCloneRight)
	def exitHelper(*arg, **args):
		sys.exit()
	top.bind("<Control-Key-q>", exitHelper)
	zzFrame.pack(fill="both")

def main():
	global cells
	global sliceFilename
	if len(sys.argv)>1:
		loadSlice(sys.argv[1])
		sliceFilename=sys.argv[1]
	if(len(cells)==0):
		try:
			loadSlice(sliceFilename)
		except Exception as e:
			print(e)
			home=ZZCell("Home")
			home.setNext("d.0", ZZCell(
"""HOW TO USE THIS APPLICATION
m/M - mark accursed cell in left/right pane      b/! - break connection (in direction)
h   - hop                                        |   - link accursed cell to marked cell (in direction)
e/c - up/down in left pane                       i/, - up/down in right pane
s/f - left/right in left pane                    j/l - left/right in right pane
tab - edit accursed cell in left pane            t/T - clone left/right accursed cell & mark that clone 
       (or exit edit mode)                               for insertion
x/X - step through dim list for x on left pane   CTRL-x/CTRL-X - step through dim list for x on right
y/Y - step through dim list for y on left pane   CTRL-y/CTRL-Y - step through dim list for y on right

CTRL-s - save     CTRL-o - open                   
CTRL-a - save as  Enter  - execute accursed cell                                        CTRL-q - exit
                            (left pane)
"""))
			home.setNext("d.1", ZZCell(
"""
(c) 2018 John Ohno
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

ZigZag(R) is a registered trademark of Project Xanadu(R).

While I have written ZigZag implementations officially for Project Xanadu, 
this implementation shares no code with those. This code contains no material
under trade secret protection related to Project Xanadu, nor is it officially
approved by Ted Nelson or Project Xanadu.

This implementation is covered by US Patent 262736B1. Please do not use without
permission from Ted Nelson.
"""))
			refreshDimList()
			saveSlice(sliceFilename)
	setupTK()
	left.refresh()
	top.mainloop()

if __name__=="__main__":
	main()
