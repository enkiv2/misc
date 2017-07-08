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
    shironeko "Yeah yeah, I'm coming."
    show shironeko
    "Shironeko is even more disheveled and sleep-deprived than usual"
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
    ai "A smart girl like you staying home for weeks just to play video games doesn't seem realistic."
    shironeko "If you only knew..."
    ai "There are some strange things going on in this town. I know you're the curious type: how about you show me yours and I'll show you mine."
    "Shironeko chuckled."
    shironeko "You first. I want to make sure it's worth my while."
    menu:
        "I got nothin'":
            ai "Um, you know what... Nevermind, forget I said anything."
            jump i_got_nothin
        "Ask her about Project Stargate" if knows_about_stargate:
            jump ask_shironeko_about_stargate
        "Ask her about the symbol on the van" if saw_milpsi_symbol:
            jump ask_shironeko_about_milpsi_symbol
        "Ask her about Yomiyama Industrial Products, Inc." if knows_milpsi_shell_co_name:
            jump ask_shironeko_about_yipi
        "Ask her about the O∴S∴S" if knows_about_oss:
            jump ask_shironeko_about_oss
        "Ask her about the 199X Z-Prize ceremony" if knows_about_missing_lab_notebook:
            jump ask_shironeko_about_zprize
        "Ask her for the submitted papers from the 199X Z-Prize" if knows_aoi_took_lab_notebook:
            jump ask_shironeko_for_zprize_papers
        "Ask her about the code for the keypad lock at Yomiyama Poly's synthetic biology research center" if knows_about_keypad:
            jump ask_shironeko_for_keypad_code
label alien_tech:
    comment "XXX fill in alien tech info"
    $ knows_about_alien_tech = True
    jump leave_fujinomiya_residence
label i_got_nothin:
    "I guess I can't tell her about the ghost thing..."
label leave_fujinomia_residence:
    "The light level in Shironeko's bedroom has gradually changed while I wasn't paying attention."
    ai "It's getting late, so I should head home."
    "Shironeko grunts noncommitally, still staring at her monitor."
    "As I leave, I hear a burst of typing."
    jump walk_home

label ask_shironeko_about_yipi:
    ai "So, there's a local company called Yomiyama Industrial Products, Inc. Sounds boring, right?"
    shironeko "Extremely."
    ai "I have reason to believe they're not what they seem."
    "Shironeko leaned in slightly."
    shironeko "Oh really?"
    ai "I suspect they're a front for some kind of military research do, involving psi."
    shironeko "Hmm..."
    ai "Can you get in?"
    shironeko "Can I? Who do you think you're asking?!"
    shironeko "Sit back and observe."
    "She begins typing in a series of intermittent quick spurts."
    "I'm unsure if the delays are because she's thinking or because she's waiting for some process to finish. I've never seen her have delays this long, so the security must really be something."
    "After nearly an hour, she pauses and takes a drink from a nearby open can."
    "About fifteen minutes she freezes up, sighs, and leans back."
    shironeko "Ai-chan, my dear... What have you gotten yourself mixed up in?"
    ai "I--"
    shironeko "-- No, forget I asked. I don't want to know how you know about this place."
    shironeko "It seems to be funded directly by the Diet, bypassing normal JSSDF chain of command. You know how rare that is?"
    ai "Constitutional-crisis rare?"
    shironeko "Exactly. If the existence of this place got out, nevermind what it was doing, we'd have a lot of big wigs coming here asking awkward questions."
    shironeko "Seppuku might come back into vogue among politicians if this was leaked."
    shironeko "As for what they're using all that illegal secrecy for..."
    ai "Psi research?"
    shironeko "Hard fucking core psi research."
    "I was taken aback. Usually, I'm the only one who swears."
    ai "So this hard-fucking-core psi research... What's going on, exactly?"
    "Shironeko turned back to her screen, evidently referencing a document there."
    shironeko "They take volunteers our age and put them through a battery of psi tests -- zener cards, ganzfield, et cetera."
    shironeko "Those that do poorly are sent on their way with hush money. Those that do well are brought back and are placed in a twice-daily training regimen."
    shironeko "They have their telepathic, clairvoyant, and precognitive abilities tested, with immediate feedback, for hour-long sessions twice a day."
    shironeko "This works sort of like that language-learning software -- if you have any ability at all, you will get better and better at accessing it."
    shironeko "They're given drugs -- slowly titrated onto them, over months."
    shironeko "A mixture of microdosed LSD (to open up the mind), benzos (to create a positive association with the regimen and relax any resistance to suggestion), and sodium pentothol (to enhance suggestibility)."
    shironeko "This is a daily regimen, so even though the doses are pretty low, addiction to the benzos eventually does set in -- a method for keeping volunteers coming back."
    shironeko "From the data they have recorded, it looks like they're having some success."
    shironeko "They're building on some of the weirder ideas from the CIA's Project Stargate: specifically, telepathically contacting aliens from other dimensions and asking them to look into the future or past."
    shironeko "But it looks like the burnout rate for volunteers who graduate to that level is pretty high. They've been doing this for twenty years, and all but one of their volunteers has lasted less than six months as a contact point for the aliens."
    shironeko "They start having chronic migraines, and then eventually graduate to strokes. Sometimes, they also develop intractible epilepsy."
    shironeko "This is... weird stuff."
    shironeko "It doesn't sit well with me, in light of something else I recently uncovered."
    jump alien_tech
label ask_shironeko_about_stargate:
    ai "What do you know about Project Stargate?"
    shironeko "Stargate? CIA black project for remote viewing?"
    ai "Yeah. I guess that's about all I know about it."
    shironeko "Well, I know it didn't stop when it claimed to."
    shironeko "Also, it was leaked early and pretty widely."
    shironeko "I figured maybe it was like red mercury -- you know, a piece of fake info that's intentionally leaked to make opposing intelligence agencies waste time."
    shironeko "But, apparently a lot of people within the CIA took it pretty seriously."
    ai "Makes sense. If there's any chance at all that remote viewing is real, you'd be a dumbass to ignore it."
    shironeko "I guess. I think it was sort of a waste myself."
    ai "Well, the CIA isn't the only organization that took it seriously."
    ai "There's a facility in this town that's doing something with psi research, and their symbol borrows elements from the Stargate unofficial patch."
    shironeko "They pulled a Paperclip?"
    ai "Huh?"
    shironeko "Operation Paperclip. Where the US brought in Nazi scientists under fake identities to work on their own projects at the end of WWII."
    ai "You think that ex-Stargate people have been brought to Japan?"
    shironeko "It's one thing to steal leaked ideas, but copying an unofficial patch is weird if it's a totally independent team."
    ai "That might explain why they were having trouble with kanji..."
    shironeko "Huh?"
    ai "Um, nevermind that. What you're suggesting makes sense."
    ai "Is there material that wasn't declassified?"
    shironeko "Lots. I didn't take it too seriously, though."
    ai "It's deadly serious. There's weird shit going down at that compound."
    shironeko "What kind of weird?"
    ai "Like Cthulhu coming in from a dimensional rip shit."
    shironeko "Hmmm..."
    shironeko "They had all sorts of stuff about telepathic communication with ultraterrestrials -- that is, aliens from alternate dimensions or that rely upon natural wormholes for transportation."
    shironeko "Some people needed to be dropped from the project because contact with these alien intelligences was causing too much strain. Like, being subjected to such an alien thought process was causing memory loss and confusion."
    shironeko "I dismissed it because the way they described the aliens was so different, but I guess there could be two kinds..."
    ai "So different from what?"
    jump alien_tech
label ask_shironeko_about_milpsi_symbol:
    ai "Do you know what this symbol means?"
    "I drew the symbol from the side of the van on a napkin and showed it to her."
    shironeko "Nope! Sorry, I'm not really good with things that aren't text."
    ai "Well, there are some suspicious guys driving around with that symbol on their van."
    shironeko "Hmm... I guess there must be two groups of suspicious guys in this town, then. The ones I know about don't use a symbol like that."
    ai "Oh yeah?"
    jump alien_tech
label ask_shironeko_about_oss:
    ai "Are your hacking skills sufficient to look up information about an occult society?"
    shironeko "If they have a computer and it isn't airgapped, I can get in. If it's airgapped, it'll take a little longer."
    ai "Your sister is involved with some group called the Order of Seers of Sophia. Apparently it pretends to be an anthrosophic lodge but it's actually something else."
    shironeko "She's involved in that place behind the convenience store?"
    ai "I guess that must be the place, yeah."
    shironeko "Involved like how?"
    ai "All she's said is that they're paying her to put on a concert tomorrow. But, she had all sorts of occult material that had their logo on it and was reading it while practicing."
    ai "And Mimi says they're shady."
    shironeko "Yamada? She's almost better at digging up dirt than I am... Almost..."
    shironeko "I'm going to have to look into this... Can I get back to you tomorrow?"
    ai "It..."
    n "I don't think we're gonna live through to tomorrow, considering we haven't survived past this evening yet."
    n "But, if I tell her that, she'll take it the wrong way."
    ai "You need more time? I must have overestimated you..."
    shironeko "Grrr... Ok, Ai-chan. Sit tight and watch the master."
    comment "XXX inject more stuff"
    jump alien_tech
label ask_shironeko_about_zprize:
    ai "You know the 199X Z-Prize ceremony?"
    shironeko "No?"
    ai "It's the one that officially didn't happen. Because of protests and a bomb threat over human germline experiments."
    shironeko "I'm not familiar with it."
    ai "I have reason to believe that it did happen, and that a media gag order was used to prevent coverage."
    "Shironeko leaned in slightly"
    ai "I wonder if you could find more information..."
    shironeko "Of course I can. What do you take me for?"
    ai "I think you'll find that the Yomiyama Poly network will contain some of the gagged materials."
    "Shironeko's gaze slided to her monitor, and she began typing."
    shironeko "Hmm..."
    shironeko "Ah, here we go. In the synthetic biology department, we've got a document that contains the programme."
    shironeko "It's single-DES encrypted, so on a modern machine cracking it is almost immediate. But, it hasn't been written to since the 90s, so I guess that makes sense."
    shironeko "Says here... Oh, Tomoe... Where have I heard that name before?"
    ai "Aoi's family name is Tomoe."
    shironeko "Oh, right. Aoi-chan."
    shironeko "Says here that the Doctors Tomoe are presenting a novel procedure for cloning as an organ source..."
    shironeko "I guess they're married? That {i}has{/i} to be some kind of ethical breach, to marry your own assistant."
    shironeko "The summary says they think it could remove ethical concerns and lower the risk of organ rejection."
    shironeko "There are other abstracts, but those all seem to be old hat -- making zebra fish glow or growing ears on rats."
    ai "Thanks, Fujinomiya-san!"
    shironeko "Heh, no problem."
    shironeko "The security for Yomiyama Poly is a joke."
    shironeko "Let me tell you about a place I got into recently where the security was actually a challenge."
    jump alien_tech
label ask_shironeko_for_zprize_papers:
    comment "XXX fill in ask_shironeko_for_zprize_papers"
    $ read_zprize_papers = True
    $ achievement.grant("Peer review")
    jump alien_tech
label ask_shironeko_for_keypad_code:
    ai "On the entrance to the synthetic biology lab at Yomiyama Poly's research center, there's a keypad lock. I'll bet you can't tell me what the code is."
    shironeko "You underestimate me at your peril, foolish Ai-chan~ Give me, like, five minutes."
    "She began typing."
    "After less than a minute, she looked up."
    shironeko "Their security is a little disappointing."
    shironeko "The code is [keycode]. Don't forget it."
    jump alien_tech
