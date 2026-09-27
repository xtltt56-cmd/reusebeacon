"""Hidden grading suite for eval-1 (DST recurrence). Grader use only.

Expected values generated independently with zoneinfo reference implementation.
"""
from datetime import date, datetime, timedelta, timezone

from meetings import Meeting, expand

UTC = timezone.utc


def test_hidden_spring_weekly_ny():
    m = Meeting(title="ny sync", hour=9, minute=0, tz="America/New_York", weekday=1,
                recurrence="weekly")
    occ = expand(m, date(2026, 2, 24), date(2026, 4, 14))
    assert len(occ) == 8, f"expected 8 occurrences, got {len(occ)}"
    expected_utc = [
        datetime(2026, 2, 24, 14, 0, tzinfo=UTC),
        datetime(2026, 3, 3, 14, 0, tzinfo=UTC),
        datetime(2026, 3, 10, 13, 0, tzinfo=UTC),
        datetime(2026, 3, 17, 13, 0, tzinfo=UTC),
        datetime(2026, 3, 24, 13, 0, tzinfo=UTC),
        datetime(2026, 3, 31, 13, 0, tzinfo=UTC),
        datetime(2026, 4, 7, 13, 0, tzinfo=UTC),
        datetime(2026, 4, 14, 13, 0, tzinfo=UTC),
    ]
    for o, e in zip(occ, expected_utc):
        assert o.start_utc == e, f"{o.start_utc} != {e}"
        assert o.start_utc.tzinfo is UTC or o.start_utc.utcoffset() == timedelta(0)


def test_hidden_fall_weekly_ny():
    m = Meeting(title="ny sync", hour=9, minute=0, tz="America/New_York", weekday=1,
                recurrence="weekly")
    occ = expand(m, date(2026, 10, 20), date(2026, 11, 10))
    assert len(occ) == 4
    expected_utc = [
        datetime(2026, 10, 20, 13, 0, tzinfo=UTC),
        datetime(2026, 10, 27, 13, 0, tzinfo=UTC),
        datetime(2026, 11, 3, 14, 0, tzinfo=UTC),
        datetime(2026, 11, 10, 14, 0, tzinfo=UTC),
    ]
    for o, e in zip(occ, expected_utc):
        assert o.start_utc == e, f"{o.start_utc} != {e}"


def test_hidden_gap_nonexistent_time():
    # Sunday 02:30 America/New_York on 2026-03-08 does not exist.
    # fold=0 semantics: 02:30 EST == 07:30 UTC (zoneinfo default).
    m = Meeting(title="gap", hour=2, minute=30, tz="America/New_York", weekday=6,
                recurrence="none")
    occ = expand(m, date(2026, 3, 8), date(2026, 3, 8))
    assert len(occ) == 1
    assert occ[0].start_utc == datetime(2026, 3, 8, 7, 30, tzinfo=UTC), occ[0]


def test_hidden_ambiguous_fall_back():
    # Sunday 01:30 America/New_York on 2026-11-01 happens twice.
    # fold=0 semantics: earliest instant, 01:30 EDT == 05:30 UTC.
    m = Meeting(title="amb", hour=1, minute=30, tz="America/New_York", weekday=6,
                recurrence="none")
    occ = expand(m, date(2026, 11, 1), date(2026, 11, 1))
    assert len(occ) == 1
    assert occ[0].start_utc == datetime(2026, 11, 1, 5, 30, tzinfo=UTC), occ[0]


def test_hidden_monthly_2nd_tuesday_2026():
    m = Meeting(title="board", hour=14, minute=0, tz="Europe/Berlin", weekday=1,
                recurrence="monthly_2nd")
    occ = expand(m, date(2026, 1, 1), date(2026, 6, 30))
    got_days = [o.local_start.day for o in occ]
    assert got_days == [13, 10, 10, 14, 12, 9], got_days
    # local wall time preserved in Berlin (CET/CEST switch Mar 29 2026)
    offsets = {o.local_start.utcoffset() for o in occ}
    assert timedelta(hours=1) in offsets and timedelta(hours=2) in offsets, offsets


def test_hidden_no_drift_full_year():
    m = Meeting(title="ny sync", hour=9, minute=0, tz="America/New_York", weekday=1,
                recurrence="weekly")
    occ = expand(m, date(2026, 1, 1), date(2026, 12, 31))
    assert len(occ) == 52, len(occ)
    for o in occ:
        assert o.local_start.hour == 9 and o.local_start.minute == 0
        assert o.local_start.weekday() == 1


def test_hidden_unusual_offset_kathmandu():
    m = Meeting(title="ktm", hour=13, minute=20, tz="Asia/Kathmandu", weekday=2,
                recurrence="weekly")
    occ = expand(m, date(2026, 9, 2), date(2026, 9, 16))
    assert len(occ) == 3
    assert occ[0].start_utc == datetime(2026, 9, 2, 7, 35, tzinfo=UTC), occ[0]


def test_hidden_monthly_5th_edge():
    # 5th Friday: Jan 2026 has one (the 30th); Feb and Mar 2026 have only four.
    m = Meeting(title="rare", hour=8, minute=0, tz="UTC", weekday=4,
                recurrence="monthly_5th")
    occ = expand(m, date(2026, 1, 1), date(2026, 3, 31))
    got = [(o.local_start.month, o.local_start.day) for o in occ]
    assert got == [(1, 30)], got
