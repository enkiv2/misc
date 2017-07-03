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