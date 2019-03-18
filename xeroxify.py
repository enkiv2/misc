import sys, os
from PIL import Image, ImageOps, ImageChops, ImageFont, ImageDraw, ImageFilter

def xeroxify(img):
    img=ImageOps.grayscale(img)

if __name__=="__main__":
    sourceImage=Image.open(sys.argv[1])
    merged=xeroxify(sourceImage)
    merged.save("merged.png")
