"""Visible acceptance tests for ics ingestion (do not modify)."""
from datetime import date, datetime, timezone

from ingest import expand_ics

F = "fixtures/"


def test_single_event_passthrough():
    occ = expand_ics(F + "single.ics", date(2026, 9, 1), date(2026, 9, 30))
    assert len(occ) == 1
    assert occ[0].start_utc == datetime(2026, 9, 21, 14, 0, tzinfo=timezone.utc)


def test_byday_count():
    # Mon/Wed weekly bounded by COUNT=5, DTSTART is Monday 2026-09-07.
    occ = expand_ics(F + "weekly_byday_count.ics", date(2026, 9, 1), date(2026, 10, 1))
    assert len(occ) == 5
    assert occ[0].start_utc == datetime(2026, 9, 7, 13, 0, tzinfo=timezone.utc)
    assert occ[1].local_start.weekday() == 2  # Wednesday follows


def test_exdate_removed_rdate_added():
    occ = expand_ics(F + "exdate_rdate_dst.ics", date(2026, 10, 1), date(2026, 12, 31))
    days = [o.local_start.day for o in occ]
    assert len(occ) == 6
    assert 3 not in days          # EXDATE 2026-11-03 removed
    assert 6 in days              # RDATE 2026-11-06 added
