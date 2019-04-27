label start:
    window hide
    scene black
    centered "{color=#fff}{cps=15}\"Witchcraft always has a hard time, until it becomes established and changes its name.\"{/cps}{/color}"
    extend "{color=#fff}{cps=15}\n{space=500}- Charles Fort,{/cps}{/color}"
    extend "{color=#fff}{cps=15}\n{space=400}            Lo!{/cps}{/color}"
    scene white with dissolve
    scene black with dissolve
    centered "{color=#fff}{cps=20}In the year 2012, in the small town of Yomiyama, a series of deaths occurred.{/cps}{/color}"
    extend "{color=#fff}{cps=20}\nDespite investigation, many mysteries remain.{/cps}{/color}"
    extend "{color=#fff}{cps=20}\nBelow the surface of this town, a great deal of machinery was in motion.{/cps}{/color}"
    centered "{color=#fff}{b}PART 1{/b}: {i}Wild Talents{/i}{/color}"
    centered "{color=#fff}{b}15th March, 2012{/b}{/color}"
    window show
    scene taxi rain
    "Taxi driver" "They sure picked a bad night to move you in, didn't they, miss?"
    misa "Yes, bad luck, isn't it?"
    misa "{i}Worse, since I'm stuck with such a perv for a driver...{/i}"
    "Taxi driver" "{i}such a pretty young girl not so many fares are so pretty girls these days grow up so fast did i remember to shut that upstairs window it sure is pouring too bad she isn't wearing white soaked already no no she would need to beg first what's that van doing there sure is an old one he's wet{/i}"
    n "Misa looked out the window."
    scene kuroki van rain splash
    misa "Driver, pick up that man please."
    "Taxi driver" "Understood."
    scene taxi rain
    n "The driver pulled up to the broken-down van and idled the engine, rolling down his window."
    "Stranded man" "Any chance of helping out a poor traveler? I need a ride to the nearest police box."
    "Taxi driver" "That's up to my passenger."
    misa "Please join me."
    "Taxi driver" "It's a little out of our way, miss."
    misa "We're almost to our desination. The time, and the cost, must be a drop in the bucket compared to how far we've already come."
    "Taxi driver" "Of course. Very good."
    n "The drenched stranger slid into the seat beside Misa."
    misa "{i}Strange... I can't read him...{/i}"
    n "The man noticed her look, and smiled graciously."
    "Stranded man" "I am Kuroki. Fyodor Federov Kuroki: poet, linguist, and freelance combat etymologist. And you?"
    misa "Umeji Misa, student."
    kuroki "Hmmm... I see..."
    misa "What do you see?"
    kuroki "You have an interesting path ahead of you. Your talents won't be enough, though they will be vital."
    misa "{i}What is this, fortune-telling?{/i}"
    kuroki "Forgive an old man his eccentricities. Oh, this looks like my destination! It has been a pleasure to meet you, even if our meeting has been short."
    n "The driver let him out by a police box, and then turned around and continued in the other direction."
    "Taxi driver" "{i}all these layabouts expecting me to go out of my way at least i'm getting paid for it who is this guy anyway paying all the guys to drive all the way out to yomiyama even takashi his wife doesn't even know about all the drinking even though i'm sure she suspects and this geezer who does he think he is talking all fancy in my car anyway he didn't impress such a pretty girl all drenched in her uniform but maybe it's a slip no stockings and panties with a hole in the crotch{/i}"
    misa "How much longer?"
    "Taxi driver" "Only a few minutes. Oh look, it's clearing up, just in time."
    n "The rain began to let up, and by the time it finally stopped there were only a few drops here and there."
    "Taxi driver" "You'll have to walk the rest of the way up to the house. This path is not accessible to cars."
    misa "Thank you."
    n "She got out of the car and grabbed her bag."
    scene moonlit house path entrance
    n "Even though it was night, the moon was bright enough in the now-clear sky that she didn't need to pull out her phone for illumination."
    scene moonlit house path
    n "Nevertheless, thick fog gathered around her heels, and the chill made her wish she had worn leggings."
    scene moonlit house
    n "The building rose out of the fog, in the center of a clearing surrounded by trees. It was old, and western-style, but clearly well-maintained: the elaborate stonework had no grime, let alone moss. Someone must have been hired to clean all the crevices in the past few weeks, probably as part of opening it up as a dormitory."
    scene moonlit door
    n "Misa knocked on the ornate door, but no answer came."
    menu:
        "Try the knob.":
            $ pass
        "Wait.":
            $ pass
    misa "{i}Who is that?{/i}"
    $ name = renpy.input("Name: ")
    misa "{i}Who the fuck is ${name}?!{/i}"
    extend "{i} ...wait. You can hear me?{/i}"
    extend "{i} Are you another telepath? Where are you?{/i}"
    n "The door opened."
    scene nave evening
    show akane at right
    "Strange girl" "Hi, are you another guest?"
    show misa at left
    misa "Yes. Are you..."
    "Strange girl" "My name is Akane. I'm also staying here. Pleased to meet you."
    misa "Ak--- That's an unusual surname. I'll bet you get a lot of people thinking it's your given name."
    akane "It is!"
    misa "But we just met..."
    akane "I go by only one name. Like Gackt."
    misa "O-- Oh..."
    misa "I'm Umeji Misa. Pleased to meet you."
    akane "Umeji-san, huh?"
    misa "I wonder... Is my sister here yet? Umeji Miko. We're both staying here."
    akane "Sorry to say, you're the second to arrive."
    misa "Then even the Master---"
    akane "Yup! I got here yesterday, and so special arrangements were made for me, but until Yuuko gets here nobody else can even move into their rooms."
    misa "Yuuko?"
    akane "She and I went to school together, back in Shibuya. She's acting as the house mother, so she's got all the room keys."
    misa "I suppose the Master shouldn't be bothered with such a task..."
    akane "Apparently he has the whole second floor to himself, which means that those two staircases are his too."
    akane "Here, why don't you come to my room until Yuuko shows? She's probably delayed by the storm."
    misa "This is an awfully oddly laid-out building. Where are the rooms?"
    scene house map
    akane "Apparently it's laid out like a church, or a cathedral, or something. Those doors to the left and right there lead to short hallways that lead to longer hallways against the left and right side of the building."
    akane "The rooms are off those long hallways."
    akane "Mine is on the left hand side, the first door on the left: room 3."
    scene hall short night
    akane "The electric system here is old-fashioned, so you'll have to get an adapter if you want to charge your phone."
    scene hall long night
    misa "Really? I would have thought they'd update it when they were doing the other maintenance."
    scene akane bedroom
    akane "Here we are, home sweet home."
    misa "Wow, a horror fan, huh?"
    akane "My father introduced me to it. He's really into giallo."
    misa "It's not very light-and-and-make-light, is it?"
    akane "Can you keep a secret?"
    misa "Of course."
    akane "I don't really believe in that stuff."
    akane "The Master has been good to my mother, and she's very dedicated to him because of that. But I'm skeptical."
    misa "I'm the same way. My mother grew up in the town where he was first contacted, and she's been following him for a long time."
    akane "Your mother is french?"
    misa "Hence the hair. My father was -- is -- outside the fold. That's where my japanese blood comes from."
    akane "My mother is the japanese one."
    misa "Oh..."
    akane "My surname... Actually, it's Bruno. You understand why I don't..."
    misa "Of course. Sometimes it's hard to be halfu."
    akane "My father is italian, so it's a little bit easier for me to pass, so long as people don't know my surname."
    misa "I understand."
    misa "Hey, I met this old guy on the way over and he said something strange to me."
    misa "He said I \"have an interesting path ahead of me\", and that my \"talents\" won't be enough."
    akane "What talents?"
    misa "{i}I guess she's not the one who was in my head...{/i}"
    misa "My sunny personality, I guess."
    akane "Are you interested in fortune telling and stuff?"
    n "She pulled out a deck of cards."
    akane "I could read your cards for you!"
    misa "Sounds fun."
    akane "But first you must cross my hand with silverrrrr~"
    extend "  kidding! You have to cut the deck though. With your left hand."
    n "Misa cut the deck."
    akane "Here we go."
    n "Akane put cards down one after another on the comforter between them, making a sort of pattern."
    scene tarot
