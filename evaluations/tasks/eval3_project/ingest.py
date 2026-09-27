"""iCalendar ingestion: parse .ics files and expand occurrences in a window."""
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from typing import List


@dataclass
class Occurrence:
    start_utc: datetime      # timezone-aware, UTC
    local_start: datetime    # timezone-aware, in the event's TZID


def expand_ics(path: str, start_date: date, end_date: date) -> List[Occurrence]:
    """Return occurrences of all VEVENTs in `path` that fall within
    [start_date, end_date] (inclusive), sorted chronologically.

    Current implementation only reads DTSTART of each VEVENT, treats every
    time as UTC, and ignores RRULE / RDATE / EXDATE / VTIMEZONE.

    TODO: full weekly recurrence support per README (RFC 5545 semantics).
    """
    text = open(path, encoding="utf-8").read()
    occurrences: List[Occurrence] = []
    for block in _vevent_blocks(text):
        m = re.search(r"DTSTART[^:]*:(\d{8}T\d{6}Z?)", block)
        if not m:
            continue
        naive = datetime.strptime(m.group(1).rstrip("Z"), "%Y%m%dT%H%M%S")
        aware = naive.replace(tzinfo=timezone.utc)
        if start_date <= aware.date() <= end_date:
            occurrences.append(Occurrence(start_utc=aware, local_start=aware))
    occurrences.sort(key=lambda o: o.start_utc)
    return occurrences


def _vevent_blocks(text: str) -> List[str]:
    """Split unfolded calendar text into VEVENT blocks (minimal parser)."""
    unfolded = text.replace("\r\n ", "").replace("\n ", "")
    return re.findall(r"BEGIN:VEVENT(.*?)END:VEVENT", unfolded, re.S)
