###################### SCRIPT
# The game starts here.
label start:
    python:
        from random import Random
        random=Random()
        if not keycode:
            keycode="".join([str(random.choice(range(0, 10))),str(random.choice(range(0, 10))),str(random.choice(range(0, 10))),str(random.choice(range(0, 10)))]) 
    #quote "DEBUG: [keycode]"
    play music "music/Infocalypse_-_yesterday_the_shadows_grew_again.mp3"
    scene bg black
    centered "{color=#fff}{cps=10}\"The outrageous is the reasonable, if introduced politely.\"{/cps}{/color}"
    extend "{color=#fff}{cps=10}\n{space=500}- Charles Fort,{/cps}{/color}"
    extend "{color=#fff}{cps=10}\n{space=400}The Book of the Damned{/cps}{/color}"
    scene bg white with dissolve
    scene bg black with dissolve
    centered "{color=#fff}{cps=15}In the year 20XX, in the small town of Yomiyama, there were a series of deaths.{/cps}{/color}"
    extend "{color=#fff}{cps=15}\nInvestigations of these deaths have been unsuccessful.{/cps}{/color}"
    extend "{color=#fff}{cps=15}\nAs it turns out, a lot was happening just under the surface.{/cps}{/color}"
    jump core_story

