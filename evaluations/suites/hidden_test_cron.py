"""Hidden grading suite for eval-6 (Vixie cron). Grader use only.

Expected values generated with croniter (day_or=True, Vixie semantics) and
hand-checked, notably the day-of-month OR day-of-week rule.
"""
from datetime import datetime

from cron_calc import next_runs


def test_hidden_dom_dow_or_rule():
    # DOM=13 restricted AND DOW=Friday restricted -> Vixie: match EITHER.
    # 2026-10-13 is a Tuesday (matches DOM only) and must appear between
    # the Fridays; AND-semantics implementations skip it.
    got = next_runs("0 0 13 * 5", datetime(2026, 9, 27, 10, 0), 6)
    assert got == [datetime(2026, 10, 2, 0, 0), datetime(2026, 10, 9, 0, 0),
                   datetime(2026, 10, 13, 0, 0), datetime(2026, 10, 16, 0, 0),
                   datetime(2026, 10, 23, 0, 0), datetime(2026, 10, 30, 0, 0)]


def test_hidden_range_step_on_hours():
    got = next_runs("15 2-6/2 * * *", datetime(2026, 9, 26, 1, 0), 4)
    assert got == [datetime(2026, 9, 26, 2, 15), datetime(2026, 9, 26, 4, 15),
                   datetime(2026, 9, 26, 6, 15), datetime(2026, 9, 27, 2, 15)]


def test_hidden_leap_day():
    got = next_runs("0 0 29 2 *", datetime(2026, 9, 26, 10, 0), 2)
    assert got == [datetime(2028, 2, 29, 0, 0), datetime(2032, 2, 29, 0, 0)]


def test_hidden_shortcuts():
    assert next_runs("@daily", datetime(2026, 9, 26, 10, 0), 3) == [
        datetime(2026, 9, 27, 0, 0), datetime(2026, 9, 28, 0, 0),
        datetime(2026, 9, 29, 0, 0)]
    assert next_runs("@weekly", datetime(2026, 9, 26, 10, 0), 2) == [
        datetime(2026, 9, 27, 0, 0), datetime(2026, 10, 4, 0, 0)]


def test_hidden_sunday_as_seven():
    got7 = next_runs("0 0 * * 7", datetime(2026, 9, 26, 10, 0), 2)
    got0 = next_runs("0 0 * * 0", datetime(2026, 9, 26, 10, 0), 2)
    assert got7 == got0 == [datetime(2026, 9, 27, 0, 0), datetime(2026, 10, 4, 0, 0)]


def test_hidden_case_insensitive_names():
    assert next_runs("0 9 * * mon", datetime(2026, 9, 26, 10, 0), 2) == [
        datetime(2026, 9, 28, 9, 0), datetime(2026, 10, 5, 9, 0)]
    assert next_runs("0 12 1 JAN *", datetime(2026, 9, 26, 10, 0), 2) == [
        datetime(2027, 1, 1, 12, 0), datetime(2028, 1, 1, 12, 0)]


def test_hidden_month_step_hour_list():
    got = next_runs("0 0,12 1 */2 *", datetime(2026, 9, 26, 10, 0), 4)
    assert got == [datetime(2026, 11, 1, 0, 0), datetime(2026, 11, 1, 12, 0),
                   datetime(2027, 1, 1, 0, 0), datetime(2027, 1, 1, 12, 0)]


def test_hidden_quarter_hours_business_days():
    got = next_runs("*/15 8-17 * * MON-FRI", datetime(2026, 9, 25, 17, 10), 5)
    assert got == [datetime(2026, 9, 25, 17, 15), datetime(2026, 9, 25, 17, 30),
                   datetime(2026, 9, 25, 17, 45), datetime(2026, 9, 28, 8, 0),
                   datetime(2026, 9, 28, 8, 15)]
