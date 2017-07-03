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
    "Second period should have been biology, but the teacher never showed up."
    "Instead, halfway through the period, a substitute came in and announced a self-study period."
    show kuroneko normal at left
    kuroneko "That's strange. Our bio teacher is usually pretty reliable."
    show mimi pensive
    mimi "Indeed. The last time she missed a class was..."
    "Mimi ruffled through her notebook."
    show mimi smug
    mimi "February third, nineteen seventy four."
    show mimi normal
    show aoi pout at right
    aoi "Yamada-kun, how is it that you know all these things?"
    kuroneko "Nevermind why you even have that information -- how did you look it up so fast?"
    mimi "I have a mnemonic system."
    show mimi smug
    show aoi blush at right
    mimi "You know how a kanji dictionary is organized by radical?"
    mimi "I have a system sort of like that in this book, but organized by shapes."
    mimi "I'm a visual thinker so I associate ideas with specific symbols, and then if I forget a detail I can look it up by shape."
    show kuroneko smile at left
    kuroneko "So I'll bet you're even better at looking up things that are already shapes, right?"
    mimi "Yeah. I usually don't have a hard time remembering those unless they're really obscure, though."
    kuroneko "Comes in handy for the school newspaper?"
    mimi "It would, if that rag did any real journalism."
    show aoi pout at right
    aoi "Ai-chan~"
    extend " Yamada-kun's m-mn-mnewhatsit thing isn't going to make you fall for her, is it?"
    "She stuck out her lower lip and looked at me with puppy-dog eyes, looking almost at the edge of tears."
    "I patted her head."
    ai "You're the only one for me, Aoi~"
    show aoi hearteyes at right
    show mimi angry
    show kuroneko normal at left
    n "She's practically vibrating. It's absurd that such a small display of affection pleases her so much."
    n "One of these days that possessiveness is going to bite me in the ass, though."
    "Mimi got up from her seat."
    mimi "Listen, since lunch is next, I'm going to head to the cafeteria and grab some lunch before the morning rush."
    if died:
        menu:
            "Let her go":
                jump dont_follow_mimi
            "Make an excuse to follow her":
                jump follow_mimi
label dont_follow_mimi:
    aoi "Don't worry, Ai-chan. I brought a bento for you~"
    hide mimi
    ai "I can make my own lunches, you know."
    show aoi pout at right
    aoi "But then our lunches wouldn't match!"
    kuroneko "I'll leave you love birds to your nesting. I'm going to go claim a good spot on the roof."
    ai "Sure, Fujinomiya. Abandon me. I'll be fine."
    show kuroneko smile at left
    kuroneko "I'm sure you will."
    hide kuroneko
    show aoi hearteyes at right
    aoi "You're not alone, Ai-chan~ I'm here with you~~"
    hide aoi
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