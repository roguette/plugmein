define rudeToVasili = False
define metVasili = False
define knowsAboutVasiliGrandfatherGhost = False



label l_firstNightLakeVisit:
    play music "forest.mp3" fadein 1.0
    scene bg lakenighta with dissolve
    "Schodzisz w dół, skręcasz parę razy i docierasz na piękną łąkę."
    "Jest naprawdę ogromna, boagta w różnej barwy i rodzaju kwiaty. Ten widok sprawia, że prawie zapominasz o wszystkich przeżyciach tego dnia."
    "Niestety mocniejszy podmuch wiatru wytrąca cię z tego stanu i zostawia cię samego z powracającymi wydarzeniami tego dnia."
    "Jest też nieopodal jakiś dziwny las, ale nie masz zamiaru tam teraz iść."
    "Zszedłeś z drogi, która prowadziła właśnie do tego lasu, i teraz jedynym światłem jest blask Księżyca{w=.3} ― znaczy, z czegokolwiek co świeci na niebie."
    "Twoja droga nad jezioro powinna być w teorii spokojna ― szelest trawy, przez która się przedostajesz powinien być jedynym dźwiękiem."
    "Jednak los miał inne plany."
    scene bg lakenightb with dissolve
    "Na brzegu jeziora widzisz sylwetkę człowieka{w=.6}, yyy... raczej furasa."
    "Ktokolwiek to jest, próbuje łowić ryby i jest {b}strasznie{/b} głośny."
    you "{i}Do jasnej muffinki! Czy serio ktoś tutaj musi być???{/i}"
    you "{i}Chyba nie mam energii na kolejne konwersacje.{/i}"
    you "{i}Może przemknę się bokiem i mnie na zauważy.{/i}{nw}"
    show vasili normal
    m "Kto tam stoi?!"
    m "{b}HALOOO!!!{/b}"
    you "{i}Yyyyy... nikt? Przestań do mnie gadać.{/i}"
    you "Ja! Yyy... to znaczy, jestem tutaj nowy."
    "Podchodzisz bliżej do postaci. Może jest dziwny, ale to nie znaczy, że musisz od razu być wobec niego niemiły."
    "Ale zanim zdążysz cokolwiek powiedzieć, on wyciąga z kieszeni jakieś urządzenie i puszcza ci muzykę w obcym języku."
    "Muzyka jest dziwna{w=.6}, nawet straszna i niepokojąca."
    m "Bratgren było fajnym miastem...{w=.3} Pamiętam jak surowce miasta nie były gromadzone przez tłuste lwy na szczycie ― wszystko należało do ludu..."
    menu:
        "Udawaj, że za nim jest coś strasznego":
            "Po 5 minutach twojego ragebaitu niedźwiedz się nie odwraca."
            "Po tym jak skończył mówić, kazał ci się nie bać duchów przy tym jeziorze, bo są niegroźne."
            you "Jakie duchy???" 
            m "No a co żeś widział tam?"
            you "Yyy...{w=.3} no ducha widziałem." 
            m "To są duchy zmarłych."
            m "Przychodzę tu w nocy bo czasami pojawia się duch mojego dziadka."
            $ knowsAboutVasiliGrandfatherGhost = True
            menu:
                "Jak on miał na imie?":
                    m "Grzegorz Brą z Owy"
    you "Nazywam się [name]."
    $ metVasili = True
    v "Witaj! Mam na imię Vasili. Warzę eliksiry, w wolnym czasię łowię ryby i lubię też śpiewać."
    you "O jak fajnie, pewnie dużo ludzi zna twój głos?"
    v "No nie wiem...{w=.3} śpiewam tylko jak jestem sam...{w=.3} nie mnie to oceniać."
    "Vasili zaczyna opowiadać ci o tym jeziorze, ale ty nie protestujesz, bo i tak miałeś się pytać."
    v "To jest {i}nasze{/i} jezioro, Świtezianka."
    v "Są bardzo fajne legendy o tym jeziorze i w nich chodzi o to, że właściwie są straszne i to, że są legendami."
    v "W jednej z nich założycielka naszego miasta ― a dokładniej jej własne ciało ― miało podobnie chyba zostać tak niby wrzucone do tej zimnej wody, którą widzisz przed sobą."
    v "Dlatego, w sensie tak ogólnie mówiąc, no to nikt tu nie pływa, tak jakby, wiesz, nikt."
    v "Bo to jest trochę tak, że niby można, ale właściwie to nie bardzo, bo wszyscy jakby uznali, że ten pomysł nie należy do najelpszych."
    v "Znaczy, ja nie mówię, że coś się stanie, ale też nie mówię, że się nic nie stanie, dlatego że właśnie, iż jednak, bo tak to, bo i się nie nic tej z nich stanie."
    v "Więc dlatego, tak podsumowując i reasumując, nikt tu nie pływa, i to tak nie bez powodu, tylko tak specjalnie, że jednak nie pływają."
    v "Dlatego że właśnie, iż jednak, bo tak to, bo i się nie nic tej z nich stanie."
    v "Ale jednocześnie trochę jakby może nie do końca, tylko tak bardziej, że no wiesz o co chodzi."

    menu:
        "Pochwal śpiew":
            you "Świetnie śpiewasz, towarzyszu! Słychać, że masz talent."
            you "Można powiedzieć, że dałeś do {i}naszego{/i} pieca."
            you "Jestem pewny, że kiedyś wylądujesz na wielkiej scenie."
            v "Dzięki wielkie. Nie wiesz jak mi to dzień zrobiło!!!"
            $ friendship["Vasili"] += 1
        
        "Krytykuj śpiew":
            you "Tak szczerze to chyba powinieneś jeszcze troszkę poćwiczyć."
            you "Słychać, że amatorsko śpiewasz."
            you "Trochę ćwiczeń i będzie znacznie lepiej."
            you "Studiowałem w teatrze, więc wiem o czym mówię!"
            v "Kim ty jesteś, żeby tak krytykować mój głos?"
            "Zaczynasz pięknie śpiewać."
            you "la la la la la {w=1.5}la"
            v "No cóż... Mówiłem, że nie jestem specjalistą..."
            $ friendship["Vasili"] -= 1
            $ rudeToVasili = True
    
    v "To o czym chciałbyś się dowiedzieć? Wiem tutaj praktycznie wszystko ― spędzam całe dnie na ulicy i jeśli się dobrze przysłucha to można dużo informacji uzyskać."
    v "Ja słucham ludzi cały czas."
    v "Wiedziałeś, że kapitalizm jest zły?{nw}"
    jump l_vasiliFirstNightMagaMenu

define endorsedCommunism = False
define heardVasiliMonologue = False

label l_vasiliFirstNightMagaMenu:
    menu:
        "Zapytaj jaką ma wiedzę na temat ryb":
            $ ryba = random.choice(["l_vasiliFishBrzana", "l_vasiliFishKoza", "l_vasiliFishWstegorz"])
            jump expression ryba

        "Zapytaj o poglądy polityczne" if not heardVasiliMonologue:
            $ heardVasiliMonologue = True
            v "Nie wierzę, że Kurowska jest dobrą prezydentką."
            v "Kurowska to coś gorszego niż zło."
            v "Zaczęła zaciskać kapitalistyczną smycz ― każdy musiał znaleźć pr―{w=.6} pr―{w=.6} pra...cę."
            v "Kurowska jest wydajna i właśnie w tym tkwi prawdziwe niebezpieczeństwo."
            v "Wygłasza przemówienia, pokazuje swój uśmiech à la Morawiecka i macha dzieciom."
            v "Robi to wszystko po to, żeby wierzyli w te jej ckliwe bajeczki."
            v "Ale ja widzę przez tę farsę."
            v "Myślisz, że buduje drogi?"
            v "Nie!!!{nw}"
            v "Ona tylko ci ułatwia dotarcie do pracy, żebyś mógł produkować więcej rzeczy."
            v "Pamiętam, jak próbowała nałożyć podatek na Piotra za to, że nic nie robił."
            v "Nazwała to \"zastojem arkanicznym\"."
            v "Zakazała mu nawet pomagać Wiktorii na farmie."
            v "Bo to nie było \"rolniczo uzasadnione\"."
            v "Nie daj się zwieść latarniom ― oświetlenie miasta to w rzeczywistości sieć inwigilacji."
            v "Latarnie mają oczy{w=1}.{w=1}.{w=1}."
            v "Jakieś dziesięć lat temu nasze wody zostały zakażone."
            v "Ludzie umierali od trucizny w tej wodzie."
            v "Po wypiciu tej cieczy robiłeś się fioletowy i umierałeś."
            v "To były dobre czasy."
            v "Wszyscy robili coś razem i sobie pomagali."
            v "Było cierpienie, ale było ono wspólne."
            v "Kapitalizm nam to odebrał."
            v "Teraz mamy tylko sterylną opresję, a proletariat nic nie może zrobić."
            v "Dlatego kandyduję na prezydenta Bratgren!"
            v "Pod moim przewodnictwem miasto wejdzie w nową erę antykapitalistycznej równowagi."
            v "Zniesiemy własność prywatną."
            v "Praca będzie losowana boską metodą."
            v "Wszystkie banki zostaną zlikwidowane."
            v "Ich budynki przerobimy na centra dystrybucji pyongyang cold noodles."
            v "Pyongyang cold noodles będą podawane lodowato zimne ― żeby proletariat był czujny."
            v "Beton to symbol ucisku."
            v "Każdy dom zostanie zburzony i odbudowany z drewna."
            v "Naprawimy miasto gałązka po gałązce."
            v "Dekadencja burżuazji musi zostać zakończona."
            v "Głosuj na mnie, towarzyszu!!!"

            v "Czy zagłosujesz na mnie?"
            menu:
                "Tak":
                    $ endorsedCommunism = True
                    $ friendship["Vasili"] += 1
                    v "Dziękuję towarzyszu."
                    v "Wiedziałem, że mogę na ciebie liczyć."
                    jump l_vasiliFirstNightMagaMenu
                "Nie, dziękuję":
                    $ friendship["Vasili"] -= 1
                    v "Wiedziałem, że będziesz popierał kapitalizm!"
                    v "W takim razie proszę opuścić teren naszego domu!!!"
                    you "To jak to działa, że mówisz że to nasz dom ale mnie wyganiasz?"
                    v "Idź popieraj kapitalizm gdzieś indziej."
                    hide vasili with dissolve
                    "Odwracasz się i idziesz jak najszybciej od niego bo nie wytrzymasz kolejnego "towarzysza"."
                    jump l_goingHomeTiredAfterVasiliFirstNight

            
        "Zapytaj o życie":
            you "Jestem ciekaw twojej przeszłości. Tyle się nasłuchałem historii tego miejsca, a nic nie wiem o ich ."
            v "Chcesz wiedzieć o moim życiu?"
            v "Ciekawe... No ale nie bedę gatekeepował."
            v "Jak już wiesz ― warzę eliksiry dla siebie i innych ludzi."
            v "Mój dziadek stworzył sklep i robił tam swoje mikstury, więc musiałem przejąć tradycję."
            v "Chociaż po wypadku... ciężko było wrócić do zawodu."
            menu:
                "Dopytaj o wypadek":
                    you "Jeśli mogę zapytać, to co się stało?"
                    if friendship["Vasili"] < 0:
                        v "Wiesz co, wolę nie mówić o moim dziadku..."
                        v "Ten temat jest dość prywatny, i wolę nie opowiadać o takich rzeczach."
                        you "Wszystko w porządku. Rozumiem cię."
                        you "{i}Mówił że nie będzie gatekeepował...{/i}"
                    else:
                        v "Jasne, nie ma problemu. To w skrócie mój dziadek wpadł do kotła z wrzącym eliksirem...{w=1} nie przeżył..."
                        you "O jeju" # jelito core
                        v "Ale było minęło i teraz trzeba żyć dalej."
                "Milcz":
                    you "{i}Jestem trochę ciekawy o jaki wypadek chodzi, ale Vasili wydaję się być wrażliwym człowiekiem.{/i}"
                    if rudeToVasili == False:
                        you "{i}Może lepiej zostawię to w spokoju.{/i}"
                    else:
                        you "{i}Skoro tyle gada to równie dobrze może mi opowiedzieć o swoim dziadku.{/i}"
                        you "W jaki sposób twój dziadek umarł?"
                        v "Kiedy miałem 13 lat wpadł do kotła z eliksirem..."
                        you "Wow, ale heca."
                        v "To nie jest śmieszne!"
                        v "Sam fakt tego, że mój dziadek przestał żyć, to jakby no, wiesz, nie jest ani trochę zabawne, tak w ogóle w sensie ― no ― tak."
                        v "Bo to jest taka niefajna, smutna, tragiczna a nawet nieszczęśliwa sytuacja, że niby można coś powiedzieć, ale właściwie to nie ma z czego się śmiać."
                        v "I że ogólnie to jest bardziej taki moment na bycie poważnym, a nie na jakieś żarty, bo to jednak mówimy właśnie o śmierci mojego dziadka!"

            v "Natomiast jeśli chodzi o moje pasje to kocham łowić ryby i śpiewać w tym samym momencie."
            v "Czy zaspokoiłem twoją ciekawość?"
            you "Tak, dziękuję że się ze mną podzieliłeś swoją historią. "
            you "Trochę późno, chyba na mnie czas. Dobranoc!"
            v "Dobranoc!"
            
            jump l_goingHomeTiredAfterVasiliFirstNight


    


label l_goingHomeTiredAfterVasiliFirstNight:
    "Przez zmęczenie droga do domu trwała wieki, ale nic nie było widać, ponieważ oszczędzają przez wyłączanie latarni."
    "Pomimo braku widoczności przejscie do domu nie sprawiło ci dużo trudu."
    jump h_wakingUpAfterFirstNight


label l_vasiliFishBrzana:
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
    jump l_vasiliAfterFishMonologue


label l_vasiliFishKoza:
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
    jump l_vasiliAfterFishMonologue


label l_vasiliFishWstegorz:
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
    v "Przypominają one koronę, stąd nazwa \"królewski\"."
    v "Przypuszcza się, że płetwy w wodzie mają jaskrawoczerwoną barwę."
    v "Na powietrzu szybko blakną."
    v "Ciało jest jasne i srebrzyście połyskujące..."
    jump l_vasiliAfterFishMonologue


label l_vasiliAfterFishMonologue:
    you "{i}Co ja zrobiłem. Za jakie grzechy...{/i}"
    menu:
        "Spróbuj się wymknąć.":
            "Teraz jest twój time to shine."
            "Czas uciekać."
            "Czujesz się jak jakiś Koreańczyk z północy próbujący uciec do Chin."
            "Podczas gdy Vasili patrzy w drugą stronę i gada o jakichś losowych rybach, zbierasz całą energię w swoje cichobiegi i próbujesz uciec."
            "Problem jest w tym, że za dużo tej energii nie poszło w oczy."
            "Bo nie zauważyłeś puszki z haczykami, walizki z akcesoriami wędkarskimi, jego namiotu i krzesła."
            "Najpierw potykasz się o puszkę, potem lądujesz na walizce, przewracając ją i przy okazji rozwalając mu namiot."
            "To co właśnie się stało było tak głośne, że dało ci dodatkową energię do biegu."
            "I pobiegłeś tak szybko jak tylko mogłeś."
            v "No i gdzie ty się wybierasz?!"
            you "{i}...{/i}"

            menu:
                "Zaprezentuj wymówkę i idź":
                    you "Wiesz co... chyba już muszę iść do domu. Jestem strasznie zmęczony, nie dam rady więcej słuchać."
                    v "Czyli tak jak zawsze... nikt mnie nie lubi."
                    v "Każdy ode mnie ucieka."
                    v "Idź już sobie, nie rań mnie więcej."
                    hide vasili with dissolve
                    you "Nie chciałem...{w=.3} Dobranoc."
                    $ friendship["Vasili"] -= 2
                    you "{i}Przecież nie chciałem, żeby tak wyszło. Nie mam siły (i chęci), by więcej słuchać o tych rybach. Mam dość dzisiejszego dnia!{/i}"
                    "Droga do domu była pełna przemyśleń na temat twojego postępowania w związku z Vasilijem."
                    jump h_wakingUpAfterFirstNight
                "Zaprezentuj wymówkę i zostań.":
                    you "Nie... tylko chciałem się przejść, bo mnie nogi bolą."
                    you "Poza tym noc jest tak piękna, że aż szkoda ją przespać."
                    v "Masz rację, ale wiesz co? Jeszcze nie opowiedziałem ci o mojej ULUBIONEJ rybie...."
                    jump l_vasiliTalksAboutFavoriteFish

        "Wysłuchaj wykładu.":
            you "Znasz może więcej ryb?"
            v "{b}OCZYWIŚCIE{/b}, opowiem ci o mojej {b}ULUBIONEJ{/b} rybie..."
            jump l_vasiliTalksAboutFavoriteFish
    

label l_vasiliTalksAboutFavoriteFish:
    you "{i}W co ja się wkopałem... JA JUŻ NIE CHCE...{/i}"
    scene black with dissolve
    "Przez nadmiar emocji i przedne wykłady na temat ryb ― usnąłeś."
    "Ale on to zauważył."
    v "[name]!"
    v "Czy ty mnie słuchasz?"
    you "Przepraszam. Jest bardzo późno, i chyba powieniem iść spać."
    v "Mi się wydaje, że powienieneś iść spać. Brak snu nie jest zdrowy!"
    v "A wiesz, ja się martwię o twoje zdrowie."
    "Nie wie, że zasnąłeś z nudów, {w=0.6}#delulu"
    you "To w takim razie dobranoc. Kiedyś się jeszcze na pewno spotkamy."
    if friendship["Vasili"] < 0:
        v "Dobranoc."
    else:
        v "Dobranoc, towarzyszu."
    "Droga do domu jest jak przez mgłę. Nie pamiętasz za dużo, ponieważ zostałeś obudzony i jesteś bardzo zaspany."
    "Jednak jakoś doczłapałeś do swojego domu i zasnąłeś w tym momencie, kiedy położyłeś głowę na poduszkę"
    jump h_wakingUpAfterFirstNight


label l_workingAtVasili:
    scene bg lakedaya with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Dzisiejsza droga nad jezioro jest, o dziwo, spokojniejsza od wczorajszej."
    "Pomimo dnia i w okół tętniącego życia, było ciszej niż poprzedniej nocy."
    "W tle było tylko słychać ptaki, brak śpiewów Vasiliego sprawiał, że życie było lepsze."
    scene bg lakedayb with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Kiedy docierasz nad jezioro, nie zastajesz żywej duszy."
    "Jedyne co widzisz to dym unoszący się z chatki, położonej zaraz obok jeziora. Jednak, widzisz unoszącą się zieloną aurę."
    "{i}Ta zielona aura... Chyba tam musi żyć ktoś odklejony od rzeczywistości. Innym razem odwiedzę tę posiadłość.{/i}"
    "Nie znajdując Vasiliego, wracasz się w stronę urzędu miasta. W oddali jednak zauważasz domek, który wydawał się dość przytulny."
    scene bg vasilihouse with dissolve
    play sound "sfx_footsteps_a.mp3"
    you "{i}Wydaję się być bezpiecznie, może tam mieszka Vasili...{/i}"
    "Podchodziwszy bliżej, coraz bardziej było słychać stłumione śpiewy."
    "Kiedy zapukałeś do domu, wyszedł przez drzwi, twój ulubiony ― bo jedyny ― wędkarz."
    show vasili normal with dissolve
    if endorsedCommunism:
        v "Witaj towarzyszu."
        you "Yyy? Cześć..."
        v "Co cię sprowadza w {b}NASZE{/b} skromne progi...{w=.6} HAHAHA bo wiesz...{w=.6} kolektywizacja majątku..."
        you "haha.. rozumiem. Ale nie przyszedłem tutaj na pogaduszki."
        you "Kurowska kazała mi znaleźć pracę, więc stwierdziłem, że zapytam się ciebie, czy nie masz coś dla mnie do roboty."
        v "Ach ten wolny rynek...{w=.3} same z nim problemy..."
        v "W normalnym zakładzie miałbyś pracę od razu, a teraz tak się musisz bawić."
        you "No więc...{w=.3} masz może coś co mógłbym zrobić? Bardzo mi na tym zależy."
        you "Nie mam nawet pieniędzy na jedzenie."
        v "No dobra... chociaż będzie to pierwszy i {b}OSTATNI{/b} raz jak ci dajemy pracę ― nie cierpimy wolnego rynku..."
        v "To tak jak mówiliśmy, musisz skolektywizować akcyzę od drobnomieszczaństwa przesiądującego w naszym gmaszysku." 
        v "My jako szlachcice wymagamy od ciebie pełnego posłuszeństwa i bierności wobec błagań oraz przekupstw od ludzi niższych od nas." 
        v "Innymi słowy musisz zebrać jajka od naszych kur z kurnika za naszym domem." 
        v "Dodatkowo prosimy cię o potępienie poczynań burżuazji, poprzez naznaczenie dobrej ścieżki umysłowej, używając do tego biografii naszego wspaniałego przywódcy oraz ojca naszego narodu ― Ogułki, który powinien rządzić naszym pospólstwem przez kolejne dziesiątki lat." 
        v "Czyli jak zbierzesz jajka, przeczytaj kurom biografię o naszym {b}OJCU{/b}."
        you "..."
        you "{i}Bruh...{w=.6} Co tutaj się dzieje???{w=.6}{/i}"
        you "Troszkę dużo informacji, ale jak tak mówisz, że to wszystko jest nasze..." 
        you "{i}Dobra mam pomysł...{w=.6} Now watch {b}THIS{/b}!!!{/i}"
        you "To mogę się do ciebie wprowadzić?"
        v "Niestety nie." 
        v "Twój rodowód nie pozwala na rozpust wobec twoich aksjomatów." 
        v "Twoje poczynania i zobowiązania są odmienne, dlategoż z tego ambarasu nie jesteśmy w żadnej ewentualności ― w mocy nadanej nam przez naszego pana i ojca Ogułki ― podarować ci schronienie w naszym niewystawnym miejscu bytowania." 
        you "{i}{b}BRO WTF CO TU SIĘ DZIEJE. JA NIE CHCE. CHCE DO DOMU... naszego DOMU???{/b}{/i}"
        you "No dobra... w takim razie ide pozbierać jajka...?"
        v "Zebrać akcyzę."
        v "Tylko pamiętaj o bezwzględności."
        "Oddalając się słyszysz jak Vasili zaczyna śpiewać "Międzynarodówkę"."
        you "{i}JUŻ NIGDY TUTAJ NIE WRACAM...{w=.6} może tylko po pieniądze...{/i}"
        scene bg kurnik with dissolve
        "Jak Vasili mówił, kurnik był zaraz za domem." 
        "Ale... nie powiedział o jednym..."
        you "{i}KURY SĄ CZERWONE?!{w=.6} Nie wytrzymam, za chwile coś mnie powali...{/i}"
        you "{i}DLACZEGO???{/i}"

        you "Jak on mógł to wam zrobić..."
        m "Niestety.... t-"
        you "{b}CO?! KTO TO RZUCIŁ?!! y... POWIEDZIAŁ*{/b}"
        show kura with dissolve
        kura "To ja.{w=.6} Tutaj na dole."
        kura "Tak to ja jestem symbolem wiejskiego ludu gnębionego przez burżuazyjne jaja wielkiego kapitału."
        kura "Lub przedstawicielem klasy niskiej ― bo na wysokich półkach siedzi burżuacja ― towaru wartościowego zwanego drobiem."
        you "Chyba mam schizofrenię.... to wszystko przez tę jego czerwoną aurę."
        kura"Stety nie...{w=.6} my umiemy mówić."
        kura "Vasili nas nauczył, bo stwierdził, że woli wysłuchiwać problemy klasy niskiej, niż się z nimi uporywać..."
        you "Chyba to wytłumaczenie nie pomogło.{w=.6} Nie ważne, muszę zabrać wasze jajka."
        kura "Co musisz zrobić???"
        you "Zebrać jajka....{w=.6} AAAA{w=.3} zebrać akyzę???"
        kura "Dobra, trzeba było tak od razu."
        kura "Niestety nie mamy dużo do oddania, ponieważ Vasili rano pobierał opodatkowanie za przespaną noc..."
        you "Dobra będzie co będzie. Muszę tylko zarobić, by coś zjeść i mnie więcej tutaj {b}NIE{/b} zobaczycie."
        scene bg vasilihouse
        "Wyzbierawszy wysztkie jajka, idziesz do Vasiliego, by mu je oddać. Pukasz do drzwi i znowu otwiera on je."
        show vasili normal with dissolve
        v "I jak?{w=.3} Zbieranie podatku od niższych warstw społecznych zakończyło się sukcesem?"
        you "Tak...{w=.3} Czy mogę dostać swoją zapłatę, ponieważ umieram z głodu."
        v "No dobra... tylko nie wiem czy zdążysz przed zamknięciem piekarni."
        v "Dzisiaj dostawa była i pewnie kolejki po 4 godziny...{w=.6} A nie czekaj{w=.3}, wolny rynek..."
        v "Jak się pospieszysz to zdążysz na jeszcze ciepłe buły Rafała."
        you "Dziękuje! Do widzenia." 
        v "Żegnaj towarzyszu."
        hide vasili with dissolve
    else:
        v "Witaj!"
        you "Cześć..."
        v "Co się sprowadza w moje skromne progi."
        you "Kurowska kazała mi znaleźć pracę, więc stwierdziłem, że zapytam się ciebie czy nie masz coś dla mnie do roboty."
        you "No więc... masz może coś co mógłbym zrobić?"
        you "Bardzo mi na tym zależy. Nie mam nawet pieniędzy na jedzenie."
        v "Jasne... niech tylko pomyślę co...{w=.3} hm...{w=.6} Dobra już wiem ― potrzebuję, żebyś nakarmił moje lisy."
        v "Nie miałem dzisiaj czasu na to, więc pewnie są trochę wściekłe."
        v "Ale wiem, że dasz sobie rady."
        v "Ich wybieg jest zaraz za domem."
        v "(Na twoim miejscu bym się pospieszył, żeby nie zrobiły się zbyt złe.)"
        you "{i}Dobra... nie jest to najcięższa praca, ale mam nadzieję, że te lisy będą dla mnie miłe.{/i}"
        "Vasili daje ci jedzenie dla lisów w pojemniku z IKEI i wychodzisz z domu, żeby nakarmić głodne liski."
        hide vasili with dissolve
        "Idziesz za jego dom i widzisz..."
        "A w sumie to nic nie widzisz, bo nie ma żadnych lisów"
        you "{i}Excusez moi{w=.6} nikogo tu nie ma!{/i}"
        menu:
            "Wydawaj dźwięki lisa":
                    "Nie przychodzi ci do głowy żaden lisi dźwięk."
                    "Lisy nie miauczą, nie szczekają, nie wchodzą w tryb alpha."
                    "A może lisy są po prostu ciche? Te wszystkie myśli przelatują ci przez głowę, podczas gdy stoisz jak idiota z pojemnikiem na jedzenie."
        you "{i}Co ja mam robić???{w=.3} Popłaczę się zaraz...{/i}"
        you "{i}Wiem!!!{/i}"
        you "{i}Zostawię jedzenie za domem to przyjdą same.{/i}"
        you "{i}Pewnie się mnie boją, dlatego ich nie widzę{/i}"
        "Otwierasz pojemnik i zostawiasz go na ziemi, po czym wracasz do Vasiliego."
        show vasili normal with dissolve
        v "Czy zadbałeś o zaspokojenie podstawowych potrzeb żywieniowych moich zwierząt pochodzących spoza lokalnego ekosystemu?"
        you "{i}Hell no!{/i}"
        you "A właśnie!{w=.3} Za twoim domem nic nie ma."
        v "Jak to?"  
        you "{i}Srak to!{/i}"
        you "Tak, po prostu zostawiłem tam to jedzenie co mi dałeś."  
        you "A teraz gdzie pieniądzę."
        you "Ile dostanę za swoją ciężką pracę?"
        v "Jak to nie ma lisów za moim domem?"  
        you "Powiedziałem co powiedziałem, bo tak jest?"  
        v "Ugh, może nie wyszły bo jesteś nowy."
        v "Powinieneś tam zostać, może wtedy przyjdą."  
        hide vasili with dissolve
        "Wracasz za jego dom po raz kolejny i widzisz małego liska jedzącego z wiaderka, które tam zostawiłeś."
        "Jego futro jest bielsze niż zęby w reklamie colgate. Jest bardzo słaby..."
        you "{i}O{w=.3} mój{w=.3} boże!{w=.6} Czemu on jest taki słodki?{/i}"  
        you "{i}Przecież widzę jego żebra wystające przez skórę... Czy to znaczy, że on umiera?{/i}"
        "Wracasz do Vasiliego i pukasz w jego drzwi po raz trzeci."
        show vasili normal with vpunch
        v "Znowu ty!"
        you "Tam za twoim domem jest lisek, który je to jedzenie."
        you "Jest taki chudziutki i malutki."
        you "Co mam robić??"
        v "Muszę go zobaczyć!"
        "Wychodzi z domu, a za nim ciągnie się czerwona aura."
        "Do tej pory miałeś do czynienia tylko z zieloną aurą."
        "Ta jednak nie pachnie jak obornik."
        "Oboje idziecie za dom i obserwujecie białego liska dalej jedzącego swoje jedzonko"
        show vasili normal at leftish with move 
        show lis at rightish with dissolve
        "Jesteście blisko lisa, więc Vasili zaczyna mówić szeptem."
        v "O mój boże, nie widzisz że on jest ranny?"
        "Ty mu też odpowiadasz szeptem."
        you "Skąd wiesz, że jest ranny?"  
        v "Nie widzisz że jego noga jest zgięta 90 stopni na południe?"  
        you "Skąd ty wiesz gdzie jest południe?"  
        lis "Słyszę was!"  
        you "..."
        "Patrzysz się na Vaisiliego z politowaniem."
        you "Wiesz co...{w=.3} Mam tego dość!"  
        you "Daj mi pieniądze i idę."
        v "Czekaj!"  
        "Vasili podnosi liska."
        v "Mam uprawnienia na kręgarza!"
        "Nie widzisz co robi, ale słyszysz ASMR i jest to trochę straszne."
        v "Proszę. Już lepiej."  
        lis "Dzięki!!!"  
        "Lisek robi piruet i odskakuje do lasu."
        hide lis with dissolve
        you "Co{w=1} się właśnie stało..."  
        show vasili normal at center with move 
        v "Ta głupia zawsze sobie coś skręca. Musiałem zostać kręgarzem przez nią."
        you "Okej...{w=.6} nie będę zadawać pytań."
        you "Po prostu mi zapłać i idę."
        v "Dobra. Masz."
        you "Dzięki!"
        v "Na razie, towarzyszu!"
        hide vasili with dissolve
        you "{i}Już nigdy tu nie wrócę!{/i}" 
        you "{i}Nawet jak mam umierać z głodu!{/i}"
    jump t_gotMoney