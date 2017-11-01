#!/usr/bin/env python
import sys, os, math
from PIL import Image, ImageOps, ImageFont, ImageDraw, ImageChops
from random import Random
random=Random()

global LENGTH
LENGTH=10

cursive=True
#cursive=False

def buildMarkovModel(vocab):
	model={}
	# Sentences is a fake corpus, which we create by iteratively adding to the end of random phrases
	# This generates the correct term frequency distribution in the resulting markov model, so it resembles a language
	sentences=[[]]
	for i in range(1, 1000):
		for j in range(0, len(vocab)):
			target=random.choice(range(0, len(sentences)+1))
			if(target>=len(sentences)):
				sentences.append([random.choice(vocab)])
			else:
				sentences[target].append(random.choice(vocab))
        print(sentences)
	for sentence in sentences:
		lastItem=""
		for item in sentence+[""]:
			if not (lastItem in model):
				model[lastItem]=[]
			model[lastItem].append(item)
			lastItem=item
	return model

def iterateModel(model, termMax, start=""):
	i=0
	item=random.choice(model[start])
        res=[item]
	item=random.choice(model[item])
	while(item!="" and i>termMax):
		i+=1
		res.append(item)
		item=random.choice(model[item])
	return res


class Line:
	def __init__(self, halfsize=False):
		self.halfsize=halfsize
	def __str__(self):
		return repr(self)
	def __repr__(self):
		#return "{type: Line, halfsize: "+str(self.halfsize)+"}"
		if(self.halfsize):
			return "a"
		return "u"
	def draw(self, pen):
		global LENGTH
		length=LENGTH
		if(self.halfsize):
			length=length/2
		pen.forward(length)
class Semicircle:
	def __init__(self, halfsize=False):
		self.halfsize=halfsize
	def __str__(self):
		return repr(self)
	def __repr__(self):
		#return "{type: Semicircle halfsize: "+str(self.halfsize)+"}"
		if(self.halfsize):
			return "e"
		return "o"
	def draw(self, pen):
		global LENGTH
		length=LENGTH
		if(self.halfsize):
			length=length/2
		pen.circle(length/2, 180)

class Acute:
	def __init__(self):
		pass
	def draw(self, pen):
		global LENGTH
		pos=pen.position()
		pen.goto(pos[0], pos[1]-(LENGTH/8))
		pen.pendown()
		pen.goto(pos[0]+(LENGTH/4), pos[1]+(LENGTH/8))
		pen.penup()
class Grave:
	def __init__(self):
		pass
	def draw(self, pen):
		global LENGTH
		pos=pen.position()
		pen.pendown()
		pen.goto(pos[0]+(LENGTH/4), pos[1]-(LENGTH/8))
		pen.penup()
		pen.goto(pos[0]+(LENGTH/4), pos[1])
class Circ:
	def __init__(self):
		pass
	def draw(self, pen):
		global LENGTH
		pos=pen.position()
		pen.goto(pos[0]+(LENGTH/4), pos[1])
		pos=pen.position()
		pen.pendown()
		pen.circle(LENGTH/8)
		pen.penup()
		pen.goto(pos[0]+(LENGTH/2), pos[1])
class Dot:
	def __init__(self):
		pass
	def draw(self, pen):
		global LENGTH
		pos=pen.position()
		pen.goto(pos[0]+(LENGTH/4), pos[1])
		pos=pen.position()
		pen.pendown()
		pen.begin_fill()
		pen.circle(LENGTH/32)
		pen.end_fill()
		pen.penup()
		pen.goto(pos[0]+(LENGTH/4), pos[1])

angleNames={}
typNames={}
angleNames[45]="b"
angleNames[90]="ch"
angleNames[180]="k"
angleNames[-45]="t"
angleNames[-90]="l"

class Stroke:
	def __init__(self, angle, typ):
		self.angle=angle
		self.typ=typ
	def __str__(self):
		return repr(self)
	def __repr__(self):
		#return "("+str(self.angle)+", "+str(self.typ)+")"
		return angleNames[self.angle]+repr(self.typ)
	def draw(self, pen):
		pen.right(self.angle)
		self.typ.draw(pen)
class Character:
	def __init__(self, strokes, accents):
		self.strokes=strokes
		self.accents=accents
	def __str__(self):
		return repr(self)
	def __repr__(self):
		#ret="{Strokes: ["
		ret=""
		sep=""
		for i in self.strokes:
			ret+=sep+str(i)
			#sep=","
		#ret+="]"
		if(len(self.accents)>0):
			#ret+=", Accents: "
			ret+=" "
			if(len(self.accents)==2):
				if(type(self.accents[0])==type(self.accents[1])):
					if(type(self.accents[0])==Dot):
						ret+="Umlaut"
					else:
						ret+="Double-"
						if(type(self.accents[0])==Acute):
							ret+="Acute"
						elif(type(self.accents[0])==Grave):
							ret+="Grave"
						elif(type(self.accents[0])==Circ):
							ret+="Circle"
				elif(type(self.accents[0])==Acute and type(self.accents[1])==Grave):
					ret+="Circumflex"
				elif(type(self.accents[0])==Grave and type(self.accents[1])==Acute):
					ret+="Inverted Circumflex"
				else:
					for a in self.accents:
						if(type(a)==Acute):
							ret+="Acute "
						elif(type(a)==Grave):
							ret+="Grave "
						elif(type(a)==Dot):
							ret+="Dot "
						elif(type(a)==Circ):
							ret+="Circle "
			else:
				for a in self.accents:
					if(type(a)==Acute):
						ret+="Acute "
					elif(type(a)==Grave):
						ret+="Grave "
					elif(type(a)==Dot):
						ret+="Dot "
					elif(type(a)==Circ):
						ret+="Circle "
		#return ret+"}"
		return ret
					
	def drawAccents(self, pen):
		global LENGTH
		pos=pen.position()
		pen.goto(pos[0]-((LENGTH/8) * len(self.accents)), pos[1]+(LENGTH*2))
		for accent in self.accents:
			accent.draw(pen)
			pos=pen.position()
			pen.goto(pos[0]+(LENGTH/8), pos[1])
	def draw(self, pen):
		lastPos=pen.position()
		pen.setheading(0)
		pen.pendown()
		for stroke in self.strokes:
			stroke.draw(pen)
		pen.penup()
		endPos=pen.position()
		if(len(self.accents)>0):
			pen.goto(*lastPos)
			self.drawAccents(pen)
			pen.goto(*endPos)
		pen.setheading(0)

def randomCharacter():
	strokeCount=random.randint(2, 5)
	strokes=[]
	for stroke in range(0, strokeCount):
		#typ=random.choice([Line, Line, Semicircle])
		typ=random.choice([Line, Semicircle])
		st=Stroke(random.choice([45, 90, 180, -45, -90]), typ(random.choice([True, False, False, False, False])))
		strokes.append(st)
	accents=[]
	for accent in range(0, random.choice([random.randint(0, 2), 0, 0])):
		accents.append(random.choice([Acute, Grave, Circ, Dot])())
	return Character(strokes, accents)

class PILPen:
	def __init__(self, image):
		self.x=0
		self.y=0
		self.up=False
		self.heading=0
		self.image=image
		self.draw=ImageDraw.Draw(self.image)
		self.fill=1
	def penup(self):
		self.up=True
	def pendown(self):
		self.up=False
	def position(self):
		return (self.x, self.y)
	def goto(self, x, y):
		if not self.up:
			self.draw.line([self.x, self.y, x, y], self.fill)
		self.x=x
		self.y=y
	def right(self, angle):
		self.heading+=angle
		self.heading=self.heading%360
	def left(self, angle):
		self.heading-=angle
		self.heading=self.heading%360
	def setheading(self, angle):
		self.heading=angle
	def forward(self, length):
		delta_x=length*math.cos(math.radians(self.heading))
		delta_y=length*math.sin(math.radians(self.heading))
		self.goto(x+delta_x, y+delta_y)
	def circle(self, radius, limit=360):
		# XXX this BB calculation is wrong -- missing corners if heading is not in [0, 90, 180, 270]
		bb=[self.x, self.y, self.x+radius, self.y+radius]
		self.draw.arc(bb, self.heading, self.heading+limit, self.fill)
	def begin_fill(self):
		pass
	def end_fill(self):
		pass
global x, y
x=100
y=100
def write(pen, chars):
	global x, y
	pen.penup()
	for char in chars:
		if(not cursive):
			pen.penup()
		pen.goto(x, y)
		char.draw(pen)
		if(cursive):
			pen.pendown()
		x+=3*LENGTH
def genVocab(characterSet, vocabsize=300, maxwordlength=5):
	words=[]
	i=0
	while(len(words)<vocabsize):
		word=[]
		for j in range(0, random.randint(1, maxwordlength)):
			word.append(random.choice(characterSet))
		if(len(word)>0):
			words.append(word)
		i+=1
	return words
def genCharacterSet(minChars, maxChars):
    characters=[]
    for i in range(0, random.choice(range(minChars, maxChars))):
	characters.append(randomCharacter())
    return characters
def genVocabImages(vocab):
    global x, y
    vocabImages=[]
    for item in vocab:
	img=Image.new('1', (500, 500))
	x=100
	y=100
	write(PILPen(img), item)
	img=img.crop(img.getbbox())
	vocabImages.append(img)
	print(vocabImages[-1].size)
    return vocabImages
vocab=genVocab(genCharacterSet(20, 36))
vocabImages=genVocabImages(vocab)
model=buildMarkovModel(range(0, len(vocab)))

print(len(vocab))
print(len(vocabImages))

def renderPages(lines):
    pages=[]
    page=Image.new('1', (int(8.5*72), 11*72))
    x=10
    y=0
    yoff=LENGTH*3
    for line in lines:
	for word in line:
	    if(word.size[1]>yoff):
		yoff=word.size[1]
	    if(x+word.size[0]>int(8.5*72)):
		x=10
		y+=yoff+5
	    if(y+yoff>int(11*72)):
		pages.append(page)
		page=Image.new('1', (int(8.5*72), 11*72))
		x=10
		y=0
	    page.paste(word, (x, y, x+word.size[0], y+word.size[1]))
	    x+=word.size[0]+(LENGTH*5)
	y+=yoff+5
        x=10
    pages.append(page)
    return pages
def savePages(pages, pfx):
    print(len(pages))
    for i in range(0, len(pages)):
	pages[i].save(pfx+str(i)+".png")


wordCount=0
lines=[]
while wordCount<50000:
    line=iterateModel(model, 500)
    print(line)
    lineImg=[]
    for item in line:
	if(item!=""):
		lineImg.append(vocabImages[item])
		wordCount+=1
    if(len(lineImg)>0):
        print("Line -- "+str(len(lineImg))+" Words")
        lines.append(lineImg)
print(wordCount)
lines_merged=[]
curr=[]
for line in lines:
    if(random.choice(range(0, 100))<98):
        curr.extend(line)
    else:
        lines_merged.append(curr)
        curr=line
lines_merged.append(curr)
savePages(renderPages(lines_merged), "asemic-")

