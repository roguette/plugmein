define asked_who_is_piotr = False
define accused_piotr_of_kidnapping = False
define asked_where_i_am_start = False
define stayed_silent_start = False

label piotrIntroductionMenu:
    menu:
        "Kim ty jesteś" if not asked_who_is_piotr:
            $ asked_who_is_piotr = True
            you "Kim ty jesteś?"
            p "A ty co??? Kim TY jesteś!?"
            you "Ja pierwszy zadałem pytanie, ale ok."
            you "Mam na imię [name]. Nie wiem gdzie jestem i dlaczego."
            "Zaczynasz myśleć o tym co się właśnie stało, ale zaczyna cię mocno boleć głowa."
            "Nie pamiętasz nic o sobie oprócz tego, jak masz na imię."
            "Nie wiesz nawet ile masz lat."
            "Jest ci strasznie przykro z tego powodu..."
            you "Może ty wiesz dlaczego tutaj jestem?"
            p "Jak powiedziałem ci wcześniej jestem czarodziejem, a nie pracownikiem w bibliotece. {b}Nie mam pojęcia!{/b}"
            p "Ja tylko oczyszczam ten las z nieczystości, np złej aury itd."
            p "Dodatkowo muszę jeszcze ochraniać przyrodę przed złem, turkuciami i pruchnicą."
            p "A w mieście leczę mieszkańców i pomagam im w przeróżnych sytuacjach związanych z ich kiepskim zdrowiem fizycznym {b}JAK I PSYCHICZNYM!!!{/b}"
            you "Okej..??"
            jump piotrIntroductionMenu
        "Oskarż o porwanie" if not accused_piotr_of_kidnapping:
            $ accused_piotr_of_kidnapping = True
            $ friendship["Piotr"] -= 1
            you "Wiem już wszystko o tobie..."
            you "To ty mnie porwałeś!{w} Jesteś okrutnym kłamcą!"
            "Wpadasz w malignę i zaczynasz płakać, walić głową o ziemię, tarzać się w malinach ⸻ dosłownie jak Raskolnikow."
            you "Dlaczegooooooo...!!!"
            you "To ty mnie porwałeś tą {b}różdżką{/b}."
            p "Bijesz mnie psychicznie, o co mnie oskarżasz!"
            you "To {b}co{/b} ty tutaj robisz?"
            p "Oczyszczam las sobie, a {b}TY{/b} mi cały rytuał zepsułeś!"
            you "Jakim cudem {b}ja{/b} jestem winny w tej sytuacji?"
            p "{b}Strzelę ci stringami jak jeszcze raz oskarżysz mnie o porwanie!!!{/b}"
            you "..."
            you "{i}Może moje słowa były trochę niemiłe...{/i}"
            jump piotrIntroductionMenu
        "Zapytaj się gdzie jesteś" if not asked_where_i_am_start:
            $ asked_where_i_am_start = True
            you "Ale gdzie ja jestem?"
            p "Jesteś w okolicach Bratgren."
            you "???"
            you "Czy ja wyglądam na osobę która wie co to jest za miejsce?! (bffr im not on mat-geo-ai pff)"
            "Piotr robi eyeroll, wzdycha i milczy."
            jump piotrIntroductionMenu
        "milcz" if not stayed_silent_start:
            $ stayed_silent_start = True
            you "{i}Milcząc chyba nic się nie dowiem{/i}"
            jump piotrIntroductionMenu
        "(nie mam więcej pytań)":
            jump piotrTravelToCity


label piotrTravelToCity:
    "Patrzysz się dookoła i widzisz tylko drzewa, a za Piotrem, z 300 metrów dalej jest ogromny mur. Taki ogromny, że mógłby to byś Wielki Mur Chiński ⸻ ale wyglądał na za bardzo z temu, żeby był oryginalny."
    if accused_piotr_of_kidnapping:
        "Twój wzrok wraca do Piotra."
        you "{i}Czy on naprawdę potrafi strzelać stringami..?{/i} {w} Jego pazury pewnie by rozszarpały te stringi."
    if stayed_silent_start:
        p "Co?"
        p "Czemu nic nie mówisz?"
        p "{b}Zatkało kakao?{/b}"
        you "Kakao nie zatyka bo nie ma patyka!!!"
        "Jesteś {b}bardzo{/b} dumny ze swojej wypowiedzi."
        you "{i}Łatwo z takimi!{/i}"
        you "Umiem gadać tylko teraz myślę."
    you "Nie znam nikogo, nie mam domu, i nie wiem co robić."
    "Patrzysz się w dół, na swoje ogromne łapy, które pięć minut temu były zwykłymi, ludzkimi dłońmi i powinieneś być bamboozled,{w=.5} ale nie jesteś."
    p "Chodź za mną, zaprowadzę cię do Kurowskiej, ona będzie wiedziała co z tobą zrobić."
    you "Czy mam się bać???"
    p "Ta..{w=.5} Nie, po prostu bądź dla niej miły, a ona ci wszystko powie."
    p "Najlepiej by było jakbyś od razu dostał pr*cę i dom, ale tego nie da się przewidzieć"
    you "..."
    you "{i}{b}PR*ACA, JAKA PR*CA!!! JA NIE CHCE{/b}{/i}"

    "Piotr zbiera swoje kamyki do torby i prowadzi cię do tego dużego muru, który wcześniej widziałeś."
    "Droga z lasu do miasta nie jest długa, chociaż czasem może zaskoczyć {i}dziką zwierzyną.{/i}"
    "Razem z Piotrem wracacie przez most i podążacie do urzędu miasta. Pomimo późnej godziny temperatura nie jest niesprzyjająca, nawet przyjemna (idealna do skinny dipping... znaczy CO)."
    scene bg entrancenight with fade 
    "Podchodzicie razem do ogromnej drewnianej bramy, za którą jest duże{w=.3}, rozległe{w=.3}, pachnące{w=.3} i zarazem śmierdzące miasto."
    you "{i}Czy ten most nie jest za stary?{/i}"
    you "{i}Przecież on się może w każdym momencie zawalić.{/i}"
    you "{i}Już mi się tutaj nie podoba, mieszkańcy polegają na starych technologiach, które już dawno powinny zostać wyparte.{/i}"

    you "{i}Przed czym chcą się bronić? Chyba nie chce wiedzieć...{w=1.0} aż strach pomyśleć co może być w ukryte w tych lasach.{/i}"
    scene bg citysquarenight with dissolve
    "Przechodzicie przez bramę do miasta, które jest zupełnie puste."
    "Na ulicach nie ma nikogo, {w}oprócz {i}was{/i}."
    "Zwróciłeś uwagę na ilość budynków, która była (g)astronomiczna. Aż w końcu dotarliście na rynek, na którym pomimo późniego wieczoru, dało się wyczuć miłą{w=.3}, ciepłą{w=.3}, witającą{w=.3} i zarazem przyjazną atmosferę."
    "Można by było powiedzieć, że ten wasz spacer jest {i}romantyczny{/i}{w=1.0}, gdyby nie to, że pewnie przez Piotra tu jesteś."
    you "{i}Brak żywej duszy na ulicach... Chyba nie jest tak późno. Mam nadzieję, że ta {u}Kurowska{/u} jeszcze ma otwarte biuro{/i}"
    "Podchodzicie do urzędu miasta. Wiedziałeś, że to wasza destynacja po wielkim{w=.3}, rozległym{w=.3}, ogromnym{w=.3} i zarazem małym herbem."
    "Miał taką...{w=0.5} urzędniczą aurę"
    scene bg cityhallinside with dissolve
    "Piotr wchodzi pierwszy do sekretariatu, po czym od razu cię wyprowadza."

    show piotr at center
    p "Siedź tu grzecznie ja zaraz wrócę."
    you "Okej"
    "{i}Ale z ciebie good boy.{nw}{/i}"
    "Siadasz na krześle obok. Krzesło się lekko ugina pod twoją ogromną dupą, ale nadal się trzyma. Ty jednak kompletnie to ignorujesz ⸻ myślisz o czymś innym."
    "O tym jak tu dotarłeś, kim jest Piotr, i co musisz robić."
    "Od razu jak się obudziłeś pod jakimś drzewem w tym lesie wiedziałeś, że coś tu nie gra..."
    "Tylko co..."
    "Rozluźniasz się i opierasz się o ścianę, czując jak sosnowe igły kłują cię w plecy."

    "Zostały na twojej koszulce od kiedy leżałeś w lesie."
    "Czujesz wstyd, ponieważ przeszedłeś przez całe miasto, wyglądając jak pijak."
    "Strzepujesz koszulkę, i wracasz do najbardziej produktywnej czynności ⸻ siedzenia ⸻ kompletnie ignorując to, że po tobie ktoś będzie musiał sprzątać te igły."
    "Po chwili wraca piotr i woła cię do sekretariatu..."
    scene bg secretary with dissolve


    show piotr at center with dissolve
    pause 0.5
    show piotr at left with move
    show filip at right with dissolve
    
    f "To jest furas pod tytułem???"
    p "[name]"
    you "Ale co ja..?"
    p "No przecież zapytał się o twoje imię."
    jump filipIntroduction