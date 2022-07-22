## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Book of the Damned")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
{b}Introduction{/b}

{i}Book of the Damned is a mystery set in the small town of Yomiyama. It takes place prior to and during the events of {/i}Manna for our Malices{i} and prior to the events of {/i}Trilogy{i}.{/i}


{b}Dramatis Personae{/b}{i}
Umeji Misato (17) - our protagonist, and the eldest of the 3 Umeji sisters. She is half french and half japanese. Her french mother joined Corto before meeting her father, a businessman who left the family when he left the cult. She is a telepath. She maintains the image of a polite 'nice girl' of good breeding.

Umeji Miko (16) - the middle child. Though she doesn't remember it clearly, she was once possessed by a fox. She loves kung-fu movies, and is a skilled martial artist.

Umeji Mina (14) - the awkward and bookish youngest Umeji sister. She has not been invited to the compound in Yomiyama.

Bruno Akane (17) - half italian (on her father's side), she is self-conscious about her name. She loves 60s and 70s italian horror cinema.

Tamaya Hanabi (17) - Akane's friend since childhood. She is obsessed with classic detective fiction.

Asahara Hikari (17) - her abiding interest is 60s spy-fi.

Hinamori Yuuko (17) - her abiding interest is in ghost stories and weird fiction.

Ikuhara Akiko (17) - quiet, athletic, tall, androgyne, and mysterious. She likes to swim laps.

Fyodor Federov Kuroki (72) - a self-described 'combat etymologist'.

Corto (62) - formerly a french tennis announcer, he pivoted into cult leader by staging a mystical experience on live television during an intensely-anticipated match. He recognizes that his time is coming to an end

Akagi Ai (17) - Protagonist of Manna for our Malices, a high school Junior, obsessed with 70s anime and manga (in particular, bancho and sukeban series)

Tomoe Aoi (16) - Ai's childhood friend, the daughter of scientists at nearby Yomiyama Polytechnic

The Fujinomiya sisters:

{space=100}Shironeko (18) - the eldest, a slacker who has been held back a year
{space=110}because of a habit of blowing off homework

{space=100}Kuroneko (17) - Also a junior, she is an academic overachiever and a
{space=110}skilled violin player

{space=100}Koneko (16) - Despite being a freshman, she is the star of the
{space=110}Yomiyama track team

Yamada Mimi (17) - Another classmate of Ai's, she handles the school newspaper

The cats: Kuro (4), a short-haired black cat, and Aka (2), a smaller long-haired ginger cat. Other cats are seen but not named.
{/i}

{b}Cultural and Localization Notes{/b}{i}

The {/i}Yomiyama{i} series is set in Japan, and while I am not Japanese, I have made an effort to keep cultural elements accurate or to justify any inaccuracies I found necessary for the sake of storytelling. This means that some things mentioned in the story will not necessarily be familiar to western audiences (and while this story is very much set in the kind of warped version of Japan seen in anime, readers may nevertheless be confused).

This is also a story about magic, conspiracy theories, and super-science, and I make references to both media and actual events and practices that a general audience will probably not be familiar with.

I am providing the following notes for the sake of such a general audience, so that puzzles that would be nearly impossible without this knowledge become solveable. I found that my in-game explanations in the first release were too oblique for some players, leading to frustration.

{b}American military bases{/b} - after the end of the occupation, a lot of american military bases remained on Japanese soil. This is the source of a lot of political friction: Japan relies upon the United States for military protection, since its ability to have its own military is limited constitutionally, so ruining its relationship with the US is an existential threat, but at the same time the continued existence of these bases is seen as a breach of autonomy & there have been many high-profile scandals involving American soldiers committing serious crimes against Japanese locals (including rape and murder) and being percieved as 'getting off easy' in the American military judicial system.

{b}Aniki{/b} - a relatively formal way of saying {/i}older brother{i}, used by yakuza members to refer to people they work with who are senior to them (particularly the people they report directly to). Also used in less organized gangs, in the same way. The feminine equivalent, used in girl gangs, is {/i}aneue{i}. Sometimes, these terms are used as a gendered form of {/i}senpai{i}, but doing so implies that the speaker has a criminal background.

{b}Bakeneko{/b} - a 'werecat' or 'phantom cat'. Like with foxes, cats have a complicated place in Japanese myth. The distinction between a bakeneko and an ordinary cat (and whether or not non-supernatural cats exist) is unclear in this context. As a cat's soul ages, it grows in power, and gains a tail with each new life. The bakeneko is said to be capable of taking human form and to resurrect the dead by jumping over corpses backwards. The bakeneko also loves to play pranks, including drinking lamp fluid and setting fire to houses. While the prefix 'bake' is sometimes translated as 'monster', it literally means 'changing', much like the prefix 'were' in english; however, unlike werewolves, who are humans that take on the shape of wolves, bakeneko and fox spirits are animals who take on human forms while remaining intellectually alien.

{b}Bancho{/b} - a stereotype of a (male) post-second-world-war juvenile delinquent. Bancho wear pageboy hats (often from school uniforms), black school uniform jackets worn open, baggy pants, wooden sandals, and wrap their stomach with white cloth as protection against blunt weapons. This type was a common trope in 60s and 70s manga aimed at teenage boys. The rough equivalent for female delinquents is {/i}sukeban{i}.

{b}Classrooms{/b} - unlike in the west, where junior high and high school students go to subject-specific classrooms, in Japanese schools, the students stay put while the teachers rotate, with specialized materials like chemistry supplies stored in rooms shared with after school clubs. Students are responsible for cleaning classrooms and performing other forms of maintenance work as a way of encouraging a sense of responsibility and ownership (part of a policy that also encourages them to make their own way to school and bring handouts and notes to the homes of sick classmates). While cleaning duty is assigned to students on a rotating schedule, it can sometimes be reassigned to a different student as a mild form of punishment.

{b}Class S{/b} - a literary genre centering around romanticized relationships between schoolgirls, originally developed in the early 20th century. While the relationships are sometimes explicitly romantic or even explicitly sexual, they are also often just ambiguous enough to provide plausible deniability. While Class S is now often considered problematic, for decades it was the primary way that lesbians were represented in Japanese media outside of sexualized depictions aimed at men. Class S traffics in specific tropes: private all-girls schools, dreamy young women obsessed with the signifiers of western luxury (especially 18th century french high culture), and deep connections between young women that dissolve upon graduation. {/i}Manna{i} is not a Class S work, but I import some tropes from it, and it provides genre justification for the idea that nearly all of the characters in the series are lesbians (rather than only about half).

{b}Edogawa Ranpo{/b} - the pen name of {/i}Tarou Hirai{i}, an early 20th century author who popularized elements of both classic mystery and weird fiction in Japan.

{b}Festival{/b} - towns in Japan often have {/i}masturi{i} (typically translated as {/i}festivals{i}) once a year. During these festivals, colorful stalls are set up selling junk food, toys, masks, and often-rigged games. Many attendees wear traditional Japanese clothing (and this is one of the rare occasions when it is normal to do so in public). The festivities also involve a parade where a shinto shrine is carried, drumming and traditional dances, and fireworks to mark the end of the festival. Festivals are usually held during the summer, but I moved this one to the spring.

{b}Charles Fort{/b} - an early 20th century satirist and author of four books: 'Lo!', 'New Lands', 'Wild Talents', and 'The Book of the Damned'. Fort's philosophy -- specifically, his claim that the world was full of unexplained events that many scientists, because of their human vices, ignore or dismiss instead of properly investigating -- inspired the Fortean movement, which itself was influential on the Zetetic wing of the Skeptic movement. Fort is considered an important figure in the study of various anomolous phenomena that now have their own fields -- UFOlogy, cryptozoology, parapsychology and psi research, and cryptoarchaeology. He is most strongly associated with 'strange rains' such as frog-falls, and strange rains are one of the two central metaphors in his 'Book of the Damned'.

{b}Golden week{/b} - this is the longest block of holidays for most Japanese adults, and one of the longest blocks of holidays for Japanese students. It is a series of national holidays that are close together, spanning from late April to early May. Because weekdays that are between two weekday holidays are considered holidays, and because holidays that fall on a weekend are moved to the weekday they border, most people have an entire week off during this period. (Meanwhile, summer vacation for Japanese students is two weeks long, and a large amount of homework is typically assigned.) Accidents of the calendar and various events can cause Golden Week to be longer -- for instance, in 2019, the ascession of the new emperor lengthened Golden Week to the point that some journalists worried that it would negatively impact students' retention of material. The Japanese school year ends just before Golden Week and begins just after it. {/i}In-universe{i}, Yomiyama Academy adopts the trend of Japanese private schools modeling themselves on western private schools. This manifests as Yomiyama Academy not having Golden Week off -- which is probably not accurate or believable, but allows us to use the western pagan year wheel in conjunction with a story set in a Japanese school.

{b}Halfu{/b} - a term for people who are of mixed race (typically with one Japanese parent and one non-asian parent -- most frequently used to refer to folks who are half-white). The halfu are exoticized within Japan, subject to both explicit and subtle racism. It is often assumed that they did not grow up in Japan, or that they cannot speak Japanese. There is a stereotype that halfu women are exceptionally beautiful, and so they are fetishized sexually.

{b}Halloween{/b} - Halloween is seen as a western holiday, and trick-or-treating is unusual, but starting in the late 90s, local yakuza syndicates began to hold annual Halloween parties for residents of their turf as a PR move.

{b}Kitsuneki{/b} - to be bewitched or possessed by a fox. This is sometimes used as an old-fashioned euphemism for mental illness (especially a psychotic break) but is also sometimes used more literally, referring to various phenomena including what westerners would refer to as being 'elf-led', 'demonically possessed', or 'kidnapped by the fair folk'. There is a more specific term, kitsunekushi, for being spirited away by foxes. The supernatural fox has an complicated place in Japanese myth, and so references to foxes have subtext of sexual seduction, madness, magic, and deception.

{b}One does not care to acknowledge the mistakes of one's youth{/b} - this is a translation of a famous line by Char Aznable, the antagonist of the original Gundam series. While in context he is describing a risky but successful military operation for which he retrieved substantial recognition, it became used in anime otaku circles as a tongue-in-cheek way of talking about now-embarassing fandom. This use can be seen in action in the second episode of {/i}Otaku no Video{i}.

{b}Parental absence{/b} - Working adults in Japan work substantially longer hours than westerners of all stripes. Unionization is extremely rare, worker's rights legislation is weak and rarely enforced, and social conventions around respecting one's superiors encourages a lot of unpaid overtime (since it's rude to go home before your boss does). Additionally, it's common for major decisions to be made during informal after-work meetings at bars, where the pressures to avoid insulting superiors are lowered or somewhat ignored. This means that working adults don't spend a lot of time at home. While married women still very often become housewives, those who stay in the workforce are still subject to these same pressures. So, it isn't entirely unrealistic for children whose parents both work to be latch-key kids to a substantially greater degree than in the west (with parents getting home after midnight and leaving before breakfast), though this is often exaggerated for story reasons in anime.

{b}Profanity{/b} - rather than the use of dedicated curse words, one should probably read the use of profanity here as an english rendering of what, in Japanese, would merely be rude and uncouth language. Ai, specifically, speaks like the stereotype of a 70s juvenile delinquent.

{b}School debut{/b} - a recurring trope in anime is the attempt to change one's personal image when transitioning from junior high to high school. Students often go to a high school unconnected to their middle school (even when it's a public school), based on academic performance, entry test results, and the subjects they would prefer to focus on, so high school is often a very different set of peers than middle school. Some students try to drastically change their image for the first day of high school, and going overboard with this is a common gag.

{b}Senpai{/b} - an honorific applied to someone older or more experienced, usually indicating admiration.

{b}Structuralism{/b} - a school of philosophy built around an extension of ideas from semiotics. Structuralism deals with the limits of knowledge as produced by the limits of language, which in a semiotic framework is seen as part of a web of associations. Much of 'postmodern' philosophy is in response to structuralism.

{b}Sukeban{/b} - literal translation is something like {/i}girl boss{i}. The term technically refers to the leader of an all-girl gang, but it's strongly tied to a specific subculture of girl gangs that actually existed in some capacity from the late 1960s to the late 1970s, and any member of such a gang or anyone who adopts their distinctive style of dress -- school uniforms with extremely long skirts worn outside of school, carrying a wooden sword -- is commonly referred to as {/i}sukeban{i}. Sometimes also associated with the (very different) style of all-girl motorcycle gangs. The male version is a {/i}bancho{i}.

{b}Yakuza{/b} - Japanese organized crime. For historical reasons related to the development of the criminal justice system and the transition from feudal rule, organized crime syndicates are tolerated substantially more in Japan than elsewhere -- by the police, because they crack down on {/i}dis{i}organized crime and because Japanese police are notoriously corrupt, by politicians, because the yakuza syndicates form the backbone of local political campaigning organization, and by businesses, who often remain tied up deeply with their loans and protection rackets even after becoming successful. Most of the yakuza money is in legal or grey-legal forms of gambling (such as pachinko) or in totally legal loans to large businesses (like Nintendo) these days, and violence against outsiders is relatively rare & taboo. So, the syndicates make efforts to portray themselves as legitimate businesses & gain the favor of citizens.

{b}Yomiyama{/b} - the town of Yomiyama does not exist. The name {/i}Yomiyama{i} translates to something like {/i}hades mountain{i}, and is also used in the gothic death game franchise {/i}Another{i}. In this game, however, the town of Yomiyama is a composite of several fictional locations from Japanese media: {/i}Hinamizawa{i} from the {/i}Higurashi no Naku Koro Ni{i} games, Fuyuki from the {/i}Fate{i} franchise, and the unnamed country town in Michio Yamamoto's {/i}The Vampire Doll{i} (1970). It is in a valley surrounded on all sides by mountains, and is now mostly suburban with a built-up 'down town' strip near the university. Until the university began pulling in big government contracts in the early 1990s, this was a much poorer and more rural town whose economic center was a small US military base, but for about twenty years it has been economically ascending, out of phase with the rest of Japan; this makes the local yakuza syndicate comparatively powerful. Since the source of its wealth is mostly-secret government research (by both the United States and Japan), it has resisted the trend in the rest of rural Japan to seek tourists and immigration, and most of the families there are either associated with the university or have been there since before the second world war.
{/i}

{b}Credits{/b}{i}

Concept, script, and programming by {a=http://www.lord-enki.net/}John Ohno{/a}

{b}Art{/b}
Art assets: John Ohno

{b}Music{/b}
{a=http://infocalypse.nfshost.com}Infocalypse{/a}
{/i}""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "BookoftheDamned"


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

define config.main_menu_music = "music/Infocalypse_-_The_Malibu.mp3"


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

define config.save_directory = "BookoftheDamned-1552075469"


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

# define build.itch_project = "renpytom/test-project"
