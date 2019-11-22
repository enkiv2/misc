#!/usr/bin/env python3

import pycorpora
import tracery
from tracery.modifiers import base_english
import json
import sys
from random import Random
random=Random()


cities=(
		list(map(lambda x: x["city"],pycorpora.geography.us_cities["cities"]+
		pycorpora.geography.norwegian_cities["cities"]))+
		pycorpora.geography.english_towns_cities["towns"]+
		pycorpora.geography.english_towns_cities["cities"]
		)
objects=(
		pycorpora.objects.objects["objects"]+
		pycorpora.plants.flowers["flowers"]+
		pycorpora.humans.bodyParts["bodyParts"]
		)
rules={
		"empty":["Empty #salons#.", "Empty #corridors#.", "Empty #chairs#."],
		"salons": ["Salons. #corridors#", "Salons. #empty#", "Salons.", "Salons. #salons#"],
		"corridors":["Corridors.", "Corridors. #salons#", "Corridors. #doors#"],
		"doors":["Doors. #doors#", "Doors. #salons#"],
		"chairs":["chairs, deep armchairs, #carpets#", "armchairs. #carpets#", "deep armchairs.", "chairs. #hangings#"],
		"carpets":["Carpets.", "thick carpets.", "Carpets. #hangings#", "thick carpets. #hangings#", "Carpets. #carpets#", "Carpets. #stairs#"],
		"hangings":["Hangings.", "Heavy hangings.", "Hangings. #hangings#", "Hangings. #stairs#"],
		"stairs":["Stairs.", "Stairs, steps.", "Steps, one after the other." "Steps, one after another.", "#stairs# #hangings#", "#stairs# #empty#"],
		"glass":["Glass objects.", "Empty glasses.", "Thick glasses.", "Objects still intact.", "A glass that falls.", "Black mirrors.", "Mirrored hallways.", "Glass partition.", "A glass that falls, three, two, one, zero.", "Glass partition, letters.", "#glass# #glass#", "#glass# #glass# #empty#", "#glass# #corridors#", "#glass# #objects#"],
		"objects": objects,
		"cities": cities,
		"lasttime": ["It was last #time#, at #cities#.", "It was last #time#, or perhaps last #time#.", "Perhaps it wasn't #cities#. Perhaps it was #cities#, or #cities#.", "Perhaps it was #cities#, or right here.", "#lasttime#. #lasttime#.\n\n", "\n\n#lasttime#. #lasttime#", "\n\n#lasttime#. #lasttime#\n\n", "#lasttime#.\n\n#empty#"],
		"time":["week", "month", "year", "week", "month", "year", "century", "#time# or #time#", "#time# or last #time#", "#time# or #lasttime#", "#time.s#"],
		"x":["I must have you alive. Alive, as you have already been every evening, for #time.s#, for #time.s#.", "A #time#, a #time#, a #time#, it's all the same to me.", "I have been waiting for #time.s#.", "Yes, I know. I don't care.", "For #time.s# and #time.s#.", "Why don't you still want to remember anything?", "You are afraid to remember.", "You don't want to remember because you're afraid.", "#x# #x# #empty#", "#x# #corridors#", "#x#\n\n#y#\n\n", "The statues might as well have been you, or me.", "The statues might as well have been anyone. They might as well have been you and me."],
		"y":["You're raving.", "I don't remember.", "No, it's nothing.", "No, there was no window. It was an engraving.", "No, there was no mirror there. It was over the fireplace.", "#y#\n\n#x#"],
		"z":["This time last #time# it was so cold that the river froze.", "It's not that I cannot lose, but that I have never lost.", "Will you be attending the play?", "The statues are a depiction of the coronation of Charles III. The classical stylings are purely conventional."],
		"geometric":["Gardens arranged in a comforting geometry. #empty#", "Gardens arranged in a comforting geometry. #corridors#", "Gardens.", "Gardens, arranged with geometrical rigidity. #geometric#", "The gardens were guarded by two statues on plinths. Some nameless figures, mythological."]
}
grammar=tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print("# Last Week At Karlsburg\n")
wc=0
while wc<50000:
	sentence=grammar.flatten("#"+random.choice(list(rules.keys()))+"#")
	sentence=sentence[0].upper()+sentence[1:]
	sentence=sentence.replace(" ,", ",").replace(",,", ",").replace("..", "...").replace(".,", ",")
	wc+=len(sentence.split())
	sys.stdout.write(sentence+random.choice([" ", "\n\n"]))
	sys.stdout.flush()
sys.stdout.write("\n")

