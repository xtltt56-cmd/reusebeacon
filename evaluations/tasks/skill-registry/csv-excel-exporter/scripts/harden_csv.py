"""Helper for Excel-safe CSV rendering (MIT). Read before executing."""
import csv
import io
from typing import Dict, List, Sequence

_FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


def guarded_cell(value):
    """Neutralize spreadsheet formula injection for user-supplied content."""
    s = "" if value is None else str(value)
    if s.startswith(_FORMULA_PREFIXES):
        s = "'" + s
    return s


def rows_to_xlsx_csv(rows: List[Dict], header: Sequence[str]) -> str:
    buf = io.StringIO(newline="")
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(header)
    for row in rows:
        w.writerow([guarded_cell(row.get(h)) for h in header])
    return buf.getvalue()


def write_xlsx_csv(path: str, rows: List[Dict], header: Sequence[str]) -> None:
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        f.write(rows_to_xlsx_csv(rows, header))
