#!/usr/bin/env python

from turtle import *
from random import Random

random=Random()
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149]

master=Turtle()
master.pu()
master.pen(speed=10)
screenSize=(master.window_width(), master.window_height())
master.goto(-screenSize[0], -screenSize[1])
master.ht()
master.color("black")
master.pd()
master.begin_fill()
master.goto(screenSize[0], -screenSize[1])
master.goto(screenSize[0], screenSize[1])
master.goto(-screenSize[0], screenSize[1])
master.goto(-screenSize[0], -screenSize[1])
master.end_fill()
master.goto(-screenSize[0]+(screenSize[0]/2), -screenSize[1]+(screenSize[1]/2))
print(master.pos())
master.pd()
master.st()
for letter in ["W", "r", "e", "a", "t", "h", "s"]:
	master.color(random.choice(["red", "green", "white", "yellow"]))
	master.write(letter, move=True, font=("Arial", "200", "italic"))
	print(letter)
master.ht()

class Wreath(Turtle):
	def __init__(self, colors, angles, steps, baubles, widths, poses):
		Turtle.__init__(self)
		self.getscreen().screensize(480, 480)
		self.pen(speed=10)
		self.wreathColors=colors
		self.angles=angles
		self.steps=steps
		self.baubles=baubles
		self.widths=widths
		self.poses=poses
		self.ht()
		self.pu()
		self.degrees()
		self.setpos(random.choice(poses))
		self.pd()
		print(angles, steps)
	def step(self):
		self.left(random.choice(self.angles))
		self.pensize(random.choice(self.widths))
		self.color(random.choice(self.wreathColors))
		self.forward(random.choice(self.steps))
		bauble=random.choice(self.baubles)
		if(bauble["enabled"]):
			self.color(random.choice(bauble["colors"]))
			if(random.choice([False, False, False, True])):
				self.shape(random.choice(["circle", "circle", "circle", "arrow", "turtle", "square", "triangle", "classic"]))
				self.stamp()
			else:
				self.begin_fill()
				self.circle(random.choice(bauble["sizes"]))
				self.end_fill()
				self.color(random.choice(self.wreathColors))

nullBauble={"enabled":False, "fill":False}
cranberryBauble={"enabled":True, "fill":True, "colors":["red", "IndianRed"], "sizes":[3]}
ballBauble={"enabled":True, "fill":True, "colors":["blue", "orange", "yellow", "red", "LightSkyBlue", "LightGoldenrod", "PaleTurquoise", "PowderBlue", "PaleVioletRed"], "sizes":[11.5]}

defaultWreathColors=["green", "DarkGreen", "DarkOliveGreen", "DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3", "DarkOliveGreen4", "DarkSeaGreen", "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3", "DarkSeaGreen4", "ForestGreen", "green1", "green2", "green3", "green4", "GreenYellow", "LawnGreen", "LightGreen", "LightSeaGreen", "LimeGreen"]

defaultBaubles=[]
defaultBaubles.extend([nullBauble]*40) 		# 50% blank
defaultBaubles.extend([cranberryBauble]*8)	# 20% 'cranberry' balls
defaultBaubles.extend([ballBauble]*2)		# 5% large balls

wreaths=[]
wreaths.append( Wreath(defaultWreathColors, [random.choice(primes[13:])], [random.choice(primes[13:])], defaultBaubles, [1, 2, 3, 4, 5], [(0, 0)]))
for i in range(1, 22):
	wreaths.append(Wreath(defaultWreathColors, [random.choice(primes)], [random.choice(primes[9:23])], defaultBaubles, [1, 2, 3, 4, 5], [
		(
			random.choice(list(range(-480, 480))), random.choice(list(range(-640, 640)))
		)
	]))
for i in range(100):
	for w in wreaths:
		w.step()

