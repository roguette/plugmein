define seenBjorkGhost = False
label wakingUpAfterFirstNight:
    "Zanim się obejrzałeś to byłeś już w domu pod kołdrą."
    stop music fadeout 1.0
    scene black with dissolve

    if fountainLoreReceived != True:
        play music "sb_soulsearcher.mp3"
        "Jesteś bardzo głodny, ale nie aż tak, żeby przez to nie spać"
        "I zanim się obejrzysz, już śpisz"

        "A czekaj... już nie"
        "Czujesz, jakbyś leciał przez swoje łóżko"
        "Potem przez podłogę"
        "Aż w końcu lądujesz w wodzie"
        "Nagła zmiana temperatury sprawia że podskakujesz"
        "Otwierasz oczy i widzisz, że jesteś w fontannie na rynku"
        you "{i}Z tą głupią fontanną zawsze jest coś{/i}"
        "Przed tobą pojawia się dusza"
        m "Fontanna nie jest głupia"
        you "{i}Jeśli this ho czyta moje thoughts to się zesram to jest crazy{/i}"
        m "Spokojnie. Nie defekuj. Nie jestem złą duszą"
        "Postanawiasz coś powiedzieć normalnie, bo się robi niezręcznie"
        "I wygląda to jak jakaś relacja parasocjalna"
        "Taka jak na twitchu"
        you "Kim pani jest"
        m "Ty wiesz kim ja jestem."
        you "Aha to ty jesteś B-{nw}"
        bjork "Tak, {w=0.6}jestem Bjork"
        pause 5
        you "Czego ty ode mnie chcesz?"
        bjork "A czego TY ode mnie chcesz?"
        pause 3
        you "Dlaczego ja tu jestem i nic nie pamiętam"
        bjork "Odpowiedź na wszystkie pytania znajdziesz w kościele"
        you "{i}Jezu to po co ona się mnie pytała{/i}"
        bjork "Słyszałam to."
        bjork "Nie potrafię opisać wszystkiego, co musisz zobaczyć, poczuć i zrozumieć"
        bjork "Musisz samemu to wszystko zobaczyć"
        bjork "Nie jesteś głupi i wszystko zrozumiesz"
        bjork "To od ciebie zależy, czy pomożesz miastu, czy doprowadzisz do jego upadku"
        "w okamngnieniu wracasz do swojego łóżka"
        $ seenBjorkGhost = True
        stop music fadeout 0.5

    ".{w=0.5}.{w=0.5}.{w=0.5}"
    "Budzisz się i ponieważ jest już rano możesz lepiej przyjrzeć się swojemu domowi."
    scene bg house with fade
    play music ""
    "Ten dom jest mały (ale dla ciebie jest ogromny bo jest skinny i ma skinny waist)"
    "Prawdopodobnie spałeś jakieś 10 godzin i był to najlepszy sen w Twoim życiu"
    "Jednak obudziło Cię uczucie głodu"
    "Od wczoraj nic nie jadłeś, ale dzisiaj musisz coś z tym zrobić, żeby nie umrzeć z głodu"
    "W mieście jest jedna osoba, która może ci teraz pomóc - Filip"
    "Prawdopodobnie właśnie pracuje, więc postanawiasz udać się prosto do niego"
    scene bg citysquareday with dissolve
    play sound "sfx_footsteps_b.mp3"
    "Wchodzisz na rynek i widzisz wielu przechodniów, co kontrastuje z wczorajszą nocą, kiedy na zewnątrz nie było nikogo."  
    "Jednak nikt nie odważy się zbliżyć do fontanny."
    "Patrzysz w górę i dziwisz się, że nie widzisz słońca"
    "Ludzie są prawdopodobnie przyzwyczajeni do niekończących się chmur stratus pokrywających niebo"
    "Nie ma czasu do stracenia i wchodzisz do ratusza, szukając Filipa"
    "Wchodzisz do jego biura i widzisz go, zmęczonego, przeglądającego dokumenty"

