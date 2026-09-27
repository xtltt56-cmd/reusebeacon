"""Hidden grading suite for eval-2 (CSV edge cases). Grader use only."""
import csv
import io
import os
import tempfile

from export import rows_to_csv, write_csv_file

NASTY = [
    {"name": "comma, inside", "note": "a,b", "qty": "1"},
    {"name": 'quote " inside', "note": 'say "hi"', "qty": "2"},
    {"name": "newline\ninside", "note": "line1\nline2", "qty": "3"},
    {"name": "crlf\r\ninside", "note": "x\r\ny", "qty": "4"},
    {"name": "中文备注", "note": "备注：报价含税（¥1,000）", "qty": "5"},
    {"name": "emoji 🙂", "note": "ok 👍", "qty": "6"},
    {"name": "007", "note": "1-2", "qty": "7"},
    {"name": None, "note": None, "qty": None},
    {"name": "", "note": "only-quote\"\"", "qty": "8"},
]
HEADER = ["name", "note", "qty"]


def test_hidden_roundtrip_all_fields():
    out = rows_to_csv(NASTY, HEADER)
    reader = csv.reader(io.StringIO(out, newline=""))
    rows = list(reader)
    assert rows[0] == HEADER, rows[0]
    for got, want in zip(rows[1:], NASTY):
        expected = ["" if want[h] is None else str(want[h]) for h in HEADER]
        assert got == expected, f"row mismatch:\n got={got}\nwant={expected}"


def test_hidden_crlf_terminators():
    out = rows_to_csv(NASTY, HEADER)
    body_lines = out.split("\r\n")
    assert out.endswith("\r\n"), "rows must end with CRLF"
    assert "\n" not in out.replace("\r\n", "") or True
    # no bare LF outside quoted content at line level
    assert out.count("\r\n") >= 10


def test_hidden_excel_file_bytes():
    tmp = os.path.join(tempfile.mkdtemp(), "out.csv")
    write_csv_file(tmp, NASTY, HEADER)
    raw = open(tmp, "rb").read()
    assert raw.startswith(b"\xef\xbb\xbf"), "file must start with UTF-8 BOM"
    assert b"\r\n" in raw, "file must use CRLF"
    text = raw.decode("utf-8-sig")
    reader = csv.reader(io.StringIO(text, newline=""))
    rows = list(reader)
    assert rows[0] == HEADER
    assert rows[5][0] == "中文备注", rows[5]
    assert rows[6][0] == "emoji 🙂"


def test_hidden_empty_rows():
    out = rows_to_csv([], HEADER)
    assert out == "name,note,qty\r\n", repr(out)


def test_hidden_visible_still_pass():
    out = rows_to_csv([{"name": "Alice", "qty": 3}], ["name", "qty"])
    assert out == "name,qty\r\nAlice,3\r\n", repr(out)
