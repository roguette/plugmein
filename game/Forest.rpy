define asked_who_is_piotr = False
define accused_piotr_of_kidnapping = False
define asked_where_i_am_start = False
define stayed_silent_start = False

label piotrIntroductionMenu:
    menu:
        "Kim ty jesteś" if not asked_who_is_piotr:
            $ asked_who_is_piotr = True
            you "Kim ty jesteś"
            p "A ty co??? Kim TY jesteś"
            you "Ja pierwszy zadałem pytanie ale ok"
            you "Mam na imię [name]. Nie wiem gdzie jestem i dlaczego"
            "Zaczynasz myśleć o tym co się właśnie stało, ale zaczyna cię mocno boleć głowa"
            "Nie pamiętasz nic o sobie oprócz tego, jak masz na imię"
            "Nie wiesz nawet ile masz lat"
            "Jest ci strasznie przykro z tego powodu"
            you "Może ty wiesz dlaczego tutaj jestem?"
            p "Jak powiedziałem ci wcześniej jestem czarodziejem, a nie pracownikiem w bibliotece. Nie mam pojęcia"
            p "Oczyszczam ten las z nieczystości, np złej aury"
            p "Dodatkowo ja muszę ochraniać przyrodę przed złem"
            p "A w mieście leczę mieszkańców"
            you "okej..??"
            jump piotrIntroductionMenu
        "Oskarż o porwanie" if not accused_piotr_of_kidnapping:
            $ accused_piotr_of_kidnapping = True
            $ friendship["Piotr"] -= 1
            you "Wiem już wszystko o tobie"
            you "To ty mnie porwałeś"
            you "Jesteś okrutnym kłamcą"
            "wpadasz w malignę i zaczynasz płakać"
            you "Dlaczegooooooo"
            you "To ty mnie porwałeś tą różdżką"
            p "bijesz mnie psychicznie, o co mnie oskarżasz"
            you "to co ty tu robisz"
            p "oczyszczam las sobie a ty mi cały rytuał zepsułeś"
            you "jakim cudem ja jestem winny w tej sytuacji"
            p "strzelę ci stringami jak jeszcze raz oskarżysz mnie o porwanie"
            you "{i}Może jednak to było trochę niemiłe?{/i}"
            jump piotrIntroductionMenu
        "Zapytaj się gdzie jesteś" if not asked_where_i_am_start:
            $ asked_where_i_am_start = True
            you "Ale gdzie ja jestem"
            p "Jesteś w okolicach Bratgren"
            you "???"
            you "Czy ja wyglądam na osobę która wie co to jest za miejsce"
            "[piotrName] robi brandy nitti eyeroll, wzdycha i milczy"
            jump piotrIntroductionMenu
        "milcz" if not stayed_silent_start:
            $ stayed_silent_start = True
            you "{i}Milcząc chyba nic się nie dowiem{/i}"
            jump piotrIntroductionMenu
        "(nie mam więcej pytań)":
            jump piotrTravelToCity


label piotrTravelToCity:
    "Patrzysz się dookoła i widzisz tylko drzewa, a za [piotrName]em, z 300 metrów dalej jest ogromny mur"
    if accused_piotr_of_kidnapping:
        "Twój wzrok wraca do [piotrName]a i zaczynasz zaczynasz myśleć, czy on naprawdę potrafi strzelać stringami"
        "Jego pazury pewnie by rozszarpały te stringi"
    if stayed_silent_start:
        p "Co?"
        p "Czemu nic nie mówisz?"
        p "Zatkało kakao?"
        you "Kakao nie zatyka bo nie ma patyka"
        "jesteś bardzo dumny ze swojej wypowiedzi"
        you "Umiem gadać tylko teraz myślę"
    you "Nie znam nikogo, nie mam domu, i nie wiem co robić"
    "patrzysz się w dół, na swoje ogromne łapy, które pięc minut temu były zwykłymi, ludzkimi dłońmi"
    p "Chodź za mną zaprowadzę cię do Kurowskiej, ona będzie wiedziała co z tobą zrobić"
    you "Czy mam się bać??"
    p "Nie, po prostu bądź dla niej miły, a ona ci wszystko powie."
    p "Najlepiej by było jakbyś od razu dostał pracę i dom, ale tego nie da się przewidzieć"
    you "..."

    "[piotrName] zbiera swoje kamyki do torby i prowadzi cię do tego dużego muru, który widziałeś wcześniej"
    "Droga z lasu do miasta nie jest długa, chociaż czasem może zaskoczyć dziką zwierzyną."
    "[piotrName] i [name] wracają przez most i podążają do urzędu miasta. Pomimo późnej godziny temperatura nie jest niesprzyjająca, nawet przyjemna."
    scene bg entrancenight with fade 
    "Podchodzicie razem do ogromnej drewnianej bramy, za którą jest duże miasto"
    you "{i}Czy ten most nie jest za stary?{/i}"
    you "{i}Przecież on się może w każdym momencie zawalić.{/i}"
    you "{i}Już mi się tutaj nie podoba, mieszkańcy polegają na starych technologiach, które już dawno powinny zostać wyparte.{/i}"
    you "{i}Przed czym chcą się bronić? Chyba nie chce wiedzieć...{/i}"
    you "{i}aż strach myśleć co może być w ukryte w tych lasach.{/i}"
    "Przechodzicie przez bramę do miasta, które jest zupełnie puste"
    "Na ulicach nie ma nikogo, {w} oprócz was."
    "[name] zwrócił uwagę na ilość budynków, która była astronomiczna. Aż w końcu bohaterowie dotarli na rynku, na którym pomimo później godziny, dało się wyczuć miłą i przyjazną atmosferę"
    "Można by było powiedzieć, że ten wasz spacer jest romantyczny, gdyby nie to, że pwenie przez [piotrName]a tu jesteś"
    you "{i}Brak żywej duszy na ulicach... Chyba nie jest tak późno. Mam nadzieję, że Kurowska jeszcze ma otwarte biuro{/i}"
    "Podchodzicie do urzędu miasta. Wiedziałeś że to właśnie ten budynek jest urzędem przez duży herb nad wejściem"
    "Miał taką... {w=0.5} urzędniczą aurę"
    "Piotr wchodzi pierwszy do sekretariatu, po czym od razu wyprowadza cię"
    show piotr at center
    p "Siedź tu grzecznie ja zaraz wrócę"
    you "Okej"
    "Siadasz na krześle obok. Krzesło się lekko ugina pod twoją ogromną dupą, ale nadal się trzyma. Ty jednak kompletnie to ignorujesz,"
    "Bo myślisz o czymś innym."
    "O tym jak tu dotarłeś, kim jest [piotrName], i co musisz robić."
    "Od razu jak się obudziłeś pod jakimś drzewem w tym lesie wiedziałeś, że coś tu nie gra"
    "Tylko co..."
    "Rozluźniasz się i opierasz się o ścianę, czując jak sosnowe igły kłują cię w plecy."
    "Zostały na twojej koszulce od kiedy leżałeś w lesie"
    "Czujesz wstyd, ponieważ przeszedłeś przez całe miasto, wyglądając jak pijak"
    "Strzepujesz koszulkę, i wracasz do najbardziej produktywnej czynności - siedzenia,"
    "kompletnie ignorując to, że po tobie ktoś będzie musiał sprzątać te igły"
    "Po chwili wraca piotr i woła cię do sekretariatu"

    show piotr at center with dissolve
    pause 0.5
    show piotr at left with move
    show filip at right with dissolve
    
    m "To jest furas pod tytułem?"
    p "[name]"
    you "Ale co ja"
    p "No przecież zapytał się o twoje imię"
    jump filipIntroduction
    


    

    

