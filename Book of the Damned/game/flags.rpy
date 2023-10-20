default persistent.skip_NSFW = False
default persistent.skip_OP = False
default persistent.override_judgement = False # i.e., control Misato with your choices, rather than having her choose based on trust_player

define debugMode = False

define day = 0

define paranoia = 0 # paranoia mechanic is similar to a sanity mechanic.
# It increases when Misato experiences something scary, and decreases when
# she experiences something calming. It decreases overnight in a way that
# is proportional to various affinity scores. If it gets to 100%, Misato has
# a panic attack and faints, has a nightmare, and has some possibility of 
# having a heart attack or stroke; if she survives, paranoia is decreased by 10%.
# The paranoia score affects Misato's likelihood of preferring certain 
# decisions, and also will affect dream selection.

define akane_route_achieved = False
define hanabi_route_achieved = False
define yuuko_route_achieved = False
define miko_route_achieved = False
define mina_route_achieved = False
define hikari_route_achieved = False
define akiko_route_achieved = False

define harem_route_allowed = False # only if all above routes achieved
define harem_route_achieved = False # opens up true end

init python:
    achievement.register("The Ides of March")
    achievement.register("April showers")
    achievement.register("Walpurgisnacht")
    achievement.register("May flowers")

    achievement.register("Goth GF") # has sex with Akane
    achievement.register("Akane route", stat_max=100)
    achievement.register("Hanabi route", stat_max=100)
    achievement.register("Yuuko route", stat_max=100)
    achievement.register("Miko route", stat_max=100)
    achievement.register("Mina route", stat_max=100)
    achievement.register("Hikari route", stat_max=100)
    achievement.register("Akiko route", stat_max=100)
    achievement.register("Harem route", stat_max=100)
    achievement.register("Your garden has been sown with asphodel.")

    achievement.register("Jellicle")
    achievement.register("A cat just walked over my grave.")
    achievement.register("Moja sestra? Moja sestra.")
    achievement.register("Heaviside layer")

    achievement.register("Panic! In the nave.")
    achievement.register("The heart police have put you under cardiac arrest")

    achievement.register("Bad end")
    achievement.register("Complete")

    def checkAchievements():
        global akane_route_achieved, hanabi_route_achieved, yuuko_route_achieved, miko_route_achieved, mina_route_achieved, hikari_route_achieved, akiko_route_achieved, harem_route_allowed, harem_route_achieved
        global day
        if trust_akane >= 100:
            akane_route_achieved = True
            achievement.grant("Akane route")
        else:
            achievement.progress("Akane route", trust_akane)

        if trust_hanabi >= 100:
            hanabi_route_achieved = True
            achievement.grant("Hanabi route")
        else:
            achievement.progress("Hanabi route", trust_hanabi)

        if trust_yuuko >= 100:
            yuuko_route_achieved = True
            achievement.grant("Yuuko route")
        else:
            achievement.progress("Yuuko route", trust_yuuko)

        if trust_miko >= 100:
            miko_route_achieved = True
            achievement.grant("Miko route")
        else:
            achievement.progress("Miko route", trust_miko)

        if trust_mina >= 100:
            mina_route_achieved = True
            achievement.grant("Mina route")
        else:
            achievement.progress("Mina route", trust_mina)

        if trust_hikari >= 100:
            hikari_route_achieved = True
            achievement.grant("Hikari route")
        else:
            achievement.progress("Hikari route", trust_hikari)

        if trust_akiko >= 100:
            akiko_route_achieved = True
            achievement.grant("Akiko route")
        else:
            achievement.progress("Akiko route", trust_akiko)

        if cat_affinity >= 100:
            achievement.grant("Jellicle")
        else:
            achievement.progress("Jellicle", cat_affinity)

        if achievement.has("Akane route") and achievement.has("Yuuko route") and achievement.has("Miko route") and achievement.has("Mina route") and achievement.has("Hikari route") and achievement.has("Akiko route") and achievement.has("Jellicle"):
            harem_route_allowed = True

        if harem_route_allowed:
            if akane_route_achieved and hanabi_route_achieved and yuuko_route_achieved and miko_route_achieved and mina_route_achieved and hikari_route_achieved and akiko_route_achieved:
                harem_route_achieved = True
                achievement.grant("Harem route")
            else:
                achievement.progress("Harem route", (trust_akane + trust_hanabi + trust_yuuko + trust_miko + trust_mina + trust_hikari + trust_akiko) / 7)

        if day==0:
            achievement.grant("The Ides of March")
        elif day==16:
            achievement.grant("April showers")
        elif day==46:
            achievement.grant("May flowers")

    def updateParanoia(delta):
        if delta > 0:
            misato("I have a bad feeling about this...")
        elif delta < 0:
            misato("That's a relief...")
        paranoia += delta
        if paranoia >= 100:
            paranoia=100
            panicAttack()

    def panicAttack():
        misato("I don't feel so good...")
        achievement.grant("Panic! In the nave.")
        if random.randint(0, 100) < 10: # for now, one in ten panic attacks lead to death
            if random.randint(0, 100) < 25: # one quarter are strokes
                comment("Misato has a stroke")
            else:
                comment("Misato has a heart attack")
           achievement.grant("The heart police have put you under cardiac arrest")
           renpy.call("badEnd") 
        paranoia = 90
