﻿# The script of the game goes in this file.

label dream:
    play music "sfx/531015__noted451__ocean-waves.wav"
    scene nameless city
    "At the end of the nameless city,"
    play music "sfx/531015__noted451__ocean-waves.wav" volume 2
    scene silver gate
    extend " the silver gate."
    scene silver thread
    "Into the silver gate,"
    play music "sfx/531015__noted451__ocean-waves.wav" volume 3
    scene silver_key
    extend " the silver key."
    scene silver gate 2
    "Beyond the silver gate,"
    play music "sfx/531015__noted451__ocean-waves.wav" volume 4
    scene silver gate 3
    extend " the blood ocean."
    return

# The game starts here.

label start:
    call dream
    stop music
    scene black
    pause
    scene studio 1
    pause
    scene empty vial
    pause
    scene studio 1
    pause
    scene coat
    pause
    scene konbini
    "TV" "...ther news, this morning NASA scientists has lost contact with the Endevour for the first time."
    "TV" "The Endevour, launched thirty years ago today, was on track to be the first manned craft to reach the edge of the solar system."
    "TV" "The pilot of the craft, Tom Sh..."
    "Clerk" "Can I help you?"
    "I nod to the clerk. He nods back, and gestures behind him. I leave the store and walk around back to the alley."
    scene alley
    "Clerk" "Fifty."
    "I palm a crisp folded fifty into his hand, and he slips a vial into mine."
    scene full vial
    pause
    scene alley
    pause
    scene coat
    pause
    scene studio 1
    pause
    scene black
    pause
    call dream
    stop music
    scene black
    play music "sfx/531015__noted451__ocean-waves.wav" volume 0.1
    pause
    scene studio 2
    pause
    scene empty vial
    pause
    scene studio 2
    pause
    scene coat
    pause
    scene konbini
    "TV" "... Shephard had modifications in preparation for his trip. These experimental cybernetic enhancements, at the limits of space medi..."
    "Clerk" "Can I help you?"
    "I nod to the clerk."
    "Clerk" "..."
    "Clerk" "How can I help you."
    "..."
    "" "... blood ocean"
    "The clerk nods, and reaches onto the shelf behind him."
    "Clerk" "Ten bucks."
    scene full vial
    scene black
    pause
    scene coat
    pause
    scene studio 2
    pause
    scene black
    pause
    call dream
    pause
    play music "sfx/531015__noted451__ocean-waves.wav" volume 6
    scene silver gate 4
    pause
    stop music
    scene black
    play music "sfx/531015__noted451__ocean-waves.wav" volume 0.2
    pause
    scene studio 3
    pause
    scene empty vial
    pause
    scene studio 3
    pause
    scene coat
    pause
    scene konbini
    "TV" "... pressure-resistant prosthetic eyes,"
    scene tv
    extend " as well as sealing of all other orifices against the vacuum of..."
    scene konbini
    "Clerk" "Can I help you?"
    "" "... blood ocean"
    "Clerk" "On the display behind you."
    scene display_case
    pause
    scene konbini
    "Clerk" "Twenty-five cents."
    scene full vial
    pause
    scene black
    pause
    scene coat
    pause
    scene black
    pause
    scene studio 3
    pause
    scene black
    pause
    call dream
    pause
    play music "sfx/531015__noted451__ocean-waves.wav" volume 6
    scene silver gate 4
    pause
    play music "sfx/531015__noted451__ocean-waves.wav" volume 8
    scene silver gate 5
    "Tom Shepherd" "I have made contact with outsideness."
    play music "sfx/531015__noted451__ocean-waves.wav" volume 10
    scene silver gate 6
    "Tom Shepherd" "I have freed the blood ocean."
    play music "sfx/531015__noted451__ocean-waves.wav" volume 20
    scene silver gate 7
    pause
    return
