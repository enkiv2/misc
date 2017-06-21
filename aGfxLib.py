#!/usr/bin/env python
import pygame
from pygame.locals import *
from pygame import gfxdraw
import time

A1Ratio=11/8.5

Universe=[]
Exit=False
FocusedWidget=None

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
	# TODO: drag_accept, drag_sprite_draw, drag_sprite_erase, takeFocus
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
		self.initialOffsetX=0	# for flow
		self.initialOffsetY=0	# for flow
		self.width=-1
		self.height=-1
		self.dirty=True
		self.bgcolor=Color("black")
		self.packMode="horizontal"
		self.alignment="center"
		self.fill=True
		self.flowable=False
		self.visible=True
		self.packed=False
	def flow(self, initalOffsetX, initialOffsetY):
		# Flow is an alternative to pack for things like text
		# In other words, you have a head and tail that's possibly
		# less wide than the 'body' and can link up with the respective
		# tail and head of something else.
		if(flowable):
			self.initialOffsetX=initialOffsetX
			self.initialOffsetY=initialOffsetY
		else:
			self.offsetY+=initialOffsetY
	def pack(self, mode="horizontal", align="center", fill=True):
		self.setDirty()
		self.packMode=mode
		self.alignment=align
		self.fill=fill
		self.packed=True
		self.repack()
	def repack(self):
		numChildren=len(self.children)
		height=self.getHeight()
		width=self.getWidth()
		positions=[]
		if(self.packMode=="vertical"):
			delta=int(height/numChildren)
		else:
			delta=int(width/numChildren)
		for i in range(0, len(self.children)):
			child=self.children[i]
			if(self.packMode=="vertical"):
				child.deltaX=0
				child.deltaY=i*delta
			else:
				child.deltaX=i*delta
				child.deltaY=0
		for child in self.children:
			if(child.packed):
				child.pack(child.packMode, self.alignment, self.fill)
	def setDirty(self):
		self.dirty=True
	def setDirtyCascade(self):
		self.setDirty()
		for child in self.children:
			child.setDirtyCascade()
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
				return parentWidth
			return self.width
		return self.width+parentWidth
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
	def findParentWindow(self):
		p=self
		while(p!=None and type(p)!=type(AWindow)):
			p=p.parent
		return p
	def updateWindowCascade(self, above=True):
		p=self.findParentWindow()
		if(p!=None):
			i=0
			try:
				i=Universe.index(p)
			except:
				return
			if(above):
				wids=Universe[i:]
			else:
				wids=Universe[:i]
			for wid in wids:
				wid.setDirtyCascade()
	def move(self, x, y):
		self.hide()
		self.offsetX=x
		self.offsetY=y
		self.show()
	def hide(self):
		self.erase()
		self.visible=False
	def show(self):
		self.visible=True
		self.dirty=True
	def erase(self):
		x=self.getX()
		y=self.getY()
		self.surface.fill(Color("black"), (x, y, x+self.width+1, y+self.height+1))
	def draw(self):
		if(self.visible):
			if(self.dirty):
				self.erase()
				self.draw_r()
			self.dirty=False
			for child in self.children:
				child.draw()
	def draw_r(self):
		pass
class ATextChunk(AContainer): # TODO implement flow support & move scrolling to a new scrollingcontainer class: this class should just be noodles
	def __init__(self, parent=None, content="", color="orange", font=None, fontSize=6, editable=False, bgcolor=None):
		AContainer.__init__(self, parent)
		self.content=content
		self.color=Color(color)
		self.bgcolor=bgcolor
		if(bgcolor):
			self.bgcolor=Color(bgcolor)
		else:
			self.bgcolor=Color(0, 0, 0, 0)
		self.editable=editable
		self.fontSize=fontSize
		self.font=font
		self.antialias=True
		if(not font):
			self.font=pygame.font.Font(pygame.font.get_default_font(), self.fontSize)
		self.scrollPosition=0
		self.scrollIndicatorWidth=10
		self.fillScrollIndicator=True
		self.invert=False
	def setScroll(self, pos):
		self.scrollPostion=pos
		self.setDirty()
	def scroll(self, delta=1):
		self.scrollPosition+=delta
		self.setDirty()
	def renderText(self, text):
		if(self.invert):
			return self.font.render(text, self.antialias, self.bgcolor, self.color)
		return self.font.render(text, self.antialias, self.color, self.bgcolor)
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
	def drawText(self, x, startY, maxWidth, height):
		lines=self.content.split("\n")
		self.lineWrap(maxWidth, lines)
		groups=self.groupLines()
		linesToDraw=groups[self.scrollPosition:]
		cumulative_height=0
		for group in linesToDraw:
			for line in group:
				line_height=line.get_height()
				if(cumulative_height+line_height>height):
					return len(groups)
				self.surface.blit(line, (x, startY+cumulative_height))
				cumulative_height+=line_height
		return len(groups)
	def drawScrollIndicator(self, x, y, maxWidth, height, groupCount):
		if(groupCount==0):
			groupCount=1
		position=(height)*((0.5+self.scrollPosition)/groupCount)
		if(self.fillScrollIndicator):
			gfxdraw.filled_circle(self.surface, x+maxWidth+int(self.scrollIndicatorWidth/2)+1, y+int(position), int(self.scrollIndicatorWidth/2)-2, self.color)
		else:
			gfxdraw.circle(self.surface, x+maxWidth+int(self.scrollIndicatorWidth/2)+1, y+int(position), int(self.scrollIndicatorWidth/2)-2, self.color)
	def draw_r(self):
		x=self.getX()
		startY=self.getY()
		maxWidth=self.getWidth()-self.scrollIndicatorWidth
		height=self.getHeight()
		groupCount=self.drawText(x, startY, maxWidth, height)
		self.drawScrollIndicator(x, startY, maxWidth, height, groupCount)

class AWindow(AContainer):
	def __init__(self, parent=None, children=None, borderWidth=5, color="orange", beveled=True):
		child=AContainer(self, children)
		child.offsetX=borderWidth+1
		child.offsetY=borderWidth+1
		child.width=-(borderWidth+2)
		child.height=-(borderWidth+2)
		AContainer.__init__(self, parent, [child])
		self.borderWidth=borderWidth
		self.color=Color(color)
		self.beveled=beveled
		self.width=200
		self.height=int(self.width*A1Ratio)
		Universe.append(self)
	def draw_r(self):
		if(self.beveled):
			drawRoundRect(self.surface, self.getX(), self.getY(), self.width, self.height, self.borderWidth, self.color)
		else:
			gfxdraw.rectangle(self.surface, (self.getX(), self.getY(), self.getX()+self.getWidth(), self.getY()+self.getHeight()), self.color)
		for child in self.children:
			child.draw()

class AWindowDecoration(AContainer):
	def __init__(self, parent=None, borderWidth=5, color="orange", beveled=True, title="AGfxLib - Untitled Window", font=None, fontSize=12, bevelSize=5):
		self.parent=parent
		AContainer.__init__(self, parent, [])
		self.borderWidth=borderWidth
		self.color=Color(color)
		self.beveled=beveled
		self.title=title
		self.titleRendered=None
		self.fontSize=fontSize
		self.font=font
		self.antialias=True
		self.bevelSize=bevelSize
		if(not font):
			self.font=pygame.font.Font(pygame.font.get_default_font(), self.fontSize)
		self.titleSize=self.font.size(self.title)
		self.buttonWidth=self.titleSize[1]
		self.maxTitleWidth=self.titleSize[0]
		self.width=self.titleSize[0]+3*self.buttonWidth+2*self.bevelSize
		self.height=self.titleSize[1]+2*self.bevelSize
	def drawButtons(self):
		buttonR=int(self.buttonWidth/2)
		gfxdraw.filled_circle(self.surface, self.getX()+self.width-buttonR, self.getY()+buttonR, buttonR, self.color)
		gfxdraw.circle(self.surface, self.getX()+self.width-buttonR-self.buttonWidth, self.getY()+buttonR, buttonR, self.color)
	def draw_r(self):
		if(self.beveled):
			drawRoundRect(self.surface, self.getX(), self.getY(), self.width, self.height, self.bevelSize, self.color)
		else:
			gfxdraw.rectangle(self.surface, (self.getX(), self.getY(), self.getX()+self.getWidth(), self.getY()+self.getHeight()), self.color)
		if not self.titleRendered:
			if(self.font.size(self.title)[0]>self.maxTitleWidth):
				title=self.title
				offset=len(title)
				while(self.font.size(title+"...")[0]>self.maxTitleWidth):
					if(offset==1):
						title=""
						break
					offset-=1
					title=title[:offset]
				if(title):
					self.titleRendered=self.font.render(title+"...", self.antialias, self.color)
				else:
					self.titleRendered=self.font.render("", self.antialias, self.color)
			else:
				self.titleRendered=self.font.render(self.title, self.antialias, self.color)
		self.surface.blit(self.titleRendered, (self.getX()+self.bevelSize, self.getY()+self.bevelSize))
		self.drawButtons()
		
		
class ADecoratedWindow(AContainer):
	def __init__(self, parent=None, children=None, borderWidth=5, color="orange", beveled=True, title="AGfxLib - Untitled Window"):
		global Universe
		self.childWindow=AWindow(self, children, borderWidth, color, beveled)
		try:
			Universe.remove(self.childWindow)	# since we are decorated don't double-store the window in list
		except:
			pass
		self.childDecoration=AWindowDecoration(self, borderWidth, color, beveled, title)
		AContainer.__init__(self, parent, [self.childDecoration, self.childWindow])
		self.width=max(self.childDecoration.width, self.childWindow.width)
		self.childDecoration.width=self.width
		self.childWindow.width=self.width
		self.height=self.childDecoration.height+self.childWindow.height
		self.childWindow.offsetY=self.childDecoration.height
		Universe.append(self)
	def iconify(self):
		self.childWindow.hide()
		self.childDecoration.setDirty()
	def deiconify(self):
		self.childWindow.show()
		self.childDecoration.setDirty()
	def close(self):
		self.childWindow.hide()
		self.childDecoration.hide()
		try:
			Universe.remove(self.childWindow)
		except:
			pass
		Universe.remove(self)
	def draw_r(self):
		self.width=max(self.childDecoration.width, self.childWindow.width)
		self.childDecoration.width=self.width
		self.childWindow.width=self.width
		self.height=self.childDecoration.height+self.childWindow.height
		self.childWindow.offsetY=self.childDecoration.height
		self.childDecoration.setDirty()
		self.childWindow.setDirty()

def windowTest():
	init()
	text=ATextChunk(content="hello, world!\nThis is a new line\nThis is a very long line and the next line should contain a single word that is also very long hold on let me pad out the line so we definitely wrap... ok here we go!\nThis_is_a_very_long_line_and_the_next_line_should_contain_a_single_word_that_is_also_very_long_hold_on_let_me_pad_out_the_line_so_we_definitely_wrap..._ok_here_we_go!\n\n\nThere should have just been two blank lines\nNow we want to make our line wrap to the very end of the box and we can do that by being very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long", fontSize=10)
	window=ADecoratedWindow(children=[text])
	for i in range(0, 5):
		mainloop_body()
		time.sleep(1)
		text.scroll()
		text.invert=(not text.invert)
		window.move(i*10, i*15)
	for i in range(0, 5):
		mainloop_body()
		time.sleep(1)
		text.scroll(-1)
		text.invert=(not text.invert)
		window.move(50+i*15, 75-i*10)
	window.iconify()
	mainloop_body()
	time.sleep(1)
	window.deiconify()
	mainloop_body()
	time.sleep(1)


windowTest()
