label firstNightLakeVisit:
    play music "forest.mp3" fadein 1.0
    scene bg lakenighta with dissolve
    "Schodzisz w dół, skręcasz parę razy i docierasz na piękną łąkę"
    "Jest naprawdę ogromna"
    "Jest też jakiś dziwny las, ale nie musisz tam teraz iść"
    "Zszedłeś z drogi i teraz jedyne światło jest z tego ciemnego nieba"
    "Znaczy, z czegokolwiek tam świeci"
    "Twoja droga nad jezioro powinna być, w teorii, spokojna"
    "Szuranie twoich nóg w wysokiej trawie powinno być jedynym dźwiękiem"
    "Jednak los miał inne plany"
    scene bg lakenightb with dissolve
    "Na brzegu jeziora widzisz jakąś sylwetkę"
    "Ktokolwiek to jest, próbuje łowić ryby i jest {b}strasznie{/b} głośny"
    you "{i}do jasnej muffinki{/i}"
    you "{i}Chyba nie mam energii na kolejne konwersacje.{/i}"
    you "{i}Może przemknę się bokiem i mnie na zauważy.{/i}{nw}"
    show vasili normal
    m "Kto tam stoi"
    m "HALOOO"
    you "{i}Yyyyy... nikt? Przestań do mnie gadać.{/i}"
    you "Jestem tutaj nowy"
    "Podchodzisz bliżej do niego. Może on jest dziwny, ale to nie znaczy, że ty będziesz od razu niemiłym do niego"
    you "Nazywam się [name]"
    v "Witaj! Mam na imię Vasili. Warzę eliksiry, w wolnym czasię łowię ryby i lubię też śpiewać"
    you "O jak fajnie, pewnie dużo ludzi cię zna?"
    v "No nie wiem... śpiewam tylko jak jestem sam... Nie mnie to oceniać."

    menu:
        "Pochwal śpiew":
            you "Świetnie śpiewasz! Słychać, że masz talent."
            you "Można powiedzieć, że dałeś do pieca."
            you "Jestem pewny, że kiedyś wylądujesz na wielkiej scenie."
            v "Dzięki wielkie. Nie wiesz jak mi to dzień zrobiło."
            $ friendship["Vasili"] += 1
        
        "Krytykuj śpiew":
            you "Tak szczerze to chyba powinieneś jeszcze troszkę pićwiczyć."
            you "Słychać, że amatorsko śpiewasz."
            you "Trochę ćwiczeń i będzie znacznie lepiej."
            v "Kim ty jesteś, żeby tak krytykować mój głos?"
            "[name] zaczyna pięknie śpiewać"
            you "la la la la la {w=1.5}la"
            v "No cóż... Mówiłem, że nie jestem specjalistą."
            $ friendship["Vasili"] -= 1
    
    v "To o czym chciałbyś się dowiedzieć? Wiem tutaj praktycznie wszystko,"
    v "spędzam całe dnie na ulicy i jeśli się dobrze przypatrzy to można się dużo plotek nasłuchać."
    jump vasiliFirstNightMegaMenu

define experiencedCommies = False
label vasiliFirstNightMegaMenu:
    menu:
        "Zapytaj jaką ma wiedzę na temat ryb":
            $ ryba = random.choice(["vasiliFishBrzana", "vasiliFishKoza", "vasiliFishWstegorz"])
            jump expression ryba

        "Zapytaj o poglądy polityczne":
            $ experiencedCommies = True
            v "Nie wierzę, że Kurowska jest dobrą prezydentką."
            v "Kurowska to coś gorszego niż zło."
            v "Zaczęła zaciskać kapitalistyczną smycz - każdy musiał znaleźć pr*cę."
            v "Kurowska jest wydajna i właśnie w tym tkwi prawdziwe niebezpieczeństwo."
            v "Wygłasza przemówienia, pokazuje swój uśmiech à la Morawiecka i macha dzieciom."
            v "Ma im wierzyć w jej bajeczki."
            v "Ale ja widzę przez tę farsę."
            v "Myślisz, że buduje drogi?"
            v "Nie."
            v "Ona tylko ułatwia ci dotarcie do pracy, żebyś mógł produkować więcej rzeczy."
            v "Pamiętam, jak próbowała nałożyć podatek na Piotra za to, że nic nie robił."
            v "Nazwała to 'zastojem arkanicznym'."
            v "Zakazała mu nawet pomagać Pyndzlowi na farmie."
            v "Bo to nie było 'rolniczo uzasadnione'."
            v "Nie daj się zwieść latarniom - oświetlenie miasta to w rzeczywistości sieć inwigilacji."
            v "Latarnie mają oczy…"
            v "Jakieś dziesięć lat temu nasze wody zostały zakażone."
            v "Ludzie umierali od trucizny w tej wodzie."
            v "Po wypiciu tej cieczy robiłeś się fioletowy i umierałeś."
            v "To były dobre czasy."
            v "Wszyscy robili coś razem i sobie pomagali."
            v "Było cierpienie, ale było wspólne."
            v "Kapitalizm nam to odebrał."
            v "Teraz mamy tylko sterylną opresję, a proletariat nic nie może zrobić."
            v "Dlatego kandyduję na prezydenta Bratgren."
            v "Pod moim przewodnictwem miasto wejdzie w nową erę antykapitalistycznej równowagi."
            v "Zniesiemy własność prywatną."
            v "Praca będzie losowana boską metodą."
            v "Wszystkie banki zostaną zlikwidowane."
            v "Ich budynki przerobimy na centra dystrybucji kimchi."
            v "Kimchi będzie podawane lodowato zimne - żeby proletariat był czujny."
            v "Beton to symbol ucisku."
            v "Każdy dom zostanie zburzony i odbudowany z drewna."
            v "Naprawimy miasto gałązka po gałązce."
            v "Dekadencja burżuazji musi zostać zakończona."
            v "Głosuj na mnie, towarzyszu."

            you "Wiesz co chyba jest już bardzo późno. Lepiej jak pójde teraz do domu."
            you "Kurowska każe mi jutro pracować od rana, więc będzie lepiej jak isę wyśpię."
            v "Tak tak, sen jest najważniejszy, zaraz po zdrowiu psychicznym."
            you "Dobranoc"
            hide vasili with dissolve
            "Odwracasz się i idziesz jaknajszybciej od niego bo nie wytrzymasz kolejnego 'towarzysza'"
            jump goingHomeTiredAfterVasiliFirstNight
        "Zapytaj o życie":
            you "Jestem ciekaw twojej przeszłości. Tyle się nasłuchałem historii tego miejsca, a nic nie wiem o ich mieszkańcach"
            v "Chcesz wiedzieć o moim życiu?"
            v "Ciekawe... No ale nie bedę gatekeepował."
            v "Jak już wiesz, warzę eliksiry dla siebie i innych ludzi."
            v "Mój dziadek stworzył sklep i robił tam swoje eliksiry, więc musiałem przejąć tradycję."
            v "Chociaż po wypadku... ciężko było wrócić do zawodu."
            menu:
                "Dopytaj o wypadek":
                    you "Jeśli mogę zapytać, to co się stało?"
                    v "Jasne, nie ma problemu. To w skrócie mój dziadek wpadł do kotła z wrzącym eliksirem..."
                    v "nie przeżył..."
                    you "O jeju" # jelito core
                    v "Ale było minęło i teraz trzeba żyć dalej."
                "Milcz":
                    you "{i}Jestem trochę ciekawy o jaki wypadek chodzi, ale Vasili wydaję się być wrażliwym człowiekiem.{/i}"
                    you "{i}Może lepiej zostawię to w spokoju.{/i}"
            v "Natomiast jeśli chodzi o moje pasje to kocham łowić ryby i śpiewać w tym samym momencie."
            v "Czy zaspokoiłem twoją ciekawość?"
            you "Tak, dziękuję że się ze mną podzieliłeś swoją historią. "
            you "Trochę późno, chyba na mnie czas. Dobranoc"
            v "Dobranoc (salutuje)"
            
            jump goingHomeTiredAfterVasiliFirstNight


    


label goingHomeTiredAfterVasiliFirstNight:
    "Przez zmęczenie droga do domu trwała wieki, ale nic nie było widać, ponieważ oszczędzają na wyłączaniu latarń."
    "Pomimo braku widoczności przejscie do domu nie sprawiło ci dużo trudu."
    jump wakingUpAfterFirstNight

label vasiliFishBrzana:
    v "Brzana (łac. Barbus barbus) to średniej wielkości, typowa rzeczna ryba z rodziny karpiowatych."
    v "Występuje w dorzeczach Loary, Rodanu, Renu, Dunaju, Łaby, Odry i Wisły."
    v "Można ją też spotkać w Tamizie, Niemnie, Dniestrze i Dnieprze oraz na Półwyspie Iberyjskim."
    v "Została introdukowana we Włoszech i Maroku."
    v "Osiąga przeciętnie około 70 cm długości."
    v "Maksymalnie dorasta do 120 cm i może ważyć do 12 kg."
    v "Brzana ma długie, niskie i walcowate ciało."
    v "Jest ono przystosowane do życia w nurcie rzeki."
    v "Grzbiet ma oliwkowozielony lub ciemnoszary."
    v "Boki są jaśniejsze, a brzuch biały."
    v "Płetwy grzbietowa i ogonowa są szare z ciemniejszym obrzeżeniem."
    v "Pozostałe płetwy mają czerwonawy kolor."
    v "Głównym pokarmem są larwy owadów wodnych, takie jak muchówki, chruściki, widelnice i jętki."
    v "Zjada też kiełże, mięczaki i skąposzczety."
    v "Rzadziej poluje na małe ryby."
    jump vasiliAfterFishMonologue


label vasiliFishKoza:
    v "Koza [[1] to gatunek małej ryby [[2] słodkowodnej z rodziny piskorzowatych [[3]."
    v "Zamieszkuje Europę [[4][[5] z wyjątkiem Irlandii [[6], Szkocji, Norwegii i północnej Szwecji."
    v "Nie występuje też w Finlandii, północnej Rosji oraz południowych[[3.5] półwyspach."
    v "Chodzi o Półwysep Iberyjski[[7][[8], Apeniński[[676767] i Bałkański."
    v "Osiąga przeciętnie ok. 10 cm[[9]."
    v "Maksymalnie dorasta do 13,5 cm długości[[123]."
    v "Ma wydłużone ciało[[10]."
    v "Posiada obronne, ruchome kolce[[11] w okolicy oka[[12][[13]."
    v "Grzbiet jest brązowoszary[[14] i pokryty[[1] ciemnymi plamkami."
    v "Wzdłuż boków biegną dwa[[2], rzadziej jeden[[1], rzędy plam."
    v "Jest ich zwykle 10-20, są duże, okrągłe i ciemne[[15]."
    v "U nasady płetwy ogonowej znajduje się jedna duża ciemna plama[[20]."
    v "Brzuch jest biały lub żółtawy[[6]."
    v "Żywi się bezkręgowcami dennymi..."
    jump vasiliAfterFishMonologue


label vasiliFishWstegorz:
    v "Wstęgor królewski to gatunek dużej, morskiej ryby strojnikokształtnej z rodziny Regalecidae."
    v "Jest zwierzęciem kosmopolitycznym — występuje w wodach Oceanu Indyjskiego, Pacyfiku, Atlantyku."
    v "Można go też spotkać w Morzu Północnym i Morzu Śródziemnym."
    v "Wstęgor osiąga zazwyczaj do 8 metrów długości."
    v "Maksymalna potwierdzona długość wynosi 11 m."
    v "Istnieje jednak doniesienie o osobniku, który miał aż 17 metrów."
    v "Maksymalna potwierdzona masa ciała wynosiła 272 kg."
    v "Ma bardzo wąskie, taśmowate i mocno bocznie spłaszczone ciało."
    v "Wzdłuż niego ciągnie się płetwa grzbietowa, od głowy do ogona."
    v "Służy ona też do napędu."
    v "Płetwa ma ponad 300 promieni, co jest rekordową liczbą."
    v "Pierwszych kilkanaście jest wysokich i zakończonych ozdobnymi zgrubieniami."
    v "Przypominają one koronę, stąd nazwa 'królewski'."
    v "Przypuszcza się, że płetwy w wodzie mają jaskrawoczerwoną barwę."
    v "Na powietrzu szybko blakną."
    v "Ciało jest jasne i srebrzyście połyskujące..."
    jump vasiliAfterFishMonologue

label vasiliAfterFishMonologue:
    you "{i}... :( co ja zrobiłem. Za jakie grzechy...{/i}"
    menu:
        "Spróbuj się wymknąć.":
            "Teraz jest twój time to shine"
            "Czas uciekać"
            "Czujesz się jak jakiś Koreańczyk z północy próbujący uciec do Chin"
            "Podczas gdy Vasili patrzy w drugą stronę i gada o jakichś losowych rybach, zbierasz całą energię w swoje cichobiegi i próbujesz uciec"
            "Problem jest w tym, że za dużo tej energii poszło nie w oczy"
            "Bo nie zauważyłeś puszki z haczykami, walizki z akcesoriami wędkarskimi, jego namiotu i krzesła"
            "Najpierw potykasz się o puszkę, potem lądujesz na walizce, przewracając ją i przy okazji rozwalając mu namiot"
            "To co właśnie się stało było tak głośne, że dało ci dodatkową energię do biegu"
            "I pobiegłeś tak szybko jak tylko mogłeś"
            v "no i gdzie ty się wybierasz"
            you "{i}...{/i}"

            menu:
                "Zaprezentuj wymówkę i idź":
                    you "Wiesz co... chyba już muszę iść do domu. Jestem strasznie zmęczony, nie dam rady więcej słuchać."
                    v "Czyli tak jak zawsze... nikt mnie nie lubi."
                    v "Każdy ode mnie ucieka."
                    v "Idź już sobie, nie rań mnie więcej."
                    hide vasili with dissolve
                    you "Nie chciałem... dobranoc."
                    $ friendship["Vasili"] -= 2
                    you "{i}Przecież nie chciałem żeby tak wyszło. Nie mam siły (i chęci), by więcej słuchać o tych rybach. Mam dość dzisiejszego dnia!{/i}"
                    "Droga do domu była pełna przemyśleń na temat twojego postępowania w związku z Vasilijem. "
                    jump wakingUpAfterFirstNight
                "Zaprezentuj wymówkę i zostań.":
                    you "Nie... tylko chciałem się przejść, bo mnie nogi bolą."
                    you "Poza tym noc jest tak piękna, że aż szkoda przespać tę noc."
                    v "Masz rację, ale wiesz co? Jeszcze nie opowiedziałem ci o mojej ULUBIONEJ rybie...."
                    jump vasiliTalksAboutFavoriteFish

        "Wysłuchaj wykładu.":
            you "Znasz może więcej ryb?"
            v "OCZYWIŚCIE, opowiem ci o mojej ULUBIONEJ rybie..."
            jump vasiliTalksAboutFavoriteFish
    

label vasiliTalksAboutFavoriteFish:
    you "{i}W co ja się wkopałem... JA JUŻ NIE CHCE...{/i}"
    scene black with dissolve
    "Przez nadmiar emocji (i najwyraźniej yappowanie Vasilia) usnąłeś"
    "Ale on to zauważył"
    "Vasili budzi cię i każe ci iść spać, ponieważ martwi się o twoje zdrowie"
    "(Nie wie, że zasnąłeś z nudów, {w=0.6}#delulu)"
    "Droga do domu jest jak przez mgłę. Nie pamiętasz za dużo, ponieważ zostałeś obudzony i jesteś bardzo zaspany."
    "Jednak jakoś doczłapałeś do swojego domu i zasnąłeś w sekundzie, kiedy położyłeś głowę na poduszkę"
    jump wakingUpAfterFirstNight