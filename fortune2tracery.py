#!/usr/bin/env python
import json
import sys

fortunepath="/usr/share/games/fortunes/"
items=[]

def parseFortuneFile(handle):
	current=[]
	for line in handle.readlines():
		if(line=="%\n"):
			items.append(("".join(current)).replace("\n", "\\n"))
			current=[]
		else:
			current.append(line)
def fortunes2tracery():
	structure={}
	structure["origin"]=items
	print(json.dumps(structure))

def main():
	if(len(sys.argv)>1):
		for db in sys.argv[1:]:
			try:
				with open(db, 'r') as f:
					parseFortuneFile(f)
			except:
				try:
					with open(fortunepath+db, 'r') as f:
						parseFortuneFile(f)
				except:
					sys.stderr.write("Could not open fortune database \""+db+"\"; skipping.\n")
		fortunes2tracery()
	else:
		parseFortuneFile(sys.stdin)
		fortunes2tracery()
if __name__=="__main__":
	main()

