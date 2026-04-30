define metTomcio = False
define rudeToTomcio = False

label t_goingHomeFirstNight:
    "Decydujesz, że ci się nie chce, więc idziesz do swojego nowego domu"
    "Czujesz dreszcze przebiegające po plecach"
    "Ale {w=0.6}nie wiesz dokładnie, co je spowodowało - to, że nie ma żywej duszy,"
    "czy to, że po prostu jest zimno"
    you "{i}Boże czemu jest tak zimno{/i}"
    "Łapiesz się za ramiona próbując się jakoś ogrzać"
    you "{i}Jaka to pora roku{/i}"
    you "{i}Czy oni w ogóle mają tu zimy{/i}"
    you "{i}Chyba że to jest wiosna...{/i}"
    you "{i}nie chcę zimy{/i}"
    "Patrzysz się w górę w poszukiwaniu odpowiedzi, ale widzisz tylko ciemne, puste i nudne niebo"
    "Jedyny fakt, którego jesteś w tym mieście 100%% pewien, to jest to, że fontanna jest magiczna"
    "Podchodzisz bliżej, żeby jej się lepiej przyjrzeć"
    
    scene bg fountainnight with dissolve
    stop music fadeout 10.0
    play sound "sfx_footsteps_a.mp3"

    "Im bliżej jesteś do tej fontanny, tym ciszej się robi"
    "Nie że wcześniej było głośno w środku nocy"
    "Tylko że wtedy słychać było wiatr w koronach drzew, ale teraz {b}wszystko{/b} ucichło"
    "oprócz wody w fontannie"
    "powietrze jest gęste i ciężkie, i ty czujesz to wyraźnie"
    "Wygląda na to, że będziesz musiał wrócić później."
    "Oddalasz się od fontanny (z tym gęstym powietrzem w prezencie) i idziesz do domu"
    scene bg colacocastreetnighta with dissolve
    play music "stillofnight.mp3" fadeout 10.0
    play sound "sfx_footsteps_b.mp3"
    you "{i}Gdzie ja w ogóle mieszkam{/i}"
    "Patrzysz na klucz w swojej dłoni"
    "Do klucza jest przypięty mały breloczek, na którym jest po prostu napisane ULICA Y/N POMOCY NIE WIEM JAK TO NAZWAĆ" # TODO: nazwać tą ulicę ??
    "Dzięki plot armor nie masz problemu ze znalezieniem ulicy z breloczka"
    "Na całej ulicy są tylko trzy domy, a ten na samym końcu jest twój"

    menu:
        "Chcę się przywitać":
            you "Nie chce wyjść na niemiłego, muszę się przywitać."
            "Podchodzisz do pierwszego lepszego domu..."
            you "{i}Czemu ma zamkniętą bramę?{/i}"
            you "{i}Czy to on dla mnie zbudował taki tor przeszkód?{/i}"
            you "{i}Co to ma być? Wipeout?{/i}"
            "Na szczęście jesteś skinny więc po prostu wsadzasz rękę przez pręty bramy i otwierasz ją od środka"
            "...i prawie utknęła ci ręka przy tym"
            "Gdyby ktoś cię teraz zobaczył, tobyś stracił tyle aury"
            "Próbujesz nonszalancko zamknąć za sobą bramę, ale po przejściu kilku kroków się otwiera"
            you "{i}głupia brama{/i}"
            you "{i}to nie mój problem{/i}"
            "Dom tego sąsiada jest strasznie nudny"
            "(to w sumie widać)"
            "[name] podchodzi do drzwi i puka 3 razy, jakby szedł na rozmowę o pracę, i czeka"
            "Nikt nie otwiera, więc [name] puka jeszcze raz, a dokładniej 3 razy"
            "Znowu nikt nie otwiera"
            "Zdecydowałeś, że to jednak nie był najlepszy pomysł robić meet & greet z sąsiadami w nocy"
            "Odwracasz się, żeby odejść, kiedy słyszysz za sobą takie ciche skrzypnięcie"
            you "{i}co to było wtffff{/i}"
            "podnosisz łapę bardzo powoli, mając nadzieję, że znowu usłyszysz to skrzypnięcie"
            "Ale nagle czyjś głęboki głos sprawia że podskakujesz ze strachu"
            m "Jezu no co ty ode mnie chcesz?"
            you "AAAAA"
            "w okamgnieniu się odwracasz i widzisz tego sąsiada - jeszcze zaspanego"
            show tomcio normal with dissolve
            "Gość jest zbudowany jak byk (no co ty nie powiesz) - bardzo wysoki i szeroki"
            you "{i}whoopsie daisy yoo hoo{/i}"
            you "{i}...{/i}"
            you "{i}będę chyba nonchalant{/i}"
            you "Nie strasz tak ludzi, to bardzo niegrzeczne"
            m "???"
            m "To nie {b}ty{/b} pukałeś mi do drzwi?"
            m "W środku nocy?"
            m "czemu tłuczesz w moje drzwi o północy"
            you "No dobra, powiedzmy że masz rację"
            "Sąsiad jest oszołomiony twoją arogancją"
            you "Jestem twoim nowym sąsiadem i chciałem się przywitać"
            you "Przepraszam, że chciałem być miły"
            m "No to cześć?"
            you "{i}za kogo on mnie ma żeby tak się do mnie odzywać{/i}"
            you "Czy to wszystko???"
            m "Ale o czym chcesz gadać jest prawie północ"
            menu:
                "Zapytaj kim on jest":
                    $ metTomcio = True
                    you "Kim jesteś"
                    t "Nazywam się Tomcio"
                    you "I to tyle??"
                    you "Opowiedz coś więcej o sobie na przykład czym się zajmujesz"
                    "Tomcio pochylił się bliżej ciebie i popatrzył się na ciebie z podejrzliwością"
                    t "A po co ci ta informacja"
                    you "{i}Ale dał do pieca{/i}"
                    you "{i}nie wiem jak na to odpowiedzieć{/i}"
                    you "{i}Aha! {w=0.6}Wiem! {w=0.6}Teraz wszystko wiem! {w=0.6}Wiem jak na to odpowiedzieć! {w=0.6}Wiem wiem wiem! {w=0.6}Eureka!{/i}"
                    you "Chcę się upewnić, że moi sąsiedzi goonują etycznie"
                    t "nigdy w życiu nie słyszałem tak oburzającego stwierdzenia"
                    t "no skoro musisz wiedzieć to pracuję dla rządu"
                    you "Aha ok"
                    you "Ale nudna praca. Myślałem że coś ukrywasz"
                    you "No to dziękuję ja idę spać"
                    you "DOBRANOCC"
                    hide tomcio normal with dissolve
                    you "{i}Ten tomcio to chyba spoko gość, tylko trochę dziwny. No cóż sąsiadów się nie wybiera, przeżyję.{/i}"
                "Opowiedz mu wszystko o sobie":
                    you "Dobry wieczór"
                    m "Raczej dobranoc"
                    you "Dobry. {w=0.3} Wieczór. {w=0.3} panie yyy"
                    you "Jak pan się nazywa?"
                    you "w każdym razie nie ważne. Ja byłem pierwszy hihi"
                    you "pewnie już wiesz ale jestem twoim nowym sąsiadem!! (irytująco wesoły ton)"
                    "On robi krok do tyłu i zamyka ci drzwi przed nosem"
                    hide tomcio normal
                    with vpunch
                    play sound "sfx_door_slam.mp3"

                "Ragebait":
                    $ rudeToTomcio = True
                    you "A w sumie nie ważne"
                    "[name] obraca się na pięcie i zaczyna, podskakując, uciekać"
                    m "CZEKAJ"
                    m "boże święty czemu ty uciekasz ode mnie"
                    m "czy ja naprawdę jestem taki groźny"
                    m "Czy to przez to że jestem gruby????"
                    "On wpada w malignę, zaczyna płakać i zamyka drzwi"
                    hide tomcio normal with dissolve

                    you "{i}???{/i}"
            "Wychodzisz przez (teraz otwartą) bramę, i idziesz do domu"
        "Chcę iść spać":
            you "Zmęczyłem się"
            "(niby czym ale ok)"
    "Dom był niedaleko, więc szybko trafiłeś pod drzwi swojego nowego lokalu."
    "Nie wyglądał on przytulnie, ale teraz jest za późno na takie rozmyślania."
    jump h_wakingUpAfterFirstNight


label t_goingIntoTownFirstNight:
    "odwracasz się w stronę urzędu miasta i widzisz ogromne jezioro w tle"
    "Ta woda w jeziorze jest całkiem spokojna, prawie jak w basenie"
    "Potem patrzysz w bok i widzisz tę nieodkrytą część małego miasteczka Bratgren"
    "Gdzie ty chcesz iść?"
    menu:
        "JEZIORO!!!":
            jump l_firstNightLakeVisit
        "MIASTO!!":
            jump t_firstNightTownWalk

define hasToApologiseToPiotr = False
define metWiktoriaP = False
label t_firstNightTownWalk:
    you "{i}Możę znajdę tu coś ciekawego do zwiedzenia. Ten rynek wydaje się być trochę pusty, ale może mnie czymś zaskoczy.{/i}"
    "rozglądasz się po rynku i próbujesz wyobrazić sobie ten coroczny festiwal właśnie tutaj na rynku."
    "Barbara nie powiedziała ci, czym właściwie jest ten festiwal, ani co ludzie wtedy robią, ani nawet czego on dotyczy,"
    "więc ta tradycja pozostaje tajemnicą którą dopiero masz odkryć."
    "Rozglądasz się i zauważasz fontannę, poza którą na rynku nie ma nic."
    "widzisz kościół w oddali i postanawiasz się mu przyjrzeć"
    scene bg churchnighta with dissolve
    #you "{i}{/i}"
    you "{i}W KOŃCU{/i}"
    you "{i}pierwszy raz widzę kogoś na tej ulicy{/i}"
    you "{i}mam nadzieję, że mnie nie ten ktoś nie pobije{/i}"
    "ktoś nieznajomy stoi blisko kościoła."
    "Nie jesteś pewien czy chcesz do tej osoby podejść i porozmawiać czy raczej unikać"
    "...aż w końcu tajemnicza osoba macha do ciebie i gestem zachęca abyś podszedł bliżej"
    you "{i}czego ona chce??{/i}"
    "podchodzisz bliżej do tajemniczej kobiety przed kościołem"
    show wp normal with dissolve
    you "Dobry wieczór?"
    m "Czy my się znamy?"
    you "Nie"
    m "Ty nie pracujesz przypadkiem po drugiej stronie miasta?"
    you "No nie bo jestem tutaj nowy"
    m "Aha"
    m "No to cześć"
    you "..."
    m "..."
    you "..."
    $ metWiktoriaP = True
    wp "Mam na imię Wiktoria"
    you "Miło cię poznać. Mam na imię [name]"
    "uśmiechasz się jak w reklamie nieruchomości"

    $ newName = name.strip().split(" ")[0].lower()#  "Dupa 3.0" -> "dupa"

    wp "no właśnie miałam mówić, że wyglądasz jak [newName]"
    wp "Masz fajne imię"
    wp "[name] [name] [name]"
    "rzucasz jej surowe spojrzenie"
    wp "skoro już tu jesteś to mogę równie dobrze opowiedzieć ci coś o tym mieście"
    "Wiktoria otwiera bramę przed kościołem żeby umożliwić ci bliższe spojrzenie."
    "Zrobiłeś tylko 3 kroki do przodu więc twój widok niewiele się zmienił"
    "(czego się spodziewałeś)"
    wp "wiesz że bjork jest założycielką naszego miasta?"
    you "No tak, kurowska mi o niej mówiła. założyła nasze miasto jakieś czterysta lat temu"
    wp "nie do końca. bjork założyła nasze miasto 399 lat temu a 400 rocznica będzie obchodzona podczas tegorocznych zielonych świątek"
    you "wow ale heca"
    wp "No rel. Bjork to islandzka podróżniczka która to wszystko zaczęła"
    wp "była zwykłą kobietą jak większość kobiet tutaj w bratgren"
    wp "pewnego dnia bjork obudziła się i miała wizję, w której pojawiła się dusza i coś jej tam szeptała"
    "Wiktoria wskazuje na witraż. patrzysz na niego i dopiero z jej pomocą uświadamiasz sobie że to duch."
    "wpatrujesz się w witraż próbując obejrzeć go pod różnymi kątami"
    wp "czy coś jest nie tak?"
    you "nie nie to nic"
    wp "Bjork zrobiła ten witraż swoimi rękami"
    you "Aha teraz ma sens czemu jest taki"
    "patrzy sie na ciebie jakbyś właśnie zabił starą lichwiarkę i jej córkę"
    "{i}Może lepiej nie obrażać ich wierzeń{/i}"
    with vpunch
    you "*gulp* ...tzn ma taki unikalny styl, nigdy wcześniej czegoś takiego nie widziałem"
    wp "{i}No ja myślę{/i}"
    wp "nikt nie wie co ta dusza tam szeptała do bjork a ten witraż to jedyna rekonstrukcja jaką mamy"
    wp "po spotkaniu z tą duszą jej serce wypełniło się determinacją a więc poszła szukać miejsca z najlepszym vibem"
    wp "Bjork dużo pisała w swoim dzienniku."
    wp "pierwsze co napisała to 'If travel is searching, and home what's been found, im not stopping' "
    wp "zaczęła podróżować po całym świecie w poszukiwaniu idealnego miejsca na miasto"
    you "ale diva"
    wp "no rel ona była final girl"
    you "ej rell"
    wp "a wiesz co po tych podróżach zrobiła?"
    you "nie"
    wp "Ale to było pytanie retoryczne"
    you "jezu no dobra mów już"
    wp "szła tu gdzieś przez las, gdy poczuła taki mega fajny vibe"
    wp "wiedziała od razu, że ten vibe był lepszy niż wszystkie i od razu wiedziała że to miejsce nadaje się na miasto"
    wp "ale ostatnio ta tarcza osłabła i czarodzieje tacy jak Piotr muszą pomagać nam chronić Bratgren"
    you "Właśnie obudziłem się obok Piotra jak robił jakiś rytuał"
    wp "Serio?"
    you "Noooo"
    you "Ja od razu myślałem, że to jego wina i wgl masakra z nim"
    you "Ale chyba jest fajny"
    wp "No fajny jest on wszystkim pomaga"
    you "Weź bo teraz wyszedłem na niemiłego"
    wp "No to przeproś go"
    $ hasToApologiseToPiotr = True
    you "No no przeproszę"
    you "No ale dobra wracając do tej bjorkowej"
    you "Ona to miasto sama zbudowała?"
    wp "nie no oczywiście że nie."
    wp "po pierwsze wtedy miasto było dużo mniejsze. minęło w końcu czterysta lat trochę się rozrosło"
    wp "a po drugie nie była sama"
    you "OKEJ...??"
    wp "była sabrina carpenter"
    "nie wiesz czemu ale to imię brzmi znajomo chociaż nikt nigdy ci go nie wspominał."
    "to bardzo dziwne i cię niepokoi"
    you "{i}gdieś to imię słyszałem{/i}"
    you "{i}czemu ja ją kojarzę{/i}"
    you "{i}chyba jest ważna{/i}{nw}"
    wp "Halo czy ty mnie słuchasz?"
    you "Yy tak tak mów"
    wp "A więc to była najlepsza przyjaciółka bjork i też jakby ironicznie cieśla."
    wp "zbudowały kilka domów i ludzie zaczęli się pojawiać tak jak ty"
    wp "btw do dziś nie wiadomo skąd ci ludzie się biorą"
    you "Nawet bjork nie wiedziała?"
    wp "No tak"
    wp "A teraz plot twist. Zgadnij jak ona umarła"
    you "została łysa?"
    wp "Co? Nie"
    wp "jej śmierć była BARDZO tragiczna"
    wp "była prezydentem tylko 23 lata kiedy sabrina ją zdradziła i dźgnęła nożem"
    you "{i}a teraz mi jest łyso bo nie wiedziałem tego{/i}"
    you "{i}wiedziałem, że sabrina jest ważna{/i}"    
    wp "Zginęła w biurze kurowskiej. dokładnie tam gdzie ona teraz siedzi"
    wp "ostatnie słowa bjork to były 'I thought i could organize freedom. How scandinavian of me'"
    wp "To był tragiczny dzień dla całego miasta i od tamtej pory co rok duchy powstają z martwych"
    jump t_firstNightTownWalkQuestionsMenu

label t_firstNightTownWalkQuestionsMenu:
    you "{i}mam tyle pytań...{/i}"
    menu:
        "Co się stało z sabriną":
            wp "Ona była w gorącej wodzie kąpana po tym jak zabiła Bjork"
            wp "W sensie nie było wody a tylko temperatura"
            wp "Bo została spalona na stosie"
            you "ej szczerze też bym ją spalił za to"
            wp "No rel"
            you "No ale czekaj"
            you "Czemu Sabrina ją zdradziła???"
            wp "Nikt nie wie"
            wp "Ale chyba była delulu"
            you "{i}czemu nikt w tym mieście nie pamięta NAJWAŻNIEJSZYCH rzeczy z historii to jest takie dziwne{/i}"
            jump t_firstNightTownWalkQuestionsMenu
        "Jak umarła Bjork":
            wp "Bjork była z Islandii co nie?"
            you "No no"
            wp "No to chcieliśmy uczcić tradycje tego kraju kiedy ona umarła"
            wp "ciało bjork zostało położone na łodzi którą wypuszczono na wyjątkowo spokojne jezioro świtezianka"
            you "czemu położyliście ją na łódź"
            wp "Jezu czy ty mnie słuchasz... mówiłam że takie są tradycje"
            you "no dobra już"
            you "i to wszystko?"
            wp "A no tak zapomniałam najważniejszej rzeczy"
            wp "Ogólnie mieliśmy podpalić tą łódkę ale jakaś siła wciągnęłą ją pod wodę"
            you "jak można o takim czymś zapomnieć??"
            jump t_firstNightTownWalkQuestionsMenu
        "Czy mogę rozmiawiać z tymi duchami":
            wp "PO PIERWSZE..."
            wp "to nie są duchy tylko dusze"
            wp "wkurzą się jeśli nazwiesz je duchami"
            you "{i}Duchy i dusze to prawie to samo. Przecież mnie nie ukrzyżują jak ich zmisgenderuje...{/i}"
            you "ups przepraszam nie wiedziałem"
            wp "nic się nie dzieje"
            wp "i tak, możesz z nimi rozmawiać. tylko podczas tego festiwalu"
            wp "a właściwie to one mogą mówić tylko przez te siedem dni"
            wp "możesz je zobaczyć przez cały rok ale nie bój się nie będą cię nawiedzać"
            jump t_firstNightTownWalkQuestionsMenu
        "Wiem już wszystko":
            jump t_afterFirstNightTownWalkQuestionsMenu

define fountainLoreReceived = False
label t_afterFirstNightTownWalkQuestionsMenu:
    you "Czy jest coś jeszcze, co powinienem wiedzieć?"
    wp "Tak, zapomniałam ci powiedzieć, czemu w ogóle opowiadam ci o tym kościele."
    you "Słucham?"
    wp "W tym kościele jest mnóstwo relikwii."
    wp "Na przykład nóż, którym zabito Bjork."
    wp "Teraz jest zamknięty, ale jeśli kiedyś będziesz potrzebować odpowiedzi, znajdziesz je tutaj."
    you "Aha, dobra, dzięki."
    "Opuszczasz teren kościoła, a Wiktoria zamyka za tobą bramę."
    "Zrobiłeś tylko 3 kroki do tyłu więc twój widok niewiele się zmienił"
    "(Czego się spodziewałeś)"
    you 'To tyle informacji naraz...'
    you 'Na pewno jutro wszystko zapomnę.'
    wp 'Ej rell'
    wp "Nie wiem jak ja to pamiętam."
    wp 'W każdym razie, jeśli będziesz czegoś potrzebować, jestem tu, żeby pomóc.'
    you 'Aww, dziękuję.'
    you "Która jest godzina?"
    wp "No jest już po północy"
    you "Czemu ty łazisz an rynku po północy"
    wp "Yyyy.."
    wp "Nie interesuj się."
    you 'Myślę, że najlepiej już pójdę do domu. Jeszcze go nawet nie widziałem.'
    wp 'Czekaj, jaki dom?? Skąd???'
    you 'Dom, który dostałem od Kurowskiej?'
    wp 'CO?'
    wp 'Jak to dostałeś, dom???'
    you '*pokazuje klucze* No, od Kurowskiej dostałem.'
    wp 'Czemu ona teraz ma swoje ulubieńce?'
    you 'Może mi ktoś wytłumaczyć, co się dzieje???'
    wp 'Kurowska zwykle nie rozdaje domów za darmo.'
    you 'To nie było za darmo, powiedziała, że muszę znaleźć pracę.'
    wp 'Aaaa, ona trochę nie lubi bezrobotnych.'
    wp 'Cokolwiek robisz, pamiętaj, żeby płacić podatki. Wtedy będziesz miał z nią spokój.'
    wp 'Jest miła tylko dla tych, co płacą podatki.'
    you 'Oho okej.'
    you 'Dziękuję ci za wszystkie informacje, bardzo to doceniam, ale teraz chciałbym się położyć.'
    you 'Dobranoc.'
    wp 'Pa.'
    $ fountainLoreReceived = True
    scene bg citysquarenight with dissolve
    "Zaczynasz iść do domu. Głowa ciąży ci od nadmiaru informacji które właśnie otrzymałeś."
    "Z wiązku z ciężkim dniem, nie myślisz nad niczym innym niż snem. Z tego powodu od razu kładziesz się spać."
    jump h_wakingUpAfterFirstNight


label t_goingToTownToKurowskaDueToHungerDayTwo:
    scene bg citysquareday with dissolve
    play sound "sfx_footsteps_b.mp3"
    "Idąc do Kurowskiej podziwiasz budynki i przyrodę, ponieważ dzień wcześniej nie dało się tego zrobić."
    "Droga do urzędu miasta była bardzo przyjemna, jednak najgorszą częścią było oparcie się zapachom wydobywającym się z piekarni"  
    "Brzuch ci burczy, niestety nie masz żadnych pieniędzy by zapłacić za przyszły posiłek"
    you "{i}NIE WYTRZYMAM... taki jestem głodny. Trzeba było wczoraj od kogoś pożyczyć pieniądze. No cóż, muszę jeszcze wytrzymać do końca dnia, aż otrzymam moją dzisiejszą wypłatę.{/i}"
    "Ulice teraz tętnią życiem, każdy spieszy się do pracy, w niektórych momentach nawet ciężko przecisnąć się przez tłumy."
    "Jednak nikt nie odważy się zbliżyć do fontanny."
    "Patrzysz w górę i dziwisz się, że dalej nie widać słońca"
    "Ludzie są prawdopodobnie przyzwyczajeni do niekończących się chmur stratus pokrywających niebo"
    "Gdy podchodzisz do urzędu, on znowu robi na tobie wrażenie, nie tak wielkie jak wczoraj, ale dalej jest bardzo inponujące."
    "Nie ma czasu do stracenia i wchodzisz do budynku, szukając Filipa"
    jump ch_goingToTownToKurowskaDueToHungerDayTwoPartTwo

define workedAtVasili = False
define workedAtFilip = False
label t_goingToFindAJob:
    scene bg citysquareday with dissolve
    play sound "sfx_door_open.mp3"
    "Wychodzisz na zewnątrz żeby zastanowić się co powinieneś zrobić dalej."
    "Jak powiedziała kurowska powinieneś wybrać kogoś kogo znasz i pójść do niego żeby poprosić o pracę."
    "Ponieważ nie chcesz umrzeć z głodu dzisiaj."
    "Stoisz na rynku i rozglądasz się, jakbyś miał całować ziemie, trzymając cyprysowy krzyżyk"
    "Do kogo idziesz pracować?"
    menu:
        "Vasili (to jest ta ciekawsza opcja)" if metVasili:
            you "{i}Pójdę do niego tylko dlatego, że jestem ciekaw{/i}" 
            you "{i}Poza tym chyba nie mam innej opcji{/i}" 
            $ workedAtVasili = True
            jump l_workingAtVasili
        "Filip":
            you "{i}Kurowska nie ma dla mnie roboty, ale Filip już może mieć.{/i}" 
            $ workedAtFilip = True
            jump ch_workingAtFilip
    
label t_gotMoney:
    scene bg citysquareday with dissolve
    "Masz dość bycia głodnym, więc idziesz prosto do BBB."
    "(Big Buły Bakery)"
    jump t_gotMoneyBakeryEntrance

label t_gotMoneyBakeryEntrance:
    scene bg bakeryfrontday with dissolve
    "Piekarnia jest rzeczywiście duża. Zapachy rozchodzące się po ulicy prowadzą cię do szału."
    "Zapach drożdży unosi się w powietrzu, a za szybą jest wiele wypieków."
    scene bg bakeryinside with dissolve
    "Pierwsze co zauważasz w środku to plakaty Taylor Spit."
    "Ale{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}. Jest kolejka."
    show wp normal at leftish with moveinleft
    show fraucrusty normal at center with moveinleft
    show rafal normal at rightish with moveinright
    "Przed tobą są dwie osoby, a pierwszą jest Frau Crusty."
    if metWiktoriaP:
        you "O hej."
        wp "No cześć! Co tam?"
        you "Masakra... Musiałem pracować..."
        wp "Do kogo poszedłeś?"
        if workedAtFilip:
            you "Do Filipa."
            you "Kazał mi przenosić dokumenty do Kurowskiej."
            you "A jak już skończyłem, Kurowska kazała mi z powrotem przenieść te listy."
            you "Bo to on ma je czytać."
            wp "Trzeba było poprosić pieniądze i wyjść po czymś takim."
            wp "I skibidi."
        if workedAtVasili:
            you "Do Vasiliego."
            if endorsedCommunism:
                you "Wiesz co, nie było źle."
                you "Mamy podobne poglądy polityczne."
                "Wiktoria robi bombastic side eye."
            else:
                you "Jezu, to była masakra, cały czas o komuniźmie gadał."
            you "Szkoda gadać."
            you "Ty go znasz lepiej ode mnie, pewnie wiesz jak to wyglądało."
            wp "Let me guess."
            wp "Śpiewał 'Międzynarodówkę'?"
            you "Tak..."
            wp "Współczuję..."
    jump t_gotMoneyBakeryCustomer

label t_gotMoneyBakeryCustomer:
    frau "A cóż to za bezczelne pytanie?"
    frau "Oczywiście, że mam pieniądze."
    frau "Tylko dzisiaj brakuje mi 23 foryntów."
    frau "Mogę je przynieść jutro."
    m "No nie jestem bankiem. To tak nie działa."
    m "To proszę je przynieść jutro."
    frau "Ale mam dzisiaj urodziny!!!"
    menu:
        "Daj jej trochę monet":
            you "Masz."
            frau "Mój gyatt tutaj utknie na dobre!"
            frau "Dziękuję."
            with vpunch
            show fraucrusty normal at offscreenleft with move
            "Frau Crusty wychodzi z piekarni z tortem skipem C"

        "Udawaj, że nic nie słyszałeś":
            frau "Wszyscy jesteście bezczelni i agresywni."
            with vpunch
            show fraucrusty normal at offscreenleft with move
            "Frau Crusty wychodzi z piekarni bez tortu skipem C"
    hide fraucrusty
    jump t_gotMoneyBakeryTea

label t_gotMoneyBakeryTea:
    wp "Okeeej."
    m "Hejka."
    wp "No cześć, co tam?"
    m "A w sumie nic, w malignie byłem cały dzień."
    wp "Tak, standardowo."
    "Oboje zaczęli się śmiać."
    wp "Poproszę 3 buły Rafała."
    m "Jasne."
    "Z tyłu widać całe koszyki z bułami Rafała."
    "Patrzysz się na te buły jak na monoporcje z LA"
    "Tylko że buły Rafała nie kosztują $15 za 150g"
    "Nie masz zielonego pojęcia jeśli chodzi o pieniądze w tym mieście"
    "Niby coś tam masz, ale nie wiesz czy tego starczy na jedną bułę, czy sto."
    you "{i}Te buły są mega popularne tutaj{/i}"
    you "{i}Ale bym zjadł taką..{/i}"
    m "Proszę."
    "Nagle wchodzi kolejny nieznany ci mężczyzna."
    "Wygląda jak jakiś alfons."
    show niuniu normal at leftish
    m "Jezu no znowu ty."
    show wp normal at rightish
    show rafal normal at left
    m "Tak, Rafale, to ja!"
    r "No co ty chcesz ode mnie, znowu?"
    m "Pokaż, co masz pod kapeluszem."
    wp "(szeptem) To jest Niu Niu."
    wp "Ogólnie to jest taki typ, co wymyśla teorie spiskowe w tym mieście."
    wp "I tym razem ofiarą jest Rafał."
    wp "On był na koncercie Taylor Spit i podczas tego koncertu ona rzuciła w niego swój kapelusz."
    wp "Od tego dnia cały czas go nosi."
    wp "A Niuniu wymyślił, że on coś ukrywa pod tym kapeluszem."
    r "Nie, dobra, mam dość."
    "Rafał wyciąga miotłę i uderza Niunia."
    with vpunch
    n "AAAAA"
    r "Sharp or dull"
    n "Sharp?"
    r "Nie. To jeszcze raz."
    with vpunch
    "Uderza go jeszcze raz."
    n "No, to jest sharp."
    r "Wyjdź z mojej piekarni, bo zaraz ci sharp or dull zrobię cegłą."
    n "Dobra, dobra."
    show niuniu normal at offscreenleft with move
    show wp normal at leftish with move
    show rafal normal at rightish with move
    you "Współczuję."
    you "Czy ty naprawdę masz tu gdzieś cegłę?"
    r "Tak. Jestem przygotowany."
    "Wyciągnął obiema łapami wielką czerwoną cegłę i z dumą pokazał ci ją, jakby była jego dzieckiem."
    "Cegła była stara. Naprawdę stara."
    "Już na pierwszy rzut oka widać było, że nie sposób określić jej wieku, o czym świadczyły niezliczone odpryski i rysy."
    "W rzeczywistości cegła była tak stara, że przypisanie jej jakiejkolwiek liczby byłoby obrazą - nie tylko dla niej,"
    "ale i dla osoby, która ją wykonała."
    "Samo nazwanie jej 'starą' oznaczało wymazanie stuleci, które ta cegła przetrwała."
    "Cegła dawno straciła ostre krawędzie i teraz była zaokrąglona,"
    "niemal jakby była wielokrotnie używana."
    "Jeden z rogów był szczególnie obtłuczony i nawet najmądrzejsza osoba w tym mieście nie byłaby w stanie stwierdzić, dlaczego ani kiedy do tego doszło."
    "Tylko Rafał mógłby to wiedzieć - to znaczy, jeśli w ogóle pamięta, co się z nią stało."
    "Jedynym zastosowaniem tej cegły jest rzucanie,"
    "więc starasz się nie wyciągać pochopnych wniosków co do tego, kim jest ofiara."
    "Patrząc na obtłuczony róg, można było dojść do wniosku, że jest to efekt licznych podróży powietrznych."
    "Można by rzec, że to cud, iż cegła jeszcze nie pękła na pół."
    "A jednak trzymała się, czego nie można powiedzieć o niektórych związkach."
    "Gdziekolwiek Rafał dotyka cegły łapami, osypuje się z niej kurz i drobinki gliny,"
    "jakby było to zjawisko całkowicie naturalne."
    "Rafał jednak całkowicie ignoruje bałagan, który właśnie narobił, jakby był do tego przyzwyczajony."
    "Ignoruje również pył na swoich miękkich łapach, najwyraźniej uznając go za problem przyszłości."
    "W tym momencie każdy rozsądny człowiek przestałby myśleć o cegle."
    "Ty tego jednak nie robisz."
    "Cegła miała jedną stronę wyraźnie ciemniejszą od pozostałych, jakby przez lata była wystawiona na działanie żywiołów,"
    "podczas gdy reszta spoczywała bezpiecznie w ścianie."
    "Prawdziwi naukowcy mogliby poświęcić całe życie badaniu tej różnicy i nadal nie dojść do porozumienia."
    "Tak tajemnicza była ta cegła."
    "Nie sposób stwierdzić, czy Rafał ją wyjął, czy też wypadła sama."
    "Można jednak odnieść wrażenie, że należy do tego miejsca - jej przygaszony czerwony kolor zdawał się pasować do reszty piekarni."
    "Przy bliższym przyjrzeniu się dostrzegasz jej niedoskonałości - ślady czasu."
    "Pęknięcia były wypełnione pyłem tak starym i tak głęboko osadzonym,"
    "że nawet woda nie byłaby w stanie go wypłukać."
    "Stał się on częścią tej cegły, jakby należał do niej od zawsze."
    "Cegła była prawdopodobnie starsza od ciebie i znajdowała się w tym mieście na długo przed twoimi narodzinami."
    "Była świadkiem setek, jeśli nie tysięcy ludzi, oraz milionów słów wypowiedzianych w jej obecności."
    "Cegła zna wszystkie sekrety miasta - ale nie może ich zdradzić."
    "Najwyraźniej miała też swoje miejsce pod biurkiem Rafała, tam, gdzie prowadził kasę i zajmował się codziennymi sprawami."
    "Nie każdy klient wiedział, ani nawet mógł podejrzewać istnienie tej cegły."
    "Jeśli Rafał wyciągnął ją przy tobie, oznaczało to jedno z dwóch:"
    "albo jesteś ofiarą,"
    "albo jego przyjacielem."
    "Zauważasz również drobne, wielokolorowe plamy rozsiane po jej powierzchni."
    "Każda z nich miała inny kształt, rozmiar i - zapewne - własną historię."
    "Jedna mogła powstać dwa dni temu, inna dwa lata temu, i nie było sposobu, by to rozróżnić."
    "Patrzysz na małe otwory w cegle, gdy nagle coś zaczyna do ciebie docierać."
    "Cegła sprawia, że czujesz coś, czego wcześniej nie czułeś."
    "Przynajmniej nie w tym mieście."
    "Z powodów, których nie potrafisz wyjaśnić, patrzenie na nią napełnia cię determinacją."
    "Twoje plany - te, które odkładałeś - nagle wydają się nie tylko możliwe, ale wręcz konieczne."
    "Nie jesteś w stanie zignorować myśli, które pojawiają się w twojej głowie."
    "Wzdychasz głęboko, niemal dramatycznie, jakbyś chciał,"
    "żeby wszystkie inne cegły w tej przytulnej piekarni wiedziały, że rozumiesz."
    "Rozumiesz historię, przez którą przeszła ta cegła."
    "Ta cegła i jej historia inspirują cię, by iść dalej i się nie poddawać."
    "Dla zwykłego człowieka to tylko cegła."
    "Ale ty widzisz w niej coś więcej."
    "Odnajdujesz w niej źródło inspiracji i determinacji."
    "Cegła była kiedyś częścią czegoś większego - czegoś bardziej monumentalnego - choć nie potrafisz powiedzieć czego."
    "Z cegieł można zbudować wszystko - od małego muru po coś znacznie większego."
    "Tak jak jedna z tych cegieł, jesteś częścią tego miasta."
    "Miasta, które cię przyjęło."
    r "Jezu, mam go dość, on tak mnie irytuje."
    you "Nie dziwię ci się."
    r "..."
    r "No dobra, co tam chciałeś?"
    "Zapomniałeś o jedzeniu przez to, co się właśnie wydarzyło."
    you "Poproszę 3 buły Rafała."
    r "Jasne."
    r "Ale czekaj, nie widziałem cię wcześniej."
    r "Nie pracujesz przypadkiem na drugim końcu miasta?"
    wp "No właśnie, też mi się tak wydawało."
    you "Nieee, jestem tutaj nowy."
    you "Urodziłem się wczoraj, jak Konrad."
    "Rafał uważnie cię słucha, wkładając buły do papierowej torebki."
    r "Aha, ma sens."
    you "Widzę, że masz plakaty Taylor Spit."
    r "Znasz ją?"
    you "Tak. Kojarzę ją."
    r "Wow, ale heca."
    "Wyciągasz bułę Rafała i zaczynasz ją jeść."
    "Ale nie tak normalnie, jakbyś jadł kajzerkę z Biedronki."
    "Tylko jak homofob jedzący banan."
    "Odrywasz pierwszy kawałek bułki ręką i Rafał patrzy się na ciebie, jakbyś popełnił zbrodnię."
    r "Co ty robisz..."
    you "W sensie?"
    you "Jem."
    r "Nie umiesz w savoir vivre..."
    you "Co???"
    r "Daj mi to. Pokażę ci, jak to się je."
    "Rafał gryzie tę bułkę jak normalna osoba."
    r "No, teraz mam nadzieję, że umiesz."
    r "A tak na marginesie, za dużo soli wsypałem do ciasta."
    you "Imo jest smaczna."
    you "Lubię sól."
    you "Masz jakieś wersje tej buły, czy tylko takie common jak jajo w Adopt Me?"
    r "No, mam tylko takie zwykłe, bo nie mam pomysłu."
    you "Hmmm"
    you "No właśnie, ta z solą jest dobra, więc tych na pewno musisz więcej zrobić."
    wp "Czy ty już kiedyś jadłeś bułę Rafała?"
    you "Tak. Filip mi dał, bo byłem głodny."
    wp "Ma sens."
    r "Okej, dobra, masz fajną aurę. Chcesz z nami wypić trochę herbaty?"
    you "Oczywiście!!"
    "Rafał znika w kuchni, ale szybko wraca z kubkami i cukrem."
    r "Usiądźcie, proszę."
    you "Wy się znacie?"
    wp "Tak. Poznałam go w tej piekarni."
    r "Wyczułem dobry vibe od niej, macie podobną aurę."
    you "{i}oby nie zieloną{/i}"
    "Rafał podchodzi do drzwi i zamyka je na klucz, sprawdzając, czy nikt nie idzie."
    "Jeszcze raz idzie do kuchni, ale tym razem przynosi gorącą wodę i matchę."
    r "Czekaj, bo zapomniałem cię zapytać."
    r "Co ty chcesz do picia?"
    you "A co tu przyniosłeś?"
    r "Matchę."
    you "KOCHAM MATCHĘ."
    wp "Matching!!!"
    "Przesuwasz się trochę bliżej ściany, żeby ktoś mógł usiąść obok ciebie."
    you "A WIĘC..."
    you "Spill the {i}tea{/i}"
    "Oboje zaczynają się śmiać."
    wp "Nie chcę brzmieć jak Niuniuś, którego Rafał pobił miotłą, ale..."
    wp "Muszę zapytać."
    wp "Czy ty też uważasz, że to miasto coś ukrywa?"
    "Nie zajmuje ci dużo czasu, żeby odpowiedzieć na to pytanie."
    "Od kiedy Kurowska opowiedziała ci o tym mieście, wiedziałeś, że coś jest nie tak."
    "Trudno powiedzieć, czy to była twoja inteligencja,{w=0.5} czy po prostu jesteś normalnie taki podejrzliwy wobec wszystkiego."
    you "No tak."
    you "Imo to miasto ogólnie jest dziwne."
    you "Na przykład, czemu to miasto leży w jakimś losowym mieście?"
    you "I dlaczego tu jest tylko jedno miasto?"
    you "Ja mam uwierzyć w to, że nikomu nie chciało się osiedlić gdzieś indziej?"
    wp "NO WŁAŚNIE."
    if knowsAboutVasiliGrandfatherGhost:
        you "Dowiedziałem się od Vasiliego, że to jezioro jest jakieś magiczne."
        you "Bo pojawia się tam duch jego dziadka."
    if metWiktoriaP:
        you "Od ciebie też dużo się dowiedziałem."
        "Patrzysz się na Wiktorię."
    if seenBjorkGhost:
        you "Poza tym widziałem dusze Bjork."
    you "Dziwne to wszystko."
    wp "WIDZISZ RAFAŁ"
    wp "Mówiłam ci."
    r "No dobra, powiedzmy, że masz rację."
    r "I co teraz?"
    wp "Nie wiem, ale nie będę mogła zasnąć po takim czymś."
    wp "Trzeba coś zrobić, po prostu."
    you "No rel."
    you "Jest może jakieś muzeum w tym mieście?"
    wp "No jest. To jest ten kościół."
    you "No to idziemy tam."
    wp "Okej."
    wp "Mogę jutro o 10:00."
    you "No to spotykamy się na rynku o 10:00."
    wp "Dobra."
    r "A ja co?"
    wp "Ale czy ty chcesz z nami iść do kościoła?"
    r "Nie."
    wp "No właśnie."
    you "Dobra, to wiecie co.."
    you "Dziękuję za herbatę, jesteście mega fajni."
    you "Ale ja muszę iść."
    you "Popatrzę się jeszcze raz na tę fontannę na rynku i pójdę do krawcowej."
    you "Bo nie mam żadnych ubrań."
    wp "Paaa"
    r "Dowidzenia, senorita."
    you "{i}Jestem dumny z siebie{/i}"
    you "{i}Chyba znalazłem besties w tej piekarni{/i}"
    scene bg bakeryfrontday with dissolve
    "Wychodzisz i idziesz prosto do tej fontanny."
    "Na szczęście fontanna jest blisko."
    scene bg fountainday with dissolve
    stop music fadeout 5
    "Powietrze dalej jest gęste przy tej fontannie."
    "Patrzysz się na tę fontannę inaczej, ponieważ już wiesz, że coś jest nie tak."
    "Analizujesz każdy centymetr kwadratowy tej fontanny jak teksty piosenek."
    "W końcu twój wzrok pada na napis w obcym języku, którego wcześniej nie widziałeś."
    you "Co za dziad to pisał..."
    show bjork normal with dissolve
    if seenBjorkGhost:
        you "Znowu ty."
    else:
        you "Hejka?"
        you "Czekaj, czy ty nie jesteś Bjork przypadkiem?"
        bjork "Jestem."
        you "Omg, widziałem twój portret."
    "Jesteś w szoku, że widzisz duszę Bjork przed sobą."
    "Nikt inny na rynku pewnie tego nie widzi, ponieważ nikt na to nie reaguje."
    "Wygląda, jakbyś miał schizofrenię przez to, że gadasz do fontanny."
    bjork "{i}Underneath our feet{/i}"
    bjork "{i}Crystals grow like plants{/i}"
    bjork "{i}Listen how they grow{/i}"
    you "Czekaj, tu ja zaraz wrócę."
    bjork "Nie ufaj w{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    scene bg bakeryfrontday with dissolve
    "Biegniesz z powrotem do piekarni, żeby powiedzieć Rafałowi i Wiktorii o tym, co właśnie zobaczyłeś."
    "I tak ci pewnie nie uwierzą, ale musisz spróbować."
    "Wiesz, jest duża szansa, że będziesz wyglądał jak idiota, jeśli na serio tylko ty możesz widzieć Bjork."
    "Bo jak nie, to serio masz schizofrenię."
    scene bg bakeryinside with vpunch
    you "Duch Bjork jest przy fontannie."
    "Wiktoria nie traci ani sekundy i wybiega z piekarni."
    "Rafał biegnie za Wiktorią, nawet nie zamykając piekarni."
    scene bg fountainday with dissolve
    show wp normal at leftish with moveinleft
    show rafal normal at rightish with moveinleft
    r "Nikogo tu nie ma."
    you "Nie ma szans, że ona zrobiła ze mnie idiotę."
    you "Zrobiła ze mnie idiotę jak w jakimś stereotypowym filmie o duchach."
    wp "Nie wiem jak, Rafał, ale ja ci wierzę."
    wp "Na pewno coś widziałeś."
    r "No, w sumie."
    you "I co teraz?"
    wp "Nie wiem."
    r "Nie wiem."
    you "Bjork pewnie nas podsłuchiwała w tej piekarni."
    you "{i}Jeśli ty to słyszysz, proszę mnie nie nawiedzać{/i}"
    you "{i}Bo nie wytrzymam{/i}"
    "Patrzycie się na tę fontannę, ale nic dziwnego się nie dzieje."
    r "Dobra, ja chyba wracam."
    wp "No, ja już też idę."
    you "Naprawdę przepraszam, że was tak oszukałem trochę."
    wp "Ok."
    you "No to cześć."
    r "Cześć siedem"
    "Po raz drugi wychodzisz z piekarni i tym razem idziesz prosto do krawcowej"
    "Bez żadnych duchów lub jakiejś fontanny"
    "Na szczęście to nie było trudne, bo zakład krawiecki jest tuż obok piekarni"
    "Zakład krawiecki wygląda tak ostentacyjnie, że aż stoisz i się gapisz"
    "Jest pięknie"
    "Kiedy w końcu się ogarniasz, wraca ci logiczne myślenie i zaczynasz myśleć o cenach"
    "Raczej nie masz tyle kasy, żeby coś kupić w takim miejscu"
    "Wchodzisz do środka i się rozglądasz."
    "Wszystko jest zastawione pięknymi sukienkami, koszulami, spodniami i innymi ubraniami, których nazw nie znasz"
    "Odwracasz głowę i widzisz zwykłe białe koszule i nudne spodnie, które bardziej pasują do twojego budżetu"
    "Wtedy słyszysz głos kobiety z kąta. To była krawcowa"
    "Na początku jej nie zauważyłeś przez te wszystkie kolorowe ubrania wokół niej"
    you "{i}Idealny kamuflaż{/i}"
    m "Dzień dobry!"
    you "Dzień dobry!"
    you "Nazywam się [name] i jestem nowy w tym mieście."
    ww "Masz fajne imię."
    you "A dziękuję dziękuję"
    return








