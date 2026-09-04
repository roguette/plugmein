testsuite script_tests:
    testsuite flags_tests:
        before testcase:
            $ flags.clear()

        testcase new_flag_is_false:
            assert eval (not flag("test_flag"))

        testcase test_flag_True:
            $ flag("test_flag", True)

            assert eval flag("test_flag")
            assert eval ("test_flag" in flags)

        testcase test_flag_False:
            $ flag("test_flag", True)
            $ flag("test_flag", False)

            assert eval (not flag("test_flag"))
            assert eval ("test_flag" not in flags)

        testcase disabling_missing_flag_does_not_crash:
            $ flag("does_not_exist", False)

            assert eval (not flag("does_not_exist"))


    testsuite time_tests:
        testcase default_time_exists:
            $ test_time = TimeClass()

            assert eval (test_time.chapter is not None)
            assert eval (test_time.hour is not None)
            assert eval (test_time.minute is not None)

        testcase set_time:
            $ test_time = TimeClass()
            $ test_time.setTime(12, 34)

            assert eval (test_time.hour == 12)
            assert eval (test_time.minute == 34)

        testcase advance_minutes:
            $ test_time = TimeClass()
            $ test_time.hour = 10
            $ test_time.minute = 15

            $ test_time.advanceTime(minutes=20)

            assert eval (test_time.hour == 10)
            assert eval (test_time.minute == 35)

        testcase advance_across_hour:
            $ test_time = TimeClass()
            $ test_time.hour = 10
            $ test_time.minute = 45

            $ test_time.advanceTime(minutes=30)

            assert eval (test_time.hour == 11)
            assert eval (test_time.minute == 15)


        testcase advance_multiple_hours_with_minutes:
            $ test_time = TimeClass()
            $ test_time.hour = 10
            $ test_time.minute = 30

            $ test_time.advanceTime(minutes=150)

            assert eval (test_time.hour == 13)
            assert eval (test_time.minute == 0)

        testcase is_day:
            # jesli ja przez przypadek zmienie kiedy jest dzien a kiedy jest noc to to wywali blad
            parameter (test_hour, expected) = [
                (0, False),
                (6, False),
                (7, True),
                (12, True),
                (17, True),
                (18, False),
                (23, False),
            ]

            $ test_time = TimeClass()
            $ test_time.hour = test_hour

            assert eval (test_time.isDay() == expected)

    testsuite friendship_tests:
        before testcase:
            $ friendship.clear()

        testcase unknown_character_defaults_to_zero:
            assert eval (friendship["kldfgjhklfjhglkfjgh"] == 0)

        testcase friendship_increase:
            $ friendship["friendshipismagic"] += 67

            assert eval (friendship["friendshipismagic"] == 67)

        testcase friendship_decrease:
            $ friendship["mamacoco"] -= 1

            assert eval (friendship["mamacoco"] == -1)


    testsuite telemetry_tests:
        before testcase:
            $ time_started = None
            $ time_finished = None
            $ telemetry_flags.clear()

        testcase telemetry_start:
            $ telemetry_start()
            assert eval (time_started is not None)

        testcase telemetry_end:
            $ telemetry_start()
            $ telemetry_end()

            assert eval (time_finished is not None)
            assert eval (time_finished >= time_started)

        testcase telemetry_flag_works:
            $ telemetry_flag("ended_bts")
            assert eval (len(telemetry_flags) == 1)
            assert eval (telemetry_flags[0][1] == "ended_bts")

        testcase telemetry_result_string:
            $ time_started = datetime(2026, 1, 1, 12, 0, 0)
            $ time_finished = datetime(2026, 1, 1, 12, 5, 0)

            $ telemetry_flags.append([
                datetime(2026, 1, 1, 12, 2, 0),
                "entered_bakery"
            ])

            $ result = telemetry_generate_result_string()

            assert eval ("zrób zrzut ekranu!" in result)
            assert eval ("2026-01-01 12:00:00" in result)
            assert eval ("2026-01-01 12:05:00" in result)
            assert eval ("0:05:00" in result)
            assert eval ("entered_bakery" in result)

