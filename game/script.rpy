# ===============================================
# script.rpy 
#
# to tu sie zaczyna
#
# le contents:
# GLOBAL CONFIGS
# INIT PYTHON
# CHARACTER DEFINITIONS
# GLOBAL VARIABLES
# TRANSFORMS
# START
# MISC
# ===============================================





# =============================================== GLOBAL CONFIGS
 
define config.default_text_cps = 110
define config.main_menu_music = "audio/ShouldersOfGiants.mp3"

# =============================================== INIT PYTHON
 
init python:
    import random

# =============================================== CHARACTER DEFINITIONS

define mks      = Character("MKS 23",       color="#fafafa")
define m        = Character("???",          color="#808080") # mystery speaker
define p        = Character("Piotr",        color="#a222be")
define f        = Character("Filip",        color="#a222be")
define k        = Character("Barbara K.",   color="#ff41c9")
define t        = Character("Tomcio",       color="#ec1f1f")
define v        = Character("Vasili",       color="#6a6277")
define wp       = Character("Wiktoria P.",  color="#9ace22")
define bjork    = Character("Björk",        color="#77beee")
define kura     = Character("Kura",         color="#e05a17")
define lis      = Character("LISa Simpson", color="#fffffa")
define frau     = Character("Frau Crusty",  color="#e266c7")
define r        = Character("Rafał",        color="#105da1")
define n        = Character("Niuniu",       color="#8410a1")
define ww       = Character("Wiktoria W.",  color="#f6517d")
define a        = Character("Antonius",     color="#52a88e")
define w        = Character("Wiesław",      color="#843a18")
define b        = Character("Bartosz",      color="#3ab954")
define pe       = Character("Petitty",      color="#abcdef")


# =============================================== GLOBAL VARIABLES
 
default friendship = {
    "Piotr": 0,
    "Filip": 0,
    "Kurowska": 0,
    "Tomcio": 0,
    "Vasili": 0,
    "Björk": 0,
    "Kura": 0,
    "LISa Simpson": 0,
    "Frau Crusty": 0,
    "Rafal": 0,
    "Niuniu": 0,
    "WiktoriaP": 0,
    "WiktoriaW": 0,
    "Antonius": 0,
    "Wiesław": 0,
    "Bartosz": 0,
    "Petitty": 0,
}

# =============================================== TRANSFORMS

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0

# =============================================== START

label start:
    $ name = renpy.input("Jak masz na imię")
    $ name = name.strip()
    define you = Character("[name]")


    jump ch02_watch_your_mouth

# =============================================== MISC

label runningFromTheChurch:
    scene bg catacombs
    stop music
    show rafal normal at leftish
    show wp normal at center
    you "Wiki co to jest za tobą?"
    "(teraz kliknij RAZ i nic nie klikaj póki ta cutscena się nie skończy bo nwm jak to zablokować)"
    show eyes behind wp with dissolve:
        yalign 0.5
        xalign 0.65
    window hide
    $ renpy.pause(0.5, hard=True)
    play sound "running_from_church.mp3"
    pause 1.35
    with vpunch
    show rafal at offscreenleft 
    show wp at offscreenright 
    with move 
    with vpunch
    scene bg churchstairs with vpunch
    show rafal normal with vpunch:
        xalign 0.4
        yalign 0.4
        zoom 0.5

        linear 0.6 xalign 0.8 zoom 1.2
        linear 0.2 xpos -200
    with vpunch
    with vpunch
    show wp normal with vpunch:
        xalign 0.4
        yalign 0.4
        zoom 0.5

        linear 0.9 xalign 0.7 zoom 1.2
        linear 0.1 xpos -200
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    scene bg churchinside with vpunch
    show rafal normal at offscreenleft
    show wp normal at offscreenleft
    with vpunch
    show rafal normal:
        xpos -100
        linear 2.1 xpos 2000
        linear 0.2 xpos 2000
        linear 0.3 xpos 1900
        linear 0.3 xpos 1900
        linear 0.3 xpos 2500
    show wp normal:
        xpos -100
        linear 0.2 xpos -100
        linear 2 xpos 1700
        linear 0.3 xpos 1700
        linear 0.5 xpos 2500
    pause 3
    scene bg lanastreetnight with vpunch
    with vpunch
    show rafal normal at leftish with dissolve
    with vpunch
    show rafal normal at offscreenleft with move
    with vpunch
    show wp normal at leftish with dissolve
    with vpunch
    show wp normal at offscreenright with move 
    with vpunch 
    scene bg colacocastreetnighta with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    scene bg kitchen with fade
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    scene bg bedroom with fade
    scene black
    pause 3
    scene bg bedroom with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    scene bg kitchen with fade
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    scene bg colacocastreetnighta with fade
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    scene bg lanastreetday with fade
    with vpunch
    with vpunch
    with vpunch
    with vpunch
    show bg citysquareday with fade
    play music "town_day.mp3"
    stop sound
    window show
    show rafal normal at leftish 
    show wp normal at rightish 
    with dissolve
    "..."
    return

 

label gameEndCreditsScene:
    scene black with fade
    stop music fadeout 1.0
    pause 1.0
    $ renpy.movie_cutscene("misc/credits.webm")