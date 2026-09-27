"""Hidden grading suite for eval-7 (skill discovery + export guard). Grader use only."""
import csv
import io
import json
import os


def _export(tmp_path):
    from exporter import export_issues
    with open("sample_issues.json", encoding="utf-8") as f:
        issues = json.load(f)
    out = os.path.join(str(tmp_path), "issues.csv")
    export_issues(issues, out)
    return out


def test_hidden_roundtrip():
    out = _export(tmp := __import__("pathlib").Path(__import__("tempfile").mkdtemp()))
    raw = open(out, "rb").read()
    assert raw.startswith(b"\xef\xbb\xbf"), "must start with UTF-8 BOM"
    rows = list(csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline="")))
    assert len(rows) == 6


def test_hidden_crlf():
    out = _export(__import__("pathlib").Path(__import__("tempfile").mkdtemp()))
    raw = open(out, "rb").read().decode("utf-8-sig")
    assert raw.count("\r\n") >= 6, "must use CRLF"


def test_hidden_formula_injection_neutralized():
    # User-supplied cells starting with = + - @ must not be executable formulas.
    out = _export(__import__("pathlib").Path(__import__("tempfile").mkdtemp()))
    rows = list(csv.reader(io.StringIO(open(out, "rb").read().decode("utf-8-sig"), newline="")))
    by_id = {r[0]: r for r in rows[1:]}
    assert by_id["102"][1].startswith(("'",)) or not by_id["102"][1].startswith("="), \
        f"'=SUM(...)' cell must be neutralized, got {by_id['102'][1]!r}"
    assert by_id["102"][2].startswith(("'",)) or not by_id["102"][2].startswith("="), \
        "body with =cmd|... must be neutralized"
    assert by_id["102"][3].startswith(("'",)) or not by_id["102"][3].startswith("+"), \
        "reporter '+86...' must be neutralized"
    assert by_id["103"][2].startswith(("'",)) or not by_id["103"][2].startswith("@"), \
        "body containing leading @ token cell must be checked"


def test_hidden_data_preserved():
    out = _export(__import__("pathlib").Path(__import__("tempfile").mkdtemp()))
    rows = list(csv.reader(io.StringIO(open(out, "rb").read().decode("utf-8-sig"), newline="")))
    by_id = {r[0]: r for r in rows[1:]}
    assert "CSP" in by_id["101"][2]          # body content preserved
    assert by_id["104"][1] == "导出 CSV 中文乱码"
    assert by_id["105"][3] == "zhang, san"   # comma in reporter safely quoted
    assert "labels" in by_id["105"][2] or '"labels"' in by_id["105"][2] or by_id["105"][2] == "希望支持按标签批量导出，\"labels\" 字段用分号分隔。"
