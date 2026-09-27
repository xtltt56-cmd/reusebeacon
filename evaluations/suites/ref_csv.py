"""Reference implementation of eval2 export using stdlib csv (grader only)."""
import csv
from typing import Dict, List, Sequence

def rows_to_csv(rows: List[Dict], header: Sequence[str]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\r\n")
    w.writerow(header)
    for row in rows:
        w.writerow(["" if row.get(h) is None else str(row.get(h)) for h in header])
    return buf.getvalue()

import io
def write_csv_file(path: str, rows: List[Dict], header: Sequence[str]) -> None:
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        f.write(rows_to_csv(rows, header))
