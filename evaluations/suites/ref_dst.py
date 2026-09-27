"""Reference implementation of eval1 expand() using zoneinfo (grader only)."""
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from typing import List
import calendar

@dataclass
class Meeting:
    title: str; hour: int; minute: int; tz: str; weekday: int; recurrence: str = "none"

@dataclass
class Occurrence:
    start_utc: datetime; local_start: datetime

def expand(meeting, start_date, end_date):
    tz = ZoneInfo(meeting.tz)
    out = []
    if meeting.recurrence == "none":
        days = [start_date] if start_date.weekday() == meeting.weekday else []
    elif meeting.recurrence == "weekly":
        days, d = [], start_date
        while d <= end_date:
            if d.weekday() == meeting.weekday: days.append(d)
            d += timedelta(days=1)
    else:
        n = {"1st":1,"2nd":2,"3rd":3,"4th":4,"5th":5}[meeting.recurrence.split("_")[1]]
        days = []
        for (y, mo) in sorted({(d.year, d.month) for d in [start_date + timedelta(days=i) for i in range((end_date-start_date).days+1)]}):
            fridays = [date(y, mo, d) for d in range(1, calendar.monthrange(y, mo)[1]+1)
                       if date(y, mo, d).weekday() == meeting.weekday]
            if len(fridays) >= n: days.append(fridays[n-1])
        days = [d for d in days if start_date <= d <= end_date]
    for d in days:
        loc = datetime(d.year, d.month, d.day, meeting.hour, meeting.minute, tzinfo=tz)
        out.append(Occurrence(start_utc=loc.astimezone(timezone.utc), local_start=loc))
    return out
