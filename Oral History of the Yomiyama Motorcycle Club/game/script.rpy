# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Interviewer")
define d = Character("Director")

define tanaka = Character("Tanaka")
define mori = Character("Mori")
define satou = Character("Satou")
define suzuki = Character("Suzuki")
define takahashi = Character("Takahashi")
define ito = Character("Ito")
define watanabe = Character("Watanabe")



# The game starts here.

label start:
    scene bg white
    d "testing 1... 2... ok we're rolling"
    scene recorder
    i "Speak clearly into the microphone please."
    d "Oral history of the Yomiyama Motorcycle Club, session one, take one."
    i "So, can you quickly summarize the history of your club?"
    # xxx characters start going on irrelevant tangents and correcting each other
    
    return
