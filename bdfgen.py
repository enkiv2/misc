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
		if(len(ax)%2):
			ax.append("0")
		ret.append("".join(ax))
	ret.append("ENDCHAR")
	return "\n".join(ret)
def bdfGenHeader(name, point_size, xres, yres, width, height, xoff, yoff, charcount):
	ret=["STARTFONT 2.1"]
	ret.append("FONT "+name)
	ret.append("SIZE "+(" ".join([str(point_size), str(xres), str(yres)])))
	ret.append("FONTBOUNDINGBOX "+(" ".join([str(width), str(height), str(xoff), str(yoff)])))
	ret.append("STARTPROPERTIES 2")
	ret.append("FONT_ASCENT 16")
	ret.append("FONT_DESCENT 0")
	ret.append("ENDPROPERTIES")
	ret.append("CHARS "+str(charcount))
	return "\n".join(ret)
def bdfGenFooter():
	return "ENDFONT"
def bdfGenFont(name, point_size, xres, yres, swidth, ppi, width, height, char_structs):
	dwidth=(point_size*ppi)/(72*1000)
	ret=[]
	ret.append(bdfGenHeader(name, point_size, xres, yres, width, height, 0, 0, len(char_structs)))
	for charStruct in char_structs:
		charName=charStruct[0]
		glyph_idx=charStruct[1]
		bitmap=charStruct[2]
		ret.append(bdfGenChar(charName, glyph_idx, swidth, dwidth, width, height, 0, 0, bitmap))
	ret.append(bdfGenFooter())
	return "\n".join(ret)

# My barcode font
space=["space", 32, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
bang=["bang", 33, [
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0]]]
quote=["quote", 34, [
		[0, 1, 0, 1, 0],
		[0, 1, 0, 1, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
pound=["pound", 35, [
		[0, 1, 0, 1, 0],
		[0, 1, 0, 1, 0],
		[1, 1, 1, 1, 1],
		[0, 1, 0, 1, 0],
		[1, 1, 1, 1, 1],
		[0, 1, 0, 1, 0]]]
dollar=["dollar", 36, [
		[0, 0, 1, 0, 0],
		[0, 1, 0, 1, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 0, 1, 0],
		[0, 0, 1, 0, 0]]]
percent=["percent", 37, [
		[1, 0, 0, 0, 1],
		[0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[0, 0, 0, 0, 1]]]
amp=["amp", 38, [
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 1, 0]]]
apostrophe=["apostrophe", 39, [
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
lparen=["left parenthesis", 40, [
		[0, 1, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0]]]
rparen=["right parenthesis", 41, [
		[0, 0, 0, 1, 0],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 1, 0]]]
asterisk=["asterisk", 42, [
		[1, 0, 1, 0, 1],
		[0, 1, 1, 1, 0],
		[1, 1, 1, 1, 1],
		[0, 1, 1, 1, 0],
		[1, 0, 1, 0, 1],
		[0, 0, 0, 0, 0]]]
plus=["plus", 43, [
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[1, 1, 1, 1, 1],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
comma=["comma", 44, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0]]]
minus=["minus", 45, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[1, 1, 1, 1, 1],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
period=["period", 46, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0],
		[0, 1, 1, 0, 0]]]
slash=["slash", 47, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0],
		[1, 0, 0, 0, 0]]]
backslash=["backslash", 92, [
		[0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0]]]
colon=["colon", 58, [
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
semicolon=["semicolon", 59, [
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 1, 1, 0, 0]]]
langle=["left angle bracket", 560, [
		[0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
equals=["equals", 61, [
		[0, 0, 0, 0, 0],
		[0, 1, 1, 1, 0],
		[0, 0, 0, 0, 0],
		[0, 1, 1, 1, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
rangle=["right angle bracket", 62, [
		[0, 0, 1, 0, 0],
		[0, 0, 0, 1, 0],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
question=["question mark", 63, [
		[0, 0, 1, 0, 0],
		[0, 1, 0, 1, 0],
		[0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 1, 0, 0]]]
bquote=["backquote", 96, [
		[0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
lsq=["left square bracket", 91, [
		[1, 1, 1, 0, 0],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
tilde=["tilde", 126, [
		[0, 0, 0, 0, 0],
		[0, 1, 0, 1, 0],
		[1, 0, 1, 0, 1],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
rsq=["right square bracket", 93, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1],
		[0, 0, 1, 1, 1]]]
carat=["carat", 94, [
		[0, 0, 1, 0, 0],
		[0, 1, 0, 1, 0],
		[1, 0, 0, 0, 1],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]]]
underscore=["underscore", 95, [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 1, 1, 1, 0]]]
at=["at", 64, [
		[0, 0, 1, 1, 0],
		[0, 1, 0, 0, 1],
		[0, 0, 1, 0, 1],
		[0, 0, 0, 0, 1],
		[1, 0, 0, 1, 0],
		[0, 1, 1, 0, 0]]]
lbrace=["left brace", 123, [
		[0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0],
		[1, 1, 0, 0, 0],
		[0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
pipe=["pipe", 124, [
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
rbrace=["right brace", 125, [
		[0, 0, 1, 0, 0],
		[0, 0, 0, 1, 0],
		[0, 0, 0, 1, 1],
		[0, 0, 0, 1, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 0, 0]]]
chars=[space, bang, quote, pound, dollar, percent, amp, apostrophe, lparen, rparen, asterisk, plus, comma, minus, period, slash, colon, semicolon, langle, equals, rangle, question, bquote, lsq, tilde, rsq, carat, underscore, at, lbrace, pipe, rbrace, backslash]
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo=[0, 0, 0, 0, 0]
hi=[1, 1, 1, 1, 1]
for i in range(0, 26):
	nameC=alpha[i]
	nameL=nameC.lower()
	idxC=65+i
	idxL=97+i
	bmpC=[hi]
	bmpL=[lo]
	bmp=[]
	for j in range(0, 5):
		if(i&(~(1<<j))):
			bmp.append(hi)
		else:
			bmp.append(lo)
	bmpC.extend(bmp)
	bmpL.extend(bmp)
	chars.append([nameC, idxC, bmpC])
	chars.append([nameL, idxL, bmpL])

if(__name__=="__main__"):
	print(bdfGenFont("barcode", 16, 75, 75, 500, 72, 5, 6, chars))
