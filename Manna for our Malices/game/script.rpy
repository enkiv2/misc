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

######################## STATUS FLAGS
define died = False
$ achievement.register("Stabbed in the back")
define num_deaths=0
$ achievement.register("Some chuunibyo BS") # >2 deaths
define knows_about_aoi_parents = False
$ achievement.register("A mysterious photograph")
define knows_about_koneko_telepathy = False
$ achievement.register("Touch telepathy")
define knows_about_kuroneko_concert = False
$ achievement.register("Some Eyes-Wide-Shut MFers")
define knows_about_kuroneko_books = False

####################### BACKGROUND IMAGES
image bg white = "white.png"
image bg black = "black.png"

image bg morning = "morning.png"
image bg downstairs = "downstairs.png"

image bg street = "street.png"
image bg street dark = "street night.png"
image bg classroom = "classroom.png"
image bg classroom dark = "classroom night.png"

####################### SPLASH IMAGES
image bg blood one = "blood 1.png"
image bg blood two = "blood 2.png"

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
    "As we entered the classroom, we saw Fujinomiya Kuroneko muttering angrily to herself, stewing over some private betrayal."
    if knows_about_kuroneko_concert:
        n "That deadline must be eating away at her."
        extend "\n{b}What deadline?{/b}"
        n "Those guys that own the anthrosophy lodge behind the convenience store are paying her to play tomorrow night."
        extend "\n{b}And she's not ready?{/b}"
        extend "\nNot even remotely."
        extend "\n{b}That's not like her...{/b}"
        extend "\nThey must have suggested it at short notice."
        extend " I don't think she'd take an offer like that if she wasn't really hurting for money though."
    show kuroneko pout at right
    ai "Fujinomiya! What crawled up your ass and died today?"
    "She took my greeting as a serious question."
    kuroneko "My sister's playing hooky again."
    show aoi happy at left
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
    show kuroneko happy at right
    show aoi pout at left
    aoi "Ai~chan~~~! Fujinomia-san is making fun of me~~"
    "I patted her on the head"
    ai "There, there."
    show aoi hearteyes at left
    show kuroneko normal at right
    kuroneko "You enable her too much, Ai."
    show aoi happy at left
    ai "Look who's talking. If you and Koneko-chan worked together, you could physically carry Shironeko-senpai to school, and she wouldn't miss so much class."
    show kuroneko happy at right
    kuroneko "She's been doing nothing but eating pocky and sitting at the computer lately. I doubt even Koneko could pick her up now."
    show kuroneko normal at right
    extend "\nWhat she does on there all day is a mystery to me."
    "Teacher" "Alright, settle down."
    stop music
    hide kuroneko
    hide aoi
    "Class rep" "Rise..."
    extend " Bow..."
    extend " Sit"
    "Teacher" "Now, let us quickly review the last chapter."
    # XXX maybe introduce Mimi & other characters here, by having them answer questions first?
    comment "The teacher asks Ai a question and Ai responds correctly but with some colorful language. The teacher chews Ai out for this, and asks to see her after school."
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
    # Here, we probably see Koneko get out of a van with a symbol on it
    # Then, we set up a flag so that later we can get information about the symbol from Mimi
    #
    # However, that doesn't happen in this run-through because a MIB sees you acting suspiciously and takes you into questioning
    #
    # Answering the questions properly has him bring you back to school to get your stuff and then you walk home and die on the way
    #
    # Answering the questions incorrectly has you locked in an interrogation room, but then you hear pounding and screams and the door opens.
    # You go through the door, see all the MIBs mangled, see some kind of glowing portal where the middle of the hallway used to be, 
    # have your legs grabbed by prehensile tentacles, and get your head bashed in against a wall.
    comment "XXX fill in look_for_koneko_before_school"
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
    "As I walk down the hallway toward the science clubroom, I hear music from across the hall."
    play music "music/mystic chord practice.mp3"
    menu:
        "Ignore the music":
            jump ignore_music
        "Investigate":
            jump music_room
label music_room:
    "I placed the box by the door to the science club's room, and went across the hall."
    "The music room was large, with carpeted walls and a stadium-style step arrangement in the floor."
    "In the center, playing a violin and looking irritated, was Kuroneko."
    show kuroneko pout
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
    play music "music/mystic chord practice.mp3"
    pause 23
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
    extend " Here, you see what I'm doing with my hand?"
    "Her fingers were held in a kind of claw shape, and her wrist was at an awkward angle. Some fingers were pressing on multiple strings simultaneously at different angles."
    kuroneko "I have to go from that to another equally complicated chord in the space of one beat."
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
    jump walk_home
label ignore_music:
    n "The music club sure is hard-working."
    "I bring the box of glassware into the science clubroom and set it down on a table."
    "The dust is thick in here."
    "I wipe off my hands on my blouse and look around for a chair."
    n "I'm fucking beat..."
    "I find a small, uncomfortable-looking chair in the corner of the room, with a stack of books on it."
    n "This will do."
    "I try to move the books but my weary arms fumble, and one of them falls to the ground."
    n "Shit"
    "I put the rest of the stack down on top of the glassware and turn to pick up the dropped book. It has fallen open."
    "A folded piece of paper is sticking out, as well a photograph."
    "The paper is yellowed and the photograph is on real photo stock, so it must have been taken before digital cameras."
    "The photo is of two people in lab coats holding some kind of trophy."
    n "Isn't this..."
    play music "music/Infocalypse_-_Lull.mp3"
    extend " Aoi's parents?"
    "The back of the photo is labeled: \"Dr. Tomoe's group, 199x, Z-Prize\""
    n "I didn't realize they were such a big deal."
    "I looked at the paper. It was a bunch of pages of printout from an old dot-matrix printer, accordion-folded."
    "It had what looked like lab instructions, and some diagrams."
    "There were flow charts, drawing of molecules, and what looked like assembly diagrams for laboratory equipment."
    stop music
    "On the last page, there was a picture of what looked like a foetus in a tube."
    $ knows_about_aoi_parents = True
    "{b}CLACK{/b}"
    "I jumped and quickly fumbled the paper back into the book, closing it."
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
    show koneko pout
    extend " but then suddenly doubles over in pain."
    ai "Koneko-chan! Are you okay?"
    koneko "I'm... it's just cramps..."
    "She was holding her stomach with one hand and her head with the other."
    ai "Are you sure you're alright?"
    "I reached for her hand to help her up."
    ai "I could get you to th--"
    play music "music/Infocalypse_-_Invent_New_Chemistry.mp3"
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
    "A few minutes later, she woke up."
    ai "Listen, Koneko-chan. I..."
    koneko "Senpai. I need to go."
    ai "If you can..."
    koneko "I'm late for an appointment."
    "Before I could say anything, she left."
    $ achievement.grant("Touch telepathy")
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
    scene bg blood one
    n "Oh shit shit shit shit"
    "A crimson stain"
    n "shit shit shit shit"
    scene bg blood two
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