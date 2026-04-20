

label filipIntroduction:
    menu:
        "Sprowokuj piotra":
            $ friendship["Piotr"] -= 1
            you "Obsrałeś się jak mnie zobaczyłeś Panie Piotrze więc sybau"
            you "{i}ale dałem do pieca{/i}"
            p "..."
            jump filipIntroduction_after            
        "Milcz":
            you "{i}on nie jest tuff{/i}" 
            jump filipIntroduction_after



label filipIntroduction_after:
    p "Oczyszczałem las, jak mi kazałeś, a on pojawił się koło mnie i zepsuł mój rytuał,"
    p "teraz muszę zacząć od nowa."
    m "Coś mi się wydaje, że są rzeczy ważniejsze."
    m "Ty możesz swoje rytuały zrobić nawet jutro. A [name] mógł w tym lesie umrzeć"
    m "Chodź tu"
    "Podchodzisz trochę bliżej do [filipName[M]]a, on wstaje i podaje ci rękę"
    f "Cześć. Nazywam się [filipName[M]] i witam w pięknym mieście Bratgren. Pewnie masz ogromną ilość pytań?"
    you "No tak"
    f "A czy coś już wiesz o tym mieście?"
    you "No nie"
    "[filipName[M]] jest uradowany tą informacją z jakiegoś powodu"
    f "No to świetnie. Teraz zaprowadzę cię do Kurowskiej, ale najpierw muszę się zapytać czy wolne."
    f "Ostatnio złapałem ją na robieniu skipu C na stole... tak, więc przyjemnie nie było i nie pachniało też dobrze..."
    you "Mam tylko jedno pytanie"
    f "Tak?"
    you "Dlaczego jeszcze nie śpicie? Czy nie jest teraz noc?"
    f "Dzisiaj mieliśmy problem z wodą w mieście i cały dzień byliśmy zajęci tym"
    f "W tym mieście zawsze coś się dzieje.."
    "[filipName[M]] podchodzi do drzwi i grzecznie puka"
    f "Dobry wieczór, mam nową osobę czy mogę ją wprowadzić tutaj?"
    m "Jasne!"
    "[filipName[M]] otwiera drzwi i wpycha cię do biura, szybko zamykając za tobą drzwi"

    scene bg office
    play sound "sounds/sfx_door_open.mp3"

    show kurowska with dissolve
    "Przed tobą siedzi Kurowska, która ma taką aurę, że jej wzrok potrafi chłodzić pokój"
    you "Dobry wieczór..."
    k "Witam cię w miasteczku Bratgren! Jak cię zwą?"
    you "Zwą...{w=1} mnie [name]."
    k "Okeeej.. Jestem [kurowskaName], prezydent miasta. Sprawuję tutaj władzę od 17 lat. Co cię tutaj sprowadza?"
    you "Właśnie obudziłem się w lesie, nie wiem kim jestem, nie wiem gdzie jestem, znam tylko swoje imie"
    k "Czyli tak jak wszyscy..."
    "[kurowskaName] pisze coś do swojego notatnika"

    "Czy chcesz zadać pytanie?"
    jump kurowskaMysteryMenu

label kurowskaMysteryMenu:
    menu:
        "Docieknij co to znaczy wszyscy.":
            k "Wszyscy, którzy tutaj mieszkają trafili w ten sam sposób do naszego miasta."
            k "Nikt nie wie skąd się tutaj bierzemy, ale jedno wiadomo - jesteśmy tutaj szczęśliwi."
            jump kurowskaBureaucracyMenu
        "Milcz":
            you "{i}Chyba nie wiem o co chodzi... ale boję się jej o to pytać.{/i}"
            you "{i}Może jest jeszcze jakaś agresywna.{/i}"
            jump kurowskaBureaucracyMenu


define askedAboutCityHistory = False
define askedAboutHousing = False
define askedAboutWork = False
define commentedOnKurowskasAppearance = False
define rudeToKurowska = False

label kurowskaBureaucracyMenu:
    if askedAboutHousing and askedAboutCityHistory and askedAboutWork:
        jump gettingHouseKeys

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
            "[kurowskaName] przegląda dokumenty na stole, potem w stole, potem za nią"
            "Wydaje się, że ona wie że jest praca ale nie może znaleźć tego papieru na stole"
            k "Do jasnej mufinki... Zgubiłam chyba..."
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
                    scene bg secretary
                    play sound "sounds/sfx_door_slam.mp3"
                    you "{i}JESZCZE ŻYJĘ! Byłoby ciężko gdyby mnie wyrzuciła na bruk. Dostałem klucze do domu, o przyjemnych rozmowach nie myślę.{/i}"
                    jump gettingHouseKeys

label gettingHouseKeys:
    k "Jeśli nie masz więcej pytań, masz tutaj klucze do twojego nowego domu."
    k "(ps. Kasia Dowbor go remontowała)"
    you "Thank you thank you thank you"
    you "{i}Tam musi być luksusowo{/i}"
    scene bg cityhallinside
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
    you "{i}Bracie its not that deep{/i}"
    jump goingIntoTown
        


label goingIntoTown:
    "Wychodzisz z urzędu miasta i idziesz przed siebie"
    "Nie masz pojęcia co teraz robić"
    menu:
        "Chcę iść do domu":
            you "{i}Chyba idę spać...{/i}"
        "Chcę zwiedzić miasto":
            you "{i}Chyba nie idę spać...{/i}"

