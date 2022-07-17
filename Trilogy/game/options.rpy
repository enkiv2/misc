﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Trilogy")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
{b}Introduction{/b}

{i}Trilogy is a mystery set in the small town of Yomiyama. It takes place after the events of {/i}Manna for our Malices{i} and {/i}Book of the Damned{i}.{/i}


{b}Dramatis Personae{/b}{i}

Umeji Misato (17) - the eldest of the 3 Umeji sisters. She is half french and half japanese. She maintains the image of a polite 'nice girl' of good breeding.

Bruno Akane (17) - half italian (on her father's side), she is self-conscious about her name. She loves 60s and 70s italian horror cinema.

Akagi Ai (17) - Protagonist of Manna for our Malices, a high school Junior, obsessed with 70s anime and manga (in particular, bancho and sukeban series)

Tomoe Aoi (16) - Ai's childhood friend, the daughter of scientists at nearby Yomiyama Polytechnic

Yamada Mimi (17) - Another classmate of Ai's, she handles the school newspaper
{/i}

{b}Cultural and Localization Notes{/b}{i}

The {/i}Yomiyama{i} series is set in Japan, and while I am not Japanese, I have made an effort to keep cultural elements accurate or to justify any inaccuracies I found necessary for the sake of storytelling. This means that some things mentioned in the story will not necessarily be familiar to western audiences (and while this story is very much set in the kind of warped version of Japan seen in anime, readers may nevertheless be confused).

The stories included in this collection also contain some obscure references to history and literature, which a general audience may not understand.

{b}Bluebeard of Gambais{/b} - The french serial killer {/i}Henri Desire Landru{i}, who killed at least ten women near Paris during and after the first world war. The name {/i}Bluebeard{i} comes from the titular european legend, sometimes associated with Giles de Rais (french serial killer and mentor to Joan of Arc), wherein a rich older man's young bride discovers the corpses of his previous wives in a forbidden room.

{b}Dead Hand System{/i} - the English name of the {/i}Система «Периметр»{i}, a Soviet 'fail-deadly' defense system that launches nuclear missiles automatically in response to a nuclear strike.

{b}Foulness{/b} - Foulness is an actual island in Essex, owned by the Ministry of Defence. Like the island in the story, it was reachable only by boat or by a path that un-submerged at low tide. Unlike the small and rocky island of the story, it has a population of more than one hundred and farmland.

{b}Hundred stories{/b} - {/i}hyakumonogatari{i}, one of several colloquial terms for ghost stories, literally translates to {/i}hundred stories{i}, and comes from a book of the same name. Telling ghost stories is a summer tradition in Japan (with the justification that the shivers caused by fear will cool you down on a hot day), and the term hyakumonogatari is used specifically for telling several in a row.

{b}Jizo{/b} - Jizo is the patron buddha of travelers, women, children, the lost, and the souls of the wandering dead. Jizo statues often are placed by public shelters (where travelers may stay to get out of the weather), though also by graveyards and roadsides. Such statues are dressed in bibs and hankerchiefs as an offering in exchange for guiding the souls of dead children and miscarriages. People sometimes request favors from Jizo while tying a rope to his statue, then untying the rope once the favor is granted.

{b}Lazarus pose{/b} - also called the {/i}lazarus sign{i} or {/i}lazarus reflex{i}, this is a movement that brain-dead patients sometimes make wherein they cross their hands over their chest.

{b}Yomiyama{/b} - the town of Yomiyama does not exist. The name {/i}Yomiyama{i} translates to something like {/i}hades mountain{i}, and is also used in the gothic death game franchise {/i}Another{i}. In this game, however, the town of Yomiyama is a composite of several fictional locations from Japanese media: {/i}Hinamizawa{i} from the {/i}Higurashi no Naku Koro Ni{i} games, Fuyuki from the {/i}Fate{i} franchise, and the unnamed country town in Michio Yamamoto's {/i}The Vampire Doll{i} (1970). It is in a valley surrounded on all sides by mountains, and is now mostly suburban with a built-up 'down town' strip near the university. Until the university began pulling in big government contracts in the early 1990s, this was a much poorer and more rural town whose economic center was a small US military base, but for about twenty years it has been economically ascending, out of phase with the rest of Japan; this makes the local yakuza syndicate comparatively powerful. Since the source of its wealth is mostly-secret government research (by both the United States and Japan), it has resisted the trend in the rest of rural Japan to seek tourists and immigration, and most of the families there are either associated with the university or have been there since before the second world war.
{/i}


{b}Credits{/b}{i}

Concept, script, and programming by {a=http://www.lord-enki.net/}John Ohno{/a}

'The Lazarus Pose', 'The House on Foulness', and 'She Awaited the Turkeys' were originally published on Medium by John Ohno

'She Awaited the Turkeys' has previously been featured on The Signal

{a=call:credits}See all credits{/a}

{/i}""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Trilogy"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "sfx/344430__babuababua__light-rain.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Trilogy-1557178364"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "enkiv2/trilogy"
