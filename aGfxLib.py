#!/usr/bin/env python
import pygame
from pygame.locals import *
from pygame import gfxdraw
import time

A1Ratio=11/8.5

Universe=[]
Exit=False

def init():
	pygame.init()
	pygame.font.init()
	pygame.display.set_mode((1024, 768))

def mainloop_body():
	for window in Universe:
		window.draw()
	pygame.display.flip()

def drawRoundRect(surface, x, y, width, height, bevelsize, color):
	gfxdraw.hline(surface, x+bevelsize, (x+width)-bevelsize, y, color)
	gfxdraw.hline(surface, x+bevelsize, (x+width)-bevelsize, y+height, color)
	gfxdraw.vline(surface, x, y+bevelsize, (y+height)-bevelsize, color)
	gfxdraw.vline(surface, x+width, y+bevelsize, (y+height)-bevelsize, color)
	gfxdraw.arc(surface, x+bevelsize, y+bevelsize, bevelsize, 180, 270, color)
	gfxdraw.arc(surface, x+width-bevelsize, y+bevelsize, bevelsize, 270, 360, color)	
	gfxdraw.arc(surface, x+bevelsize, y+height-bevelsize, bevelsize, 90, 180, color)
	gfxdraw.arc(surface, x+width-bevelsize, y+height-bevelsize, bevelsize, 0, 90, color)

class AContainer(object):
	def __init__(self, parent=None, children=None):
		global Universe
		self.surface=pygame.display.get_surface()
		self.parent=parent
		self.children=children
		if(children==None):
			self.children=[]
		for child in self.children:
			child.parent=self
		self.offsetX=0
		self.offsetY=0
		self.width=-1
		self.height=-1
		self.dirty=True
	def getHeight(self):
		if(self.parent):
			parentHeight=self.parent.getHeight()
		else:
			parentHeight=self.surface.get_height()
		if(self.height>0):
			if(self.height>parentHeight):
				return parentHeight-self.offsetY
			return self.height-self.offsetY
		return self.height+parentHeight-self.offsetY
	def getWidth(self):
		if(self.parent):
			parentWidth=self.parent.getWidth()
		else:
			parentWidth=self.surface.get_width()
		if(self.width>0):
			if(self.width>parentWidth):
				return parentWidth-self.offsetX
			return self.width-self.offsetX
		return self.width+parentWidth-self.offsetX
	def getX(self):
		parentX=0
		if(self.parent):
			parentX=self.parent.getX()
		return parentX+self.offsetX
	def getY(self):
		parentY=0
		if(self.parent):
			parentY=self.parent.getY()
		return parentY+self.offsetY
	def draw(self):
		self.dirty=False
		for child in self.children:
			child.draw()
class ATextChunk(AContainer):
	def __init__(self, parent=None, content="", color="orange", font=None, fontSize=6, editable=False):
		AContainer.__init__(self, parent)
		self.content=content
		self.color=Color(color)
		self.editable=editable
		self.fontSize=fontSize
		self.font=font
		self.antialias=True
		if(not font):
			self.font=pygame.font.Font(pygame.font.get_default_font(), self.fontSize)
		self.scrollPosition=0
	def renderText(self, text):
		return self.font.render(text, self.antialias, self.color)
	def splitWord(self, width, word):
		wordSize=self.font.size(word)
		offset=len(word)
		while wordSize[0]>width:
			offset-=1
			wordSize=self.font.size(word[:offset]+"-")
		self.renderedLines.append(self.renderText(word[:offset]+"-"))
		if(self.font.size(word[offset:])[0]>width):
			return self.splitWord(width, word[offset:])
		else:
			return word[offset:]
	def lineWrap(self, width, lines):
		self.renderedLines=[]
		self.lineStarts=[]
		for line in lines:
			self.lineStarts.append(len(self.renderedLines))
			estimatedSize=self.font.size(line)
			if(estimatedSize[0]>width):
				words=line.split(" ")
				if(len(words)==1):
					self.renderedLines.append(self.renderText(self.splitWord(width, words[0])))
				else:
					while(len(words)>0):
						offset=len(words)
						lineSize=self.font.size(" ".join(words))
						while(lineSize[0]>width):
							if(offset==1):
								wordEnd=self.splitWord(words[0])
								words[0]=wordEnd
								offset=len(words)
								lineSize=self.font.size(" ".join(words))
							else:
								offset-=1
								lineSize=self.font.size(" ".join(words[:offset]))
						self.renderedLines.append(self.renderText(" ".join(words[:offset])))
						if(offset==len(words)):
							words=[]
						else:
							words=words[offset:]
			else:
				self.renderedLines.append(self.renderText(line))
	def groupLines(self):
		groups=[]
		if(len(self.lineStarts)==1):
			return [self.renderedLines]
		for i in range(0, len(self.lineStarts)-1):
			groups.append(self.renderedLines[self.lineStarts[i]:self.lineStarts[i+1]])
		groups.append(self.renderedLines[self.lineStarts[-1]:])
		return groups
	def draw(self):
		x=self.getX()
		startY=self.getY()
		maxWidth=self.getWidth()
		height=self.getHeight()
		self.surface.fill(Color("black"), (x, startY, x+maxWidth, startY+height))
		lines=self.content.split("\n")
		self.lineWrap(maxWidth, lines)
		linesToDraw=self.groupLines()[self.scrollPosition:]
		cumulative_height=0
		for group in linesToDraw:
			for line in group:
				line_height=line.get_height()
				if(cumulative_height+line_height>height):
					return
				self.surface.blit(line, (x, startY+cumulative_height))
				cumulative_height+=line_height

class AWindow(AContainer):
	def __init__(self, parent=None, children=None, borderWidth=5, color="orange", beveled=True):
		child=AContainer(self, children)
		child.offsetX=borderWidth+1
		child.offsetY=borderWidth+1
		child.width=-(borderWidth+1)
		child.height=-(borderWidth+1)
		AContainer.__init__(self, parent, [child])
		self.borderWidth=borderWidth
		self.color=Color(color)
		self.beveled=beveled
		self.width=200
		self.height=int(self.width*A1Ratio)
		Universe.append(self)
	def draw(self):
		drawRoundRect(self.surface, self.getX(), self.getY(), self.width, self.height, self.borderWidth, self.color)
		for child in self.children:
			child.draw()

def windowTest():
	init()
	text=ATextChunk(content="hello, world!\nThis is a new line\nThis is a very long line and the next line should contain a single word that is also very long hold on let me pad out the line so we definitely wrap... ok here we go!\nThis_is_a_very_long_line_and_the_next_line_should_contain_a_single_word_that_is_also_very_long_hold_on_let_me_pad_out_the_line_so_we_definitely_wrap..._ok_here_we_go!\n\n\nThere should have just been two blank lines\nNow we want to make our line wrap to the very end of the box and we can do that by being very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long", fontSize=10)
	window=AWindow(children=[text])
	mainloop_body()
	time.sleep(1)
	text.scrollPosition+=1
	mainloop_body()
	time.sleep(1)
	text.scrollPosition+=1
	mainloop_body()
	time.sleep(1)
	text.scrollPosition+=1
	mainloop_body()
	time.sleep(1)
	text.scrollPosition+=1
	mainloop_body()
windowTest()
