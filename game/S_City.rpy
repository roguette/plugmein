default _map_loc = None
default _map_dest = None

init python:

    def travel_to(screen_name):
        renpy.show_screen(screen_name)
        renpy.transition(dissolve)

screen s_walkable_Square():
    tag map

    add loc_bg("square")
    vbox:
        # lana street arrow
        xpos 0.08 ypos 0.75
        imagebutton:
            idle "images/arrows/270_b.png"
            hover "images/arrows/270_b_hover.png"
            action Function(travel_to, "s_walkable_LanaStreet")
            
    vbox:
        # field slope arrow
        xpos 0.25 ypos 0.6
        imagebutton:
            idle "images/arrows/0_a.png"
            hover "images/arrows/0_a_hover.png"
            action Function(travel_to, "s_walkable_LakeSlope")

    vbox:
        # city hall arrow
        xpos 0.45 ypos 0.68
        imagebutton:
            idle "images/arrows/0_a.png"
            hover "images/arrows/0_a_hover.png"
            action [SetVariable("_map_loc", "square"), SetVariable("_map_dest", "city_hall"), Jump("map_leave")]

    vbox:
        # fountain arrow
        xpos 0.61 ypos 0.87
        imagebutton:
            idle "images/arrows/45_b.png"
            hover "images/arrows/45_b_hover.png"
            action [SetVariable("_map_loc", "square"), SetVariable("_map_dest", "fountain"), Jump("map_leave")]


screen s_walkable_LanaStreet():
    tag map

    add loc_bg("lanastreet")
    vbox:
        # back to the square arrow
        xpos 0.5 ypos 0.9
        imagebutton:
            idle "images/arrows/180_a.png"
            hover "images/arrows/180_a_hover.png"
            action Function(travel_to, "s_walkable_Square")
    vbox:
        # church arrow
        xpos 0.25 ypos 0.6
        imagebutton:
            idle "images/arrows/270_b.png"
            hover "images/arrows/270_b_hover.png"
            action [SetVariable("_map_loc", "lanastreet"), SetVariable("_map_dest", "church"), Jump("map_leave")]
    vbox:
        # bakery arrow
        xpos 0.8 ypos 0.67
        imagebutton:
            idle "images/arrows/90_a.png"
            hover "images/arrows/90_a_hover.png"
            action [SetVariable("_map_loc", "lanastreet"), SetVariable("_map_dest", "bakery"), Jump("map_leave")]

    if time.chapter == 1:
        vbox:
            # wiktoria p
            xpos 0.4 ypos 0.42
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                idle "wp silhouette"
                action [SetVariable("_map_loc", "lanastreet"), SetVariable("_map_dest", "ch01_firstNightTownWalk"), Jump("map_leave")]



screen s_walkable_LakeSlope():
    tag map

    add loc_bg("lakeslope")
    vbox:
        # back to square arrow
        xpos 0.1 ypos 0.85
        imagebutton:
            idle "images/arrows/180_a.png"
            hover "images/arrows/180_a_hover.png"
            action Function(travel_to, "s_walkable_Square")

    vbox:
        # field arrow
        xpos 0.49 ypos 0.42
        imagebutton:
            idle "images/arrows/0_a.png"
            hover "images/arrows/0_a_hover.png"
            action Function(travel_to, "s_walkable_LakeField")

screen s_walkable_LakeField():
    tag map
    
    add loc_bg("lakefield")

    vbox:
        xpos 0.2 ypos 0.9
        imagebutton:
            idle "images/arrows/180_b.png"
            hover "images/arrows/180_b_hover.png"
            action Function(travel_to, "s_walkable_LakeSlope")

    vbox:
        xpos 0.5 ypos 0.5
        imagebutton:
            idle "images/direction_sign.png"
            action [SetVariable("_map_loc", "lakefield"), SetVariable("_map_dest", "lake_direction_sign"), Jump("map_leave")]
    

label map_leave:
    scene expression loc_bg(_map_loc)
    jump expression _map_dest

# ======================================== exit labels

label lake_direction_sign:
    menu:
        "Lake ↑":
            if time.chapter == 1:
                jump ch01_lakeVisit
            else:
                call generic_unavailable
        "Vasili's house →":
            call generic_unavailable
        "Niuniu's house →":
            call generic_unavailable

    call screen s_walkable_LakeField() with dissolve


default ch01_f_visitedFountain = False
label fountain:
    if time.chapter == 1:
        if ch01_f_visitedFountain == False:
            call ch01_m_fountainFirstClick
            $ ch01_f_visitedFountain = True
        else:
            call ch01_m_fountainSecondClick
    else:
        call generic_unavailable
    
    call screen s_walkable_Square() with dissolve

default ch01_f_wentToCityHall = False
label city_hall:
    if time.chapter == 1:
        if rudeToKurowska == True:
            call ch01_m_cityHallRudeToKurowska
        else:
            if ch01_f_wentToCityHall == False:
                $ ch01_f_wentToCityHall = True
                call ch01_m_cityHallNormalFirstInteraction
            else:
                "Filip is very busy. I shouldn't be bothering him right now"

    else:
        call generic_unavailable

    call screen s_walkable_Square() with dissolve


label church:
    if time.chapter == 1:
        # jumping because y/n wont go back to the map after this
        jump ch01_m_enteringChurch
    else:
        call generic_unavailable
    call screen s_walkable_LanaStreet() with dissolve

default ch01_f_triedBakery = False
label bakery:
    if time.chapter == 1:
        if ch01_f_triedBakery == False:
            "The bakery is now closed (duh)"
            "You can see countless pastries behind it and your stomach growls"
            "You will have to come back tomorrow"
            $ ch01_f_triedBakery = True
        else:
            call generic_unavailable
    else:
        call generic_unavailable
    call screen s_walkable_LanaStreet() with dissolve


label generic_unavailable:
    "There's nothing to do here at this moment"
