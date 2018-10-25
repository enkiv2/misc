#!/usr/bin/env python

import json
import sys
import re

stdin=sys.stdin
if(len(sys.argv)>1):
    stdin=open(sys.argv[1], 'r')
grammar=json.load(stdin)

print("/* Usage: swipl -s output.pl -g tracery_all */")
print(":- set_prolog_flag(double_quotes, chars).")

for pred in grammar.keys():
    pred2="t_"+pred
    for rule in grammar[pred]:
        print(pred2+" --> \""+re.sub("#([A-Za-z0-9_]*)#", "\", t_\\1, \"", rule)+"\".")
print("tracery :- phrase(t_origin, X), atom_chars(Y, X), writeln(Y).")
print("tracery_all :- findall(_, tracery, _).")

