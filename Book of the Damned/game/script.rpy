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






