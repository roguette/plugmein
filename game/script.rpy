define config.default_text_cps = 90
define config.main_menu_music = "audio/ShouldersOfGiants.mp3"

define mks = Character("MKS 23", color="#fafafa")
define m = Character("???") #mystery speaker

image side piotr = "piotr side.png"

define p = Character("Piotr", image="piotr", color="#a222be")
define f = Character("Filip", color="#a222be")
define k = Character("Barbara K.", color="#ff41c9")
define t = Character("Tomcio", color="#ec1f1f")
define v = Character("Vasili", color="#6a6277")
define wp = Character("Wiktoria P.", color="#7e3611")
define bjork = Character("Björk", color="#77beee")

init python:
    import random




default friendship = {
    "Piotr": 0, 
    "Filip": 0, 
    "Kurowska": 0,
    "Tomcio": 0,
    "Vasili": 0
}



label start:
    play music "audio/street.mp3" 
    

    $ name = renpy.input("Jak masz na imię")
    $ name = name.strip()
    define you = Character("[name]")
    jump wakingUpAfterFirstNight 

    scene bg busstopa with dissolve

    you "{i}No szybciej już{/i}"
    "Szybko, nerwowo, impulsywnie oraz intensywnie wciskasz przycisk na światłach (ten taki żółty)"
    "Wczoraj naprawiali światła właśnie na tym przejściu i ewidentnie coś zepsuli"
    "{cps=1}...{/cps}"
    "Stoisz na tym przejściu z minutę, a światła dalej są czerwone"
    you "{i}Zostały mi tylko 2 minuty, a muszę jeszcze iść do baru {w=.5}po matchę.{/i}"
    you "{i}Jeśli jeszcze raz się spóźnię to obniżą mi zachowanie{/i}"
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
    
    #"(tu będzie dzwięk kroków i wgl muzyka ale nie chciało mi się jeszcze szukać)"
    
    m "Do jasnej muffinki!!!"
    m "Proszę pana, czy pan żyje?!"
    "Ktoś kładzie swoją rękę na twoim ramieniu i próbuje cię obudzić, a jego długie pazury wbijają ci się w skórę."



    scene bg forestnight with vpunch

    you "AAAAA!!!!"
    you "Proszę mnie nie dotykać!!!"
    you "This is my no-no square!!!"
    you "Stranger Danger!!!"
    show piotr at center with dissolve
    "Otwierasz oczy i widzisz przed sobą wysokiego ptaka, od którego próbujesz się odsunąć, ale{w=.5} za tobą jest drzewo."
    "Dlatego siedzisz i patrzysz się na niego jak głupi."
    you "{i}Co jest?{/i}"
    you "{i}Czemu on jest {w=.5}{u}ptakiem{/u}???{/i}"
    "Patrzysz się na niego z 10 sekund... {w=1.0}1{w=1.0}2{w=1.0}3{w=1.0}4{w=1.0}5{w=1.0}6{w=1.0}7{w=1.0}8{w=1.0}9{w=1.0}10{nw}"
    "Bardzo chcesz do niego podejść i mu się przyjrzeć, ale...{w=.5} bardzo się go boisz..."
    "Kiedy ptak wykluwa się ze swojego jajka traktuje pierwszą rzecz, którą widzi jako swoją matkę. {w=1.0}Coś podobnego dzieję się z Tobą,{w=.1} ale na odwrót."
    "On na pewno miał coś wspólnego z tym, cokolwiek się właśnie wydarzyło, więc od razu go nie lubisz."
    you "{i}Co on ze mną zrobił???{/i}"
    you "{i}To chyba {cps=10}{b}on{/b}{/cps} mnie tutaj przywołał jak jakiegoś ducha.{/i}"
    "Patrzysz się na niego z podejrzliwością, jak spod byka niemalże."
    you "Kim ty jesteś??{w=.5} Halo???{w=.5} Co ty tutaj robisz???"
    m "Nie drzyj się, jesteś w lesie!!!"
    p "Jednakże, nazywam się Piotr i jestem czarodziejem."
    "Patrzysz się dookoła i widzisz obok siebie koło z onyksu."
    "Piotr daje ci swoją rękę, a dokładniej łapę, i pomaga ci wstać."
    you "Co to za kamyki tam masz"
    you "Te takie czarne"
    p "To? (wskazuje jednym ze swoich długich,{w=.5} czarnych,{w=.5} strasznych,{w=.5} a nawet krzywych{w=.5} pazurów na koło z onyksu)"
    you "Tak"
    "Piotr podchodzi do tego koła i podnosi dwa kamienie"
    you "Co to jest..."
    p "To jest onyks. Używam tych kamieni do usuwania złych vibeów z tego lasu"
    p "Im więcej złej energii wchłaniają, tym są cięższe"
    p "Weź ten i ten i zrób takie six seven"
    "Jeden z tych kamieni jest rzeczywiście o wiele cieższy od drugiego"
    "Mimo tego, że są prawie identyczne"
    you "Ale heca"
    you "Co się robi z najcięższymi kamykami"
    p "Zostawiam je w piwnicy jeśli jest zbyt ciężki"
    p "Miałem właśnie oczyszczać las, ale {b}twoja obecność{/b} mi przeszkodziła."
    you "{cps=15}Dziękuję! Czekaj co?{/cps}{nw}"
    you "{cps=15}Co masz na myśli mówiąć, że {b}ja{/b} ci przeszkodziłem?{/cps}{nw}"
    you "{cps=15}Czemu ty jesteś ptakiem?{/cps}{nw}"
    you "{cps=15}{b}CO SIĘ DZIEJE!?{/b}{/cps}{nw}"
    show piotr angry
    with vpunch
    p "SYBAU!"
    show piotr
    p "Mogę odpowiedzieć na twoje pytania, ale pod warunkiem że będziesz {b}c i c h o{/b}{w} (bo przyjdzie Zdicho)."

    jump piotrIntroductionMenu




label gameEndCreditsScene:
    scene black with fade
    stop music fadeout 1.0
    pause 1.0
    $ renpy.movie_cutscene("misc/credits.webm")