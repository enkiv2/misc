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
    def randomByPref(weightDict):
        keys=list(weightDict.keys())
        ax=[]
        ax2=0
        for k in keys:
            ax2+=weightDict[k]
            ax.append(ax2)
        sel=random.randint(0, ax2)
        for i in range(0, len(ax)):
            if sel<=ax[i]:
                return keys[i]

    def prefMenu(itemDict, best=None, worst=None, trustIncrement=5, keys=None):
        """
            itemDict should be a dictionary of the form:
                {
                    "label": ["human-readable description", weight],
                }
        """
        global trust_player
        weightDict={}
        menuPairs=[]
        if not keys:
            keys=list(itemDict.keys())
        for k in keys:
            menuPairs.append([itemDict[k][0].capitalize(), k])
            weightDict[k]=itemDict[k][1]
        sel2=randomByPref(weightDict)
        if debugMode:
            comment("Misato's selection: "+sel2)
            misato("I want to "+itemDict[sel2][0])
        sel=renpy.display_menu(menuPairs)
        if debugMode:
            comment("Player's selection: "+sel)
        if random.randint(0, trust_player) <= 50 and not persistent.override_judgement:
            if sel!=sel2:
                renpy.say(misato, "{i}I'm not going to do that. Instead, I will "+itemDict[sel2][0]+".{/i}")
                if sel==worst:
                    trust_player-=trustIncrement
                    trust_player=max(trust_player, 0)
                elif sel2==worst:
                    trust_player+=trustIncrement
                elif sel==best:
                    trust_player+=trustIncrement
            else:
                renpy.say(misato, "{i}That's exactly what I was thinking...{/i}")
                trust_player+=1
                if sel==worst:
                    trust_player-=trust_increment
                    trust_player=max(trust_player, 0)
                elif sel==best:
                    trust_player+=trustIncrement
            sel=sel2
        else:
            renpy.say(misato, "{i}OK, I trust you on this one.{/i}")
        renpy.call(sel)

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

label doNothing:
    $ pass
    return
label doNothing2:
    $ pass
    return
label snark:
    misato "{i}Very funny...{/i}"
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
