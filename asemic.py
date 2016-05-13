#!/usr/bin/env python

import turtle
from random import Random
random=Random()

global LENGTH
LENGTH=10

#cursive=True
cursive=False

turtle.speed(0)

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

turtle.penup()
turtle.goto(-500, 550)
turtle.pendown()
turtle.write("Alphabet")
turtle.penup()

characterSet=[]
for i in range(0, random.randint(23, 37)):
	characterSet.append(randomCharacter())

print("# of characters: "+str(len(characterSet)))
print("Characters: ", characterSet)

global x, y
x=-500
y=500

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
		x+=5*LENGTH
		if(x>500):
			x=-500
			y-=7*LENGTH
			pen.penup()
def box(pen, x1, y1, x2, y2):
	pos=pen.position()
	pen.penup()
	pen.goto(x1, y1)
	pen.pendown()
	pen.goto(x2, y1)
	pen.goto(x2, y2)
	pen.goto(x1, y2)
	pen.goto(x1, y1)
	pen.penup()
	pen.goto(*pos)

write(turtle, characterSet)

box(turtle, -570, 570, 570, y-70)

y-=(70*2)
x=-500
oldy=y ; oldx=x; oldlength=LENGTH
y=500 ; x=-800 ; LENGTH=LENGTH/2

turtle.penup()
turtle.goto(-800, 510)
turtle.pendown()
turtle.write("Vocabulary")
turtle.penup()

text=[]
words=[]
vocabsize=300
maxwordlength=5
for i in range(0, vocabsize):
	word=[]
	wlen=(((vocabsize-i)+1) % maxwordlength) 
	if(wlen==0):
		wlen=3
	for j in range(0, random.randint(0, wlen)):
		word.append(random.choice(characterSet))
	if(not word in words):
		if(i<50):
			write(turtle, word)
			x=-800; y-=LENGTH*5
		for j in range(0, random.randint(1, (vocabsize-i)%20 + 1)):
			words.append(word)
box(turtle, -810, 550, -800 + (LENGTH*5*(maxwordlength+1)), y+(LENGTH*5))

y=oldy; x=oldx ; LENGTH=oldlength

for i in range(0, 1000):
	write(turtle, random.choice(words))
	x+=LENGTH*5
	turtle.goto(x, y)


