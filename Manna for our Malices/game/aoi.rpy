label return_box:
    "The box of glassware is heavier than it looks."
    n "No wonder nobody moved it before."
    menu:
        "Leave it for somebody else":
            jump ignore_box
        "Do it anyway":
            jump science_clubroom
label science_clubroom:
    scene bg hallway
    "As I walk down the hallway toward the science clubroom, I hear music from across the hall."
    play music "music/mystic chord practice.mp3"
    menu:
        "Ignore the music":
            jump ignore_music
        "Investigate":
            jump music_room
label ignore_music:
    n "The music club sure is hard-working."
    scene bg science room
    "I bring the box of glassware into the science clubroom and set it down on a table."
    "The dust is thick in here."
    "I wipe off my hands on my blouse and look around for a chair."
    n "I'm fucking beat..."
    "I find a small, uncomfortable-looking chair in the corner of the room, with a stack of books on it."
    n "This will do."
    "I try to move the books but my weary arms fumble, and one of them falls to the ground."
    n "Shit"
    "I put the rest of the stack down on top of the glassware and turn to pick up the dropped book. It has fallen open."
    scene splash science room book
    "A folded piece of paper is sticking out, as well a photograph."
    "The paper is yellowed and the photograph is on real photo stock, so it must have been taken before digital cameras."
    if knows_about_missing_lab_notebook:
        n "I should make sure Aoi isn't the one who took this."
        n "I mean, she had a weak excuse for showing up, and the notebook does have a connection to her family."
        scene bg science room
        "I stacked the books back up the way they were and looked for a hiding place. Luckily, at the back of the room there was a nearly empty locker."
        "I hid, and looking through the grate, I watched as Aoi came in, looked around, and picked up the lab notebook."
        n "Hmm..."
        n "If it's hers, why is she bringing evidence of a government coverup to school? If it's not hers, who brought it and why is she being sent to pick it up?"
        n "And why is she hanging out in the science club room after school?"
        n "After all, I was with her until the end of classes. If the notebook wasn't here at lunch then she can't have brought it until the end of the day."
        n "If it was she who brought it."
        $ knows_aoi_took_lab_notebook = True
        $ achievement.grant("In the closet")
        n "Anyhow, if the timeline's lining up then it's getting late and I should get home."
        scene bg hallway dark
        pause 1
        jump walk_home
    scene splash trophy photo
    "The photo is of two people in lab coats holding some kind of trophy."
    n "Isn't this..."
    play music "music/Infocalypse_-_Lull.mp3"
    extend " Aoi's parents?"
    "The back of the photo is labeled: \"Dr. Tomoe's group, 199x, Z-Prize\""
    n "I didn't realize they were such a big deal."
    "I looked at the paper."
    scene splash science printout
    "It was a bunch of pages of printout from an old dot-matrix printer, accordion-folded."
    "It had what looked like lab instructions, and some diagrams."
    "There were flow charts, drawing of molecules, and what looked like assembly diagrams for laboratory equipment."
    stop music
    "On the last page, there was a picture of what looked like a foetus in a tube."
    $ knows_about_aoi_parents = True
    "{b}CLACK{/b}"
    "I jumped and quickly fumbled the paper back into the book, closing it."
    scene bg science room
    "???" "Ai-chan?"
    "???"
    show aoi pout
    aoi "What are you doing here?"
    play music "music/Infocalypse_-_vapor_intrusion.mp3"
    ai "Aoi!"
    extend " I was on cleanup duty."
    aoi "Didn't you have clean up last w---"
    show aoi happy
    extend " Oh, right!"
    show aoi pout
    aoi "That teacher really has it out for you, Ai-chan~"
    show aoi happy
    ai "Don't I know it?"
    ai "What are you doing here?"
    show aoi pout
    pause 1
    show aoi happy
    aoi "I forgot something in class."
    n "But we didn't have lab science today..."
    n "I guess she means the bio homework she copied off me."
    ai "Well, I was just about to leave. Why don't you get it and then we can walk home together?"
    show aoi pout
    pause 1
    aoi "Sorry, Ai-chan. No can do."
    aoi "I forgot something else too, and it'll take me a while to find it."
    aoi "Why don't you go on ahead?"
    ai "Alright. I'll see you tomorrow?"
    show aoi hearteyes
    aoi "You betcha!"
    $ achievement.grant("A mysterious photograph")
    scene bg hallway dark
    with dissolve
    jump walk_home

label sneak_to_yomipoly:
    play music "music/Infocalypse_-_Logolo.mp3"
    "I threw on street clothes, rather than my usual uniform, and carefully climbed out the window so Aoi wouldn't see me."
    scene bg street
    "The facility was in the opposite direction from school, and if I made good time, I could be gone long before my mother -- or Aoi -- noticed."
    "After all, I've often slept in or been hard to rouse. It would take probably fifteen minutes before their suspicion was piqued."
    "After a little while I came upon the campus."
    scene bg yomi poly entrance
    n "Looks remarkably innocent... I guess all campuses do."
    "I had taken pains to pick out an outfit that would let me pass as a university student, but many of the students were dressed in their uniforms from high school, so I needn't have bothered."
    n "I guess they're trying to get the most out of them..."
    "I made my way to the lab building."
    scene bg yomi poly security desk
    "I was in luck. The security desk was deserted."
    if knows_poly_guard_position:
        n "It's not deserted. It only looks that way."
        n "{b}What do you mean?{/b}"
        n "Look carefully at that pillar."
        n "{b}Smoke?{/b}"
        n "The guard is behind there, sneaking a cig."
        n "He can't run for shit, but he's packing."
        n "{b}What should we do?{/b}"
        n "I'll bet that when he puts that cigarette out he's going to do it somewhere far away from the desk, so he's got plausible deniability."
        n "If we hide behind the desk and wait for him to leave, we should be able to get to the elevator."
        n "{b}Worth a try{/b}"
        "I hid behind the desk. Just as expected, once the guard had smoked most of the way to the filter, he went far down the hall to dump the cup in the trash can of a nearby office."
        "I dashed toward the elevator. The doors opened."
        "Guard" "Miss! That's a--"
        jump keypad_entry
    else:
        "I looked around and then dashed toward the elevator."
        "???" "Young lady!"
        "My head whipped around and I saw the security guard."
        n "{b}Of course the desk wasn't abandoned, if they had top secret stuff here.{/b}"
        n "Will you give me a break? I have a lot on my mind, OK?"
        n "{b}I'll bet we can make it if we run for it. He was surreptitiously smoking behind that pole so he's probably got a pretty heavy habit. Why else would he be smoking at work, in a non-smoking area, during his shift?{/b}"
        n "OK, I'll try it. Nothing to lose, right?"
        "I started running again."
        "Guard" "That's a sec-- Young lady! Stop!"
        "Guard" "Listen, I'm authorized to shoot! Stop!"
        n "{b}Just keep--{/b}"
        play sound "sfx/gun-shot.wav"
        "{b}BANG{/b}"
        $ knows_poly_guard_position = True
        jump death
label keypad_entry:
    "I slammed the close door button and the doors, thankfully, closed."
    if knows_about_keypad:
        n "Press the button for the basement. That's where the facility is."
        n "{b}Roger that!{/b}"
        scene bg yomi poly keypad
        "The basement was sparse, with the only door other than the elevator locked with a keypad."
        n "{b}Man, this place does NOT care about the fire code. Such a liability.{/b}"
        n "I think they're violating more than the fire code down here."
        "I walked up to the keypad."
    else:
        "I guessed that if there was going to be a secret facility, it would be in the basement, so that's what I punched."
        scene bg yomi poly keypad
        "Getting out, my suspicions were somewhat confirmed. There were no other entrances or exits to this small intercene area. The only other door was locked with a keypad."
        n "Shit..."
    $ knows_about_keypad = True
    python:
        keycode_try = renpy.input("What is the password?")
        if keycode==keycode_try:
            keycode_success=True
        else:
            keycode_success=False
    if keycode_success:
        jump clone_racks
    else:
        "Guard" "Time's up."
        play sound "sfx/gun-shot.wav"
        "{b}BANG{/b}"
        jump death

label clone_racks:
    "The door opened."
    play music "music/Infocalypse_-_Pitted_Crystal-Chrome_Kryptonite.mp3"
    queue music "music/Infocalypse_-_Dickless_Whore__The_Disembodied_.mp3"
    scene bg clone rack
    n "Oh my god..."
    "The clones were naked. Tubes went into various orifices."
    "They were mounted on rack-like devices on top of pedestals."
    if knows_about_clone_racks:
        n "Quick, turn around!"
        n "{b}Wh--{/b}"
        n "Aoi's coming!"
        n "{b}Aoi? Why--{/b}"
        aoi "I hoped you'd never see this."
        menu:
            "What the hell is going on?":
                ai "What the hell is going on, Aoi?"
                "I turned."
                show aoi pout
                aoi "It's too late. You could never love me, now that you know."
                show aoi yandere
                aoi "That's why you have to die. So we can be together."
                "She made a quick motion with her hand, and I saw a flash of steel. Blood seeped into my shirt."
                jump death
            "What is this place?":
                ai "What is this place, Aoi-chan? And what are you doing here?"
                show aoi pout
                aoi "You--"
                aoi "It's a long story. Come with me; it's dangerous to stay here."
                jump aoi_saves
    "They were drooling and dazed, but their eyes looked at me as I entered the room and I sensed some intelligence behind them, like that of a dying old dog."
    "???" "I hoped you'd never find out..."
    "I turned"
    show aoi pout
    aoi "I hoped you'd never see this."
    ai "Aoi-chan?"
    "She was within arm's length, but she stepped closer."
    "There was a cold, sad look in her eyes."
    "I stepped back."
    aoi "But now, it's too late."
    show aoi yandere
    "She was a few steps too close for comfort. I was pinned up against the barrier."
    aoi "I have no choice."
    "She made a quick motion with her hand and I felt warm fluid soak through my shirt. Then..."
    $ knows_about_clone_racks = True
    jump death

label aoi_saves:
    play music "music/Infocalypse_-_Imploded_Transcendence.mp3"
    "Aoi directed me toward a plain grey metal door at the end of the clone area."
    "We passed many clones. Among them I saw one that resembled myself. Her eyes, though glazed and unfocused, followed me as I passed."
    # XXX insert stairwell image
    "We went through the door into what looked like a service stairwell."
    aoi "There are no cameras here, but I need to edit the tapes. Stay here."
    "Aoi went up the stairs a few flights."
    n "{b}Is she calling for guards?{/b}"
    n "I don't think so. The last time, she just stabbed us. If she wanted to get rid of us, thats easier"
    "After a short time, she returned."
    aoi "Ok, I removed the evidence that you were here. We need to leave quick, while the cameras are still blanked out."
    ai "Lead on."
    # XXX insert outside image
    "Aoi led me down the stairs and out some kind of service or emergency exit."
    n "{b}If we had known about this, we wouldn't have had to run past that asthmatic guard.{/b}"
    n "I think we've found out what we need to know. This is probably the last time I'll need to visit this place."
    aoi "I should probably explain."
    aoi "I haven't told anybody else this, ever. I'll tell you because you're my very very best friend and I love you, okay, Ai-chan? But don't ever ever tell anybody, okay?"
    ai "I wouldn't snitch on you, Aoi-chan."
    ai "First, should we be doing this so close to the secret exit? There isn't even a keypad on this side."
    aoi "Oh, yeah. You're right. Let's go to... um..."
    aoi "Let's go to the women's locker room for the pool. There aren't any cameras or microphones there, and the pool's closed anyway."
    "I followed Aoi across the campus and through a building with maze-like corridors, which she navigated with ease."
    # XXX insert image of pool building hallways
    aoi "I used to swim here when I was little. My parents would work in the lab until late, so I was allowed to stay."
    aoi "Nobody asked for the key back, so I still have it."
    "She unlocked an unlabeled door."
    aoi "Come on in."
    # XXX insert image of women's locker room
    ai "You know this campus well, don't you?"
    aoi "I was born here."
    aoi "This is the secret. Promise not to tell anybody, okay?"
    aoi "And super promise not to hate me?"
    ai "Of course I won't hate you."
    aoi "Pinkie swear?"
    ai "Okay. Pinky swear."
    "We shook pinkies."
    aoi "I'm not..."
    aoi "You're sure you won't be mad?"
    ai "Seriously, I'm sure."
    aoi "I'm not the real Aoi."
    aoi "I... died. Or the original me died."
    aoi "Some kind of accident. Fell and hit my head? Or her head?"
    aoi "But I had a copy. In there. Everybody my age born in this town does."
    aoi "My parents took all the umbilical cord blood! So they could keep organs for everybody! But they couldn't do a head transplant and anyway there wasn't anything left."
    aoi "I didn't have anything in my head either. I mean, me-me, not the first me. So I had to learn everything."
    n "Aoi is ditzy, sure, but the paper said the cerebellum should be disconnected. She definitely has higher brain function."
    ai "The clones in there aren't like you, though, right? They're not as smart as you."
    aoi "The clones were supposed to have no brains at all, but it turned out that the organs didn't grow right with no brain at all."
    ai "I see... So, organ development is regulated partially by the cerebellum?"
    aoi "Yeah, organs are told how to grow by the cera-whatsit. So instead of removing it, they just made sure it got only a little blood."
    n "So their cognitive development is higher than planned, but their higher brain regions have constant hypoxia..."
    aoi "I was like that when I was taken out."
    "I remembered, distantly, what she was like after the accident. The glazed eyes, blank staring, learning to talk again..."
    aoi "But my parents make me take all kinds of pills and they make me think better."
    ai "Why did they use umbilical blood?"
    aoi "Um... Something about stem cells? I don't really understand."
    ai "I guess something like that would be beyond me too."
    aoi "Beyond you? But you're getting As in biology! I've seen your tests!"
    ai "You've copied my tests. Anyhow, there's a big difference between being good at high school biology and being a genius like your parents."
    aoi "My parents are geniuses?"
    ai "Yeah. You never realized? Nobody else has ever done human cloning. This was done before anybody had officially cloned a sheep."
    aoi "Weird."
    ai "Hey. We should probably get back to school. We'll be in trouble if we miss too much class. Especially you."
    aoi "Oh, yeah. Let's head back."
    $ knows_whole_aoi_story = True
    scene bg street
    pause 1
    play music "music/Infocalypse_-_scathing_frolic.mp3"
    scene bg classroom
    show kuroneko normal at left
    show aoi blush at right
    kuroneko "Well aren't we adventurous, skipping morning classes together?"
    ai "It's not..."
    ai "Something urgent came up, is all."
    kuroneko "Lots of things can be urgent, when you're young and in love."
    ai "We're the same age!"
    kuroneko "Youth is ninety nine percent perspective."
    ai "So you're, what, mentally a spinster?"
    kuroneko "Something like that. By the way, you just missed Yamada. She went off to the cafeteria in a huff."
    ai "The cafeteria, huh?"
    ai "I skipped breakfast, so I'm pretty hungry."
    jump dont_follow_mimi