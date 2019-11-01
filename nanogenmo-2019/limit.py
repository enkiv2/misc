#!/usr/bin/env python3

import pycorpora
import tracery
from tracery.modifiers import base_english
import json
import nltk
from nltk.corpus import wordnet, cmudict
import sys
import randomWikimediaImage
from random import Random
random=Random()


synonyms={}
def syns(w):
        global synonyms
        w=w.lower()
        if not (w in synonyms):
                ret=[]
                for syn in wordnet.synsets(w):
                        for l in syn.lemmas():
                                ret.append(l.name().replace("_", " "))
                ret.append(w)
                synonyms[w]=list(set(ret))
        if len(synonyms[w])==0: return [w]
        return synonyms[w]
def synexp(ws):
		ax=[]
		for w in ws:
				ax+=syns(w)
		return list(set(ax))

gross=(
		pycorpora.get_file("materials", "abridged-body-fluids")["abridged body fluids"]+
		["matted hair", "rotting meat", "maggots", "feces", "used chewing gum", "teeth", "fingers", "spiders", "snakes", "flies", "wasps", "bees", "yellowjackets", "worms"])
gross=synexp(gross)
materials=(
		((pycorpora.get_file("materials", "layperson-metals")["layperson metals"]+
		pycorpora.get_file("materials", "natural-materials")["natural materials"]+
		pycorpora.materials["packaging"]["packaging"]+
		pycorpora.get_file("materials", "plastic-brands")["plastic brands"])*5)+
		pycorpora.plants.flowers["flowers"]+
		pycorpora.humans.bodyParts["bodyParts"]+
		pycorpora.get_file("materials", "decorative-stones")["decorative stones"]+
		gross)
cities=(
		list(map(lambda x: x["city"],pycorpora.geography.us_cities["cities"]+
		pycorpora.geography.norwegian_cities["cities"]))+
		pycorpora.geography.english_towns_cities["towns"]+
		pycorpora.geography.english_towns_cities["cities"]
		)
with open("containers.json") as f:
		containers=json.load(f)["containers"]
containers=containers+pycorpora.architecture.rooms["rooms"]+pycorpora.architecture.passages["passages"]
large=["massive", "cyclopean", "huge", "vast", "enormous", "great"]
small=["tiny", "miniscule", "infinitesimal"]
old=["ancient", "antedeluvian", "crumbling", "mouldy", "shattered", "forgotten", "long-forgotten"]
new=["evanescent", "fresh", "polished"]
sublime=large+small+old+new
sublime2=synexp(sublime)
objects=(
		pycorpora.objects.objects["objects"]+
		pycorpora.plants.flowers["flowers"]+
		pycorpora.humans.bodyParts["bodyParts"]+
		pycorpora.mythology.greek_gods["greek_gods"]+
		pycorpora.mythology.lovecraft["deities"]+
		pycorpora.mythology.lovecraft["supernatural_creatures"]+
		pycorpora.mythology.monsters["names"]+
		pycorpora.mythology.norse_gods["norse_deities"]["gods"]+
		pycorpora.mythology.norse_gods["norse_deities"]["goddesses"]+
		pycorpora.mythology.greek_titans["greek_titans"]+
		pycorpora.mythology.roman_deities["roman_deities"]+
		list(map(lambda x: x["name"], pycorpora.mythology.hebrew_god["names"]))+
		list(pycorpora.mythology.egyptian_gods["egyptian_gods"].keys())
		)
unheimlich_one=["replica", "model", "scale model", "twin", "duplicate", "copy", "doll", "sculpture"]
unheimlich_adj=["ersatz", "duplicate", "replica", "model", "twin"]
unheimlich_many=["endless", "uncountable", "countless"]
rules={
		"origin": (
				[
				"#origin#, but #origin#",
				"#origin#, however #origin#",
				"#origin#, while #origin#",
				"#origin#, meanwhile #origin#"
				]+(["#position# #origin#"]*5)+
				([
				"within #contained_a#, #unheimlich_sing# of #materials# #eeries_sing#",
				"within #contained_a#, #unheimlich_plur# of #materials# #eeries_plur#",
				"within #contained_s#, #unheimlich_plur# of #materials# #eeries_plur#"
				]*3)
				),
		"position":["#relative_position# #location#"],
		"relative_position":["above", "below", "high above", "deep below", "miles above", "fathoms below", "miles below", "#cardinal_dir# of"],
		"cardinal_dir":["north", "south", "east", "west", "upriver", "upstream", "downriver", "downstream", "upwind", "downwind"],
		"location":["Philly", "earth", "the forgotten city", "the sublunar world", "the forgotten city", "the deep woods"]+cities,
		"contained_a": [
				"#sublimex.a# #containers# of #materials#", 
				"#containers.s# of #materials#", 
				],
		"contained_s": [
				"#sublimex# #containers.s# of #materials#",
				"#containers.s# of #materials#",
				],
		"eeries_sing": ([
				"waits", "calls", "knows your name", "silently judges", "beckons", "weeps", "wails", "chuckles", 
				"awaits your words", "listens", "judges", "sits in silent judgement", "whispers your name"]*3)+
				[
				", #adj#, #adj#, #eeries_sing#",
				", #adj#, #sublimex#, #eeries_sing#",
				", #sublimex#, #adj#, #eeries_sing#",
				", whose origin we may never know, #eeries_sing#", ", whose purpose we cannot imagine, #eeries_sing#",
				", whose purpose we may never know, #eeries_sing#", ", whose dark purpose we cannot imagine, #eeries_sing#",
				", whose unknowable origins are lost in the fog of time, #eeries_sing#", 
				", whose terrible unknowable purpose remains unimaginable, #eeries_sing#",
				", whose unimaginable origins are lost in the fog of time, #eeries_sing#", 
				", whose terrible purpose remains incomprehensible to man, #eeries_sing#",
				", #sublimex#, #eeries_sing#",
				", whose #objects.s# #eeries_plur#, #eeries_sing#", 
				", whose #sublimex# #objects.s# #eeries_plur#, #eeries_sing#",
				", whose #contained_s# #unheimlich_plur# #eeries_plur#, #eeries_sing#", 
				", whose #contained_a# #unheimlich_sing# #eeries_sing#, #eeries_sing#",
				", whose #adj# origin we may never know, #eeries_sing#", ", whose #adj# purpose we cannot imagine, #eeries_sing#",
				", whose #adj# purpose we may never know, #eeries_sing#", ", whose #adj# dark purpose we cannot imagine, #eeries_sing#",
				", whose #adj# unknowable origins are lost in the fog of time, #eeries_sing#", 
				", whose #adj# terrible unknowable purpose remains unimaginable, #eeries_sing#",
				", whose #adj# unimaginable origins are lost in the fog of time, #eeries_sing#", 
				", whose #adj# terrible purpose remains incomprehensible to man, #eeries_sing#",
				", #sublimex#, #eeries_sing#",
				", whose #adj# #objects.s# #eeries_plur#, #eeries_sing#", 
				", whose #adj# #sublimex# #objects.s# #eeries_plur#, #eeries_sing#",
				", whose #adj# #contained_s# #unheimlich_plur# #eeries_plur#, #eeries_sing#", 
				", whose #adj# #contained_a# #unheimlich_sing# #eeries_sing#, #eeries_sing#"
				],
		"eeries_plur": (["wait", "call", "know your name", "silently judge", "beckon", "weep", "wail", "chuckle"]*3)+
		["whose #adj# origin we may never know #eeries_plur#", "whose #adj# purpose we cannot imagine #eeries_plur#",
		", #sublimex#, #eeries_plur#",
		", #sublimex#, #sublimex#, #eeries_plur#",
		", #sublimex#, #eerie_gerund#, #eeries_plur#",
		", #sublimex#, #sublimex#, #eerie_gerund#, #eeries_plur#",
		"whose #objects# #eeries_sing#, #eeries_plur#",
		"whose #objects.s# #eeries_plur#, #eeries_plur#",
		"whose #sublimex# #objects# #eeries_sing#, #eeries_plur#",
		"whose #sublimex# #objects# #eeries_sing#, #eeries_plur#",
		"whose #sublimex# #objects#, #sublimex#, #sublimex#, #eeries_sing#, #eeries_plur#",
		"whose #sublimex# #objects#, #sublimex#, #eerie_gerund#, #eeries_sing#, #eeries_plur#",
		"whose #adj# #objects# #eeries_sing#, #eeries_plur#",
		"whose #adj# #objects.s# #eeries_plur#, #eeries_plur#",
		"whose #adj# #sublimex# #objects# #eeries_sing#, #eeries_plur#",
		"whose #adj# #sublimex# #objects# #eeries_sing#, #eeries_plur#",
		"whose #adj# #sublimex# #objects#, #sublimex#, #sublimex#, #eeries_sing#, #eeries_plur#",
		"whose #adj# #sublimex# #objects#, #sublimex#, #eerie_gerund#, #eeries_sing#, #eeries_plur#",
		", #adj#, #adj#, #eeries_plur#",
		", #adj#, #eerie_gerund#, #eeries_plur#",
		", #eerie_gerund#, #adj#, #eeries_plur#",
		", #adj#, #sublimex#, #eeries_plur#",
		", #sublimex#, #adj#, #eeries_plur#",
		", #adj#, #sublimex#, #eerie_gerund#, #eeries_plur#"
		],
		"eerie_gerund":["waiting", "watching", "lurking", "biding time", "mocking", "knowing", "judging", "silently judging", "sitting in judgement", "watching", "watching in judgement", "waiting in judgement", "watching carefully", "watching mockingly", "silently mocking", "watching in silent judgement", "watching in silent mockery", "waiting patiently", "#sublimex#, #eerie_gerund#", "#eerie_gerund#, #eerie_gerund#"],
		"adj":["vast", "purposeless", "unknowable", "arcane", "unimaginable", "mad", "terrible", "incredible", "unnameable", "unimaginable", "nameless"],
		"sublimex":(["#sublime#"]*10+["#sublime2#"]+["#adj#"]*5),
		"sublime":sublime,
		"sublime2":sublime2,
		"containers":containers,
		"materials":materials,
		"objects":synexp(objects),
		"unheimlich_sing": [
				"#sublimex# #unheimlich_sing#",
				"#unheimlich_one.a#", 
				"#unheimlich_one.a# of #objects.a#",
				"#unheimlich_adj.a# #unheimlich_one#", 
				"#unheimlich_adj.a# #unheimlich_one# of #objects.a#",
				],
		"unheimlich_plur": [
				"#sublimex# #unheimlich_plur#",
				"#unheimlich_many# #objects.s#", 
				"#unheimlich_many# #unheimlich_adj# #objects.s#", 
				"#unheimlich_many# #unheimlich_adj# #unheimlich_one.s#",
				"#unheimlich_many# #unheimlich_adj# #unheimlich_one.s# of #objects.s#"
				],
		"unheimlich_one":unheimlich_one,
		"unheimlich_many":synexp(unheimlich_many),
		"unheimlich_adj":synexp(unheimlich_adj)
}
grammar=tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print("# A Catalogue of Limit Objects\n")
print("## Object #"+str(random.randint(0, 1000000))+"\n")
wc=0
while wc<50000:
	sentence=grammar.flatten("#origin#")+"."
	sentence=sentence[0].upper()+sentence[1:]
	sentence=sentence.replace(" ,", ",").replace(",,", ",")
	wc+=len(sentence.split())
	sys.stdout.write(sentence+random.choice([" ", " ", " ", "\n\n## Object #"+str(random.randint(0, 1000000))+"\n\n"]))
	if(random.choice([False]*2+[True])):
		words=sentence.split()
		item=random.choice(random.choice([words, objects, materials]))
		img=randomWikimediaImage.getRandomImage(item)
		if(img):
				sys.stdout.write(random.choice(["", "\n", "\n"])+"\n!["+item+"]("+img+" \""+item+"\")\n"+random.choice(["", "\n", "\n"]))
		sys.stdout.flush()
sys.stdout.write("\n")

