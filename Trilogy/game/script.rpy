define quote   = nvl_narrator
define comment = Character("COMMENT") # XXX delete this before launch

define ai    = Character("Akagi Ai", color="#000000")
define aoi   = Character("Tomoe Aoi", color="#0000af")
define mimi  = Character("Yamada Mimi", color="#ff7777")
define misato  = Character("Umeji Misato")
define akane = Character("Akane")

image street daylight = "street daylight.png"
image street rain 1 = "street rain1.png"
image street rain 2 = "street rain2.png"
image street rain dagashi = "street rain dagashi 1.png"
image dagashi outside = "dagashi outside.png"
image dagashi outside 2 = "dagashi outside 2.png"
image dagashi outside 3 = "dagashi outside 3.png"
image dagashi outside 4 = "dagashi outside 4.png"
image flame = "match1.png"
image flame2 = "match2.png"
image flame3 = "match light 1.png"
image flame4 = "match light 2.png"
image flame5 = "match light 3.png"
image flame6 = "light two candles.png"
image blowout = "candle blown out.png"
image dagashi interior dim = "dagashi interior dim.png"
image dagashi interior candle 1 = "dagashi interior candle 1.png"
image dagashi interior candle 2 = "dagashi interior candle 2.png"
image dagashi interior candle 3 = "dagashi interior candle 3.png"

$ achievement.register("Complete")

label story_start:
    stop music
    nvl clear
    scene black
    pause 0.1
    return

label story_end:
    stop music
    nvl clear
    scene black
    pause 0.5
    play sound "sfx/499020__16fthumaf__04-extinguishing-of-candle.wav"
    scene blowout
    pause 0.5
    scene black
    call rain
    pause 0.1
    return

label rain:
    play music "sfx/344430__babuababua__light-rain.mp3" volume 0.25
    return

label start:
    quote "\"I’ve given up fiction. Or in a way I haven’t. I am convinced that everything is fiction; so here I am in the same old line.\""
    quote "- Charles Fort, in private communication with Theodore Dreiser"
    stop music
    nvl clear
    scene black
    quote "June 22nd, 2012"
    scene street daylight
    ai "Shiiiit it's hottttt~~"
    show mimi smug at left
    mimi "That's because you're wearing a leather jacket..."
    show aoi akimbo at right
    "Aoi looks at them from her position crouched at the shop window and skips back over."
    show aoi hearteyes at right
    aoi "I like the jacket~"
    "Aoi grabs Ai's arm proprietarily and nuzzles her shoulder."
    show mimi angry at left
    mimi "..."
    play sound "sfx/114683__qat__whack02.mp3"
    ai "Ow!" with vpunch
    "Ai turns to whisper in Mimi's ear."
    ai "{fast}Ow!{nw}"
    play music "sfx/344430__babuababua__light-rain.mp3" volume 0.5 fadein 5.0
    extend " {size=-10}{i}You didn't have to do that; it's not my fault!{/i}{/size}"
    mimi "{size=-10}{i}Sure it is! If you were honest with her, she wouldn't keep doing it!{/i}{/size}"
    show aoi akimbo at right
    aoi "Hey~~~ What are you whispering about~~"
    show aoi blush at right
    extend " {size=-10}{i}I wanna hear secrets too~~~~~{/i}{/size}"
    show aoi at right
    "Aoi pauses and holds her hand up."
    scene street rain 1
    play music "sfx/344430__babuababua__light-rain.mp3" volume 1.5 fadein 5.0
    show aoi blush at right
    aoi "Hau~~ It's raining~~~"
    hide aoi
    "Aoi runs in wide lazy circles, trying to catch raindrops on her tongue."
    aoi "Hahahaha!"
    "She sees a puddle, steadies herself dizzily, and crouches. Then, she sprints toward it and jumps, with a big splash!"
    aoi "Wheee~"
    show mimi pensive
    mimi "Should we find some cover?"
    ai "Nah, let her have her fun."
    mimi "If it keeps up, this dress is gonna get soaked."
    ai "Aoi's already is -- look."
    show mimi angry
    "Mimi looks, and then turns away, blushing."
    play music "sfx/344430__babuababua__light-rain.mp3" volume 1.5
    scene street rain 2
    show mimi
    mimi "It's getting worse..."
    ai "Yeah... I don't think there's anywhere up here to shelter, but if we keep going straight, we should reach the train station."
    show mimi angry
    mimi "That's like half a mile away!"
    ai "The nearest shelter in the other direction is further."
    show mimi
    mimi "... Why did I ever agree to window-shopping in the rainy season?"
    ai "{size=-10}{i}To see Aoi in her new dress and boots.{/i}{/size}"
    show mimi pensive
    mimi "..."
    show mimi
    extend " {size=-10}{i}Fair enough.{/i}{/size}"
    ai "Come on, Aoi. We're gonna go up the street and look for shelter."
    show aoi akimbo at right
    aoi "Awww~ I was having fun..."
    ai "You won't be having much fun when you're recovering from a head cold."
    show aoi blush at right
    aoi "Alright~~"
    scene street rain dagashi
    mimi "I don't remember this being here..."
    scene dagashi outside
    ai "Who gives a flying fuck? It's open, and I'm wetter than a witch's cunt already, so let's go in."
    "The three of them go inside, into the dark."
    call rain
    scene black
    pause
    scene dagashi outside
    pause 0.5
    scene dagashi outside 2
    pause 0.5
    scene dagashi outside 3
    pause 0.5
    scene dagashi outside 4
    pause
    scene black
    play sound "sfx/match_strike.wav" volume 10.0
    pause 3
    stop sound
    play sound "sfx/match_light.wav" volume 10.0
    scene flame
    pause 0.1
    scene flame2
    "Suddenly, a burst of flame appears!"
    scene flame3
    pause 0.1
    scene flame4
    "A face is illuminated by a match,"
    scene flame5
    extend "and a candle is lit."
    scene dagashi interior dim
    show akane
    show misato at right
    misato "Oh, Akagi-san! And Yamada-san, and Tomoe-san too! Good day to you all!"
    scene dagashi interior candle 1
    "Akane puts the candle down on the table."
    show misato
    misato "Akane, this is Akagi Ai-san in the jacket, and Yamada Mimi-san, and Tomoe Aoi-san in the pretty dress."
    show akane at right
    akane "Yo."
    show mimi at left
    mimi "Pleased to meet you, miss... I'm sorry, I didn't catch your full name."
    akane "Just Akane. Like Danzig."
    ai "..."
    misato "... These girls are in my class at the Academy."
    hide mimi
    show aoi at left
    "Misato turned to Aoi, who has been darting all over the room looking at all the candy, then turns to Ai."
    hide aoi
    misato "Akane and I live together."
    ai "..."
    show mimi at left
    mimi "..."
    "Mimi fidgets with her skirt."
    hide mimi
    show aoi at left
    aoi "Oh!"
    play sound "sfx/114683__qat__whack02.mp3"
    "A pile of candles fall to the floor with a crash, and everyone looks to Aoi."
    show aoi akimbo at left
    aoi "Sorry~"
    "Ai goes over to help Aoi put them back, and after a moment, Mimi joins."
    misato "... Geez, this rain really isn't letting up, isn't it?"
    "..."
    scene dagashi interior candle 1
    show akane
    play sound "sfx/114683__qat__whack02.mp3"
    akane "I have an idea!" with vpunch
    "All eyes look to Akane, who has one booted foot on the table."
    akane "Hyaku-monogatari!"
    show aoi at left
    aoi "Hyaku-whatsit?"
    show mimi at right
    mimi "You mean, scary stories?"
    ai "Well, it is still fucking hot, despite the rain. It'd be nice to have something spooky to chill our bones."
    misato "That's brilliant, Akane. It'll pass the time, and we can get to know each other a little better."
    aoi "But we don't have time for a hundred..."
    akane "How about..."
    scene flame6
    "Akane lights two more candles from the first."
    akane "... just three?"
    scene dagashi interior candle 3
    "..."
    show mimi
    mimi "... I've got one."
    show akane at right
    "Akane puts her foot back down, leans in, and nods."
    mimi "This one is called... {b}{k=2}T{size=-5}HE{/size} L{size=-5}AZARUS{/size} P{size=-5}OSE{/size}{/k}{/b}."
    call story_start
    call lazarus_pose
    call story_end
    scene dagashi interior candle 2
    ai "Well, that was a Mimi story if I ever heard one."
    misato "How so?"
    ai "Who else would tell a scary story with a journalist protagonist?"
    akane "Dario Argento."
    ai "Ok, well who else would tell it in the form of a newspaper article?"
    akane "Bram Stoker."
    "..."
    akane "Or Stephen King."
    "..."
    misato "..."
    misato "Okay, who's next?"
    akane "I'll go."
    ai "Good, because I don't have one yet."
    "Akane stands up, looming over them, and puts one foot on the desk again, leaning in."
    akane "For the benefit of the summer storm society..."
    play sound "sfx/114683__qat__whack02.mp3"
    akane "{b}{k=2}T{size=-5}HE{/size} H{size=-5}OUSE{/size} {size=-5}ON{/size} F{size=-5}OULNESS{/size}{/k}{/b}" with vpunch
    call story_start
    call house_on_foulness
    call story_end
    scene dagashi interior candle 1
    aoi "So what happened to the little wormies? Are they okay??"
    akane "The worms always prevail in the end."
    aoi "But the fire?"
    mimi "Worms are like insects -- they produce lots of young so that losing a couple isn't a big deal."
    "Aoi pauses, a pensive look on her face."
    aoi "I still think that it might hurt."
    misato "You're a very kind person, aren't you, miss Tomoe?"
    aoi "hehehe~"
    "..."
    ai "Ok, so I still don't have any--"
    aoi "I'll go next!"
    ai "You'll g..."
    misato "You have something?"
    aoi "Yeah, I got all..."
    "Aoi grimaces, trying to think of the word."
    aoi "{fast}Yeah, I got all...{nw}"
    extend " inspired~~~"
    akane "I wanna hear this..."
    mimi "I'm looking forward to it!"
    aoi "This one is called..."
    akane "..."
    misato "..."
    mimi "..."
    ai "..."
    aoi "{b}{k=2}S{size=-6}HE{/size} A{size=-6}WAITED{/size} {size=-6}THE{/size} T{size=-7}URKEYS{/size}{/k}{/b}"
    call story_start
    call turkeys
    call story_end
    stop music fadeout 10.0
    scene dagashi interior dim
    misato "Well that was..."
    mimi "... grim."
    aoi "heh heh~"
    ai "Yeah! You really got the spirit of the exercise!"
    "Akane stared blankly at the wall."
    "Misato caught her eye."
    stop music
    jump end


image newspaper = "newspaper.png"
image rocket = "rocket.png"
image twitter = "twitter.png"
image siberia = "siberia.png"
image hole = "hole.png"
image daisychain = "daisychain.png"
image hole3 = "hole3.png"
image sat = "sat.png"
image cold_war = "coldwar.png"
image ancient_aliens = "ancientaliens.png"

label lazarus_pose:
    scene black
    quote  "T{size=-5}HE{/size} L{size=-5}AZARUS{/size} P{size=-5}OSE{/size}"
    nvl clear
    scene  newspaper
    quote  "{font=uwch.ttf}February 23, 2025{/font}"
    nvl clear
    quote  "{font=uwch.ttf}Two weeks ago, when the first manned ship to Mars exploded, even if nation states wanted to cover it up, such a thing would be impossible.{/font}"
    quote  "{font=uwch.ttf}The scale and suddenness of this event exposed the the internet cranks' claims of international conspiracy as wishful thinking.{/font}"
    quote  "{font=uwch.ttf}Much speculation about the evidence caught on radar and sattelite imagery has occurred, but to my knowledge, I am the only one to directly investigate the black squares.{/font}"
    nvl clear
    scene  rocket
    quote  "{font=uwch.ttf}Let me first reiterate the obvious:{/font}"
    quote  "{font=uwch.ttf}The Heart of Gold was the largest, fastest space vehicle humans have ever built by a large margin, and took a great deal of time and capital.{/font}"
    quote  "{font=uwch.ttf}It was one month into the three month trip.{/font}"
    quote  "{font=uwch.ttf}The things that intercepted it were of comparable size, and the time from when the squares in Siberia and the Outback first appeared and impact was only twenty minutes.{/font}"
    quote  "{font=uwch.ttf}This was not part of the abandoned Soviet Dead Hand interception system; the Soviets could not have built a device this size.{/font}"
    nvl clear
    scene  twitter
    quote  "{font=uwch.ttf}I got lucky: I was on Twitter when the news hit.{/font}"
    quote  "{font=uwch.ttf}I immediately booked a red-eye flight to Siberia; after all, the Australian square would be much harder to travel to. I bought every drone for sale in the airport mall.{/font}"
    nvl clear
    scene  siberia
    quote  "{font=uwch.ttf}The Siberian square, like the Australian one, was about a mile across.{/font}"
    quote  "{font=uwch.ttf}When it opened, it caused a building above it to collapse.{/font}"
    quote  "{font=uwch.ttf}I imposed upon the landlord of this building; luckily, there were no tenants at the time, though the landlord suspects that some squatters may have been lost.{/font}"
    nvl clear
    scene  hole
    quote  "{font=uwch.ttf}With a hole a mile across, it's reasonable to expect quite a bit of depth.{/font}"
    quote  "{font=uwch.ttf}The scale of the things launched from here gave me a bit of an estimate: at least 800 feet.{/font}"
    quote  "{font=uwch.ttf}I modified the drone firmware so that each drone could act as a signal repeater for the next one in the chain.{/font}"
    quote  "{font=uwch.ttf}I also added a ping function as a means of estimating depth, although with slow microcontrollers like those in the drones there's a margin of error of about 2\%.{/font}"
    nvl clear
    scene  daisychain
    quote  "{font=uwch.ttf}My daisy chain of drones demonstrated that the square extended straight down about 200 feet, with some indication of shear stress on the edges for the first 25 feet below the rockhead.{/font}"
    quote  "{font=uwch.ttf}After 200 feet, the space opened up: my drone's cameras, radar, and sonar all couldn't find edges.{/font}"
    quote  "{font=uwch.ttf}There wasn't much to see, other than a lot of dust.{/font}"
    quote  "{font=uwch.ttf}About a hundred feet lower, some debris (presumably from the collapsed buildings) sat atop a blunt cone made of a material that resembles smooth concrete.{/font}"
    quote  "{font=uwch.ttf}I had my lead drone land on the cone to get a closer look.{/font}"
    nvl clear
    scene  hole3
    quote  "{font=uwch.ttf}From the perspective of the tip of the cone, I could see a vast grid of similar cones in all directions.{/font}"
    quote  "{font=uwch.ttf}However, the lead cone (and others) began to move; tremors made the building I was staying in become unstable, and I had to flee.{/font}"
    quote  "{font=uwch.ttf}Unfortunately, my recordings were lost when the building collapsed on top of my computer, during the square's closure.{/font}"
    nvl clear
    scene  sat
    quote "{font=uwch.ttf}From public sattelite imagery, it seems that the other square closed during the same two hour window; I suspect that it actually closed simultaneously.{/font}"
    nvl clear
    scene  cold_war
    quote  "{font=uwch.ttf}With regard to the mystery of the squares and the tragic demise of our Martian colonists, it is my position that history has repeated itself.{/font}"
    quote  "{font=uwch.ttf}The Soviet dead hand system accidentally recapitulated, in some small way, an antedeluvian drama that once occurred between Earth and Mars, long before the age of man.{/font}"
    quote  "{font=uwch.ttf}We have finally reached the level of technological development necessary to become pitted against our forebears, who while not human were also people of Earth.{/font}"
    quote  "{font=uwch.ttf}However, their defenses are far beyond what we can reasonably wish to escape.{/font}"
    nvl clear
    quote  "{font=uwch.ttf}How long will we be trapped on this planet by the nervous twitches of a long-dead race?{/font}"
    quote  "{font=uwch.ttf}The thousands of cyclopean missiles beneath the Siberian tundra are our formidable jailers, along with similar stockpiles who knows where else.{/font}"
    quote  "{font=uwch.ttf}We cannot leave the cradle of earth until we outwit them.{/font}"
    quote  "{font=uwch.ttf}Yet, even something as simple as the door mechanism for this defense system is centuries beyond our technology.{/font}"
    quote  "{font=uwch.ttf}Even the very existence of a race who could build such things is beyond the current reach of our archaeology.{/font}"
    nvl clear
    scene  ancient_aliens
    quote "{font=uwch.ttf}Who were the figures in this ancient drama?We have been presented with a mystery whose clues will be inaccessible for the forseeable future.{/font}"
    nvl clear
    return

label house_on_foulness:
    scene black
    quote  "T{size=-5}HE{/size} H{size=-5}OUSE{/size} {size=-5}ON{/size} F{size=-5}OULNESS{/size}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}2nd April, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}Dearest Mary,{/font}"
    quote  "{font=AquilineTwo.ttf}It might seem childish of me to keep writing this diary in the form of letters to you after so many years, but I am still working toward our promise in my own way.{/font}"
    quote  "{font=AquilineTwo.ttf}Perhaps, by the time I get to Paris, you will already be there — perhaps the streets will no longer be full of dull bureaucrats!{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I have taken the position of governess to a pair of children, at an estate on the coast, in a town called Foulness.{/font}"
    quote  "{font=AquilineTwo.ttf}What a queer name! I shall be travelling there for most of tomorrow.{/font}"
    quote  "{font=AquilineTwo.ttf}In this way, I squirrel away savings for the trip.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}3rd April, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}My dearest Mary,{/font}"
    quote  "{font=AquilineTwo.ttf}Foulness is indeed an appropriate name! The stench of the neighbouring salt marsh pervades this town, and those strange oversized marsh insects buzz in tight circles in every corner of the town.{/font}"
    quote  "{font=AquilineTwo.ttf}It is uncomfortably hot in the sun and uncomfortably cold in the shade.{/font}"
    quote  "{font=AquilineTwo.ttf}The people here look wind-beaten.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}The estate where I will be working is on a small rocky island across the marsh, and a low bridge of stones apparently connects it to the town proper, though this is now covered by the tides.{/font}"
    quote  "{font=AquilineTwo.ttf}There is no ferry out, and no dock on the other side.{/font}"
    quote  "{font=AquilineTwo.ttf}I will be taking that bridge in the morning.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}4th April, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}Mary,{/font}"
    quote  "{font=AquilineTwo.ttf}At long last, I have arrived at the estate proper — just as the maid was leaving.{/font}"
    quote  "{font=AquilineTwo.ttf}I presume that the bridge is so low as to be submerged most of the time, and the household is careful to cross in and out of town as close to low tide as possible so as to not be caught out.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}The stench out here is stronger, and animals and sea life sometimes die on the rocks, lending their own unique spices to the already-thick sea air during the warm parts of the day.{/font}"
    quote  "{font=AquilineTwo.ttf}As I came up to the stone staircase leading from the low bridge to the main building, I saw the corpse of a gull on a nearby rock, its eyes crawling with maggots.{/font}"
    quote  "{font=AquilineTwo.ttf}I saw a figure clambering on the rocky piles beyond, running back behind the house.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I later determined that this must have been the boy, Terence, who is twelve — that age when boys make sport of poking dead things with sticks.{/font}"
    quote  "{font=AquilineTwo.ttf}He does not seem abnormally unruly for a boy of twelve.{/font}"
    quote  "{font=AquilineTwo.ttf}His sister, Anna, is only four but preternaturally calm.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I introduced myself to the children — the maid is the only other member of the household staff, and she sleeps in town, and meanwhile, the master of the house is still involved in his work in London — and got to preparing meals for them.{/font}"
    quote  "{font=AquilineTwo.ttf}Although the kitchen has been cleaned, the pantry is emptied of anything that could be eaten without cooking — I wonder how long the children have been fending for themselves here.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}5th April, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}Dearest Mary,{/font}"
    quote  "{font=AquilineTwo.ttf}My bedroom is cold and drafty during the night, and gusts of wind kept me awake late, but when finally I fell asleep I dreamt of good times with you before the war.{/font}"
    quote  "{font=AquilineTwo.ttf}Paris was not the only foolish youthful promise we made in the woods that summer! I had forgotten all the others.{/font}"
    quote  "{font=AquilineTwo.ttf}I don't know what prompted all those memories to return.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I awoke early, my cold and drafty room becoming hot and stale shortly after sunrise, and so I was able to catch the maid, a Mrs Grant, before she left.{/font}"
    quote  "{font=AquilineTwo.ttf}She informed me that the reason there is no ferry and no dock here is that the tides would smash them against the island — and from the sounds I heard last night, I believe it!{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}She also told me that Master Marsten had moved to London at the beginning of the war, like your father did.{/font}"
    quote  "{font=AquilineTwo.ttf}She said that the house was built by some eccentric ancestor — a gentleman-scientist who fancied himself an authority on salt-marsh wildlife (although his works were never accepted by the natural philosophers of the Royal Society and never had any kind of wide circulation).{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I suppose the seventeenth century had its cranks as well.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}She indicated that she was grateful that I wasn't like the previous governess, who she held in some low regard.{/font}"
    quote  "{font=AquilineTwo.ttf}Apparently, that woman was about my age & quickly became close to the children, only to suddenly disappear one day — leaving the children totally alone for some weeks before I could be hired.{/font}"
    quote  "{font=AquilineTwo.ttf}How irresponsible!{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I requested she pick up some groceries — eggs, fresh fruit and vegetables if she can find any, and flour, since the bag left here has been invaded by some unfamiliar marsh-insect.{/font}"
    quote  "{font=AquilineTwo.ttf}She will bring them tomorrow morning.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}Other than feeding the children and keeping one eye on their adventures on the rocks, I spent the remainder of the day acquainting myself with the house.{/font}"
    quote  "{font=AquilineTwo.ttf}It has no basement, but it's larger than it looks from the outside — an octagonal assemblage of rooms piled together like the rock walls it perches on, with a staircase wrapped around the inside of one wall.{/font}"
    quote  "{font=AquilineTwo.ttf}Most rooms are empty, only storing sheet-draped furniture.{/font}"
    quote  "{font=AquilineTwo.ttf}In a few places, there were signs of water damage behind and below the radiators; I must remember to ask Mrs Grant about fungicide.{/font}"
    quote  "{font=AquilineTwo.ttf}One small door set into the wall at the top of the stairway is locked, and I cannot for the life of me imagine where it goes — I will ask about that as well.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}The children's play is strange — though I imagine it must have been borne out of siblings of such different ages being alone together for so long with nothing to do.{/font}"
    quote  "{font=AquilineTwo.ttf}Terence scrambles among the rocks with a stick in one hand, while Anna sits and watches, seeming to give him commands.{/font}"
    quote  "{font=AquilineTwo.ttf}How Terence manages to scramble so all day, in such oppressive heat, is beyond my comprehension.{/font}"
    quote  "{font=AquilineTwo.ttf}Were we so energetic when we were young?{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}This must have been the game he was playing when I first came, as well.{/font}"
    quote  "{font=AquilineTwo.ttf}Had Anna sent him to poke that dead bird? She's such a calm and sweet girl that the notion seems absurd — but still, I cannot shake it.{/font}"
    quote  "{font=AquilineTwo.ttf}Her calmness remains when she plays this game, but something else — a kind of commanding authority, and not a child's play-act of authority — comes through in her face.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}After supper, the children and I sat by the little stove in the centre of the ground floor landing and I read them a story.{/font}"
    quote  "{font=AquilineTwo.ttf}Then, Anna said something strange.{/font}"
    quote  "{font=AquilineTwo.ttf}She said, \"Mama says she likes you.\"{/font}"
    quote  "{font=AquilineTwo.ttf}Young children often have vivid imaginations, and so I dismissed it, but her face had that same seriousness.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}6th April, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}When Mrs Grant came (thankfully hauling flour and eggs, although no fruit and only some meagre-looking withered vegetables unsuitable for pickling), I asked her if Anna had been close to her mother.{/font}"
    quote  "{font=AquilineTwo.ttf}\"Oh dear no,\"she said. \"Mrs Marsten, god rest her soul, died giving birth to Anna, who never knew her mother.\"{/font}"
    quote  "{font=AquilineTwo.ttf}This lifted a weight from my heart.{/font}"
    quote  "{font=AquilineTwo.ttf}Anna is not seeing her mother out of trauma — she has no concept of what it's like to have one, and so an imaginary mother is no different from an imaginary aardvark or some other fantastical creature a child might pretend about.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}Mrs Grant also lifted my spirits with regard to the water damage from the radiators, saying that the house is mostly cedar and gets far worse from the surf — everything dries out in the summer, when it is even hotter during the day than it is now, and the copper roof practically bakes the steam out of the whole house.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}Terence was even busier at Anna's game today than usual.{/font}"
    quote  "{font=AquilineTwo.ttf}When the wind was right, I heard her preface her orders with something like \"Mama says\".{/font}"
    quote  "{font=AquilineTwo.ttf}Perhaps this is not an imaginary friend at all, but merely a part of the game they invented together.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}The activity, in this heat, must have been too much for Terence.{/font}"
    quote  "{font=AquilineTwo.ttf}Around sundown, I went to call them in, and only Anna came.{/font}"
    quote  "{font=AquilineTwo.ttf}I asked where Terence was and she said, \"still on the rocks\".{/font}"
    quote  "{font=AquilineTwo.ttf}I let him play for a little while longer, but darkness fell quicker than I expected, so I gathered up a lamp & went out to look for him.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I found him laid out on one of the stone steps, the water line up to his ears, flushed and warm to the touch, & carried him in.{/font}"
    quote  "{font=AquilineTwo.ttf}As I did, I thought I saw a light in the small parapet atop the roof.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I tended to his fever with cool, damp rags, until Anna told me \"Mama said use the paracetamol\".{/font}"
    quote  "{font=AquilineTwo.ttf}I did, and his fever broke, though he didn't wake up.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}April 6th, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}Mary,{/font}"
    quote  "{font=AquilineTwo.ttf}Last night, below the gusts of wind, the waves against the rocks, and the groans of the shifting house, I thought I heard a soft, clear voice as I fell asleep.{/font}"
    quote  "{font=AquilineTwo.ttf}While it disturbed me, it didn't keep me awake, and I dreamt of you again.{/font}"
    quote  "{font=AquilineTwo.ttf}I had forgotten the reason we met in the woods that summer, and how cruelly your father was treating you.{/font}"
    quote  "{font=AquilineTwo.ttf}I think I was too young to understand the extent of it at that time.{/font}"
    quote  "{font=AquilineTwo.ttf}I naively thought friendships formed in a vacuum, and that our connection was the result of some shared piece of soul between us, but probably at that time the woods and my companionship were your sanctuary.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I checked on Terence, whose temperature was rising only a little, and roused him into a state of half-wakefulness to give him additional paracetamol, after which he lapsed back into slumber.{/font}"
    quote  "{font=AquilineTwo.ttf}I noticed his skin was a little greasy & that he was beginning to develop pimples on his cheeks.{/font}"
    quote  "{font=AquilineTwo.ttf}He is an adolescent after all, but I hadn't noticed these things earlier in the week, even when ensuring his face and hands were properly washed for supper.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I told Mrs Grant about Anna's strange prescription, and she looked slightly disturbed.{/font}"
    quote  "{font=AquilineTwo.ttf}She said, \"Anna never called her mother ‘Mama'.\"{/font}"
    quote  "{font=AquilineTwo.ttf}After all, she had never had a mother.{/font}"
    quote  "{font=AquilineTwo.ttf}Instead, that had been Anna's pet name for the previous governess, who had come nearly four years ago and stayed until recently.{/font}"
    quote  "{font=AquilineTwo.ttf}\"Mama Mary.\"{/font}"
    quote  "{font=AquilineTwo.ttf}I did not say that I had a childhood friend named Mary; it is, after all, a common name!{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}Mrs Grant will be off on holiday for the next two days, so she stayed a little later than usual to ensure the house was cleaned up.{/font}"
    quote  "{font=AquilineTwo.ttf}She even helped me a little with the pie I was baking (using a couple rusty cans of fruit that nevertheless smelled edible).{/font}"
    quote  "{font=AquilineTwo.ttf}She stayed late enough that she had to pick up her skirts to walk back to the mainland! A small part of me wished she had stayed until the tide hit the high water mark on the stone steps, about half a foot above my head, and that she would need to stay the night.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}After Mrs Grant left, Anna continued ordering me about — \"Mama says fill the bathtub with cold water\", \"Mama says take in all the towels off the line\".{/font}"
    quote  "{font=AquilineTwo.ttf}I played along.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I must have tired myself out, because I found myself dozing before the stove late in the evening, after I would have normally gone to bed.{/font}"
    quote  "{font=AquilineTwo.ttf}I heard a creaking above me, and a pair of soft voices from the radiator.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}One was rambling on and on and periodically giving orders, while the other was giving short responses.{/font}"
    quote  "{font=AquilineTwo.ttf}I identified the one giving short responses as Anna.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}\"{i}We have always lived here in tune with the cycle of the waves and the cycle of the tides and we have always let them burst into the waters when they are ripe,{/i}\" said the rambler.{/font}"
    quote  "{font=AquilineTwo.ttf}There was a creak and a scraping sound above me.{/font}"
    quote  "{font=AquilineTwo.ttf}\"{i}You are not of age but you can feel this truth inside you.{/i}{/font}"
    quote  "{font=AquilineTwo.ttf}{i}{space=1}You must let him ripen and the seeds burst out into the water.{/i}{/font}"
    quote  "{font=AquilineTwo.ttf}{i}{space=1}Do not be afraid of it.{/i}{/font}"
    quote  "{font=AquilineTwo.ttf}{i}{space=1}He will burst so that you will not.{/i}{/font}"
    quote  "{font=AquilineTwo.ttf}{i}{space=1}It is only his blood that is wrong.{/i}{/font}"
    quote  "{font=AquilineTwo.ttf}{i}{space=1}He cannot become one of us.{/i}{/font}"
    quote  "{font=AquilineTwo.ttf}{i}{space=1}When he is ripened, let him go.{/i}\"{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}The rambler went on and on like this, and I tried to transcribe more, but the more closely I listen to the echoes in the radiator, the sleepier I get.{/font}"
    quote  "{font=AquilineTwo.ttf}Perhaps I, too, have become feverish and delirious? I will finish this letter and go to bed.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}April 7th, 1919{/font}"
    quote  "{font=AquilineTwo.ttf}Mary,{/font}"
    quote  "{font=AquilineTwo.ttf}Late last night, awakened by Terence's cries, I discovered the meaning of Anna's preparations.{/font}"
    quote  "{font=AquilineTwo.ttf}His fever had gotten worse — far worse — and he was squirming, his muscles spasming.{/font}"
    quote  "{font=AquilineTwo.ttf}I remembered that the tub was still full of cold water, and being unable to get him to swallow the paracetamol, I carried him there.{/font}"
    quote  "{font=AquilineTwo.ttf}But, as soon as his torso was submerged, it split open like a pomegranite, white pips floating to the surface.{/font}"
    quote  "{font=AquilineTwo.ttf}His skin was a thin shell, muscle eaten away and full of small holes, with nothing inside but bones and these squirming white worms that now rushed out.{/font}"
    quote  "{font=AquilineTwo.ttf}They burbled under the skin on his unsubmerged limbs and face, while the others floated or clung to the edges of the tub.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I heard the front door open, and the worms began evacuating his body, pouring out of the tub onto a line of fresh, dry towels laid out on the floor — a pathway to the doorway, where Anna stood in her nightgown in the pouring rain.{/font}"
    quote  "{font=AquilineTwo.ttf}I watched them march out, down the steps, and into the moonlit marsh clay, which had risen up above the water line.{/font}"
    quote  "{font=AquilineTwo.ttf}The worms scattered out, created each a tiny hole, and dove in.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}\"Mama wants you to understand,\"Anna said.{/font}"
    quote  "{font=AquilineTwo.ttf}\"Mama is mama now, and Mary too, and even Papa's Mama.{/font}"
    quote  "{font=AquilineTwo.ttf}\"I was too shocked to respond.\"{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I climbed up the stairs to my room, and as I slipped into sleep, I heard the radiator calling my name, saying \"remember Paris, remember our promise before the war\".{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I was naive to hold on so tightly to a youthful promise.{/font}"
    quote  "{font=AquilineTwo.ttf}Paris is the domain of the Bluebeard of Gambais now, not some glamorous fantasy land of Byronic heroes and symbolist poets.{/font}"
    nvl clear
    quote  "{font=AquilineTwo.ttf}I took a shovel from the root cellar and destroyed Anna while she slept.{/font}"
    quote  "{font=AquilineTwo.ttf}Tonight, when the sun sets and your twisted, infected body can move again, I will do the same to you.{/font}"
    quote  "{font=AquilineTwo.ttf}This is the last letter I will write.{/font}"
    quote  "{font=AquilineTwo.ttf}In the morning, before Mrs Grant comes, I will take my shovel to London to finish the Marsten dynasty.{/font}"
    nvl clear
    return

label turkeys:
    scene black
    quote "S{size=-5}HE{/size} A{size=-5}WAITED{/size} {size=-5}THE{/size} T{size=-5}URKEYS{/size}"
    nvl clear
    quote "{font=JIANGKRIK.otf}The load-bearing wall groaned behind her. She would need to move again soon.{/font}"
    nvl clear
    quote "{font=JIANGKRIK.otf}Houses used to last a lot longer.{/font}"
    quote "{font=JIANGKRIK.otf}This was the third in as many weeks, and she had put off leaving for longer than was wise: the previous tenants had left furniture, and she had almost convinced herself that the smell of rotting carrion was actually the nearby sewage treatment facility.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}Taking a claw hammer from the pocket of her mangled overalls, she peeled some of the boards back from the doorjam.{/font}"
    quote  "{font=JIANGKRIK.otf}Covering her body with a plastic tub, she pushed her way through three or four feet of bloodied feathers and claws.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}The smell no longer bothered her, but without the tub she would be smothered before she could be crushed, and the tub provided valuable protection from the rain of small winged bodies as she made her way to her next shelter.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}This area was developed during the last real estate boom, and so almost any house she found would probably be abandoned.{/font}"
    quote  "{font=JIANGKRIK.otf}She risked a glimpse at the sky, but it was pointless — as usual, the sun was blotted out.{/font}"
    quote  "{font=JIANGKRIK.otf}For her efforts, she received a white-capped chickadee in the eye.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}When she was young, her parents and friends thought it was a blessing, and treated it like a parlor trick.{/font}"
    quote  "{font=JIANGKRIK.otf}They'd make jokes about Disney princesses and sing that Carpenters song.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}It wasn't until she was ten years old that the rate had accelerated to the point of being distressing.{/font}"
    quote  "{font=JIANGKRIK.otf}Her family had to replace the sliding glass doors on the porch with something opaque, and shortly afterward painted the outside of the house a dull rust color to hide the blood.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}When the roof of that house finally collapsed, they were still in denial, unprepared; only she escaped.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}She had been in this development for a year — or maybe two.{/font}"
    quote  "{font=JIANGKRIK.otf}It was hard to keep track anymore.{/font}"
    quote  "{font=JIANGKRIK.otf}The birds kept coming in thicker.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}She wore rubber rain boots that went up above her knees, tucked into her pants.{/font}"
    quote  "{font=JIANGKRIK.otf}Nevertheless, some songbirds, already mostly rotten, fell inside as she shuffled through some of the taller mounds and became squished between her leg and the inside of the boot, beaks and claws and little bones pressing into her flesh.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}As she pushed through a front door, she felt an unusually large thump on her tub: a hawk, maybe.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}She pushed the door closed, reinforcing it with boards and nails with a practiced ease.{/font}"
    quote  "{font=JIANGKRIK.otf}Then, satisfied, she turned around to survey the rest of the building.{/font}"
    quote  "{font=JIANGKRIK.otf}But, the back end of the house had already collapsed: she must have already stayed here!{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}She heard a banging to her left, and it jogged her memory.{/font}"
    quote  "{font=JIANGKRIK.otf}This was the place with the wild turkeys.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}She had thought having turkey would be nice — an easy meal.{/font}"
    quote  "{font=JIANGKRIK.otf}She had underestimated their strength.{/font}"
    quote  "{font=JIANGKRIK.otf}That time, she had barely escaped.{/font}"
    quote  "{font=JIANGKRIK.otf}She had been much stronger then — inside for nearly a month.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}Unable to imagine herself summoning the strength to pull out the boards and trudge through another deluge, she slumped, her back against the door.{/font}"
    nvl clear
    quote  "{font=JIANGKRIK.otf}She awaited the turkeys.{/font}"
    nvl clear
    return

label end:
    misato "Hey..."
    akane "The rain stopped."
    ai "Good. It's gotten dark and creepy in here."
    ai "I feel like spiders are crawling all over my arms."
    mimi "Too much information."
    "Aoi stood up suddenly and bolted for the door."
    aoi "Wheee~~~"
    "The others followed more slowly, yawning and stretching."
    scene dagashi outside
    pause
    scene street daylight
    pause 0.1
    scene dagashi outside 4
    pause 0.1
    scene street daylight
    "Everyone turned around to look, but the old dagashi shop was gone."
    call credits
    return

label credits:
    window hide
    scene black with dissolve
    play music "sfx/344430__babuababua__light-rain.mp3"
    init python:
        import re
        name2url={
            "John Ohno": "http://www.lord-enki.net",
            "Ryusei": "http://glitch.social/@ryusei"
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


        sfx=[["babuababua", "344430", "light rain.mp3"],
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
            ["Background art", "John Ohno"],
            ["Sound effects", sfx_credit]
        ]
    $ showCredits(credits)

    window show
    return
