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
    "Jedyny fakt, którego jesteś w tym mieście 100% pewien, to jest to, że fontanna jest magiczna"
    "Podchodzisz bliżej, żeby jej się lepiej przyjrzeć"
    
    scene bg fountainnight with dissolve

    "Im bliżej jesteś do tej fontanny, tym ciszej się robi"
    "Nie że wcześniej było głośno w środku nocy"
    "Tylko że wtedy słychać było wiatr w koronach drzew, ale teraz {b}wszystko{/b} ucichło"
    "oprócz wody w fontannie"
    "powietrze jest gęste i ciężkie, i ty czujesz to wyraźnie"
    "Wygląda na to, że będziesz musiał wrócić później."
    "Oddalasz się od fontanny (z tym gęstym powietrzem w prezencie) i idziesz do domu"
    you "{i}Gdzie ja w ogóle mieszkam{/i}"
    "Patrzysz na klucz w swojej dłoni"
    "Do klucza jest przypięty mały breloczek, na którym jest po prostu napisane ULICA Y/N POMOCY NIE WIEM JAK TO NAZWAĆ" # TODO: nazwać tą ulicę ??
    "Dzięki plot armor nie masz problemu ze znalezieniem ulicy z breloczka"
    "Na całej ulicy są tylko dwa domy, a ten na samym końcu jest twój"

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
            "Gość jest zbudowany jak byk (no co ty nie powiesz) - bardzo wysoki i szeroki"
            you "{i}whoopsie daisy yoo hoo{/i}"
            you "{i}...{/i}"
            you "{i}będę chyba nonchalant{/i}"
            you "Nie strasz tak ludzi, to bardzo niegrzeczne"
            m "???"
            m "To nie {b}ty{/b} pukałeś mi do drzwi?"
            m "W środku nocy?"
            m "czemu tłuczesz w moje drzwi o 23"
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
                    you "{i}Ten tomcio to chyba spoko gość, tylko trochę dziwny. No cóż sąsiadów się nie wybiera, przeżyję.{/i}"
                "Opowiedz mu wszystko o sobie":
                    you "Dobry wieczór"
                    m "Raczej dobranoc"
                    you "Dobry. {w=0.3} Wieczór. {w=0.3} panie yyy"
                    you "Jak pan się nazywa?"
                    you "w każdym razie nie ważne. Ja byłem pierwszy hihi"
                    you "pewnie już wiesz ale jestem twoim nowym sąsiadem!! (irytująco wesoły ton)"
                    "On robi krok do tyłu i zamyka ci drzwi przed nosem"
                "Ragebait":
                    $ rudeToTomcio = True
                    you "A w sumie nie ważne"
                    "[name] obraca się na pięcie i zaczyna, podskakując, uciekać"
                    m "CZEKAJ"
                    m "boże święty czemu ty uciekasz ode mnie"
                    m "czy ja naprawdę jestem taki groźny"
                    m "Czy to przez to że jestem gruby????"
                    "On wpada w malignę, zaczyna płakać i zamyka drzwi"
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

label firstNightTownWalk:
    




