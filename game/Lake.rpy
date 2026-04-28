define rudeToVasili = False
define metVasili = False
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
    "wyciąga z kieszeni jakieś urządzenie i puszcza ci muzykę w obcym języku."
    "muzyka jest dziwna, nawet niepokojąca."
    m "bratgren było fajnym miastem. Pamiętam jak surowce miasta nie były gromadzone przez tłuste lwy na szczycie. Wszystko należało do ludu"
    menu:
        "Udawaj, że za nim jest coś strasznego":
            "Po 5 minutach twojego ragebaitu Vasili się nie odwraca"
            "po tym jak skończy mówić, każe ci się nie bać duchów przy tym jeziorze bo nic ci nie zrobią."
            you "Jakie duchy?" 
            m "no a co żeś widział tam"
            you 'a no ducha widziałem' 
            m "To są duchy zmarłych."
            m "Przychodzę tu w nocy bo czasami pojawia się duch mojego dziadka."
            menu:
                "Jak on miał na imie?":
                    m "Grzegorz Brą z Owy"
    you "Nazywam się [name]"
    $ metVasili = True
    v "Witaj! Mam na imię Vasili. Warzę eliksiry, w wolnym czasię łowię ryby i lubię też śpiewać"
    you "O jak fajnie, pewnie dużo ludzi cię zna?"
    v "No nie wiem... śpiewam tylko jak jestem sam... Nie mnie to oceniać."
    "Vasili zaczyna opowiadać ci o tym jeziorze, ale ty nie protestujesz, bo i tak miałeś się pytać"
    v "To jest {i}nasze{/i} jezioro, Świtezianka."
    v "Są bardzo fajne legendy o tym jeziorze, i w nich chodzi o to, że właściwie są straszne, i że w ogóle to są legendy"
    v "W jednej z nich, założycielka naszego miasta, a dokładniej jej własne ciało, miało podobnie chyba zostać tak niby wrzucone do tej zimnej wody, którą widzisz przed sobą"
    v "I możesz zobaczyć teraz."
    v "Dlatego, w sensie tak ogólnie mówiąc, no to nikt tu nie pływa, tak jakby, wiesz, nikt"
    v "Bo to jest trochę tak, że niby można, ale właściwie to nie bardzo, bo wszyscy jakby uznali, że ten pomysł nie jest z najelpszych"
    v "Znaczy, ja nie mówię, że coś się stanie, ale też nie mówię, że się nie stanie, dlatego że właśnie iż jednak bo tak to bo i się nie nic tej z nich."
    v "Więc dlatego, tak podsumowując i reasumując, nikt tu nie pływa, i to tak nie bez powodu, tylko tak specjalnie, że jednak nie"
    v "dlatego że właśnie iż jednak bo tak to bo i się nie nic tej z nich"
    v "ale jednocześnie trochę jakby może nie do końca, tylko tak bardziej że no wiesz o co chodzi"

    menu:
        "Pochwal śpiew":
            you "Świetnie śpiewasz, towarzyszu! Słychać, że masz talent."
            you "Można powiedzieć, że dałeś do {i}naszego{/i} pieca."
            you "Jestem pewny, że kiedyś wylądujesz na wielkiej scenie."
            v "Dzięki wielkie. Nie wiesz jak mi to dzień zrobiło."
            $ friendship["Vasili"] += 1
        
        "Krytykuj śpiew":
            you "Tak szczerze to chyba powinieneś jeszcze troszkę poćwiczyć."
            you "Słychać, że amatorsko śpiewasz."
            you "Trochę ćwiczeń i będzie znacznie lepiej."
            you "Studiowałem w teatrze, więc wiem o czym mówię"
            v "Kim ty jesteś, żeby tak krytykować mój głos?"
            "[name] zaczyna pięknie śpiewać"
            you "la la la la la {w=1.5}la"
            v "No cóż... Mówiłem, że nie jestem specjalistą."
            $ friendship["Vasili"] -= 1
            $ rudeToVasili = True
    
    v "To o czym chciałbyś się dowiedzieć? Wiem tutaj praktycznie wszystko,"
    v "spędzam całe dnie na ulicy i jeśli się dobrze przypatrzy to można się dużo plotek nasłuchać."
    v "Ja słucham ludzi cały czas."
    v "Wiedziałeś, że kapitalizm jest zły?{nw}"
    jump vasiliFirstNightMegaMenu

define endorsedCommunism = False
define heardVasiliMonologue = False
label vasiliFirstNightMegaMenu:
    menu:
        "Zapytaj jaką ma wiedzę na temat ryb":
            $ ryba = random.choice(["vasiliFishBrzana", "vasiliFishKoza", "vasiliFishWstegorz"])
            jump expression ryba

        "Zapytaj o poglądy polityczne" if not heardVasiliMonologue:
            $ heardVasiliMonologue = True
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
            v "Zakazała mu nawet pomagać Wiktorii na farmie."
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

            v "Czy zagłosujesz na mnie?"
            menu:
                "Tak":
                    $ endorsedCommunism = True
                    $ friendship["Vasili"] += 1
                    v "Dziękuję towarzyszu."
                    v "Wiedziałem, że mogę na ciebie liczyć."
                    jump vasiliFirstNightMegaMenu
                "Nie dziękuję":
                    $ friendship["Vasili"] -= 1
                    v "wiedziałem, że będziesz popierał kapitalizm"
                    v "W takim razie proszę opuścić teren naszego domu"
                    you "To jak to działa, że mówisz że to nasz dom ale mnie wyganiasz"
                    v "Idź popieraj kapitalizm gdzieś indziej."
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
                    if friendship["Vasili"] < 0:
                        v "Wiesz co, wolę nie mówić o moim dziadku"
                        v "Ten temat jest dość prywatny, i wolę nie opowiadać o takich rzeczach"
                        you "Wszystko w porządku. Rozumiem cię."
                    else:
                        v "Jasne, nie ma problemu. To w skrócie mój dziadek wpadł do kotła z wrzącym eliksirem..."
                        v "nie przeżył..."
                        you "O jeju" # jelito core
                        v "Ale było minęło i teraz trzeba żyć dalej."
                "Milcz":
                    you "{i}Jestem trochę ciekawy o jaki wypadek chodzi, ale Vasili wydaję się być wrażliwym człowiekiem.{/i}"
                    if rudeToVasili == False:
                        you "{i}Może lepiej zostawię to w spokoju.{/i}"
                    else:
                        you "{i}Skoro tyle gada to równie dobrze może opowiedzieć o swoim dziadku.{/i}"
                        you "Na co umarł twój dziadek"
                        v "Kiedy miałem 13 lat wpadł do kotła z eliksirem"
                        you "wow ale heca"
                        v "To nie jest śmieszne."
                        v "Sam fakt tego, że mój dziadek przestał żyć, to jakby no, wiesz, nie jest ani trochę zabawne, tak w ogóle w sensie no tak"
                        v "Bo to jest taka niefajna, smutna, tragiczna a nawet nieszczęśliwa sytuacja, że niby można coś powiedzieć, ale właściwie to nie ma z czego się śmiać."
                        v "I że ogólnie to jest bardziej taki moment na bycie poważnym, a nie na jakieś żarty, bo to jednak mówimy właśnie o śmierci mojego dziadka"

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
    v "Chodzi o Półwysep Iberyjski[[7][[8], Apeniński[[67] i Bałkański."
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
    v "[name]!"
    v "Czy ty mnie słuchasz?"
    you "Przepraszam. Jest bardzo późno, i chyba powieniem iść spać"
    v "Mi się wydaje, że powienieneś iść spać. Brak snu nie jest zdrowy"
    v "A wiesz, ja się martwię o twoje zdrowie."
    "(Nie wie, że zasnąłeś z nudów, {w=0.6}#delulu)"
    you "To w takim razie dobranoc. Kiedyś się jeszcze na pewno spotkamy."
    if friendship["Vasili"] < 0:
        v "Dobranoc."
    else:
        v "Dobranoc, towarzyszu."
    "Droga do domu jest jak przez mgłę. Nie pamiętasz za dużo, ponieważ zostałeś obudzony i jesteś bardzo zaspany."
    "Jednak jakoś doczłapałeś do swojego domu i zasnąłeś w sekundzie, kiedy położyłeś głowę na poduszkę"
    jump wakingUpAfterFirstNight

label workingAtVasili:
    "Dzisiejsza droga nad jezioro jest, o dziwo, spokojniejsza od wczorajszej."
    "Pomimo dnia i w okół tętniącego życia, było ciszej niż poprzedniej nocy."
    "W tle było tylko słychać ptaki, brak fal i śpiewów Piwowarskiego sprawiały, że życie było lepsze."
    "Kiedy docierasz nad jezioro, nie zastajesz żywej duszy."
    "Jedyne co widzisz to dym unoszący się z chatki, położonej zaraz obok jeziora. Jednak, widzisz unowszącą się zieloną aurę."
    "{i}Ta zielona aura... Chyba tam musi żyć ktoś odklejony od rzeczywistości. Innym razem odwiedzę tę posiadłość.{/i}"
    "Nie znajdując Piwowarskiego, wracasz się w stronę Urzędu miasta. W oddali jednak zauważasz domek, który wydawał się dość przytulny."
    "Wydaję się być bezpiecznie, może tam mieszka Piwowarski..."
    "Podchodziwszy bliżej, coraz bardziej było słychać stłumione śpiewy."
    "Kiedy zapukałeś do domu, wyszedł przez drzwi, twój ulubiony, bo jedyny, wędkarz."
    if endorsedCommunism:
        v "Witaj towarzyszu."
        you "Yyy? Cześć..."
        v "Co cię sprowadza w NASZE skromne progi... HAHAHA bo wiesz... kolektywizacja majątku..."
        you "haha(??).. rozumiem. Ale nie przyszedłem tutaj na pogaduszki."
        you "Kurowska kazała mi znaleźć pracę, więc stwierdziłem, że zapytam się ciebie czy nie masz coś dla mnie do roboty."
        v "Ach ten wolny rynek... same z nim problemy."
        v "W normalnym zakładzie miałbyś pracę od razu, a teraz tak się musisz bawić."
        you "No więc... masz może coś co mógłbym zrobić? Bardzo mi na tym zależy."
        you "Nie mam nawet pieniędzy na jedzenie."
        v "No dobra... chociaż będzie to pierwszy i OSTATNI raz jak ci dajemy pracę, nie cierpimy wolnego rynku..."
        v "To tak jak mówiliśmy, musisz skolektywizować akcyzę od drobnomieszczaństwa przesiądującego w naszym gmaszysku." 
        v "My jako szlachcice wymagamy od ciebie pełnego posłuszeństwa i bierności wobec błagań oraz przekupstw od ludzi niższych od nas." 
        v "Innymi słowy musisz zebrać jajka od naszych kur z kurnika za naszym domem." 
        v "Dodatkowo prosimy cię o potępienie poczynań burżuazji, poprzez naznaczenie dobrej ścieżki umysłowej, używając do tego biografii naszego wspaniałego przywódcy oraz ojca naszego narodu Ogułki," 
        v " który powinien rządzić naszym pospólstwem przez kolejne dziesiątki lat." 
        v "Czyli jak zbierzesz jajka, przeczytaj kurom biografię o naszym OJCU."
        you "...."
        you "Troszkę dużo informacji, ale jak tak mówisz, że to wszystko jest nasze..." 
        you "to mogę się do ciebie wprowadzić?"
        v "Niestety nie." 
        v "Twój rodowód nie pozwala na rozpust wobec twoich aksjomatów." 
        v "Twoje poczynania i zobowiązania są odmienne, dlategoż z tego ambarasu nie jesteśmy w żadnej ewentualności," 
        v "w mocy nadanej nam przez naszego pana i ojca Ogułki, podarować ci schronienie" 
        v "w naszym niewystawnym miejscu bytowania."
        you "{i}BRO WTF CO TU SIĘ DZIEJE. JA NIE CHCE. CHCE DO DOMU... naszego DOMU....{/i}"
        you  "No dobra... w takim razie ide pozbierać jajka...?"
        v "Zebrać akcyzę."
        v "Tylko pamiętaj o bezwzględności."
        "Oddalając się słyszysz jak Piwowarski zaczyna śpiewać 'Międzynarodówkę'."
        you "{i}JUŻ NIGDY TUTAJ NIE WRACAM... może tylko po pieniądze...{/i}"
        "Jak Vasili mówił kurnik był zaraz za domem." 
        "Ale... nie powiedział o jednym..."
        you "{i}KURY SĄ CZERWONE?! Nie wytrzymam, za chwile coś mnie powali....{/i}"
        you "{i}DLACZEGO???{/i}"

        you "Jak on mógł to wam zrobić..."
        m "Niestety.... t-"
        you "CO?! KTO TO RZUCIŁ?!! y... POWIEDZIAŁ*"
        kura "To ja. Tutaj na dole."
        kura "Tak to ja jestem symbolem wiejskiego ludu gnębionego przez burżuazyjne jaja wielkiego kapitału"
        kura "lub przedstawiciel klasy niskiej"
        kura "(bo na wysokich półkach siedzi burżuacja)"
        kura "towaru wartościowego zwanego drobiem."
        you "Chyba mam schizofrenię.... przez tę jego czerwoną aurę."
        kura"Niestety nie... my umiemy mówić."
        kura "Vasili nas nauczył, bo stwierdził, że woli wysłuchiwać problemy klasy niskiej, niż się z nimi uporywać..."
        you "Chyba to wytłumaczenie nie pomogło. Nie ważne, muszę zabrać wasze jajka."
        kura "Co musisz zrobić???"
        you "Zebrać jajka.... AAAA zebrać akyzę???"
        kura "Dobra, trzeba było tak od razu."
        kura "Niestety nie mamy dużo do oddania, ponieważ Vasili rano pobierał opodatkowanie za przespaną noc..."
        you "Dobra będzie co będzie. Muszę tylko zarobić, by coś zjeść i mnie więcej tutaj NIE zobaczycie."
        "Wyzbierawszy wysztkie jajka, idziesz do Vasiliego, by mu je oddać. Pukasz do drzwi i znowu otwiera je Vasili."
        v "I jak zbieranie podatku od niższych warstw społecznych zakończyło się sukcesem?"
        you "Tak. Czy mogę dostać swoją zapłatę, ponieważ umieram z głodu."
        v "No dobra... tylko nie wiem czy zdążysz przed zamknięciem piekarni."
        v "Dzisiaj dostawa była i pewnie kolejki po 4 godziny... A nie czekaj, wolny rynek..."
        v "Jak się pospieszysz to zdążysz na jeszcze ciepłe buły Rafała."
        you "Dziękuje! Do widzenia." 
        v "Żegnaj towarzyszu."
    else:
        v "Witaj!"
        you "Cześć..."
        v "Co się sprowadza w moje skromne progi."
        you "Kurowska kazała mi znaleźć pracę, więc stwierdziłem, że zapytam się ciebie czy nie masz coś dla mnie do roboty."
        you "No więc... masz może coś co mógłbym zrobić?"
        you "Bardzo mi na tym zależy. Nie mam nawet pieniędzy na jedzenie."
        v "Jasne... niech tylko pomyślę co... hm... Dobra już wiem potrzebuję,"
        v "żebyś nakarmił moje lisy."
        v "Nie miałem dzisiaj czasu na to, więc pewnie są trochę wściekłe."
        v "Ale wiem, że dasz sobie rady."
        v "Ich wybieg jest zaraz za domem."
        v "(Na twoim miejscu bym się pospieszył, żeby nie zrobiły się zbyt złe)."
        you "{i}Dobra... nie jest to najcięższa praca, ale mam nadzieję, że te lisy będą dla mnie miłe.{/i}"
        "Vasili daje ci żarcie dla lisów w pojemniku z IKEI i wychodzisz z domu, żeby nakarmić głodne liski."
        "Idziesz za jego dom i widzisz..."
        "A w sumie to nic nie widzisz, bo nie ma żadnych lisów"
        you "{i}excusez moi nikogo tu nie ma{/i}"
        menu:
            "Wydawaj dźwięki lisa":
                    "Nie przychodzi ci do głowy żaden lisowy dźwięk."
                    "Lisy nie miauczą, nie szczekają, nie wchodzą w tryb alpha."
                    "A może lisy są po prostu ciche? Te wszystkie myśli przelatują ci przez głowę,"
                    "podczas gdy stoisz jak idiota z pojemnikiem na jedzenie"
        you "{i}Co ja mam robić popłaczę się zaraz{/i}"
        you "{i}Wiem.{/i}"
        you "{i}Zostawię jedzenie za domem to przyjdzie sam{/i}"
        you "{i}Pewnie mnie się boi, dlatego go nie widzę{/i}"
        "Otwierasz pojemnik i zostawiasz go na ziemi, po czym wracasz do Vasiliego"
        v "Czy zadbałeś o zaspokojenie podstawowych potrzeb żywieniowych moich zwierząt pochodzących spoza lokalnego ekosystemu?"
        you "{i}Hell no{/i}"
        you "A właśnie"  
        you "Za twoim domem nic nie ma"  
        v "Jak to"  
        you "{i}srak to{/i}"
        you "Tak, po prostu zostawiłem tam to jedzenie co mi dałeś"  
        you "A teraz gdzie hajs"
        you "Ile dostanę za swoją ciężką pracę?"
        v "Jak to nie ma lisów za moim domem"  
        you "Powiedziałem co powiedziałem"  
        v "Ugh, może nie wyszły bo jesteś nowy"  
        v "Powinieneś tam zostać, może wtedy przyjdą"  
        "Wracasz za jego dom po raz kolejny i widzisz małego liska jedzącego jedzenie, które tam zostawiłeś."
        "Jego futro jest bielsze niż zęby w reklamie colgate. Jest bardzo słaby"
        you "{i}O mój boże czemu on jest taki słodki{/i}"  
        you "{i}Czy to znaczy że on umiera...{/i}"  
        "Wracasz do Vasiliego i pukasz w jego drzwi po raz trzeci"
        v 'Znowu ty'  
        you 'Tam za twoim domem jest lisek który je to jedzenie'  
        you 'Jest taki chudziutki i malutki'  
        you 'Co mam robić??'  
        v 'muszę go zobaczyć omg'  
        "Wychodzi z domu, a za nim ciągnie się czerwona aura."
        "Do tej pory miałeś do czynienia tylko z zieloną aurą."
        "Ta jednak nie pachnie jak obornik."
        "Oboje idziecie za dom i obserwujecie białego liska dalej jedzącego swoje jedzonko"
        v '(szeptem)O mój boże, nie widzisz że on jest ranny?'  
        you '(też szeptem)Skąd wiesz że jest ranny?'  
        v 'Nie widzisz że jego noga jest zgięta 90 stopni na południe?'  
        you 'Skąd ty wiesz gdzie jest południe'  
        lis 'Słyszę was'  
        you '...'
        "patrzysz się z politowaniem"
        you 'Wiesz co'  
        you 'Mam tego dość'  
        you 'Daj mi pieniądze i idę'  
        v 'Czekaj'  
        "Piwowarski podnosi liska i mówi, że jest kręgarzem."
        "Nie widzisz co robi, ale słyszysz ASMR i jest to trochę straszne"
        v 'Proszę. Już lepiej'  
        lis 'Dzięki!!!'  
        "Lisek robi piruet i odskakuje do lasu"
        you 'co się właśnie stało'  
        v 'Ta głupia zawsze sobie coś skręca. Musiałem zostać kręgarzem przez nią'  
        you 'Okej... nie będę zadawać pytań'  
        you 'Po prostu mi zapłać i idę'  
        v 'Dobra. Masz'  
        you 'Dzięki'  
        v 'Na razie, towarzyszu'
        you "{i}już nigdy tu nie wrócę{/i}" 
        you "{i}nawet jak mam umierać z głodu{/i}"
    jump gotMoney