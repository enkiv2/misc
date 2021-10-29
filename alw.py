#!/usr/bin/env python
import sys

rot=11
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in sys.stdin.readlines():
		for c in line:
				c=c.upper()
				if alpha.find(c)>0:
						sys.stdout.write(alpha[(alpha.find(c)+11)%26])
				else:
						sys.stdout.write(c)
		sys.stdout.flush()


