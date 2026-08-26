define config.default_text_cps = 110
define config.main_menu_music = "audio/ShouldersOfGiants.mp3"

define mks = Character("MKS 23", color="#fafafa")
define m = Character("???", color="#808080") # mystery speaker

image side piotr = "piotr side.png"

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

init python:
    import random

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
    "Rafal": 0
    "Niuniu": 0,
    "WiktoriaP": 0,
    "WiktoriaW": 0,
    "Antonius": 0,
    "Wiesław": 0,
    "Bartosz": 0,
    "Petitty": 0,
}

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0

label start:
    play music "audio/street.mp3" 

    $ name = renpy.input("Jak masz na imię")
    $ name = name.strip()
    define you = Character("[name]")
    scene bg busstopa with dissolve

    you "{i}No szybciej już{/i}"
    "Szybko, nerwowo, impulsywnie oraz intensywnie wciskasz przycisk na światłach (ten taki żółty)."
    "Wczoraj naprawiali światła właśnie na tym przejściu i ewidentnie coś zepsuli."
    "{cps=1}...{/cps}"
    "Stoisz na tym przejściu z minutę, a światła dalej są czerwone."
    you "{i}Zostały mi tylko 2 minuty, a muszę jeszcze iść do baru {w=.5}po matchę.{/i}"
    you "{i}Jeśli jeszcze raz się spóźnię to obniżą mi zachowanie.{/i}"
    "{cps=1}...{/cps}"
    you "{i}O dobra mam zielone mogę przejść!{/i}"

    show bus at center

    mks "Ohayoooo!!!!"

    window hide

    play sound "audio/hit_by_bus.mp3"
    show bus:
        linear 3.0 zoom 3.0
    pause 2.5
    you "AAAAAAAAAAAAAAAAAAA{nw}"
    scene black

    pause 3.0
    stop music fadeout 2.0

    window show
    

    "{cps=1}...{/cps}"
    "{cps=25}Zostałeś właśnie potrącony przez mks 23{w} (do przybówki).{/cps}"
    "{cps=20}Twoje krzyki usłyszał tylko kierowca tego autobusu.{/cps}"
    "{cps=15}Który pewnie już uciekł i jedzie sobie dalej.{/cps}"
    "{cps=2}...{/cps}"
    "Mimo tego,{w=.5} o dziwo,{w=.5} żyjesz{w=.5}<3"
    play music "forest.mp3" fadein 2.0
    "Strasznie cię boli głowa, ale nie możesz podnieść ręki, aby sprawdzić czy w ogóle ją jeszcze masz."
    "Jesteś tak słaby, że nie możesz nawet otworzyć oczu."
    
    m "Do jasnej muffinki!!!"
    m "Proszę pana, czy pan żyje?!"
    "Ktoś kładzie swoją rękę na twoim ramieniu i próbuje cię obudzić, a jego długie pazury wbijają ci się w skórę."



    scene bg forestnight with vpunch

    you "AAAAA!!!!"
    you "Proszę mnie nie dotykać!!!"
    you "This is my no-no square!!!"
    you "Stranger Danger!!!"
    show piotr normal at center with dissolve
    "Otwierasz oczy i widzisz przed sobą wysokiego ptaka, od którego próbujesz się odsunąć, ale{w=.5} za tobą jest drzewo."
    "Dlatego siedzisz i patrzysz się na niego jak głupi."
    you "{i}Co jest?{/i}"
    you "{i}Czemu on jest {w=.5}{u}ptakiem{/u}???{/i}"
    "Patrzysz się na niego z 10 sekund...\n{w=1.0}1{w=1.0}2{w=1.0}3{w=1.0}4{w=1.0}5{w=1.0}6{w=1.0}7{w=1.0}8{w=1.0}9{w=1.0}10{nw}"
    "Bardzo chcesz do niego podejść i mu się przyjrzeć, ale...{w=.5} bardzo się go boisz..."
    "Kiedy ptak wykluwa się ze swojego jajka traktuje pierwszą rzecz, którą widzi jako swoją matkę. {w=1.0}Coś podobnego dzieję się z Tobą,{w=.1} ale na odwrót."
    "On na pewno miał coś wspólnego z tym, cokolwiek się właśnie wydarzyło, więc od razu go nie lubisz."
    you "{i}Co on ze mną zrobił???{/i}"
    you "{i}To chyba {cps=10}{b}on{/b}{/cps} mnie tutaj przywołał, jak jakiegoś ducha.{/i}"
    "Patrzysz się na niego z podejrzliwością, jak spod byka niemalże."
    you "!Who the hell are you"
    you "!And why did you put me in this cliche visual novel situation"
    you "!Waking up in the forest and all that"
    m "Nie drzyj się, jesteś w lesie!!!"
    you "!Oh no no no you are going to answer all my questions first"
    you "!You have 10 seconds until i let you know i ate eggs for breakfast"
    p "!Can you shut up for once"
    p "!You are in a forest so SHUT UP"
    p "Nazywam się Piotr i jestem czarodziejem."
    you "!Magician? Like a birthday party magician?"
    p "???"
    you "!Like do you do silly tricks like pulling rabbits out of your conveniently huge top hat"
    p "!No that is called animal abuse"
    you "!Oh"
    you "{i}!He's so cute i cannot be angry at him{/i}"
    you "{i}!A little feisty but i can tolerate that{/i}"
    "Patrzysz się dookoła i widzisz obok siebie koło z czarnych kamieni."
    "Piotr daje ci swoją rękę, a dokładniej łapę, i pomaga ci wstać."
    you "Co to za kamyki tam masz?"
    you "Te takie czarne..."
    p "To?"
    "Wskazuje jednym ze swoich długich,{w=.5} czarnych,{w=.5} strasznych,{w=.5} a nawet krzywych{w=.5} pazurów na koło z czarnego kamienia."
    you "Tak."
    "Piotr podchodzi do tego koła i podnosi dwa kamienie."
    menu:
        "!Omg they are dark like your crusty ass nails":
            p "!Hell no"
        "!Can i have one?":
            p "!Hell no"
    p "To jest onyks. Używam tych kamieni do usuwania złych vibeów z tego lasu."
    p "Im więcej złej energii wchłaniają, tym są cięższe. Patrz tu..."
    "!your enthusiasm knows no bounds so you add a few ohs here and there to support the conversation"
    p "Weź ten i ten i zrób takie six―seven."
    "Jeden z tych kamieni rzeczywiście jest o wiele cieższy od drugiego. Mimo tego, że są prawie identyczne."
    you "Ale heca!"
    you "!So why are you carrying these heavy stones are you stupid"
    p "!No its because {nw}"
    p "!Actually no i've been nothing but nice to you and you are rude like this"
    p "!I am not telling you anytihng"
    you "{i}this bitch{/i}"
    you "!Okay fine sorry i got a little carried away you can continue"
    p "So as i was saying... before your rude ass interrupted me"
    p "Theres a limited supply of these stones"
    p "We use them for clearing bad energy in this forest"
    "You should be thankful he is doing this because if it werent for the magical bird in front of you monsters would have mauled you like bts stans on twitter"
    you "{i}Okay that is indeed terrifying{/i}"
    p "anyways... back to those stones"
    p "If a stone is too heavy i leave it at home"
    you "So you just have a pile of rocks at home?"
    p "Yes"
    you "It's giving coal miner"
    p "NO IT DOESNT"
    you "I'll be the judge of that.. (small text idk how to do it)"
    p "What did you say?"
    you "What did you hear"
    p "Im not sure"
    you "Then i guess we will never know"
    you "What were you doing before you isekaied me here?"
    p "I was cleaning the forest like i explained before and this had nothing to do with you"
    you "Okay so you havent started yet?"
    p "Yes"
    you "What if i am evil"
    p "You're not evil you are just being rude on purpose"
    p "Im sure you couldnt even hurt a fly"
    you "True.. they are way too fast"
    you "So when are you gonna answer my questions?"
    p "I will provide answers only IF you promise to stay quiet"
    you "{i}This bitch{/i}"
    you "{i}Fine. I will stay silent for a moment{/i}"
    you "{i}If he tries me again i will just say he kept me in his basement{/i}"
    you "{i}Does he have a basement though?? What if he doesnt?{/i}"
    you "Do you have a basement"
    p "What? Yes. Why did you ask {nw}"
    you "{i}Bingo{/i}"
    you "Okay then we have a deal."
    

    jump f_piotrIntroductionMenu

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

    jump runningFromTheChurch
 

label gameEndCreditsScene:
    scene black with fade
    stop music fadeout 1.0
    pause 1.0
    $ renpy.movie_cutscene("misc/credits.webm")