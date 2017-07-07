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

define misa = Character("Umeji Misa", color="#77ff77")
# Misa: UFO cultist, appears to be pure / yamato nadeshiko type character
# Probably want to link UFO cult to both OSS & to the stuff Shironeko dug up
# I'm thinking the cult should be pseudo-Raelian

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
# The knows_about_missing_lab_notebook flag opens up several options:
# * one that makes us able to hide in the science club room's locker after school and verify that Aoi took the book
define knows_aoi_took_lab_notebook = False
$ achievement.register("In the closet")
# * one that makes us able to ask shironeko about the 199X Z-Prize (like trying to get the papers entered)
define read_z_prize_papers = False
$ achievement.register("Peer review")
# * one that lets us skip school at the very beginning of the game by climbing out the window to go investigate in person at Yomiyama Poly's research facility
# That last one branches out: we get killed by a guard having a smoke break behind a pole when we go straight into the employees-only area,
# which opens up a new option to hide behind a neighbouring pole until the guard leaves to do rounds.
define knows_poly_guard_position = False
# We then go up against a keypad lock.
define knows_about_keypad = False
# We inevitably get killed here but now that we know there's a keypad lock we can dare shironeko to get the combination (which will be randomly 
# generated and then stored in persistent storage, so that it's unique to the game copy but the same each time we ask her)
define keycode = False # this is defined in a python block in start
# Entering the code lets us enter the facility where we eventually find the clone racks. Aoi, who has followed us, kills us here.
define knows_about_clone_racks = False
# Following that death if we do the same operation we open up dialogue trees that will allow us to get Aoi's backstory & info about the clones.
# (But some of the info about the clones should be able to come from getting a copy of the paper from shironeko -- a proposal that probably has 
# fully disconnected cerebellums instead of hypoxic cerebellums. It will be hard to explain the technical details of the cloning in a way consistent
# with even yandere-mode Aoi.)

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
define knows_milpsi_shell_co_name = False

# Shironeko route
define knows_about_alien_tech = False
$ achievement.register("The truth is out there")

####################### BACKGROUND IMAGES
# Generic
image bg white = "white.png"
image bg black = "black.png"
# Shared
image bg street = "street.png"
image bg street dark = "street night.png"
image bg classroom = "classroom.png"
image bg classroom dark = "classroom night.png"
image bg hallway = "hallway.png"
image bg hallway dark = "hallway dark.png"
# Ai route
image bg morning = "morning.png"
image bg downstairs = "downstairs.png"
# Kuroneko route
image bg music room = "musicroom.png"
# Aoi route
image bg science room = "science room.png"
# Koneko route
image bg track = "track.png"
image bg nurse office = "nurse office.png"
image bg nurse office dark = "nurse office night.png"
image bg loading dock = "loadingdock.png"
image bg interrogation room = "interrogation room.png"
image bg milpsi parking lot = "milpsi parking lot.png"
image bg milpsi entrance = "milpsi entrance.png"
# Shironeko route
image bg fujinomiya household = "fujinomiya residence.png"
image bg shironeko bedroom = "shironeko bedroom.png"


####################### SPLASH IMAGES
# Ai route
image splash blood one = "blood 1.png"
image splash blood two = "blood 2.png"
# Kuroneko route
image splash kuroneko violin = "kuroneko violin musicroom splash.png"
image splash kuroneko fingering = "splash violin fingering.png"
image splash sigils = "sigil splash.png"
# Aoi route
image splash science room book = "science room book splash.png"
image splash trophy photo = "science room photo splash.png"
image splash science printout = "science room printout splash.png"
# Koneko route
image splash koneko pain = "splash koneko pain.png"
image splash koneko shocked pain = "splash koneko shocked pain.png"
image milpsi corridor = "milpsi corridor.png"
image milpsi corridor massacre = "milpsi corridor massacre.png"
image splash van = "van splash.png"



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

