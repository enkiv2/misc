#!/usr/bin/env python

"""
**Eliza** is a pattern-matching automated psychiatrist.  Given a set of rules
in the form of input/output patterns, Eliza will attempt to recognize user input
phrases and generate relevant psychobabble responses.

Each rule is specified by an input pattern and a list of output patterns.  A
pattern is a sentence consisting of space-separated words and variables.  Input
pattern variables come in two forms: single variables and segment variables;
single variables (which take the form `?x`) match a single word, while segment
variables (which take the form `?*x`) can match a phrase.  Output pattern
variables are only single variables.  The variable names contained in an input
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


## Talking to the computer

def interact(prompt, rules, default_responses):
	"""Have a conversation with a user."""
	# Read a line, process it, and print the results until no input remains.
	while True:
		try:
			# Remove the punctuation from the input and convert to upper-case
			# to simplify matching.
			input = remove_punct(raw_input(prompt).upper())
			if not input:
				continue
		except:
			break
		print respond(rules, input, default_responses)


def respond(rules, input, default_responses):
	"""Respond to an input sentence according to the given rules."""

	input = input.split() # match_pattern expects a list of tokens

	# Look through rules and find input patterns that matches the input.
	matching_rules = []
	for pattern, transforms in rules:
		pattern = pattern.split()
		replacements = match_pattern(pattern, input)
		if replacements:
			matching_rules.append((transforms, replacements))

	# When rules are found, choose one and one of its responses at random.
	# If no rule applies, we use the default rule.
	if matching_rules:
		responses, replacements = random.choice(matching_rules)
		response = random.choice(responses)
	else:
		replacements = {}
		response = random.choice(default_responses)

	# Replace the variables in the output pattern with the values matched from
	# the input string.
	for variable, replacement in replacements.items():
		replacement = ' '.join(switch_viewpoint(replacement))
		if replacement:
			response = response.replace('?' + variable, replacement)
	
	return response.capitalize()
	

## Pattern matching

def match_pattern(pattern, input, bindings=None):
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
	if pattern == input:
		return bindings

	bindings = bindings or {}

	# Match input and pattern according to their types.
	if is_segment(pattern):
		token = pattern[0] # segment variable is the first token
		var = token[2:] # segment variable is of the form ?*x
		return match_segment(var, pattern[1:], input, bindings)
	elif is_variable(pattern):
		var = pattern[1:] # single variables are of the form ?foo
		return match_variable(var, [input], bindings)
	elif contains_tokens(pattern) and contains_tokens(input):
		# Recurse:
		# try to match the first tokens of both pattern and input.  The bindings
		# that result are used to match the remainder of both lists.
		return match_pattern(pattern[1:],
							 input[1:],
							 match_pattern(pattern[0], input[0], bindings))
	else:
		return False


def match_segment(var, pattern, input, bindings, start=0):
	"""
	Match the segment variable against the input.

	pattern and input should be lists of tokens.

	Looks for a substring of input that begins at start and is immediately
	followed by the first word in pattern.  If such a substring exists,
	matching continues recursively and the resulting bindings are returned;
	otherwise returns False.
	"""

	# If there are no words in pattern following var, we can just match var
	# to the remainder of the input.
	if not pattern:
		return match_variable(var, input, bindings)

	# Get the segment boundary word and look for the first occurrence in
	# the input starting from index start.
	word = pattern[0]
	try:
		pos = start + input[start:].index(word)
	except ValueError:
		# When the boundary word doesn't appear in the input, no match.
		return False

	# Match the located substring to the segment variable and recursively
	# pattern match using the resulting bindings.
	var_match = match_variable(var, input[:pos], dict(bindings))
	match = match_pattern(pattern, input[pos:], var_match)

	# If pattern matching fails with this substring, try a longer one.
	if not match:
		return match_segment(var, pattern, input, bindings, start + 1)
	
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
			and pattern[1] in string.letters
			and ' ' not in pattern)


def is_segment(pattern):
	"""Test if pattern begins with a segment variable."""
	return (type(pattern) is list
			and pattern
			and len(pattern[0]) > 2
			and pattern[0][0] == '?'
			and pattern[0][1] == '*'
			and pattern[0][2] in string.letters
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
		"How do you do. Please state your problem."
		],
	"?*x computer ?*y": [
		"Do computers worry you?",
		"What do you think about machines?",
		"Why do you mention computers?",
		"What do you think machines have to do with your problem?",
		],
	"?*x name ?*y": [
		"I am not interested in names",
		],
	"?*x sorry ?*y": [
		"Please don't apologize",
		"Apologies are not necessary",
		"What feelings do you have when you apologize",
		],
	"?*x I remember ?*y": [
		"Do you often think of ?y?",
		"Does thinking of ?y bring anything else to mind?",
		"What else do you remember?",
		"Why do you recall ?y right now?",
		"What in the present situation reminds you of ?y?",
		"What is the connection between me and ?y?",
		],
	"?*x do you remember ?*y": [
		"Did you think I would forget ?y?",
		"Why do you think I should recall ?y now?",
		"What about ?y?",
		"You mentioned ?y",
		],
	"?*x I want ?*y": [
		"What would it mean if you got ?y?",
		"Why do you want ?y?",
		"Suppose you got ?y soon."
		],
	"?*x if ?*y": [
		"Do you really think it's likely that ?y?",
		"Do you wish that ?y?",
		"What do you think about ?y?",
		"Really--if ?y?"
		],
	"?*x I dreamt ?*y": [
		"How do you feel about ?y in reality?",
		],
	"?*x dream ?*y": [
		"What does this dream suggest to you?",
		"Do you dream often?",
		"What persons appear in your dreams?",
		"Don't you believe that dream has to do with your problem?",
		],
	"?*x my mother ?*y": [
		"Who else in your family ?y?",
		"Tell me more about your family",
		],
	"?*x my father ?*y": [
		"Your father?",
		"Does he influence you strongly?",
		"What else comes to mind when you think of your father?",
		],
	"?*x I am glad ?*y": [
		"How have I helped you to be ?y?",
		"What makes you happy just now?",
		"Can you explain why you are suddenly ?y?",
		],
	"?*x I am sad ?*y": [
		"I am sorry to hear you are depressed",
		"I'm sure it's not pleasant to be sad",
		],
	"?*x are like ?*y": [
		"What resemblence do you see between ?x and ?y?",
		],
	"?*x is like ?*y": [
		"In what way is it that ?x is like ?y?",
		"What resemblence do you see?",
		"Could there really be some connection?",
		"How?",
		],
	"?*x alike ?*y": [
		"In what way?",
		"What similarities are there?",
		],
	"?* same ?*y": [
		"What other connections do you see?",
		],
	"?*x no ?*y": [
		"Why not?",
		"You are being a bit negative.",
		"Are you saying 'No' just to be negative?"
		],
	"?*x I was ?*y": [
		"Were you really?",
		"Perhaps I already knew you were ?y.",
		"Why do you tell me you were ?y now?"
		],
	"?*x was I ?*y": [
		"What if you were ?y?",
		"Do you think you were ?y?",
		"What would it mean if you were ?y?",
		],
	"?*x I am ?*y": [
		"In what way are you ?y?",
		"Do you want to be ?y?",
		],
	"?*x am I ?*y": [
		"Do you believe you are ?y?",
		"Would you want to be ?y?",
		"You wish I would tell you you are ?y?",
		"What would it mean if you were ?y?",
		],
	"?*x am ?*y": [
		"Why do you say 'AM?'",
		"I don't understand that"
		],
	"?*x are you ?*y": [
		"Why are you interested in whether I am ?y or not?",
		"Would you prefer if I weren't ?y?",
		"Perhaps I am ?y in your fantasies",
		],
	"?*x you are ?*y": [
		"What makes you think I am ?y?",
		],
	"?*x because ?*y": [
		"Is that the real reason?",
		"What other reasons might there be?",
		"Does that reason seem to explain anything else?",
		],
	"?*x were you ?*y": [
		"Perhaps I was ?y?",
		"What do you think?",
		"What if I had been ?y?",
		],
	"?*x I can't ?*y": [
		"Maybe you could ?y now",
		"What if you could ?y?",
		],
	"?*x I feel ?*y": [
		"Do you often feel ?y?"
		],
	"?*x I felt ?*y": [
		"What other feelings do you have?"
		],
	"?*x I ?*y you ?*z": [
		"Perhaps in your fantasy we ?y each other",
		],
	"?*x why don't you ?*y": [
		"Should you ?y yourself?",
		"Do you believe I don't ?y?",
		"Perhaps I will ?y in good time",
		],
	"?*x yes ?*y": [
		"You seem quite positive",
		"You are sure?",
		"I understand",
		],
	"?*x someone ?*y": [
		"Can you be more specific?",
		],
	"?*x everyone ?*y": [
		"Surely not everyone",
		"Can you think of anyone in particular?",
		"Who, for example?",
		"You are thinking of a special person",
		],
	"?*x always ?*y": [
		"Can you think of a specific example?",
		"When?",
		"What incident are you thinking of?",
		"Really--always?",
		],
	"?*x what ?*y": [
		"Why do you ask?",
		"Does that question interest you?",
		"What is it you really want to know?",
		"What do you think?",
		"What comes to your mind when you ask that?",
		],
	"?*x perhaps ?*y": [
		"You do not seem quite certain",
		],
	"?*x are ?*y": [
		"Did you think they might not be ?y?",
		"Possibly they are ?y",
		],
	}

default_responses = [
	"Very interesting",
	"I am not sure I understand you fully",
	"What does that suggest to you?",
	"Please continue",
	"Go on",
	"Do you feel strongly about discussing such things?",
	]

def elizaResponse(line):
	rules_list = []
	for pattern, transforms in rules.items():
		# Remove the punctuation from the pattern to simplify matching.
		pattern = remove_punct(str(pattern.upper())) # kill unicode
		transforms = [str(t).upper() for t in transforms]
		rules_list.append((pattern, transforms))
	return respond(rules_list, remove_punct(line).upper(), map(str.capitalize, default_responses))

def main():
	# We need the rules in a list containing elements of the following form:
	# `(input pattern, [output pattern 1, output pattern 2, ...]`
	rules_list = []
	for pattern, transforms in rules.items():
		# Remove the punctuation from the pattern to simplify matching.
		pattern = remove_punct(str(pattern.upper())) # kill unicode
		transforms = [str(t).upper() for t in transforms]
		rules_list.append((pattern, transforms))
	interact('> ', rules_list, map(str.capitalize, default_responses))

if __name__ == '__main__':
	main()
