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
