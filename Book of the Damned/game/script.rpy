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

label static:
    play music "sfx/static.mp3"
    scene static1
    pause 0.1
    scene static2
    pause 0.1
    stop music
    return
label staticIn:
    call static
    scene static_in
    pause 0.1
    scene black
    pause 0.1
    scene white
    pause 0.1
    return
label staticOut:
    call static
    scene static_out
    pause 0.1
    scene black
    pause 0.1
    return

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
    call staticIn
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
    play sound "sfx/175039__makofox__phone-vibrate.wav"
    pause
    show cellphone
    stop sound
    mina_phone "Fun fact: the house you're staying in was built in 1939!"
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



label misato_and_akane_love_scene:
    akane "But how did you know?"
    misato "Can you keep a secret?"
    akane "Of course..."
    misato "The truth is, I'm a telepath."
    akane "Really?"
    "Akane looks excited"
    akane "Send something to my mind!"
    "Misato shakes her head"
    misato "I've never been able to send. I've only ever recieved."
    akane "Ok, then what am I thinking now?"
    akane "{i}I want to kiss you{/i}"
    misato "... I want to kiss you."
    "Akane leans in and kisses her deeply, then pulls back slightly, her eyes wide and gentle."
    "As though drawn into those dark pools, Misato leans in to return the kiss, tangling her fingers in the brown locks. They tumble onto the bed."
    "Misato found herself straddling Akane's knee, and ground herself into it. Their mouths reconnected, tongues meeting, before exploring ears, necks, nipples."
    "As they stroked each other, skin flushed first pink, then, eventually, scarlet. Long fingers explored warm, wet grottoes."
    "The steady beat of the surf, indistinguishable in their ears from heartbeat or breath, beat both their brains in time."
    "Soon, a hot pleasurable itch began in Misato's crotch -- or was it Akane's? It was hard to tell anymore. They were no longer so distinguishable."
    "In their desire they became a single organism: four caressing arms, twenty exploratory fingers, four hungry lips, two questing tongues."
    "But one buzzing intoxicated brain, one ocean of fluids, and one single throbbing clit shared between them -- the waves crashing against it quickly reaching high tide and breaking, leaving them shipwrecked, wet, naked, gasping on the shore, holding hands."
    akane "Wow..."
    "Akane struggled to catch her breath."
    akane "Is this what sex with a telepath is always like?"
    misato "I'm not sure... I'm good at knowing how to please people"
    akane "... I'll say."
    misato "But I think something else was going on there."
    akane "Are you sure you can't transmit?"
    misato "I never have... I think."
    akane "You should give it a try."
    "Misato took a moment to compose herself."
    akane "I mean, we should give it a try."
    misato "You know, you're the first one I've told."
    akane "Nobody else knows?"
    misato "My sister knows, I think."
    misato "She had... when we were younger, she was kitsuneki."
    akane "Possessed?"
    misato "Yeah. Like, actually possessed, by a fox spirit. Growing up in a home where we all believed in the teachings of Master Corto, I thought it was normal."
    misato "Not just the fox spirit, but telepathy too. I didn't know that kitsuneki was a euphemism for psychosis until that kid on the playground said so."
    misato "It was terrible for Miko, all the bullying. And I punched him out, to stand up for her. But it turned out, much of what I heard him say, nobody else heard."
    misato "That was when I realized that I was special too. Other people couldn't hear what people said when they 'closed their lips'."
    misato "I realized that if I told anybody, I'd be bullied too. So from then on--"
    akane "You used it to blend in."
    misato "To become invisible, indiscernible. To match people's expectations."
    akane "How'd it work out for you?"
    "Misato let out a single chuckle."
    misato "Not great. I was popular -- loved, even -- or at least something was. The distance between the face I put on for people and how I felt inside grew."
    akane "Kids can be terrible. Some adults, too. But all of us in this dorm are already weirdos. I feel like we all already know the real you, at least a little."


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
    "Corto rings the bell again and again, but to no avail."
    "Misato lets herself into his room, slipping the lock as she told Seyton to do."
    misato "They're gone, you know. They took your money."
    corto "{i}How does she know about the money? What the hell was that cat thing? Does she know about the book?{/i}"
    corto "Ahh, Umeji. Come, sit down. {i}How the hell did she get in anyway? Was the cat thing a fluke?{/i}"
    misato "I think not. We've decided that we're leaving."
    misato "All of us."
    corto "{i}Mouthy brat{/i} Umeji, I understand you have some contraband. A lighter, I believe?"
    "Misato says nothing."
    corto "And that furthermore, you girls have been engaging in... unnatural... activities."
    misato "I prefer to call them supernatural."
    corto "I know you want to be a good girl and be in the good graces of the space brothers, which can only happen with a pure soul. So p{i}--wait, what? Supernatural?{/i}"
    corto "...So please hand over the lighter and I will overlook your indiscretions with miss Bruno."
    misato "I'm keeping it. Goodbye, Master Corto."
    "Misato turns toward the door, but is brought short by the hook of Corto's cane on her shoulder."
    corto "You will stay. You're all going to stay. You have been put in my care, and I intend to take care of you."
    # flashes of bloody plastic wrap, a limply dangling arm
    misato "Like you took care of Akiko?"
    corto "{i}How much does she know?{/i}"
    misato "I know about the book."
    "Corto's gaze darts to a black book on his desk."
    corto "{i}She could ruin me.{/i}"
    misato "The cats were not a fluke. And everything I need to ruin you is right there in that book."
    corto "{i}Without that money, I can't even escape{/i}"
    misato "There's no escape for you now."
    "Corto grabs Misato's arms roughly, wrenches them behind her back, and quickly ties them behind her back with a scarf. He then gags her, and throws her into the closet."
    corto "I'm locking you in there for your own good!"
    "The closet door is jammed by his cane."
    corto "{i}Jesus christ jesus christ what do I do{/i}"
    "A scratching sound comes from the back of the closet, and Misato crawls closer to hear it. It is a cat, clawing at the back side of a heating vent."
    "Misato tries to turn around enough to get her fingers under the edge of the vent housing. She gets her fingernails under it and nearly loses one before it pops loose enough for the edgeof a finger to fit."
    "Scrambling, slicing her fingertips, she finally pulls it loose enough that the cat's weight is able to push it out. Corto doesn't seem to notice the noise, in his panic."
    "The cat is Kuro. He grabs onto the scarf's knot with his teeth and pulls back with all his might, and it comes loose. Then he mews once and hops back into the vent."
    "The closet door still jammed shut, Misato peers down into the murky depths of the chute, just big enough to fit into. She hears mewing down there."
    misato "{i}Cats only mew to talk to humans, so he must want me down there.{/i}"
    "The mewing became more insistent. She removed her gag and gingerly entered the chute --"
    "-- and promptly slid down two stories into wet muck."
    "She struggles to sit up, wipes off her hands the best she can, then rummages through her vest pockets for the lighter."
    "Click... Click... Click... Whoosh"
    "The flame illuminates a stone-walled room, shin-deep in dirty water. Towering over her, a form like a chair, covered with a tattered shroud."
    "The shroud moves. A rat escapes and runs away across the floating muck, and the Throne is revealed."
    "The Throne is made of hair. It is the hair of its late occupants, woven together as it was still growing from their heads. Their bodies, collapsed beneath vermillion robes, are still shackled at the wrists and ankles."
    "Cats begin slinking around it in a circle, yowling. There are more of them than she has ever seen together."
    "A plop, and then another. Fingerbones are plopping into the water. They float to the surface, in the shape of a skeletal hand, pointing at a spot on the far wall."
    "At that moment, the throne spontaneously blazes."
    "The light illuminates the whole room: the spot on the wall is a boarded up window."
    "Misato wades through the murk, the light dying as the hair is rapidly consumed by the flames. She pries the boards off with dirty, bleeding fingers."
    "Using the lighter again, she checks the space she's just opened up: an unused chimney flue, large enough to fit into, with brick protrusions at regular intervals."
    "She stumbles to get up into the hole, and drops the lighter. She's about to go down to get it, but she sees hundreds of pairs of cat eyes glowing in the dark. They begin to pur in unison."
    "She climbs slowly, crumbling brick against bleeding fingers and raw nail beds, scuffing soaked dress shoes and sending dull shocks through the bruised and blistered feet within."
    "Finally, she sees a light open up before her. The grate, in Corto's room."
    "She hops onto the platform of the unused fireplace, then kicks the grate open."
    "She stands there in front of him, muddy and covered in soot, bleeding finger pointing accusingly like a revenant. In his shock, he drops the black book, which he has just set on fire, onto the thick carpet."
    misato "Do you know why I know all this?"
    "Corto shakes his head timidly, unsure if she is alive or a ghost."
    misato "Because I am a telepath."
    "She runs past him and bursts through the door to nowhere, focusing her whole mind on the intent to transmit."
    misato "{i}THERE'S A FIRE! EVACUATE NOW!{/i}"
    "As she falls, she glimpses a lick of flame through the door she just exited through the corner of her eye, and hears a support collapse, then is overtaken by merciful darkness."
    "She awakes on grass, something soft beneath her head."
    akane "You're finally awake."
    misato "You escaped..."
    akane "You warned all of us in time."
    misato "What happened to--"
    "Akane gestured toward the now shockingly empty landscape -- the grass they lay on now surrounding a strangely barren area illuminated here and there by popping coals."
    "A bit of debris crumbled and fell into what must have been the hidden basement. A scrabbling of little paws, then a black shape popped out, holding something."
    "As the sun rose on the First of May, 2012, Kuro emerged from the remains of the vanished house carrying Corto's skull in his mouth. He put it down in front of Misato."
    "On top of the skull was a single gold coin."
    "In the distance, a honking."
    "Kuroki's van pulls up."
    kuroki "Sorry I missed the party. I saw some of the fireworks as I was passing by, though. Do you girls need a ride anywhere?"
    "There was a general agreement that, yes, the girls needed a ride -- back home, or to relatives, or to school friends."
    kuroki "What about you two?"
    "Akane and Misato had by this point gotten themselves vertical and were brushing the dirt and ash off their ruined clothes. They looked at each other."
    misato "I think we're going to stay here for a while, thanks."
    "Akane laced her fingers between Misato's gingerly."
    kuroki "Suit yourselves! Ok, everybody else, just move the banana crates wherever to make room--"
    hanabi "... Wait... why are there bananas..."
    call staticOut
    call credits
