define metPetitty = False
# renpy-graphviz: BREAK
label l_GoingToTheLibrary:
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
            "{i}Naraz słychać głos fasoli:{/i}"
            "{i}Gdzie się pani tu gramoli?!{/i}"
            "{i}Nie bądź dla mnie taka wielka -{/i}"
            "{i}Odpowiada jej brukselka.{/i}"
            "{i}Widzieliście, jaka krewka! -{/i}"
            "{i}Zaperzyła się marchewka.{/i}"
            "{i}Niech rozsądzi nas kapusta!{/i}"
            "{i}Co, kapusta?! Głowa pusta?!{/i}"
            "{i}A kapusta rzecze smutnie:{/i}"
            "{i}Moi drodzy, po co kłótnie,{/i}"
            "{i}Po co wasze swary głupie,{/i}"
            "{i}Wnet i tak zginiemy w zupie!{/i}"
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
            jump l_petittyFirstEncounter
        "Hell nah":
            "Stwierdzasz, że on jest dziwny więc omijasz go szerokim łukiem"
            jump l_afterPetitty
# renpy-graphviz: BREAK
label l_petittyFirstEncounter:
    menu:
        "Przedstaw się":
            you "Nazywam sie [name] i mieszkam tutaj od 3 dni"
            m "Ok"
            pe "A ja jestem Petitty i ja czytam mangi"
            menu:
                "Wstyd":
                    $ friendship["Petitty"] -= 1
                    "Petitty robi side eye"
                    jump l_tooAssertive
                "Współczuję":
                    $ friendship["Petitty"] -= 1
                    "Petitty robi side eye"
                    jump l_tooAssertive
                "Masakra":
                    $ friendship["Petitty"] -= 1
                    "Petitty robi side eye"
                    jump l_tooAssertive
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
                    jump l_PetittyQuiz
        "\"Przedstaw się\"":
            jump l_tooAssertive
            
# renpy-graphviz: BREAK
label l_tooAssertive:
    $ friendship["Petitty"] -= 1
    you "Przedstaw się."
    "Czujesz się jak alfa"
    "Ale.."
    "Ten ktoś najwidoczniej przestraszył się z powodu twojej asertywności i wybiegł z biblioteki do swojej piwnicy"
    you "???"
    jump l_afterPetitty
# renpy-graphviz: BREAK
label l_PetittyQuiz:
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
    jump l_afterPetitty
# renpy-graphviz: BREAK
label l_afterPetitty:
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
    jump t_firstTimeLeftTheLibraryBeforeRaidingChurch

    
