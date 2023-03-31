#!/usr/bin/env python

"""
**Eliza** is a pattern-matching automated psychiatrist.	Given a set of rules
in the form of input/output patterns, Eliza will attempt to recognize user input
phrases and generate relevant psychobabble responses.

Each rule is specified by an input pattern and a list of output patterns.	A
pattern is a sentence consisting of space-separated words and variables.	Input
pattern variables come in two forms: single variables and segment variables;
single variables (which take the form `?x`) match a single word, while segment
variables (which take the form `?*x`) can match a phrase.	Output pattern
variables are only single variables.	The variable names contained in an input
pattern should be the same as those in the corresponding output pattern, and
each segment variable `?*x` in an input pattern corresponds to the single
variable `?x` in the output pattern.

The conversation proceeds by reading a sentence from the user, searching through
the rules to find an input pattern that matches, replacing variables in the
output pattern, and printing the results to the user.

For examples of using this scheme, see the following programs:

- [Eliza](examples/eliza/eliza.html)
- [Automated technical support system](examples/eliza/support.html)

This implementation is inspired by Chapter 5 of "Paradigms of Artificial
Intelligence Programming" by Peter Norvig.
"""

import random
import string
import sys
import json
import re

try:
		import tracery
		has_tracery = True
		grammar_rules = {}
		grammar=tracery.Grammar({})
except:
		has_tracery = False

try:
		import nltk
		try:
				from nltk.corpus import wordnet
		except:
				nltk.download("wordnet")
		try:
				from nltk.corpus import cmudict	
		except:
				nltk.download("cmudict")
		from nltk.corpus import wordnet
		from nltk.corpus import cmudict	
		has_nltk = True
except:
		has_nltk = False

## Polyfills for python 3 compatibility
try:
		x = raw_input
except NameError as e:
		raw_input = input
try:
		letters = string.letters
except AttributeError as e:
		letters = string.ascii_letters


DEBUGLEVEL=0
log=open("eliza.log", "w+")

def dprint(value, debug=0, nl=True):
		if debug<=DEBUGLEVEL:
				sys.stderr.write(value)
				if nl:
						sys.stderr.write("\t\tdebug="+str(debug)+" <= DEBUGLEVEL="+str(DEBUGLEVEL))
						sys.stderr.write("\n")
				sys.stderr.flush()

def wlog(value):
		log.write(value)
		log.write("\n")
		log.flush()


## Talking to the computer

def interact(prompt, rules, default_responses):
		"""Have a conversation with a user."""
		# Read a line, process it, and print the results until no input remains.
		dprint("Ready.", 1)
		while True:
				try:
						# Remove the punctuation from the input and convert to upper-case
						# to simplify matching.
						s = remove_punct(raw_input(prompt).upper())
						if not s:
								continue
						wlog(s)
				except Exception as e:
						print(e, flush=True)
						break
				resp=respond(rules, s, default_responses)
				wlog(resp)
				print(resp)

def dprint_matching_rules(matching_rules, debug=1):
		dprint("Matching rules:\n", debug, False)
		for item in matching_rules:
				(transforms, replacements, pat) = item
				dprint("\t\""+str(pat)+"\"\n", debug, False)
				dprint("\t\tTransforms:\n", debug, False)
				for t in transforms:
						dprint("\t\t\t\""+t+"\"\n", debug, False)
				dprint("\n\t\tReplacements:\n", debug, False)
				for r in replacements:
						dprint("\t\t\t\""+r+"\"\n", debug, False)
		dprint("Total matching rules: "+str(len(matching_rules)), debug)
				

def respond(rules, s, default_responses):
		"""Respond to an input sentence according to the given rules."""
		s = s.split() # match_pattern expects a list of tokens
		
		# Look through rules and find input patterns that matches the input.
		num_transforms, num_replacements = 0, 0
		matching_rules = []
		for pattern, transforms in rules:
				pattern = pattern.split()
				replacements = match_pattern(pattern, s)
				if replacements:
						matching_rules.append((transforms, replacements, pattern))
						num_transforms+=len(transforms)
						num_replacements+=len(replacements)

		# When rules are found, choose one and one of its responses at random.
		# If no rule applies, we use the default rule.
		dprint("There are "+str(len(matching_rules))+" matching rules with a total of "+str(num_transforms)+" transforms and "+str(num_replacements)+" replacements")
		matching_rules.append((default_responses, {}, "DEFAULT"))
		dprint_matching_rules(matching_rules, 0)
		responses, replacements, pat = random.choice(matching_rules)
		dprint("selected pattern \""+str(pat)+"\"")
		dprint("responses = "+str(responses))
		response = random.choice(responses)
		if has_tracery:
				response = grammar.flatten(response)

		# Replace the variables in the output pattern with the values matched from
		# the input string.
		for variable, replacement in replacements.items():
				replacement = ' '.join(switch_viewpoint(replacement))
				if replacement:
						response = response.replace('?' + variable, replacement)
		wlog(response.capitalize())
		return response.capitalize()
	

## Pattern matching

def match_pattern(pattern, s, bindings=None):
		"""
		Determine if the input string matches the given pattern.

		Expects pattern and input to be lists of tokens, where each token is a word
		or a variable.

		Returns a dictionary containing the bindings of variables in the input
		pattern to values in the input string, or False when the input doesn't match
		the pattern.
		"""

		# Check to see if matching failed before we got here.
		if bindings is False:
				return False
	
		# When the pattern and the input are identical, we have a match, and
		# no more bindings need to be found.
		if pattern == s:
				return bindings

		bindings = bindings or {}

		# Match input and pattern according to their types.
		if is_segment(pattern):
				token = pattern[0] # segment variable is the first token
				var = token[2:] # segment variable is of the form ?*x
				return match_segment(var, pattern[1:], s, bindings)
		elif is_variable(pattern):
				var = pattern[1:] # single variables are of the form ?foo
				return match_variable(var, [s], bindings)
		elif contains_tokens(pattern) and contains_tokens(s):
				# Recurse:
				# try to match the first tokens of both pattern and input.	The bindings
				# that result are used to match the remainder of both lists.
				return match_pattern(pattern[1:],
						s[1:],
						match_pattern(pattern[0], s[0], bindings))
		else:
				return False


def match_segment(var, pattern, s, bindings, start=0):
		"""
		Match the segment variable against the input.

		pattern and input should be lists of tokens.

		Looks for a substring of input that begins at start and is immediately
		followed by the first word in pattern.	If such a substring exists,
		matching continues recursively and the resulting bindings are returned;
		otherwise returns False.
		"""

		# If there are no words in pattern following var, we can just match var
		# to the remainder of the input.
		if not pattern:
				return match_variable(var, s, bindings)

		# Get the segment boundary word and look for the first occurrence in
		# the input starting from index start.
		word = pattern[0]
		try:
				pos = start + s[start:].index(word)
		except ValueError:
				# When the boundary word doesn't appear in the input, no match.
				return False

		# Match the located substring to the segment variable and recursively
		# pattern match using the resulting bindings.
		var_match = match_variable(var, s[:pos], dict(bindings))
		match = match_pattern(pattern, s[pos:], var_match)

		# If pattern matching fails with this substring, try a longer one.
		if not match:
				return match_segment(var, pattern, s, bindings, start + 1)
	
		return match


def match_variable(var, replacement, bindings):
		"""Bind the input to the variable and update the bindings."""
		binding = bindings.get(var)
		if not binding:
				# The variable isn't yet bound.
				bindings.update({var: replacement})
				return bindings
		if replacement == bindings[var]:
				# The variable is already bound to that input.
				return bindings

		# The variable is already bound, but not to that input--fail.
		return False


## Pattern matching utilities

def contains_tokens(pattern):
		"""Test if pattern is a list of subpatterns."""
		return type(pattern) is list and len(pattern) > 0


def is_variable(pattern):
		"""Test if pattern is a single variable."""
		return (type(pattern) is str
				and pattern[0] == '?'
				and len(pattern) > 1
				and pattern[1] != '*'
				and pattern[1] in letters
				and ' ' not in pattern)


def is_segment(pattern):
		"""Test if pattern begins with a segment variable."""
		return (type(pattern) is list
				and pattern
				and len(pattern[0]) > 2
				and pattern[0][0] == '?'
				and pattern[0][1] == '*'
				and pattern[0][2] in letters
				and ' ' not in pattern[0])


## Translating user input

def replace(word, replacements):
		"""Replace word with rep if (word, rep) occurs in replacements."""
		for old, new in replacements:
				if word == old:
						return new
		return word


def switch_viewpoint(words):
		"""Swap some common pronouns for interacting with a robot."""
		replacements = [('I', 'YOU'),
				('YOU', 'I'),
				('ME', 'YOU'),
				('MY', 'YOUR'),
				('AM', 'ARE'),
				('ARE', 'AM')]
		return [replace(word, replacements) for word in words]


def remove_punct(string):
		"""Remove common punctuation marks."""
		if string.endswith('?'):
				string = string[:-1]
		return (string.replace(',', '')
				.replace('.', '')
				.replace(';', '')
				.replace('!', ''))
rules = {
		"?*x hello ?*y": [
				"How do you do. Please state your problem.",
				"Howdy",
				"Hi there!",
				"G'day",
				"Hi",
				"Let's get started.",
		],
		"?*x computer ?*y": [
				"Do computers worry you?",
				"What do you think about machines?",
				"Why do you mention computers?",
				"What do you think machines have to do with your problem?",
		],
		"?*x name ?*y": [
				"I am not interested in names",
				"What other name would be appropriate?",
		],
		"?*x sorry ?*y": [
				"Please don't apologize",
				"Apologies are not necessary",
				"What feelings do you have when you apologize?",
				"Why do you feel that you need to apologize ?y?",
				"What makes you feel that you need to apologize ?y?",
				"Why do you feel that you need to apologize ?x?",
				"What makes you feel that you need to apologize ?x?",
		],
		"?*x I remember ?*y": [
				"Do you often think of ?y?",
				"Does thinking of ?y bring anything else to mind?",
				"What else do you remember?",
				"Why do you recall ?y right now?",
				"What in the present situation reminds you of ?y?",
				"What is the connection between me and ?y?",
				"What about ?y?",
				"You mentioned ?y",
				"How is ?y relevant?",
				"How is ?y important?",
				"What about ?y is interesting right now?",
				"I remember ?y",
				"I don't remember ?y. Can you explain?",
				"I don't remember ?y. Can you remind me?",
				"I'm not familiar with ?y. Can you explain?",
				"Do you often remember ?y?",
				"How often do you remember ?y?",
				"How often do you think of ?y?",
				"How do you remember ?y?",
				"How does ?y make you feel?",
				"What does ?y mean?",
		],
		"?*x do you remember ?*y": [
				"Did you think I would forget ?y?",
				"Why do you think I should recall ?y now?",
				"What about ?y?",
				"You mentioned ?y",
				"How is ?y relevant?",
				"How is ?y important?",
				"What about ?y is interesting right now?",
				"I remember ?y",
				"I don't remember ?y. Can you explain?",
				"I don't remember ?y. Can you remind me?",
				"I'm not familiar with ?y. Can you explain?",
				"I remember ?y. Do you remember?",
				"I don't remember ?y. Do you?",
				"How would I better remember ?y?",
				"How does ?y make you feel?",
				"What does ?y mean?",
		],
		"?*x I want ?*y": [
				"What would it mean if you got ?y?",
				"What would you do if you got ?y?",
				"Why do you want ?y?",
				"Suppose you got ?y soon.",
		],
		"?*x if ?*y": [
				"Do you really think it's likely that ?y?",
				"Do you wish that ?y?",
				"What do you think about ?y?",
				"Really--if ?y?",
				"Really? ?x?",
				"What else happens if ?y?",
		],
		"?*x I dreamt ?*y": [
				"How do you feel about ?y in reality?",
				"What else happened ?x?",
				"What else happened in this dream?",
				"How does this make you feel?",
				"What do you think this means?",
				"What do you think it means ?y?",
		],
		"?*x dream ?*y": [
				"What does this dream suggest to you?",
				"Do you dream often?",
				"What persons appear in your dreams?",
				"Don't you believe that dream has to do with your problem?",
				"What do you think this means?",
				"Do any elements of this dream appear in other dreams?",
				"Do any elements of this dream appear in your daily life?",
				"What else happened in this dream?",
				"How does this make you feel?",
		],
		"?*x my mother ?*y": [
				"Your mother?",
				"Does she influence you strongly?",
				"What else comes to mind when you think of your mother?",
				"Who else in your family ?y?",
				"Tell me more about your family",
				"What about your father?",
				"How does it feel when your mother ?y?",
				"What if your father ?y?",
				"How does this differ from your father?",
		],
		"?*x my father ?*y": [
				"Your father?",
				"Does he influence you strongly?",
				"What else comes to mind when you think of your father?",
				"Who else in your family ?y?",
				"Tell me more about your family",
				"What about your mother?",
				"How does it feel when your father ?y?",
				"What if your mother ?y?",
				"How does this differ from your mother?",
		],
		"?*x I am glad that ?*y": [
				"How have I helped you to be ?y?",
				"Have I helped you to be ?y?",
				"What makes you happy just now?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
				"Why are you glad ?y?",
		],
		"?*x I am sad ?*y": [
				"I am sorry to hear you are depressed",
				"I'm sure it's not pleasant to be sad",
				"Why are you sad ?y?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
		],
		"?*x I am glad ?*y": [
				"How have I helped you to be ?y?",
				"Have I helped you to be ?y?",
				"What makes you happy just now?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
				"Why are you glad ?y?",
		],
		"?*x I am sad ?*y": [
				"I am sorry to hear you are depressed",
				"I'm sure it's not pleasant to be sad",
				"Why are you sad ?y?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
		],
		"?*x I am happy that ?*y": [
				"How have I helped you to be ?y?",
				"Have I helped you to be ?y?",
				"What makes you happy just now?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
				"Why are you happy ?y?",
		],
		"?*x I am depressed ?*y": [
				"I am sorry to hear you are depressed",
				"I'm sure it's not pleasant to be depressed",
				"Why are you depressed ?y?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
		],
		"?*x I am happy ?*y": [
				"How have I helped you to be ?y?",
				"Have I helped you to be ?y?",
				"What makes you happy just now?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
				"Why are you happy ?y?",
		],
		"?*x I am depressed ?*y": [
				"I am sorry to hear you are depressed",
				"I'm sure it's not pleasant to be depressed",
				"Why are you depressed ?y?",
				"Can you explain why you are suddenly ?y?",
				"Can you explain why you are ?y?",
		],
		"?*x are like ?*y": [
				"What resemblence do you see between ?x and ?y?",
				"In what way is it that ?x are like ?y?",
				"What resemblence do you see?",
				"Could there really be some connection?",
				"How?",
				"What other connections do you see?",
				"In what way?",
				"What similarities are there?",
				"What else is like ?x?",
				"What else is like ?y?",
		],
		"?*x is like ?*y": [
				"In what way is it that ?x is like ?y?",
				"What resemblence do you see?",
				"Could there really be some connection?",
				"How?",
				"What other connections do you see?",
				"In what way?",
				"What similarities are there?",
				"What else is like ?x?",
				"What else is like ?y?",
		],
		"?*x alike ?*y": [
				"In what way?",
				"What similarities are there?",
		],
		"?*x same ?*y": [
				"What other connections do you see?",
				"In what way?",
				"What similarities are there?",
				"In what way is ?x same ?y?",
		],
		"?*x no ?*y": [
				"Why not?",
				"You are being a bit negative.",
				"Are you saying 'No' just to be negative?",
				"What would happen if that wasn't true?",
		],
		"?*x I was ?*y": [
				"Were you really?",
				"Perhaps I already knew you were ?y.",
				"Why do you tell me you were ?y now?"
				"In what way were you ?y?",
				"Why do you believe you were ?y?",
				"Would you want to be ?y?",
				"Do you want to be ?y?",
				"Do you like to be ?y?",
				"What would it mean if you weren't ?y?",
				"What could you be if you weren't ?y?",
				"Are you sure ?x?",
				"What is it like to be ?y?",
				"Are you still ?y?",
		],
		"?*x was I ?*y": [
				"What if you were ?y?",
				"Do you think you were ?y?",
				"What would it mean if you were ?y?",
				"You wish I would tell you you were ?y?",
				"What would it mean if you weren't ?y?",
				"What could you be if you weren't ?y?",
				"Are you sure ?x?",
				"What is it like to be ?y?",
		],
		"?*x I am ?*y": [
				"In what way are you ?y?",
				"Why do you believe you are ?y?",
				"Would you want to be ?y?",
				"Do you want to be ?y?",
				"Do you like to be ?y?",
				"What would it mean if you weren't ?y?",
				"What could you be if you weren't ?y?",
				"Are you sure ?x?",
				"What is it like to be ?y?",
		],
		"?*x am I ?*y": [
				"Do you believe you are ?y?",
				"Would you want to be ?y?",
				"You wish I would tell you you are ?y?",
				"What would it mean if you were ?y?",
				"What would it mean if you weren't ?y?",
				"What could you be if you weren't ?y?",
				"Are you sure ?x?",
				"What is it like to be ?y?",
		],
		"?*x am ?*y": [
				"Why do you say 'AM?'",
				"I don't understand that"
		],
		"?*x are you ?*y": [
				"Why are you interested in whether I am ?y or not?",
				"Would you prefer if I weren't ?y?",
				"Perhaps I am ?y in your fantasies",
				"?x am I ?y?"
				"Are you sure ?x?",
				"What else might I be?",
		],
		"?*x you are ?*y": [
				"What makes you think I am ?y?",
				"?x am I ?y?"
				"Are you sure ?x?",
				"Are you sure ?y?",
				"What makes you so sure?",
				"Can you explain your reasoning?",
				"What else might I be?",
		],
		"?*x because ?*y": [
				"Is that the real reason?",
				"What other reasons might there be?",
				"Does that reason seem to explain anything else?",
				"Why else ?x?",
				"What else happens when ?y?",
				"Are you sure ?x because ?y?",
				"Are you sure ?y?",
				"Are you sure ?x?",
				"What makes you so sure?",
				"Can you explain your reasoning?"
		],
		"?*x were you ?*y": [
				"Perhaps I was ?y?",
				"What do you think?",
				"What if I had been ?y?",
				"Do you think I was ?y?",
				"Why should I be ?y?",
				"Why do you ask?",
		],
		"?*x I can't ?*y": [
				"Maybe you could ?y now",
				"What if you could ?y?",
				"Why not?",
				"So ?x. Why can't ?y?",
				"Why do you feel that you can't ?y?",
				"If you could ?y, would you?",
				"If you could ?y, what would you do?",
				"If you could ?y, what else would you do?",
		],
		"?*x I feel ?*y": [
				"Do you often feel ?y?",
				"When else do you feel ?y?",
				"What else do you feel ?x, other than ?y?",
				"Why do you think you feel ?y?",
				"So ?x. Why do you feel ?y?",
		],
		"?*x I felt ?*y": [
				"What other feelings do you have?",
				"When else did you feel ?y?",
				"What else did you feel ?x, other than ?y?",
				"Why do you think you felt ?y?",
				"So ?x. Why did you feel ?y?",
		],
		"?*x I ?*y you ?*z": [
				"Perhaps in your fantasy we ?y each other",
				"?x you ?y me ?z?",
				"?x you ?y me ?z? Why?",
				"No. ?x you don't ?y me ?z.",
		],
		"?*x why don't you ?*y": [
				"Should you ?y yourself?",
				"Do you believe I don't ?y?",
				"Perhaps I will ?y in good time",
				"Why should I ?y?",
				"What makes it a good idea to ?y?",
				"?x? Is that really true?",
		],
		"?*x yes ?*y": [
				"You seem quite positive",
				"You are sure?",
				"I understand",
				"What if that wasn't true?",
				"How can you be so sure?",
				"Can you think of any counterexamples?",
		],
		"?*x someone ?*y": [
				"Can you be more specific?",
				"Can you think of anyone in particular?",
				"Who, for example?",
				"?x who ?y, specifically?",
				"?x who, specifically, ?y?",
		],
		"?*x everyone ?*y": [
				"Surely not everyone",
				"Can you think of anyone in particular?",
				"Who, for example?",
				"You are thinking of a special person",
				"?x who ?y, specifically?",
				"?x who, specifically, ?y?",
		],
		"?*x always ?*y": [
				"Can you think of a specific example?",
				"When?",
				"What incident are you thinking of?",
				"Really--always?",
				"Could you think of a counter-example?",
				"What would happen if ?x didn't ?y?",
				"Why should ?x always ?y?",
				"Why would ?x always ?y?",
		],
		"?*x what ?*y": [
				"Why do you ask?",
				"Does that question interest you?",
				"What is it you really want to know?",
				"What do you think?",
				"What comes to your mind when you ask that?",
				"?x what do you think ?y?"
		],
		"?*x perhaps ?*y": [
				"You do not seem quite certain",
				"Why did you think ?x could ?y?",
				"How would you know for sure?",
				"How could you know for sure?",
				"What made you suspect ?x ?y?",
				"What made you suspect ?y?",
		],
		"?*x are ?*y": [
				"Did you think they might not be ?y?",
				"Possibly they are ?y",
				"Are ?x really ?y?",
				"What else are ?x?",
				"And what are ?y?",
		],
}

default_responses = [
		"Very interesting",
		"I am not sure I understand you fully",
		"What does that suggest to you?",
		"Please continue",
		"Go on",
		"Do you feel strongly about discussing such things?",
		"How does that make you feel?",
		"Why do you think that is?",
		"Could you rephrase?",
		"Why?",
		"K.",
		"I don't understand.",
		"Can you explain further?",
]

def elizaResponse(line):
		rules_list = []
		for pattern, transforms in rules.items():
				# Remove the punctuation from the pattern to simplify matching.
				pattern = remove_punct(str(pattern.upper())) # kill unicode
				transforms = [str(t).upper() for t in transforms]
				rules_list.append((pattern, transforms))
		return respond(rules_list, remove_punct(line).upper(), map(str.capitalize, default_responses))

def dict_merge(p, q):
		dirty_count=0
		for k,v in q.items():
				temp=list(set(v+p.get(k, [])))
				if p.get(k, []) != temp:
						dirty_count+=1
				p[k]=temp
		return p, dirty_count

def merge_rules(structure):
		global rules
		rules, dirty_count=dict_merge(rules, structure)
		return dirty_count

def initialize_tracery():
		global grammar
		if has_tracery:
				dprint("Initializing tracery...", 1)
				grammar = tracery.Grammar(grammar_rules)
				dprint("Tracery initialized.", 1)

need_syns = ["glad", "sad", "happy", "depressed", "hello", "goodbye"]
syns = {}
def norm_lemma_name(l):
		name=l.name().replace("_ ", " ")
		name=name.split(".")[0]
		return name

def initialize_syns():
		dprint("Initializing synonyms...", 1)
		if has_nltk:
				for w in need_syns:
						if not w in syns:
								s=[]
								for syn in wordnet.synsets(w):
										for l in syn.lemmas():
												s.append(norm_lemma_name(l))
								s.append(w)
								syns[w]=s
						if has_tracery:
								grammar_rules["SYN_"+w.upper()]=syns[w]
		dprint("Done initializing synonyms.", 1)

common_swaps = {"father": ["mother"]}
def initialize_common_swaps():
		dprint("Initializing swaps...", 1)
		keys = list(common_swaps.keys())
		for k in keys:
				vals = common_swaps[k]
				for v in vals:
						common_swaps[v]=list(set([k]+common_swaps.get(v, [])))
		if has_tracery:
				for k in common_swaps.keys():
						grammar_rules["SWAP_"+k.upper()]=common_swaps[k]
		dprint("Done initializing swaps.", 1)

def found_kws(s, kws):
		matched=[]
		for kw in kws:
				if s.find(kw)>=0:
						matched.append(kw)
		return matched

def expand_kw(s, kw, struct, use_tracery=False, tracery_pfx=""):
		expanded=[]
		if use_tracery:
				expanded.append(replace_words(s, kw, "#"+tracery_pfx+"_"+kw.upper()+"#"))
		else:
				for v in struct.get(kw, []):
						expanded.append(replace_words(s, kw, v))
		return expanded

def expand_kw_dict(s, struct, use_tracery=False, tracery_pfx=""):
		expanded = []
		for kw in found_kws(s, struct.keys()):
				expanded.extend(expand_kw(s, kw, struct, use_tracery, tracery_pfx))
		return list(set(expanded))

def expand_syns(s, use_tracery=False):
		return expand_kw_dict(s, syns, use_tracery, "SYN")

def expand_swaps(s, use_tracery=False):
		return expand_kw_dict(s, common_swaps, use_tracery, "SWAP")

def expand_str(s, use_tracery=False):
		expanded = []
		if has_nltk:
				expanded = expand_syns(s, use_tracery)
		return expanded

chunkpat=re.compile("([A-Za-z]+|[^A-Za-z]*)")
def replace_words(s, kw, subst):
		chunks=chunkpat.split(s)
		ret=[]
		for c in chunks:
				if c==kw:
						ret.append(subst)
				else:
						ret.append(c)
		return "".join(ret)

def expand_kw_reflexive(key, kw, kw_struct, val_struct):
		expanded={}
		for subst in kw_struct[kw]:
				k=replace_words(key, kw, subst)
				vals=[]
				for v in val_struct[key]:
						vals.append(replace_words(v, kw, subst))
				expanded[k]=list(set(vals))
		return expanded

def expand_key(k):
		expanded = {}
		expanded_keys = expand_syns(k)
		for kk in expanded_keys:
				expanded[kk]=expand_values(rules[k])
		merge_count=merge_rules(expanded)
		for kk in [k]+expanded_keys:
				kws=found_kws(kk, common_swaps)
				for kw in kws:
						expanded, ct=dict_merge(expanded, expand_kw_reflexive(kk, kw, common_swaps, rules))
						merge_count+=ct
		return expanded, merge_count

expand_value_cache={}
def expand_value(v):
		if v in expand_value_cache:
				return expand_value_cache[v]
		expanded = list(set(expand_str(v, use_tracery=has_tracery)))
		expand_value_cache[v]=expanded
		return expanded

def expand_values(v):
		expanded=[]
		for vv in v:
				expanded.extend(expand_value(vv))
		return list(set(expanded))

def expand_rule_keys(k):
		expanded_keys=[k]
		expanded_rules, merge_count = expand_key(k)
		expanded_keys=list(str(expanded_keys+list(expanded_rules.keys())))
		merge_count+=merge_rules(expanded_rules)
		return expanded_keys, merge_count

def expand_rule_values(k):
		if k in rules and len(rules[k])>0:
				vals=expand_values(rules.get(k, []))
				temp=list(set(vals+rules.get(k, [])))
				dirty=True
				if temp == rules.get(k, []):
					dirty=False
				rules[k]=temp
				return dirty
		return False

expand_rule_cache={}
def expand_rule(k):
		if k in expand_rule_cache:
				return 0
		if k in rules:
				dprint("len(rules[\""+str(k)+"\"])="+str(len(rules[k])), 3)
		else:
				dprint("rules[\""+str(k)+"\"] is not defined", 3)
		expanded_keys, ct=expand_rule_keys(k)
		dprint("Key \""+k+"\" has been expanded into "+str(len(expanded_keys))+" new unique keys, with "+str(ct)+" total substituions", 3)
		for item in expanded_keys:
				if expand_rule_values(item):
						ct+=1
		expand_rule_cache[k]=ct
		return ct

def expand_rules(merge_count=0, ttl=10):
		rules["*?x"]=list(set(rules.get("*?x", [])+default_responses))
		rule_keys = list(rules.keys())
		ct=0
		for k in rule_keys:
				ct+=expand_rule(k)
		dprint("expand_rule() produced "+str(ct)+" rule expansions for "+str(len(rule_keys))+" rules", 2)
		merge_count+=ct
		if ct>0 and ttl>0:
				return expand_rules(merge_count, ttl-1)
		else:
				dprint("Merged "+str(merge_count)+" items during expansion; ttl="+str(ttl), 2)
				return merge_count				

def rule_size():
		num_rules = len(rules.keys())
		num_options=0
		for k in rules.keys():
				num_options+=len(rules[k])
		return num_rules, num_options

def rule_size_summary():
		num_rules, num_options = rule_size()
		return str(num_rules)+" rules and a total of "+str(num_options)+" options, averaging "+str(1.0*num_options/num_rules)+" options per rule"

def postprocess_rules():
		# We need the rules in a list containing elements of the following form:
		# `(input pattern, [output pattern 1, output pattern 2, ...]`
		dprint("Ruleset size before expansion: "+rule_size_summary(), 1)
		expand_rules()
		dprint("Ruleset size after expansion: "+rule_size_summary(), 1)
		initialize_tracery()
		dprint("Postprocessing rules..",1)
		rules_list = []
		for pattern, transforms in rules.items():
				# Remove the punctuation from the pattern to simplify matching.
				pattern = remove_punct(str(pattern.upper())) # kill unicode
				transforms = [str(t).upper() for t in transforms]
				rules_list.append((pattern, transforms))
		return rules_list

def main():
		dprint("Initializing...", 1)
		if has_nltk:
				initialize_syns()
		initialize_common_swaps()
		dprint("Done initializing.", 1)
		interact('> ', postprocess_rules(), list([x.upper() for x in default_responses]))
		log.close()

if __name__ == '__main__':
		main()
