default playerRobbed = False
default workedAtVasili = False
default workedAtFilip = False
default robberyStopped = False
default metPetitty = False
default gotCoffeeForPiotr = False
default gotCakeForPiotr = False
default gotBreadForPiotr = False
default piotrFoodPoints = 0
default piotrWritingPoints = 0


label ch02_watch_your_mouth:
    "Jesteś bardzo głodny, ale nie aż tak, żeby przez to nie iść spać."
    "I zanim się obejrzysz, już śpisz."

    call chapterTransition("Akt 2", "lorem ipsum")

    ".{w=0.5}.{w=0.5}.{w=0.5}"
    "The sun lined up perfectly with your face, which, in turn, warmed it up just enough to wake you up"
    scene bg houseday with dissolve
    "You instinctively cover the face but you can still see the sun through the gaps between your fingers"
    "It's time to stop being so lazy and get off the bed"
    "Now that it's not dark anymore you can see the interior of the house better"
    "The house didnt chage much, except for the fact that the morning light is making it feel more abandoned"
    "You lazily get off your bed and change your clothes"
    "It's still you in the mirror, just not smelly and covered in forest dirt"
    "When you walk past the clock you notice the time and stop for a moment"
    you "{i}There's no way i slept for 10 hours{/i}"
    you "{i}Kurowska is going to think i am lazy{/i}"
    you "{i}Hell. No.{/i}"
    $ time.setTime(10,32)
    show screen s_Clock()
    "Hunger definitely contributed to waking you up from your slumber"
    if ch01_f_triedBakery:
        "The only thing you can think of are the pastries you saw at a bakery"
    else:
        "The only thing you can think of is (favorite food) and all its flavors"
    "Luckily, there is a fridge"
    you "{i}Okay what kind of house would this be if i didnt get food{/i}"
    you "{i}That would be very rude{/i}"
    you "{i}I got a whole house here why wouldnt this have food?{/i}"
    you "{i}Oh my god what if its magical and can make any food i think of{/i}"
    "You close your eyes and try to summon..."
    menu:
        "Kawior":
            "This food is going to require the most concentration"
            "You close your eyes and think of caviar and try your best to channel your inner sorcerer..."
            you "{i}This HAS to work{/i}"
        "Winniczki":
            "This food is going to require the least concentration"
            "You close your eyes and think of those slimy things and try your best to channel your inner sorcerer..."
            you "{i}This HAS to work{/i}"
        "Dead dove":
            "This food is going to require some concentration"
            "You close your eyes and think of dead doves and try your best to channel your inner sorcerer..."
            "Suddenly you remember that you shouldn't eat dead doves"
            you "{i}I need to dream bigger. I want a rotisserie chicken.{/i}"
        "Nie chcę jeść":
            "Actually, you dont have to concentrate at all"
            you "{i}Actually no if i stay hungry i will stay skinny{/i}"
            you "{i}Po takiej diecie mój snatched waist będzie potężny, może tylko się czegoś napiję.{/i}"

    "Otwierasz lodówkę i ku twojemu zdziwieniu nie ma w tej lodówce nic poza krasnalem, który włącza i wyłącza w niej swiatło."
    you "{i}What the hell{/i}"
    you "Hello?"
    you "Who are you?"
    "The little gnome ignores you"
    you "sprechen sie deutsch???"
    "While he's ignoring you, you ignore the fact that he could be deaf"
    you "Excuse me young man what are you doing in my fridge?"
    "He looks up at you with a gnarly smile and waves his hand"
    you "{i}I'm not getting paid enough for this{/i}"
    you "{i}In fact i dont get paid at all{/i}"
    "You leave the door open just in case he was trapped in there and wants to get out only for him to start dusting the top shelf"
    you "{i}???{/i}"
    "Due to pure confusion you close the fridge door"
    you "{i}If i wont look at it it will go away{/i}"
    you "{i}Wait what if he's hungry{/i}"
    you "{i}I'll get food and share{/i}"
    "The gnome was only a brief distraction from the calories in your stomach, or lack thereof"
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
    "Ulice teraz tętnią życiem, każdy spieszy się do pracy."
    "Gdy podchodzisz do urzędu, on znowu robi na tobie wrażenie, nie tak wielkie jak wczoraj, ale dalej jest bardzo imponujący."
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
    you "Okay this is actually really awkward"
    you "I havent eaten anything since yesterday"
    you "Do you have literally any food here i'm hungrier than a shein worker"
    show filip normal
    f "Tak. Codziennie przynoszę Kurowskiej ciepłe buły Rafała z kawą."
    you "Czy mógłbyś mi dać jedną? Nie mam żadnych pięniędzy, więc nie mogę kupić jedzenia"
    you "Dosłownie zaraz umrę jeśli nic nie zjem!!!"
    f "Sure. I have some stale ones i was too lazy to throw out. Is that okay?"
    you "YES"
    f "Okay"
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
    if "rudeToKurowska" not in flags:
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
    k "Because there's alot of them"
    k "I was supposed to give this to Filip to use as change for people but then he raised the prices"
    k "And now i do not need this"
    k "Trzymałam je w biurze cały miesiąc i chciałam się ich pozbyć więc to jest win-win situation."
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
        "Uśmiechnij się":
            m "Po co"
            you "Lubię żółty"
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
            hide kamil with dissolve
            "Złodziej zaczyna płakać i ucieka."
    play music "town_day.mp3"
    you "{i}To nie mój problem.{/i}"
    you "{i}Przez tego idiotę teraz muszę wrócić do Kurowskiej i zapytać co robić...{/i}"
    you "{i}Trochę się boję co może ona zrobić, ale no cóż, nic innego nie mogę wymyślić.{/i}"
    scene bg secretary with dissolve
    play sound "sfx_footsteps_a.mp3"
    "After being robbed there is no other choice but to go back to Kurowska"
    "Even if she doesn't have any more money for you, it would be wise to report this"
    "When you enter the city hall, filip is not there, which is confirmed by a cacophony of noises coming from the storage room"
    "With no other choice, you knock on Kurowska's door"
    "..."
    you "Dzień dobry! To znowu ja."
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
    k "Znajdź. Pracę."
    hide kurowska normal with dissolve
    jump ch02_goingToFindAJob

label ch02_goingToFindAJob:
    scene bg citysquareday with dissolve
    play sound "sfx_door_open.mp3"
    "Wychodzisz na zewnątrz, żeby zastanowić się co powinieneś zrobić dalej."
    "Jak powiedziała Kurowska, powinieneś wybrać kogoś kogo znasz i pójść do niego, żeby poprosić o pracę."
    "Stoisz na rynku i rozglądasz się, jakbyś miał całować ziemie, trzymając cyprysowy krzyżyk."
    "Do kogo idziesz pracować?"
    menu:
        "Vasili (to jest ta ciekawsza opcja)" if "metVasili" in flags:
            you "{i}Pójdę do niego tylko dla fabuły.{/i}" 
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
    show filip normal with dissolve
    "This time he is actually doing his job and not lollygagging in the storage room"
    play sound "sfx_door_open.mp3"
    you "A to znowu ja."
    f "Hejka."
    you 'Jeszcze jedno pytanie.'
    f 'Tak?'
    you 'Masz może jakąś robotę dla mnie?'
    you 'Czy jest dosłownie cokolwiek co mogę zrobić?'
    f 'Hmm...'
    f "I {i}do{/i} need to move mail from that storage room to Kurowska but i am wayy too lazy for that"
    you "I can do it"
    f "Then wait here"
    show filip normal at offscreenright with move
    "Filip wstaje i znowu idzie do swojej szafy." 
    "Słychać, że znowu przesuwa ciężkie pudła, ale tym razem trwa to dłużej." 
    you "{i}How big is that storage room what{/i}"
    show filip normal at center with move
    "Filip finally gets out of the suspiciously large storage room while pulling a huge luggage cart full of paper" 
    "Zanim się obejrzysz, przed tobą są już cztery wysokie stosy papieru"
    you "Okay i have two questions"
    you "First of all is what the hell is in that storage room?"
    you 'And what the hell is this'
    f 'A to są po prostu jakieś papiery i poczta, która nigdy nie dotarła do Kurowskiej.'
    f 'Po prostu przez lata zbierałem i uważałem, że nie jest zbyt ważna, więc ją trzymałem.'
    f 'A teraz ona chce to wszystko zobaczyć.'
    you 'No to co mam z tym zrobić??'
    f 'Weź to wszystko i zanieś to do Kurowskiej.'
    you "Cant you just shove the whole luggage cart through the door?"
    f "No because it is too wide"
    you "Oh my god"
    you 'Ale nie dam rady tego unieść ty jesteś zdrowy??'
    f 'Nie mówię ci żebyś niósł wszystko na raz głuptasie.'
    f 'Tu jest z 120kg papieru nie oczekuję że to podniesiesz.'
    f 'Zwłaszcza z twoim snatched waistem...'
    you 'No spoko...\n {i}ZAUWAŻYŁ!!!{/i}'
    "You pick up a stack of paper the size of anna karenina and your spine cracks"
    "Then, with all that paper still in your hand, you take one step and decide against doing a second one"
    "You go back and leave half of your 40cm stack on the luggage cart"
    "Only then your back allows you to move"
    "You knock on Kurowska's door"
    if "rudeToKurowska" not in flags:
        k "KTO TAK PUKA NA BELZEBUBA??"
    else:
        k "Wejdź."
    scene bg office with dissolve
    show kurowska normal at center with dissolve
    "You enter her office and see her knee-deep in documents, like she always is"
    you "{i}Does she really have time to read all this?{/i}"
    you 'Gdzie to zostawić?'
    k 'Na moim stole.'
    you 'Na pewno? Ten papier NIE jest skinny.'
    k 'Dobra zostaw na podłodze.'
    "Zostawiasz pierwszy stosik papierów na podłodze." 
    scene black with dissolve
    "Po chwili zaczyna ci się nudzić, więc czytasz to co przenosisz."
    "Najwidoczniej przenosisz jakieś skargi."
    "Każdy nagłowek jest gorszy od poprzedniego."
    "Pierwsza strona ma tytuł 'Raport o hałaśliwych sąsiadach'."
    if ("metVasili" in flags) or knowsAboutVasili:
        you "{i}Wiadomo, że chodzi o Vasiliego pff..{/i}"
    "Z każdą linijką coraz trudniej powstrzymać śmiech, bo ten raport jest tak absurdalny, że aż nierealny."
    "Nie dziwota że Filip uznał to za nieważne - wygląda jak jakiś fanfik."
    you "{i}\"Krzyczenie 'WYPAROWAĆ BURŻUAZJĘ!!!' podczas mojej pracy było niestosowne.\" {/i}"
    you "{i}KTO TO NAPISAŁ?{/i}"
    "Nosisz dzielnie jeden po drugim, ale część ciebie chce tylko czytać te śmieci."
    "Nagłówki są coraz bardziej dzikie..."
    "{i}'Kapelusz Rafała sieje dramat wśród Bratgrenian.'{/i}"
    "{i}'Skarga na robale z Kolorado atakujące pomidory.'{/i}"
    "{i}'Ktoś mi nasrał przed drzwiami do domu proszę to usunąć.'{/i}"
    scene bg office with dissolve
    show kurowska normal at center with dissolve
    "Zanim się obejrzysz przeniosłeś już wszystko i zabrakło ci nagłówków do czytania."
    you 'Dużo tych mailów...'
    k 'Co? jakich mailów?'
    you 'No tych które noszę od ostatnich 40 minut.'
    k 'MAILE?? prosze mi je wynieść, to praca filipa, ja mam ważniejsze rzeczy na głowie!'
    you 'To po co ja je tyle nosiłem?'
    k "Ty mi powiedz"
    "Bierzesz z rezygnacją kupkę mailów i wracasz do filipa."
    scene bg secretary with dissolve
    show filip normal with dissolve
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
    "(Big Buły Bakery) duhh"
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
    "This leaves you with time to take in the surroundings"
    "From the brick walls to the warm glow of incandescent light bulbs, every piece of the interior was deliberately chosen by the owner"
    "Every little detail, even the posters made the bakery feel premium - a word your wallet is not ready to hear"
    show wp normal at leftish with moveinleft
    show fraucrusty normal at center with moveinleft
    show rafal normal at rightish with moveinright
    "Przed tobą są dwie osoby."
    "Pierwszą w kolejce jest Frau Crusty."
    if "metWiktoriaP" in flags:
        you "O, hej."
        wp "No cześć! Co tam?"
        
        if workedAtFilip:
            you "Masakra... Musiałem pracować..."
            wp "Do kogo poszedłeś?"
            you "Do Filipa."
            you "Kazał mi przenosić dokumenty do Kurowskiej."
            you "A jak już skończyłem, Kurowska kazała mi z powrotem przenieść te listy."
            you "Bo to on ma je czytać."
            wp "Trzeba było zarządać pieniędzy i wyjść po czymś takim."
            wp "I skibidi."
        elif workedAtVasili:
            you "Masakra... Musiałem pracować..."
            wp "Do kogo poszedłeś?"
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
        "Zaraz przed tobą jest Wiktoria P."
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
    menu:
        "Skip the brick":
            $ telemetry_flag("skippedBrickDescription")
            jump ch02_brickDescriptionEnd
        "No i want to hear all about it":
            pass
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
    show wp normal at offscreenright with move
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
    jump ch02_brickDescriptionEnd
label ch02_brickDescriptionEnd:
    'Cegła była częścią czegoś większego, bardziej monumentalnego, choć nie wiesz czego.'
    'Cegły mogą być używane do budowania wszystkiego - od małego muru podczas protestu w Paryżu po wielką willę zdolną przetrwać tornado.'
    'Tak jak jedna z tych cegieł, ty również jesteś częścią tego miasta.'
    'Miasta, które przyjęło cię z otwartymi ramionami.'
    r "Why are you staring like that"
    "The sudden question catches you off-guard, interrupting your delusions"
    you "I got inspired?"
    "When you snap back to reality you notice Wiktoria had already left the bakery"
    r "Weirdo"
    "Rafał puts the brick back where it belongs - below the register"
    r "Okay so what do you want"
    you "Uhhh"
    "There are many buns laid out in front of you"
    "Each one was deliberately laid out to appear different"
    "when in reality its the same exact thing"
    you "I'll have four buns"
    "Rafał wipes his dirty paws and assembles your order"
    r "Anything else?"
    you "Do you have any cold drinks i could buy?"
    r "Yes i sell bottled performative-ness"
    you "what"
    r "Its an iced matcha latte"
    you "No thank you"
    "The black cat eagerly taps the buttons on the cash register"
    r "That will be $80"
    you "Uhh.. i have a really stupid question"
    r "Yes?"
    you "Is $80 alot of money?"
    you "You know, i was born yesterday"
    r "Its not alot but its not spare change"
    r "There's cheaper food across the street if you want that"
    r "In here you are also paying for the skills needed to make such a bun"
    "BBB is the equivalent of a millenial burger place with black gloves, fake brick walls and food served on a cutting board"
    "Except this place is cheaper"
    you "Here you go"
    r "Thank you and BON APPETIT"
    you "Bye"
    "You look at the bag of coins in your hand and start thinking"
    "Would you still be holding money right now if Piotr didnt come to help?"
    "And to think that you were so rude to him"
    you "{i}I really do need to apologize to him{/i}"
    you "Wait"
    you "Where does Piotr live?"
    r "He has a potions shop down the street"
    r "Piotr lives in the same building"
    r "You wont miss it theres a sign outside"
    you "Okay thanks"
    you "But... i'm not done"
    you "I have an unusual request"
    you "So yesterday I was rude to Piotr and I need to apologize to him. What should i get?"
    r "Well.. I dont know how to describe it BUT if he was a color he would be blue"
    r "And not the sky blue because that has too much sky"
    r "Also he wouldnt be navy blue either bc its blue with responsibilities"
    r "Its the kind of blue you think of when looking at something green"
    r "Maybe get something.. rectangular..??"
    "With every word Rafal says your confidence quickly gets replaced with confusion"
    "They say that a smile goes a long way when trying to be polite"
    "That is exactly why you keep smiling even though you have absolutely no idea what he is saying"
    "you scratch your head in pure confusion"
    you "{i}Just smile and nod...{/i}"
    you "Okay that makes sense"
    menu:
        "3 cups of coffee in a paper bag":
            $ gotCoffeeForPiotr = True
            $ piotrFoodPoints = 2
        "Bread in a paper bag":
            $ gotBreadForPiotr = True
            $ piotrFoodPoints = 0
        "A slice of red velvet cake (in a paper bag)":
            $ gotCakeForPiotr = True
            $ piotrFoodPoints = 1

    r "Okay give me just a moment!"
    "Rafał twirls on his right foot and assembles your order with pride"
    "You watch him swiftly assemble your order, and when he comes back you are already ready to pay"
    "He puts your apology gift on the table, and the plain paper bag gives you an idea"
    you "Can i have a pen i want to write something"
    r "Yes sure"
    you "{i}I want to write...{/i}"
    menu:
        "Sorry :(":
            $ piotrWritingPoints = 2
        "Sorry but be more fun next time":
            $ piotrWritingPoints = 0
        "Sorry i forgot your name":
            $ piotrWritingPoints = 1
        "Sorry, i forgot your name":
            $ piotrWritingPoints = 0
    "You scribble away trying to keep every letter steady and even with the rest"
    you "{i}Perfect{/i}"
    you "Okay that should be it. Thank you very much"
    r "No problem senorita"
    you "Bye"
    r "Byee"
    scene expression loc_bg("lanastreet") with dissolve
    "Finally happy, you leave the bakery and head straight to Piotr"
    scene expression loc_bg("cityexit") with dissolve
    "Rafał was right - it {i}was{/i} hard to miss the shop"
    "Especially the HUGE wooden door which was blocking half the pavement"
    scene bg potionshop with dissolve
    you "HELLO EVERYONE"
    "Your impatience knows no bounds. You are ready to jump over the counter just to apologize to piotr"
    you "{i}Where is this little bird{/i}"
    you "PIooooOTR come here"
    "Piotr emerges from the back of the shop"
    show piotr normal at center with dissolve
    you "{i}Why does he leave his shop open if he spends most of the time there{/i}"
    you "{i}Thats like sooo dangerous gurl i-{/i}"
    "Piotr opens his mouth to start speaking but before he can mutter a single word you overpower him with your proclamation"
    you "I've come to announce that i am a different [name]"
    you "I am no longer [name] i am now [name] version TWO"
    you "You hear me? I am version DOS. Even tres!"
    you "I can even be version four but i dont even know how to say four in spanish"
    you "That's how great i am"
    you "And to prove how much i've changed i hereby bequeath you a little treat"
    "You put on a smug grin before placing the paper bag directly onto the table, and sliding it over the countertop, careful not to scratch it"
    you "Enjoy"

    if gotCakeForPiotr:
        "Piotr carefully looks inside the oil-staned paper bag before noticing the message"
    elif gotBreadForPiotr:
        "Piotr carefully looks inside the extremely rectangular paper bag before noticing the message"
    elif gotCoffeeForPiotr:
        "Piotr smells the aroma of fresh coffee and quickly tears the bag apart, before noticing the message"
        "The message you wrote with great care and precision stayed intact due to sheer luck"

    "His eyes quickly skim the text"
    if piotrWritingPoints == 2:
        "He exhales and lowers his guard"
        "Piotr cant possibly be mad at you"
    if piotrWritingPoints == 1:
        "Piotr ignores the message and moves on"
    elif piotrWritingPoints == 0:
        "Piotr's eyes widen"
        p "what the"
        p "WHAT IS THIS"
    you "Now don't be so shy. Please indulge in this bratgrenian delicacy"

    if gotCakeForPiotr:
        "Piotr decided that taking the cake out was too risky so he ripped the bag"
        "Which revealed a slightly-smooshed cake"
        "The cake doesn't look very presentable anymore but its still edible"
        you "Like i said, Enjoy"

    elif gotBreadForPiotr:
        "Piotr lifts the bag because he has had enough and does not want to deal with this right now"
        "When suddenly..."
        "The bag rips and the bread falls out onto the tabletop, leaving a dent"
        "you start laughing very loudly and very obnoxiously"
        you "WHY DID IT FALL OUT LIKE THAT"
        "You are the only one laughing"
        you "I haven't laughed this much in a while"
        p "Great there's now a dent"
        you "okay okay wait"
        you "Here's the receipt. You can go back to the store and return it for store credit"
        "Piotr rolls his eyes"
        you "i'm actually really sorry this was supposed to be an actual gift but i didnt check the bread"
    elif gotCoffeeForPiotr:
        you "One is poisoned by the way"
        p "WHAT"
        p "No thank you"
        you "Just kidding"
        you "żarcik kosmonaucik"
        "piotr looks suspiciously at the coffees and exhales"
    
    you "Apology accepted?"

    if piotrFoodPoints + piotrWritingPoints > 2:
        p "Yes."
        p "Thank you"
        you "And thank {i}you{/i} for being as cool as a cucumber"
        p "Don't push it"
    elif piotrFoodPoints + piotrWritingPoints > 1:
        p "Yeah i guess"
        you "I can hear the doubt in your voice that is extremely rude"
        you "Where are your manners young man"
        p "That's exactly what i'm talking about you are NEVER serious"
        you "{i}Hmph!{/i}"
        you "{i}This isn't the end of it{/i}"
    else:
        p "Hell no"
        you "Aww why"
        p "I was working and you just barged into my shop"
        p "Just to waste my time"
        you "Where are your manners young man"

    you "Okay okay fine"
    you "Ignore the food i just wanted to say sorry"
    you "Yes i can be rude but im not rude because i have tofu with you its just because im sassy like that"
    p "..."
    "Piotr inspects you top to bottom, his gaze landing on your eyes and piercing you"
    p "Fine"
    p "You will change"
    you "???"
    you "{i}No YOU will change{/i}"
    you "So what were you working on"
    p "A ritual"
    you "That's it. Just some nondescript ritual?"
    p "Well if you MUST know i was getting ready to do a spell"
    you "SO YOU ARENT JUST A BORING FOREST JANITOR"
    you "I knew you had it in you"
    p "Actually that is exactly what i was going to do"
    you "..."
    "You dramatically roll your eyes, larping disappointment"
    p "Do you want to come and see how i do it?"
    "The bored [name] quickly turned into amused [name]"
    you "I'm all ears. What do i have to do?"
    p "Shut up and not touch anything"
    you "I cant promise to not touch anything but i will try"
    p "There's always something with you"
    p "Let's go"
    scene bg black with dissolve
    "Piotr takes you outside of the city"
    "Walking even two steps outside feels very wrong after all that you've heard about the forest"
    "He takes you to a small clearing about ten meters from the drawbridge"
    scene bg forestday with dissolve
    show piotr normal at center with dissolve
    p "Today i want you to just stand there and do nothing"
    p "I'm not sure this will even work with you around i do this alone"
    you "Okay"
    p "Pretend you are a tree or something"
    "you stand straighter than ever"
    p "Hold my bag"
    p "Actually no wait"
    "Piotr takes the bag and dumps its contents on the floor"
    p "Now hold it"
    you "Ok"
    "You hold it for about ten seconds before putting it on the floor"
    "Piotr is too preoccupied with his magic to notice that though"
    "He claws at the onyx stones on the ground and arranges them in a small circle"





    $ telemetry_end()
    if TESTING:
        call screen s_Telemetry()

