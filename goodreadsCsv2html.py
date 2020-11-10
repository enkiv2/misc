#!/usr/bin/env python

import csv
import sys

f=open(sys.argv[1], 'r')
lines=f.readlines()
fieldnames=lines[0].split(",")

reader=csv.DictReader(lines[1:], fieldnames=fieldnames)

print("<html><head><title>Books</title><link rel=\"stylesheet\" type=\"text/css\" href=\"vt240.css\"></head><body><table>")
print("<hr><th>"+("</th><th>".join(fieldnames))+"</th></hr>")

for book in reader:
		print("<tr>")
		for field in fieldnames:
				print("<td>"+book[field]+"</td>")
		print("</tr>")

print("</table></body></html>")

