#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter

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

def panelify(sourceImage, targetSize, borderWidth=5, colorized=True, sketchOnly=False):
    sourceImage=sketchify(sourceImage, colorized, sketchOnly)
    sourceImage=ImageOps.fit(sourceImage, targetSize)
    frame=Image.new("RGBA", targetSize, "#ffff")
    frame.paste(sourceImage.resize((targetSize[0]-(2*borderWidth), targetSize[1]-(2*borderWidth))), (borderWidth, borderWidth))
    return frame

if __name__=="__main__":
    sourceImage=Image.open(sys.argv[1])
    #merged=sketchify(sourceImage, True)
    merged=panelify(sourceImage, sourceImage.size)
    merged.save("merged.png")

