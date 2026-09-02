screen s_Telemetry():
    tag menu

    vbox:
        xsize 0.8
        ysize 0.5
        xalign 0.5
        yalign 0.5

        text telemetry_generate_result_string():
            size 18
            line_spacing 4

        textbutton "Zamknij":
            action Return()