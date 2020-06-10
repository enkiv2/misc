init python:
    from random import Random
    random=Random()
    def adjustLikelihoodByPreference(r, item, pref):
        pref=int(pref*r)
        if pref==0: return []
        elif pref>0: return [item]*pref
        else:
            ax=[]
            for i in range(0, r):
                if i!=item:
                    ax+=adjustLikelihoodByPreference(r, i, -1*pref)
            return ax
    def randomByPref(r, selected=-1, selPref=0, pref=[]):
        coll=[]
        if len(pref)==0:
            coll=range(0, r)
        else:
            if len(pref)<r:
                for i in range(len(pref)-1, r):
                    pref[i]=1
            for i in range(0, r):
                coll+=adjustLikelihoodByPreference(r, i, pref[i])
        if(selected>=0):
            if(selPref!=0):
                coll+=adjustLikelihoodByPreference(r, selected, selPref)
        return random.choice(coll)
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
    misato "Yes, bad luck, isn't it?"
    misato "{i}Worse, since I'm stuck with such a perv for a driver...{/i}"
    "Taxi driver" "{i}such a pretty young girl not so many fares are so pretty girls these days grow up so fast did i remember to shut that upstairs window it sure is pouring too bad she isn't wearing white soaked already no no she would need to beg first what's that van doing there sure is an old one he's wet{/i}"
    n "Misato looked out the window."
    scene kuroki van rain splash
    misato "Driver, pick up that man please."
    "Taxi driver" "Understood."
    scene taxi rain
    n "The driver pulled up to the broken-down van and idled the engine, rolling down his window."
    "Stranded man" "Any chance of helping out a poor traveler? I need a ride to the nearest police box."
    "Taxi driver" "That's up to my passenger."
    misato "Please join me."
    "Taxi driver" "It's a little out of our way, miss."
    misato "We're almost to our desination. The time, and the cost, must be a drop in the bucket compared to how far we've already come."
    "Taxi driver" "Of course. Very good."
    n "The drenched stranger slid into the seat beside Misato."
    misato "{i}Strange... I can't read him...{/i}"
    n "The man noticed her look, and smiled graciously."
    "Stranded man" "I am Kuroki. Fyodor Federov Kuroki: poet, linguist, and freelance combat etymologist. And you?"
    misato "Umeji Misato, student."
    kuroki "Hmmm... I see..."
    misato "What do you see?"
    kuroki "You have an interesting path ahead of you. Your talents won't be enough, though they will be vital."
    misato "{i}What is this, fortune-telling?{/i}"
    kuroki "Forgive an old man his eccentricities. Oh, this looks like my destination! It has been a pleasure to meet you, even if our meeting has been short."
    n "The driver let him out by a police box, and then turned around and continued in the other direction."
    "Taxi driver" "{i}all these layabouts expecting me to go out of my way at least i'm getting paid for it who is this guy anyway paying all the guys to drive all the way out to yomiyama even takashi his wife doesn't even know about all the drinking even though i'm sure she suspects and this geezer who does he think he is talking all fancy in my car anyway he didn't impress such a pretty girl all drenched in her uniform but maybe it's a slip no stockings and panties with a hole in the crotch{/i}"
    misato "How much longer?"
    "Taxi driver" "Only a few minutes. Oh look, it's clearing up, just in time."
    n "The rain began to let up, and by the time it finally stopped there were only a few drops here and there."
    "Taxi driver" "You'll have to walk the rest of the way up to the house. This path is not accessible to cars."
    misato "Thank you."
    n "She got out of the car and grabbed her bag."
    scene moonlit house path entrance
    n "Even though it was night, the moon was bright enough in the now-clear sky that she didn't need to pull out her phone for illumination."
    scene moonlit house path
    n "Nevertheless, thick fog gathered around her heels, and the chill made her wish she had worn leggings."
    scene moonlit house
    n "The building rose out of the fog, in the center of a clearing surrounded by trees. It was old, and western-style, but clearly well-maintained: the elaborate stonework had no grime, let alone moss. Someone must have been hired to clean all the crevices in the past few weeks, probably as part of opening it up as a dormitory."
    scene moonlit door
    n "Misato knocked on the ornate door, but no answer came."
    menu:
        "Try the knob.":
            $ pass
        "Wait.":
            $ pass
    misato "{i}Who is that?{/i}"
    $ name = renpy.input("Name: ")
    misato "{i}Who the fuck is ${name}?!{/i}"
    extend "{i} ...wait. You can hear me?{/i}"
    extend "{i} Are you another telepath? Where are you?{/i}"
    n "The door opened."
    scene nave evening
    show akane at right
    "Strange girl" "Hi, are you another guest?"
    show misato at left
    misato "Yes. Are you..."
    "Strange girl" "My name is Akane. I'm also staying here. Pleased to meet you."
    misato "Ak--- That's an unusual surname. I'll bet you get a lot of people thinking it's your given name."
    akane "It is!"
    misato "But we just met..."
    akane "I go by only one name. Like Gackt."
    misato "O-- Oh..."
    misato "I'm Umeji Misato. Pleased to meet you."
    akane "Umeji-san, huh?"
    misato "I wonder... Is my sister here yet? Umeji Miko. We're both staying here."
    akane "Sorry to say, you're the second to arrive."
    misato "Then even the Master---"
    akane "Yup! I got here yesterday, and so special arrangements were made for me, but until Yuuko gets here nobody else can even move into their rooms."
    misato "Yuuko?"
    akane "She and I went to school together, back in Shibuya. She's acting as the house mother, so she's got all the room keys."
    misato "I suppose the Master shouldn't be bothered with such a task..."
    akane "Apparently he has the whole second floor to himself, which means that those two staircases are his too."
    akane "Here, why don't you come to my room until Yuuko shows? She's probably delayed by the storm."
    misato "This is an awfully oddly laid-out building. Where are the rooms?"
    scene house map
    akane "Apparently it's laid out like a church, or a cathedral, or something. Those doors to the left and right there lead to short hallways that lead to longer hallways against the left and right side of the building."
    akane "The rooms are off those long hallways."
    akane "Mine is on the left hand side, the first door on the left: room 3."
    scene hall short night
    akane "The electric system here is old-fashioned, so you'll have to get an adapter if you want to charge your phone."
    scene hall long night
    misato "Really? I would have thought they'd update it when they were doing the other maintenance."
    scene akane bedroom
    akane "Here we are, home sweet home."
    misato "Wow, a horror fan, huh?"
    akane "My father introduced me to it. He's really into giallo."
    misato "It's not very light-and-make-light, is it?"
    akane "Can you keep a secret?"
    misato "Of course."
    akane "I don't really believe in that stuff."
    akane "The Master has been good to my mother, and she's very dedicated to him because of that. But I'm skeptical."
    misato "I'm the same way. My mother grew up in the town where he was first contacted, and she's been following him for a long time."
    akane "Your mother is french?"
    misato "Hence the hair. My father was -- is -- outside the fold. That's where my japanese blood comes from."
    akane "My mother is the japanese one."
    misato "Oh..."
    akane "My surname... Actually, it's Bruno. You understand why I don't..."
    misato "Of course. Sometimes it's hard to be halfu."
    akane "My father is italian, so it's a little bit easier for me to pass, so long as people don't know my surname."
    misato "I understand."
    misato "Hey, I met this old guy on the way over and he said something strange to me."
    misato "He said I \"have an interesting path ahead of me\", and that my \"talents\" won't be enough."
    akane "What talents?"
    misato "{i}I guess she's not the one who was in my head...{/i}"
    misato "My sunny personality, I guess."
    akane "Are you interested in fortune telling and stuff?"
    n "She pulled out a deck of cards."
    akane "I could read your cards for you!"
    misato "Sounds fun."
    akane "But first you must cross my hand with silverrrrr~"
    extend "  kidding! You have to cut the deck though. With your left hand."
    n "Misato cut the deck."
    akane "Here we go."
    n "Akane put cards down one after another on the comforter between them, making a sort of pattern."
    scene tarot
    comment "XXX tarot scene goes here: Akane reads spread, and Misato reads her mind about some of the meanings she is too polite to explain."
    scene akane bedroom
    play sound "sfx/txtmsg.wav"
    scene cellphone
    mina "Fun fact: the house you're staying in was built in 1939!"
    scene akane bedroom
    akane "Your sister?"
    misato "My other sister. She likes to send me trivia."
    akane "Oh yeah?"
    misato "Apparently this place was built in 1939."
    akane "It feels older than that..."
    comment "XXX they talk for a while & then eventually go to sleep. In the middle of the night, Misato wakes to the sound of banging outside the door. She reaches out for Akane, who is sleeping too heavily to wake. She reaches out with her mind, but can't sense a human consciousness outside the door. She talks to the player as a paniced distraction. Eventually the noise goes away, and she falls asleep. (Ref: Haunting of Hill House dog scene.)"
    comment "XXX Upon waking, Misato & Akane talk about the noise. Akane says (quote from Vampire Doll, re: old houses)."
    comment "XXX They hear noises elsewhere in the building, primed to be freaked out, grab ad-hoc weapons to check it out."
    comment "XXX It's Hanabi, Yuuko, and Hikari. Akane excitedly rushes Hanabi, hugging her, then introduces her. Hanabi introduces Yuuko and Hikari, who she met when their transportation stopped at the same inn for the night due to flooding."
    comment "XXX Akiko and Miko arrive, and Misato introduces Miko, while Miko introduces Akiko but does not explain how they met. Akiko doesn't talk much, causing awkwardness."
    comment "XXX The group talks about how Corto isn't there yet. They start helping each other move in. Hanabi has keys to various rooms, & distributes them. They work together to make a big meal, using a hot plate in a closet and some cans, and eat it while sitting on the floor in the nave."
    comment "XXX Misato sleeps alone, and again, there's a banging in the hall. She asks the player for advice."
    comment "XXX If she decides to check, she discovers the black cat (Kuro) hunting at this point. She asks what to do, & if she plays with the cat she gets points toward cat affinity & towards affinity with Kuro."

# Monologue (maybe from Kuroki?)
# "Four years ago, the rest of the industrialized world caught up to Japan in our direct traffic with the true meaning of the end of history: the expectation of growth so permanent it becomes meaningless, except as a pressure on your shoulders, thumping thumping thumping as it asks to proclaim your belief in the unstated empty promise whose fulfillment is made impossible by the very logic that relies on it."

# Setting details (maybe from Mina?)
# The ring of mountains keeps the fog lingering within the bowl of Yomiyama proper, so whenever it rains, visibility remains low and brocken spectres are easily produced. This may have led to ideas about this valley being haunted or a favorite area of reality-warping Tengu.

# Opening animation:
# we see a UFO with a windowed onion-dome top spewing sparks across the night sky, toward a mountain that obscures the full moon.
# cut to a character image of KUROKI on the left leaning against a stack of books, followed by SAFFYRE and SEYTON back to back on the right, SEYTON grinning while SAFFYRE pouts
# cut to a bunch of yomiyama academy students walking down the street (seen from behind). Some of the students have haircuts that indicate they are the characters from MfoM. Superimposed on the right is MISATO who is also facing away from the camera but is initially looking to her left, and she turns in the direction the students are walking.
# MISATO fades away along with the students and the street, but it is replaced with a black and white tiled hall with pillar globes on left and right, an eye in a down-pointing triangle at the end
# the triangle lowers as both it & the hall cross-fade to the house in sunlight.
# all of the tenants appear one by one in front of the house, forming a happy group pose
# the tenants and house move down as the setting darkens. in the air above the house, giant cats eyes fade in, and then above that, CORTO holding out his hands like a puppet-master
# a book appears and opens, and "BOOK of the DAMNED" is written in it stroke by stroke in red
# underneath, "by Double Mojo" in rainbow
# "BOOK of the DAMNED" shines and then drips like blood.
# cut to tv static

# FIRST DREAM
# an image of the doorknob appears, and then a face fades in on it
# THE HERMIT appears in rider-waite style facing a human-sized box. he turns to the camera, becoming a crone
# the front of the box opens to reveal a dismembered corpse floating in some kind of fluid
# the corpse focuses its eyes and begins to speak: "without love you have nothing. your garden shall be sown with asphodel."
# in later dream, this sequence repeats but the corpse and the hermit both fade into MISATO's face.

# DREAM IF CAT AFFINITY LOW
# sillhouette: a conquerer on horseback, with a cat held aloft skewered on his sword (like the statue in Val Lewton's Cat People); he himself becomes skewered with numerous swords, sprouting from inside himself

# LATER DREAM
# a nordic-style alien removes his face to reveal he is a grey in a wig, then removes the grey face (a mask) to reveal an ape face, then removes that to reveal MISATO's face. he then says "you will see me two times."

# LATER DREAM
# BIG GIRL, a little girl whose flowery red dress takes up three quarters of the vertical height of the screen, appears. From under her dress, LITTLE MAN, a man in a David Byrne style 'big suit'. These are repeating dream characters who sometimes give advice.
# To warn of some bad ends, BIG GIRL's dress becomes a mountain of hair (like the angagonist of MAZE).

label drugged_scene:
# Misato is summoned to Corto's penthouse. She is offered tea, and drinks it, as he monologues at her. She wonders why she's here.
# She begins to hallucinate: her vision gets slightly fuzzy, she begins to see tiny figures marching along the edge of the teacup,  it morphs into a desert landscape, etc.
# If cat affinity is high enough, this transitions to a Louis Wain style of cats marching in, and Misato wakes up downstairs. She later discovers Corto has been mauled.
# Otherwise, there is a warped & delirious perception of Misato's violation and murder
# initially, with increasingly dark imagery:
# the desert landscape becomes a geometric garden (like Last Year At Marienbad), but the shrubs become wheels (fading into the final shot of Ken Russel's The Devils)
# then, fish and bubbles and a blur/haze overlay this: it is underwater
# after this, we get description --
# (extremely vague: shapes pressing on her, a warm feeling lapping at her neck as she feels like she's floating, followed by the game announcing her death).
# death is followed by tv static animation

label true_end:
# Following the clues & the cats, Misato opens up a small hole in the baseboard by her room just large enough to drop through.
# She finds the secret basement, wet floor. There is a half-sized door against the north wall. The throne is covered with a tattered shroud.
# The shroud moves, and a rat pops out, runs away, pulling off the shroud. The cats crouch and growl, staring at the throne of hair.
# It is a full-sized throne made out of braided human hair coming from three dessicated-but-not-quite-rotten human heads. The hair is damp and matted.
# The cats begin slinking around it in a circle, and start a low yowling.
# The throne spontaneously catches fire, and despire being stunned for a moment,
# Misato manages to crawl out of the basement just as the floor under her room & adjacent hallway collapses. She scrambles to various rooms, banging on doors, evacuating.
# They get out of the house just as it lights up and collapses. They sit around on the lawn all night in a state of shock, and then as the new day dawns (may 1st) the flames die.
# Out of the ashes come the cats, and the final cat is Kuro, carrying Corto's head in his mouth.

