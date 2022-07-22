label credits:
    window hide
    scene black with dissolve
    play music "sfx/344430__babuababua__light-rain.mp3"
    init python:
        import re
        name2url={
            "John Ohno": "http://www.lord-enki.net",
            "Ryusei": "http://glitch.social/@ryusei",
            "Cryptovexillologist": "http://mastodon.social/@cryptovexillologist",
            "Infocalypse":"http://infocalypse.nfshost.com"
        }
        def creditize_names(n):
            if type(n) == list:
                return [creditize_names(x) for x in n]
            if n in name2url:
                return "{a="+name2url[n]+"}"+n+"{/a}"
            return n

        anchor_start=re.compile("({a=[^}]*})")
        anchor_end=re.compile("({/a})")
        def creditize_anchors(s, color):
            return anchor_end.sub("{/color}\\1", anchor_start.sub("\\1"+color, s))

        def creditize(s, cps=20, color="#fff"):
            cps="{cps="+str(cps)+"}"
            color="{color="+str(color)+"}"
            return cps+color+creditize_anchors(s, color)+"{/cps}{/color}{w=1.0}{nw}"

        def doubleMojoSplash(cps=2):
            def colorize(s, colors=["f00", "fa0", "ff0", "0f0", "00f", "f0f", "fff", "f00", "0f0", "ff0", "f0f", "fff"]):
                return "{/color}".join(["{color="+colors[i%len(colors)]+"}"+s[i] for i in range(0, len(s))])+"{/color}"
            centered(creditize("A "+colorize("Double Mojo")+" Production", cps=cps)+creditize("\n\"If you can't be good, at least be a lot!\"", cps=40))

        def showCredit(credit):
            headline="{b}"+credit[0]+"{/b}: "
            byline=creditize_names(credit[1])
            if type(byline)==list:
                sep="\n"
                byline=sep+sep.join(byline)
            centered(creditize(headline+byline))

        def showCredits(credits):
            for credit in credits:
                showCredit(credit)
                renpy.scene()
                renpy.show("black")
                renpy.with_statement(dissolve)
            centered(creditize("A part of the {color=#0f0}Yomiyama FLAP{/color} series"))
            doubleMojoSplash()
            achievement.grant("Complete")
            centered(creditize("If you liked this game, please leave a {color=#0f0}rating{/color} or {color=#0f0}review{/color}! The exposure produced by reviews is vital to support small projects like this one.", cps=40))


        sfx=[
             ["InspectorJ", "400402", "Rain, Car Interior, A.wav"],
             ["babuababua", "344430", "light rain.mp3"],
             ["JarredGibb", "248237", "Match - Strike and Light 01.wav"],
             ["16FThumaF",  "499020", "04_Extinguishing of a candle.wav"],
             ["Qat",        "114683", "whack02.mp3"]
        ]
        sfx_url = ["http://freesound.org/people/"+x[0]+"/" for x in sfx]
        sfx_url2 = [sfx_url[x]+"/sounds/"+sfx[x][1]+"/" for x in range(0, len(sfx))]
        sfx_credit = ["{a="+sfx_url2[x]+"}\""+sfx[x][2]+"\"{/a} by {a="+sfx_url[x]+"}{i}"+sfx[x][0]+"{/i} of Freesound.org" for x in range(0, len(sfx))]
        credits=[
            ["Story", "John Ohno"],
            ["Character design & sketches", ["John Ohno", "Ryusei"]],
            ["Character art inking & coloring", "John Ohno"],
            ["Background art", ["John Ohno", "Cryptovexillologist"]],
            ["Music", ["Infocalypse", "An Anonymous Benefactor"]],
            ["Sound effects", sfx_credit]
        ]
    $ showCredits(credits)

    window show
    return
