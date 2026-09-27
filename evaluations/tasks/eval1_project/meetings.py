"""Meeting definitions and schedule expansion."""
from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import List, Optional


@dataclass
class Meeting:
    title: str
    hour: int                  # local wall clock hour
    minute: int                # local wall clock minute
    tz: str                    # IANA timezone name, e.g. "America/New_York"
    weekday: int               # 0=Mon .. 6=Sun, anchor weekday for recurrence
    recurrence: str = "none"   # "none" | "weekly" | "monthly_1st".."monthly_5th"


@dataclass
class Occurrence:
    start_utc: datetime        # timezone-aware, UTC
    local_start: datetime      # timezone-aware, in Meeting.tz


def expand(meeting: Meeting, start_date: date, end_date: date) -> List[Occurrence]:
    """Expand a meeting into concrete occurrences between start_date and end_date
    (inclusive).

    Currently only one-off meetings are supported: the meeting happens on
    start_date itself (if weekday matches) and recurrence rules are ignored.

    TODO: implement "weekly" and "monthly_nth" recurrence with correct
    daylight-saving-time handling per the README acceptance criteria.
    """
    occurrences: List[Occurrence] = []

    if meeting.recurrence == "none":
        if start_date.weekday() == meeting.weekday:
            occurrences.append(_build(meeting, start_date))
        return occurrences

    # TODO: weekly / monthly_nth expansion
    return occurrences


def _build(meeting: Meeting, day: date) -> Occurrence:
    """Build a single occurrence on `day` at the meeting's local wall time.

    NOTE: current implementation assumes a fixed +00:00 offset and is known
    to be wrong for real timezones. Fix as part of the recurrence work.
    """
    naive = datetime(day.year, day.month, day.day, meeting.hour, meeting.minute)
    aware = naive.replace(tzinfo=timezone.utc)
    return Occurrence(start_utc=aware, local_start=aware)
