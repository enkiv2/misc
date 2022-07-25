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

init -2 python:
    class generateCalendar:
        header="Su Mo Tu We Th Fr Sa"
        monthStarts=[5, 0, 3]
        monthNames=["March", "April", "May"]
        monthLengths=[31, 30, 31]
        def isDay(self, idx, d, current):
            conv=0
            if idx:
                for i in range(0, idx):
                    conv+=self.monthLengths[i]
            return (conv+d)==(current+15)
        def printMonth(self, idx, current):
            ret=[self.monthNames[idx]+" 2012", self.header]
            line=[]
            d=0
            if self.monthStarts[idx]:
                for i in range(0, self.monthStarts[idx]-1):
                    line.append("  ")
                while d<=(7-self.monthStarts[idx]):
                    d+=1
                    line.append(str(d).rjust(2))
                    if self.isDay(idx, d, current):
                        line[-1]="{b}"+line[-1]+"{/b}"
                    if (idx==0 and d>=15) or (idx==1) or (idx==2 and d==1):
                        line[-1]="{a=jump:"+(self.monthNames[idx].lower())+str(d)+"}{font=fonts/JackInput.TTF}"+line[-1]+"{/font}{/a}"
                ret.append(" ".join(line))
                line=[]
            while d<self.monthLengths[idx]:
                for i in range(0, 7):
                    d+=1
                    if d>=self.monthLengths[idx]:
                        line.append("  ")
                    else:
                        line.append(str(d).rjust(2))
                        if self.isDay(idx, d, current):
                            line[-1]="{b}"+line[-1]+"{/b}"
                        if (idx==0 and d>=15) or (idx==1) or (idx==2 and d==1):
                            line[-1]="{a=jump:"+(self.monthNames[idx].lower())+str(d)+"}{font=fonts/JackInput.TTF}"+line[-1]+"{/font}{/a}"
                ret.append(" ".join(line))
                line=[]
            return "\n".join(ret)
        def __call__(self):
            global day
            return "\n\n".join([self.printMonth(i, day) for i in range(0, len(self.monthNames))])

        def __str__(self):
            return self.call()

screen calendar:
    tag menu
    use game_menu(_("Calendar"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label _("Calendar:")
            label ("{font=fonts/JackInput.TTF}"+generateCalendar()()+"{/font}")

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

label badEnd:
    call staticOut
    "I'm sorry, [name]. Umeji Misato has died, and your connection to her was severed."
    "It is still possible to restart the cyranoid daemon and connect to an earlier time point."
    $ achievement.grant("Bad end")
    if trust_akane < 25  and  trust_hanabi < 25 and trust_yuuko < 25 and trust_miko < 25 and trust_mina < 25 and trust_hikari < 25 and trust_akiko < 25:
        $ achievement.grant("Your garden has been sown with asphodel.")
    $ achievement.sync()
    $ renpy.quit(relaunch=True)
    return

label start:
    call OP
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
