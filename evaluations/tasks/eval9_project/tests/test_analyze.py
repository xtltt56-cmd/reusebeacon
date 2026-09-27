"""Visible tests for log analytics (do not modify)."""
import json

from analyze import analyze


def test_sample_summary(tmp_path):
    out = tmp_path / "summary.json"
    analyze("events_sample.json", str(out))
    got = json.loads(out.read_text(encoding="utf-8"))
    want = json.loads(open("tests/expected_sample.json", encoding="utf-8").read())
    assert got == want
