
define config.default_text_cps = 50
define config.main_menu_music = "audio/ShouldersOfGiants.mp3"


define e = Character("Eileen")
define mks = Character("MKS 23", color="#fafafa")
define m = Character("???")


define piotrName = "Piotr"
image side piotr = "piotr side.png"
define p = Character("[piotrName]", image="piotr", color="#a222be")

define filipName = "Filip"
define f = Character("[filipName]", color="#a222be")

define kurowskaName = "Kurowska"
define k = Character("[kurowskaName]", color="#ff41c9")

default friendship = {"Piotr": 0, "Filip": 0, "Kurowska": 0}

style window:
    background Solid("#00000080")



label start:
    play music "audio/street.mp3" 
    

    $ name = renpy.input("Jak masz na imię")
    $ name = name.strip()
    define you = Character("[name]")

    scene bg busstopa with dissolve

    you "{i}głupi mks oczywiście że musiał się spóźnić{/i}"
    you "{i}zostały mi 2 minuty a muszę jeszcze iść do szatni{/i}"
    "{cps=1}...{/cps}"
    you "{i}o dobra mam zielone mogę przejść{/i}"

    show bus at center

    mks "hejka naklejka"

    window hide

    play sound "audio/hit_by_bus.mp3"
    show bus:
        linear 3.0 zoom 3.0
    you "AAAAAAAAAAAAAAAAAAA{nw}"
    pause 2.5
    scene black

    pause 3.0
    stop music fadeout 2.0

    window show
    

    "{cps=1}...{/cps}"
    "{cps=25}zostałeś właśnie potrącony przez mks 23{w}(do przybówki){/cps}"
    "{cps=20}twoje krzyki usłyszał tylko kierowca tego autobusu{/cps}"
    "{cps=15}który pewnie już uciekł i jedzie sobie dalej{/cps}"
    "{cps=2}...{/cps}"
    "Mimo tego,{w=1.0} o dziwo,{w=1.0} żyjesz"
    "Strasznie cię boli głowa, ale nie możesz podnieść ręki, aby sprawdzić czy w ogóle ją jeszcze masz"
    "Jesteś tak słaby że nie możesz nawet otworzyć oczu"
    "(tu będzie dzwięk kroków i wgl muzyka ale nie chciało mi się jeszcze szukać)"
    m "do jasnej mufinki.."
    m "proszę pana czy pan żyje"
    "ktoś kładzie swoją rękę na twoje ramienie i próbuje cię obudzić, a jego długie pazury wbijają się w twoją koszulkę"

    scene bg forestnight with fade

    you "AAAAA"
    you "Proszę mnie nie dotykać"
    show piotr at center with dissolve
    "otwierasz oczy i widzisz przed sobą wysokiego ptaka, próbujesz się odsunąc od niego ale za tobą jest drzewo"
    "więc siedzisz i patrzysz się na niego jak głupi"
    you "{i}Co jest{/i}"
    you "{i}Czemu on jest ptakiem{/i}"
    "patrzysz się na niego z 10 sekund"
    "bardzo ci się chce podejść do niego i mu się przyjrzeć ale bardzo się go boisz..."
    "Kiedy ptak wykluwa się ze swojego jajka traktuje pierwszą rzecz ktorą widzi jako swoją matkę"
    "coś podobnego się dzieję z tobą ale na odwrót"
    "On na pewno miał coś wspólnego z tym, cokolwiek się właśnie wydarzyło, więc od razu go nie lubisz"
    you "{i}Co on ze mną zrobił{/i}"
    you "{i}To chyba {b}on{/b} mnie tutaj przywołał jak jakiegoś ducha{/i}"
    "patrzysz się na niego z podejrzliwością"
    you "Kim ty jesteś?? Halo?? Co ty tutaj robisz???"
    m "Nie drzyj się jesteś w lesie"
    p "Nazywam się [piotrName] i jestem czarodziejem"
    p "To znaczy miałem oczyszczać las, ale twoja obecność mi przeszkodziła"
    "patrzysz się dookoła i widzisz obok siebie koło z onyksu"
    "[piotrName] daje ci swoją rękę, a dokładniej łapę i pomaga ci wstać"
    you "{cps=20}Dziękuję! Czekaj co{/cps}{nw}"
    you "{cps=20}tfym ja ci przeszkodziłem{/cps}{nw}"
    you "{cps=20}czemu ty jesteś ptakiem{/cps}{nw}"
    you "{cps=20}CO SIĘ DZIEJE{/cps}{nw}"
    show piotr angry
    p "SYBAU"
    show piotr
    p "Mogę odpowiedzieć na twoje pytania, ale pod warunkiem że będziesz cicho"

    jump piotrIntroductionMenu

