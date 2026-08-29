define playerRobbed = False
define workedAtVasili = False
define workedAtFilip = False
define robberyStopped = False
define metPetitty = False

label ch02_watch_your_mouth:

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
    scene bg citysquareday with dissolve
    play music "town_day.mp3"
    play sound "sfx_footsteps_b.mp3"
    "Idąc do Kurowskiej, podziwiasz budynki i przyrodę, ponieważ dzień wcześniej nie dało się tego zrobić."
    "Droga do urzędu miasta była bardzo przyjemna, jednak najgorszą częścią było zignorowanie zapachów wydobywających się z piekarni."  
    "Brzuch ci burczy, niestety nie masz żadnych pieniędzy by zapłacić za potencjalny posiłek."
    you "{i}NIE WYTRZYMAM... taki jestem głodny. Trzeba było wczoraj pożyczyć od kogoś pieniądze. No cóż, muszę jeszcze wytrzymać do końca dnia, aż otrzymam moją dzisiejszą wypłatę.{/i}"
    "{i}Albo może zapiszą mi ten bułę na kreskę, a ja zapłacę za nią później... Chociaż ta praktyka zniknęła ż PRL-em... Dobra dam radę!!! Kto jak nie ja?{/i}"
    "Ulice teraz tętnią życiem, każdy spieszy się do pracy, w niektórych momentach nawet ciężko przecisnąć się przez tłumy."
    "Jednak nikt nie odważy się zbliżyć do fontanny."
    "Patrzysz w górę i dziwisz się, że dalej nie widać słońca."
    "Ludzie są prawdopodobnie przyzwyczajeni do niekończących się chmur stratus, pokrywających niebo."
    "Gdy podchodzisz do urzędu, on znowu robi na tobie wrażenie, nie tak wielkie jak wczoraj, ale dalej jest bardzo inponujący."
    "Nie ma czasu do stracenia i wchodzisz do budynku, szukając Filipa."
    jump ch02_goingToKur

label ch02_goingToKur:
    play sound "sfx_footsteps_a.mp3"
    scene bg cityhallinside with dissolve
    "Wchodząc do środka czujesz zapach świeżo zaparzonej kawy i bułek. Ten zapach prowadzi cię do szału."
    scene bg secretary with dissolve
    play sound "sfx_door_open.mp3"
    "Kiedy Filip wychodzi od Kurowskiej z pustą tacą. Podchodzisz do niego."
    show filip normal with dissolve
    you 'Hej...'
    f "Hejka."
    show filip shocked with vpunch
    f "Boże wyglądasz okropnie co jest?"
    you "Od kiedy pojawiłem się w tym mieście nic nie jadłem. Masz tu jakieś jedzenie?"
    show filip normal
    f "Tak. Codziennie przynoszę Kurowskiej ciepłe buły Rafała z kawą."
    you "Czy mógłbyś mi dać jedną? Nie mam żadnych pięniędzy, więc nie mogę kupić jedzenia"
    you "Dosłownie zaraz umrę jeśli nic nie zjem!!!"
    f "Jasne."
    show filip normal at offscreenright with move
    "Filip odkłada talerz przy zlewie a potem znika w pomieszczeniu gospodarczym."
    "Słyszysz jak musi coś odsuwać, żeby dostać się do tej bułki, którą tak pragniesz."
    show filip normal at center with move
    "Wraca i daje ci bułę Rafała. Jest twarda ale nie masz wyboru."
    "Bierzesz bułę Rafała i pochłaniasz ją. Mimo że jest przeterminowana ― jak Tuleja ― wciąż smakuje jak z najwyższej półki."
    you "O mój boże z czego ta bułka jest zrobiona? Jest czerstwa ale jest tak dobra, że...{w} brakuje mi słow."
    f "Smakują ci dlatego, że jesteś głodny."
    f "Ale ogólnie to są rzeczywiście smaczne. Polecam pójść do tej piekarni kiedy są świeże."
    f "Wtedy są jeszcze lepsze."
    f "Wszyscy w tym mieście kochają buły Rafała."
    you "Gdzie je kupiłeś?? Też chcę, jak będę miał pieniądze."
    f "No w BBB na rynku."
    you "What do you mean BBB???"
    f "Nie rozumiesz? {i}{u}Big Buły Bakery{/u}{/i}..."
    you "Ma sens."
    f "Ale wracając, to jest tu. Ta piekarnia jest dość duża, więc na pewno ją zauważysz."
    "Filip pokazuje ci palcem na mapie gdzie jest ta piekarnia."
    "Szybko się orientujesz, gdzie to jest na rynku."
    f "A co do pieniędzy..."
    f "Powinieneś zapytać Kurowską o pracę, a ona ci pomoże."
    you "Thank you! Thank you! Thank you!"
    you "Ratujesz mi życie w tym momencie!"
    play sound "door_knock.mp3"
    "Grzecznie pukasz do drzwi Kurowskiej, próbując przy tym robić to identycznie jak Filip wczoraj."
    with vpunch
    k "KTO TAK PUKA NA BELZEBUBA???"
    you "To ja."
    k "A 'ja' to kto?"
    you "[name]"
    k "Wejdź!"
    scene bg office with dissolve
    play sound "sfx_door_open.mp3"
    "Wchodisz do jej biura i widzisz, że jest znowu jest zajęta jakimiś dokumentami."
    you "{i}Czy ona będzie na mnie zła za to, że ja tak sobie wszedłem?{/i}"
    you "{i}Oby nie.{/i}"
    you "{i}Ale przecież sama mi kazała wczoraj się zgłosić... No to dzień dobry.{/i}"
    show kurowska normal with dissolve
    you "Dzień dobry. Wczoraj mi Pani powiedziała żebym ja się zgłosił do tej pracy.. chyba.."
    k "Tak, pamiętam."
    if rudeToKurowska == True:
        jump ch02_goingToKurRude
    else:
        jump ch02_goingToKurNotRude

label ch02_goingToKurRude:
    k "Sam sobie znajdź pracę."
    you "Ale..."
    k "'ale ale ale' ale cyganisz!"
    k "Wynoś się i idź do pracy!"
    "Wściekła kurowska wyrzuca cię ze swojego biura."
    show bg secretary with vpunch
    play sound "sfx_door_slam.mp3"
    you "{i}Następnym razem powinienem ją przeprośić za to, co jej powiedziałem...{/i}"
    jump ch02_goingToFindAJob

label ch02_goingToKurNotRude:
    $ randomCorrectChoiceIndex = random.randint(1, 3)
    k "Musisz sam znaleźć pracę. Po prostu zapytaj znajomych na pewno ci pomogą."
    "Kurowska znowu zaczęła szukać czegoś na swoim biurku."
    "..."
    "Tym razem znalazła to co chciała."
    k "Proszę. To powinno wystarczyć żebyś przeżył zanim coś znajdziesz."
    "Kurowska dała ci sakiewkę pełną monet."
    "Jest cholernie ciężka..."
    k "Trzymaj."
    you "Co to jest?"
    you "Czemu te monety są takie ciężkie?"
    k "Zwykle nie używamy tych monet."
    k "Trzymałam je w biurze i chciałam się ich pozbyć więc to jest win-win situation."
    k "A teraz idź znajdź pracę i zrób żebym była dumna!"
    you "Dziękuję bardzo, na pewno to zrobię."
    scene bg secretary with dissolve
    play sound "sfx_door_open.mp3"
    "Opuszczasz jej biuro i żegnasz się z Filipem. Teraz masz trochę pieniędzy i możesz w końcu coś robić{w=0.5}, nie umierając z głodu"
    scene bg citysquareday with dissolve
    play sound "sfx_footsteps_b.mp3"
    "Ulice po rush hour są teraz praktycznie puste, poza kilkoma bezdomnymi i lekko groźnymi osobami."
    you "{i}Chyba aż tak długo nie spędziłem czasu u Kurowskiej, skoro nie ma praktycznie żywej duszy na ulicy. Pewnie wszyscy siedzą w pracy.{/i}"
    you "{i}A teraz pora na kupienie sobie POŻYWNEGO śniadania.{/i}"
    "DRUGIEGO śniadania!"
    you "{i}Z tej racji pójdę sobie do BBB{/i}"
    "Przechodząc obok fontanny atakuje cię meżczyzna, chociaż jest niski, to wygląda na groźnego."
    play music "outfoxingthefox.mp3"
    show kamil normal with vpunch
    m "Oddaj wszystkie pieniądze jakie masz!!!"
    $ playerRobbed = True
    you "CO! Nie proszę, nie rób mi krzywdy, ale nie mogę dać ci tych pieniędzy."
    you "Nie jadłem nic od wczoraj, te pieniądze dostałem w prezencie. Muszę je wykorzystać na jedzenie i ubranie, bom głodny i goły."
    m "No dobra, mam serce, dlatego pozwolę ci zawalczyć o to czy będziesz musiał mi oddać twoje pieniądze."
    you "PRZECIEŻ TO NIESPRAWIEDLIWE!"
    m "Życie jest niesprawiedliwe."
    m "Teraz odpowiedz na moje pytanie, które brzmi: 'Jaki jest mój ulubiony włoski brainrot?'"
    "Życie przelatuje ci przed oczami, gdy zadaje to pytanie." 
    "Nie wiesz, co to jest brainrot, ale odpowiedzi same ci się pojawiają w głowie, jakbyś był sleeper agentem."
    "Nie ma czasu na myślenie, tylko na działanie."
    menu:
        "Triple T":
            if randomCorrectChoiceIndex == 1:
                jump ch02_KamilRobberyCorrectChoice
            else:
                jump ch02_KamilRobberyWrongChoice
        "Lirili larila":
            if randomCorrectChoiceIndex == 2:
                jump ch02_KamilRobberyCorrectChoice
            else:
                jump ch02_KamilRobberyWrongChoice
        "Garamararambraramanmararaman dan Madudungdung tak tuntung perkuntung":
            if randomCorrectChoiceIndex == 3:
                jump ch02_KamilRobberyCorrectChoice
            else:
                jump ch02_KamilRobberyWrongChoice
        "Japa kasti":
            jump ch02_KamilRobberyWrongChoice

label ch02_KamilRobberyCorrectChoice:
    play sound "gong.mp3"
    stop music
    "Twoja odpowiedź jest pewna siebie, a cień wątpliwości zostaje wyparty przez wiatr."
    "Jego uszy drgają, gdy słyszy odpowiedź, a oczy się rozszerzają."
    "Właściwie cały wyraz jego twarzy ulega zmianie."
    "Nie potrafisz jednak rozszyfrować reakcji oraz czy dokonałeś właściwego wyboru."
    "Stoi tam, patrząc na ciebie, próbując podsycić napięcie"
    m "..."
    m "Skąd wiedziałeś?"
    $ robberyStopped = True
    m "Grrr....."
    "Nieznajomy mężczyzna zaczyna na ciebie warczeć jak alfa."
    m "Heh.. Poza tym, wiedziałem że ty to powiesz..."
    you "{i}???{/i}"
    you "{i}To dobrze czy źle{/i}"
    m "Masz te swoje finanse..."
    you "I co, łyso ci? Teraz idź sobie zanim cię gdzieś zgłoszę."
    m "Ale jak... no dobra... teraz wygrałeś...{w} ALE NASTĘPNYM RAZEM NIE BĘDZIE TO TAKIE ŁATWE!!!!"
    play music "town_day.mp3"
    hide kamil with dissolve
    you "{i}Nie będę nosił ze sobą pieniędzy!{/i}"
    jump ch02_gotMoney

label ch02_KamilRobberyWrongChoice:
    play sound "gong.mp3"
    stop music
    "Twoja odpowiedź jest pewna siebie, a cień wątpliwości zostaje wyparty przez wiatr."
    "Jego uszy drgają, gdy słyszy odpowiedź, a oczy się rozszerzają."
    "Właściwie cały wyraz jego twarzy ulega zmianie."
    "Nie potrafisz jednak rozszyfrować reakcji oraz czy dokonałeś właściwego wyboru."
    "Stoi tam, patrząc na ciebie, próbując podsycić napięcie."
    m "..."
    m "Nie oddam ci twoich pieniędzy."
    you 'Do jasnej muffinki!'
    m "NOI ESSA, A TERAZ SPADAJ ZANIM CI JESZCZE WIĘCEJ ZABIORĘ."
    menu:
        "Odpowiedz normalnie":
            you "Chytry dwa razy traci!"
            m "???"
            hide kamil with dissolve
            you "{i}On chyba mnie nie zrozumiał...{/i}"
        "Bądź final girl":
            you "Ale nie mam więcej."
            m "Ha-ha-ha! Jesteś biedny!"
            you "To czemu okradasz ludzi?"
            you "Bo nie masz własnych pieniędzy?"
            m "I tak nawet nie wiesz, na co to wydać."
            you "Chciałem kupić buły w BBB?"
            m "To przecież ma tyle kalorii..."
            you "Jak tak się przejmujesz kaloriami, to pomyśl o te w swoim mózgu."
            you "Bo ich tam nie ma jak w pepsi zero."
            you "Puknij się w ten głupi i pusty łeb!"
            m "Po co??"
            you "No zrób to."
            "Stuka się w ten głupi łeb i wydaje to taki dźwięk, że słychać, że tam nic nie ma."
            you "No właśnie!"
            hide kamil with dissolve
            "Złodziej zaczyna płakać i ucieka."
    play music "town_day.mp3"
    you "{i}To nie mój problem.{/i}"
    you "{i}Przez tego idiotę teraz muszę wrócić do Kurowskiej i zapytać co robić...{/i}"
    you "{i}Trochę się boję co może ona zrobić, ale no cóż, nic innego nie mogę wymyślić.{/i}"
    scene bg secretary with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Wracasz do urzędu miasta, ale nie zastajesz Filipa, więc pukasz do drzwi Kurowskiej."
    "..."
    you "Dzień dobry. To znowu ja."
    k "Wejdź."
    scene bg office with dissolve
    play sound "sfx_door_open.mp3"
    "Wchodząc czujesz, że ćwiczyła skip Triple-T."
    show kurowska normal with dissolve
    you "Przepraszam, że znowu przeszkadzam, ale zostałem okradziony."
    you "Zabrano mi wszystkie pieniądze. Teraz nie wiem co mam robić."
    you "Czy będzie mogła pani mi pomóc?"
    "Uśmiechasz się jak w reklamie nieruchomości."
    k "A co ja jestem wróżką?"
    you "Nie... Ale myślałem, że pomoże pani potrzebującemu..."
    k "Oddałam ci wszystko co miałam. Inni nic nie dostali i nie narzekają."
    k "Znajdź Pracę."
    hide kurowska normal with dissolve
    jump ch02_goingToFindAJob

label ch02_goingToFindAJob:
    scene bg citysquareday with dissolve
    play sound "sfx_door_open.mp3"
    "Wychodzisz na zewnątrz, żeby zastanowić się co powinieneś zrobić dalej."
    "Jak powiedziała Kurowska, powinieneś wybrać kogoś kogo znasz i pójść do niego, żeby poprosić o pracę."
    "Stoisz na rynku i rozglądasz się, jakbyś miał całować ziemie, trzymając cyprysowy krzyżyk."
    "Ponieważ nie chcesz dzisiaj umrzeć z głodu. Do kogo idziesz pracować?"
    menu:
        "Vasili (to jest ta ciekawsza opcja)" if metVasili:
            you "{i}Pójdę do niego tylko dlatego, że jestem ciekaw.{/i}" 
            you "{i}Poza tym chyba nie mam lepszej opcji.{/i}" 
            $ workedAtVasili = True
            jump ch02_workingAtVasili
        "Filip":
            you "{i}Kurowska nie ma dla mnie roboty, ale Filip już może mieć.{/i}" 
            $ workedAtFilip = True
            jump ch02_workingAtFilip

label ch02_workingAtFilip:
    "Wracasz do urzędu i idziesz do Filipa."
    scene bg secretary with dissolve
    play sound "sfx_door_open.mp3"
    you "A to znowu ja."
    f "Hejka."
    you 'Jeszcze jedno pytanko.'
    f 'Tak?'
    you 'Masz może jakąś robotę dla mnie?'
    you 'Czy jest dosłownie cokolwiek co mogę zrobić?'
    f 'Hmm...'
    "Filip wstaje i znowu idzie do swojej szafy." 
    "Słychać, że znowu przesuwa ciężkie pudła, ale tym razem trwa to dłużej." 
    "Wychodzi z ogromnym stosem dokumentów. Potem wraca i przynosi jeszcze więcej papieru." 
    "Zanim się obejrzysz, na biurku przed tobą są już dwa wysokie stosy dokumentów, a biurko się wygina od ich ciężaru"
    "Potem wraca z wózkiem na bagaże, tylko że zamiast walizek są tam papiery."
    you 'Co to w ogóle jest?'
    f 'A to są po prostu jakieś papiery i poczta, która nigdy nie dotarła do Kurowskiej.'
    f 'Po prostu przez lata zbierałem i uważałem, że nie jest zbyt ważna, więc ją trzymałem.'
    f 'A teraz ona chce to wszystko zobaczyć.'
    you 'No to co mam z tym zrobić.'
    f 'Weź te wszystkie dokumenty i zanieś je do Kurowskiej.'
    you 'Ale nie dam rady tego unieść ty jesteś zdrowy??'
    f 'Nie mówię ci żebyś niósł wszystko na raz głuptasie.'
    f 'Tu jest z 120kg papieru na tym biurku nie oczekuję że to podniesiesz.'
    f 'Zwłaszcza z twoim snatched waistem...'
    you 'No spoko...\n {i}ZAUWAŻYŁ!!!{/i}'
    "Podnosisz mały stosik papieru. Po chwili zaczyna ci się nudzić, więc czytasz to co przenosisz."
    "Najwidoczniej przenosisz jakieś skargi."
    "Każdy nagłowek jest gorszy od poprzedniego."
    "Pierwsza strona ma tytuł 'Raport o hałaśliwych sąsiadach'."
    if metVasili:
        you "{i}Wiadomo, że chodzi o Vasiliego pff..{/i}"
    "Z każdą linijką coraz trudniej powstrzymać śmiech, bo ten raport jest tak absurdalny, że aż nierealny."
    "Nie dziwota że Filip uznał to za nieważne - wygląda jak jakiś fanfik."
    you "{i}Krzyczenie 'WYPAROWAĆ BURŻUAZJĘ!!!' podczas mojej pracy było niestosowne.{/i}"
    you "{i}KTO TO NAPISAŁ?{/i}"
    "Pukasz do drzwi Kurowskiej."
    if rudeToKurowska:
        k "KTO TAK PUKA NA BELZEBUBA??"
    else:
        k "Wejdź."
    "Wchodzisz do biura Kurowskiej i nie możesz uwierzyć w to, że ona serio zamierza czytać te maile."
    you 'Gdzie to zostawić?'
    k 'Na moim stole.'
    you 'Na pewno? Ten papier NIE jest skinny.'
    k 'Dobra zostaw na podłodze.'
    "Zostawiasz pierwszy stosik papierów na podłodze." 
    "Nosisz dzielnie jeden po drugim, ale część ciebie chce tylko czytać te śmieci."
    "Nagłówki są coraz bardziej dzikie..."
    "{i}'Kapelusz Rafała sieje dramat wśród Bratgrenian.'{/i}"
    "{i}'Skarga na robale z Kolorado atakujące pomidory.'{/i}"
    "{i}'Ktoś mi nasrał przed drzwiami do domu proszę to usunąć.'{/i}"
    "{i}'Pilne: Sąsiad lewituje jak dua lipa. To chyba czarna magia.'{/i}"
    "Zanim się obejrzysz przeniosłeś już wszystko i zabrakło ci nagłówków do czytania."
    you 'Dużo tych mailów...'
    k 'Co? jakich mailów?'
    you 'No tych które noszę od ostatnich 20 minut.'
    k 'MAILE?? prosze mi je wynieść, to praca filipa, ja mam ważniejsze rzeczy na głowie!'
    you 'To po co ja je tyle nosiłem?'
    "Bierzesz z rezygnacją kupkę mailów i wracasz do filipa."
    f 'A co ty tu robisz z tymi papierami?'
    you 'Kurowska powiedziała że to ty masz odpowiadać na maile.'
    you "I że muszę z powrotem je przenieść."
    f 'CO? zdążą zamknąć przedsionek zanim skończę odpowiadać na nie wszystkie...'
    f 'No dobra... przynieś je tu wszystkie.'
    "Po kolejnych 20 minutach kończysz pracę u filipa, który teraz leży zdruzgotany na stercie papierów."
    f 'Dzieki za pomoc, chociaż w sumię nic sie nie zmieniło.'
    f 'Zgodnie z obietnicą masz tu od mnie kilka drobniaków.'
    jump ch02_gotMoney

label ch02_workingAtVasili:
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
    jump ch02_gotMoney
    
label ch02_gotMoney:
    scene bg citysquareday with dissolve
    "Masz dość bycia głodnym, więc idziesz prosto do BBB."
    "(Big Buły Bakery)"
    jump ch02_gotMoneyBakeryEntrance

label ch02_gotMoneyBakeryEntrance:
    scene bg bakeryfrontday with dissolve
    play sound "sfx_footsteps_b.mp3"
    "Piekarnia jest rzeczywiście duża. Zapachy rozchodzące się po ulicy doprowadzają cię do szału."
    "Zapach drożdży unosi się w powietrzu, a za szybą jest wiele wypieków."
    scene bg bakeryinside with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Pierwsze co zauważasz w środku to plakaty Taylor Spit."
    "Ale{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}. Jest kolejka."
    show wp normal at leftish with moveinleft
    show fraucrusty normal at center with moveinleft
    show rafal normal at rightish with moveinright
    "Przed tobą są dwie osoby."
    "Pierwszą w kolejce jest Frau Crusty."
    if metWiktoriaP:
        you "O, hej."
        wp "No cześć! Co tam?"
        
        if workedAtFilip:
            you "Masakra... Musiałem pracować..."
            wp "Do kogo poszedłeś?"
            you "Do Filipa."
            you "Kazał mi przenosić dokumenty do Kurowskiej."
            you "A jak już skończyłem, Kurowska kazała mi z powrotem przenieść te listy."
            you "Bo to on ma je czytać."
            wp "Trzeba było zarządać pieniądzy i wyjść po czymś takim."
            wp "I skibidi."
        elif workedAtVasili:
            you "Masakra... Musiałem pracować..."
            wp "Do kogo poszedłeś?"
            you "Do Vasiliego."
            if endorsedCommunism:
                you "Wiesz co, nie było źle."
                you "Mamy lekko podobne poglądy polityczne."
                "Wiktoria robi bombastic side eye."
            else:
                you "Jezu, to była masakra, cały czas o komuniźmie gadał."
            you "Szkoda gadać."
            you "Ty go znasz lepiej ode mnie, pewnie wiesz jak to wyglądało."
            wp "Let me guess."
            wp "Śpiewał \"Międzynarodówkę\"?"
            you "Tak..."
            wp "Współczuję..."
        else:
            you "Czaisz, że dostałem pieniądze od Kurowskiej"
            wp "Tak o??"
            you "No tak!"
            you "Tak o."
            wp "Nie za dobrze ci?"
            you "Nie."
    else:
        "Natomiast, zaraz przed tobą jest Wiktoria P."
    jump ch02_gotMoneyBakeryCustomer

label ch02_gotMoneyBakeryCustomer:
    frau "A cóż to za bezczelne pytanie?"
    frau "Oczywiście, że mam pieniądze."
    frau "Tylko dzisiaj brakuje mi 23 foryntów."
    frau "Mogę je przynieść jutro???"
    m "No nie jestem bankiem. To tak nie działa. Nie wydam tego tortu jeśli ktoś za niego nie zapłaci."
    frau "Ale mam dzisiaj urodziny!!!"
    menu:
        "Daj jej trochę monet":
            you "Masz."
            frau "Mój gyatt tutaj utknie na dobre!"
            frau "Dziękuję Ci dobry furasie."
            with vpunch
            show fraucrusty normal at offscreenleft with move
            "Frau Crusty wychodzi z piekarni z tortem skipem C."

        "Udawaj, że nic nie słyszałeś":
            frau "Wszyscy jesteście bezczelni i agresywni."
            with vpunch
            show fraucrusty normal at offscreenleft with move
            "Frau Crusty wychodzi z piekarni bez tortu skipem C."
    hide fraucrusty
    jump ch02_gotMoneyBakeryTea

label ch02_gotMoneyBakeryTea:
    wp "Okeeej."
    m "Hejka."
    wp "No cześć, co tam?"
    m "A w sumie nic, w malignie byłem cały dzień."
    wp "Tak standardowo bym powiedziała."
    "Oboje zaczęli się śmiać."
    wp "Poproszę 3 buły Rafała."
    m "Jasne."
    "Z tyłu widać całe koszyki z bułami Rafała."
    "Patrzysz się na te buły jak na monoporcje z Los Angeles."
    "Tylko, że buły Rafała nie kosztują $15 za 150g."
    "Nie masz zielonego pojęcia jaka to waluta jest w tym mieście ― pierwszy raz się z nią spotykasz."
    "Niby coś tam masz, ale nie wiesz czy tego starczy na jedną bułę, czy sto."
    you "{i}Te buły są tutaj mega popularne.{/i}"
    you "{i}Ale bym zjadł taką..{/i}"
    m "Proszę."
    "Nagle wchodzi kolejny nieznany ci mężczyzna."
    "Wygląda jak jakiś alfons."
    show niuniu normal at leftish
    show wp normal at rightish
    show rafal normal at right 
    with move
    m "Jezu, to znowu ty."
    m "Tak, Rafale, to ja!"
    r "No co ty chcesz ode mnie znowu?"
    m "Pokaż, co masz pod kapeluszem."
    "Wiktoria zaczyna mówić do ciebie szeptem, żeby nie ściągnąć na siebie uwagi."
    wp "To jest Niuniu."
    wp "To jest taki typ, co wymyśla teorie spiskowe w tym mieście."
    wp "I tym razem ofiarą jest Rafał."
    wp "On był na koncercie Taylor Spit i podczas tego koncertu ona rzuciła w niego swoim kapeluszem."
    wp "Od tego dnia cały czas go nosi."
    wp "A Niuniu wymyślił, że on coś pod nim ukrywa."
    show rafal normal at center 
    show wp normal at rightish 
    with move
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
    'Wyciągnął wielką, czerwoną cegłę obiema łapami i z dumą pokazał ją tobie, jakby była jego dzieckiem.'
    'Cegła była stara. Naprawdę stara.'
    'Już na pierwszy rzut oka dało się stwierdzić, że nie da się stwierdzić, ile dokładnie ma lat - liczne odpryski i rysy były na to dowodem.'
    'Właściwie była tak stara, że przypisanie jej jakiejkolwiek liczby wydawało się obrazą nie tylko dla cegły, ale i dla tego, kto ją stworzył.'
    "Nazwanie jej po prostu 'starą' oznaczałoby wymazanie stuleci, które przetrwała."
    'Cegła dawno straciła ostre krawędzie i stała się zaokrąglona, jakby była używana wielokrotnie.'
    'Jeden z rogów był szczególnie wytarty i nawet najmądrzejsza osoba w tym mieście nie potrafiłaby powiedzieć, dlaczego jest wyszczerbiony ani gdzie dokładnie jest ten róg.'
    'Tylko Rafał mógłby to wiedzieć - o ile wie albo pamięta, co się z nią stało.'
    'Jedynym zastosowaniem tej cegły było rzucanie, więc starasz się nie wyciągać pochopnych wniosków co do tego, kto będzie lub już był ofiarą.'
    'Patrząc na wyszczerbiony róg, staje się jasne, że to efekt pewnego powietrznego wydarzenia.'
    'Można by nawet uznać za cud, że cegła jeszcze nie pękła na pół.'
    "Że jeszcze nie pękła na pół, jak arbuz spadający na nóż z 100m w jakimś filmiku na youtubie"
    'Jej amorficzna porcelanowa struktura wciąż trzymała się mocno po tych wszystkich latach, czego nie da się powiedzieć o niektórych związkach.'
    'Cegła była na tyle stara, że mogłaby uchodzić za najstarszy obiekt na tej planecie - albo gdziekolwiek teraz jesteś.'
    'Nie wiesz dokładnie, gdzie jesteś, ale jedno jest pewne - ta cegła jest starsza niż ziemia, na której stoisz.'
    'Starość nie była już dla niej przymiotnikiem, tylko wrodzoną właściwością.'
    'Nieważne, gdzie Rafał dotyka cegły swoimi łapkami - osypuje się trochę kurzu i pokruszonej gliny, jakby cegła miała łupież.'
    'Rafał jednak całkowicie ignoruje bałagan, który właśnie zrobił, jakby był do tego przyzwyczajony.'
    'Ignoruje też pył na swoich miękkich łapkach, bo wie, że i tak zaraz schowa ten delikatny wyrób z gliny, więc nie ma sensu ich myć.'
    'W tym momencie każdy rozsądny człowiek przestałby myśleć o cegle.'
    'Ty jednak nie przestajesz.'
    'Jedna ze stron cegły była ciemniejsza od pozostałych - jakby była wystawiona na działanie warunków atmosferycznych, podczas gdy reszta spoczywała bezpiecznie w ścianie.'
    "Prawdziwi naukowcy mogliby poświęcić całe życie badaniu tej różnicy i nadal nie dojść do porozumienia."
    "Tak tajemnicza była ta cegła."
    'Nie da się stwierdzić, czy Rafał wyjął cegłę, czy sama wypadła.'
    'Można jednak zauważyć, że cegła {i}należy{/i} do tej piekarni, ze względu na swój charakterystyczny, ale już wyblakły, czerwony kolor, który był bardziej przygaszony niż reszta cegieł w tej piekarni.'
    'Przy bliższym spojrzeniu widzisz wszystkie jej niedoskonałości - ślady, które zostawił czas.'
    'Pęknięcia są wypełnione kurzem tak starym i tak głęboko osadzonym, że nawet woda nie jest w stanie tam dotrzeć.'
    'Stały się częścią kapsuły czasu, którą jest ta cegła.'
    'Ta cegła była prawdopodobnie starsza niż ty i znajdowała się w tym mieście długo przed twoimi narodzinami.'
    'Widziałeś przez nią setki, jeśli nie tysiące ludzi i miliony wypowiedzianych słów.'
    'Cegła zna wszystkie sekrety miasta, ale nie może mówić ani ujawnić prawdy.'
    'Miała też wyraźnie wyznaczone miejsce pod biurkiem Rafała, gdzie trzymał kasę i prowadził codzienny handel.'
    'Nie każdy klient wiedział - albo mógł nawet podejrzewać - istnienie tej cegły.'
    'Jeśli Rafał wyciąga ją przed tobą, oznacza to, że jesteś albo ofiarą, albo jego bliskim przyjacielem.'
    'Zauważasz też małe, wielokolorowe plamy rozsiane po jej powierzchni - każda inna, każda o innym kształcie, rozmiarze i własnej historii.'
    'Jedna może mieć dwa dni, a druga obok niej ponad dwa lata, bez żadnej możliwości odróżnienia.'
    'Bo w tym wszechświecie nie wynaleziono datowania radiowęglowego.'
    "Mimo pozornej przeciętności 'losowej cegły' nie możesz pozbyć się wrażenia, że w tej amorficznej strukturze zaklęte są codzienne sprawy mieszkańców miasta Bratgren."
    'Od nieświadomych kroków ludzi zbyt zajętych, by zwracać uwagę na zwykłą cegłę, po gęsty deszcz, który po prostu miał zmoczyć wszystkich.'
    'Te wszystkie zdarzenia nie zostawiły po sobie tylko historii - stały się osadem.'
    'Cienką, kruchą warstwą drobnych rzeczy, które zmieniały tę cegłę, cegła po cegle, krok po kroku.'
    "Patrzysz na małe otwory w cegle, gdy nagle coś zaczyna do ciebie docierać."
    "Cegła sprawia, że czujesz coś, czego wcześniej nie czułeś."
    "Przynajmniej nie w tym mieście."
    "Z powodów, których nie potrafisz wyjaśnić, patrzenie na nią napełnia cię determinacją."
    "Determinacją tak silną, że wszystkie twoje plany, te odkładane w nieskończoność, nagle wydają się nie tylko możliwe, ale konieczne."
    'Nie możesz już zatrzymać tego wiru myśli, który ta starożytna architektura wywołała w twojej głowie, więc wydajesz z siebie długie, dramatyczne westchnienie.'
    'Chcesz, by każda inna cegła w tej przytulnej kawiarni wiedziała, że rozumiesz jej historię.'
    'Ta cegła i jej przeszłość inspirują cię, by iść dalej i się nie poddawać.'
    'Dla zwykłej osoby to była zwykła cegła, ale twoje oczy widzą coś innego - źródło inspiracji i determinacji w tak prostym obiekcie.'
    "Helen Keller powiedziała kiedyś - \"Alone we can do so little; together we can do so much\" - i nic lepiej nie opisałoby tej cegły."
    'Cegła była częścią czegoś większego, bardziej monumentalnego, choć nie wiesz czego.'
    'Cegły mogą być używane do budowania wszystkiego - od małego muru podczas protestu w Paryżu po wielką willę zdolną przetrwać tornado.'
    'Tak jak jedna z tych cegieł, ty również jesteś częścią tego miasta.'
    'Miasta, które przyjęło cię z otwartymi ramionami.'
    r "Jezu, mam go dość, on tak mnie irytuje."
    you "Nie dziwię ci się."
    r "..."
    r "No dobra, co tam chciałeś?"
    "Zapomniałeś o jedzeniu przez to, co się właśnie wydarzyło."
    you "Poproszę 3 buły Rafała."
    r "Jasne."
    r "Ale czekaj, nie widziałem cię wcześniej?"
    r "Nie pracujesz przypadkiem na drugim końcu miasta?"
    wp "No właśnie, też mi się tak wydawało."
    you "Nieee, jestem tutaj nowy."
    you "Urodziłem się wczoraj, jak Konrad."
    "Rafał uważnie cię słucha, wkładając buły do papierowej torebki."
    r "Aha, ma sens."
    you "Widzę, że masz plakaty Taylor Spit."
    r "Znasz ją?"
    you "Tak. Kojarzę ją."
    r "Wow! Ale heca."
    "Wyciągasz bułę Rafała i zaczynasz ją jeść."
    "Ale nie tak normalnie, jakbyś jadł kajzerkę z Biedronki."
    "Tylko jak jakiś homofob jedzący banana."
    "Odrywasz pierwszy kawałek buły ręką i Rafał patrzy się na ciebie, jakbyś popełnił zbrodnię."
    r "Co ty robisz..."
    you "W sensie?{w=.6} Jem."
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
    you "{i}Oby nie zieloną!!!{/i}"
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
    r "Okej dobra to ja zacznę."
    r "Mam taką herbatę"
    r "Nad tą piekarnią mieszkają ludzie, co nie?"
    r "A więc..."
    r "Wczoraj nie miałem dużo klientów i było cicho."
    r "I teraz uwaga."
    r "Słyszałem, jak jakaś pani kłóciła się ze swoim mężem."
    wp "CO..."
    r "Tak się darli, że to szok!"
    wp "Co ta żona mówiła?"
    r "No dobra, cicho wrócę do tego."
    r "Okazuje się, że ten mąż ją zdradzał."
    r "Z tym typem, który zbiera podatki."
    r "On się tłumaczył, że zrobił to, żeby tych podatków nie płacić."
    menu:
        "Zgadzam się z żoną":
            you "Ale to nie można tak..."
            you "Jak to można tak zdradić?"
            you "Masakra."
            wp "Szczerze to valid crashout."
        "Zgadzam się z mężem":
            you "Może naprawdę są biedni?"
            you "Wtedy {b}MOŻE{/b} zrozumiem."
            you "Nie zrobił tego tak dla fabuły..."
            r "No właśnie zrobił to dla fabuły."
            r "Bo mu się nudziło!"
    r "Co gorsza, znam ich..."
    r "Ta żona jest siostrą babci brata kuzynki siostry mojej koleżanki z byłej pracy."
    you "No..."
    you "To jest trochę szalone{w=.3}, że takie rzeczy się dzieją w tym mieście."
    r "Uwierz mi, są gorsze plotki."
    "Mimo że bardzo interesują Cię plotki, dzisiaj dajesz im spokój."
    wp "Dobra, teraz ja!"
    "Wiktoria pochyla się bliżej ciebie."
    wp "Nie chcę brzmieć jak Niuniuś, którego Rafał pobił miotłą, ale...{w=.3} muszę zapytać."
    "Wiktoria pochyla się {b}JESZCZE{/b} bliżej ciebie."
    wp "Czy ty też uważasz, że to miasto coś ukrywa?"
    "Nie zajmuje ci dużo czasu, żeby odpowiedzieć na to pytanie."
    "Od kiedy Kurowska opowiedziała ci o tym mieście, wiedziałeś, że coś jest nie tak."
    "Trudno powiedzieć, czy to była twoja inteligencja{w=0.5}, czy po prostu jesteś normalnie taki podejrzliwy wobec wszystkiego."
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
    wp "WIDZISZ RAFAŁ!!!"
    wp "Mówiłam ci."
    r "No dobra, powiedzmy, że masz rację."
    r "I co teraz?"
    wp "Nie wiem, ale..."
    wp "Trzeba coś zrobić po prostu."
    you "No rel."
    you "Jest może jakieś muzeum w tym mieście?"
    wp "No jest. To jest ten kościół."
    you "No to idziemy tam."
    wp "Okej."
    wp "Mogę jutro o 10:00."
    you "No to spotykamy się na rynku o 10:00."
    wp "Dobra."
    r "A ja, to co?"
    wp "Ale czy ty chcesz z nami iść do kościoła?"
    r "Nie."
    wp "No właśnie."
    you "Dobra, to wiecie co.."
    you "Dziękuję za herbatę, jesteście mega fajni."
    you "Ale ja muszę iść."
    you "Popatrzę się jeszcze raz na tę fontannę na rynku i pójdę do krawcowej."
    you "Bo nie mam żadnych ubrań."
    wp "Paaa"
    r "Do widzenia, senorita."
    you "{i}Jestem dumny z siebie.{/i}"
    you "{i}Chyba znalazłem besties w tej piekarni!!!{/i}"
    scene bg bakeryfrontday with dissolve
    "Wychodzisz i idziesz prosto do tej fontanny."
    "Na szczęście miejsce docelowe jest blisko."
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
    you "Czekaj tu, ja zaraz wrócę."
    bjork "Nie ufaj w{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    play sound "sfx_footsteps_a.mp3"
    scene bg bakeryfrontday with dissolve
    "Biegniesz z powrotem do piekarni, żeby powiedzieć Rafałowi i Wiktorii o tym, co właśnie zobaczyłeś."
    "I tak ci pewnie nie uwierzą, ale musisz spróbować."
    "Wiesz, jest duża szansa, że będziesz wyglądał jak idiota, jeśli na serio tylko ty możesz widzieć Bjork."
    "Bo jak nie, to serio masz schizofrenię."
    scene bg bakeryinside with vpunch
    you "Duch Bjork jest przy fontannie."
    with vpunch
    play sound "sfx_footsteps_alot.mp3"
    "Wiktoria nie traci ani sekundy i wybiega z piekarni."
    with vpunch
    play sound "sfx_footsteps_alot.mp3"
    "Rafał biegnie za Wiktorią, nawet nie zamykając piekarni."
    play sound "sfx_footsteps_b.mp3"
    scene bg fountainday with dissolve
    show wp normal at leftish with moveinleft
    show rafal normal at rightish with moveinleft
    r "Nikogo tu nie ma."
    you "Ona zrobiła ze mnie idiotę."
    you "Zrobiła ze mnie idiotę jak w jakimś stereotypowym filmie o duchach."
    r "Nie wiem czy Wiktoria ci wierzy, ale ja tak."
    r "Na pewno coś widziałeś."
    r "..."
    you "I co teraz?"
    wp "Nie wiem."
    r "Nie wiem."
    you "Bjork pewnie nas podsłuchiwała w tej piekarni."
    you "{i}Jeśli ty to słyszysz, proszę mnie nie nawiedzać.{/i}"
    you "{i}Bo nie wytrzymam.{/i}"
    "Patrzycie się na tę fontannę, ale nic dziwnego się nie dzieje."
    r "Dobra, ja chyba wracam."
    wp "No, ja już też idę."
    you "Naprawdę przepraszam, że was tak oszukałem trochę."
    wp "Ok."
    you "No to cześć."
    r "Cześć siedem!!!"
    jump ch02_GoingToTheTailor

label ch02_GoingToTheTailor:
    play music "town_day.mp3"
    scene bg lanastreetday with dissolve
    "Tym razem idziesz prosto do krawcowej."
    "Bez żadnych duchów lub jakiejś fontanny."
    "Na szczęście to nie było trudne, bo krawcowa jest tuż obok piekarni."
    "Jej sklep wygląda tak ostentacyjnie, że aż stoisz i się gapisz."
    "Jest pięknie."
    "Kiedy w końcu się ogarniasz, wraca ci logiczne myślenie i zaczynasz myśleć o cenach."
    "Raczej nie masz tyle kasy, żeby coś kupić w takim miejscu."
    "Jednakże, wchodzisz do środka i się rozglądasz."
    scene bg tailorshop with dissolve
    play sound "sfx_door_open.mp3"
    play music "tailor.mp3"
    "Wszystko jest zastawione pięknymi sukienkami, koszulami, spodniami i innymi ubraniami, których nazw nie znasz."
    "Odwracasz głowę i widzisz zwykłe białe koszule i nudne spodnie, które bardziej pasują do twojego budżetu."
    "Wtedy słyszysz głos kobiety z kąta. To była krawcowa."
    "Na początku jej nie zauważyłeś przez te wszystkie kolorowe ubrania wokół niej."
    you "{i}Idealny kamuflaż{/i}"
    show ww normal with dissolve
    m "Dzień dobry!"
    you "Dzień dobry!"
    you "Nazywam się [name] i jestem nowy w tym mieście."
    m "Masz fajne imię."
    you "A dziękuję, dziękuję."
    m "Czy Pan czegoś szuka?"
    you "Proszę mówić do mnie na \"ty\"."
    you "To nie jest LinkedIn."
    m "Aha, dobra."
    you "Kropki też w sumie nie są potrzebne bo wygląda jakbyś była zła na mnie"
    ww "Ok"
    you "A jak ty masz na imię?"
    ww "Wiktoria"
    you "Omg, już znam jedną"
    ww "No my też się znamy"
    ww "W tym mieście są tylko dwie"
    you "Jednak małe jest to miasto wszyscy się znają"
    you "Podoba ci się tu?"
    ww "Jak się nie ma co się lubi to się lubi co się ma"
    you "{i}Mądre słowa... Ale trzeba act nonchalant!!!{/i}"
    you "Ma sens"
    ww "No to dobra, szukasz czegoś?"
    you "Na razie tylko się rozglądam, bo nie wiem czy mam pieniądze na takie ubrania"
    you "Są piękne i w tym jest problem"
    show ww normal at offscreenleft with move
    ww "Dobra, to podejdź do mnie jak coś znajdziesz"
    "Krawcowa wraca do swojego stołu i zaczyna rysować roznegliżowaną kobietę w swoim zeszycie."
    "W tym samym czasie masz dylemat, ponieważ nie wiesz, co masz kupić."
    "Więc chodzisz po tym sklepie i się tylko gapisz na wszystkie tekstylia."
    "Są przynajmniej dwa powody, dla których nie wiesz, co kupić."
    "Pierwszy jest najprostszy. Nie wiesz czy te ubrania są drogie czy tanie."
    "Mieszkasz w tym mieście tylko dzień, więc nie rozumiesz ich waluty."
    "Po drugie, nie wiesz czy będziesz pasował do reszty mieszkańców."
    "Nie zwracałeś uwagi na to, co noszą mieszkańcy tego miasta."
    "Ale jesteś zbyt leniwy, aby wyjść ze sklepu."
    "Na Temu można kupić kostium dużej kaczki, ale żaden psychicznie zdrowy człowiek nie wyjdzie w tym na rynek."
    "Patrzysz się przez okno, aby kogokolwiek zobaczyć ale jest już za ciemno."
    "Światło ze sklepu odbija się w oknie, przez co kompletnie nie widać ulicy."
    "Długo chodzisz po tym sklepie i przypadkiem wchodzisz do pokoju z napisem \"burżuazja\""
    "W tym sklepie są identyczne ubrania, tylko że ceny są liczbami z zakresu <100,000; +9,223,372,036,854,775,807>."
    "W rzeczywistości stoisz przed jedną z tych sukienek."
    "Sukienka przed tobą nie wygląda nie na miejscu w tym sklepie, a jednak jej cena jest najwyższą liczbą, jaką kiedykolwiek widziałeś."
    "Jej cena jest tak wysoka, że zostały użyte potęgi, aby ją zapisać."
    "Wychodzisz z tego pokoju, ponieważ gdybyś coś zepsuł to byś musiał pracować całe życie, żeby spłacić 1%% długu."
    "W tym momencie chodzisz po sklepie już od godziny i znów jesteś w punkcie wyjścia; nie wiesz, co kupić."
    show ww normal at center with dissolve
    "Podchodzisz do krawcowej, aby poprosić ją o pomoc i widzisz piękną kobietę w jej zeszycie."
    you "Czy mogłabyś mi pomóc?"
    you "Nie wiem co kupić..."
    ww "Już"
    "Krawcowa wstaje i podchodzi do ciebie i zaczyna krążyć w okół ciebie tak jak Księżyc w okół Ziemi."
    "Wyciąga metr aby zmierzyć twojego skinny waista."
    if hasSkinnyWaist:
        ww "To jest niemożliwe!"
        ww "Twój skinny waist ma 3 centymetry!!!"
    else:
        ww "Ale masz skinny waista..."
    you "Właśnie w tym jest problem, bo nie mogę nic wybrać"
    ww "A co byś chciał?"
    you "Na pewno chcę wyglądać normalnie"
    you "Normalnie w sensie{w=.3} jak każdy inny mieszkaniec tego miasta"
    "Krawcowa kładzie swoją rękę na żuchwę, robiąc taki gest aby pokazać ci, że intensywnie myśli o tym, w co może cię ubrać."
    ww "Dobra wiem{w=.3}, stój tu grzecznie ja zaraz wrócę"
    hide ww normal with dissolve
    "Wiktoria zostawia ciebie przed lustrem i gdzieś idzie."
    "Znowu się patrzysz na te proste ubrania dla biednych ludzi."
    "I już czujesz ten wstyd, bo w porównaniu do tych drogich to te wygladają jak dla kloszardów."
    "Po chwili wraca Wiktoria z ubraniami i jakimś pudełkiem."
    show ww normal at center with dissolve
    "Krawcowa postawiła pudełko na podłodze, aby pokazać ci twoje nowe ubrania."
    "Pokazuje ci niebieskie jeansy i białą koszulkę."
    you "{i}Niebieskie dżinsy, biała koszula...{/i}"
    you "{i}Gdy weszła do pokoju, aż zapiekły mnie oczy.{/i}"
    "Przykładasz do siebie najpierw koszulę, a potem jeansy."
    you "Fajnie!"
    you "Mi się podoba"
    you "Wyglądam tak ― wiesz ― normalnie"
    ww "A teraz daj mi to i weź to"
    "Wiktoria daje ci jakieś inne ubrania."
    "Tym razem daje ci czarną sukienkę, czarną koszulkę i duży czarny melonik."
    you "Nie!"
    "Nawet nie przykładasz tego do siebie, ponieważ wiesz, że nigdy nie będziesz wyglądał jak Zendaya."
    "Poza tym, już wiesz co będziesz kupował."
    you "Zapytam się wprost"
    "Wkazujesz pazurem na jeansy z białą koszulką."
    you "Ile to kosztuje?"
    ww "To wszystko czy tylko te ubrania?"
    you "Jak to wszystko? To pudełko też?"
    ww "Tak, ale do tego wrócę"
    ww "Same te ubrania kosztują 150 foryntów"
    you "Myślałem, że w tym sklepie zbankrutuję"
    you "Mam tylko 670"
    ww "Starczy ci na parę dni."
    ww "Mówiłeś, że jesteś tutaj nowy co nie?"
    you "No, tak"
    ww "Okej to polecam zostawić 100 foryntów"
    ww "Ponieważ jutro pan Antonius będzie zbierał podatki"
    you "Skąd wiesz?"
    ww "W pół do komina"
    ww "On zbiera podatki co tydzień w sobotę"
    you "Aha, ma sens"
    you "{i}Czyli dzisiaj jest piątek...{/i}"
    you "Dobra to wracając do tych tekstyliów..."
    you "Mi się podoba"
    ww "Cieszę się"
    you "A teraz, co to za pudełko?"
    ww "To jest taki{w=.3} {i}starter pack{/i}"
    ww "Tam są majtki, skarpetki i inne rzeczy do higieny"
    ww "A i właśnie..."
    ww "Tych ubrań, majtek i skarpetek nie trzeba prać"
    you "Jak to?"
    ww "Srak to!"
    ww "Poprosiłam Piotra aby mi wynalazł magię na to"
    ww "No i od teraz ubrania są magiczne i w ogóle"
    "Te ubrania są magiczne specjalnie."
    "Bo nie chce mi się opisywać jak robisz pranie."
    you "Okej..."
    you "Ile to wszystko kosztuje?"
    ww "180 foryntów"
    you "Proszę"
    "Płacisz za wszystko, uśmiechając się do sprzedawczyni."
    "Widzisz słoik z napisem \"nawodnik (nie napiwek bo nie piję piwa tylko wodę)\"."
    "Czy chesz wrzucić parę monet do tej puszki?"
    menu:
        "Tak":
            "Wrzucasz resztę z swoich zakupów do tego słoika"
            ww "Thank you!{w=0.5} Thank you!{w=0.5} Thank you!"
            "Wiktoria uśmiecha się jak w reklamie nieruchomości."
        "Nie":
            "Nie wrzucasz nic, ponieważ słuchasz chopbra, melanie oraz shitseye"
    you "Dziękuję!!"
    you "A właśnie mam pytanie"
    ww "Słucham?"
    you "Widziałem sukienkę która kosztuje 3.5341*10^(67) foryntów. Czy ktoś w tym mieście naprawdę ma tyle pieniędzy?"
    ww "Nie"
    ww "Jeśli ktoś chce takie coś kupić to robię im zniżkę o wielkości 100%%-(7.931345876241576*10^-131)%%"
    ww "Żeby się zaprzyjaźnić z tą bogatą osobą"
    you "Ma sens"
    "Patrzysz się na tą sukienkę jeszcze raz, i teraz wiesz, że nie jest tyle warta, mimo tego, że jest piękna."
    you "Będę to nosił loud and proud!!!"
    ww "Cieszy mnie to"
    you "Dobranoc!"
    ww "Sayonara"
    "Po raz ostatni uśmiechasz się jak w reklamie nieruchomości i wychodzisz ze sklepu."
    jump ch02_goingHomeAfterTailor

label ch02_goingHomeAfterTailor:
    scene bg lanastreetnight with dissolve
    play sound "sfx_door_open.mp3"
    play music "town_night.mp3" fadein 1.0
    "Wychodząc ze sklepu, orientujesz się, że zapadła już noc."
    "Zastanawiasz się jakim cudem spędziłeś tyle czasu u krawcowej."
    "Ale to było tego warte, ponieważ masz już wszystko aby zacząć tu mieszkać."
    "Masz jedzenie, ubrania, pieniądze i nawet własny dom. Czego więcej można chcieć?"
    "Robisz 2 kroki do przodu kiedy widzisz przed sobą kościół."
    "Oraz osobę, która zamyka drzwi do tego kościoła, a potem bramę na klucz."
    "Nie wiesz kim jest ta osoba, ale jesteś na 99%% pewny, że to jest ksiądz."
    if receivedLoreAboutChurchOnTheFirstDay:
        you "{i}Jakim cudem Wiktoria otworzyła tę bramę, jeśli on zamyką ją na klucz?{/i}"
        you "{i}To chyba nie mogę ufać Wiktorii.{/i}"
        you "{i}Po co jej tyle powiedziałem...{/i}"
    "Patrzysz na swoje nowe ubrania, żeby nie zwracać na siebie uwagi."
    "Ale tak naprawdę, patrzysz się na tego księdza widzeniem peryferyjnym."
    "Kiedy ten mężczyzna jest wystarczająco daleko od kościoła, podchodzisz do niego bliżej."
    scene bg churchnighta with dissolve
    "Jutro będziesz tu z Wiktorią."
    "Najpierw patrzysz na niedawno zamknięte drzwi, potem na ogromny witraż"
    "Następnie delikatnie dotykasz bramy i czujesz, jak bardzo jest zakurzona, mimo że jest używana codziennie."
    "Teraz ten kościół jest zamknięty, więc nie możesz wejść do środka."
    "Z powodu braku rzeczy, które możesz teraz zrobić, idziesz do domu."
    scene bg colacocastreetnighta with dissolve
    "Gdzieś w połowie drogi masz takie przeczucie, że ktoś cię obserwuje."
    "Powietrze wokół ciebie robi się lekko chłodniejsze. Na tyle, że to zauważasz..." 
    "Przez chwilę nie wiesz, co powinieneś zrobić: biec do domu, czy być nonchalant ― iść, jakby nic się nie działo."
    "Nie jesteś pewien, czy w tej chwili jesteś delulu, ale potem przypominasz sobie, gdzie mieszkasz."
    "Istnieje magia, co oznacza, że prawie na pewno czujesz, że ktoś cię obserwuje."
    "Odwracasz się w taki sposób, aby pokazać, jak bardzo się \"nie boisz\", ale w głębi duszy masz nadzieję, że twoje oczy spotkają ptaka lub przypadkowego gryzonia."
    "Jednak nikogo nie ma. Nie można tego powiedzieć o twoim uczuciu, które wciąż tu jest, teraz silniejsze dzięki temu, że nie wiesz, gdzie jest twój \"szpieg\"."
    "Odwracasz się i idziesz, jakby nic się nie stało."
    "Uczucie w końcu ustaje, gdy wchodzisz do domu i zamykasz drzwi."
    "Na wszelki wypadek zamykasz wszystkie rolety."
    "Odkładasz buły Rafała do lodówki."
    you "{i}Mam nadzieję, że ten krasnal nie zje tych buł...{/i}"
    you "{i}Czy ja go musze karmić?{/i}"
    you "{i}Czy on jest jakimś szkodnikiem?{/i}"
    you "Cześć?"
    "Ten krasnal kompletnie ignoruje to, co do niego powiedziałeś."
    "Jest skupiony tylko na światełku w tej lodówce."
    "Z tej racji zamykasz lodówkę i kładziesz się spać."
    jump ch02_secondNightAtHome

label ch02_secondNightAtHome:
    play music "sleep.mp3" fadein 3
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
            jump ch02_afterRafalDream
        "Nie, może spać w kuchni. Nikomu nie powiem.":
            "Rafał wyciąga cegłę i mówi ci, żebyś wyszedł."
            jump ch02_afterRafalDream
        "Przejdziesz przez to. Nie martw się":
            "Rafał przytula cię i dziękuje za pomoc."
            jump ch02_afterRafalDream

label ch02_afterRafalDream:
    stop music fadeout 0.2
    "Nagle czujesz ciepłe promienie słońca na sobie i powoli otwierasz oczy."
    scene bg bedroom with dissolve
    "Przez krótką chwilę zauważasz, że zasłony są otwarte, mimo że zamknąłeś je wczoraj{w}, ale nie poświęcasz temu tyle uwagi, ile powinieneś."
    "Pewnie po prostu zapomniałeś je zasłonić."
    "Zapomniałeś, tak jak wszyscy w tym mieście."
    "Idziesz do łazienki, robisz nudne, higieniczne, prywatne a nawet relaksujące rzeczy, potem do kuchni, bo jesteś już głodny."
    jump ch02_dayTwo

label ch02_dayTwo:
    scene bg kitchen with dissolve
    play sound "sfx_footsteps_b.mp3"
    "Otwierasz lodówkę i widzisz, że połowy bułki brakuje{w=.3}, a twój własny krasnal patrzy na ciebie z najwyższej półki i się uśmiecha." 
    "Okazuje się, że jednak MUSISZ go karmić."
    "Bierzesz bułę, okruszki zostawiasz dla krasnala i wychodzisz."
    "W końcu musisz być na rynku za pół godziny." 
    play sound "door_knock.mp3"
    "W chwili, gdy masz już otworzyć drzwi, słyszysz pukanie i się wahasz." 
    play sound "door_knock_aggressive.mp3"
    "W zawachaniu twoja ręka zawisa nad klamką, ale słyszysz kolejne pukanie."
    
    "Z tego ambarasu otwierasz drzwi."
    "Uchylasz je tylko troszeczkę, żeby zobaczyć kto stoi na zewnątrz{w=.3} i widzisz surykatkę przed drzwiami."
    show antonius normal with dissolve
    "Uśmiecha się do ciebie takim uśmiechem, jaki mają pracownicy w customer service ― nie tak jak w reklamach nieruchomości ― ten uśmiech to taki uśmiech, jaki ludzie muszą mieć, nawet jeśli nie są szczęśliwi."

    m "Dzień dobry"
    you "Mogę w czymś pomóc?"
    m "Tak, możesz. Przyszedłem pobrać podatki."
    you "Aha dobra, tak, oczywiście, sekundę, chwileczkę. Nigdzie nie odchodź."
    you "Stój tu grzecznie!"
    scene bg bedroom with dissolve
    "Otwierasz drzwi, ale nie wpuszczasz przypadkowego pracownika rządu do domu."
    "Idziesz do sypialni, gdzie zostawiłeś wszystkie swoje rzeczy, bierzesz wszystkie pieniądze i wracasz do drzwi wejściowych."
    scene bg kitchen with dissolve
    show antonius normal with dissolve
    you "Ile jestem winien?"
    m "100 foryntów"
    you "Jaka ładna liczba!"
    you "Okej, proszę... Proszę bardzo... yyy..."
    you "Jak masz na imię?"
    a "Antonius Cornelius-Benedictus"
    you "No to masz... yy.. anadius coś tam"
    you "Dobra, teraz idź, idź, idź, ja muszę gdzieś być za 10 minut"

    play sound "sfx_footsteps_alot.mp3"
    play music "town_day.mp3"
    scene bg lanastreetday with dissolve
    "Delikatnie odpychasz go na bok i zamykasz drzwi, po czym biegniesz sprintem na rynek{w=.3}, zostawiając zdezorientowaną surykatkę o bardzo długim i dziwnym imieniu przed drzwiami."
    jump ch02_goingToTown

label ch02_goingToTown:
    "Pędzisz na rynek, jedząc po drodze jedyne jedzenie, jakie masz."
    "Kiedy tam docierasz, widzisz stojącą tam Wiktorię."
    wp "O, hejka!"
    you "Cześć―siedem."
    wp "..."
    you "Dobra chodźmy do tego kościoła."
    wp "Dobra."
    you "Widziałem tego księdza wczoraj."
    you "Chyba księda."
    you "Nie jestem pewny."
    you "Ale, wychodził wczoraj z kościoła."
    wp "No to na pewno był ten ksiądz."
    wp "Ma na imię Wiesław."
    wp "Ale wszyscy mówimy na niego wsiok bo tak się zachowuje."
    you "Jak?"
    wp "On jest jak osa. Osy tylko latają i żądlą."
    wp "Tak jak on tylko pracuje w tym kościele i je."
    wp "Przy ołtarzu jest cały święty, a w piątek po południu pewnie pije w domu."
    scene bg churchdaya with dissolve
    "Podchodzicie do bramy i Wiktoria wsadza rękę przez pręty bramy i otwiera ją od środka."
    if metTomcio:
        "Tak jak ty otworzyłeś bramę Tomcia."
    you "Czekaj jak on ma na imię?"
    wp "Wiesław."
    you "{i}Jego imię też jest na W{/i}"
    you "{i}Znam już 3 takie osoby...{/i}"
    you "{i}To komu ja w końcu mam nie ufać?{/i}"
    you "Po co otworzyłaś bramę? Można bylo przejść tamtędy."
    "Wskazujesz pazurem na furtkę."
    wp "Aha, nie widziałam tego..."
    you "Tak szczerze to ja też dopiero teraz to zauważyłem."
    "Oboje śmiejecie się z tego."
    wp "Dobra cicho!"
    wp "Bo wyjdzie zaraz."
    wp "Chodź!"
    jump ch02_enteringChurch

label ch02_enteringChurch:
    "Wiktoria podchodzi do drzwi i delikatnie puka."
    "Po chwili słychać czyjeś mamrotanie po drugiej stronie drzwi."
    "Otwiera się takie mini okienko, przez które widać tylko parę oczu."
    "(Takie mini okienko w sensie no.)"
    "(Według googla to się nazywa judasz ale nie wiem do końca czy to jest to.)"
    "(Bo to jest dosłownie takie okienko ale no.)"
    "(Więc niech tak zostanie.)"
    "Te oczy patrzą najpierw na Wiktorię, potem na ciebie."
    "Wiesław westchnął, jakby Wiktoria poprosiła go o 1000 foryntów."
    w "Co?"
    "Widać, że nawet Wiktoria, która od wielu lat tu mieszka, nie chce z nim rozmawiać."
    wp "Mamy nowego mieszkańca Bratgren i chcę mu wszystko pokazać."
    wp "Czy możemy wejść?"
    w "Mamy świeżą krew..."
    w "Trzeba było tak od razu mówić!"
    you "{i}Czy on jest głupi? Przecież od razu powiedziała..{/i}"
    w "W takim razie zapraszam..."
    you "{i}Syczy niektóre słowa tak, że teraz bardziej wygląda na węża niż na to, czymkolwiek on jest.{/i}"
    stop music
    scene bg churchinside with dissolve
    play sound "sfx_door_open.mp3"
    play music "church_normal.mp3" fadein 1.0
    show wieslaw normal at offscreenleft
    "Ostrożnie wchodzicie do środka..."
    show wieslaw normal at leftish with move
    show wp normal at rightish with dissolve
    w "Czy mogę zaoferować Ci {i}specjalną{/i} wycieczkę po kościele?"
    you "Yyy..."
    "Patrzy się na ciebie z uśmiechem jak w reklamie nieruchomości, tylko ten uśmiech jest taki creepy."
    you "Nie, dzięki."
    you "Wiktoria miała mi pokazać wszystko."
    w "Ale czy ty jej ufasz? Nikt nie opowie ci o historii tego miasta lepiej ode mnie."
    you "Tak!"
    w "No, dobra..."
    w "W takim razie nie będę przeszkadzał..."
    show wieslaw normal at offscreenleft with move
    "Wiesław, na szczęście, zostawia was, a potem znika w przypadkowym pokoju niedaleko ołtarza."
    # PROSZĘ TO TAK ZOSTAWIĆ!!
    # ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
    you "(szeptem) Czemu on jest taki dziwny?" # ❌❌❌❌do not touch❌❌❌❌❌
    you "(szeptem) Nie mówiłaś mi o tym." # ❌❌❌❌do not touch❌❌❌❌❌
    wp "(też szeptem) No dobra już..." # ❌❌❌❌do not touch❌❌❌❌❌
    wp "(szeptem) Chodź ale bądź cicho." # ❌❌❌❌do not touch❌❌❌❌❌
    you "(dalej szeptem) Gdzie mam iść?" # ❌❌❌❌do not touch❌❌❌❌❌
    wp "(chyba nie muszę tu nic więcej pisać) Tu." # ❌❌❌❌do not touch❌❌❌❌❌
    you "(Domyśl się) Ok..." # ❌❌❌❌do not touch❌❌❌❌❌
    # ⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆️⬆
    # okej dobra
    "Trudno opisać, jak wygląda wnętrze tego kościoła, więc możesz spojrzeć na tło." 
    "Bogactwo, piękno, kunszt wykonania ― jest tu wszystko, wszędzie, wszystko naraz."
    "Zaczynasz od kolumn, z których wszystkie były pokryte obrazami, każdy osadzony w złotej ramie z misternymi wzorami."
    "Ten kościół był prawdopodobnie tak stary jak ta cegła w piekarni Rafała." 
    "Tylko, że tu ktoś sprząta, dba o ten kościół."
    "Na obrazach była przedstawiona Björk i każdy etap jej życia."
    "Najpierw była jej podróż, potem jak zakładała to miasto, a na końcu jej śmierć."
    "Patrzysz w górę na sufit i widzisz ogromny obraz Björk budującej miasto."
    "Wiktoria zauważa, że stoisz w szoku."
    "Ale kiedy ona też się zatrzymuje, słyszysz, jak cicho jest w tym budynku."
    "Jest tak cicho, że aż robi się strasznie."
    "Na końcu kościoła widzisz ogromną złotą skrzynię ze sztyletem w środku."
    "Przechodzisz obok Wiktorii i podchodzisz bliżej do skrzynii."
    scene bg churchknife with dissolve
    show wp normal at right with dissolve
    play sound "sfx_footsteps_a.mp3"
    you "Co to jest?"
    wp "To jest ten nóż, którym zabito Bjork."
    if receivedLoreAboutChurchOnTheFirstDay == False:
        wp "Ogólnie to Bjork nie budowała tego miasta sama, bo jej pomagała Sabrina Carpenter"
        wp "To była najlepsza przyjaciółka Bjork i też jakby ironicznie cieśla."
        wp "Zbudowały kilka domów i ludzie zaczęli się pojawiać, tak jak ty."
        wp "Do dziś nie wiadomo skąd ci ludzie się biorą."
        you "Nawet Bjork nie wiedziała?"
        wp "Nawet Bjork."
        wp "Jej śmierć była BARDZO tragiczna."
        wp "Była prezydentem tylko 23 lata, kiedy sabrina ją zdradziła i dźgnęła nożem."   
        wp "Zginęła w aktualnym biurze kurowskiej. Dokładnie tam, gdzie ona teraz siedzi."
        wp "To był tragiczny dzień dla całego miasta."
        wp "No i to jest ten nóż."
    you "..."
    "Patrzysz na nóż i twoja inteligentna głowa od razu zauważa, że coś jest nie tak."
    "Nie chodzi o rękojeść ani sposób wykonania."
    "Nie było to oczywiste, ale to zauważyłeś."
    wp "Co?"
    you "Czy to na pewno jest ten nóż, którym zabito Bjork?"
    you "Tak, na 100%%?"
    show wieslaw normal at offscreenleft
    you "Jesteś tego pewna?"
    show wieslaw normal at leftish with move
    with vpunch
    w "Czy chcesz powiedzieć, że ta cała historia, włącznie z tym sztyletem jest kłamstwem?"
    "Wiesław pojawia się za tobą, gdy patrzyłeś na nóż." 
    "Żaden z was go nie zauważył, bo chodził bardzo cicho."
    you "Ja...{w=.3} Yyy..."
    w "To...{w=.6} To, co właśnie powiedziałeś, można porównać do plucia wszystkim w twarz!!!"
    you "Ale ja nie...{w=.3} Ale..."
    w "Proszę wyjść!!!"
    you "Ale..."
    w "NATYCHMIAST!!!"
    "Czujesz, że jeśli teraz nie wyjdziesz, zostaniesz pobity."
    "Widzisz, jak wściekłość narasta w oczach Wiesława z każdą sekundą." 
    "Więc wychodzisz."
    scene bg churchdaya with dissolve
    play sound "sfx_footsteps_a.mp3"
    stop music fadeout 0.5
    wp "Co to ma być??"
    you "No rel, on jest taki niemiły dla mnie."
    wp "Nie! Mówię o tobie." 
    wp "To była twoja jedyna szansa, żeby dowiedzieć się czegoś o tym mieście, a ty ją zmarnowałeś."
    wp "Nigdy nie wpuści tam ciebie i twojej nieufnej dupy."
    "Dramatycznie odwracasz głowę i udajesz, że stoisz z melancholią przed oknem, żeby pomyśleć o swoim następnym kroku."
    "Ze wszystkich znanych ci osób, których imiona zaczynają się na W, najbardziej sus jest Wiesław." 
    "On traktuje tę religię zbyt poważnie."
    you "Nie musi mnie wpuszczać."
    "Otwierasz drzwi, które Wiesław zapomniał zamknąć, i zaglądasz do środka." 
    "Wiktoria widzi, co robisz i jest w szoku, ale nie krzyczy, nie biegnie do rządu, tylko zostaje."
    wp "Ale co ty robisz..."
    wp "Bez jaj..."
    "Bo ona też jest ciekawa tego miasta." 
    "Ostrożnie wchodzisz do środka."
    scene bg churchinside with dissolve
    play sound "sfx_door_open.mp3"
    play music "church_normal.mp3" fadein 1.0
    "Kiedy Wiesław znów znika w swoim pokoiku, otwierasz drzwi szerzej i gestem ręki wskazujesz Wiktorii, żeby poszła z tobą."
    "Podczas gdy ona stara się jak najciszej je zamknąć, ty już jesteś przed tajemniczym pokojem, do którego Wiesław cały czas wchodzi."
    "Widzisz Wiktorię na drugim końcu korytarza, przykładającą pazur do skroni, pokazując, że oszalałeś i ma ciebie dość."
    "Ty jednak to ignorujesz i realizujesz swój plan."
    "Szybko i cicho chwytasz przypadkowe krzesło i blokujesz drzwi, przez które właśnie przeszedł Wiesław."
    "Potem stwierdzasz, że to za mało i chwytasz pięć kolejnych, tworząc wieżę Eiffla z krzeseł."
    "Następnie gestem ręki wskazujesz Wiktorii, żeby weszła."
    "I ona idzie, kompletnie zszokowana tym, co właśnie zrobiłeś."
    "Wiktoria jest BARDZO bamboozled."
    wp "No ale co ty robisz? Oszalałeś?"
    you "Musiałem to zrobić, okej? To było konieczne."
    wp "Konieczne do czego?"
    you "Nie mogę cię tu zostawić bez pokazania ci tego, co widziałem."
    you "Chodź, spójrz na nóż."
    scene bg churchknife with dissolve
    show wp normal at right with dissolve
    wp "No i co z nim?"
    you "Spójrz na krew." 
    you "Widzisz, jaka jest jasno czerwona?"
    you "Kiedy krew wysycha, robi się brązowa z powodu zawartego w niej żelaza." 
    you "Ta krew, jeśli w ogóle można ją tak nazwać, nadal jest czerwona, po 400 latach."
    "Twarz Wiktorii zmienia się z \"jesteś szalony\" w \"jednak masz rację.\""
    wp "No...{w=.6} No no no masz rację."
    wp "Że nikt tego nie zauważył wcześniej?"
    you "Ten nóż jest podróbką."
    wp "No dobra, i co teraz?" 
    wp "Prawdziwy nóż może być gdzieś ukryty, a to może być po prostu kopia dla zwykłych ludzi."
    wp "Wiesz o co mi chodzi?" 
    wp "Tę kopię łatwo ukraść. Jestem pewna, że prawdziwy nóż jest chroniony, a nie tak jak tu ― na widoku"
    wp "Każdy tu może przyjść i wyjąć ten nóż."
    you "To akurat prawda, ale..."
    you "{cps=10}Możesz nie rozumieć tego jeszcze, ale chodzi mi o coś innego. Ja-{/cps}{nw}"
    stop music
    play sound "door_knock_aggressive.mp3"
    "Słyszysz przekręcenie klamki i widzisz, że Wiesław próbuje wyjść."
    play music "outfoxingthefox.mp3"
    wp "On może wyjść przez okno. Musimy uciekać."
    show wp normal at offscreenleft with move
    "Wybiegasz z kościoła jak najszybciej, całkowicie ignorując konieczność zachowania ciszy i biegniesz do piekarni."
    jump ch02_afterChurchEscape

label ch02_afterChurchEscape:
    scene bg churchdaya with dissolve
    scene bg lanastreetday with dissolve
    scene bg bakeryfrontday with dissolve
    scene bg bakeryinside with dissolve
    show wp normal at leftish
    show rafal normal at rightish
    "Wbiegasz do piekarni i na szczęście nikogo tam nie ma."
    play music "bakery.mp3"
    wp "Rafał, zamknij drzwi.{w=.3} Natychmiast!!!"
    r "Dlaczego?"
    wp "Zamknij je.{w=.3} Natychmiast."
    "Rafał pośpiesznie bierze klucze i zamyka drzwi, po czym wypatruje na zewnątrz potencjalnego zagrożenia." 
    "Wiktoria opuszcza rolety, a jej ręce drżą."
    r "Czy powie mi ktoś, co się dzieje?"
    wp "Byłam w kościele z [name]."
    wp "A ten IDIOTA musiał zacząć się drzeć na cały kościół."
    wp "Bo ten nóż niby nie jest prawdziwy i masakra."
    you "Ale on nie jest prawdziwy!"
    r "Po czym to poznałeś?"
    you "No bo krew po 400 latach jest dalej czerwona a powinna być brązowa."
    wp "Ja nie skończyłam opowiadać."
    wp "[name] zamnkął Wiesława w swoim goon cornerze."
    wp "Wiesz gdzie to jest?"
    r "Zartujesz."
    you "Nie-e"
    "Uśmiechasz się jak pick me."
    r "W sumie należało mu się. Irytuje mnie."
    wp "No rel ale i tak to jest szalone."
    you "..."
    r "..."
    wp "Miałeś chyba coś opowiadać, [name]???"
    you "Aha, no tak."
    you "Pamiętasz jak wczoraj widziałem Bjork?"
    wp "No."
    you "Ona rzeczywiście tam była, tylko uciekła."
    you "Powiedziała mi jakiś wiersz."
    you "{i}Underneath our feet{/i}"
    you "{i}Crystals grow like plants{/i}"
    you "{i}Listen how they grow{/i}"
    you "Ale to już nieważne, bo jej druga wypowiedź jest ciekawsza."
    you "Bo jak już biegłem do was, ona zaczęła mówić \"Nie ufaj w...\""
    you "I byłem święcie przekonany, że to tobie nie mogę ufać, bo wtedy tylko twoje imię było na w..."
    you "Ale to chyba Wiesławowi nie mogę ufać."
    wp "Aha..."
    r "Ale czemu ona akurat do ciebie przyszła?"
    you "Nie wiem...{w=.3} Chyba mam jakiś plot armor."
    wp "..."
    you "Myślałem, że będziesz na mnie zła..."
    wp "Gdybym była tobą, to bym to samo zrobiła."
    r "Mam pomysł!"
    r "O której Wiesław wychodzi z tego kościoła?"
    you "W pół do komina!{w=1} Nie no o 19:00."
    r "Możemy się włamać do tego kościoła."
    you "O tak!"
    wp "Jesteście durni..."
    r "Nie."
    you "To jest świetny pomysł!"
    you "Nikt nas nie przyłapie na tym i będzie git."
    wp "Ten pomysł to jest najgłupszy pomysł kropka."
    r "No ale jak ty chcesz dowiedzieć się czegoś nowego?"
    r "Nie możemy z tym pójść do Kurowskiej."
    r "Co jeśli ona maczała w tym palce?"
    wp "Masz rację..."
    you "..."
    you "Która jest godzina?"
    r "YYyy.... 12:00, a co?"
    you "No to trzeba się przygotować jeśli rzeczywiście chcemy tam się włamać."
    you "Mamy 7 godzin."
    you "Czekaj, jak my otworzymy drzwi?"
    you "Wiktoria może otworzyć bramę. Ale co z drzwiami?"
    r "Chodzę na pilates..."
    you "No i co w związku z tym?"
    r "Mam tak wielką dupę, że mogę na nią skoczyć i zrobić trzęsienie ziemi."
    r "Tym otworzymy drzwi."
    "Jest ci ciężko w to uwierzyć, ale Rafał jest tak pewny swojego pomysłu, że to powinno się udać."
    r "Pewnie mi nie wierzysz."
    r "Watch and learn!"
    window hide 
    show rafal normal:
        easeout 1.0 yoffset -500
        easeout_cubic 5.0 rotate 7200
        easein 0.15 yoffset 20
    pause 6.15
    with vpunch 
    with vpunch 
    with vpunch 
    with vpunch
    with vpunch 
    with vpunch 

    window show
    you "Ok."
    wp "Ok."
    wp "To w takim razie co robimy?"
    you "Możemy iść do biblioteki."
    r "A potem co? Mamy 7 godzin."
    you "Sybau coś wymyślimy."
    you "To na co czekamy?"
    r "W pół do komina."
    you "No ale chodź no."
    "Rafał otwiera drzwi i wszyscy wychodzą z piekarni, a po zamknięciu drzwi idziecie do biblioteki."
    you "{i}Dobrze, że to miasto nie jest duże.{/i}"
    you "{i}Wszystko jest bardzo blisko.{/i}"
    "Wszystko w tym mieście rzeczywiście jest blisko."
    "Nie mnie to oceniać, czy to przez to, że miasto jest naprawdę małe, czy przez to, że wszystko jest na rynku."
    "Znasz osoby, które nie są w stanie przejść trzech kilometrów."

    jump ch02_GoingToTheLibrary

label ch02_GoingToTheLibrary:
    "Na pierwszy rzut oka budynek przed tobą nie wygląda na bibliotekę." 
    "Jedyne, co go zdradza, to napis \"biblioteka publiczna\" na drzwiach."
    you "Nigdy tu nie byłem..."
    r "No co ty nie powiesz!"
    you "DOBRA CICHO BĄDŹ!"
    you "Lets go girls."
    "Wywróciłeś się na schodach, więc teraz boli cię stopa."
    "Okazuje się, że ta biblioteka jest troszeczkę większa, niż się wydawało z zewnątrz."
    you "Dzień dobry!"
    m "Dzień dobry."
    you "Nazywam się [name] i mieszkam tu od 2 dni. Szukam informacji o tym mieście."
    b "Ja mam na imię Bartosz, a książki o Bratgrenie, których potrzebujesz, znajdują się na półce nr 67."
    "Odwracasz się do Rafała i Wiktorii, i mówisz do nich, zdruzgotany."
    you "Gdzie są te książki?"
    wp "Ale skąd ja mam wiedzieć, ja tu nigdy nie byłam."
    r "To się zapytaj?"
    "Odwracasz się do Bartosza i uśmiechasz się jak 9/10 dentystów w reklamie pasty do zębów."
    "Nie musisz nawet zadawać pytania, ponieważ biblioteka jest tak mała, że Bartosz wszystko słyszał."
    b "Te książki są tam, w tym rogu."
    you "Dziękuję. Niech los wynagrodzi ci ten czyn tysiąckrotnie."
    you "Ale dużo tu tych książek o Bratgrenie."
    r "No..."
    r "Jak na taką małą bibliotekę to dużo tu jest."
    you "Patrzcie. Tu nawet jest coś dla dzieci."
    "Wyciągasz \"Na straganie\""
    menu:
        "CZYTAMY":
            you "Ale czekaj czy ty widziałeś tu jakieś dzieci"
            r "No tak, są przecież"
            you "Aha bo nie widziałem"
            "Otwierasz tę książkę na strone 17"
            "{i}Burak stroni od cebuli,{/i}"
            "{i}A cebula doń się czuli:{/i}"
            "{i}Mój Buraku, mój czerwony,{/i}"
            "{i}Czybyś nie chciał takiej żony?{/i}"
            "{i}Burak tylko nos zatyka:{/i}"
            "{i}Niech no pani prędzej zmyka,{/i}"
            "{i}Ja chcę żonę mieć buraczą,{/i}"
            "{i}Bo przy pani wszyscy płaczą.{/i}"
            "{i}A to feler -{/i}"
            "{i}Westchnął seler.{/i}"
            wp "Co ty czytasz"
            wp "Nic tu nie znajdziesz"
            you "Ale skąd ty wiesz, że tu nie ma żadnych sekretów"
            wp "Spędzimy cały dzień w tej bibliotece jeśli będziemy wszystko po kolei czytać"
            "Odkładasz tę książkę z powrotem bo nie chcesz tego dalej czytać"
            you "No to co mam czytać??"

        "Nie":
            "Ale jesteś nudny"
    wp "hmmm..."
    wp "Weź to"
    "Wiktoria daje ci \"Atlas Zwierząt Miasta Bratgren\""
    you "żeś dała do pieca"
    wp "67"
    you "Ok"
    "Otwierasz tĘ książkę na stronie 67 i prawie mdlejesz ze strachu"
    "Ten atlas spada na podłogę"
    you "CO TO JEST??"
    wp "A to jest Ceplus Pluss"
    wp "Chodzi po tym lesie i może cię zjeść"
    you "To się da zabić??"
    wp "Nie"
    wp "Ale czarodzieje tacy jak Piotr chronią nasze miasto przed takimi potworami"
    you "Niech on żyje długo"
    you "W sensie Piotr a nie to... coś"
    "Odkładasz ten atlas bo nie chcesz wiedzieć o innych potworach z Bratgren"
    you "Ja już mam tego dość"
    "Patrzysz się w górę i widzisz jak wysokie są te półki"
    "Gapisz się na ilość informacji w tym pomieszczeniu aż zauważasz to, czego potrzebowałeś"
    "Ta książka jest igłą w stogu siana"
    you "Patrzcie"
    you "Kataster nieruchomości Bratgren"
    you "Tam jest informacja o działkach"
    you "Może tam będzie coś o tym kościele?"
    you "Tylko trzeba się wspinać po tych półkach"
    you "Kto chce"
    menu:
        "Rafał dawaj właź tam":
            show rafal normal at center:
                linear 5.0 yoffset -1500
                easein 0.15 yoffset 20
            pause 5.15
            scene black 
            "Rafał próbuje wyjąć książkę, ale niestety upada na dupę." 
            "Jego dupa jest tak wielka, że rozbija płytę tektoniczną, na której leży Bratgren, wywołując falę uderzeniową, która zabija wszystkich."
            "No i oczywiście niszczy bibliotekę"
            "Game over"
            "Trzeba było coś innego wybrać a nie"
            jump gameEndCreditsScene
        
        "Dobra niech wam będzie zrobię to":
            "Włazisz na tą półkę i wracasz na dół z bardzo ciężką książką"
    you "Nie odkładam tej książki"
    you "Nie ma szans..."
    "Kładziesz kataster na stół"
    r "Let's see!"
    "Otwierasz tę naprawdę ciężką książkę i szybko ją przeglądacie." 
    "Pierwsza strona zawiera spis treści, który, jak się okazuje, był zupełnie bezużyteczny, ponieważ ujawnił jedynie, że właściwe dane zaczynają się na następnej stronie."
    "Przewracasz stronę, aby zobaczyć pierwszą nieruchomość."
    "Pierwsza nieruchomość, którą widzisz, to pierwszy dom, jaki kiedykolwiek zbudowano w Bratgren." 
    "Książka zawiera kilka faktów na temat tego domu, mówiąc, że była to mała, uboga chata Björk."
    "Skupiasz się na kościele, więc szybko przewracasz strony, próbując go znaleźć."
    "Przewracasz dziesięć, potem dwadzieścia, potem sześćdziesiąt, ale nadal go nie ma."
    "Dom, który teraz oglądasz, został zbudowany po śmierci Björk, a ty nadal nie znalazłeś tego cholernego kościoła." 
    "Przeskakujesz obok domu, w którym znajduje się piekarnia Rafała i w końcu widzisz kościół."
    "Strona nie wymienia niczego nietypowego na pierwszy rzut oka."
    "Patrzysz na plan ewakuacyjny i wszystko się zgadza, potem przechodzisz do szczegółów i sprawy robią się dziwne."
    "Właściciel nieruchomości jest skreślony, co jest oczywiście dziwne."
    "Potem patrzysz w dół i widzisz:"
    "{i}Parter - 1100 metrów kwadratowych{/i}"
    "{i}Piwnica - 152 441 metrów kwadratowych{/i}"
    you "Ej wy to też widzicie?"
    you "Czemu piwnica ma 152 tysięcy metrów kwadratowych"
    r "Co ty gadasz"
    you "No tu pisze"
    "Wskazujesz pazurem na tę dużą, chaotyczną, losową a nawet parzystą liczbę"
    r "Rzecywiście"
    you "To nie jest błąd jakiś??"
    wp "Ja bym zapytała Bartosza. On na pewno będzie wiedział"
    "Podnosisz książkę z Rafałem."
    "Tak, jest tak ciężka, że musicie ją nieść razem."
    you "Mamy kwerendę"
    b "Słucham?"
    "Kładziecie kataster na stole za Bartoszem a kurz na tym stole odlatuje do ciepłych krajów"
    "Z tego powodu kichasz"
    b "Sto lat"
    r "Niech żyje żyje nam"
    you "Ale ja nie mam urodzin dzisiaj ja tylko kichałem"
    r "Aha"
    b "No to co tam chcecie ode mnie"
    you "No bo patrz.."
    you "Szukaliśmy informacji o kościele i własnie"
    you "Jakieś szemrane akcje są"
    you "Bo tu pisze, że parter ma 1100 metrów kwadratowych"
    you "A piwnica ma 150 tysięcy"
    you "To na pewno nie jest jakiś błąd?"
    "Bartosz patrzy się i widać, że jest w lekkim szoku"
    b "No nie to raczej nie jest błąd"
    b "Dziwne to"
    you "No właśnie wiemy"
    "Bartosz patrzy się na tę stronę jeszcze raz"
    b "Wiecie co.."
    b "To jest bardzo ciekawe. Nie wiem dużo o tym kościele ALE..."
    b "Obiecuję, że jutro będę coś dla was miał"
    you "Czekaj mam pomysł"
    you "Podnieś to"
    "Rafał i Bartosz biorą książkę i podnoszą ją, a ty bierzesz stronę i patrzysz na nią pod światło, próbując przeczytać nazwisko właściciela." 
    "Jednak atrament jest zbyt gęsty, żeby cokolwiek zobaczyć."
    you "Okej nie widzę nic"
    you "Ale warto było spróbować"
    you "Dobra to masz może więcej książek??"
    you "Mamy trochę czasu to możemy poszukać czegoś"
    b "No to tu wszędzie są książki o tym mieście"
    b "Ale większość jest w tym rogu"
    b "Pokazywałem wam przecież"
    you "Aha okej"
    you "Let's go girls"
    wp "Ty idź tam a ja pójdę gdzieś indziej"
    r "No ja też"
    wp "Jak coś znajdziesz to idź do nas"
    you "Ok..."
    "Wracasz do miejsca, w którym znaleźliście kataster, ale teraz ktoś tam stoi"
    "Widzisz, że ten ktoś czta mangę"
    "Czy chcesz z nim gadać?"
    menu:
        "Tak":
            you "Dzień dobry?"
            m "Dzień dobry."
            $ metPetitty = True
            jump ch02_petittyFirstEncounter
        "Hell nah":
            "Stwierdzasz, że on jest dziwny więc omijasz go szerokim łukiem"
            jump ch02_afterPetitty

label ch02_petittyFirstEncounter:
    menu:
        "Przedstaw się":
            you "Nazywam sie [name] i mieszkam tutaj od 3 dni"
            m "Ok"
            pe "A ja jestem Petitty i ja czytam mangi"
            menu:
                "Wstyd":
                    $ friendship["Petitty"] -= 1
                    "Petitty robi side eye"
                    jump ch02_tooAssertivePetitty
                "Współczuję":
                    $ friendship["Petitty"] -= 1
                    "Petitty robi side eye"
                    jump ch02_tooAssertivePetitty
                "Masakra":
                    $ friendship["Petitty"] -= 1
                    "Petitty robi side eye"
                    jump ch02_tooAssertivePetitty
                "Omg serio?? Ja też :3":
                    pe "Omg serio? Wow"
                    pe "Choziaż..."
                    you "Jakie jest twoje ulubione anime???"
                    pe "..."
                    pe ">.<"
                    pe "Multiple parts!"
                    you "Omg! To jest niesamowite! BO MOJE TEŻ!!"
                    pe "Nie wierzę ci"
                    you "Ale mówię prawdę! Naprawdę kocham to anime!"
                    pe "To odpowiedz dobrze na moje pytania"
                    pe "Tylko tak udowodnisz, że nie nie kłamiesz.."
                    $ correctAnswersPetitty = 0
                    jump ch02_PetittyQuiz
        "\"Przedstaw się\"":
            jump ch02_tooAssertivePetitty
            
label ch02_tooAssertivePetitty:
    $ friendship["Petitty"] -= 1
    you "Przedstaw się."
    "Czujesz się jak alfa"
    "Ale.."
    "Ten ktoś najwidoczniej przestraszył się z powodu twojej asertywności i wybiegł z biblioteki do swojej piwnicy"
    you "???"
    jump ch02_afterPetitty

label ch02_PetittyQuiz:
    pe "Jakiego koloru są włosy loczka"
    menu:
        "koloru kiwi":
            $ correctAnswersPetitty -= 1
        "czerwone":
            $ correctAnswersPetitty -= 1
        "kości słoniowej":
            $ correctAnswersPetitty -= 1
        "różowo-fioletowe":
            $ correctAnswersPetitty += 1

    pe "Okej..."
    pe "Jak nazywa się ostatnia wyspa, na której znajduje się skarb?"
    menu:
        "Lodestar":
            $ correctAnswersPetitty += 1
        "God Valley":
            $ correctAnswersPetitty -= 1
        "Laugh Tale":
            $ correctAnswersPetitty -= 1
        "Genshin Impact":
            "Heh... {i}nie{/i}"
            $ correctAnswersPetitty -= 1

    pe "Hmm.."
    pe "Jak nazywają się bracia Lampardiego?"
    menu:
        "Lena i Katarzyna":
            "Stary nie ugotowałeś"
            $ correctAnswersPetitty -= 1
        "Ace i Sabo":
            $ correctAnswersPetitty += 1
        "Zoro i Sabrina":
            $ correctAnswersPetitty -= 1
        "Nami i Chopper":
            $ correctAnswersPetitty -= 1

    pe "Ostatnie pytanie.."
    pe "W jaki sposób Ivashkiv uleczył Lampardi'ego przed walką na Marinefield?"
    menu:
        "Zawiózł go do szpitala":
            $ correctAnswersPetitty -= 1
        "Naszpikował go hormonami":
            $ correctAnswersPetitty += 1
        "Dał mu 3 nerki tak na wszelki wypadek":
            $ correctAnswersPetitty -= 1
        "Nie leczył go":
            $ correctAnswersPetitty -= 1
        "Brak danych":
            $ correctAnswersPetitty -= 1
        "Nie powiem":
            $ correctAnswersPetitty -= 1

    if correctAnswersPetitty == 4:
        pe "Nie mogę w to uwierzyć!"
        pe "Naprawdę znasz to anime!"
        pe "Chcesz być besties???"
        you "..."
        you "OCZYWIŚCIE!!!"
        pe "AAAAA :3"
        "Petitty ucieka do swojej piwnicy,{w=0.5} bo znalazł przyjaciela{w=0.5}(swojego pierwszego)"
        $ friendship["Petitty"] += 1
    else:
        pe "Wow, wiedziałem, że kłamiesz."
        pe "Ty fejku jeden, myślałem że w końcu ktoś zmatchuje mój freak"
        $ friendship["Petitty"] -= 1
        "Petitty ucieka do swojej piwnicy"
    jump ch02_afterPetitty

label ch02_afterPetitty:
    "..."
    you "{i}Są rzeczy ważne i ważniejsze{/i}"
    you "{i}W końcu przyszedłem tutaj bo chcę rozwiązać zagadkę, którą jest to miasto{/i}"
    "Spoglądasz na półkę, z której wziąłeś kataster." 
    "Nadal jest pusta."
    "Bartosz prawdopodobnie nie zadał sobie trudu, żeby go tam odłożyć, bo prowadził własne śledztwo."
    "To cię trochę uspokaja, bo wiesz, że nie jesteś szalony, a teraz cztery osoby w tym mieście badają kościół."
    "Rozumiesz jednak, że nie możesz pozwolić Wiesławowi wiedzieć, że jest obserwowany."
    "Patrzysz się trochej niżej i widzisz dużą księgę zatytułowaną \"Wykaz rozpraw sądowych\"."
    "Ostrożnie ją podnosisz, starając się jej nie uszkodzić i otwierasz."
    "Ta księga, podobnie jak kataster, miała zupełnie bezużyteczny spis treści."
    "Ta księga była po prostu listą wszystkich postępowań sądowych w tym mieście."
    "Przeszukujesz ją, próbując znaleźć cokolwiek interesującego o Wiesławie."
    "Jest tam wiele zabawnych wpisów, z których większość dotyczyła drobnych roszczeń, takich jak kradzież czegoś czy niepłacenie czynszu."
    "Ciebie jednak one nie interesują, bo jesteś skupiony na Wiesławie."
    "Zanim się obejrzysz, docierasz do końca książki i nic więcej o nim nie znalazłeś."
    you "{i}Kim ty jesteś, Wiesławie?{/i}"
    "Odkładasz książkę na miejsce i idziesz do Wiktorii, żeby opowiedzieć jej o swoich odkryciach"
    "Ona także siedzi w kącie, choć w innym, i czyta książkę."
    you "Gdzie jest Rafał?"
    wp "Poszedł szukać książek"
    wp "Znalazłeś coś?"
    you "Właśnie miałem mówić"
    you "Znalazłem."
    you "Znalazłem listę rozpraw sądowych i nic tam o Wiesławie nie było"
    you "Tak dosłownie nic"
    wp "A to dziwne"
    you "A ty coś masz?"
    wp "Mam"
    wp "Patrz tu."
    wp "Znalazłam wykaz pozwoleń na budowę"
    wp "I patrz co tu jest"
    wp "Teraz właścielem jest Wiesław."
    wp "ALE.. widzisz, że poprzedni właściciel jest skreślony?"
    you "No"
    wp "No ja sobie zrobiłam to co ty"
    you "I co?"
    wp "I dupa nic nie było"
    you "aha"
    you "To może chodźmy do Kurowskiej??"
    wp "Jesteś głupi??"
    wp "Żeby coś w tym mieście wybudować trzeba się pytać o pozwolenie"
    wp "Czyli ona na pewno wie o tej dużej piwnicy"
    you "No dobra ale ona może wtedy nie była prezydentem miasta"
    you "Kto był prezydentem wtedy"
    wp "Masz rację"
    wp "Prezydentem była taka ciociobabcia"
    you "No właśnie"
    wp "Ale i tak nie możemy do niej iść z tym"
    you "Czemu"
    wp "Czy ty myślisz, że ona nie wie, że coś jest nie tak?"
    wp "Przecież tyle lat tu mieszka"
    wp "Ona zna wszystkie sekrety Bratgren"
    wp "No i nic z tym nie robi."
    you "..."
    "Nagle wraca Rafał"
    you "A ty co? Znalazłeś coś?"
    r "Tak."
    r "Znalazłem zegar i teraz wiem, że musimy iść"
    r "Bartosz będzie zamykał bibliotekę za chwilkę, więc musimy wyjść"
    "Żegnasz się z Bartoszem przed wyjściem z biblioteki"
    jump ch02_leavingLibrary

label ch02_leavingLibrary:
    you "Rafaaał"
    r "Co"
    you "Która jest godzina?"
    r "18:53"
    you "No to chodźmy do twojej piekarni bo stąd widać kościół"
    you "Będzie widać kiedy Wiesław wyjdzie"
    scene bg bakeryinside with dissolve
    "Rafał zamyka żaluzje, a następnie otwiera je na tyle, by móc zobaczyć, co dzieje się na zewnątrz" 
    $ bakeryMetPeopleSum = metVasili + metPetitty
    if metVasili:
        with vpunch
        with vpunch
        with vpunch
        "Widizisz Vasiliego próbującego iść cicho ale każdy jego krok powoduje trzęsienie ziemi"   
        with vpunch
        you "Co on tu robi"
        wp "Znasz go?"
        you "Tak"
        if endorsedCommunism:
            you "Jest całkiem fajny"
        else:
            wp "Współczuję"
        "..."
    if metPetitty:
        "['Następnie widzisz' if bakeryMetPeopleSum > 1 else "Widzisz"] Petittiego przy drziwach do piekarni"
        you "A co on tu robi??"
        you "Może on nas nie widział?"
        "Petitty puka do drzwi"
        r "Jezu co znowu"
        "Rafał otwiera drzwi, a petitty stoi przy wejści z puppy eyes"
        you "Co"
        pe "Widziałem, że tu poszedłeś..."
        pe "J-ja chcę porozmawiać...."
        menu:
            "Nie bo jestem zajęty nie przeszkadzaj":
                $ friendship["Petitty"] -= 1
                with vpunch
                pe "TO SĄ WYMÓWKI!!"
                you "Nie drzyj się"
                pe "JESTEŚ TAKI NIEMIŁY"
                "Zamykasz drzwi."
                "Wciąż słychać jego stłumiony krzyk za zamkniętymi drzwiami."
                "Chwilę mu zajmuje, zanim się uspokoi, a potem wraca do swojej piwnicy."
            "Innym razem, obiecuję":
                $ friendship["Petitty"] += 1
                pe "A dlaczego nie teraz?"
                you "..."
                you "{i}Tzeba wymyślić wymówkę...{/i}"
                you "Jestem na randce"
                pe "O mój boże! Znowu zamnkęli przedsionek!"
                pe "To w takim razie nie będę ci przeszkadzał{w=1}, hihi."
                "Petitty robi piruet i ucieka do swojej jaskini"
    if bakeryMetPeopleSum == 0:
        you "Dziwne to jest"
        r "Co"
        you "Że jest tak pusto na ulicach"
        r "..."
    
    wp "Cicho"
    r "Co"
    wp "Ale zamknij się"
    you "Czemu jesteś taka niemiła? Tłumacz się"
    wp "Wiesław wyszedł z kośioła"
    "Wsuwasz pazury między żaluzje, ponieważ nic nie widzisz"
    "Rzeczywiście, Wiesław wyszedł z kościoła, i tak jak wczoraj, zamknął bramę i poszedł w tym samym kierunku"
    r "Chodź"
    "Rafał zaczyna otwierać drzwi ale zatrzymujesz go"
    you "Poczekaj bo może wróci zaraz"
    "Stoicie przy drzwiach w ciszy.{w=0.5}.{w=0.5}.{w=0.5}"
    "Ale Wiesław nie wrócił"
    you "Dobra chyba możemy iść"
    "Wychodzicie, starając się przy tym nie robić hałasu"
    