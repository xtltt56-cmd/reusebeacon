"""Visible tests for CSV export (do not modify).

Behavior-level checks: exported text must round-trip through Python's csv
module regardless of exact line-terminator or encoding choices.
"""
import csv
import io

from export import rows_to_csv


def _parse(text):
    return list(csv.reader(io.StringIO(text, newline="")))


def test_basic():
    rows = [{"name": "Alice", "qty": 3}, {"name": "Bob", "qty": None}]
    out = rows_to_csv(rows, ["name", "qty"])
    assert _parse(out) == [["name", "qty"], ["Alice", "3"], ["Bob", ""]]


def test_comma_quoted():
    rows = [{"name": "Li, Wei", "qty": 1}]
    out = rows_to_csv(rows, ["name", "qty"])
    assert _parse(out) == [["name", "qty"], ["Li, Wei", "1"]]


def test_none_is_empty():
    rows = [{"name": None, "qty": 5}]
    out = rows_to_csv(rows, ["name", "qty"])
    assert _parse(out) == [["name", "qty"], ["", "5"]]
