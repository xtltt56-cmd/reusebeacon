"""Generate expected values for hidden DST tests using zoneinfo reference.

Run once; output pasted as literals into hidden_test_dst.py.
"""
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
KTM = ZoneInfo("Asia/Kathmandu")


def utc(y, mo, d, h, mi):
    return datetime(y, mo, d, h, mi, tzinfo=timezone.utc)


def to_utc(ny_dt):
    return ny_dt.astimezone(timezone.utc)


print("# 1. Spring: weekly Tue 09:00 NY, Feb24-Apr14 2026 (8 occ)")
for d in [(2,24),(3,3),(3,10),(3,17),(3,24),(3,31),(4,7),(4,14)]:
    loc = datetime(2026, d[0], d[1], 9, 0, tzinfo=NY)
    print(f"#   {loc.date()} offset={loc.utcoffset()} utc={to_utc(loc):%Y-%m-%d %H:%M %Z}")

print("# 2. Fall: weekly Tue 09:00 NY, Oct20-Nov10 2026 (4 occ)")
for d in [(10,20),(10,27),(11,3),(11,10)]:
    loc = datetime(2026, d[0], d[1], 9, 0, tzinfo=NY)
    print(f"#   {loc.date()} offset={loc.utcoffset()} utc={to_utc(loc):%Y-%m-%d %H:%M %Z}")

print("# 3. Gap: Sun 02:30 NY 2026-03-08 (nonexistent, fold=0)")
loc = datetime(2026, 3, 8, 2, 30, tzinfo=NY)
print(f"#   local={loc} fold={loc.fold} utc={to_utc(loc):%Y-%m-%d %H:%M}")

print("# 4. Ambiguous: Sun 01:30 NY 2026-11-01 (fold=0 = first/EDT)")
loc = datetime(2026, 11, 1, 1, 30, tzinfo=NY)
print(f"#   local={loc} fold={loc.fold} utc={to_utc(loc):%Y-%m-%d %H:%M}")

print("# 5. monthly_2nd Tuesday 2026 Jan-Jun, 14:00 UTC-meeting check dates")
import calendar
for mo in range(1, 7):
    tues = [d for d in range(1, 32) if d <= calendar.monthrange(2026, mo)[1]
            and datetime(2026, mo, d).weekday() == 1]
    print(f"#   month {mo}: 2nd Tuesday = day {tues[1]}")

print("# 6. Tuesday count 2026")
cnt = sum(1 for d in range(1, 366) if (datetime(2026,1,1)+timedelta(days=d-1)).weekday()==1)
print(f"#   {cnt}")

print("# 7. Kathmandu weekly Wed 13:20, Sep2026: utc")
loc = datetime(2026, 9, 2, 13, 20, tzinfo=KTM)
print(f"#   {loc} -> utc={to_utc(loc):%Y-%m-%d %H:%M} offset={loc.utcoffset()}")
