define asked_who_is_piotr = False
define accused_piotr_of_kidnapping = False
define asked_where_i_am_start = False
define stayed_silent_start = False

# renpy-graphviz: BREAK

label f_piotrIntroductionMenu:
    menu:
        "Kim ty jesteś" if not asked_who_is_piotr:
            $ asked_who_is_piotr = True
            you "Okay but jokes aside i have to know who you are"
            you "Are you my dad or something"
            p "My name is Piotr and i am a magician, if you remember"
            you "Is being a forest janitor your whole personality"
            p "No ofc not"
            you "Then tell me about the other side of you"
            p "Oh you actually care about that? Thats so kind of you"
            you "{i}oh my god{/i}"
            p "Dodatkowo muszę jeszcze ochraniać przyrodę przed złem, turkuciami i próchnicą."
            p "A w mieście leczę mieszkańców i pomagam im w przeróżnych sytuacjach związanych z ich kiepskim zdrowiem fizycznym {b}JAK I PSYCHICZNYM!!!{/b}"
            you "Oh my gof thats so cute"
            you "I almost feel bad for being rude to you you are a doctor"
            p "You should be"
            you "Hold your horses i said ALMOST"
            p "So what about you?"
            you "What about me"
            p "Who are you"
            you "Oh... about that.."
            "Trying to remember facts about you cannot come up with anything"
            "Since you are the main character AND the final girl you use your 300 iq brain to deduce something is blocking your memories"
            "What's weird is that you know what you like and what you hate"
            "But you cannot remember why or how that is"
            "Its almost as if you just survived amnesia and became a new person"
            you "I actually dont remember anything but if I had to guess I'd say i survived cancer but got long term memory loss"
            p "Thats not how it works"
            
            jump f_piotrIntroductionMenu
        "Oskarż o porwanie" if not accused_piotr_of_kidnapping:
            $ accused_piotr_of_kidnapping = True
            $ friendship["Piotr"] -= 1
            you "I can see right through your lies"
            you "You think im not the sharpest tool in the shed"
            you "But you are wrong!"
            p "What"
            you "You are trying to play 5d chess with me"
            p "And how exactly am i doing that?"
            you "You kidnapped me and you erased my memory"
            you "I can smell it in the air it has that kidnapping smell"
            "With every word you say his expression goes more and more grim"
            p "Is this ragebait?"
            you "No"
            p "I did not kidnap anyone"
            you "Thats exactly what a kidnapper would say"
            p "Ok then prove that i kidnapped you"
            you "Prove that you did not"
            you "zatkało kakao???"
            p "Okay lets go your way"
            p "Even if i did kidnap you and even if i erased your memory"
            p "You know nothing and you still need your help"
            p "What are you gonna do alone in the forest"
            you "Larp worms and live underground?"
            p "Not with that waist"
            you "EXCUSE ME"
            "You aren't evil and you aren't stupid either"
            "It's just ragebait. Prankless harm"
            "You give him a sassy hmph and after little thinking you realize you actually do need his help"
            you "Fine. I guess you are right this once"
            p "Jeszcze raz mi takie dyrdymały powiesz ja ci strzelę stringami"
            jump f_piotrIntroductionMenu
        "Zapytaj się gdzie jesteś" if not asked_where_i_am_start:
            $ asked_where_i_am_start = True
            you "Where am I?"
            p "In a forest near Bratgren"
            p "Bratgren is the city we all live in"
            you "That's so cool I thought you live up there in the trees"
            p "That is NOT TRUE"
            you "And where is this bratgren?"
            if accused_piotr_of_kidnapping:
                you "Or did you lie about that too?"
            p "Right behind you."
            "Theres a huge wall behind you and you can only assume it guards a city"
            "You try to hide the embarrassment on your face because you havent even thought of turning around"
            you "How convenient. Are you sure you didnt move it there with magic just to embarrass me?"
            p "Do you ever shut up?"
            jump f_piotrIntroductionMenu
        "milcz" if not stayed_silent_start:
            $ stayed_silent_start = True
            you "{i}Milcząc chyba nic się nie dowiem{/i}"
            jump f_piotrIntroductionMenu
        "(nie mam więcej pytań)":
            jump f_piotrTravelToCity

# renpy-graphviz: BREAK

label f_piotrTravelToCity:
    "Patrzysz się dookoła i widzisz tylko drzewa, a z 300 metrów dalej jest ogromny mur. Taki ogromny, że mógłby to być Wielki Mur Chiński - ale wyglądał na za bardzo z Temu, żeby był oryginalny."

    if stayed_silent_start:
        p "Co?"
        p "Czemu nic nie mówisz?"
        p "{b}Zatkało kakao?{/b}"
        you "Kakao nie zatyka bo nie ma patyka!!!"
        "Jesteś {b}bardzo{/b} dumny ze swojej wypowiedzi."
        you "{i}Łatwo z takimi!{/i}"
        you "Ale wracając, umiem gadać tylko teraz myślę."

    if accused_piotr_of_kidnapping:
        "Twój wzrok wraca do Piotra ale nie tak romantycznie tylko tak 'o jezu znowu ten yy jak on miał na imię??'."
        you "{i}Czy on naprawdę potrafi strzelać stringami..?{w} Jego pazury pewnie by rozszarpały te stringi.{/i}"

    "W końcu postanawiasz przemówić coś sensownego."
    "you also decide that it would be best to calm down"
    you "Nie znam nikogo, nie mam domu, i nie wiem co robić."
    "Patrzysz się w dół, na swoje ogromne łapy, które pięć minut temu były zwykłymi, ludzkimi dłońmi i powinieneś być bamboozled,{w=.5} ale nie jesteś."
    p "Chodź za mną, zaprowadzę cię do Kurowskiej, ona będzie wiedziała co z tobą zrobić."
    you "Czy mam się bać???"
    p "Ta..{w=.5} Nie, po prostu bądź dla niej miły, a ona ci wszystko powie."
    p "Najlepiej by było jakbyś od razu dostał pr*cę i dom, ale tego nie da się przewidzieć"
    you "..."
    you "{i}{b}PR*ACA, JAKA PR*CA!!! JA NIE CHCE{/b}{/i}"
    "Piotr zbiera swoje kamyki do torby i prowadzi cię do tego dużego muru, który wcześniej widziałeś."
    you "So you are not gonna do the ritual?"
    p "You are more important right now"
    you "{i}is he flirting with me right now{/i}"
    you "I HAVE A GIRLFRIEND"
    p "No"
    "Damn it"
    "Droga z lasu do miasta nie jest długa, chociaż czasem może zaskoczyć {i}dziką zwierzyną.{/i}"
    "Razem z Piotrem wracacie przez most i podążacie do urzędu miasta. Pomimo późnej godziny temperatura nie jest niesprzyjająca, nawet przyjemna (idealna do skinny dipping... znaczy CO)."
    scene bg entrancenight with fade
    "Podchodzicie razem do ogromnej drewnianej bramy, za którą jest duże{w=.6}, rozległe{w=.6}, pachnące{w=.6} i zarazem podśmierdujące miasto."
    you "{i}Czy ten most nie jest za stary?{/i}"
    you "{i}Przecież on się może w każdym momencie zawalić.{/i}"
    you "{i}Już mi się tutaj nie podoba, mieszkańcy polegają na starych technologiach, które już dawno powinny zostać wyparte.{/i}"
    you "{i}Przed czym chcą się bronić? Chyba nie chce wiedzieć...{w=1.0} aż strach pomyśleć co może być w ukryte w tych lasach.{/i}"
    you "Czy wy kupiliście tę ścianę na Temu?"
    show piotr normal with dissolve
    p "Jakie Temu o czym ty mówisz."
    you "No taki sklep internetowy."
    p "Jaki?"
    you "Tam można kupić wszystko ale to ci przychodzi po dwóch miesiącach."
    p "Ale o czym ty mówisz???"
    you "{i}Albo on jest głupi albo takie coś nie istnieje w tym świecie...{/i}"
    you "Gdzie my w ogóle jesteśmy?"
    p "No przcież mówiłem!!! Wchodzimy teraz do miasta Bratgren."
    you "Znaczy to wiem ale"
    you "{i}On nic nie wie. Z kim ja rozmawiam.{/i}"
    you "{i}Jeśli ktoś może odpowiedzieć na moje pytania, to to na pewno będzie ta Kurowska...{/i}"
    you "Nie ważne..."
    play sound "sfx_footsteps_alot.mp3"
    scene bg citysquarenight with dissolve
    play music "town_night.mp3" fadein 0.5
    "Przechodzicie przez bramę do miasta, które jest zupełnie puste."
    you "Dlaczego dosłownie nikogo nie ma na ulicach?"
    p "No bo jest zimno dzisiaj."
    you "Ale mi nie jest zimno."
    p "Nie wiem jak ci nie jest zimno, ja tu zamarznę zaraz."
    you "To chodźmy szybicej do tej Kurowskiej!"
    "Na ulicach nie ma nikogo{w}, oprócz {i}was{/i}."
    "Zwróciłeś uwagę na ilość budynków, która była (g)astronomiczna. Aż w końcu dotarliście na rynek, na którym pomimo późnego wieczoru, dało się wyczuć miłą{w=.6}, ciepłą{w=.6}, witającą{w=.6} i zarazem przyjazną atmosferę."
    "Można by było powiedzieć, że ten wasz spacer jest {i}romantyczny{/i}{w=1.0}, gdyby nie to, że pewnie przez Piotra tu jesteś."
    you "{i}Brak żywej duszy na ulicach... Chyba nie jest tak późno. Mam nadzieję, że ta {u}Kurowska{/u} jeszcze ma otwarte biuro{/i}"
    "Podchodzicie do urzędu miasta. Wiedziałeś, że to wasza destynacja po wielkim{w=.6}, rozległym{w=.6}, ogromnym{w=.6} i zarazem małym herbem."
    "Miał taką...{w=0.5} urzędniczą aurę."
    scene bg cityhallinside with dissolve
    "Piotr wchodzi pierwszy do sekretariatu, po czym od razu cię wyprowadza."
    show piotr normal at center
    p "Jednak nie wchodź bo muszę jeszcze z Filipem pogadać"
    you "O czym?"
    p "Mowa jest srebrem, a milczenie złotem."
    "Jesteś oszołomiony arogancją Piotra. Jesteś pewny że będzie ciebie obgadywać."
    p "Siedź tu grzecznie ja zaraz wrócę."
    you "Okej"
    "{i}Ale z ciebie good boy.{nw}{/i}"
    hide piotr
    "Siadasz na krześle obok. Krzesło się lekko ugina pod twojim ogromnym gyattem, ale nadal się trzyma. Ty jednak kompletnie to ignorujesz - myślisz o czymś innym."
    "O tym jak tu dotarłeś, kim jest Piotr, i co musisz robić."
    "Od razu jak się obudziłeś pod jakimś drzewem w tym lesie wiedziałeś, że coś tu nie gra..."
    "Tylko co..."
    "Rozluźniasz się i opierasz się o ścianę, czując jak sosnowe igły kłują cię w plecy."
    "Zostały na twojej koszulce od kiedy leżałeś w lesie."
    "Czujesz wstyd, ponieważ przeszedłeś przez całe miasto, wyglądając jak idiota."
    you "{i}Tyle aury straciłem{/i}"
    you "{i}Ale nikogo nie było na zewnątrz. Nikt mnie nie zobaczył{/i}"
    you "{i}Chyba że ktoś patrzył się przez okno?{/i}"
    "Strzepujesz koszulkę, i wracasz do najbardziej produktywnej czynności - siedzenia - kompletnie ignorując to, że po tobie ktoś będzie musiał sprzątać te igły."
    "Po chwili wraca piotr i woła cię do sekretariatu..."
    scene bg secretary with dissolve
    show piotr normal at center with dissolve
    pause 0.5
    show piotr normal at leftish with move 
    show filip normal at rightish with dissolve
    f "To jest furas pod tytułem???"
    p "[name]"
    you "Ale co ja..?"
    p "No przecież zapytał się o twoje imię."
    jump ch_filipIntroduction

# renpy-graphviz: BREAK