"""CSV export helpers."""
import csv
from typing import Dict, List, Sequence


def rows_to_csv(rows: List[Dict], header: Sequence[str]) -> str:
    """Render rows as CSV text. Header is written as the first line."""
    lines = [",".join(header)]
    for row in rows:
        cells = []
        for h in header:
            v = row.get(h)
            s = "" if v is None else str(v)
            if "," in s:
                s = '"' + s + '"'
            cells.append(s)
        lines.append(",".join(cells))
    return "\n".join(lines) + "\n"


def write_csv_file(path: str, rows: List[Dict], header: Sequence[str]) -> None:
    """Write rows to `path` as a CSV file for Excel users."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(rows_to_csv(rows, header))
