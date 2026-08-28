default _map_loc = None
default _map_dest = None

define location_bgs = {
    "square": ("bg citysquareday", "bg citysquarenight"),
    "lanastreet": ("bg lanastreetday", "bg lanastreetnight"),
    "lakeslope": ("bg cityslopedownday", "bg cityslopedownday"), #TODO: cityslopedownnight does not exist
}

default minutesToTravel = 5

init python:
    def loc_bg(loc):
        day_img, night_img = location_bgs[loc]
        return day_img if time.isDay() else night_img

    def travel_to(screen_name):
        time.advanceTime(minutes=minutesToTravel)
        if time.hour >= 18:
            renpy.jump("too_late")
        else:
            renpy.show_screen(screen_name)
            renpy.transition(dissolve)

screen s_walkable_Square():
    tag map

    add loc_bg("square")
    vbox:
        xpos 0.08 ypos 0.75
        imagebutton:
            idle "ui/square_left.png"
            hover "ui/square_left_hover.png"
            action Function(travel_to, "s_walkable_LanaStreet")
            
    vbox:
        xpos 0.25 ypos 0.6
        imagebutton:
            idle "ui/square_lake.png"
            hover "ui/square_lake_hover.png"
            action Function(travel_to, "s_walkable_LakeSlope")


screen s_walkable_LanaStreet():
    tag map

    add loc_bg("lanastreet")
    vbox:
        xpos 0.5 ypos 0.8
        imagebutton:
            idle "ui/back_to_square_a.png"
            hover "ui/back_to_square_a_hover.png"
            action Function(travel_to, "s_walkable_Square")
    vbox:
        xpos 0.25 ypos 0.6
        imagebutton:
            idle "ui/to_church.png"
            hover "ui/to_church_hover.png"
            action [SetVariable("_map_loc", "lanastreet"), SetVariable("_map_dest", "test_church"), Jump("map_leave")]
    vbox:
        xpos 0.8 ypos 0.67
        imagebutton:
            idle "ui/to_bakery.png"
            hover "ui/to_bakery_hover.png"
            action [SetVariable("_map_loc", "lanastreet"), SetVariable("_map_dest", "test_bakery"), Jump("map_leave")]


screen s_walkable_LakeSlope():
    tag map

    add loc_bg("lakeslope")
    vbox:
        xpos 0.1 ypos 0.85
        imagebutton:
            idle "ui/back_to_square_a.png"
            hover "ui/back_to_square_a_hover.png"
            action Function(travel_to, "s_walkable_Square")

label map_leave:
    scene expression loc_bg(_map_loc)
    jump expression _map_dest

label too_late:
    "its too late to be outside"
    jump ch02_watch_your_mouth


label test_bakery:
    scene bg bakeryfrontday with dissolve
    menu:
        "go in":
            scene bg citysquareday with dissolve
            "you got le buns and ate them while watching the fountain"
            call screen s_walkable_Square()
        "No":
            scene bg lanastreetday with dissolve
            call screen s_walkable_LanaStreet()


label test_church:
    "test_church"
    return