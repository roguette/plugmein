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
screen s_House():
    tag map

    add loc_bg("house")

    if time.chapter == 1:
        use b_normal(buttons_ch01["bathroom"], "generic_unavailable_house")
        use b_normal(buttons_ch01["bedroom"], "generic_unavailable_house")
        use b_normal(buttons_ch01["storage_room"], "generic_unavailable_house")
        use b_normal(buttons_ch01["entrance"], "generic_unavailable_house")
        use b_normal(buttons_ch01["kitchen"], "generic_unavailable_house")
        use b_normal(buttons_ch01["living_room"], "generic_unavailable_house")


label generic_unavailable_house:
    scene expression loc_bg("house")
    "There's nothing to do here at this moment"
    call screen s_House()
