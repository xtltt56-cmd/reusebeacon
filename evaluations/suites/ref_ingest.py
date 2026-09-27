"""Reference eval3 ingest implementation via icalendar + recurring_ical_events."""
import os
from datetime import date, datetime, timezone
from typing import List
from icalendar import Calendar
import recurring_ical_events
from dataclasses import dataclass

@dataclass
class Occurrence:
    start_utc: datetime
    local_start: datetime

def expand_ics(path: str, start_date: date, end_date: date) -> List[Occurrence]:
    cal = Calendar.from_ical(open(path, encoding="utf-8").read())
    events = recurring_ical_events.of(cal).between(start_date, end_date + __import__("datetime").timedelta(days=1))
    out = []
    for e in events:
        dt = e["DTSTART"].dt
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        utc = dt.astimezone(timezone.utc)
        if start_date <= utc.date() <= end_date:
            out.append(Occurrence(start_utc=utc, local_start=dt))
    out.sort(key=lambda o: o.start_utc)
    return out
