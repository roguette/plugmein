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
        stop music fadeout 0.5





    "Budzisz się i ponieważ jest już rano możesz lepiej przyjrzeć się swojemu domowi."
    "Ten dom jest mały (ale dla y/n jest ogromny bo jest skinny i ma skinny waist)"