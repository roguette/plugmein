screen s_clock:
    zorder 100

    # add "ui/clock_bg.png":
    #     xanchor 0.5 yanchor 0.5
    #     xpos 100 ypos 50

    text time.getTimeString():
        xpos 90 ypos 45
        xanchor 0.5 yanchor 0.5
        size 25
        color "#fafafa"