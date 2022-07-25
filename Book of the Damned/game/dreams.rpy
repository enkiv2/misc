label dreamIn:
    window hide
    stop music fadeout 1.0
    scene dream
    with fade
    play music "music/Infocalypse_-_The_Heads_Sprang_Up__Featuring_The_Dixie_Flatline_.mp3" volume 0.23 fadein 2.0
    return
label dreamOut:
    window hide
    stop music fadeout 1.0
    scene black
    with dissolve
    $ checkAchievements()
    return

label dream1:
    call dreamIn
    # FIRST DREAM
    # an image of the doorknob appears, and then a face fades in on it
    scene doorknob
    with dissolve
    pause 1
    scene doorknob face
    with dissolve
    pause 1
    # THE HERMIT appears in rider-waite style facing a human-sized box. he turns to the camera, becoming a crone
    scene hermit
    with fade
    pause 1
    scene hermit turn
    with dissolve
    pause 1
    scene hermit crone
    with dissolve
    pause 1
    # the front of the box opens to reveal a dismembered corpse floating in some kind of fluid
    scene hermitbox opened
    with dissolve
    pause 1
    # the corpse focuses its eyes and begins to speak: "without love you have nothing. your garden shall be sown with asphodel."
    "Floating corpse" "Without love you have nothing. Your garden shall be sown with asphodel."
    # in later dream, this sequence repeats but the corpse and the hermit both fade into MISATO's face.
    call dreamOut
    return

label dream2:
    call dreamIn
    # FIRST DREAM
    # an image of the doorknob appears, and then a face fades in on it
    scene doorknob
    with dissolve
    pause 1
    scene doorknob face
    with dissolve
    pause 1
    # THE HERMIT appears in rider-waite style facing a human-sized box. he turns to the camera, becoming a crone
    scene hermit
    with fade
    pause 1
    scene hermit turn
    with dissolve
    pause 1
    scene hermit crone
    with dissolve
    pause 1
    # the front of the box opens to reveal a dismembered corpse floating in some kind of fluid
    scene hermitbox opened
    with dissolve
    pause 1
    # the corpse focuses its eyes and begins to speak: "without love you have nothing. your garden shall be sown with asphodel."
    "Floating corpse" "Without love you have nothing. Your garden shall be sown with asphodel."
    # in later dream, this sequence repeats but the corpse and the hermit both fade into MISATO's face.
    scene hermitbox misatoface
    with dissolve
    pause 1
    call dreamOut
    return

label cat_affinity_low_dream:
    call dreamIn
    # DREAM IF CAT AFFINITY LOW
    comment "sillhouette: a conquerer on horseback, with a cat held aloft skewered on his sword (like the statue in Val Lewton's Cat People);"
    comment "he himself becomes skewered with numerous swords, sprouting from inside himself"
    $ achievement.grant("A cat just walked over my grave.")
    call dreamOut
    return

label dream3:
    call dreamIn
    # a nordic-style alien removes his face to reveal he is a grey in a wig,
    scene nordic
    with dissolve
    pause 1
    scene nordic grey
    with dissolve
    pause 1
    # then removes the grey face (a mask) to reveal an ape face,
    scene nordic ape
    with dissolve
    pause 1
    # then removes that to reveal MISATO's face.
    scene nordic misato
    with dissolve
    pause 1
    "Space Brother" "If you do good, you will see me two times. If you do bad, you will see me three times."
    call dreamOut
    return

init python:
    dreamStatements={
        "loneliness":[],
        "akane":[],
        "hanabi":[],
        "yuuko":[],
        "miko":[],
        "mina":[],
        "hikari":[],
        "akiko":[],
        "player":[],
        "kuroki":[],
        "cats":[]
    }
    def dreamStatementLookup(about):
        return renpy.random.choice(dreamStatements[about])

define selectedCharacter = ""
define about = ""
label generalDream:
    call dreamIn
    $ selectedCharacter = randomByPref({"Big Girl":((trust_akane + trust_hanabi + trust_yuuko + trust_miko + trust_mina + trust_hikari + trust_akiko) / 7), "Little Man":(trust_player+trust_kuroki)/2, "Black Deer":(cat_affinity+trust_player)/2})
    if selectedCharacter == "Little Man" or selectedCharacter == "Big Girl":
        scene big girl
        with dissolve
        pause 1
        $ about = randomByPref({"akane":(100-min(trust_akane, 100)), "hanabi":(100-min(trust_hanabi, 100)), "yuuko":(100-min(trust_yuuko, 100)), "miko":(100-min(trust_miko, 100)), "hikari":(100-min(trust_hikari, 100)), "akiko":(100-min(trust_akiko, 100)), "loneliness":25})
        $ renpy.say("Big Girl", dreamStatementLookup(about))
        $ about = randomByPref({"akane":(100-min(trust_akane, 100)), "hanabi":(100-min(trust_hanabi, 100)), "yuuko":(100-min(trust_yuuko, 100)), "miko":(100-min(trust_miko, 100)), "hikari":(100-min(trust_hikari, 100)), "akiko":(100-min(trust_akiko, 100)), "loneliness":25})
        window hide
    if selectedCharacter == "Little Man":
        scene big girl door open
        with dissolve
        pause 1
        show little man
        pause 1
        $ about = randomByPref({"player":(100-min(trust_player, 100)), "kuroki":(100-min(trust_kuroki, 100)), "aoi":(100-min(trust_aoi, 100))})
    if selectedCharacter == "Black Deer":
        scene black deer
        with dissolve
        pause 1
        $ about = randomByPref({"player":(100-min(trust_player, 100)), "cats":(100-min(cat_affinity, 100)), "loneliness":25})
    $ renpy.say(selectedCharacter, dreamStatementLookup(about))
    call dreamOut
    return

# LATER DREAM
# BIG GIRL, a little girl whose flowery red dress takes up three quarters of the vertical height of the screen, appears.
# From under her dress, LITTLE MAN, a man in a David Byrne style 'big suit'. These are repeating dream characters who sometimes give advice.
# To warn of some bad ends, BIG GIRL's dress becomes a mountain of hair (like the angagonist of MAZE).
