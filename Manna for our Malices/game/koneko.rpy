label visit_track:
    scene bg track
    with dissolve
    play music "music/Infocalypse_-_Other_Lands.mp3"
    "By the time I made it down to the track, Koneko was winding down."
    ai "Koneko-chan!"
    "She caught my eye and waved, and then ran over."
    show koneko happy
    koneko "Ai-senpai. Good evening."
    ai "You don't need to be so formal."
    show koneko normal
    "..."
    koneko "Understood."
    ai "You sure are training hard. I was up in the classroom on cleaning duty and saw you running out here, all alone."
    koneko "I see."
    ai "Why isn't the rest of the team training with you?"
    koneko "They train in the mornings."
    ai "Why don't you train with them?"
    n "I had the impression Koneko was an early riser, unlike her eldest sister."
    koneko "I have scheduling conflicts."
    n "What kind of person schedules appointments before 7 AM?!"
    koneko "If you'll excuse me, I--"
    "Koneko starts to brush past me,"
    stop music
    scene splash koneko pain
    extend " but then suddenly doubles over in pain."
    ai "Koneko-chan! Are you okay?"
    koneko "I'm... it's just cramps..."
    "She was holding her stomach with one hand and her head with the other."
    ai "Are you sure you're alright?"
    "I reached for her hand to help her up."
    ai "I could get you to th--"
    play music "music/Infocalypse_-_Invent_New_Chemistry.mp3"
    scene splash koneko shocked pain
    "As soon as I touched her hand, she let out a yelp and pulled it back. I felt a weird tickle down my spine."
    koneko "You--"
    extend "\nThere are two people in your head?!"
    $ knows_about_koneko_telepathy = True
    "..."
    ai "How do you..."
    koneko "What's g..."
    stop music
    scene bg track
    "She slumped to the ground."
    play music "music/Infocalypse_-_Dread_Hypoborea.mp3"
    "I checked to make sure she was breathing. She had passed out."
    scene bg nurse office dark
    "I carried her to the nurse's office and laid her out on a bed."
    "A few minutes later, she woke up."
    show koneko normal
    ai "Listen, Koneko-chan. I..."
    koneko "Senpai. I need to go."
    ai "If you can..."
    koneko "I'm late for an appointment."
    "Before I could say anything, she left."
    hide koneko
    $ achievement.grant("Touch telepathy")
    scene bg hallway dark
    with dissolve
    jump walk_home

label look_for_koneko_before_school:
    play music "music/Infocalypse_-_Stimulated_Emission.mp3"
    ai "Hey, Aoi, Fujinomiya, could you spot me for a bit?"
    aoi "Sure! Anything for you~"
    kuroneko "What are you planning?"
    ai "Nothing suspicious. I just forgot something in my locker."
    ai "When the teacher comes in, tell her I'm in the bathroom. I'll leave my bag here."
    kuroneko "I don't buy it, but whatever. Sure, I'll lie for you."
    aoi "I'd lie for you any time, Ai-chan!"
    extend " Fujinomiya-san says she'd lie for you but don't let that tempt you."
    extend " If you need a really big lie or a really dangerous lie, leave it to me!"
    extend " She can't lie well enough to steal you away from me! I'm sure she can't!"
    n "Down, girl."
    ai "Thanks. I'll be right back."
    scene bg hallway
    "I almost passed the teacher heading toward the stairs, but I hid around the corner of the stairwell until she passed."
    n "I've never seen her get dropped off, and the front entrance is visible from the classroom window. So, she must be getting dropped off in the rear."
    n "That would explain how she's never late. Freshmen are on the first floor, and the loading dock entrance is in back and it's by the end of the hall right near her classroom."
    scene bg loading dock
    "I head to the loading dock and hide behind a trash can."
    scene splash van
    "A black van pulls up. It has a symbol on the door."
    "A man in a black uniform gets out the passenger side, opens up the back, and helps Koneko out."
    "She's stumbling and holding her head."
    "He walks her to the door. As he passes, I see that he has the same symbol as on the van on his left shoulder."
    "He pushes Koneko through the door and then returns to the van."
    scene bg loading dock
    "It drives off. Once it's out of sight, I get up, preparing to head back to class."
    stop music
    "I feel a hand grab my arm."
    play music "music/Infocalypse_-_Dread_Hypoborea.mp3"
    "I turn. It's another man in the same dark uniform, with the same symbol on the shoulder."
    "MIB" "Seen anything interesting?"
    ai "I was just..."
    "MIB" "You were just hanging out behind a trash can during class?"
    "I couldn't think of a better excuse."
    "MIB" "We have a zero tolerance policy for suspicious behavior. I'm sorry to say you're going to have to come with us."
    "He didn't look sorry."
    "MIB" "Sorry but you're gonna have to wear this."
    "He held up a black cloth bag. He still didn't look sorry."
    scene bg black
    extend "\nBefore I had a chance to say anything, he shoved my head into it roughly. He then grabbed my other arm and quickly zip-tied my wrists together."
    "I was dragged some distance, lifted slightly off the ground, and laid face down on what felt like carpeting."
    "Then, I was rolled onto my side and my legs were pushed in. I heard a door slam, another, and then felt the van begin to move."
    "After a little while, I felt the van make a sharp turn and then head down a steep hill. The terrain then evened out but became bumpy."
    "It's hard to get a clear sense of time when your senses are cut off, but it felt like twenty or thirty minutes before the van once again stopped."
    play music "music/Infocalypse_-_The_Heads_Sprang_Up__Featuring_The_Dixie_Flatline_.mp3" fadein 600
    "I felt a gust of air as the door was opened, and somebody grabbed me."
    "My feet dragged over some gravel, and then a smoother surface. They went over a small bump, like the bottom edge of a doorway, and then another one."
    "I was placed, sitting down, in a folding chair. My mask was removed."
    scene bg interrogation room
    "MIB" "Okay, start talking."
    "I was still disoriented from the experience of being suddenly blindfolded and restrained."
    "MIB" "Today."
    ai "W-"
    "MIB" "Who sent you?"
    ai "N-"
    "MIB" "..."
    "I took a moment to gather myself."
    ai "Nobody sent me."
    "MIB" "Nobody sent you? You're saying you were just hanging out behind that t-"
    ai "My friend was hurting."
    ai "Something was making her hurt. And she was acting strange."
    ai "So I decided to see what it was she was doing in the mornings."
    "MIB" "This friend of yours is..."
    "He read something off a clipboard."
    "MIB" "Fu... ji... nomiya? Am I pronoucing that right?"
    ai "Yes. Fujinomiya motherfucking Koneko. Okay? You know her?"
    "MIB" "She's on the list."
    ai "What list?"
    "He shot me a glare."
    "MIB" "I'm"
    extend " asking"
    extend " the questions."
    extend "\nYou're"
    extend " giving"
    extend " the answers."
    "MIB" "Are we clear on our roles?"
    n "This guy is really getting on my nerves."
    ai "Clear as fucking crystal."
    "MIB" "I'll forgive the attitude if you tell me what I need to know."
    "MIB" "Name?"
    ai "Akagi Ai"
    "MIB" "How do you spell it?"
    ai "Aka as in red. Gi as in garment. Ai as in true fucking love."
    "MIB" "... OK."
    n "It looks like he's having trouble with the kanji. Is he even Japanese?"
    n "I didn't notice an accent, so maybe he's just illiterate."
    "MIB" "And what were you doing spying from behind that trash can?"
    ai "I already told you. I was worried about my f--"
    "MIB" "Oh, yes. That"
    extend " ..."
    extend " Fu-ichi-nandemoyo fellow."
    ai "Fujinomiya."
    n "I don't think it's kosher to use 'fellow' to refer to a teenage girl. This guy can't be a native speaker."
    ai "She was acting weirdly."
    "The man looked surprised, as though I hadn't just told him all this less than five minutes ago."
    "MIB" "Acting strange? When?"
    ai "Tod--"
    ai "Yesterday."
    n "What the hell am I doing? I can't tell this guy that I saw her acting strange LATER TODAY."
    n "Get it together, Akagi Ai! The situation's strange but that's all the more reason that thinking straight is Fucking Important."
    "The man didn't seem to notice my mistake."
    "MIB" "When did you see her acting strangely yesterday?"
    n "It's hard to remember anything that happened \"yesterday\". I've lived through \"today\" [num_deaths] times now."
    n "Shit, if this keeps up I won't be able to remember anything that didn't happen \"today\"."
    "The man cleared his throat."
    "MIB" "When did you see her ac--"
    "The man cleared his throat again."
    "MIB" "When di--"
    "He began coughing."
    "After an extended bout of coughing, he put his clipboard down, got up, and went across the room."
    "I got a look at his clipboard. His writing was chicken-scratch. Not just messy, but borderline unreadable."
    "He'd be thrown out of second grade for that hirigana."
    "The kanji was... not wrong, per-se, but the strokes were out of order, even on simple characters."
    "He rattled around in a cabinet across the room for a little while, took out a pill bottle, filled a glass with water from the fountain in the corner, and took several pills."
    "He then put the pill bottle and glass down on the fountain, locked the cabinet, and came back to the table."
    "MIB" "Name?"
    ai "I just told you my name."
    "He looked down at the clipboard and then looked surprised."
    "MIB" "So you did."
    "He peered closely at the clipboard."
    "MIB" "So you said you saw Fu-shi-gi-namae-ya--"
    ai "Fujinomiya."
    "MIB" "Yeah, Fushiginamaeyo. You say Fushiginomuru acting strangely yesterday. Could you describe the--"
    "He stopped for a moment and looked blankly into space."
    "He started to get up, and then sat back down."
    "He started to get up again and stopped in the middle."
    "MIB" "Excuse me for a moment."
    "He got up, opened the door, and left."
    "I don't know how long I was waiting for him to return."
    "I began examining the scratches in the table in front of me. There were a lot of them."
    if saw_milpsi_symbol:
        play music "music/Infocalypse_-_Ludibrium.mp3" fadein 100
        "I vaguely remembered all of this happening before, but it felt like a half-remembered dream"
        "All my memories of this place feel foggy, as though I was drugged"
        n "Maybe I should try to focus"
        n "{b}Why?{/b}"
        n "Why should I focus?"
        n "{b}Why should I focus?{/b}"
        n "I..."
        n "Why should I focus?"
        n "Should I focus?"
        menu:
            "Make a concerted effort to focus":
                jump make_effort_to_focus
            "Nevermind, it's all good":
                jump dont_focus_next
label dont_focus_next:
    "The ceiling was the kind with big, flat tiles with recessed flourescent lights."
    "The tiles had little holes in them."
    "I counted the holes for a while."
    "When I lost count of the holes for the umpteenth time, I looked around for something else to do."
    if saw_milpsi_symbol:
        "I vaguely remembered all of this happening before, but it felt like a half-remembered dream"
        "All my memories of this place feel foggy, as though I was drugged"
        n "Maybe I should try to focus"
        n "{b}Why?{/b}"
        n "Why should I focus?"
        n "{b}Why should I focus?{/b}"
        n "I..."
        n "Why should I focus?"
        n "Should I focus?"
        menu:
            "Make a concerted effort to focus":
                jump make_effort_to_focus
            "It's all good":
                jump dont_focus_next_2
label dont_focus_next_2:
    "I wondered why my wrists hurt, and then I remembered the zip tie."
    "My gaze wandered to the other side of the room."
    "The pill bottle was open, partially filled, and sitting on the fountain. The glass was also sitting on the fountain, partway off the edge."
    "The cabinet door was open and the key was still in the lock. It was attached to a key ring."
    if saw_milpsi_symbol:
        "I vaguely remembered all of this happening before, but it felt like a half-remembered dream"
        "All my memories of this place feel foggy, as though I was drugged"
        n "Maybe I should try to focus"
        n "{b}Why?{/b}"
        n "Why should I focus?"
        n "{b}Why should I focus?{/b}"
        n "I..."
        n "Why should I focus?"
        n "Should I focus?"
        menu:
            "Make a concerted effort to focus":
                jump make_effort_to_focus
            "Nah, I'm sure everything will be fine":
                jump dont_focus_next_3
label dont_focus_next_3:
    "I was considering going over to look in the cabinet when the lights went out."
    scene bg black
    play music "music/Infocalypse_-_KILL_CONSUME_MULTIPLY_CONQUER.mp3"
    "I heard a series of popping sounds, followed by a scream and several loud bangs."
    "Then, I heard a sliding sound, like somebody slowly rubbing sandpaper along the outside of a metal pipe."
    "I heard two banging sounds. The second one coincided with a dent appearing in the door."
    "The door slowly creaked open."
    "I got up and went to look outside."
    scene milpsi corridor massacre
    "The lights were all out in the corridor except for one, which was flickering."
    "The primary illumination was the dim glow from some kind of circular..."
    extend " thing."
    "The thing was swirling, and so was the light coming from it."
    "It illuminated bloodstains in the dented walls and crumpled bodies in black uniforms."
    "I was about to step back inside the interrogation room when I felt someone grab my ankle."
    "I looked down, expecting to see the black-uniformed man from before, but instead there were a bunch of thin rubbery strands, about the width of a pencil."
    "I bent down and touched them. They were covered in a sticky mucousy substance, and smelled overpoweringly rank, like week-old road kill."
    "The mucous made webs between my fingers."
    "Suddenly, I was lifted off my feet, upside down."
    "I saw a wall coming toward me, too fast."
    $ saw_milpsi_symbol = True
    jump death
label make_effort_to_focus:
    play music "music/Infocalypse_-_yesterday_the_shadows_grew_again.mp3"
    "Focusing was hard. It was although my head was full of cotton."
    scene bg black
    pause 0.1
    scene milpsi corridor massacre
    pause 0.1
    scene bg black
    pause 0.1
    scene bg interrogation room
    "I remembered that something bad had already happened to me here."
    scene bg black
    pause 0.1
    scene milpsi corridor massacre
    pause 0.1
    scene bg black
    pause 0.1
    scene bg interrogation room
    "I had stayed in this room for a long time, distracted and bored, and by the time I left"
    scene bg black
    pause 0.1
    scene milpsi corridor massacre
    pause 0.1
    scene bg black
    pause 0.1
    scene bg interrogation room
    pause 0.1
    scene bg black
    pause 0.1
    scene milpsi corridor massacre
    pause 0.1
    scene bg black
    pause 0.1
    scene bg interrogation room
    pause 0.1
    scene milpsi corridor massacre
    pause 0.1
    scene bg interrogation room
    pause 0.1
    scene milpsi corridor massacre
    n "Something like that happened..."
    scene bg interrogation room
    n "I need to get out of here..."
    # XXX we attempt to focus again and end up breaking the glass to cut the zip ties and leaving (the door is open). We may look in cabinet.
    # Everyone in the hallway is standing still, staring into space, wobbling slightly
    # We leave, run up the hill until we see the sign for the shell company, and then the building expodes, we're thrown to the ground, and a chunk of shrapnel impales us
    $ knows_milpsi_shell_co_name = True
    jump death