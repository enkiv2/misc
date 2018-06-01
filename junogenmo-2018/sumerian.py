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
epithets["drink"]=["whose domain is the hops", "who transmogrifies the barley", "whose spit is the yeast", "joy-giving", "mirth-making"]
epithets["beer"]=["who watches over the barley", "who guides the hops", "whose semen is the yeast", "who guides the yeast", "mirth-giving", "joy-making"]
epithets["tea"]=["who boils the water", "who gathers the herbs", "who makes the herbs grow straight"]
epithets["wind"]=["whose breath spreads the pollen"]
epithets["rain"]=["storm-bringer"]
epithets["weather"]=["storm-maker"]
epithets["sky"]=["rosy-fingered", "star-speckled"]
epithets["heaven"]=["who holds the firmament", "star-maker"]
epithets["stars"]=["star-speckled", "star-maker", "shining", "sparkling", "star-fingered", "star-spangled", "highest", "altitudinous"]

storyTemplates=[
	"%a% went to the market and met %b%.", 
	"%a% was sitting on a throne.", 
	"%a% and %b% made a bet, wagering %wagers%. %a% won, and %b% became jealous, accusing %a% of cheating. So, %b% and %a% made another bet, and %a% won again. Finally, %b% removed all their clothes and seduced %a%, who gave up their winnings, and %b% left on a magic boat",
	"%a% was sad. %b% said, \"%a%, why are you crying?\" %a% didn't respond. %b% said, \"%a%, my %a%, why do you cry? You are %a%, %a% is who is crying. Why should %a% cry?\" %a% saw that %b% was correct. %a% was happy again."
]

def buildGod(domain):
	properDomain=random.choice(domainInverse[domain])
	name=random.choice(([random.choice(godpfx)+properDomain]*3)+[properDomain+random.choice(godpfx)])
	return (name.capitalize(), properDomain)

def buildEpithet(domain, godName):
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

def genStory():
	a=random.choice(gods)
	b=random.choice(gods)
	template=random.choice(storyTemplates)
	while(template.find("%")>=0):
		template=template.replace("%a%", buildEpithetList(a[1], a[0], random.randint(1, 50)))
		template=template.replace("%b%", buildEpithetList(b[1], b[0], random.randint(1, 50)))
		template=template.replace("%wagers%", random.choice(["the crown", "the great ME of princeship", "the domain of the "+random.choice((list)(domainInverse.keys()))]))
	return template
for i in range(0, 15):
	print(genStory())

