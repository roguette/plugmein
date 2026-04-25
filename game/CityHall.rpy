
define wasRudeToPiotr = False
label filipIntroduction:
    menu:
        "Sprowokuj piotra":
            $ wasRudeToPiotr = True
            $ friendship["Piotr"] -= 1
            you "Obsrałeś się jak mnie zobaczyłeś Panie Piotrze więc sybau"
            p "To nie prawda. Proszę nie oczerniać mojego wizerunku"
            you "{i}ale dałem do pieca{/i}"
            p "..."
            jump filipIntroduction_after            
        "Milcz":
            you "{i}on nie jest tuff{/i}" 
            jump filipIntroduction_after



label filipIntroduction_after:
    p "Oczyszczałem las, jak mi kazałeś, a on pojawił się koło mnie i zepsuł mój rytuał,"
    p "teraz muszę zacząć od nowa."
    you "Jakim cudem to jest moja wina?"
    you "Trzeci raz cię pytam i dalej nie wiem"
    m "No właśnie też bym chciał usłyszeć jakim cudem to jest twoja wina w tej sytuacji"
    m "Coś mi się wydaje, że są rzeczy ważniejsze."
    m "Ty możesz swoje rytuały zrobić nawet jutro. A [name] mógł w tym lesie umrzeć"
    m "Chodź tu"
    "Podchodzisz trochę bliżej do Filipa, on wstaje i podaje ci rękę"
    "Uśmiechasz się jak w reklamie nieruchomości"
    "Nie wiesz, czy możesz mu ufać, ale on na pewno ma lepsze viby od Piotra."
    f "Cześć. Nazywam się Filip i witam w naszym małym, pięknym, fajnym i zarazem przytulnym mieście Bratgren. Pewnie masz ogromną ilość pytań?"
    you "No tak"
    f "A czy coś już wiesz o tym mieście?"
    you "No nie"
    "Filip jest uradowany tą informacją z jakiegoś powodu"
    f "No to świetnie. Teraz zaprowadzę cię do Kurowskiej, ona odpowie na wszystkie twoje pytania."
    f "Ona lubi takie rzeczy opowiadać tylko musisz się pytać"
    f "Tylko nie stresuj się. Bądź dla niej miły i ona będzie miła dla ciebie"
    f "Aha powiem ci jeszcze jedną rzecz - nie jesteś jedyny."
    f "Wszyscy pojawiliśmy się przed tym miastem, tak jak ty."
    you "Piotr mi tego nie powiedział..."
    f "A to czemu gatekeepujesz, panie Piotrze"
    p "To jest mój pierwszy raz, kiedy spotykam taką osobę"
    f "Ma sens, ale proszę następnej osobie takie rzeczy mówić"
    f "Pan [name] pewnie się stresował przez ciebie"
    you "no właśnie"
    f "No dobra wracając do Kurowskiej"
    f "Najpierw muszę się zapytać czy wolne"
    f "Ostatnio złapałem ją na robieniu skipu C na stole... tak, więc przyjemnie nie było i nie pachniało też dobrze..."
    you "Mam tylko jedno pytanie"
    f "Tak?"
    you "Dlaczego jeszcze nie śpicie? Czy nie jest teraz noc?"
    f "Dzisiaj mieliśmy problem z wodą w mieście i cały dzień byliśmy zajęci tym"
    f "W tym mieście zawsze coś się dzieje.."
    "Filip podchodzi do drzwi i grzecznie puka"
    f "Dobry wieczór, mam nową osobę czy mogę ją wprowadzić tutaj?"
    m "Jasne!"
    play sound "audio/sfx_door_open.mp3"
    "Filip otwiera drzwi i wpycha cię do biura, szybko zamykając za tobą drzwi"
    f "no no no idź idź"

    scene bg office
    stop music

    "..."
    "Przed tobą siedzi Pani Kurowska, która ma taką aurę, że jej wzrok potrafi chłodzić pokój"
    show kurowska with dissolve
    you "Dobry wieczór..."
    k "Witam cię w miasteczku Bratgren! Jak cię zwą?"
    you "Zwą...{w=1} mnie [name]."
    k "Okeeej.. Mam na imię Barbara, jestem prezydentem miasta. Sprawuję tutaj władzę od 17 lat. Co cię tutaj sprowadza?"
    you "Właśnie obudziłem się w lesie, nie wiem kim jestem, nie wiem gdzie jestem, znam tylko swoje imie"
    you "Piotr znalazł mnie i zaprowadził mnie do pani"
    you "No i tyle wiem"
    k "Czyli tak jak wszyscy..."
    "Barbara pisze coś do swojego notatnika"
    k "Jeszcze raz jak masz na imię???"
    you "[name]"
    k "Jakie dziwne imię. Weź mi to przeliteruj"

    $ nameSpelled = '-'.join([f"{letter}{{w=0.5}}" for letter in name])
    you "[nameSpelled]"
    k "Okej mam"


    "{nw}"
    jump kurowskaMysteryMenu

label kurowskaMysteryMenu:
    menu:
        "Docieknij co to znaczy wszyscy.":
            k "Wszyscy, którzy tutaj mieszkają trafili w ten sam sposób do naszego miasta."
            k "Nikt nie wie skąd się tutaj bierzemy, ale jedno wiadomo - jesteśmy tutaj szczęśliwi."
        "Milcz":
            you "{i}Chyba nie wiem o co chodzi... ale boję się jej o to pytać.{/i}"
            you "{i}Może jest jeszcze jakaś agresywna.{/i}"
    you "Mam kwerendę"
    k "Słucham?"
    you "Co jest w lesie poza miastem, i dlaczego to miasto jest w jakichś hebździnkach dolnych"
    k "Ha ha!"
    k "Jeśli wyjdziesz do lasu zjedzą cię potwory albo umrzesz z powodu jakiejś niszowej choroby"
    you "..."
    you "(w szoku)"
    k "No właśnie dlatego Piotr robi te rytuały. Wokół tego miasta jest taka tarcza, która odpycha od siebie zlą energię"
    you "No piotr mi mówił jak on to robi tym onyksem"
    k "Problem jest w tym, że za jakieś 5 lat braknie nam tego onyksu"
    k "Więc albo znajdziemy jakiś sposób na oczyszczanie tego onyksu"
    k "Albo będziemy musieli go przenosić w 5 osób, bo będzie tak ciężki, że inaczej się nie da"
    k "...albo wszyscy umrzemy"
    you "..."
    you "{i}Nie daję zgody na śmierć{/i}"
    you "{i}Na pewno coś wymyślą do tego czasu więc nie muszę się tym przejmować{/i}"
    you "A może pani ma do mnie jakieś pytania?"
    k "Hmm...."
    k "Czy ty cokolwiek pamiętasz?"
    "Ale ty nie pamiętasz nic. Twoja pamięc jest pusta, jak nowy dysk Simsang SSD T1 2TB Titan Gray USB-C"
    "Próbujesz coś sobie przypomnieć, ale znowu zaczyna cię boleć głowa"
    "Tym razem głowa cię boli jeszcze bardziej więc chwytasz się głowy i szybko zaczynasz myśleć o czymś innym"
    you "{i}Ewidentnie coś albo ktoś nie chce, żebym coś pamiętał{/i}"
    you "{i}Na razie lepiej będzie udawać, że nic nie rozumiem{/i}"
    you "{i}Bo jeszcze wyczyszczą mi pamięc jeszcze raz{/i}"
    you "Nic nie pamiętam."
    k "Właśnie nikt w tym mieście nic nie pamięta"
    k "Wszyscy mają jakieś zaniki pamięci"
    k "Ja też."
    you "Chciałem porozmawiać o czymś innym, nie takim ponurym jak śmierć całego miasta,"
    you "Ale śkończyło się na tym, że wszyscy mamy alzheimera"
    you "Było by to zabawne, gdyby nie było to tak straszne"
    k "Jakoś trzeba sobie radzić."
    jump kurowskaBureaucracyMenu


define askedAboutCityHistory = False
define askedAboutHousing = False
define askedAboutWork = False
define commentedOnKurowskasAppearance = False
define rudeToKurowska = False

label kurowskaBureaucracyMenu:
    if askedAboutHousing and askedAboutCityHistory and askedAboutWork:
        jump gettingHouseKeysGood

    k "Czy masz jakieś pytania?"
    menu:
        "Zapytaj o historię miasta." if not askedAboutCityHistory:
            $ askedAboutCityHistory = True
            you "A czy Bratgren ma jakąś historię?"
            k "Wywalę cię zaraz. Oczywiście, że ma."
            you "To proszę coś mi opowiedzieć o tym mieście, bo czuję że ma potężny lore"
            k "No to siadaj i słuchaj"
            k "Islandzka podróżniczka o imieniu Bjork stworzyła to miasto 399 lat temu."
            "Kurowska wskazała swoim pazurem na fontannę na rynku"
            k "Dokładnie tam stała Bjork prawie 400 lat temu i wyczuła źródło energii"
            k "A co roku obchodzimy rocznicę miasta na rynku."
            k "Oczywiście wszystko się dzieje wokół tej fontanny"
            k "Dlatego nasz rynek jest dla nas miejscem świętym."
            k "Jeśli chcesz wiedzieć więcej to moge ci wyporzyczyć książkę na ten temat. Jednak to nie dzisiaj, gdzieś mi się zapodziała"
            you "{i}Warto by było coś się więcej o tym miejscu dowiedzieć, skoro mam tu zostać na zawsze.{/i}"
            jump kurowskaBureaucracyMenu

        "Zapytaj o nocleg." if not askedAboutHousing:
            $ askedAboutHousing = True
            you "Gdzie jest najbliższy hotel czy coś bo nie mam ani domu ani mieszkania, gdzie ja będę spał"
            k "Muszę tylko znaleźć klucze do twojego domu"
            you "Dom?? Za darmo???"
            k "Oczywiście że nie za darmo. Darmowe domy mają tylko ci co pracują"
            k "Powiedzmy że w ten sposób ja inwestuję w ciebie"
            you "Oczywiście że będę pracował!!!"
            k "Mam nadzieję, że mnie nie cyganisz."
            you "{i}I klasa. Dom za darmo? W snach mi się to nie śniło.{/i}"
            jump kurowskaBureaucracyMenu

        "Zapytaj o pracę." if not askedAboutWork:
            $ askedAboutWork = True
            you "A co z pracą?"
            you "Wiem, że filip pracuje w sekretariacie. A co robią inni?"
            you "Inni w sensie przeciętni ludzie"
            k "Powiem ci, że praca to znaczy robić co kolwiek na korzyść miasta."
            k "Są rolnicy, są piekarze, są kurierzy"
            k "A jest na przykład taki pan Vasilij, który mimo tego że mieszka w mieście i korzysta z naszej ochrony przed złem, nie robi kompletnie nic"
            k "Vasilij tylko siedzi w domu i narzeka na rząd"
            you "Nie no coś tam wymyślę"
            you "Chyba umarłbym z nudów gdybym był taki jak on"
            k "No ja też nie wiem jak mu się nie nudzi"
            k "Kompletnie nie jestem w stanie wyobrazić takiego życia bez jakichkolwiek czynności"
            you "{i}Pryszniców on pewnie też nie może wyobrazić{/i}"
            k "Dobra wracając do twojej pracy..."
            "Barbara przegląda dokumenty na stole, potem w stole, potem za nią"
            "Wydaje się, że ona wie że jest praca ale nie może znaleźć tego papieru na stole"
            k "Do jasnej muffinki... Zgubiłam chyba..."
            k "No to w takim razie nie mam nic. Jutro bedę w stanie powiedzieć wiecęj, dlatego dzisiaj jesteś wolny."
            k "Tylko zgłoś się do mnie jutro."
            you "Spoko"
            jump kurowskaBureaucracyMenu

        "Powiedz coś o jej wyglądzie." if not commentedOnKurowskasAppearance:
            $ commentedOnKurowskasAppearance = True
            menu:
                "Powiedz coś o jej ubiorze":
                    you "Czy każdy może kupić takie ubrania?"
                    you "Bo Pani wygląda jak DIVA!"
                    k "Ha ha, dziękuje. Oczywiście, że można, trzeba się tylko zgłosić do naszej krawcowej."
                    k "Jest na rynku, obok piekarni"
                    $ friendship["Kurowska"] += 1
                    jump kurowskaBureaucracyMenu
                "Powiedz coś o jej fryzurze":
                    you "jakie wydarzenia doprowadziły cię do zrobienia sobie tej fryzury"
                    k "Masz jakiś problem z moimi lśniącymi włosami z reklamy maybelline?"
                    you "Nazywanie tego włosami jest dość łaskawym określeniem..."
                    k "Czy ty mnie obrażasz??"
                    you "Myślę że daję ci coś co nazywa się konstruktywną krytyką"
                    k "Zaraz ty i twoja konstruktywna krytyka zostaną wywaleni przez to okno"
                    $ rudeToKurowska = True
                    k "Dobrze w takim razie koniec tego wywiadu. Masz tutaj klucze do twojego domu, a teraz idź zanim cię wywale!"
                    scene bg secretary with vpunch
                    play sound "audio/sfx_door_slam.mp3"
                    you "{i}JESZCZE ŻYJĘ! Byłoby ciężko gdyby mnie wyrzuciła na bruk. Dostałem klucze do domu, o przyjemnych rozmowach nie myślę.{/i}"
                    jump gettingHouseKeysUniversal

label gettingHouseKeysGood:
    k "Jeśli nie masz więcej pytań, masz tutaj klucze do twojego nowego domu."
    k "(ps. Kasia Dowbor go remontowała)"
    you "{i}Tam musi być luksusowo{/i}"
    you "Thank you thank you thank you"
    jump gettingHouseKeysUniversal

label gettingHouseKeysUniversal:
    scene bg cityhallinside
    play music "stillofnight.mp3"
    show piotr 
    "Wychodzisz"
    p "dobrze wszystko? coś ty długo u niej byłeś"
    you "jesteś delulu nie było mnie dosłownie 5 minut"
    p "*patrzy z politowaniem*"
    p "jak ci poszło?"
    you "patrz co mam!! *pokazuje klucze od nowego domu* (#flex)"
    "Piotr jest zazdrosny, ponieważ musiał pracować by dostać dom"
    p "Aha. Okej."
    p "W takim razie muszę iść dokończyć rytuał z wcześniej, w którym mi przeszkodziłeś. ŻEGNAM"
    hide piotr with dissolve
    you "{i}Chyba się na mnie obraził{/i}"
    if wasRudeToPiotr == True:
        you "{i}Chyba przesadziłem w sekretariacie{/i}"
    you "{i}Ale bracie its not that deep{/i}"
    "Przed wyjściem z urzędu miasta patrzysz się na zegar, i widzisz, że jest 23:40"
    jump goingIntoTown
        


label goingIntoTown:
    scene bg citysquarenight with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Wychodzisz z urzędu miasta i idziesz przed siebie"
    "Nie masz pojęcia co teraz robić"
    menu:
        "Chcę iść do domu":
            you "{i}Chyba idę spać...{/i}"
            jump goingHomeFirstNight
        "Chcę zwiedzić miasto":
            you "{i}Chyba nie idę spać...{/i}"
            you "{i}Miasto duże, zobaczę ile ma do zaoferowania.{/i}"
            jump goingIntoTownFirstNight

