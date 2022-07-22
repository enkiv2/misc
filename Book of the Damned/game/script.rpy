#      March 2012       
# Su Mo Tu We Th Fr Sa  
#              1  2  3  
#  4  5  6  7  8  9 10  
# 11 12 13 14 15 16 17  
# 18 19 20 21 22 23 24  
# 25 26 27 28 29 30 31  
#                       
#      April 2012       
# Su Mo Tu We Th Fr Sa  
#  1  2  3  4  5  6  7  
#  8  9 10 11 12 13 14  
# 15 16 17 18 19 20 21  
# 22 23 24 25 26 27 28  
# 29 30                 
                      
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

label phone:
    play sound "sfx/175039__makofox__phone-vibrate.mp3"
    pause
    show cellphone
    stop sound
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
    call march15
    return

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
    if not persistent.skip_NSFW:
        "As though drawn into those dark pools, Misato leans in to return the kiss, tangling her fingers in the brown locks. They tumble onto the bed."
        "Misato found herself straddling Akane's knee, and ground herself into it. Their mouths reconnected, tongues meeting, before exploring ears, necks, nipples."
        "As they stroked each other, skin flushed first pink, then, eventually, scarlet. Long fingers explored warm, wet grottoes."
        "The steady beat of the surf, indistinguishable in their ears from heartbeat or breath, beat both their brains in time."
        "Soon, a hot pleasurable itch began in Misato's crotch -- or was it Akane's? It was hard to tell anymore. They were no longer so distinguishable."
        "In their desire they became a single organism: four caressing arms, twenty exploratory fingers, four hungry lips, two questing tongues."
        "But one buzzing intoxicated brain, "
        " one ocean of fluids,"
        " and one single throbbing clit shared between them --"
        " -- the waves crashing against it quickly reaching high tide and breaking,"
        " leaving them shipwrecked,"
        extend " wet,"
        extend " naked,"
        extend " gasping on the shore,"
        extend " holding hands."
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

