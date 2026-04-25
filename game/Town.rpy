define metTomcio = False
define rudeToTomcio = False

label goingHomeFirstNight:
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
    jump wakingUpAfterFirstNight


label goingIntoTownFirstNight:
    "odwracasz się w stronę urzędu miasta i widzisz ogromne jezioro w tle"
    "Ta woda w jeziorze jest całkiem spokojna, prawie jak w basenie"
    "Potem patrzysz w bok i widzisz tę nieodkrytą część małego miasteczka Bratgren"
    "Gdzie ty chcesz iść?"
    menu:
        "JEZIORO!!!":
            jump firstNightLakeVisit
        "MIASTO!!":
            jump firstNightTownWalk

define hasToApologiseToPiotr = False
label firstNightTownWalk:
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
    jump firstNightTownWalkQuestionsMenu

label firstNightTownWalkQuestionsMenu:
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
            jump firstNightTownWalkQuestionsMenu
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
            jump firstNightTownWalkQuestionsMenu
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
            jump firstNightTownWalkQuestionsMenu
        "Wiem już wszystko":
            jump afterFirstNightTownWalkQuestionsMenu

define fountainLoreReceived = False
label afterFirstNightTownWalkQuestionsMenu:
    you "czy jest coś jeszcze co powinienem wiedzieć"
    wp "tak zapomniałam ci powiedzieć czemu w ogóle opowiadam ci o tym kościele"
    you "słucham?"
    wp "w tym kościele jest mnóstwo relikwii"
    wp "na przykład nóż którym zabito bjork"
    wp "teraz jest zamknięty ale jeśli kiedyś będziesz potrzebować odpowiedzi znajdziesz je tutaj"
    you "aha dobra dzięki"
    "opuszczasz teren kościoła a Wiktoria zamyka za tobą bramę"

    you 'to tyle informacji naraz...'
    you 'na pewno jutro wszystko zapomnę'
    wp 'spokojnie, to w porządku zapominać'
    wp 'jeśli będziesz czegoś potrzebować jestem tu żeby pomóc'
    you 'aww dziękuję'
    you 'myślę że najlepiej już pójdę do domu jeszcze go nawet nie widziałem'
    wp 'czekaj jaki dom?? skąd???'
    you 'dom który dostałem od kurowskiej?'
    wp  'CO'
    wp 'jak to dostałeś dom???'
    you '*pokazuje klucze* no od kurowskiej dostałem'
    wp 'czemu ona teraz ma swoje ulubieńce'
    you 'może mi ktoś wytłumaczyć co się dzieje???'
    wp 'kurowska zwykle nie rozdaje domów za darmo'
    you 'to nie było za darmo powiedziała że muszę znaleźć pracę'
    wp 'aaaa ona trochę nie lubi bezrobotnych'
    wp 'cokolwiek robisz pamiętaj żeby płacić podatki wtedy będziesz miał z nią spokój'
    wp 'jest miła tylko dla tych co płacą podatki'
    you 'oho okej'
    you 'dziękuję ci za wszystkie informacje bardzo to doceniam ale teraz chciałbym się położyć'
    you 'dobranoc'
    wp 'pa'
    $ fountainLoreReceived = True
    scene bg citysquarenight with dissolve
    "zaczynasz iść do domu. głowa ciąży ci od nadmiaru informacji które właśnie otrzymałeś."
    "Z wiązku z ciężkim dniem, nie myślisz nad niczym innym niż snem. Z tego powodu od razu kładziesz się spać."
    jump wakingUpAfterFirstNight







