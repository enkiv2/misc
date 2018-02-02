#!/usr/bin/env python

import sys, os

if len(sys.argv)!=3:
    sys.stderr.write("Usage: "+sys.argv[0]+" ground figure\nCreates a piece of blackout poetry by blacking out every non-whitespace character in the 'ground' file that doesn't match the next character in 'figure', writing to stdout\n")
    sys.exit(0)

ground=open(sys.argv[1])
figure=open(sys.argv[2])

fill="#"

whitespacelist=" \t\n\r"
whitelist=whitespacelist+".,!"

whitelist=whitespacelist


fc=figure.read(1)
while fc!="":
    gc=ground.read(1)
    if(gc==""):
        sys.stderr.write("Ground underrun\n")
        sys.exit(1)
    while(gc!=fc):
        if whitelist.find(gc)>=0:
            sys.stdout.write(gc)
        else:
            sys.stdout.write(fill)
        gc=ground.read(1)
        if(gc==""):
            sys.stderr.write("Ground underrun\n")
            sys.exit(1)
    sys.stdout.write(fc)
    fc=figure.read(1)

gc=ground.read(1)
while gc!="":
    if whitelist.find(gc)>=0:
        sys.stdout.write(gc)
    else:
        sys.stdout.write(fill)
    gc=ground.read(1)

sys.stdout.flush()

