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
        "loneliness":[
            "I like the darkness. It's friendly.",
            "Persephone's grey garland's roots are edible, but not nourishing. It is a food for ghosts.",
            "I have to watch her when she's in the room. I have to touch her when she's near.",
            "The snow is dead, grasping.",
            "Marriage? Marriage is how girls get eaten.",
            "This head is getting crowded, but there's room for one more.",
            "The company says the line was cut. They found it dragging, at a crossroads.",
            "It's the only time she can wear her wedding gown.",
            "You may think of me as a clingy sort of woman, but I was always waiting for your call.",
            "Comb me smooth, stroke my head, and thou shalt have my cockle-bread."
        ],
        "akane":[
            "Ah, I've been expecting you. The french girl. I knew you'd come.",
            "He speaks only romanian. I'm very attached to him.",
            "I once read that names that start with the letter 'A' are the names of asps.",
            "It all seems so absurd... So fantastic.",
            "Steak? No. No steak.",
            "Radiation, yes indeed.",
            "Hey mister, do you know 'Rock 'n Roll'?",
            "I've had fifty-six lovers and haven't killed even one of them.",
            "Can't you tell I'm alive?",
            "A pretty girl is never ridiculous.",
            "I'm not a man of thought.",
            "It's all so absurd, meaningless. And what's absurd is dangerous.",
            "My God! I've almost revealed a secret!",
            "You're not supposed to eat the fuzz.",
            "We sit in the sun and wait... sleep... dream...",
            "They're peering around buildings at night.",
            "These are the dead that killed them."
        ],
        "hanabi":[
            "Flames bloom on the sides of my face.",
            "The game is a foot. The weapon is an arm.",
            "In the drawing room, with a pen.",
            "Whatsoever is impossible, is curtains.",
            "A two pipe problem...",
            "Only one boot...",
            "Do you imagine that I can influence the powers of darkness?",
            "The depth a human being can sink to!",
            "I never guess.",
            "You enjoy Shakespeare and possess a sense of honor.",
            "You think that everything is always something else.",
            "It is hard to find, I grant you, but it is here.",
            "There are no masses in Dodge City.",
            "You're being presumptuous. Good night.",
            "I've never found her so.",
            "Look at this: an urgent appeal to find some missing midgets.",
            "How can you say it's a figment of my imagination when for years you've been saying I have no imagination whatsoever?",
            "Some of us are cursed with memories like flypaper.",
            "He had been everywhere, and done everything -- except to earn an honest livelihood.",
            "Why, you'll be suspecting myself next!",
            "There I found anchor.",
            "A glib lie always ready on the tip of her tongue for every emergency.",
            "Next day she missed it and jumped at conclusions.",
            "Your suspicions, I suppose, centre upon the servants?",
            "It was, I suppose, the weak point of the house?",
            "I suppose the key was frequently left in the possession?",
            "A singular discovery.",
            "They were wont, so to snarl.",
            "What is my thought like?",
            "Bates felt encouraged to proceed.",
            "Who is this coming along in this buggy at such a good pace?"
        ],
        "yuuko":[
            "She tried to go, but her feet are missing.",
            "The moon, once wan, is now rugose.",
            "Too large for a dismissal. And there is a moon.",
            "There's an owl caught in the engine.",
            "He had powers beyond the world of men.",
            "The corpse collectors always come when someone is doomed to meet his fate.",
            "The outbreak will make a tremendous occasion of Thursday night.",
            "One can always find mice -- or cats -- or monkeys.",
            "Such animals are things of the past, caro amico.",
            "What wonders could one not work in time?",
            "The vaporous soul is so much lighter.",
            "I was the venturesome one, to be abroad in moonlight.",
            "My life had been like a placid scream.",
            "The bright colours of autumn leaves strangely.",
            "I felt that this was romance.",
            "Will you ride tonight, Lemora?",
            "Drive continued through the flying hours.",
            "I knew they were true books and stories, now.",
            "My fancies have always, I'm afraid, been a little grim.",
            "They're safer in lockers, you know!",
            "I needed a corpse, and here.",
            "I waited for an unfamiliar footstep, which seemed to slide.",
            "Sick terrors of a hospital night!",
            "Doctors of horrible and fantastic crime...",
            "I leaned back in the night -- the stars -- the sea.",
            "Dr. Everywhere",
            "Palingenesis, didn't you?",
            "I threw aside shepherd pipes in my garden.",
            "Glad to be shut of it.",
            "The third girl was really of no account.",
            "Bodiless -- Inexplicable",
            "She felt him moving about in there.",
            "Repugnance, and antiquarian enthusiasm.",
            "Salutation, to all unbeliefs.",
            "'Familiar' would not, presumably, be ill, indisposed.",
            "Everything but the sea. The sea's invisible.",
            "I suppose you're sure there's nowhere else?",
            "Like the snake on the stairs, nowhere to repeat itself.",
            "It's the nearest, as Elizabeth cycles."
        ],
        "miko":[
            "She comes to my window, to tell me the news of the forest.",
            "Hot-stepping asphalt and electricity.",
            "We have trained him wrong on purpose, as a joke.",
            "I'm sorry, my sweet.",
            "Where is my skin?",
            "I will only say this once: we are not sick men.",
            "Teacher...",
            "I feel dizzy, too dizzy!",
            "You come right out of a comic book.",
            "Boards don't hit back.",
            "You got a lot of guts, Oscar.",
            "Rogan's kung fu is unorthodox.",
            "You'll die mutilated today!",
            "You, who would soon rule the world, allow a ghost to frighten you.",
            "You humans! Never will I comprehend you.",
            "If arrows cannot open a gate, then a corpse will."
        ],
        "mina":[
            "I would think for you, but this scar marks me as unclean.",
            "Are you coming? Everybody's coming...",
            "He kept calling me Lucy. Can you believe that?",
            "The flair says they're NPOV.",
            "What mighty contests rise from trivial things.",
            "Upon coming across a discussion that is borderline lame, thrust.",
            "I might inadvertently become useful.",
            "Was Chopin French?",
            "Is it a name or just a system?"
        ],
        "hikari":[
            "What about ant rights? What about plant rights?",
            "Can you turn it off? It's hurting my eyes.",
            "Miss? We're needed.",
            "Too many christmas trees...",
            "Champagne... champagne...",
            "I have to condemn you.",
            "There's a sting in my tail.",
            "A fallen horse near Piccadilly caused a terrible congestion.",
            "Virtue, it seems, has been rewarded."
        ],
        "akiko":[
            "Is this going to be the story of the little girl, who lived down the lane?",
            "Your sister knows, or what's in her...",
            "I slipped... I think this is going to stain.",
            "The tea is bitter like medicine.",
            "Light, and water...",
            "The acre where the waves meet the shore..."
        ],
        "player":[
            "Naturally, I have always depended upon the kindness of strangers.",
            "People from other worlds have minds that are unknowable.",
            "There is now a mockery of the moon.",
            "It's a kind of influencing machine, like an air loom."
        ],
        "kuroki":[
            "He was saying, make a rhizome with a minority literature.",
            "There are piles of dictionaries.",
            "Quandum ubique, quandum semper, quandum ad omnibus creditur est.",
            "Belief is the enemy.",
            "If the control system is to be subverted, one must first become indiscernible.",
            "He's just trying to warn you about {k=2}the bridge{/k}.",
            "The basis of reality is fairy tales.",
            "Beneath your feet, they remember lemuria.",
            "Garbage time is running.",
            "We come from anywhere.",
            "It cannot be intelligent, because it does not attack us."
        ],
        "cats":[
            "You can fool anybody, but you can't fool a cat. They seem to know who's not right.",
            "She never lied to us, my sister.",
            "Are you riding with me?",
            "We have an agreement, you know. I scratch their backs. They don't scratch mine.",
            "Any cat can open a door, but only a witch cat can close one.",
            "Bright eyes. Bright eyes, sharp little teeth.",
            "Don't you know? Mice live underground, like worms, in tunnels.",
            "No. I was thinking of an animal.",
            "Oh! A furry little man. What are you doing out here?"
        ],
        "aoi":[
            "A pale flower...",
            "She reproduces through budding.",
            "She reproduces through burning.",
            "They are suspended by the long bones, but it doesn't last. Then they don't have any insides."
        ],
        "mimi":[
            "The ears have walls..."
        ],
        "shironeko":[
            "Whatever happened to poor old George oblique stroke XR40?"
        ]
    }
    def dreamStatementLookup(about):
        return renpy.random.choice(dreamStatements[about])

define selectedCharacter = ""
define about = ""
label generalDream:
    call dreamIn
    $ selectedCharacter = randomByPref({"Big Girl":(100-min(100, ((trust_akane + trust_hanabi + trust_yuuko + trust_miko + trust_mina + trust_hikari + trust_akiko) / 7))), "Little Man":(100-min(100, (trust_player+trust_kuroki)/2)), "Black Deer":(100-min(100, (cat_affinity+trust_player)/2)), "Guardian of the Dream":(100-min(100, cat_affinity)), "Hermes":(100-min(100, (trust_mimi+trust_shironeko)/2))})
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
        $ about = randomByPref({"player":(100-min(trust_player, 100)), "kuroki":(100-min(trust_kuroki, 100)), "aoi":(100-min(trust_aoi, 100)), "cats":(100-min(cat_affinity, 100))})
    if selectedCharacter == "Black Deer":
        scene black deer
        with dissolve
        pause 1
        $ about = randomByPref({"player":(100-min(trust_player, 100)), "cats":(110-min(cat_affinity, 100)), "loneliness":25})
    if selectedCharacter == "Guardian of the Dream":
        scene guardian of the dream
        with dissolve
        pause 1
        $ about = randomByPref({"cats":(100-min(cat_affinity, 100)), "loneliness":25})
    if selectedCharacter == "Hermes":
        scene hermes
        with dissolve
        pause 1
        $ about = randomByPref({"mimi":(100-min(trust_mimi, 100)), "shironeko":(100-min(trust_shironeko, 100)), "loneliness":(100-min((trust_mimi+trust_shironeko)/2, 100))})
    $ renpy.say(selectedCharacter, dreamStatementLookup(about))
    call dreamOut
    return

# LATER DREAM
# BIG GIRL, a little girl whose flowery red dress takes up three quarters of the vertical height of the screen, appears.
# From under her dress, LITTLE MAN, a man in a David Byrne style 'big suit'. These are repeating dream characters who sometimes give advice.
# To warn of some bad ends, BIG GIRL's dress becomes a mountain of hair (like the angagonist of MAZE).
