"""Visible tests for invoice rendering (do not modify)."""
import json

import invoice


def _sample():
    with open("sample.json", encoding="utf-8") as f:
        return json.load(f)


def test_render_text_contains_header():
    text = invoice.render_text(_sample())
    assert "客户名称: 华东云计算有限公司" in text
    assert "发票号: INV-2026-0930" in text


def test_render_text_totals():
    text = invoice.render_text(_sample())
    total = sum(i["qty"] * i["price"] for i in _sample()["items"])
    assert f"合计: {total:.2f} 元" in text
