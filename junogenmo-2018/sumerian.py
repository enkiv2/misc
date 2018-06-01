#!/usr/bin/env python

from random import Random
random=Random()

godpfx=["en", "nin"]
domains={}
domains["ki"]=["earth", "land"]
domains["a"]=["water", "sea", "drink", "beer"]
domains["kashi"]=["drink", "beer", "tea"]
domains["lil"]=["wind", "rain", "weather", "sky"]
domains["an"]=["sky", "stars", "heaven"]

domainInverse={}
for i in domains.keys():
	for j in domains[i]:
		if not (j in domainInverse):
			domainInverse[j]=[i]
		else:
			domainInverse[j].append(i)

genericEpithets=["beloved %god%", "whose advice is always advisable"]

epithets={}
epithets["earth"]=["who puts the continents in their places", "who sets the nations and draws their borders", "whose hands build the mountains and topple them"]
epithets["land"]=["whose excrement fertilizes the fields", "whose plow-furroughs are the valleys", "whose dung-heaps are the mountains"]
epithets["water"]=["whose bodily fluids are the life-giving river", "who sets the seas in motion", "whose breath is the waves"]
epithets["sea"]=["who guides the ships", "whose sweat is the waves", "fish-speckled"]
epithets["drink"]=["whose domain is the hops", "who transmogrifies the barley", "whose spit is the yeast", "joy-giving", "mirth-making", "joyous", "mirthful", "drunken", "red-cheeked"]
epithets["beer"]=["who watches over the barley", "who guides the hops", "whose semen is the yeast", "who guides the yeast", "mirth-giving", "joy-making"]
epithets["tea"]=["who boils the water", "who gathers the herbs", "who makes the herbs grow straight"]
epithets["wind"]=["whose breath spreads the pollen", "whose rage blows down houses", "whose sneeze caresses the foliage"]
epithets["rain"]=["storm-bringer", "rain-bringer", "whose tears are the rain", "whose snot is the hail"]
epithets["weather"]=["storm-maker", "lord of sunshine", "wind-bringer", "lord of air-space"]
epithets["sky"]=["rosy-fingered", "star-speckled", "cosmic", "cloud-adorned", "airy"]
epithets["heaven"]=["who holds the firmament", "star-maker", "cosmic", "star-lord", "planet-pusher", "firmament-holder"]
epithets["stars"]=["star-speckled", "star-maker", "shining", "sparkling", "star-fingered", "star-spangled", "highest", "altitudinous"]

storyTemplates=[
	"%a% went to the market in %city%. There were %band% %a% met %b%.", 
	"%a% was sitting on a throne. Around %a% there were %band% and %band% and %band% and the throne was in %city%.", 
	"%a% and %b% made a bet, wagering %wagers%. %a% won, and %b% became jealous, accusing %a% of cheating. So, %b% and %a% made another bet, and %a% won again. Finally, %b% removed all their clothes and seduced %a%, who gave up their winnings, and %b% left on a magic boat",
	"%a% was sad. %b% said, \"%a%, why are you crying?\" %a% didn't respond. %b% said, \"%a%, my %a%, why do you cry? You are %a%, %a% is who is crying. Why should %a% cry?\" %a% saw that %b% was correct. %a% was happy again."
]

cities=["Ur", "Uruk", "Arrata", "Eridu", "Eridug", "Niveh", "Gas", "Oz"]

storyNames=[
	"The lamentation of %a%",
	"The lamentation of %a% in %city%",
	"%a% and %b%",
	"%a% and %b% in %city%",
	"%a% and the lord of %city%",
	"%a% and the priest of %b%"
]

def musicalInstrumentName():
	return (
		random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z", ""])+
		random.choice(["a", "e", "i", "o", "u"])+
		random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z", ""])+
		random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z", ""])+
		random.choice(["a", "e", "i", "o", "u"])+
		random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z", ""])+
		" "+random.choice(["drums", "lutes", "flutes", "whistles", "reeds", "birds", "singers", "lamentation singers"]))
def buildBand(ttl=25):
	bandMembers=[]
	for i in range(0, ttl):
		bandMembers.append(musicalInstrumentName())
	return ",\n\t".join(bandMembers)+"\n"
def buildGod(domain):
	properDomain=random.choice(domainInverse[domain])
	name=random.choice(([random.choice(godpfx)+properDomain]*3)+[properDomain+random.choice(godpfx)])
	return (name.capitalize(), properDomain)

def buildEpithet(domain, godName):
	if(random.randint(0, 25)==0):
		return "["+str(random.randint(1, 25))+" ms have: "
	if(random.randint(0, 2)):
		if(random.randint(0, 3)):
			return random.choice(epithets[random.choice(domains[domain])])
		else:
			if(random.randint(0, 5)):
				return "whose domain is the "+random.choice(domains[domain])
			else:
				return godName
	else:
		return random.choice(genericEpithets).replace("%god%", godName)

def buildEpithetList(domain, godName, ttl=25):
	epithetList=[godName]
	for i in range(0, ttl):
		epithetList.append(buildEpithet(domain, godName))
	return ", \n\t".join(epithetList)+"\n"

gods=[]
for i in range(0, 15):
	gods.append(buildGod(random.choice((list)(domainInverse.keys()))))

def genStoryName():
	template=random.choice(storyNames)
	template=template.replace("%a%", random.choice(gods)[0])
	template=template.replace("%b%", random.choice(gods)[0])
	template=template.replace("%city%", random.choice(cities))
	return template

def genStory():
	a=random.choice(gods)
	b=random.choice(gods)
	template=random.choice(storyTemplates)
	while(template.find("%")>=0):
		template=template.replace("%a%", buildEpithetList(a[1], a[0], random.randint(1, 50)))
		template=template.replace("%b%", buildEpithetList(b[1], b[0], random.randint(1, 50)))
		template=template.replace("%wagers%", random.choice(["the crown of %city%", "the great ME of princeship", "the domain of the "+random.choice((list)(domainInverse.keys()))]))
		template=template.replace("%city%", random.choice(cities))
		template=template.replace("%band%", buildBand())
	return template

print(genStoryName().upper())
print()
for i in range(0, 15):
	print(genStory())

