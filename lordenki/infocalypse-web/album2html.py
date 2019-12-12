#!/usr/bin/env python
import json
import sys, os
import urllib

album=json.loads("\n".join(open(sys.argv[1], "r").readlines()))
album=album["results"][0]
img=album["image"]
zipfile=album["zip"]
shareurl=album["shareurl"]
name=album["name"]
albumid=album["id"]
filename="Infocalypse - "+name.replace("'", "_").replace("!", "_").replace(":", "_").replace("(", "_").replace(")", "_")+" - "+albumid+" --- Jamendo - MP3.zip"
#print(filename)
filename=urllib.quote(filename)
#print("wget -O "+albumid+".jpg "+img)
print("<a href=\""+shareurl+"\"><img src=\""+albumid+".jpg\" alt=\""+name+"\" /></a><br>"+name+"<br><a href=\""+zipfile+"\">Download (jamendo)</a> <a href=\""+filename+"\">Download (local)</a>")

