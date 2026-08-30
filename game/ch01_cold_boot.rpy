
define askedWhoPiotrWas = False
define accusedPiotrOfKidnapping = False
define askedWhereIAmStart = False
define stayedSilentStart = False
define wasRudeToPiotr = False
define askedAboutCityHistory = False
define askedAboutHousing = False
define askedAboutWork = False
define commentedOnKurowskasAppearance = False
define rudeToKurowska = False
define metTomcio = False
define rudeToTomcio = False
define seenBjorkGhost = False
define hasSkinnyWaist = False
define rudeToVasili = False
define metVasili = False
define knowsAboutVasiliGrandfatherGhost = False
define hasToApologiseToPiotr = False
define metWiktoriaP = False
define receivedLoreAboutChurchOnTheFirstDay = False
define askedAboutSabrina = False
define askedAboutBjorkDeath = False
define askedAboutGhostsTalking = False
define fountainLoreReceived = False
define endorsedCommunism = False
define heardVasiliMonologue = False


# region INTERACTIONS

label ch01_m_fountainFirstClick:
    scene expression loc_bg("fountain") with dissolve
    "You spy with your little eye..."
    "and its a fountain..."
    you "{i}No tourists?{/i}"
    "There aren't any coins on the bottom of the fountain"
    you "{i}Well, atleast they dont have to scoop them out twice a week like in Rome{/i}"
    "You look around and there's not a single soul out"
    ".{w=0.5}.{w=0.5}."
    menu:
        "Touch the water":
            you "{i}i HAVE to touch it{/i}"
            "Either there's too little water in the fountain or the edges are way too tall for you"
            "Almost like they dont want random people touching the water"
            ".{w=0.5}.{w=0.5}."
            "!"
            you "{i}Huh{/i}"
            "You now have: {w=0.5}{b}a wet finger{/b}!"

        "Do not":
            you "Why am i even considering this"
            "and you were right to think that"
            "what if this city had more tricks up its sleeve and the water was poisonous"
            you "{i}Hell no{/i}"
    return

label ch01_m_fountainSecondClick:
    scene expression loc_bg("fountain") with dissolve
    "Your attitude towards the fountain is as cold as the water in it"
    "There's nothing to do here at this moment"
    return
    

label ch01_m_cityHallRudeToKurowska:
    you "{i}Hell no i'm not going back in there{/i}"
    you "{i}She's gonna eat me alive!{/i}"
    return

label ch01_m_cityHallNormalFirstInteraction:
    you "{i}I have more questions...{/i}"
    scene bg cityhallinside with dissolve
    "Everything here is new to you because i chose this cliche way to start a visual novel"
    "That way i have more control over the lore and what can happen"
    scene bg secretary with dissolve
    show filip normal with dissolve
    if rudeToKurowska:
        f "Oh. It's you."
        you "What?"
        f "What do u want"
        # happy meal
        menu:
            "What's her problem":
                "Filip's face contorted"
                "It looks like he's having a nightmare"
                f "Girl i-"
                f "you literally le insulted her hair"
                f "She spends so much money to have maybelline hair and you just..."
                "He waves his hands around due to the lack of words"
                f "That was rude"
                menu:
                    "That was constructive criticism":
                        "It's been a long day and Filip is very tired and you are NOT helping."
                        "He covers his face and pretends to sob dramatically"
                        f "When will you finally understand?"
                        f "She is the president you HAVE to be on good terms with her"
                        f "She has a ton of power over you and you chose to fight her"
                        f "Play stupid games win stupid prizes"

                    "Hmph! I will apologize if you so wish.":
                        f "Good"
                        f "Wait no hold on"
                        f "What are you going to say"
                        f "I dont want you to say something stupid and get into more trouble"
                        "You put your hand on your chin and pretend to think really hard"
                        menu:
                            "I was on drugs and thought you were bald":
                                pass
                            "I had something in my eye":
                                pass
                            "I lied because im a pick me":
                                pass
                            "I thought her weave reminded me of my dead hamster":
                                pass
                        "Filip starts giggling uncontrollably"
                        "You arent sure if its your answers which made him laugh or your stupidity"
                        f "Yeah no that is not gonna work. You will have to come up with something better"
                        you "Hmm.."
                        you "Ok i will do something tomorrow"
                        you "I'm too tired for this today"
    else:
        f "Oh hey"
        you "I have a question..."
        menu:
            "Where is my house":
                "Filip rolls his eyes dramatically"
                f "Did you even look at the keys"
                f "Theres an address attached"
                "You take the keys and put them on the table and inspect them closely"
                "Indeed, there is a small keychain with a street name written on it"
                you "But isnt this like dangerous?"
                f "How"
                you "If i lose my keys the person who finds them will be able to unlock my house"
                f "Then rip the tag off and write your name"
                f "If someone finds the keys they will give them to us"
                you "And what if they dont"
                "Filip has clearly had enough and sighs"
                f "Then you will come to me and we will come up with something"
            "Where is everyone":
                f "Its almost midnight and its cold as hell outside"
                f "If you werent \"born\" today you would be asleep right now"
                "You audibly breathe out"
                you "{i}I guess he's right{/i}"
                you "{i}I'd rather be in a warm bed than here{/i}"
                you "Oh."
                f "And yes, we have alot of residents"
                f "It's just that its, you know, late"
                f "Come to the square tomorrow and you will see"
            "What's in the forest":
                f "Ebola"
                "your eyes widen"
                f "Jk its not ebola its bts stans"
                you "Oh! That's cute"
                you "What do i need to do if i see one"
                f "You dont look like you can end bts so you can sing dynamite and pretend you are an army"
                you "I'd rather die"
                you "And piotr was trying to clean the forest?"
                f "Yes"
                f "Now you know why you shouldn't go to the forest"
                you "{i}We will see about that{/i}"
            "Are there any tourist traps?":
                f "No there aren't any"
                f "Because we don't have any tourists"
                you "How"
                f "It's just us here in Bratgren"
                you "So theres literally no one else?"
                f "As far as we are aware, yes"
                f "The forest is way too dangerous so we didnt explore it much"
                you "That's a shame"
                f "Why? Are you already trying to escape?"
                you "I came from a rich family and my bedroom was the size of the square outside soo"
                you "So this feels like prison"
                "Filip giggles"
                f "Yeah right"
                f "If you ever accidentally slip and tumble all the way into the forest and meet the monsters in it"
                f "Sing a bts song"
        you "Okay..."
        you "Well i dont want to take up more of your PRECIOUS time"
        you "Thank you and goodnight"
        f "Bye"
    return

label ch01_m_enteringChurch:
    "Walking up to the church you feel a sudden breeze of air graze your back"
    scene bg churchnighta with dissolve
    "The building in front of you, which you can only assume is a church, looks very old and a bit dilapidated"
    jump ch01_firstNightTownWalkPartB


# endregion

label ch01_cold_boot:
    "{cps=1}...{/cps}"
    stop sound fadeout 0.5
    "{cps=25}Zostałeś właśnie potrącony przez mks 23{w} (do przybówki).{/cps}"
    "{cps=20}Twoje krzyki usłyszał tylko kierowca tego autobusu.{/cps}"
    "{cps=15}Który pewnie już uciekł i jedzie sobie dalej.{/cps}"
    "{cps=2}...{/cps}"
    "Mimo tego,{w=.5} o dziwo,{w=.5} żyjesz{w=.5}<3"
    "Strasznie cię boli głowa, ale nie możesz podnieść ręki, aby sprawdzić czy w ogóle ją jeszcze masz."
    "Jesteś tak słaby, że nie możesz nawet otworzyć oczu."
    call chapterTransition("Akt 1", "Zatkało kakao?")
    play music "forest.mp3" fadein 2.0
    m "Do jasnej muffinki!!!"
    m "Proszę pana, czy pan żyje?!"
    "Ktoś kładzie swoją rękę na twoim ramieniu i próbuje cię obudzić, a jego długie pazury wbijają ci się w skórę."



    scene bg forestnight with vpunch

    you "AAAAA!!!!"
    you "Proszę mnie nie dotykać!!!"
    you "This is my no-no square!!!"
    you "Stranger Danger!!!"
    show piotr normal at center with dissolve
    "Otwierasz oczy i widzisz przed sobą wysokiego ptaka, od którego próbujesz się odsunąć, ale{w=.5} za tobą jest drzewo."
    "Dlatego siedzisz i patrzysz się na niego jak głupi."
    you "{i}Co jest?{/i}"
    you "{i}Czemu on jest {w=.5}{u}ptakiem{/u}???{/i}"
    "Patrzysz się na niego z 10 sekund...\n{w=1.0}1{w=1.0}2{w=1.0}3{w=1.0}4{w=1.0}5{w=1.0}6{w=1.0}7{w=1.0}8{w=1.0}9{w=1.0}10{nw}"
    "Bardzo chcesz do niego podejść i mu się przyjrzeć, ale...{w=.5} bardzo się go boisz..."
    "Kiedy ptak wykluwa się ze swojego jajka traktuje pierwszą rzecz, którą widzi jako swoją matkę. {w=1.0}Coś podobnego dzieję się z Tobą,{w=.1} ale na odwrót."
    "On na pewno miał coś wspólnego z tym, cokolwiek się właśnie wydarzyło, więc od razu go nie lubisz."
    you "{i}Co on ze mną zrobił???{/i}"
    you "{i}To chyba {cps=10}{b}on{/b}{/cps} mnie tutaj przywołał, jak jakiegoś ducha.{/i}"
    "Patrzysz się na niego z podejrzliwością, jak spod byka niemalże."
    you "!Who the hell are you"
    you "!And why did you put me in this cliche visual novel situation"
    you "!Waking up in the forest and all that"
    m "Nie drzyj się, jesteś w lesie!!!"
    you "!Oh no no no you are going to answer all my questions first"
    you "!You have 10 seconds until i let you know i ate eggs for breakfast"
    p "!Can you shut up for once"
    p "!You are in a forest so SHUT UP"
    p "Nazywam się Piotr i jestem czarodziejem."
    you "!Magician? Like a birthday party magician?"
    p "???"
    you "!Like do you do silly tricks like pulling rabbits out of your conveniently huge top hat"
    p "!No that is called animal abuse"
    you "!Oh"
    you "{i}!He's so cute i cannot be angry at him{/i}"
    you "{i}!A little feisty but i can tolerate that{/i}"
    "Patrzysz się dookoła i widzisz obok siebie koło z czarnych kamieni."
    "Piotr daje ci swoją rękę, a dokładniej łapę, i pomaga ci wstać."
    you "Co to za kamyki tam masz?"
    you "Te takie czarne..."
    p "To?"
    "Wskazuje jednym ze swoich długich,{w=.5} czarnych,{w=.5} strasznych,{w=.5} a nawet krzywych{w=.5} pazurów na koło z czarnego kamienia."
    you "Tak."
    "Piotr podchodzi do tego koła i podnosi dwa kamienie."
    menu:
        "!Omg they are dark like your crusty ass nails":
            p "!Hell no"
        "!Can i have one?":
            p "!Hell no"
    p "To jest onyks. Używam tych kamieni do usuwania złych vibeów z tego lasu."
    p "Im więcej złej energii wchłaniają, tym są cięższe. Patrz tu..."
    "!your enthusiasm knows no bounds so you add a few ohs here and there to support the conversation"
    p "Weź ten i ten i zrób takie six―seven."
    "Jeden z tych kamieni rzeczywiście jest o wiele cieższy od drugiego. Mimo tego, że są prawie identyczne."
    you "Ale heca!"
    you "!So why are you carrying these heavy stones are you stupid"
    p "!No its because {nw}"
    p "!Actually no i've been nothing but nice to you and you are rude like this"
    p "!I am not telling you anytihng"
    you "{i}this bitch{/i}"
    you "!Okay fine sorry i got a little carried away you can continue"
    p "So as i was saying... before your rude ass interrupted me"
    p "Theres a limited supply of these stones"
    p "We use them for clearing bad energy in this forest"
    "You should be thankful he is doing this because if it werent for the magical bird in front of you monsters would have mauled you like bts stans on twitter"
    you "{i}Okay that is indeed terrifying{/i}"
    p "anyways... back to those stones"
    p "If a stone is too heavy i leave it at home"
    you "So you just have a pile of rocks at home?"
    p "Yes"
    you "It's giving coal miner"
    p "NO IT DOESNT"
    you "I'll be the judge of that.. (small text idk how to do it)"
    p "What did you say?"
    you "What did you hear"
    p "Im not sure"
    you "Then i guess we will never know"
    you "What were you doing before you isekaied me here?"
    p "I was cleaning the forest like i explained before and this had nothing to do with you"
    you "Okay so you havent started yet?"
    p "Yes"
    you "What if i am evil"
    p "You're not evil you are just being rude on purpose"
    p "Im sure you couldnt even hurt a fly"
    you "True.. they are way too fast"
    you "So when are you gonna answer my questions?"
    p "I will provide answers only IF you promise to stay quiet"
    you "{i}This bitch{/i}"
    you "{i}Fine. I will stay silent for a moment{/i}"
    you "{i}If he tries me again i will just say he kept me in his basement{/i}"
    you "{i}Does he have a basement though?? What if he doesnt?{/i}"
    you "Do you have a basement"
    p "What? Yes. Why did you ask {nw}"
    you "{i}Bingo{/i}"
    you "Okay then we have a deal."
    jump ch01_piotrIntroductionMenu

label ch01_piotrIntroductionMenu:
    menu:
        "Kim ty jesteś" if not askedWhoPiotrWas:
            $ askedWhoPiotrWas = True
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
            
            jump ch01_piotrIntroductionMenu
        "Oskarż o porwanie" if not accusedPiotrOfKidnapping:
            $ accusedPiotrOfKidnapping = True
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
            jump ch01_piotrIntroductionMenu
        "Zapytaj się gdzie jesteś" if not askedWhereIAmStart:
            $ askedWhereIAmStart = True
            you "Where am I?"
            p "In a forest near Bratgren"
            p "Bratgren is the city we all live in"
            you "That's so cool I thought you live up there in the trees"
            p "That is NOT TRUE"
            you "And where is this bratgren?"
            if accusedPiotrOfKidnapping:
                you "Or did you lie about that too?"
            p "Right behind you."
            "Theres a huge wall behind you and you can only assume it guards a city"
            "You try to hide the embarrassment on your face because you havent even thought of turning around"
            you "How convenient. Are you sure you didnt move it there with magic just to embarrass me?"
            p "Do you ever shut up?"
            jump ch01_piotrIntroductionMenu
        "milcz" if not stayedSilentStart:
            $ stayedSilentStart = True
            you "{i}Milcząc chyba nic się nie dowiem{/i}"
            jump ch01_piotrIntroductionMenu
        "(nie mam więcej pytań)":
            jump ch01_afterPiotrIntroductionMenu

label ch01_afterPiotrIntroductionMenu:
    "Patrzysz się dookoła i widzisz tylko drzewa, a z 300 metrów dalej jest ogromny mur. Taki ogromny, że mógłby to być Wielki Mur Chiński - ale wyglądał na za bardzo z Temu, żeby był oryginalny."

    if stayedSilentStart:
        p "Co?"
        p "Czemu nic nie mówisz?"
        p "{b}Zatkało kakao?{/b}"
        you "Kakao nie zatyka bo nie ma patyka!!!"
        "Jesteś {b}bardzo{/b} dumny ze swojej wypowiedzi."
        you "{i}Łatwo z takimi!{/i}"
        you "Ale wracając, umiem gadać tylko teraz myślę."

    if accusedPiotrOfKidnapping:
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
    menu:
        "Sprowokuj piotra":
            $ wasRudeToPiotr = True
            $ friendship["Piotr"] -= 1
            you "Obsrałeś się jak mnie zobaczyłeś Panie Piotrze, więc {i}SYBAU!{/i}"
            p "To nieprawda. Proszę nie oczerniać mojego wizerunku!"
            you "{i}Ale dałem do pieca...{/i}"
            p "..."
            jump ch01_afterPiotrRagebaitMenu            
        "Milcz":
            you "{i}On NIE jest tuff.{/i}" 
            jump ch01_afterPiotrRagebaitMenu

label ch01_afterPiotrRagebaitMenu:
    p "Oczyszczałem las, jak mi kazałeś, a on pojawił się koło mnie i zepsuł mój rytuał, teraz muszę zacząć od nowa."
    you "Jakim cudem to jest moja wina?"
    you "Trzeci raz cię pytam i dalej nie wiem."
    m "No właśnie też bym chciał usłyszeć jakim cudem to jest twoja wina w tej sytuacji."
    m "Coś mi się wydaje, że są rzeczy ważniejsze."
    m "Ty możesz swoje rytuały zrobić nawet jutro. A [name] mógł w tym lesie umrzeć!"
    you "Mówiłem!"
    m "Chodź tu."
    "Podchodzisz trochę bliżej do Filipa, on wstaje i podaje ci rękę."
    "Uśmiechasz się jak w reklamie nieruchomości."
    "Nie wiesz, czy możesz mu ufać, ale on na pewno ma lepsze vibe-y od Piotra."
    you "Tak się wita z ludźmi Panie Piotrze"
    f "Cześć. Nazywam się Filip i witam w naszym małym{w=.6}, pięknym{w=.6}, fajnym{w=.6} i zarazem przytulnym mieście Bratgren. Pewnie masz ogromną ilość pytań?"
    you "No tak!"
    f "A czy coś już wiesz o tym mieście?"
    you "No nie..."
    "Filip jest uradowany tą informacją z jakiegoś powodu."
    f "No to świetnie. Teraz zaprowadzę cię do Kurowskiej, ona odpowie na wszystkie twoje pytania."
    f "Ona lubi takie rzeczy opowiadać tylko musisz zadać {i}odpowiednie.{/i}"
    you "{i}TFYM ODPOWIEDNIE?!{/i}"
    f "Tylko nie stresuj się. Bądź dla niej miły i ona będzie miła dla ciebie"
    f "Aha powiem ci jeszcze jedną rzecz - nie jesteś jedyny."
    f "Wszyscy pojawiliśmy się przed tym miastem, tak jak ty."
    you "Piotr mi tego nie powiedział..."
    f "A to czemu gatekeepujesz, panie Piotrze?"
    p "To jest mój pierwszy raz, kiedy spotykam taką osobę..."
    f "Ma sens, ale proszę następnej osobie takie rzeczy mówić!"
    f "Pan [name] pewnie się stresował przez ciebie."
    you "No właśnie!!!"
    f "No dobra wracając do Kurowskiej."
    f "Najpierw muszę się zapytać czy pana przyjmie."
    f "Ostatnio złapałem ją na robieniu skipu C na stole..., więc przyjemnie nie było i nie pachniało też dobrze..."
    you "Mam tylko jedno pytanie..."
    f "Tak?"
    you "Dlaczego jeszcze nie śpicie? Czy nie jest teraz noc?"
    f "Dzisiaj mieliśmy problem z wodą w mieście i cały dzień byliśmy tym zajęci."
    f "W tym mieście zawsze coś się dzieje..."
    "Filip podchodzi do drzwi i grzecznie puka."
    play sound "door_knock.mp3"
    f "Dobry wieczór, mam nową osobę czy mogę ją tutaj wprowadzić?"
    m "Jasne!"
    play sound "audio/sfx_door_open.mp3"
    "Filip otwiera drzwi i wpycha cię do biura, szybko zamykając za tobą drzwi."
    f "No no no idź idź..."

    scene bg office
    stop music

    "..."
    "Przed tobą siedzi Pani Kurowska, która ma taką aurę, że jej wzrok potrafi schłodzić pokój."
    show kurowska normal with dissolve
    you "Dobry wieczór..."
    k "Witam cię w miasteczku Bratgren! Jak cię zwą?"
    you "Zwą...{w=1} mnie [name]."
    k "Okeeej.. Mam na imię Barbara, jestem prezydentem miasta. Sprawuję tutaj władzę od 7 lat. Co cię tutaj sprowadza?"
    you "Właśnie obudziłem się w lesie, nie wiem kim jestem, nie wiem gdzie jestem, znam tylko swoje imie."
    you "Piotr znalazł mnie i zaprowadził mnie do Pani."
    you "No i tyle wiem."
    k "Czyli tak jak wszyscy..."
    "Barbara pisze coś do swojego notatnika."
    k "Jeszcze raz jak masz na imię???"
    you "[name]"
    k "Jakie dziwne imię. Weź mi to przeliteruj."

    $ nameSpelled = '-'.join([f"{letter}{{w=0.5}}" for letter in name])
    you "[nameSpelled]"
    k "Okej mam."


    menu:
        "Docieknij co to znaczy wszyscy.":
            you "Co to znaczy, że \"tak jak wszyscy\"?"
            k "Wszyscy, którzy tutaj mieszkają trafili w ten sam sposób do naszego miasta."
            k "Nikt nie wie skąd się tutaj bierzemy, ale jedno wiadomo - jesteśmy tutaj szczęśliwi."
        "Milcz":
            you "{i}Chyba nie wiem o co chodzi... ale boję się jej o to pytać.{/i}"
            you "{i}Może jest jeszcze jakaś agresywna.{/i}"
    you "Mam kwerendę!"
    k "Słucham?"
    you "Co jest w lesie poza miastem, i dlaczego to miasto jest w jakichś hebździnkach dolnych?"
    k "Ha ha!"
    k "Jeśli wyjdziesz do lasu zjedzą cię potwory albo umrzesz z powodu jakiejś niszowej choroby."
    you "..."
    "Jesteś w totalnym szoku!"
    k "No właśnie dlatego Piotr robi te rytuały. Wokół tego miasta jest taka tarcza, która odpycha od siebie złą energię."
    you "No piotr mi mówił jak on to robi tym takim onyksem."
    k "Problem jest w tym, że za jakieś 5 lat braknie nam tego onyksu..."
    k "Więc albo znajdziemy jakiś sposób na oczyszczanie tego onyksu."
    k "Albo będziemy musieli przenosić onyks w 5 osób, bo będzie tak ciężki, że inaczej się nie da."
    k "...albo wszyscy umrzemy."
    you "..."
    you "{i}Nie daję zgody na śmierć!{/i}"
    you "{i}Na pewno coś wymyślą do tego czasu więc nie muszę się tym przejmować.{/i}"
    you "A może pani ma do mnie jakieś pytania?"
    k "Hmm...."
    k "Czy ty cokolwiek pamiętasz?"
    "Ale ty nie pamiętasz nic. Twoja pamięc jest pusta, jak nowy dysk Simsang SSD T1 2TB Titan Gray USB-C."
    "Próbujesz coś sobie przypomnieć, ale znowu zaczyna cię boleć głowa."
    "Tym razem ból jest jeszcze gorszy niż wcześniej, więc chwytasz się jej i szybko zaczynasz myśleć o czymś innym."
    you "{i}Ewidentnie coś albo ktoś nie chce, żebym coś pamiętał...{/i}"
    you "{i}Na razie lepiej będzie udawać, że nic nie rozumiem.{/i}"
    you "{i}Bo jeszcze wyczyszczą mi pamięc jeszcze raz!{/i}"
    you "Nic nie pamiętam."
    k "Właśnie nikt w tym mieście nic nie pamięta..."
    k "Wszyscy mają jakieś zaniki pamięci."
    k "Ja też."
    you "Chciałem porozmawiać o czymś innym, nie takim ponurym jak śmierć całego miasta..."
    you "Ale śkończyło się na tym, że wszyscy mamy alzheimera!"
    you "Było by to zabawne, gdyby nie było to tak straszne."
    k "Jakoś trzeba sobie radzić."
    jump ch01_kurowskaDialogMenu

label ch01_kurowskaDialogMenu:
    if askedAboutHousing and askedAboutCityHistory and askedAboutWork:
        jump ch01_gettingHouseKeysGood

    k "Czy masz jakieś pytania?"
    menu:
        "Zapytaj o historię miasta." if not askedAboutCityHistory:
            $ askedAboutCityHistory = True
            you "A czy Bratgren ma jakąś historię?"
            k "Wywalę cię zaraz. Oczywiście, że ma."
            k "See the portrait on the wall? That's bjork"
            k "You should take a good look at it and remember her face"
            k "She is, i mean was, the most important lady in this city"
            k "Theres a very very long story and i will tell you that some other time"
            k "What you need to know is that we aren't the only city in this world"
            k "Theres, for example, Lupus"
            k "Bjork was born in Lupus and one day, she got kicked out of it"
            k "Bratren is the city she started"
            you "And where did I come from?"
            k "We actually don't know"
            k "People just started appearing at some point"
            you "That's not suspicious"
            k "Would you rather go back to the forest?"
            you "{i}Damn it shes right{/i}"
            you "No"
            k "Exactly"
            jump ch01_kurowskaDialogMenu

        "Zapytaj o nocleg." if not askedAboutHousing:
            $ askedAboutHousing = True
            you "Gdzie jest najbliższy hotel czy coś, bo nie mam ani domu ani mieszkania, gdzie ja będę spał?"
            k "Muszę tylko znaleźć klucze do twojego domu..."
            you "Dom?? Za darmo???"
            k "Oczywiście że nie za darmo. Darmowe domy mają tylko ci co pracują."
            k "Powiedzmy że w ten sposób ja inwestuję w ciebie."
            you "Oczywiście że będę pracował!!!"
            k "Mam nadzieję, że mnie nie cyganisz."
            you "{i}I klasa. Dom za darmo? W snach mi się to nie śniło.{/i}"
            jump ch01_kurowskaDialogMenu

        "Zapytaj o pracę." if not askedAboutWork:
            $ askedAboutWork = True
            you "A co z pracą?"
            you "Wiem, że filip pracuje w sekretariacie. A co robią inni?"
            you "Inni w sensie przeciętni ludzie."
            k "Powiem ci, że praca to znaczy robić cokolwiek na korzyść miasta."
            k "Są rolnicy, są piekarze, są kurierzy..."
            k "A jest na przykład taki pan Vasilij, który mimo tego że mieszka w mieście i korzysta z naszej ochrony przed złem, nie robi kompletnie nic."
            k "Vasilij tylko siedzi w domu i narzeka na rząd."
            you "Nie no coś tam wymyślę!"
            you "Chyba umarłbym z nudów gdybym był taki jak on."
            k "No ja też nie wiem jak mu się nie nudzi."
            k "Kompletnie nie jestem w stanie wyobrazić takiego życia bez jakichkolwiek czynności..."
            you "{i}Pryszniców on pewnie też nie może wyobrazić.{/i}"
            k "Dobra wracając do twojej pracy..."
            "Barbara przegląda dokumenty na stole, potem w stole, potem za nią."
            "Wydaje się, że ona wie że jest jakaś praca, ale nie może znaleźć tego papieru na stole."
            k "Do jasnej muffinki... Zgubiłam chyba..."
            k "No to w takim razie nie mam nic. Jutro bedę w stanie powiedzieć wiecęj, dlatego dzisiaj jesteś wolny."
            k "Tylko zgłoś się do mnie jutro."
            you "Jasne!!! XOXO"
            jump ch01_kurowskaDialogMenu

        "Powiedz coś o jej wyglądzie." if not commentedOnKurowskasAppearance:
            $ commentedOnKurowskasAppearance = True
            menu:
                "Powiedz coś o jej ubiorze":
                    you "Czy każdy może kupić takie ubrania?"
                    you "Bo Pani wygląda jak DIVA!"
                    k "Ha ha, dziękuje. Oczywiście, że można, trzeba się tylko zgłosić do naszej krawcowej."
                    k "Jest na rynku, obok piekarni"
                    $ friendship["Kurowska"] += 1
                    jump ch01_kurowskaDialogMenu
                "Powiedz coś o jej fryzurze":
                    you "Jakie wydarzenia spłodziły te fryzurę?"
                    k "Masz jakiś problem z moimi lśniącymi włosami z reklamy Maybelline?"
                    you "Nazywanie tego włosami jest dość łaskawym określeniem..."
                    k "Czy ty mnie obrażasz??"
                    you "Myślę, że daję ci coś co nazywa się konstruktywną krytyką!"
                    k "Zaraz ty i twoja konstruktywna krytyka zostaną wywaleni przez to okno."
                    $ rudeToKurowska = True
                    k "Dobrze w takim razie koniec tego wywiadu. Masz tutaj klucze do twojego domu, a teraz idź zanim cię wywale!"
                    scene bg secretary with vpunch
                    play sound "audio/sfx_door_slam.mp3"
                    you "{i}JESZCZE ŻYJĘ! Byłoby ciężko gdyby mnie wyrzuciła na bruk. Dostałem klucze do domu, o przyjemnych rozmowach nie myślę.{/i}"
                    jump ch01_gettingHouseKeysUniversal

label ch01_gettingHouseKeysGood:
    k "Jeśli nie masz więcej pytań, masz tutaj klucze do twojego nowego domu.{w} (ps. Kasia Dowbor go remontowała)"
    you "{i}Tam musi być luksusowo{/i}"
    you "Thank you! Thank you! Thank you!"
    jump ch01_gettingHouseKeysUniversal

label ch01_gettingHouseKeysUniversal:
    scene bg cityhallinside with dissolve
    play music "town_night.mp3"
    show piotr normal 
    "Wychodzisz z gabinetu Kurowskiej."
    p "Wyszstko dobrze?! Coś ty długo u niej byłeś..."
    you "Jesteś delulu nie było mnie dosłownie 5 minut."
    p "Jak ci poszło?"
    you "Patrz co mam!! (#flex)"
    "Mówiąc to pokazujesz mu klucze do Twojego własnego domu."
    "Podnosisz klucze do twarzy Piotra i widzisz brelok z adresem"
    "Piotr jest zazdrosny, ponieważ on musiał pracować by dostać swój dom."
    p "Aha. Okej."
    p "W takim razie muszę iść dokończyć rytuał z wcześniej, w którym mi przeszkodziłeś. ŻEGNAM!"
    hide piotr with dissolve
    you "{i}Chyba się na mnie obraził.{/i}"
    if wasRudeToPiotr == True:
        you "{i}Chyba przesadziłem w tym sekretariacie.{/i}"
    you "{i}Ale bracie its not that deep. No cóż, idgaf.{/i}"
    "Przed wyjściem z urzędu miasta patrzysz się na zegar, i widzisz, że jest 23:44."
    $ time.setTime(23,44)
    show screen s_clock
    scene bg citysquarenight with dissolve
    play sound "sfx_footsteps_a.mp3"
    "Wychodzisz z urzędu miasta i idziesz przed siebie."
    "Czujesz dreszcze przebiegające cię po plecach."
    "Ale{w=0.6} nie wiesz dokładnie, co je spowodowało - to, że nie ma żywej duszy{w=0.6}, czy to, że po prostu jest zimno."
    you "{i}Boże czemu jest tak zimno???{/i}"
    "Łapiesz się za ramiona próbując się jakoś ogrzać."
    you "{i}Jaka to pora roku?{/i}"
    you "{i}Czy oni w ogóle mają tu zimy?{/i}"
    you "{i}Chyba, że to jest wiosna...{/i}"
    you "{i}Nie chcę zimy!{/i}"
    "Mówiąc to, tupnąłeś nóżką jakbyś robił wino."
    "Patrzysz się w górę w poszukiwaniu odpowiedzi, ale widzisz tylko ciemne, puste a nawet nudne niebo."
    "Nie masz pojęcia co teraz robić."
    call screen s_walkable_Square()
        
label ch01_goingHomeFirstNight:
    "Jedyny fakt o tym mieście, którego jesteś w 100%% pewien, to jest to, że fontanna jest magiczna."
    "Podchodzisz więc bliżej, żeby jej się lepiej przyjrzeć..."
    
    scene bg fountainnight with dissolve
    stop music fadeout 10.0
    play sound "sfx_footsteps_a.mp3"

    "Im bliżej jesteś do tej fontanny, tym ciszej się robi..."
    "Nie, że wcześniej było głośno w środku nocy."
    "Tylko, że wtedy słychać było wiatr w koronach drzew, żarzące się latarnie na ulicach, szum przelatujących ptaków, ale teraz {b}wszystko{/b} ucichło..."
    "Wszystko oprócz szumu wody w fontannie, który z sekundy na sekundę staje się coraz bardziej uciążliwy i głośniejszy."
    "Powietrze jest gęste i ciężkie, a ty czujesz to wyraźnie..."
    "Nic się nie dzieje. Stoisz tam przez dłuższą chwilę, ale sytuacja nie nabiera tępa i znudziło ci się czekanie, więc postanawiasz wrócić do domu."
    "Wygląda na to, że będziesz musiał wrócić tutaj później."
    "Oddalasz się od fontanny i idziesz do domu."
    scene bg colacocastreetnighta with dissolve
    play music "town_night.mp3" fadeout 10.0
    play sound "sfx_footsteps_b.mp3"
    you "{i}Gdzie ja w ogóle mieszkam?{/i}"
    "Patrzysz na klucz w swojej dłoni."
    "Do klucza jest przypięty mały breloczek, na którym jest napisane ul. króla Aszurnasirpala II."
    "Dzięki plot armor nie masz problemu ze znalezieniem ulicy z breloczka."
    "Na jej długości są tylko trzy domy, a ten na samym końcu jest twój."

    menu:
        "Chcę się przywitać":
            you "Nie chce wyjść na niemiłego, muszę się przywitać."
            "Podchodzisz do pierwszego lepszego domu..."
            you "{i}Czemu ma zamkniętą bramę?{/i}"
            you "{i}Czy to dla mnie zbudowano taki tor przeszkód?{/i}"
            you "{i}Co to ma być? Wipeout?{/i}"
            "Na szczęście jesteś skinny więc po prostu wsadzasz rękę przez pręty bramy i otwierasz ją od środka." 
            "Ale plot armor nie jest taki duży, więc ręka utyka ci w ogrodzeniu. Na szczęście po kilku sekundach ciągnięcia udaje ci się ją wyciągnąć."
            "Gdyby ktoś cię teraz zobaczył, to byś stracił tyle aury..."
            "Próbujesz nonszalancko zamknąć za sobą bramę, ale po przejściu kilku kroków się otwiera."
            you "{i}Głupia brama!{/i}"
            you "{i}Pff... to już nie mój problem{/i}"
            "Dom tego sąsiada jest strasznie nudny, a brak jakichkolwiek roślin w około budynku nie poprawia tej sytuacji."
            "Podchodzisz do drzwi i pukasz do drzwi ― tak samo jakbyś szedł na rozmowę o pracę ― i czekasz."
            "Nikt nie otwiera, więc pukasz jeszcze raz, a dokładniej 3 razy."
            "Znowu nikt nie otwiera..."
            "Zdecydowałeś, że to jednak nie był najlepszy pomysł, żeby robić meet & greet z sąsiadami w nocy. Z tego powodu odwracasz się, żeby odejść, ale słyszysz za sobą ciche skrzypnięcie."
            you "{i}Co to było?!{/i}"
            "Postanawiasz zignorować ten dźwięk i kontynuować podróż do swojego domu."
            "Ale nagle czyjś głęboki i gardłowy głos sprawia, że podskakujesz ze strachu."
            m "Czy mogę ci w czymś pomóc??"
            you "AAAAA!!!"
            #TODO: (S)creaming sound
            "w okamgnieniu odwracasz się i widzisz sąsiada, którego chciałeś odwiedzić ― jeszcze zaspanego."
            show tomcio normal with dissolve
            "Gość jest zbudowany jak byk (i to tak dosłownie) ― wysoki i szeroki."
            you "{i}Whoopsie daisy yoo hoo{/i}"
            you "{i}...{/i}"
            you "{i}No i co mam teraz zrobić???{/i}"
            you "{i}Będę chyba nonchalant.{/i}"
            you "Nie strasz tak ludzi, to bardzo niegrzeczne!"
            m "???"
            m "To nie {b}ty{/b} przypadkiem pukałeś {b}mi{/b} do drzwi i to w {b}środku nocy{/b}???"
            m "Jaki jest powód takiego ― nie ukrywajmy ― niemiłego najścia?!"
            you "No dobra, powiedzmy że masz rację.."
            "Sąsiad jest oszołomiony twoją arogancją i zaczyna patrzeć na ciebie jak spod byka."
            you "Jestem twoim nowym sąsiadem i chciałem się przywitać."
            you "Przepraszam, że chciałem być miły!"
            m "No to cześć?"
            you "{i}Za kogo on mnie ma że tak się do mnie odzywa!{/i}"
            you "Czy to wszystko???"
            m "Ale o czym chcesz gadać, jest prawie północ!!!"
            menu:
                "Zapytaj kim on jest":
                    $ metTomcio = True
                    you "Kim jesteś?"
                    t "Nazywam się Tomcio."
                    you "I to tyle???"
                    you "Opowiedz coś więcej o sobie, np. czym sie zajmujesz."
                    "Tomcio pochylił się bliżej ciebie i popatrzył się na ciebie jeszcze bardziej podejrzliwie niż wcześniej."
                    t "A po co ci ta informacja?"
                    you "{i}Ale dał do pieca...{/i}"
                    you "{i}I zatkało mi kakao...{/i}"
                    you "{i}Aha! {w=0.6}Wiem! {w=0.6}Teraz wszystko wiem! {w=0.6}Wiem jak na to odpowiedzieć! {w=0.6}Wiem wiem wiem! {w=0.6}Eureka!{/i}"
                    you "Chcę się upewnić, że moi sąsiedzi nie szponcą nieleganie."
                    t "Nigdy w życiu nie słyszałem {b}tak{/b} oburzającego stwierdzenia!!!"
                    t "No ale skoro musisz wiedzieć... to pracuję dla rządu."
                    you "Aha, ok."
                    you "Ale nudna praca. Myślałem że coś ukrywasz."
                    you "No to dziękuję ja idę spać."
                    you "DOBRANOC!"
                    hide tomcio normal with dissolve
                    you "{i}Ten tomcio to chyba spoko gość, tylko trochę dziwny. No cóż sąsiadów się nie wybiera, przeżyję.{/i}"

                "Opowiedz mu wszystko o sobie":
                    you "Dobry wieczór."
                    m "Raczej dobranoc!"
                    you "Dobry―a... {w=0.3}noc???"
                    you "Jak pan się nazywa?"
                    you "Yyy... {w=.3}w każdym razie nie ważne. Ja będe pierwszy!!!"
                    you "Pewnie się domyślasz, ale jestem twoim sąsiadem i jestem bardzo szczę..."
                    "On robi krok do tyłu i zamyka ci drzwi przed nosem."
                    hide tomcio normal with vpunch
                    play sound "sfx_door_slam.mp3"

                "Ragebait":
                    $ rudeToTomcio = True
                    you "A w sumie, nie ważne."
                    "Obracasz się na pięcie i zaczynasz uciekać, podskakując."
                    m "CZEKAJ!!!"
                    m "Boże święty...{w=.6} czemu ty ode mnie uciekasz???"
                    m "Czy ja naprawdę...{w=.6} jestem taki groźny???"
                    m "Czy to przez to{w=.6}, że jestem gruby???"
                    "On wpada w malignę, zaczyna płakać i zamyka drzwi."
                    hide tomcio normal with dissolve
                    you "{i}???{/i}"
                    you "Nie mam {b}ZIELONEGO{/b} pojęcia co się właśnie stało, chyba pora na sen."
            "Wychodzisz przez bramę, spoglądając przy tym przez ramię by upewnić się, że sąsiad cie nie goni i idziesz do domu."
        "Chcę iść spać":
            you "Zmęczyłem się"
            "Czym niby??? Ale ok."
    "Dom był niedaleko, więc szybko trafiłeś pod drzwi swojego nowego lokalu."
    "Nie wyglądał on przytulnie, ale teraz jest za późno na takie rozmyślania."
    "Zanim się obejrzałeś to byłeś już w domu pod kołdrą."
    stop music fadeout 1.0
    scene black with dissolve
    jump ch02_watch_your_mouth


label ch01_firstNightTownWalk:
    $ receivedLoreAboutChurchOnTheFirstDay = True
    scene bg lanastreetnight with dissolve
    jump ch01_firstNightTownWalkPartB

# ch01_m_enteringChurch goes here and i dont want lanastreet in the bg
label ch01_firstNightTownWalkPartB:
    "Gdy już postanawiasz spuścić wzrok z tego pięknego zabytku architektury, widzisz...{w=.1} kogoś."
    you "{i}W KOŃCU!{/i}"
    you "{i}Pierwszy raz widzę kogoś na tej ulicy.{/i}"
    "Nie jesteś pewien czy chcesz do tej osoby podejść i porozmawiać czy raczej unikać."
    you "{i}Mam nadzieję, że mnie nie ten ktoś nie pobije.{/i}"
    "Aż w końcu tajemnicza osoba macha do ciebie i gestem zachęca abyś podszedł bliżej."
    you "{i}Czego onx chce???{/i}"
    "Podchodzisz bliżej do tajemniczej sylwetki przed kościołem, zachowując przy tym wszystkie środki bezpieczeństwa."
    show wp normal with dissolve
    you "Dobry wieczór...?"
    m "Czy my się znamy?"
    you "Nie wydaję mi się."
    m "Ty nie pracujesz przypadkiem po drugiej stronie miasta?"
    you "No nie, bo jestem tutaj nowy!"
    m "Aha."
    m "No to cześć."
    you "..."
    m "..."
    you "..."
    $ metWiktoriaP = True
    wp "Mam na imię Wiktoria."
    you "Miło cię poznać! Mam na imię [name]."
    "Uśmiechasz się jak w reklamie nieruchomości."

    $ newName = name.strip().split(" ")[0].lower()#  "Dupa 3.0" -> "dupa"

    wp "No właśnie miałam mówić, że wyglądasz na [newName]."
    wp "Masz fajne imię."
    wp "[name] [name] [name]"
    "Rzucasz jej surowe spojrzenie ― niemalże piorunujesz ją wzrokiem."
    wp "Skoro już tu jesteś to mogę równie dobrze opowiedzieć ci coś o tym mieście."
    scene bg churchnighta with dissolve
    show wp normal at leftish with moveinleft
    "Wiktoria otwiera bramę przed kościołem, żeby umożliwić ci bliższe obejźrnięcie."
    "Zrobiłeś tylko 3 kroki do przodu, więc twój widok niewiele się zmienił."
    "(Czego się spodziewałeś?)"
    wp "Wiesz, że Bjork jest założycielką naszego miasta?"
    you "No tak, kurowska mi o niej mówiła. Założyła nasze miasto jakieś czterysta lat temu."
    wp "Nie do końca. Bjork założyła nasze miasto 399 lat temu a 400 rocznica będzie obchodzona podczas tegorocznych zielonych świątek."
    you "Wow! Ale heca."
    wp "No rel. Bjork to islandzka podróżniczka która to wszystko zaczęła."
    wp "Była zwykłą kobietą ― jak większość kobiet tutaj w bratgren."
    wp "Pewnego dnia Bjork obudziła się i miała wizję, w której pojawiła się dusza, która coś jej tam wyszeptała."
    "Wiktoria wskazuje na witraż. Patrzysz na niego i dopiero z tą narracją uświadamiasz sobie, że to duch."
    "Wpatrujesz się w witraż próbując obejrzeć go pod różnymi kątami."
    wp "Czy coś jest nie tak?"
    you "Nie, nie to nic."
    wp "Bjork zrobiła ten witraż swoimi rękami."
    you "Aha teraz ma sens czemu jest taki..."
    "Patrzy sie na ciebie jakbyś właśnie zabił starą lichwiarkę i jej siostrę."
    "{i}Może lepiej nie obrażać ich wierzeń...{/i}"
    with vpunch
    # TODO: *gulp* - dodaj dźwięk a nie takie chyry byry mi tutaj robisz
    you "...{w=.3} Tzn ma taki...{w=.6} unikalny styl ― nigdy wcześniej czegoś takiego nie widziałem."
    wp "{b}No ja myślę!{/b}"
    wp "Ale wracając, nikt nie wie co ta dusza tam wyszeptała do Bjork, a ten witraż to jedyna interpretacja szeptu jaką mamy."
    wp "Po spotkaniu z tą duszą jej serce wypełniło się determinacją, więc poszła szukać miejsca z najlepszym vibem."
    wp "Bjork dużo pisała w swoim dzienniku."
    wp "Pierwsze co napisała to \"If travel is searching, and home what's been found, im not stopping.\""
    wp "Zaczęła podróżować po całym świecie w poszukiwaniu idealnego miejsca na miasto."
    you "Wow! Ale diva."
    wp "No rel ona była taką {b}final girl{/b}."
    you "Ej, rell."
    wp "A wiesz co po tych podróżach zrobiła?"
    you "Nie."
    wp "Ale to było pytanie retoryczne..."
    "-1000 aury!"
    you "No dobra mów już!"
    wp "Szła tu gdzieś przez las, gdy poczuła taki mega fajny vibe."
    wp "Zorientowała się od razu, że ten vibe był lepszy niż wszystkie i od razu wiedziała że to miejsce nadaje się na miasto."
    wp "Ale ostatnio ta tarcza osłabła i czarodzieje tacy jak Piotr muszą pomagać nam chronić Bratgren."
    you "Właśnie obudziłem się pierwszy raz obok Piotra, jak robił jakiś rytuał."
    wp "Serio?"
    you "Noooo..."
    you "Od razu myślałem, że to jego wina i wgl masakra z nim."
    you "Ale chyba jest spoko..."
    wp "No fajny jest on wszystkim pomaga."
    you "Weź bo teraz wyszedłem na niemiłego..."
    wp "No to przeproś go?"
    $ hasToApologiseToPiotr = True
    you "No, no przeproszę..."
    you "No ale dobra, wracając do tej Bjorkowej."
    you "Ona to miasto sama zbudowała?"
    wp "Nie no, oczywiście, że nie."
    wp "Po pierwsze, wtedy miasto było dużo mniejsze. Minęło w końcu czterysta lat, trochę się rozrosło."
    wp "A po drugie, nie była sama..."
    you "OKEJ...??"
    wp "Była jeszcze{w=.3} Sabrina Carpenter."
    "Nie wiesz czemu, ale to imię brzmi znajomo, chociaż nikt nigdy ci go nie wspominał."
    "To bardzo dziwne i cię trochę niepokoi."
    you "{i}Gdzieś to imię już słyszałem...{/i}"
    you "{i}Czemu ja ją kojarzę?{/i}"
    you "{i}Chyba jest ważna!{/i}{nw}"
    wp "Halo, czy ty mnie w ogóle słuchasz?"
    you "Yyy... tak, tak mów."
    wp "A więc to była najlepsza przyjaciółka Bjork i też jakby ironicznie cieśla."
    wp "Zbudowały kilka domów i ludzie zaczęli się pojawiać ― tak jak ty."
    wp "I tak w ogóle to do dziś nie wiadomo skąd ci ludzie się biorą."
    you "Nawet Bjork nie wiedziała?"
    wp "No{w=.3} nie."
    wp "A teraz plot twist! Zgadnij jak ona umarła..."
    you "Została łysa?"
    wp "Co?{w=.3} Nie?"
    wp "Jej śmierć była {b}BARDZO{/b} tragiczna."
    wp "Była prezydentem tylko 23 lata kiedy sabrina ją zdradziła i dźgnęła nożem!!!"
    you "{i}A teraz {b}mi{/b} jest łyso, bo nie wiedziałem tego faktu.{/i}"
    you "{i}Wiedziałem, że sabrina jest ważna!!!{/i}"    
    wp "Zginęła w aktualnym biurze kurowskiej. Dokładnie tam, gdzie ona teraz siedzi."
    wp "Ostatnie słowa Bjork były \"I thought I could organize freedom. How scandinavian of me...\""
    wp "To był tragiczny dzień dla całego miasta i od tamtej pory co rok duchy powstają z martwych."
    you "{i}Mam tyle pytań...{/i}"
    jump ch01_firstNightTownWalkQuestionsMenu

label ch01_firstNightTownWalkQuestionsMenu:
    if askedAboutSabrina and askedAboutBjorkDeath and askedAboutGhostsTalking:
        jump ch01_afterFirstNightTownWalkQuestionsMenu

    menu:
        "Co się stało z sabriną" if not askedAboutSabrina:
            $ askedAboutSabrina = True
            wp "Ona była w gorącej wodzie kąpana po tym jak zabiła Bjork..."
            wp "W sensie nie było wody, a tylko temperatura{w=.6} ― została spalona na stosie."
            you "Ej szczerze ― też bym ją spalił za to."
            wp "No, rel!"
            you "No, ale czekaj..."
            you "Czemu Sabrina ją zdradziła???"
            wp "Nikt nie wie."
            wp "Ale chyba była delulu."
            you "{i}Czemu nikt w tym mieście nie pamięta {b}NAJWAŻNIEJSZYCH{/b} rzeczy z historii, to jest takie dziwne...{/i}"
            jump ch01_firstNightTownWalkQuestionsMenu 
        "Jak umarła Bjork" if not askedAboutBjorkDeath:
            $ askedAboutBjorkDeath = True
            wp "Bjork była z Islandii, no co nie?"
            you "Mnie się pytasz?!"
            wp "Dobra nie ważne!"
            wp "No to chcieliśmy uczcić tradycje tego kraju kiedy ona umarła."
            wp "Ciało Bjork zostało położone na łodzi, którą wypuszczono na wyjątkowo spokojne jezioro Świtezianka."
            you "Czemu położyliście ją na łódzi."
            wp "Jezu czy ty mnie słuchasz...{w=.3} Mówiłam, że takie są tradycje!"
            you "No, dobra już...{w=.3} I to wszystko?"
            wp "A no tak ― zapomniałam najważniejszej rzeczy!"
            wp "Ogólnie mieliśmy podpalić tę łódkę, ale jakaś siła wciągnęłą ją pod wodę..."
            you "Jak można o czymś takim zapomnieć???"
            jump ch01_firstNightTownWalkQuestionsMenu
        "Czy mogę rozmiawiać z tymi duchami" if not askedAboutGhostsTalking:
            $ askedAboutGhostsTalking = True
            wp "PO PIERWSZE...{w=.6} To nie są duchy tylko dusze ― wkurzą się jeśli nazwiesz je duchami."
            you "{i}Duchy i dusze to prawie to samo. Przecież mnie nie ukrzyżują jak ich zmisgenderuje...{/i}"
            you "Ups, przepraszam nie wiedziałem."
            wp "Nic się nie dzieje..."
            wp "I tak, możesz z nimi rozmawiać, ale tylko podczas tego festiwalu."
            wp "A właściwie to one mogą mówić tylko przez te siedem dni."
            wp "Jednak nie bój żaby ― bo możesz je zobaczyć przez cały rok ― ale nie będą cię nawiedzać."
            jump ch01_firstNightTownWalkQuestionsMenu

label ch01_afterFirstNightTownWalkQuestionsMenu:
    you "Czy jest coś jeszcze, co powinienem wiedzieć?"
    wp "Tak, zapomniałam ci powiedzieć, czemu w ogóle opowiadam ci o tym kościele."
    you "Słucham?"
    wp "W tym kościele jest mnóstwo relikwii.{w=.3} Na przykład nóż, którym zabito Bjork."
    wp "Teraz jest zamknięty, ale jeśli kiedyś będziesz potrzebować odpowiedzi, znajdziesz je tutaj."
    you "Aha, dobra, dzięki."
    "Opuszczasz teren kościoła, a Wiktoria zamyka za tobą bramę."
    "Zrobiłeś tylko 3 kroki do tyłu więc twój widok niewiele się zmienił."
    "(Czego się spodziewałeś?)"
    you "To tyle informacji naraz..."
    you "Na pewno do jutra wszystko zapomnę."
    wp "Ej, rell!!!"
    wp "Tak szczerze, sama nie wiem jak ja to pamiętam."
    wp "W każdym razie, jeśli będziesz czegoś potrzebować, jestem tu, żeby pomóc."
    you "Aww, dziękuję."
    you "Dobra to teraz mi powiedz, która jest godzina?"
    wp "No jest już po północy."
    you "Czemu ty łazisz an rynku po północy???"
    wp "Yyyy...{w=.6} Nie interesuj się!"
    you "{i}SUSPICIOUS BEHAVIOUR{/i}"
    you "Myślę, że najlepiej już pójdę do domu. Jeszcze go nawet nie widziałem."
    wp "Czekaj, jaki dom???{w=.6} Skąd???"
    you "Dom{w=.6}, który dostałem od Kurowskiej?"
    wp "CO?"
    wp "Jak to dostałeś, dom???"
    "Pokazujesz jej klucze, które się okazują mocno spocone od twojej ręki."
    you "No, od Kurowskiej dostałem."
    wp "Czemu ona teraz magicznie ma swoich ulubieńców?"
    you "Może mi ktoś wytłumaczyć, co się dzieje???"
    wp "Kurowska zwykle nie rozdaje domów za darmo."
    you "To nie było za darmo, powiedziała, że muszę znaleźć pracę."
    wp "Aaaa, ona trochę nie lubi bezrobotnych."
    wp "Cokolwiek robisz, pamiętaj, żeby płacić podatki. Wtedy będziesz miał z nią spokój."
    wp "Jest miła tylko dla tych, co je płacą."
    you "Oho, okej."
    you "Dziękuję ci za wszystkie informacje, bardzo to doceniam, ale teraz chciałbym się położyć."
    you "Dobranoc."
    wp "Pa."
    $ fountainLoreReceived = True
    scene bg citysquarenight with dissolve
    "Zaczynasz iść do domu. Głowa ciąży ci od nadmiaru informacji, które właśnie otrzymałeś."
    "Z wiązku z ciężkim dniem, nie myślisz nad niczym innym niż snem. Z tego powodu od razu kładziesz się spać."
    jump ch02_watch_your_mouth

label ch01_lakeVisit:
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
    jump ch01_vasiliFirstNightMagaMenu

label ch01_vasiliFirstNightMagaMenu:
    menu:
        "Zapytaj jaką ma wiedzę na temat ryb":
            $ ryba = random.choice(["ch01_vasiliFishBrzana", "ch01_vasiliFishKoza", "ch01_vasiliFishWstegorz"])
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
                    jump ch01_vasiliFirstNightMagaMenu
                "Nie, dziękuję":
                    $ friendship["Vasili"] -= 1
                    v "Wiedziałem, że będziesz popierał kapitalizm!"
                    v "W takim razie proszę opuścić teren naszego domu!!!"
                    you "To jak to działa, że mówisz że to nasz dom ale mnie wyganiasz?"
                    v "Idź popieraj kapitalizm gdzieś indziej."
                    hide vasili with dissolve
                    "Odwracasz się i idziesz jak najszybciej od niego bo nie wytrzymasz kolejnego "towarzysza"."
                    jump ch01_goingHomeTiredAfterVasiliFirstNight

            
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
            
            jump ch01_goingHomeTiredAfterVasiliFirstNight

label ch01_goingHomeTiredAfterVasiliFirstNight:
    "Przez zmęczenie droga do domu trwała wieki, ale nic nie było widać, ponieważ oszczędzają przez wyłączanie latarni."
    "Pomimo braku widoczności przejscie do domu nie sprawiło ci dużo trudu."
    jump ch02_watch_your_mouth

label ch01_vasiliFishBrzana:
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
    jump ch01_vasiliAfterFishMonologue

label ch01_vasiliFishKoza:
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
    jump ch01_vasiliAfterFishMonologue

label ch01_vasiliFishWstegorz:
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
    jump ch01_vasiliAfterFishMonologue

label ch01_vasiliAfterFishMonologue:
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
                    jump ch02_watch_your_mouth
                "Zaprezentuj wymówkę i zostań.":
                    you "Nie... tylko chciałem się przejść, bo mnie nogi bolą."
                    you "Poza tym noc jest tak piękna, że aż szkoda ją przespać."
                    v "Masz rację, ale wiesz co? Jeszcze nie opowiedziałem ci o mojej ULUBIONEJ rybie...."
                    jump ch01_vasiliTalksAboutFavoriteFish

        "Wysłuchaj wykładu.":
            you "Znasz może więcej ryb?"
            v "{b}OCZYWIŚCIE{/b}, opowiem ci o mojej {b}ULUBIONEJ{/b} rybie..."
            jump ch01_vasiliTalksAboutFavoriteFish
    
label ch01_vasiliTalksAboutFavoriteFish:
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
    jump ch02_watch_your_mouth