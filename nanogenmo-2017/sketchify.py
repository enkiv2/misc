#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter
import tracery, json
from random import Random
random=Random()

def sketchify(sourceImage, colorized=True, sketchOnly=False):
    sketch=ImageOps.invert(ImageOps.autocontrast(sourceImage).filter(ImageFilter.FIND_EDGES))
    if sketchOnly:
        return sketch
    if(colorized):
        sourceImage=ImageOps.posterize(sourceImage, 2)
    else:
        sourceImage=ImageOps.grayscale(sourceImage)
    sourceImage=sourceImage.convert("RGBA")
    sketch=sketch.convert("RGBA")
    merged=Image.blend(sourceImage, sketch, 0.5)
    return merged

if __name__=="__main__":
    sourceImage=Image.open(sys.argv[1])
    merged=sketchify(sourceImage, True)
    merged.save("merged.png")

