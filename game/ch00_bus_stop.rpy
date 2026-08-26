label ch00_bus_stop:
    play music "audio/street.mp3" 
    scene bg busstopa with dissolve

    you "{i}No szybciej już{/i}"
    "Szybko, nerwowo, impulsywnie oraz intensywnie wciskasz przycisk na światłach (ten taki żółty)."
    "Wczoraj naprawiali światła właśnie na tym przejściu i ewidentnie coś zepsuli."
    "{cps=1}...{/cps}"
    "Stoisz na tym przejściu z minutę, a światła dalej są czerwone."
    you "{i}Zostały mi tylko 2 minuty, a muszę jeszcze iść do baru {w=.5}po matchę.{/i}"
    you "{i}Jeśli jeszcze raz się spóźnię to obniżą mi zachowanie.{/i}"
    "{cps=1}...{/cps}"
    you "{i}O dobra mam zielone mogę przejść!{/i}"

    show bus at center

    mks "Ohayoooo!!!!"

    window hide

    play sound "audio/hit_by_bus.mp3"
    show bus:
        linear 3.0 zoom 3.0
    pause 2.5
    you "AAAAAAAAAAAAAAAAAAA{nw}"
    scene black

    pause 3.0
    stop music fadeout 2.0
    window show

    jump ch01_cold_boot

    