#!/usr/bin/env python

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import sys

DPI=75
def in2px(inches):
		return (int)(inches*DPI)
def px2in(pixels):
		return (int)(pixels/DPI)

A1=(in2px(8.5), in2px(11))
font=ImageFont.load_default()
em=font.getsize("m")[0]

curs=(0, 0)
off=(0, 0)
rot=0
pgsz=A1
page=PIL.Image.new("L", pgsz, color=255)

rotations=0
rotated=False
for line in sys.stdin.readlines():
		for w in line.split():
				word=w+" "
				size=font.getsize(word)
				mask=Image.new("L", size, color=255)
				mask.paste(font.getmask(word), (0, 0, size[0], size[1]))
				print(word)
				if(not
						((rot==0   and curs[0]+size[0]+off[0]<pgsz[0]) or
						( rot==270 and curs[1]+size[0]+off[1]<pgsz[1]) or
						( rot==180 and curs[0]-size[0]>off[0]        ) or
						( rot==90  and curs[1]-size[0]>off[1]        ))):
						if rot==90: # rotate from left to top
								off=(off[0], off[1]+curs[1]-em)
								curs=(curs[0], 0)
						elif rot==270: # rotate from right to bottom
								pgsz=(pgsz[0], (off[1]+curs[1])-em)
								curs=(curs[0], curs[1]-em*2)
						elif rot==180: # rotate from bottom to left
								off=(off[0]+curs[0]-em, off[1])
								curs=(0, curs[1])
						else: # rot=0 from top to right
								pgsz=((off[0]+curs[0])-em, pgsz[1])
						rot=(rot+270)%360
						if(rotated):
								page.save("page.png")
								sys.exit()
						rotated=True
						rotations+=1
						print("rot:", rot, "curs:", curs, "off:", off, "pgsz:", pgsz, "size:", size)
						draw=ImageDraw.Draw(page)
						draw.line((off[0], off[1], off[0], pgsz[1]))
						draw.line((off[0], pgsz[1], pgsz[0], pgsz[1]))
						draw.line((pgsz[0], pgsz[1], pgsz[0], off[1]))
						draw.line((pgsz[0], off[1], off[0], off[1]))
						print("rotating ", rot)
						page.save("page.png")
				else:
						rotated=False
				if rot==180:
						curs=(curs[0]-size[0], curs[1])
				elif rot==90:
						curs=(curs[0], curs[1]-size[0])
				page.paste(mask.rotate(rot, expand=1), (curs[0]+off[0], curs[1]+off[1]))
				if rot==0:
						curs=(curs[0]+size[0], curs[1])
				elif rot==270:
						curs=(curs[0], curs[1]+size[0])


page.save("page.png")
