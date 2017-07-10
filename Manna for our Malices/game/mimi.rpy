label follow_mimi:
    play music "music/Infocalypse_-_vapor_intrusion.mp3" fadeout 5 fadein 5
    ai "I need to use the john. I'll be right back."
    kuroneko "Too much information."
    aoi "Have fun~"
    scene bg hallway
    show mimi angry
    ai "Hey, sorry about Aoi. She can be a little overbearing sometimes."
    mimi "I don't need your pity just because I don't have a wonderful girlfriend to cook for me."
    ai "She's not--"
    extend " It's not like that."
    extend "\nI can't think of her that way."
    mimi "You should tell her that."
    ai "I--"
    extend " I really should."
    ai "At first I thought it was a bit. She's always been clingy and needy but it's gotten worse."
    ai "I went along with it initially but I don't know what she'd do if I broke it to her now."
    ai "It's fucked up, I know."
    mimi "It really is."
    ai "She was always clingy. I used to be a little more standoffish."
    ai "One time, when we were four, we were playing out on... you know that waist-high wall down the street from the school?"
    mimi "Yeah."
    ai "So, we were playing there, and we had the kind of stupid fight little kids have. I started walking away and she started following me."
    ai "And, I yelled at her, and she backed up and fell off the wall."
    ai "She hit her head. She was in the hospital for a while, and when she was released she was all confused."
    ai "After that, I was afraid to push her away."
    show mimi normal
    mimi "I'm sorry. I'm giving you a hard time without knowing the situation."
    ai "You couldn't know."
    mimi "I'm glad Tomoe-san has a friend like you. Even if you're leading her on a bit."
    ai "What do you think I should do?"
    mimi "If she needs a girlfriend, then --"
    mimi "... nevermind."
    ai "N--"
    ai "Yamada... You have a crush on Aoi, don't you?!"
    mimi "n- noooo"
    ai "You really do..."
    mimi "you won't tell will you"
    ai "Hey, I may swear like a sailor, but I'm not a fucking asshole."
    ai "Anyway, I fully support you here. If Aoi can be part of a sickeningly cute scene that doesn't involve me for once, that'll be a load off my shoulders."
    mimi "Thank you, Akagi-san!"
    ai "Hey, we just swapped secrets, didn't we? Call me Ai."
    mimi "That... is too much of a convenient name, isn't it."
    ai "For once, yeah, Yamada, it is."
    mimi "Call me Mimi."
    ai "Alright, Mimi."
    if knows_about_aoi_parents:
        if knows_about_kuroneko_books:
            jump trade_info_mimi_p
        if saw_milpsi_symbol:
            jump trade_info_mimi_p
        jump dont_trade_info_mimi
    else:
        jump dont_trade_info_mimi
label trade_info_mimi_p:
    n "Mimi has quite a lot in that book. Maybe I should see if she can tell me something."
    menu:
        "Nah, that would be a little manipulative.":
            jump dont_trade_info_mimi
        "Ask her about that symbol on the black van" if saw_milpsi_symbol:
            jump trade_info_mimi_milpsi_symbol
        "Ask her about that symbol on Kuroneko's notes" if knows_about_kuroneko_books:
            jump trade_info_mimi_kuroneko_books
label trade_info_mimi_milpsi_symbol:
    ai "Hey, Mimi. Do you happen to know what this symbol means?"
    "I drew an inverted triangle with a snake in it."
    mimi "That's, um..."
    mimi "I recognize the components without having to look them up. The snake swallowing its tail is an ouraboros -- an ancient symbol of the cycle of rebirth."
    mimi "A triangle with a circle in it pointing upward is usually a reference to the divine eye of providence -- a masonic symbol for god as engineer of the world."
    mimi "Having it point downward... is weird, since inverting it is indicating, like, ending the world. But maybe that has to do with the ouraboros. Like, ending the world in order to rebuild it."
    mimi "Where did you see this symbol?"
    ai "Um... on a truck?"
    mimi "I sure hope I never meet the owner of that truck..."
    mimi "Lemme just double check that I haven't seen this exact symbol before...."
    "Mimi flipped through her red book."
    mimi "Nope! The closest I have is an unofficial patch design for Project Stargate, which has both an ouroboros and the eye of providence."
    mimi "But in that, the ouraboros is around the earth, and the eye of providence is right-side up and looking at the earth."
    ai "What the fuck is Project Stargate? Some kind of fan film?"
    mimi "During the cold war, the CIA thought that the Russians were researching ESP. So, they started researching ESP themselves."
    mimi "Project Stargate was one of these projects. Specifically, remote viewing. The idea was that psychic spies could watch anything anywhere from the safety of a secure facility."
    mimi "They had some early luck but later it was attributed to bad experimental design. By the mid 90s, it was cancelled. It was declassified a couple years ago."
    ai "Weird. And they had a patch?"
    mimi "An unofficial one. Most military groups will make one, even if they aren't given one, because it's like a symbol they can all get behind and bond over."
    mimi "They get made even when it doesn't really make sense. For instance, undercover narcotics officers assigned to investigate party drugs in the FBI had one that had a disco-dancing skeleton at a laser light show."
    ai "No fucking way."
    mimi "That's not the weirdest one."
    ai "Do you have, like, a collection?"
    mimi "I saw a website that has pictures of all of them once."
    ai "You're going to have to link me to that website."
    "Mimi flipped through her notebook, then took a post-it note out of her pocket and wrote a URL on it."
    ai "Thanks!"
    mimi "No problem. Weird symbols are sort of my thing."
    ai "I noticed!"
    $ knows_about_stargate = True
    jump trade_info_mimi
label trade_info_mimi_kuroneko_books:
    ai "So, Mimi... I wonder if you can do me a favor."
    mimi "What kind of favor?"
    ai "Do you know what these symbols mean?"
    scene splash sigils
    "I take out a piece of paper and draw the symbols I saw on Kuroneko's books."
    "Mimi looks at the symbols I drew and then takes out her red notebook and flips through it."
    mimi "The one on the left with the six circles is the logo for the Order of the Seers of Sophia, or the O∴S∴S. That symbol with the three dots means they have, or claim to have, the \"mason word\"."
    mimi "They're a pseudo-masonic occult society along the same lines as the Order of the Golden Dawn. In fact, they claim that the leader of their society is the proper outer head of the Golden Dawn, and they also claim to be the true lineage of the Anthrosophical and Theosophical societies."
    mimi "Neither claim is taken seriously by scholars. Aside from an obsession with the early 20th century Russian composer Alexander Scriabin, the O∴S∴S has nothing to do with Anthrosophy."
    mimi "Instead, it seems to be some kind of cult created out of whole cloth by their founder, a former Soviet music student who currently goes by the name Father Nikolai."
    ai "The fuck is a pseudo-masonic?"
    mimi "Pseudo-masonic means something that appropriates elements of freemasonry. It's pretty common with western occult groups."
    mimi "Usually the elements they appropriate are things like graded initiation --"
    ai "Graded initiation?"
    mimi "Where members are given a rank and only told certain parts of the mythology when they go through a ritual associated with graduating to a new rank"
    ai "OK"
    mimi "-- and elaborate oaths of secrecy (often involving cutting out one's tongue or having one's heart cut into four pieces)."
    mimi "Claiming to have the mason word is another one."
    mimi "Scholars aren't sure there even ever was a mason word, and all the groups that have it disagree on what it was."
    mimi "But, it's basically a string of nonsense syllables, and claiming to have it means claiming to be part of the lineage of \"true masonry\", which typically involves claiming that the tradition goes back to ancient egypt or even to before the biblical flood."
    mimi "Of course, freemasonry is actually a lot younger than that, and appears to have started in the rennaisance."
    mimi "But, occult groups like to claim absurd lineages as a way of indicating the kinds of things that influenced their ideas, and a lot of members look at the lineage claims as a list of fandoms rather than a serious historical claim."
    ai "Ok. That's very informative. Why do you know this?"
    mimi "Well, we have an Anthrosophy lodge in our town. I figured that researching Anthrosophy and its offshoots might come in handy for a story..."
    mimi "You know, if that rag did any real journalism."
    mimi "As for the one on the right, it looks kind of familiar but I couldn't tell you."
    mimi "You should ask Kuroneko. She's into all that occult stuff."
    ai "She's into occult stuff?"
    mimi "Yeah! Didn't you know? I don't think she takes it too seriously, but she's always reading pretty obscure western grimoires under her desk during class."
    ai "She reads spellbooks during class?!"
    mimi "You didn't know? You sit right next to her!"
    ai "I don't usually stare at her crotch during class."
    mimi "Your loss, I guess!"
    scene bg hallway
    show mimi normal
    $ knows_about_oss = True
    jump trade_info_mimi
label trade_info_mimi:
    if knows_about_missing_lab_notebook is False:
        ai "So, in exchange for that information, I'm going to tell you something interesting about Aoi."
        mimi "Oh yeah?"
        ai "Yeah. This is something she never even told me."
        mimi "Is it some kind of secret? I'm curious, but you shouldn't be telling me Tomoe-san's secrets."
        ai "It's not anything embarassing."
        ai "Actually, I'm not really sure why she hasn't bragged about it."
        ai "Apparently, her parents won the Z-Prize back in 199X."
        mimi "The... um..."
        "Mimi opened up her red notebook and flipped through it."
        mimi "I knew that didn't sound right..."
        mimi "The thing is, the Z-Prize didn't happen in 199X. The ceremony was cancelled."
        "She read off something from her notebook."
        mimi "\"Despite the protests and the loss of their usual venue, the organizers pushed ahead. However, they were stopped in their tracks by a bomb threat which cleared out the hotel.\" No prizes were given that year, because of protests over human germline research."
        mimi "Where did you get this information?"
        ai "I found a notebook in the science club room. It had a photo of them recieving the prize."
        ai "It's probably still there -- nobody really goes in there."
        n "Or rather, it's probably already there..."
        mimi "You've piqued my interest. A coverup would be a huge scoop."
        scene bg science room
        ai "It was on the top of that pile of books on the chair..."
        "I looked through the stack."
        ai "It's not here! I wonder what happened to it."
        mimi "Well... If you find it, let me know, I guess? I mean, it'd be a big scoop if there was evidence."
        n "If the book was here later today... will be here later today... and it's not here now, that means somebody brought it here... will bring it here... later on."
        n "I had assumed that the notebook had been here for years, because it was so old. But if somebody's moving around this evidence..."
        ai "If I find it, I'll let you know."
        $ knows_about_missing_lab_notebook = True
label dont_trade_info_mimi:
    ai "Well, I should get back to the classroom. Aoi's going to get suspicious."
    mimi "Thank you for keeping her happy."
    ai "Make sure to eat the hell out of your lunch too!"
    mimi "Will do!"
    play music "music/Infocalypse_-_scathing_frolic.mp3" fadeout 2 fadein 2
    scene bg classroom
    ai "I just spoke to the UN human rights inspector; they're about to declare that bathroom unsafe for habitation."
    show aoi at right
    aoi "Huh?"
    ai "I took a big shit, is what I'm saying."
    show kuroneko at left
    kuroneko "Your crudeness sometimes borders on endearing, but I think you're starting to overdo it."
    ai "What? All I'm saying is that I've completely evacuated my digestive track of rotting vegetable matter."
    jump dont_follow_mimi
