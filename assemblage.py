#!/usr/bin/env python

"""
Assemblage -- a generative grammar system in the vein of Tracery

The first interesting feature it will support is inline expansion. This way, we can quickly inline small rules.

Possible future directions include:
* Memoization (with a sigil, probably carat like in MUMPS): we make an expansion permanent.
		=> Plus indexing (by something that can be a reference), so we can bind particular memoized expansions to keys
* Conditions (and conditional expression resolution)
		=> to filter out options, or to control whether or not to perform filters or modifications
		=> passing conditions to rules means condition expansion is part of the rule name for memoization purposes
		=> so we have a mycroft-like rule resolution environment

Format is JSON, much like tracery:
{
		"rule1":["opt1", ...],
		...
}

Unlike tracery, references to rules begin with a dollar sign. Rule names may contain alphanumerics and underscore.

The following tracery grammar:
		{
				"origin": ["#greeting#, how are you"],
				"greeting": ["hi", "hello"]
		}

can be expressed as:
		{
				"origin": ["$greeting, how are you"],
				"greeting": ["hi", "hello"]
		}

or, using inline expansion:
		{
				"origin":["{hi|hello}, how are you"]
		}


"""

import re
from random import Random
random=Random()

def canonicalize(grammar):
		"""
				Convert expressions inline in the grammar into part of the grammar

				First is inline expansion.
				Basically, this expands:
						{"foo":["bar {expr1|expr2} baz"]}
				into:
						{
								"foo":["bar $___SYNTH0 baz"],
								"___SYNTH0":["expr1", "expr2"]
						}

		"""
		rules=list(grammar.keys()
		synth_count=len([rule for rule in rules) where rule.find("___SYNTH") == 0])
		def add_rule(name, body):
				grammar[name]=grammar.get(name, [])+body)
		def add_synth(body):
				add_rule("___SYNTH"+str(synth_count), body)
				synth_count += 1
		def process_snippet(s):
				if s.find("{")>=0:
						if s.find("}")<s.find("{"):
								raise SyntaxError("Cannot canonicalize: Invalid assemblage template: } before {")
						span=(s.find("{"), s.find("}"))
						snippet=s[span[0]+1:span[1]-1]
						# TODO: use pyparsing here https://stackoverflow.com/questions/5454322/python-how-to-match-nested-parentheses-with-regex
						# Iterate recursively over the tree of pipe separated token groups, and (from the leaves up) replace them to references
						# to new synthetic rules

						s=s[0:span[0]-1]+process_snippet(snippet)+s[span[1]+1:]
				
		for rule in rules:
				body=rules[rule]
				rules[rule]=[process_snippet(opt) for opt in rules[rule]]

				

template_pat=re.compile("\$([A-Za-z0-9_]+)")
def flatten(grammar, prompt):
		return re.sub(template_pat, lambda m: flatten(grammar, random.choice(grammar[m.group(1)])), prompt)
		

