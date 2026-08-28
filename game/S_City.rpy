default _map_loc = None
default _map_dest = None

define location_bgs = {
    "square": ("bg citysquareday", "bg citysquarenight"),
    "lanastreet": ("bg lanastreetday", "bg lanastreetnight"),
    "lakeslope": ("bg cityslopedownday", "bg cityslopedownday"), #TODO: cityslopedownnight does not exist
    "lakefield": ("bg lakedaya", "bg lakedayb")
}



init python:
    def loc_bg(loc):
        day_img, night_img = location_bgs[loc]
        return day_img if time.isDay() else night_img

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
        xpos 0.5 ypos 0.8
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
        xpos 0.1 ypos 0.85
        imagebutton:
            idle "images/arrows/180_a.png"
            hover "images/arrows/180_a_hover.png"
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
            "There's nothing to do there at this moment"
        "Vasili's house →":
            "There's nothing to do there at this moment"
        "Niuniu's house →":
            "There's nothing to do there at this moment"

    call screen s_walkable_LakeField()

label fountain:
    "There's nothing to do near the fountain at this moment"
    call screen s_walkable_Square()

label city_hall:
    "There's nothing to do in the town hall at this moment"
    call screen s_walkable_Square()

label church:
    "There's nothing to do at the church at this moment"
    call screen s_walkable_LanaStreet()

label bakery:
    "There's nothing to do in the bakery at this moment"
    call screen s_walkable_LanaStreet()

