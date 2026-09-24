label ch00_bus_stop:
    play music "audio/street.mp3" 
    scene bg busstop with dissolve

    
    you "{i}Oh my god can this light even turn green???{/i}"
    "You already pushed the big yellow button to cross the street,"
    "So clicking it twenty more times shouldn't help it in any way."
    "According to you, it absolutely should."
    "{cps=1}...{/cps}"
    "It's now been about thirty seconds, which is completely absurd"
    "Yesterday there was a construction crew replacing the traffic lights, and clearly, they messed something up."
    "You reach for your phone to check the time, which proudly displayed 7:53."
    you "{i}Great. I have two minutes, in which I have to not only get to class, but first go to the cafeteria {w=.5}to buy matcha.{/i}"
    you "{i}If I come to class late one more time they will change my behavior grade.{/i}"
    "You hit the button a bunch more times out of desperation.{w=.5}"
    "{cps=1}...{/cps}"
    "!"
    "The traffic light on the other side of the street turns green without any warning, and you don't even check if there are any cars coming."
    "You just run like a fool."

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
    stop sound fadeout 0.5

    jump ch01_cold_boot

    