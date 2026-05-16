label c_enteringChurch:
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
    jump t_goingBackToTheBakeryAfterEscapingChurch