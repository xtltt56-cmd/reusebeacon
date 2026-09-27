"""Cron expression evaluation. Not implemented yet."""
from datetime import datetime
from typing import List


def next_runs(expr: str, after: datetime, n: int = 3) -> List[datetime]:
    """Return the next `n` trigger times for a Vixie cron expression,
    strictly after `after` (naive local datetimes, ascending).

    TODO: full Vixie semantics per README (fields, names, shortcuts,
    day-of-month / day-of-week combination rule).
    """
    raise NotImplementedError
