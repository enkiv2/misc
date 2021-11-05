#!/usr/bin/env python3

import pycorpora
import tracery
from tracery.modifiers import base_english
import json
import sys
from random import Random
random=Random()


rules={
		"questions":[
								"Have you done it?", 
								"Is it finished?",
								"Is it done?", 
								"Is he gone?", 
								"Is he gone yet?", 
								"Where has he gone?",
								"Where did he go?",
								"Where is he?",
								"Where is it?",
								"Where the hell is it?",
								"Where the hell did it go?",
								"Where did it go?",
								"Where did the damned thing go?",
								"What is it?",
								"What the hell is it?",
								"What is that?",
								"What was that?",
								"What on earth was that?",
								"What the hell was that?",
								"What on earth could that be?",
								"What on earth could that possibly be?",
								"Why on earth could that possibly be?",
								"Why?",
								"Why did he do it?",
								"Why did he do that?",
								"Why did you do that?",
								"How can that be?",
								"Why do you say that?",
								"Do you have any idea why?",
								"What did he do?",
								"He couldn't have, could he?"
								],
		"evasions":[
								"Why?",
								"I don't know and I don't care.",
								"I don't care, and neither should you.",
								"You should know better than to ask.",
								"It doesn't concern you.",
								"It shouldn't concern you.",
								"That should be the least of your worries."
								"How should I know?",
								"It's none of your business.",
								"I didn't think it was any of your business.",
								"It doesn't seem to be any of your business.",
								"As long as you're paid, and paid well, do you really care?",
								"That's my business.",
								"I'd like to keep that quiet. You have things you like to keep quiet too, don't you?",
								"What do you think?",
								"Why are you asking?",
								"Why do you ask?",
								"What makes you ask?",
								"Well, uh... In this particular instance, I'm not so sure.",
								"Well...",
								"To tell you the truth, I'm not so sure.",
								"To tell you the truth, I don't care, and neither should you.",
								"There is more going on than you know.",
								"There is more going on than I know, and it scares me.",
								"Remaining ignorant on this count is good for your health.",
								"What do you mean by that?",
								"Perhaps...",
								"Do you really want the answer to that question?",
								"Do you really want to know?",
								"Do you really want to know the answer to that question?",
								"You know as well as I do.",
								"Don't ask me.",
								"Don't even.",
								"Don't ask me that question.",
								"You know who you should be asking.",
								"You know as well as I do who you should be asking that question.",
								"Sometimes it's better not to talk.",
								"I can't talk about it.",
								"There's no use.",
								"There's no use in asking.",
								"No soap.",
								"What if I'm wrong?",
								"#evasions# #evasions#",
								"#evasions# #questions#",
								"#evasions# #responses#",
								"#evasions# #responses# #responses#"
								],
		"responses":[
								"Now, I find that hard to believe.",
								"You've stood in my way long enough.",
								"Well now...",
								"I see.",
								"That's right.",
								"Maybe there's good left in him yet.",
								"Do you really think so?",
								"Perhaps you're right.",
								"I'll drink to that.",
								"There's no point in hiding it from me.",
								"You're not going to get any arguments from me.",
								"No soap, huh?",
								"I know.",
								"Don't give me that."
								],
		"names": [
								"Loomis",
								"Barnabas",
								"Caroline",
								"Miss Jessel",
								"Willie",
								"Dr. Freudstein",
								"Victoria",
								"Lord Eaten",
								"Elizabeth",
								"Miss Summers"
								],
		"actions":[
								"brooded",
								"stormed out",
								"glared",
								"kicked at the ground",
								"started",
								"gasped",
								"sighed",
								"jumped",
								"turned",
								"paced",
								"stared into space",
								"stepped out of the shadows",
								"stepped into the shadows",
								"stepped into the light",
								"stepped out of the light",
								"whistled tonelessly",
								"squinted"
				],
		"argument":[ 
				'"#questions#", said #names#.\n\n"#evasions#", #names# replied.\n\n',
				'"#questions#", asked #names#. #names# stormed out.\n\n',
				'#names# #actions#. #argument#',
				'#names# #actions#. \'#questions#\'\n\n',
				'"#questions#"\n\n"#evasions#"\n\n"#responses#"\n\n',
				'"#questions#"\n\n"#evasions#"\n\n#argument##argument#',
				'"#questions#" #names# #actions#.\n\n#names# #actions#. "#evasions#"\n\n"#responses#" #names# #actions#.\n\n',
				'#names# #actions#. "#questions#"\n\n#names# #actions#. "#evasions#"\n\n#argument##argument#'
				],
		"location":[
				"The fog rose from the graveyard. In the distance, a wolf howled.",
				"The cobwebs hung heavy from the candlestick.",
				"Grotesque carvings peered out from the corners of the stone walls, leering in the flickering light.",
				"The surf crashed against the cliffs.",
				"These are mysterious days at Colinwood.",
				"The house stands, not sane, walls upright, doors sensibly shut. Whatever walks there walks alone.",
				"Lightning flashes, illuminating the barred windows.",
				"The rain lashed in sheets."
				],
		"origin":[
				"#location#\n\n#argument##argument#\n\n*\n\n",
				"#location# #names# #actions#.\n\n#argument##argument#\n\n*\n\n",
				"#location# #names# #actions#. #names# #actions#.\n\n#argument##argument#\n\n*\n\n",
				"#location# #names# #actions#. #names# #actions#.\n\n#argument##argument##names# #actions#. #argument#\n\n*\n\n",
				"#location# #names# #actions#. #names# #actions#. #names# #actions#.\n\n#argument##argument#\n\n*\n\n",
				"#location# #names# #actions#. #names# #actions#. #names# #actions#.\n\n#argument##argument##argument##names# #actions#. #argument#\n\n*\n\n",
				"#location# #names# #actions#. #names# #actions#. #names# #actions#.\n\n#argument##argument##names# #actions#. #argument##argument#\n\n*\n\n",
				"#location# #names# #actions#. #names# #actions#. #names# #actions#.\n\n#argument##argument##argument##names# #actions#. #argument##argument#\n\n*\n\n"
				]
}
grammar=tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print("# Shark Dadoes, a Can Durtis production\n")
wc=0
while wc<50000:
	sentence=grammar.flatten("#origin#")
	sentence=sentence[0].upper()+sentence[1:]
	sentence=sentence.replace(" ,", ",").replace(",,", ",").replace("..", "...").replace(".,", ",")
	wc+=len(sentence.split())
	sys.stdout.write(sentence+random.choice([" ", "\n\n"]))
	sys.stdout.flush()
sys.stdout.write("\n")

