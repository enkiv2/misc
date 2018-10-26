#!/usr/bin/env python

import json
import sys
import re

max_solutions=100000

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
print("""
format_helper(X) :- format("~s\\n", [X]).
tracery_print(Goal) :- phrase(Goal, X), format_helper(X).
tracery_helper(X) :- phrase(t_origin, X).
tracery_rand :- findnsols("""+str(max_solutions)+""", X, tracery_helper(X), Res), length(Res, N), ItemNum is random(N), nth0(ItemNum, Res, Item), format_helper(Item).
tracery :- tracery_print(t_origin).
tracery_all :- findall(_, tracery, _).""")

