#!/usr/bin/env python3

import tracery
from tracery.modifiers import base_english
import pycorpora

rules=tracery.Grammar({"origin":"How is #noun.a# like #noun.a#?", "noun":pycorpora.words.nouns["nouns"]})
rules=tracery.Grammar({"origin":"I am once again asking you how #noun.a# is like #noun.a#?", "noun":pycorpora.words.nouns["nouns"]})

rules.add_modifiers(base_english)

print(rules.flatten("#origin#"))

