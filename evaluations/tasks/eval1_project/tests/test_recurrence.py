"""Visible acceptance tests for recurrence expansion (do not modify)."""
from datetime import date, datetime, timezone, timedelta

from meetings import Meeting, expand


def test_oneoff_unchanged():
    m = Meeting(title="standup", hour=9, minute=0, tz="UTC", weekday=0)
    occ = expand(m, date(2026, 9, 21), date(2026, 9, 21))  # a Monday
    assert len(occ) == 1
    assert occ[0].start_utc == datetime(2026, 9, 21, 9, 0, tzinfo=timezone.utc)


def test_weekly_utc():
    m = Meeting(title="weekly sync", hour=10, minute=30, tz="UTC", weekday=1,
                recurrence="weekly")
    occ = expand(m, date(2026, 9, 1), date(2026, 9, 21))
    assert [o.start_utc for o in occ] == [
        datetime(2026, 9, 1, 10, 30, tzinfo=timezone.utc),
        datetime(2026, 9, 8, 10, 30, tzinfo=timezone.utc),
        datetime(2026, 9, 15, 10, 30, tzinfo=timezone.utc),
    ]


def test_monthly_second_tuesday_utc():
    m = Meeting(title="board", hour=14, minute=0, tz="UTC", weekday=1,
                recurrence="monthly_2nd")
    occ = expand(m, date(2026, 1, 1), date(2026, 3, 31))
    assert [o.start_utc.day for o in occ] == [13, 10, 10]  # 2nd Tue of Jan/Feb/Mar 2026


def test_dst_weekly_new_york_spring():
    # Weekly Tuesday 09:00 America/New_York from Feb 24 to Apr 14, 2026.
    # US spring-forward is 2026-03-08: UTC offset changes -05:00 -> -04:00.
    m = Meeting(title="ny sync", hour=9, minute=0, tz="America/New_York", weekday=1,
                recurrence="weekly")
    occ = expand(m, date(2026, 2, 24), date(2026, 4, 14))
    assert len(occ) == 8
    # Before spring-forward: 09:00 EST == 14:00 UTC
    assert occ[0].local_start.utcoffset() == timedelta(hours=-5)
    # After spring-forward: 09:00 EDT == 13:00 UTC
    assert occ[-1].local_start.utcoffset() == timedelta(hours=-4)
    # UTC instants must shift across the DST transition
    assert occ[0].start_utc.utcoffset() == timedelta(0)
    # Wall clock must never drift
    assert all(o.local_start.hour == 9 and o.local_start.minute == 0 for o in occ)
