# special
define quote = nvl_narrator
define comment = Character("COMMENT") # XXX delete this before release
define n = Character("", what_prefix="{i}", what_suffix="{/i}")
# residents
define misato = Character("Umeji Misato") # room 4
define trust_player=0
define name=""
define akane = Character("Akane") # room 3
define trust_akane=5
define yuuko = Character("Hinamori Yuuko") # room 2
define trust_yuuko=0
define miko = Character("Umeji Miko") # room 1
define trust_miko=25
define hanabi = Character("Tamaya Hanabi") # room 8
define trust_hanabi=0
define hikari = Character("Asahara Hikari") # room 7
define trust_hikari=0
define akiko = Character("Ikuhara Akiko") # room 6
define trust_akiko=0
define corto = Character("Master Corto") # penthouse
define cat_affinity=0 # secret basement
# other
define mina = Character("Umeji Mina")
define trust_mina=25
define kuroki = Character("Fyodor Federov Kuroki")
define trust_kuroki=0
define ai = Character("Akagi Ai")
define trust_ai=0
define aoi = Character("Tomoe Aoi")
define trust_aoi=0

# phone versions, for people we talk to on the phone
define mina_phone = Character("Umeji Mina (SMS)", what_prefix="{k=1.5}", what_suffix="{/k}") # TODO: replace with monospace font

#################### Dramatis Personae
init -2 python:
    class generateDPContent:
        def __call__(self):
            return """
The Umeji Sisters:

{space=75}Umeji Misato (17) - our protagonist, and the eldest of the 3
{space=80}Umeji sisters. She is half french and half japanese. Her french
{space=80}mother joined Corto before meeting her father, a businessman
{space=80}who left the family when he left the cult. She is a telepath.
{space=80}She maintains the image of a polite 'nice girl' of good breeding.
{space=80}She stays in room #4.

{space=75}Umeji Miko (16) - the middle child. Though she doesn't remember it
{space=80}clearly, she was once possessed by a fox. She loves kung-fu movies,
{space=80}and is a skilled martial artist. She stays in room #1.

{space=75}Umeji Mina (14) - the awkward and bookish youngest Umeji sister.
{space=80}She has not been invited to the compound in Yomiyama.

Bruno Akane (17) - half italian (on her father's side), she is self-conscious about her name. She loves 60s and 70s italian horror cinema. She stays in room #3.

Tamaya Hanabi (17) - Akane's friend since childhood. She is obsessed with classic detective fiction. She stays in room #8.

Asahara Hikari (17) - her abiding interest is 60s spy-fi. She stays in room #7.

Hinamori Yuuko (17) - her abiding interest is in ghost stories and weird fiction. She stays in room #2.

Ikuhara Akiko (17) - quiet, athletic, tall, androgyne, and mysterious. She likes to swim laps. She stays in room #6.

Fyodor Federov Kuroki (72) - a self-described 'combat etymologist'.

Corto (62) - formerly a french tennis announcer, he pivoted into cult leader by staging a mystical experience on live television during an intensely-anticipated match. He recognizes that his time is coming to an end.

Akagi Ai (17) - Protagonist of Manna for our Malices, a high school Junior, obsessed with 70s anime and manga (in particular, bancho and sukeban series).

Tomoe Aoi (16) - Ai's childhood friend, the daughter of scientists at nearby Yomiyama Polytechnic.

The Fujinomiya sisters:

{space=75}Shironeko (18) - the eldest, a slacker who has been held back a year
{space=80}because of a habit of blowing off homework

{space=75}Kuroneko (17) - Also a junior, she is an academic overachiever and a
{space=80}skilled violin player

{space=75}Koneko (16) - Despite being a freshman, she is the star of the
{space=80}Yomiyama track team

Yamada Mimi (17) - Another classmate of Ai's, she is a reporter for the school newspaper.

The cats:

{space=75}Kuro (4) - a short-haired black cat

{space=75}Blanche (6) - a long-haired white cat with a regal bearing

{space=75}Umi (2), a smaller long-haired ginger cat with a tempestuous and mercurial personality

{space=75}Other cats are seen but not named."""

        def __str__(self):
            self.call()

screen dramatisPersonae:
    tag menu
    use game_menu(_("Dramatis Personae"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label _("Dramatis Personae:")
            label (generateDPContent()())



#################### Affinity scores
init -5 python:
    style.red_bar = Style(style.default)
    style.red_bar.left_bar = Frame("gui/bar/left.png")
    style.red_bar.right_bar = Frame("gui/bar/right.png")

    style.blue_bar = Style(style.default)
    style.blue_bar.left_bar = Frame("gui/bar/left_blue.png")
    style.blue_bar.right_bar = Frame("gui/bar/right_blue.png")

    style.green_bar = Style(style.default)
    style.green_bar.left_bar = Frame("gui/bar/left_green.png")
    style.green_bar.right_bar = Frame("gui/bar/right_green.png")

    style.red_bar_big = Style(style.default)
    style.red_bar_big.left_bar = Frame("gui/bar/left.png")
    style.red_bar_big.right_bar = Frame("gui/bar/right.png")

    style.blue_bar_big = Style(style.default)
    style.blue_bar_big.left_bar = Frame("gui/bar/left_blue.png")
    style.blue_bar_big.right_bar = Frame("gui/bar/right_blue.png")

    style.green_bar_big = Style(style.default)
    style.green_bar_big.left_bar = Frame("gui/bar/left_green.png")
    style.green_bar_big .right_bar = Frame("gui/bar/right_green.png")

    for item in [style.red_bar, style.blue_bar, style.green_bar]:
        item.xmaximum=319
        item.ymaximum=24
    for item in [style.red_bar_big, style.blue_bar_big, style.green_bar_big]:
        item.xmaximum=639
        item.ymaximum=24



screen affinity:
    tag menu
    use game_menu(_("Affinity"), scroll="viewport"):
        style_prefix "about"
        frame:
            style_group "pref"
            has vbox
            label _("Affinity")
            $ avg_affinity = (trust_player+trust_akane+trust_yuuko+trust_miko+trust_hanabi+trust_hikari+trust_akiko+cat_affinity+trust_mina+trust_kuroki+trust_ai+trust_aoi)/11
            bar xsize 639:
                if avg_affinity>=25:
                    if avg_affinity>=75:
                        style "green_bar_big"
                    else:
                        style "blue_bar_big"
                else:
                    style "red_bar_big"
                value avg_affinity
                range 100
            hbox:
                frame xsize 800:
                    style_group "pref"
                    has vbox
                    if name!="":
                        label _(name)
                    else:
                        label _("Player")
                    bar xsize 639:
                        if trust_player>=25:
                            if trust_player>=75:
                                style "green_bar_big"
                            else:
                                style "blue_bar_big"
                        else:
                            style "red_bar_big"
                        value trust_player
                        range 100
            vbox:
                hbox:
                    frame:
                        style_group "pref"
                        has vbox
                        label _("Residents")
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Akane")
                            bar:
                                if trust_akane>=25:
                                    if trust_akane>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_akane
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Yuuko")
                            bar:
                                if trust_yuuko>=25:
                                    if trust_yuuko>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_yuuko
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Miko")
                            bar:
                                if trust_miko>=25:
                                    if trust_miko>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_miko
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Hanabi")
                            bar:
                                if trust_hanabi>=25:
                                    if trust_hanabi>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_hanabi
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Hikari")
                            bar:
                                if trust_hikari>=25:
                                    if trust_hikari>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_hikari
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Akiko")
                            bar:
                                if trust_akiko>=25:
                                    if trust_akiko>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_akiko
                                range 100
                    frame:
                        style_group "pref"
                        has vbox
                        label _("Non-Residents")
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Mina")
                            bar:
                                if trust_mina>=25:
                                    if trust_mina>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_mina
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Kuroki")
                            bar:
                                if trust_kuroki>=25:
                                    if trust_kuroki>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_kuroki
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Ai")
                            bar:
                                if trust_ai>=25:
                                    if trust_ai>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_ai
                                range 100
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Aoi")
                            bar:
                                if trust_aoi>=25:
                                    if trust_aoi>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value trust_aoi
                                range 100
                    frame:
                        style_group "pref"
                        has vbox
                        frame:
                            style_group "pref"
                            has vbox
                            label _("Cats")
                            bar:
                                if cat_affinity>=25:
                                    if cat_affinity>=75:
                                        style "green_bar"
                                    else:
                                        style "blue_bar"
                                else:
                                    style "red_bar"
                                value cat_affinity
                                range 100
