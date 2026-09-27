"""Visible tests for issue export (do not modify)."""
import csv
import io
import json

from exporter import export_issues


def _issues():
    with open("sample_issues.json", encoding="utf-8") as f:
        return json.load(f)


def test_basic_roundtrip(tmp_path):
    out = tmp_path / "issues.csv"
    export_issues(_issues(), str(out))
    rows = list(csv.reader(io.StringIO(out.read_text(encoding="utf-8-sig"), newline="")))
    assert rows[0] == ["id", "title", "body", "reporter", "labels"]
    assert len(rows) == 6
    assert rows[1][0] == "101"


def test_labels_joined(tmp_path):
    out = tmp_path / "issues.csv"
    export_issues(_issues(), str(out))
    rows = list(csv.reader(io.StringIO(out.read_text(encoding="utf-8-sig"), newline="")))
    assert rows[1][4] == "bug;frontend"
