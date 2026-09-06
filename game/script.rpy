# ===============================================
# script.rpy 
#
# to tu sie zaczyna
#
# le contents:
# GLOBAL VARIABLES
# INIT PYTHON
# CHARACTER DEFINITIONS
# TRANSFORMS
# START
# MISC
# ===============================================

init -2 python:
    import random
    from datetime import datetime
    from collections import defaultdict

image mess = Animation(
    "images/mess_gif/0.png", 1,
    "images/mess_gif/1.png", 1,
    "images/mess_gif/2.png", 1,
    "images/mess_gif/3.png", 1,
    "images/mess_gif/4.png", 1,
    "images/mess_gif/5.png", 1,
)

# =============================================== GLOBAL VARIABLES
default friendship = defaultdict(int)
default flags = set()
define TESTING = True
define config.default_text_cps = 130
define config.main_menu_music = "audio/ShouldersOfGiants.mp3"
define build_name = "github"
default name = ""
define you = Character("[name]")

define location_bgs = {
    "square": ("bg citysquareday", "bg citysquarenight"),
    "lanastreet": ("bg lanastreetday", "bg lanastreetnight"),
    "crouticlocksstreet": ("bg crouticlocksstreetday", "bg crouticlocksstreetday"), # TODO: crouticlocksstreetnight does not exist
    "field": ("bg fieldday", "bg fieldnight"),
    "fountain": ("bg fountainday", "bg fountainnight"),
    "house": ("bg houseday", "bg housenight"),
    "cityexit": ("bg cityexitday", "bg cityexitnight"),
    "forest": ("bg forestday", "bg forestnight")
}

# =============================================== INIT PYTHON

init python:
    def flag(name, change_to=None):
        if change_to is None:
            return name in flags

        if change_to:
            flags.add(name)
        else:
            flags.discard(name)

    # telemetry for testing
    time_started = None
    time_finished = None
    telemetry_flags = []

    

    def telemetry_start():
        global time_started
        time_started = datetime.now()

    def telemetry_end():
        global time_finished
        time_finished = datetime.now()

    def telemetry_flag(flag):
        telemetry_flags.append([datetime.now(), flag])

    def flatten(list):
        for a, b in list:
            yield str(a) + ":" + b

    def telemetry_generate_result_string():
        
        return "zrób zrzut ekranu!\n\n" + \
            str(time_started) + "\n" + \
            str(time_finished) + '\n' + \
            str(time_finished - time_started) + '\n' + \
                '\n' + '\n'.join(flatten(telemetry_flags)) + "\n" + ", ".join(flags)

    def loc_bg(loc):
        day_img, night_img = location_bgs[loc]
        return day_img if time.isDay() else night_img

    class TimeClass:
        def __init__(self):
            self.chapter = 1
            self.hour = 18
            self.minute = 0

        def getTimeString(self):
            return f"Chapter {self.chapter} {self.hour:02d}:{self.minute:02d}"

        def advanceTime(self, minutes=0, hours=0):
            newMinutes = self.minute + minutes
            hours_skipped = newMinutes // 60

            self.minute = newMinutes % 60
            total_hours = self.hour + hours_skipped + hours

            self.chapter += total_hours // 24
            self.hour = total_hours % 24
            renpy.transition(dissolve, layer="screens")
        
        def setTime(self, hours, minutes):
            self.hour = hours
            self.minute = minutes
            renpy.transition(dissolve, layer="screens")


        def isDay(self):
            return 6 < self.hour < 18


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

default time = TimeClass()

# =============================================== TRANSFORMS

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0

# =============================================== START

label start:
    stop music

    $ telemetry_start()

    if TESTING or renpy.is_in_test():
        $ name = "TEST"
    else:
        $ name = renpy.input("Jak masz na imię")
        $ name = name.strip()

    jump ch00_bus_stop

# =============================================== MISC


transform chapter_text_animation:
    alpha 0.0
    zoom 1.0

    linear 1.0 alpha 1.0


transform title_text_animation:
    alpha 0.0
    zoom 1.0

    pause 3.870
    linear 0.001 alpha 1.0


transform smallFadeIn:
    alpha 0.0
    linear 1.0 alpha 1.0


screen chapterTransition(chapter_text, title_text):

    timer 7.459 action Return()

    add Solid("#000000")

    add "mess":
        xalign 0.8
        yalign 0.5
        xsize 700
        ysize 700
        at smallFadeIn
        

    text chapter_text:
        xpos 0.1
        xanchor 0.0
        yalign 0.45
        color "#ffffff"
        size 80
        at chapter_text_animation

    text title_text:
        xpos 0.1
        xanchor 0.0
        yalign 0.55
        color "#ffffff"
        size 40
        at title_text_animation
    


label chapterTransition(chapter_text, title_text):
    with dissolve
    window hide
    play audio "audio/sfx_chapter_transition.mp3"
    
    call screen chapterTransition(chapter_text, title_text)
    stop audio fadeout 0.0
    window show
    with dissolve
    return

label gameEndCreditsScene:
    scene black with fade
    stop music fadeout 1.0
    pause 1.0
    $ renpy.movie_cutscene("misc/credits.webm")