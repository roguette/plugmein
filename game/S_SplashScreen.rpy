
transform splash_grow:
    alpha 0.0
    zoom 0.99
    linear 3 alpha 1.0 zoom 1.01
    linear 3 alpha 1.0 zoom 1.02
    linear 3 alpha 0.0 zoom 1.03

init  -1 python:
    quotes = [
        "Singing is like a celebration of oxygen",
        "I am a grateful grapefruit",
        "Everything that a guy says once, you have to say five times",
        "There's more to Life than this",
        "I do believe sometimes discipline is very important.\nI'm not just lying around like a lazy cow all the time",
        "People are always asking me about eskimos, but there are no eskimos in Iceland",
        "I thrive best hermit style.\nWith a beard and a pipe",
        "I'd done three solo albums in a row, and that's quite narcissistic"
    ]

    def intro_random_quote():
        return f"\"{random.choice(quotes)}\"\n- Bjork \n\n\n REPORT ISSUES ON GITHUB!!!!!"

screen S_StartMessage():
    add Solid("#f6f4f1")
    text intro_random_quote():
        size 24
        color "#1a1a1a" 
        xpos 0.5 ypos 0.5 
        xanchor 0.5 yanchor 0.5 
        at splash_grow


label splashscreen:
    show screen S_StartMessage
    pause 9 
    hide screen S_StartMessage with dissolve

    show image "images/backgrounds/titlescreen.png" with dissolve

    return