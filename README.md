# misc
things that don't deserve their own repo

mirrored on git-ssb at ssb://%peZat1oevgpj9Irwc/lToAh9pm5TiGsxM/MRM04RV4U=.sha256

Text generation or manipulation:

* [applyMapping.py](applyMapping.py): apply mapping created by buildVowelSubstitutionMap
* [buildVowelSubstitutionMap.py](buildVowelSubstitutionMap.py): create a random mapping of vowels
* [jepcah.py](jepcah.py): random Cards Against Humanity question card, with a random Jeopardy answer filled in
* [markov2tracery.py](markov2tracery.py): given a text file input, generate a tracery grammar that is a first order markov model of that file
* [junogenmo-2016](junogenmo-2016): Auxiliary National Novel Genration Month 2016
* [junogenmo-2018](junogenmo-2018): Auxiliary National Novel Genration Month 2018
* [nanogenmo-2016](nanogenmo-2016): National Novel Generation Month 2016
* [nanogenmo-2017](nanogenmo-2017): National Novel Generation Month 2017
* [nanogenmo-2018](nanogenmo-2018): National Novel Generation Month 2018
* [napogenmo2017](napogenmo2017): National Poetry Generation Month 2017
* [phrasechain](phrasechain): like a markov chain for phrases
* [scp.gg](scp.gg): grammar for generating a SCP wiki entry
* [typoize.py](typoize.py): introduce typos
* [verbal_inarticulations.json](verbal_inarticulations.json): a tracery grammar for filler words
* [disarticulate.py](disarticulate.py): apply typoize.py and also inject verbal inarticulations
* [X_except_its_Y.py](X_except_its_Y.py): use wordnet to semantically shift one text stream by another
* [colorByTF](colorByTF.py): produce an html document where the opacity of each word corresponds to its frequency (as a proxy for information content)

Novelty aggregators:

* [autopsy.sh](autopsy.sh): download random startup autopsy
* [cah.py](cah.py): random Cards Against Humanity pairing
* [jep.py](jep.py): random Jeopardy question/answer pair
* [kwotes.py](kwotes.py): tool to dump the semi-official memebomb database
* [memebombs.json](memebombs.json): tracery grammar containing a dump of [the semi-official memebomb database](http://principiadiscordia.com/memebombs)
* [salt.sh](salt.sh): download seminars on long-term thinking
* [salt.txt](salt.txt): list of seminars on long-term thinking
* [simile.sh](simile.sh): random simile
* [Holzertron](barbara_holzer.py): generate a Barbara Kreuger style image macro with a Jenny Holzer slogan (or one based on a different template)

Pretty pictures:

* [asemic.py](asemic.py): generate asemic writing
* [wreath.py](wreath.py): generate pretty christmas wreaths

Utilities:

* [ncgopher](ncgopher.py): curses-based gopher client
* [stupidrss](stupidrss.sh): the stupidest possible RSS reader: parse feeds with regex & dump the links to stdout using w3m
* [nam](nam): fall back from 'man' to other sources of documentation, like 'info', and eventually to wikipedia
* [scrambleExif](scrambleExif.sh): scramble or falsify EXIF data like date and geolocation
* [fake-mvgen](fake-mvgen.sh): create a new video track for a given audio track by picking random clips from a video corpus & applying random effects to them
* [choose.sh](choose.sh): pick an arg at random
* [extract-epub.sh](extract-epub.sh): turn an epub into a text file
* [list-dl.sh](list-dl.sh): download a playlist from youtube with helpful numbering
* [notes.sh](notes.sh): simple shell routines for taking short notes
* [links.sh](links.sh): simple shell routines for handling an archive of URLs (similar to a bookmarking service like postboard)
* [post](post): a tool to post short strings to multiple microblogging services at once
* [tpost](tpost): when posting to twitter, break long messages into threads
* [pbs](pbs): post to bluesky / ATProto. Includes making URLs into clickable links.
* [ssb-digest](ssb-digest.sh): post a message to secure scuttlebutt with the links added with [links.sh](links.sh) that day
* [randlinkd](randlinkd.sh): daemon to periodically post previously-archived links
* [unpopular-posts-only.user.js](unpopular-posts-only.user.js): greasemonkey script to hide tumblr posts with too many notes
* [update_checkouts.sh](update_checkouts.sh): update everything in the directory checked out with git or svn
* [fix_transmission.sh](fix_transmission.sh): set a parameter that sometimes causes transmission to fail to work with certain tracker/CDN combinations
* [RBG](rbg.sh): change the desktop background to a randomly selected image from one or more local directories, on a configurable delay 

Games (in progress):
* [Book of the Damned](Book%20of%20the%20Damned): taking place during the events of [Manna for our Malices](http://github.com/enkiv2/mannaforourmalices), this game follows young telepath Yumeji Misato as she is moved to a group home in Yomiyama by the leader of a UFO cult & deals with new friends, new enemies, and you, the player.

Games (finished):
* [Trilogy](Trilogy): after the events of [Manna for our Malices](http://github.com/enkiv2/mannaforourmalices) and [Book of the Damned](Book%20of%20the%20Damned), Akagi Ai and her friends get stuck in the rain with Yumeji Misato and Bruno Akane, and they tell ghost stories in this short non-interactive VN. [Moved here](https://github.com/enkiv2/trilogy)
* [Blood Ocean](Blood%20Ocean): a painter discovers that the dream-enhancing street drug Blood Ocean is not what it seems. [Moved here](https://github.com/enkiv2/bloodocean)

Misc:

* [medium-export](medium-export): archive of my medium posts
* [lordenki](lordenki): a backup of my website
* [README.md](README.md): this file
* [ds-lib](ds-lib): small python libraries for data structures or algorithms for which there are no readily-available open source implementations easily understood by beginners. [Moved here](https://github.com/enkiv2/ds-lib)
* [kamui](kamui): composable UI project in io, with 'senketsu' io interpreter in go
* [mtv](mtv): Minimal Transliterature Viewer -- a hypertext project on top of IPFS
* [vidsort](vidsort.py): sort a video by frame similarity and reencode
* [wokebroke.txt](wokebroke.txt): a list of dictionary words that rhyme with 'woke' and 'broke'
* [fortunes](fortunes): various fortune databases
* [templates](templates): various tracery templates

Moved:

* [yabot](yabot): [Yet Another irc chatBot](http://github.com/enkiv2/yabot)
* [Manna for our Malices](Manna for our Malices): [Manna for our Malices](https://github.com/enkiv2/mannaforourmalices)
* [fern](fern): [fern](https://github.com/enkiv2/fern)
