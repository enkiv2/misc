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
# Kuroneko route
define knows_about_kuroneko_concert = False
$ achievement.register("Some Eyes-Wide-Shut MFers")
define knows_about_kuroneko_books = False
# Koneko route
define knows_about_koneko_telepathy = False
$ achievement.register("Touch telepathy")
define saw_milpsi_symbol = False

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

###################### SCRIPT
# The game starts here.
label start:
    play music "music/Infocalypse_-_yesterday_the_shadows_grew_again.mp3"
    scene bg black
    centered "{cps=10}\"The outrageous is the reasonable, if introduced politely.\"{/cps}"
    extend "{cps=10}\n{space=500}- Charles Fort,{/cps}"
    extend "{cps=10}\n{space=400}The Book of the Damned{/cps}"
    scene bg white with dissolve
    scene bg black with dissolve
    centered "{cps=15}In the year 20XX, in the small town of Yomiyama, there was a series of deaths.{/cps}"
    extend "{cps=15}\nInvestigations of these deaths have been unsuccessful.{/cps}"
    extend "{cps=15}\nAs it turns out, a lot was happening just under the surface.{/cps}"
    jump core_story

# core_story is the beginning of the core story loop
# Each time the protagonist dies she is brought back here.
label core_story:
    play music "music/Infocalypse_-_vapor_intrusion.mp3"
    scene bg morning
    "Alarm clock" "Ring Ring Ring Ring"
    n "Ughhhhh"
    "Alarm clock" "Ring Ring Ring Ring"
    n "What the hell happened last night?"
    "Alarm clock" "Ring Ring Ring Ring"
    n "I shouldn't be so goddamned tired"
    "Alarm clock" "BiBiBiBiBiBi"
    if died:
        n "Was it all a dream? I distinctly remem..."
        extend "{b}Hey! What the fuck?{/b}"
        extend "Wow, I must still be dr--"
        extend "{b}Why is there a voice in my hea--{/b}"
        if num_deaths > 1:
            extend "This is going to be hard to ex--"
            extend "{b}I'm going crazy, aren't I?{/b}"
            extend " Look, shut the fuck up a minute. "
            extend "{b}You want me to shut up? It's my fucking head.{/b}"
            extend " Shut up and listen."
            n "OK. Look, I'm you. It's a long story, but I'm you from the future."
            extend "\n{b}I'm listening.{/b}"
            n "I keep dying. And, whenever I die, I end up back here, now, as a voice in my past self's head."
            n "OK?"
            extend "\n{b}...{/b}"
            extend "{b} I guess that isn't any less acceptable than the alternative.{/b}"
            n "OK. You're going to have to trust me and take my advice if you want to eventually not die."
            extend "\n{b}You've lost me there. I'm supposed to obey a voice in my head? If you're me, then you know exactly how unimpressed I am by that suggestion.{/b}"
            n "I'll do what I can to explain the situation. But, if you don't trust me at least a little we'll be stuck in this loop forever."
            n "{b}OK. For now, I'll accept your story. But, if you start telling me to do anything crazy...{/b}"
        else:
            extend "The fuck is going on?! I died and now I'm--"
            extend "{b}You're --{/b}"
            extend "{b} I'm---{/b}"
            extend "{b} dead?{/b}"
            extend "I remember dying, and now there's a voice in my head."
            n "{b}This is my head, fucker.{/b}"
            extend "\nFine, whatever. Your head."
            n "{b}Who the fuck are you anyway?{/b}"
            extend "\nYou first."
            extend "\n{b}No, you first. I'm not letting a strange ghost squat in my skull. The least you can do is fucking introduce yourself.{/b}"
            n "I'm Akagi Ai."
            extend "\n{b}No, {u}I{/u} am Akagi Ai. Try again.{/b}"
            n "No, seriously. I'm Akagi Ai. I'm a junior at Yomiyama High. My student ID number is XXXXX."
            n "{b}You're saying you're me?{/b}"
            n "I guess?"
            n "{b}OK, then. What's my darkest secret?{/b}"
            n "It would have to be that time at the pool in sixth grade, when the..."
            n "{b}OK OK STOP FINE ENOUGH{/b}"
            extend "\n{b}I guess I believe you, OK?{/b}"
            extend "\n{b}But I'm not dead{/b}"
            n "I think I might be you from the future."
            extend "\n{b}What?{/b}"
            extend "{b} Weird.{/b}"
            n "I remember dying and then seeing, like, a white light. Then I woke up here."
            extend "\n{b}How does that make you from the future?{/b}"
            extend "\nBecause you don't remember dying."
    "I slap the snooze button, and then look at the clock's face."
    ai "God damn it!"
    "7 o'clock."
    n "I'm going to be late for school"
    "I throw my clothes on and rush downstairs."
    scene bg downstairs
    with fade
    "Mom" "Don't swear so much, honey. It's not ladylike."
    ai "I learned from the best!"
    "Mom" "... Fuck you."
    scene bg street
    "Mom" "By the way, Aoi's already waiting"
    show aoi happy
    play music "music/Infocalypse_-_scathing_frolic.mp3"
    aoi "Ai-chan~"
    ai "I don't know how you're so fucking energetic in the morning, Aoi."
    aoi "Why wouldn't I be?"
    extend "\nAfter all..."
    show aoi hearteyes
    extend " I get to see"
    extend " my"
    extend " beloved"
    extend " Ai~"
    extend " chan~"
    extend "~"
    extend "~"
    n "I don't know how to respond when she's like this."
    show aoi happy
    aoi "By the way, Ai-chan~~~"
    n "Here it comes..."
    aoi "You wouldn't maybe happen to have today's biology homework, would you?"
    ai "Jesus, Aoi."
    ai "Yeah, sure. You can copy it again."
    show aoi hearteyes
    aoi "{i}Squeee!{/i}"
    ai "Your parents must be reconsidering their whole field. What are the odds of the child of two genius geneticists being such a ditz!"
    show aoi pout
    pause 1
    aoi "Meanie~"
    show aoi happy
    if knows_about_aoi_parents:
        n "I seriously do wonder what's going on with her."
        extend "\nI knew her folks were smart, but the Z Prize is..."
        extend "\n{b}What?{/b}"
        extend "\nHer parents won the Z Prize back in the 90s. I found a picture of them holding it."
        n "I wonder why she never said anything about it."
        extend "\n{b}She gets enough flack for being dense as it is.{/b}"
        extend "\n{b}If people knew her parents weren't just smart but winners of the closest thing synthetic biology has to a Fields Medal...{/b}"
        n "I guess you're right."
    "We continued to make smalltalk the rest of the way to school."
    hide aoi
    scene bg classroom
    show kuroneko pout at left
    "As we entered the classroom, we saw Fujinomiya Kuroneko muttering angrily to herself, stewing over some private betrayal."
    if knows_about_kuroneko_concert:
        n "That deadline must be eating away at her."
        extend "\n{b}What deadline?{/b}"
        n "Those guys that own the anthrosophy lodge behind the convenience store are paying her to play tomorrow night."
        extend "\n{b}And she's not ready?{/b}"
        extend "\nNot even remotely."
        n "{b}That's not like her...{/b}"
        extend "\nThey must have suggested it at short notice."
        extend " I don't think she'd take an offer like that if she wasn't really hurting for money though."
    ai "Fujinomiya! What crawled up your ass and died today?"
    "She took my greeting as a serious question."
    kuroneko "My sister's playing hooky again."
    show aoi happy at right
    aoi "Koneko-chan?"
    kuroneko "Are you an idiot? Koneko hasn't so much as been tardy once since preschool!"
    if knows_about_koneko_telepathy:
        n "Something very weird is going on with Koneko-chan."
        extend "\n{b}Weirder than a ghost in her head?{/b}"
        extend "\nMaybe."
        n "{b}What could be weirder than that?{/b}"
        extend "\nShe knew about the ghost in my head."
        extend "\n{b}In a previous iteration?{/b}"
        extend "\nYeah. And she was in a lot of pain, too."
        n "{b}We're going to find a way to help her, right?{/b}"
        n "I think we should. Ghosts and telepaths in the same town can't possibly be a coincidence. Helping her might also help us not get shanked."
        n "{b}Do we have any leads?{/b}"
        extend "\nShe said something about an appointment before school..."
        extend "\n{b}So we could catch her as she was leaving it.{/b}"
        menu:
            "Don't bother":
                jump dont_look_for_koneko_before_school
            "Look for her":
                jump look_for_koneko_before_school
label dont_look_for_koneko_before_school:
    aoi "Then... Shironeko-senpai?"
    n "Why is that a question?!"
    kuroneko "It seems even Tomoe-san is capable of using the process of elimination."
    show kuroneko happy at left
    show aoi pout at right
    aoi "Ai~chan~~~! Fujinomia-san is making fun of me~~"
    "I patted her on the head"
    ai "There, there."
    show aoi hearteyes at right
    show kuroneko normal at left
    kuroneko "You enable her too much, Ai."
    show aoi happy at right
    ai "Look who's talking. If you and Koneko-chan worked together, you could physically carry Shironeko-senpai to school, and she wouldn't miss so much class."
    show kuroneko happy at left
    kuroneko "She's been doing nothing but eating pocky and sitting at the computer lately. I doubt even Koneko could pick her up now."
    show kuroneko normal at left
    extend "\nWhat she does on there all day is a mystery to me."
    "Teacher" "Alright, settle down."
    stop music
    hide kuroneko
    hide aoi
    "Class rep" "Rise..."
    extend " Bow..."
    extend " Sit"
    "Teacher" "Now, let us quickly review the last chapter."
    "Teacher" "Let me see... We left off with the Genpei War."
    extend " Who can tell me the name of the two eras that this conflict borders?"
    extend " ... "
    extend "\nSince nobody's volunteering, Tomoe?"
    show aoi blush
    aoi "Ummm..."
    extend " The Nara period and the Meiji period?"
    "The teacher sighed."
    n "Sweet merciful fuck this girl is dense. Not only do those periods not border each other, but there's a thousand year gap!"
    "Teacher" "Sit down, Tomoe."
    hide aoi
    "Teacher" "Yamada?"
    show mimi
    mimi "Um..."
    show mimi pensive
    "Mimi picked up a small notebook and nervously flipped through the pages."
    show mimi scoop
    extend " She made a surprised face and then stood up straight."
    show mimi smug
    mimi "The Jisho and the Juei. Hence the alternate name, the Jisho-Juei War."
    "Teacher" "Correct, Yamada. But you should really remember this. You won't be able to consult your notebook for the test."
    show mimi angry
    "Teacher" "Ok, so who were the two sides?"
    hide mimi
    extend " ... Fujinomiya"
    show kuroneko happy
    kuroneko "The Minamoto and the Taira. Genpei is an alternate reading of the two names stuck together."
    "Teacher" "Correct, as always. I should give you a harder one next time."
    show kuroneko normal
    kuroneko "If you try to stump me, you will fail..."
    "Teacher" "Wh-- "
    extend "Nevermind. "
    hide kuroneko
    extend "Okay, Akagi. What sparked the conflict?"
    ai "The Minamoto and the Taira kept bitch-slapping each other over their place in the imperial court's hierarchy, which is stupid because having favor would just make them a target anyway."
    ai "This culminated in the Hogen and Heiji rebellions, where the Minamoto tried to fuck up the Taira but fucked themselves over instead."
    ai "Then the Taira made a toddler emperor, which pissed off the previous emperor's other kid Mochihito, so Mochihito went and helped out the Minamoto."
    ai "Of course, he and his Minamoto buddy got killed anyway so what was the point?"
    ai "Anyway, Mochihito started building up an army, and the Taira heir -- not the rugrat, the geezer -- tried to lock him up. They chased him through Mii-dera and finally got him on the Uji bridge, and the other Minamoto offed himself."
    "Teacher" "Not... incorrect."
    extend " But again I need to remind you to watch your language in class."
    extend "\nSee me after school."
    "The class continued. We didn't even finish covering the Genpei War by the time the bell rang and second period began."
    # XXX fill in other classes, or mention them. We can introduce new characterization for established characters, plug in the cue for Mimi's crush on Aoi, etc.
    # We should especially have some kind of self-study / study hall class, in which the characters talk.
    "The rest of the day came and went without incident" # XXX this is crap
    "Finally, the bell rang."
    "I was about to leave until..."
    "Teacher" "Akagi."
    n "Oh, right."
    "Teacher" "It was the elder Fujinomya's turn to clean the classroom today. Since she isn't in, I'd like you to do it."
    n "Laaaame"
    "Teacher" "Or, if you prefer, you can bring her all her missed printouts."
    "She pointed at a thick stack of printouts on the desk, which looked very heavy."
    if died is False:
        jump clean_classroom
    menu:
        "Clean the classroom":
            jump clean_classroom
        "Deliver printouts":
            jump deliver_printouts

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
    $ saw_milpsi_symbol = True
    "He pushes Koneko through the door and then returns to the van."
    scene bg loading dock
    "It drives off. Once it's out of sight, I get up, preparing to head back to class."
    stop music
    "I feel a hand grab my arm."
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
    "The ceiling was the kind with big, flat tiles with recessed flourescent lights."
    "The tiles had little holes in them."
    "I counted the holes for a while."
    "When I lost count of the holes for the umpteenth time, I looked around for something else to do."
    "I wondered why my wrists hurt, and then I remembered the zip tie."
    "My gaze wandered to the other side of the room."
    "The pill bottle was open, partially filled, and sitting on the fountain. The glass was also sitting on the fountain, partway off the edge."
    "The cabinet door was open and the key was still in the lock. It was attached to a key ring."
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
    jump death
label deliver_printouts:
    # We go to the Fujinomiya household, in the opposite direction from school
    scene bg street
    "The Fujinomiya household isn't very far away. It's about the same distance as between school and my house, but in the opposite direction."
    "Nevertheless, the stack of printouts is heavy, and carrying it is tiring."
    n "How long has she been playing hooky? We don't get much homework so this must be several weeks' worth!"
    scene bg fujinomiya household
    "I ring the bell."
    pause 3
    "No answer."
    "I ring the bell again."
    pause 2
    "This time, I hear some shuffling from inside."
    "The door opens."
    # Shironeko is even more disheveled and sleep-deprived than usual
    shironeko "Yeah yeah, I'm coming."
    show shironeko
    shironeko "Oh, Ai-chan. Wassup?"
    ai "I brought you your printouts."
    shironeko "Come on in."
    scene bg shironeko bedroom
    show shironeko
    shironeko "You can put them on top of the others."
    "There's a pile of printouts several times larger than the one I'm carrying in the center of the floor. I brush a dead bug off the top of it and set the papers down."
    ai "What have you been up to?"
    "Shironeko, distracted by her computer screen, answered vaguely."
    shironeko "Oh, you know..."
    # If you play your cards right, she will admit to having hacked into a nearby facility and gotten info about alien technology
    # You can get info about the facility like how to sneak in, by encouraging her to show off.
    comment "XXX fill in deliver_printouts"
    "The light level in Shironeko's bedroom has gradually changed while I wasn't paying attention."
    ai "It's getting late, so I should head home."
    "Shironeko grunts noncommitally, still staring at her monitor."
    "As I leave, I hear a burst of typing."
    jump walk_home
    
label clean_classroom:
    play music "music/Infocalypse_-_lost_staircase.mp3"
    "The classroom isn't particularly dirty."
    "I stacked up the desks and started cleaning the floor."
    "In the corner of the room there's a box of glassware on loan from the science clubroom."
    if died:
        menu:
            "Ignore the box":
                jump ignore_box
            "Return the box":
                jump return_box
    else:
        jump ignore_box
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
label music_room:
    "I placed the box by the door to the science club's room, and went across the hall."
    scene bg music room
    "The music room was large, with carpeted walls and a stadium-style step arrangement in the floor."
    "In the center, playing a violin and looking irritated, was Kuroneko."
    scene splash kuroneko violin
    with dissolve
    # XXX If we know about the music room from before, we look more carefully and see that Kuroneko has some books with scraps of sheet music shoved in them
    # These are not music-related books but occult-related books.
    if knows_about_kuroneko_concert:
        "The first time this happened, I didn't really pay attention to what else was in the room."
        "This time, I let Kuroneko continue playing, unaware of my presence, while I glanced around."
        "For the most part, the music room was as it usually is at the beginning of practice. All the instruments are put away."
        "I noticed some papers stuffed in Kuroneko's violin case, and a pile of books on a nearby stool."
        "The books had scraps of sheet music sticking out of them, but they were not sheet music books. Instead, they were thick, leather-bound, and looked quite heavy."
        "The book on the very top of the pile was open, and there was a piece of paper sitting on top of it, covered in scribbled notes, and a pencil."
        "There were some geometrical figures on the paper."
        "The bindings of the books had titles in some european language, and a funny-looking symbol."
        $ knows_about_kuroneko_books = True
    # We can ask Mimi or Shironeko to research them.
    # The occult books indicate that Kuroneko knows more than she initially seems to about the purpose of the concert.
    # Once you know the details, you can ask her about that stuff up-front. She will think you are a superior from the lodge sent to supervise her.
    ai "Having trouble?"
    stop music
    scene bg music room
    with dissolve
    show kuroneko pout
    "Kuroneko jumped."
    show kuroneko normal
    kuroneko "The fingering is hard on this piece."
    ai "That's what she said."
    show kuroneko pout
    kuroneko "If you're done..."
    ai "Don't worry, I'm not just here to fuck with you."
    ai "I'm all wiped out from lugging heavy boxes, and I happened to hear some pretty music."
    show kuroneko happy
    kuroneko "Oh yeah?"
    ai "Yeah. And I figured I could rest my bones a while here."
    extend "\nThey say the key to happiness is wine, women, and song. Two out of three ain't bad, right?"
    show kuroneko pout
    kuroneko "Just don't interrupt, OK?"
    ai "Fine, fine."
    show kuroneko normal
    scene splash kuroneko violin
    with dissolve
    play music "music/mystic chord practice.mp3"
    pause 23
    scene bg music room
    show kuroneko pout
    stop music
    kuroneko "I'm getting nowhere with this."
    ai "What is it, exactly, that you're trying to do?"
    show kuroneko normal
    kuroneko "This score is just really weird."
    extend "\nIt's the same six notes over and over in different combinations."
    ai "What's so weird about that?"
    kuroneko "It wants me to play combinations of notes that normally would be done on two different instruments."
    kuroneko "In order to play both notes at the same time on the same instrument I have to hold my fingers like..."
    scene splash kuroneko fingering
    extend " Here, you see what I'm doing with my hand?"
    "Her fingers were held in a kind of claw shape, and her wrist was at an awkward angle. Some fingers were pressing on multiple strings simultaneously at different angles."
    kuroneko "I have to go from that to another equally complicated chord in the space of one beat."
    scene bg music room
    show kuroneko normal
    kuroneko "The whole piece is like that."
    ai "Why don't you play something else? Or get a second violinist?"
    kuroneko "You know those weirdos out in that building with the gold roof?"
    ai "The cylindrical building? Out behind the convenience store?"
    kuroneko "Yeah. They gave me this."
    ai "And?"
    show kuroneko happy
    kuroneko "They offered me a lot of money to play at a concert they have coming up."
    show kuroneko pout
    extend "\nBut I have to play this piece, and they said it has to be exactly as notated."
    ai "When's the concert?"
    kuroneko "The first."
    ai "May first?!"
    kuroneko "That's why I'm in here practicing after dark!"
    ai "Do those fuckers know what they're asking of you?"
    show kuroneko happy
    kuroneko "The money is {i}very{/i} good."
    extend "\nI was suspicious but they told me it wasn't for an orgy or anything."
    ai "Thank god. I don't think I could bear living in a town with that kind of eyes wide shut shit going on."
    $ knows_about_kuroneko_concert = True
    ai "Wait, did you say it was after dark?"
    extend "\nShit, I need to get home!"
    ai "My mom's gonna fucking kill me."
    ai "Thanks for the set, Fujinomya! I gotta jet!"
    kuroneko "Sure, Ai. Just leave me here to stew in my failure."
    extend "\nLater."
    $ achievement.grant("Some Eyes-Wide-Shut MFers")
    scene bg hallway dark
    with dissolve
    jump walk_home
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
label ignore_box:
    "The glassware can wait. I think it's been here for weeks already anyway."
    "I look out the window. There's a solitary figure running around the track."
    n "Must be Koneko-chan. She sure works hard."
    if died:
        menu:
            "Continue tidying up.":
                jump dont_visit_track
            "Go see Koneko-chan":
                jump visit_track
    else:
        jump dont_visit_track

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
    show koneko pain
    extend " but then suddenly doubles over in pain."
    ai "Koneko-chan! Are you okay?"
    scene splash koneko pain
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
    "She slumped to the ground."
    "I checked to make sure she was breathing. She had passed out."
    "I carried her to the nurse's office and laid her out on a bed."
    scene bg nurse office dark
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

label dont_visit_track:
    if died:
        n "She's busy training for the track meet. I'd better not disturb her."
    n "This is exhausting."
    if died:
        menu:
            "Take a nap":
                jump take_nap
            "Continue cleaning":
                jump dont_take_nap
    else:
        jump take_nap
label dont_take_nap:
    n "I'd better not take a nap. I should finish cleaning and head home."
    n "..."
    n "But I'm so fucking tired right now. I guess a little one can't hurt."
    n "That's right..."
    n "A little one. Just a cat nap."
    jump take_nap
label take_nap:
    n "Nobody's in the school, and I have nowhere to go."
    n "I guess I might as well take a little nap."
    n "Then I'll have the energy to finish up."
    "I pull out a desk and chair and fall asleep."
    pause
    n "{cps=1}...{/cps}"
    extend "..."
    extend "zzz"
    extend "zzz"
    n "{cps=1}zzz{/cps}"
    scene bg black
    n "{cps=1}zzZ{/cps}"
    stop music
    n "{cps=1}zz{/cps}Oh shit"
    scene bg classroom dark
    n "Shitfuck"
label walk_home:
    scene bg classroom dark
    stop music
    n "Shit"
    n "The sun has gone down. How late is it?"
    n "I'd better get home."
    "I gather my things and head home."
    scene bg street dark
    play music "music/Infocalypse_-_Light.mp3"
    if died is False:
        n "Are the streetlights malfunctioning? I don't remember the walk home ever being this dark..."
    else:
        n "{b}Are the streetlights malfunctioning? I don't remember the walk home ever being this dark...{/b}"
    if died:
        n "Shit shit shit"
        extend "\n{b}What?{/b}"
        n "This is where I---"
    else:
        n "I have a bad feeling..."
    "Suddenly"
    play music "music/Infocalypse_-_Harvest.mp3"
    extend " I feel a pinch and a strange pressure in my chest."
    "I look down."
    scene splash blood one
    n "Oh shit shit shit shit"
    "A crimson stain"
    n "shit shit shit shit"
    scene splash blood two
    "Vermillion droplets on the ground"
    n "shit shit sh"
    "The outline of a blade poking out of the center of my chest."
    jump death
    
label death:
    play music "music/Infocalypse_-_Try_to_remember.mp3"
    scene bg black
    n "God damn it..."
    n "I'm dying..."
    if died:
        n "Why the hell do I keep dying?"
        if num_deaths > 2:
            n "What kind of stupid-ass chuunibyo bullshit is this?"
            $ achievement.register("Some chuunibyo BS")
            if num_deaths > 5:
                n "If there's a god, I hope he's ready to get an earful."
                n "Jesus fuck. [num_deaths] times? Really?"
            n "People are only supposed to die once, you know!"
    $ num_deaths += 1
    jump rebirth

label rebirth:
    scene bg white
    if died:
        n "I guess it happened again"
    else:
        n "I guess this is what dying is like."
        n "I was never much for religious conjecture. I never thought about life after death or anything like that."
        n "I figured I'd find out firsthand eventually."
        n "I didn't expect it to be this soon, though."
    $ died = True
    $ achievement.grant("Stabbed in the back")
    jump core_story