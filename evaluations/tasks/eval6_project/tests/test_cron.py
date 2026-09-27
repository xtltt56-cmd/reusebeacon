"""Visible tests for cron evaluation (do not modify)."""
from datetime import datetime

from cron_calc import next_runs


def test_every_five_minutes():
    got = next_runs("*/5 * * * *", datetime(2026, 9, 26, 10, 2), 3)
    assert got == [datetime(2026, 9, 26, 10, 5),
                   datetime(2026, 9, 26, 10, 10),
                   datetime(2026, 9, 26, 10, 15)]


def test_weekday_morning():
    got = next_runs("0 9 * * 1-5", datetime(2026, 9, 26, 10, 0), 3)  # Saturday
    assert got == [datetime(2026, 9, 28, 9, 0),
                   datetime(2026, 9, 29, 9, 0),
                   datetime(2026, 9, 30, 9, 0)]


def test_monthly_fourth():
    got = next_runs("30 4 1 * *", datetime(2026, 9, 26, 10, 0), 2)
    assert got == [datetime(2026, 10, 1, 4, 30),
                   datetime(2026, 11, 1, 4, 30)]
