#!/usr/bin/env python
import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter

# Make an image more closely resemble a pen drawing, with optional shading and coloring
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

# Run sketchify and then fit to a particular size, followed by the addition of a gutter
def panelify(sourceImage, targetSize, borderWidth=5, colorized=True, sketchOnly=False):
    sourceImage=sketchify(sourceImage, colorized, sketchOnly)
    sourceImage=ImageOps.fit(sourceImage, targetSize)
    frame=Image.new("RGBA", targetSize, "#ffff")
    frame.paste(sourceImage.resize((targetSize[0]-(2*borderWidth), targetSize[1]-(2*borderWidth))), (borderWidth, borderWidth))
    return frame

if __name__=="__main__":
    sourceImage=Image.open(sys.argv[1]).convert("RGB")
    #merged=sketchify(sourceImage, True)
    merged=panelify(sourceImage, sourceImage.size)
    merged.save("merged.png")

