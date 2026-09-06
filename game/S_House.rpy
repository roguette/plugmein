screen b_normal(pos, label):
    imagebutton:
        idle "images/buttons/normal.png"
        hover "images/buttons/normal_hover.png"
        action Jump(label)
        xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5

screen b_important(pos, label):
    imagebutton:
        idle "images/buttons/important.png"
        hover "images/buttons/important_hover.png"
        action Jump(label)
        xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5

screen b_disabled(pos):
    imagebutton:
        idle "images/buttons/disabled.png"
        xpos pos[0] ypos pos[1] xanchor 0.5 yanchor 0.5


define buttons_ch01 = dict(
    bathroom=(0.279, 0.273),
    bedroom=(0.649, 0.225),
    storage_room=(0.424, 0.168),
    entrance=(0.484, 0.856),
    kitchen=(0.358, 0.691),
    living_room=(0.608, 0.641),
) 

define buttons_ch02 = dict(
    entrance=(0.486, 0.863),
    window=(0.34, 0.878),
    fridge=(0.342, 0.469),
    table=(0.359, 0.697),
    sink=(0.236, 0.678),
    suspicious_pot=(0.738, 0.563),
    normal_pot=(0.742, 0.762),
    bathroom=(0.282, 0.252),
    pantry=(0.411, 0.177),
    bed=(0.661, 0.211),
    wardrobe=(0.54, 0.18),
)

screen s_House():
    tag map
    add loc_bg("house")

    if time.chapter == 1:
        if flag("ch01_house_seenEntrance"):
            use b_normal(buttons_ch01["bathroom"], "ch01_h_bathroom")
            use b_normal(buttons_ch01["bedroom"], "ch01_h_bedroom")
            use b_normal(buttons_ch01["storage_room"], "ch01_h_storageRoom")
            use b_normal(buttons_ch01["kitchen"], "ch01_h_kitchen")
            use b_normal(buttons_ch01["living_room"], "ch01_h_livingRoom")
            use b_disabled(buttons_ch01["entrance"])
        else:
            use b_normal(buttons_ch01["entrance"], "ch01_h_entrance")
    elif time.chapter == 2:
        use b_normal(buttons_ch02["entrance"], "ch02_h_entrance")
        use b_normal(buttons_ch02["window"], "ch02_h_window")
        use b_normal(buttons_ch02["fridge"], "ch02_h_fridge")
        use b_normal(buttons_ch02["table"], "ch02_h_table")
        use b_normal(buttons_ch02["sink"], "ch02_h_sink")
        use b_normal(buttons_ch02["suspicious_pot"], "ch02_h_suspicious_pot")
        use b_normal(buttons_ch02["normal_pot"], "ch02_h_normal_pot")
        use b_normal(buttons_ch02["bathroom"], "ch02_h_bathroom")
        use b_normal(buttons_ch02["pantry"], "ch02_h_pantry")
        use b_normal(buttons_ch02["wardrobe"], "ch02_h_wardrobe")

label generic_unavailable_house:
    scene expression loc_bg("house")
    "There's nothing to do here at this moment"
    call screen s_House()
