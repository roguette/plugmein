define seenBjorkGhost = False
define hasSkinnyWaist = False
# renpy-graphviz: BREAK

label h_wakingUpAfterFirstNight:
    "Zanim się obejrzałeś to byłeś już w domu pod kołdrą."
    stop music fadeout 1.0
    scene black with dissolve

    if fountainLoreReceived != True:
        play music "sb_soulsearcher.mp3"
        "Jesteś bardzo głodny, ale nie aż tak, żeby przez to nie iść spać."
        "I zanim się obejrzysz, już śpisz."

        "A czekaj... już nie."
        "Czujesz, jakbyś leciał przez swoje łóżko."
        "Potem przez podłogę."
        "Aż w końcu lądujesz w wodzie."
        "Nagła zmiana temperatury sprawia, że podskakujesz."
        "Otwierasz oczy i widzisz, że jesteś w fontannie na rynku."
        you "{i}Z tą głupią fontanną zawsze jest coś...{/i}"
        "Przed tobą pojawia się dusza."
        m "Fontanna nie jest głupia."
        you "{i}Jeśli this ho czyta moje thoughts to się zesram to jest crazy.{/i}"
        m "Spokojnie. Nie defekuj. Nie jestem złą duszą."
        "Postanawiasz coś powiedzieć normalnie, bo się robi niezręcznie."
        "I wygląda to jak jakaś relacja parasocjalna."
        "Taka jak na twitchu."
        you "Kim pani jest?"
        m "Ty wiesz kim ja jestem."
        you "Aha to ty jesteś B-{nw}"
        bjork "Tak, {w=0.6}jestem Bjork"
        pause 5
        you "Czego ty ode mnie chcesz?"
        bjork "A czego TY ode mnie chcesz?"
        pause 3
        you "Dlaczego ja tu jestem i nic nie pamiętam?"
        bjork "Odpowiedź na wszystkie pytania znajdziesz w kościele."
        you "{i}Jezu to po co ona się mnie pytała?{/i}"
        bjork "Słyszałam to."
        bjork "Nie potrafię opisać wszystkiego, co musisz zobaczyć, poczuć i zrozumieć."
        bjork "Musisz samemu to wszystko zobaczyć."
        bjork "Nie jesteś głupi i wszystko zrozumiesz."
        bjork "To od ciebie zależy, czy pomożesz miastu, czy doprowadzisz do jego upadku."
        "W okamngnieniu wracasz do swojego łóżka."
        $ seenBjorkGhost = True
        stop music fadeout 0.5

    ".{w=0.5}.{w=0.5}.{w=0.5}"
    "Budzisz się i ponieważ jest już rano możesz lepiej przyjrzeć się swojemu domowi."
    scene bg bedroom with fade
    "Ten dom jest mały (ale dla ciebie jest ogromny bo [name] jest skinny i ma skinny waist)."
    "Prawdopodobnie spałeś jakieś 10 godzin i był to najlepszy sen w Twoim życiu."
    "Jednak obudziło Cię uczucie głodu."
    "Od wczoraj nic nie jadłeś, ale dzisiaj musisz coś z tym zrobić, żeby nie umrzeć z głodu."

    scene bg kitchen with fade
    "Idziesz do kuchni po jakieś jedzenie, na szczęście w kuchni masz dużą lodówkę."
    "Co chcesz zjeść?"
    menu:
        "Kawior":
            "Jesteś na 99%% pewny, że nie masz czegoś takiego w lodówce."
            "Dostałeś ten dom za darmo, ale nie przesadzajmy. Nie ma szans, że też dostałeś tak luksusowe jedzenie w prezencie"
        "Winniczki":
            you "{i}To jest chyba jedyna rzecz w mojej lodówce{/i}"
        "Dead dove":
            "Wiadomo, że nie należy jeść martwych gołębi."
        "Nie chcę jeść":
            $ hasSkinnyWaist = True
            you "{i}Po takiej diecie mój snatched waist będzie potężny, może tylko się czegoś napiję.{/i}"

    "Otwierasz lodówkę i ku twojemu zdziwieniu nie ma w tej lodówce nic poza krasnalem, który włącza i wyłącza w niej swiatło."
    "Wychodząc z domu prawie zapominasz zamknąć drzwi, ale w ostatnim momencie przypomniałeś sobie w jakiej okolicy mieszkasz."
    "Prawie mdlejesz z głodu. Chyba nie opłacało ci się być skinny."
    "W mieście jest jedna osoba, która może ci teraz pomóc - Kurowska."
    "Prawdopodobnie właśnie pracuje, więc postanawiasz udać się prosto do niej."
    jump t_goingToTownToKurowskaDueToHungerDayTwo

# renpy-graphviz: BREAK

label h_wakingUpSecondNightAtHome:
    "Zamykając oczy, zaczynasz myśleć o funkcji kwadratowej i wszystkich jej miejscach zerowych ― o ile istnieją ― co sprawia, że natychmiast zasypiasz." 
    "Przed całkowitą utratą świadomości masz nadzieję, że Björk nie będzie nawiedzać twoich snów." 
    "I tej nocy nie będzie."
    "Ale Rafał tak."
    "Życie cofa się o kilka godzin i znów jesteś w piekarni, czekając na Rafała."
    "Wychodzi z kuchni z bułką w ręce i zaczyna mówić z ustami pełnymi glutenu."

    r "Wiesz...{w=.3} jestem taki samotny."
    r "Nikt do mnie nie przychodzi pogadać ― każdy chce tylko moje buły, a ja nie mam z kim słowa wymienić..."
    you "A Wiktoria to co?"
    r "No tak, ale ona rzadko tu przychodzi..." 
    r "Przez większość czasu jestem tu sam, jak ten palec..."
    r "Siedzę w tej piekarni i piekę, i piekę ― {b}ILEŻ TAK MOŻNA{/b}?!"
    r "Nie mam tu {b}NIC{/b} do roboty oprócz tych głupich buł..."
    you "Chcesz o tym porozmawiać?"
    r "Tak."
    you "No to powiedz co się dzieje."
    r "Kiedyś mieszkałem razem z moją mamą w domu po drugiej stronie Bratgren." 
    r "Nie żyliśmy zbyt burżuazyjnie ― dom był mały, ale jakoś było." 
    r "Moja mama straciła pracę i ten dom był wszystkim, co nam zostało."
    r "W sensie oprócz mojej pracy."
    r "No i tej piekarni ale no..."
    r "Mojej mamnie nie przelewa się.{w=.6} To znaczy, przelewa się, ale przez dach."
    r "Meteoryt uderzył w nasz dom, robiąc przy tym ogromną dziurę w dachu..."
    r "Chyba nie muszę tłumaczyć, dlaczego to jest dużym problemem?"
    r "Nie stać mnie na naprawę dachu. Nie będę nawet mówił o nowym domu."
    r "I popatrz na tę piekarnię..."
    r "Nie zmieścimy tu się we dwójkę."
    r "Gdzie ma spać? NA MOICH BUŁACH?!{w=.6} To nie jest zgodne z BHP." 

    menu:
        "Dobrym sposobem na zarobienie pieniędzy jest high level prostytucja.":
            "Rafał wyciąga cegłę i mówi ci, żebyś wyszedł."
            jump h_afterRafalDream
        "Nie, może spać w kuchni. Nikomu nie powiem.":
            "Rafał wyciąga cegłę i mówi ci, żebyś wyszedł."
            jump h_afterRafalDream
        "Przejdziesz przez to. Nie martw się":
            "Rafał przytula cię i dziękuje za pomoc."
            jump h_afterRafalDream

label h_afterRafalDream:
    "Nagle czujesz ciepłe promienie słońca na sobie i powoli otwierasz oczy."
    "Przez krótką chwilę zauważasz, że zasłony są otwarte, mimo że zamknąłeś je wczoraj{w}, ale nie poświęcasz temu tyle uwagi, ile powinieneś."
    "Pewnie po prostu zapomniałeś je zasłonić."
    "Zapomniałeś, tak jak wszyscy w tym mieście."
    "Idziesz do łazienki, robisz nudne, higieniczne, prywatne a nawet relaksujące rzeczy, potem do kuchni, bo jesteś już głodny."
    jump h_moornin

label h_moornin:
    "Otwierasz lodówkę i widzisz, że połowy bułki brakuje{w=.3}, a twój własny krasnal patrzy na ciebie z najwyższej półki i się uśmiecha." 
    "Okazuje się, że jednak MUSISZ go karmić."
    "Bierzesz bułę, okruszki zostawiasz dla krasnala i wychodzisz."
    "W końcu musisz być na rynku za pół godziny." 
    "W chwili, gdy masz już otworzyć drzwi, słyszysz pukanie i się wahasz." 
    "W zawachaniu twoja ręka zawisa nad klamką, ale słyszysz kolejne pukanie. Z tego ambarasu otwierasz drzwi."
    "Uchylasz je tylko troszeczkę, żeby zobaczyć kto stoi na zewnątrz{w=.3} i widzisz surykatkę przed drzwiami."
    "Uśmiecha się do ciebie takim uśmiechem, jaki mają pracownicy w customer service ― nie tak jak w reklamach nieruchomości ― ten uśmiech to taki uśmiech, jaki ludzie muszą mieć, nawet jeśli nie są szczęśliwi."

    m "Dzień dobry"
    you "Mogę w czymś pomóc?"
    m "Tak, możesz. Przyszedłem pobrać podatki."
    you "Aha dobra, tak, oczywiście, sekundę, chwileczkę. Nigdzie nie odchodź."
    you "Stój tu grzecznie!"

    "Otwierasz drzwi, ale nie wpuszczasz przypadkowego pracownika rządu do domu."
    "Idziesz do sypialni, gdzie zostawiłeś wszystkie swoje rzeczy, bierzesz wszystkie pieniądze i wracasz do drzwi wejściowych."

    you "Ile jestem winien?"
    m "100 foryntów"
    you "Jaka ładna liczba!"
    you "Okej, proszę... Proszę bardzo... yyy..."
    you "Jak masz na imię?"
    a "Antonius Cornelius-Benedictus"
    you "No to masz... yy.. anadius coś tam"
    you "Dobra, teraz idź, idź, idź, ja muszę gdzieś być za 10 minut"

    "Delikatnie odpychasz go na bok i zamykasz drzwi, po czym biegniesz sprintem na rynek{w=.3}, zostawiając zdezorientowaną surykatkę o bardzo długim i dziwnym imieniu przed drzwiami."

# renpy-graphviz: BREAK



