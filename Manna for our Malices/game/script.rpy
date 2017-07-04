######################### CHARACTER DEFINITIONS

# The 'comment' character is for in-game reminders of TODO issues, during dev
# Remember to remove it before shipping to make sure we have the script completed!
define comment = Character("Comment")
define quote = nvl_narrator

# Ai has two character objects: 'n', used for internal monologue, and 'ai', 
# used for speech.
# NB: 'n' is used with extend + bold to represent 'current Ai', when arguing
# with 'ghost Ai'.
define n = Character("Akagi Ai", what_prefix="{i}", what_suffix="{/i}")
define ai = Character("Akagi Ai", color="#000000")

define aoi = Character("Tomoe Aoi", color="#0000af")
image aoi happy = "aoi.png"
image aoi hearteyes = "aoi hearteyes.png"
image aoi pout = "aoi akimbo.png"
image aoi blush = "aoi blush.png"
image aoi yandere = "aoi yandere.png"

define kuroneko = Character("Fujinomiya Kuroneko", color="#aa0000")
image kuroneko normal = "kuroneko.png"
image kuroneko pout = "kuroneko.png" # XXX
image kuroneko happy = "kuroneko smile.png"

define shironeko = Character("Fujinomiya Shironeko", color="#77aaaa")
image shironeko happy = "shironeko happy.png"
image shironeko normal = "shironeko.png"
image shironeko pout = "shironeko pout.png"
image shironeko surprised = "shironeko surprised.png"

define koneko = Character("Fujinomiya Koneko", color="#777700")
image koneko normal = "koneko.png"
image koneko happy = "koneko smile.png"
image koneko pout = "koneko pout.png"

define mimi = Character("Yamada Mimi", color="#ff7777")
image mimi normal = "mimi.png"
image mimi angry = "mimi angry.png"
image mimi pensive = "mimi pensive.png"
image mimi smug = "mimi smug.png"
image mimi scoop = "mimi scoop.png"

######################## STATUS FLAGS
# Ai route
define died = False
$ achievement.register("Stabbed in the back")
define num_deaths=0
$ achievement.register("Some chuunibyo BS") # >2 deaths
# Aoi route
define knows_about_aoi_parents = False
$ achievement.register("A mysterious photograph")
define knows_about_missing_lab_notebook = False
$ from random import Random
$ random = Random()
define keycode = False
# Kuroneko route
define knows_about_kuroneko_concert = False
$ achievement.register("Some Eyes-Wide-Shut MFers")
define knows_about_kuroneko_books = False
define knows_about_oss = False
# Koneko route
define knows_about_koneko_telepathy = False
$ achievement.register("Touch telepathy")
define saw_milpsi_symbol = False
define knows_about_stargate = False

####################### BACKGROUND IMAGES
image bg white = "white.png"
image bg black = "black.png"

image bg morning = "morning.png"
image bg downstairs = "downstairs.png"

image bg street = "street.png"
image bg street dark = "street night.png"
image bg classroom = "classroom.png"
image bg classroom dark = "classroom night.png"
image bg music room = "musicroom.png"
image bg hallway = "hallway.png"
image bg hallway dark = "hallway dark.png"
image bg science room = "science room.png"
image bg track = "track.png"
image bg fujinomiya household = "fujinomiya residence.png"
image bg shironeko bedroom = "shironeko bedroom.png"
image bg nurse office = "nurse office.png"
image bg nurse office dark = "nurse office night.png"
image bg loading dock = "loadingdock.png"
image bg interrogation room = "interrogation room.png"

####################### SPLASH IMAGES
image splash blood one = "blood 1.png"
image splash blood two = "blood 2.png"
image splash kuroneko violin = "kuroneko violin musicroom splash.png"
image splash kuroneko fingering = "splash violin fingering.png"
image splash science room book = "science room book splash.png"
image splash trophy photo = "science room photo splash.png"
image splash science printout = "science room printout splash.png"
image splash koneko pain = "splash koneko pain.png"
image splash koneko shocked pain = "splash koneko shocked pain.png"
image milpsi corridor = "milpsi corridor.png"
image milpsi corridor massacre = "milpsi corridor massacre.png"
image splash van = "van splash.png"
image splash sigils = "sigil splash.png"

###################### SCRIPT
# The game starts here.
label start:
    python:
        from random import Random
        random=Random()
        if not keycode:
            keycode="".join([str(random.choice(range(0, 10))),str(random.choice(range(0, 10))),str(random.choice(range(0, 10))),str(random.choice(range(0, 10)))]) 
    #quote "DEBUG: [keycode]"
    play music "music/Infocalypse_-_yesterday_the_shadows_grew_again.mp3"
    scene bg black
    centered "{color=#fff}{cps=10}\"The outrageous is the reasonable, if introduced politely.\"{/cps}{/color}"
    extend "{color=#fff}{cps=10}\n{space=500}- Charles Fort,{/cps}{/color}"
    extend "{color=#fff}{cps=10}\n{space=400}The Book of the Damned{/cps}{/color}"
    scene bg white with dissolve
    scene bg black with dissolve
    centered "{color=#fff}{cps=15}In the year 20XX, in the small town of Yomiyama, there was a series of deaths.{/cps}{/color}"
    extend "{color=#fff}{cps=15}\nInvestigations of these deaths have been unsuccessful.{/cps}{/color}"
    extend "{color=#fff}{cps=15}\nAs it turns out, a lot was happening just under the surface.{/cps}{/color}"
    jump core_story

