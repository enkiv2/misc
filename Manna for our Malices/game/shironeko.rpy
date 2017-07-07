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
        "Ask her about the symbol on the van" if knows_about_milpsi_symbol:
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
label i_got_nothin:
    "I guess I can't tell her about the ghost thing..."
    "The light level in Shironeko's bedroom has gradually changed while I wasn't paying attention."
    ai "It's getting late, so I should head home."
    "Shironeko grunts noncommitally, still staring at her monitor."
    "As I leave, I hear a burst of typing."
    jump walk_home

label ask_shironeko_about_yipi:
    comment "XXX fill in ask_shironeko_about_yipi"
    jump alien_tech
label ask_shironeko_about_stargate:
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
    shironeko "She's involved in that place behind the convenient store?"
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
    comment "XXX fill in ask_shironeko_about_yipi"
    jump alien_tech
label ask_shironeko_for_zprize_papers:
    comment "XXX fill in ask_shironeko_about_yipi"
    jump alien_tech
label ask_shironeko_for_keypad_code:
    ai "On the entrance to the synthetic biology lab at Yomiyama Poly's research center, there's a keypad lock. I'll bet you can't tell me what the code is."
    shironeko "You underestimate me at your peril, foolish Ai-chan~ Give me, like, five minutes."
    "She began typing."
    "After less than a minute, she looked up."
    shironeko "Their security is a little disappointing."
    shironeko "The code is [keycode]. Don't forget it."
    jump alien_tech
