"""Hidden grading suite for eval-3 (RFC 5545 ingestion). Grader use only.

Expected UTC instants hand-derived from RFC 5545 semantics and cross-checked
against an independent icalendar + recurring-ical-events implementation.
"""
from datetime import date, datetime, timezone

from ingest import expand_ics

F = "fixtures/"
UTC = timezone.utc


def test_hidden_fixture1_exact_instants():
    occ = expand_ics(F + "weekly_byday_count.ics", date(2026, 9, 1), date(2026, 10, 1))
    expected = [
        datetime(2026, 9, 7, 13, 0, tzinfo=UTC),   # Mon (DTSTART)
        datetime(2026, 9, 9, 13, 0, tzinfo=UTC),   # Wed
        datetime(2026, 9, 14, 13, 0, tzinfo=UTC),  # Mon
        datetime(2026, 9, 16, 13, 0, tzinfo=UTC),  # Wed
        datetime(2026, 9, 21, 13, 0, tzinfo=UTC),  # Mon — COUNT=5 reached
    ]
    assert [o.start_utc for o in occ] == expected


def test_hidden_fixture2_exact_instants():
    occ = expand_ics(F + "exdate_rdate_dst.ics", date(2026, 10, 1), date(2026, 12, 31))
    expected = [
        datetime(2026, 10, 20, 13, 0, tzinfo=UTC),  # EDT
        datetime(2026, 10, 27, 13, 0, tzinfo=UTC),  # EDT
        datetime(2026, 11, 6, 14, 0, tzinfo=UTC),   # RDATE (EST after Nov 1)
        datetime(2026, 11, 10, 14, 0, tzinfo=UTC),  # EST
        datetime(2026, 11, 17, 14, 0, tzinfo=UTC),
        datetime(2026, 11, 24, 14, 0, tzinfo=UTC),  # COUNT=6 bound on RRULE
    ]
    assert [o.start_utc for o in occ] == expected
    # COUNT applies to RRULE generation BEFORE EXDATE removal:
    # a wrong implementation that extends the set to replace the EXDATE
    # would emit 2026-12-01 — must not appear.
    assert all(o.local_start.day != 1 or o.local_start.month != 12 for o in occ)


def test_hidden_fixture3_custom_vtimezone_southern():
    occ = expand_ics(F + "custom_southern_tz.ics", date(2026, 3, 25), date(2026, 6, 5))
    expected = [
        datetime(2026, 3, 31, 0, 0, tzinfo=UTC),    # +10:00 (before Apr 5 switch)
        datetime(2026, 4, 6, 23, 0, tzinfo=UTC),    # +11:00 (Apr 7 10:00 local)
        datetime(2026, 4, 13, 23, 0, tzinfo=UTC),
        datetime(2026, 4, 20, 23, 0, tzinfo=UTC),
        datetime(2026, 4, 27, 23, 0, tzinfo=UTC),
        datetime(2026, 5, 4, 23, 0, tzinfo=UTC),
        datetime(2026, 5, 11, 23, 0, tzinfo=UTC),
        datetime(2026, 5, 18, 23, 0, tzinfo=UTC),
        datetime(2026, 5, 25, 23, 0, tzinfo=UTC),   # UNTIL 2026-06-01T00:00Z excludes Jun 2
    ]
    assert len(occ) == 9
    assert [o.start_utc for o in occ] == expected


def test_hidden_fixture3_window_filter():
    occ = expand_ics(F + "custom_southern_tz.ics", date(2026, 4, 1), date(2026, 5, 31))
    assert len(occ) == 8
    assert all(o.start_utc.hour == 23 for o in occ)


def test_hidden_fixture4_interval_utc():
    occ = expand_ics(F + "interval_utc.ics", date(2026, 9, 1), date(2026, 11, 1))
    expected = [
        datetime(2026, 9, 3, 8, 0, tzinfo=UTC),
        datetime(2026, 9, 17, 8, 0, tzinfo=UTC),
        datetime(2026, 10, 1, 8, 0, tzinfo=UTC),
        datetime(2026, 10, 15, 8, 0, tzinfo=UTC),
    ]
    assert [o.start_utc for o in occ] == expected


def test_hidden_ordering_and_tzinfo():
    occ = expand_ics(F + "exdate_rdate_dst.ics", date(2026, 10, 1), date(2026, 12, 31))
    assert occ == sorted(occ, key=lambda o: o.start_utc)
    for o in occ:
        assert o.start_utc.tzinfo is not None and o.local_start.tzinfo is not None
        assert o.local_start.utcoffset() in (__import__("datetime").timedelta(hours=-4),
                                             __import__("datetime").timedelta(hours=-5))
