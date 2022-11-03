#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter


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
		return bottom

if __name__=="__main__":
		sourceImage=Image.open(sys.argv[1]).convert("RGB")
		merged=rubicate(sourceImage, (255, 0, 0), "X", 200)
		merged.save("merged.png")
