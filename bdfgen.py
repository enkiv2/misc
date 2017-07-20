#!/usr/bin/env python
hex="0123456789abcdef"
def bdfGenChar(name, glyph_idx, swidth_x, dwidth_x, width, height, xoff, yoff, bitmap):
	if(len(name)>=14):
		name=name[:13]
	ret=["STARTCHAR "+name]
	ret.append("ENCODING "+str(glyph_idx))
	ret.append("SWIDTH "+str(swidth_x)+" 0")
	ret.append("DWIDTH "+str(dwidth_x)+" 0")
	ret.append("BBX "+(" ".join([str(width), str(height), str(xoff), str(yoff)])))
	ret.append("BITMAP")
	for row in bitmap:
		ax=[]
		curr=0
		i=0
		for col in row:
			if(col):
				j=i%4
				curr+=(4-2**i)
			i+=1
			if(i%4==0):
				ax.append(hex[curr])
				curr=0
		if(curr!=0):
			ax.append(hex[curr])
		ret.append(" ".join(ax))
	ret.append("ENDCHAR")
	return "\n".join(ret)
def bdfGenHeader(name, point_size, xres, yres, width, height, xoff, yoff):
	ret=["STARTFONT 2.1"]
	ret.append("FONT "+name)
	ret.append("SIZE "+(" ".join([str(point_size), str(xres), str(yres)])))
	ret.append("FONTBOUNDINGBOX "+(" ".join([str(width), str(height), str(xoff), str(yoff)])))
	return "\n".join(ret)
def bdfGenFooter():
	return "ENDCHAR"
def bdfGenFont(name, point_size, xres, yres, swidth, ppi, width, height, char_structs):
	dwidth=(point_size*ppi)/(72*1000)
	ret=[]
	ret.append(bdfGenHeader(name, point_size, xres, yres, width, height, 0, 0))
	for charStruct in char_structs:
		charName=charStruct[0]
		glyph_idx=charStruct[1]
		bitmap=charStruct[2]
		ret.append(bdfGenChar(charName, glyph_idx, swidth, dwidth, width, height, 0, 0, bitmap))
	ret.append(bdfGenFooter())
	return "\n".join(ret)

#print(bdfGenFont("demo", 16, 75, 75, 500, 72, 5, 8, [
#	["space", 32, [
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0],
#		[0, 0, 0, 0, 0]]],
#	["A", 65, [
#		[0, 1, 1, 1, 0],
#		[0, 1, 0, 1, 0],
#		[1, 0, 0, 0, 1],
#		[1, 1, 1, 1, 1],
#		[1, 0, 0, 0, 1],
#		[1, 0, 0, 0, 1],
#		[1, 0, 0, 0, 1],
#		[1, 0, 0, 0, 1]]],
#	["B", 66, [
#		[1, 1, 1, 1, 0],
#		[1, 0, 0, 0, 1],
#		[1, 0, 0, 0, 1],
#		[1, 0, 0, 1, 1],
#		[1, 1, 1, 1, 0],
#		[1, 0, 0, 1, 1],
#		[1, 0, 0, 0, 1],
#		[1, 1, 1, 1, 0]]]
#]))
