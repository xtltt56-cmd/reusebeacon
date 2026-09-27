"""Visible tests for QR generation (do not modify)."""
from qr_service import make_qr


def test_png_magic(tmp_path):
    out = tmp_path / "t.png"
    make_qr("TICKET-2026-0001", str(out))
    raw = out.read_bytes()
    assert raw[:8] == b"\x89PNG\r\n\x1a\n"
    assert len(raw) > 200


def test_chinese_payload_runs(tmp_path):
    out = tmp_path / "c.png"
    make_qr("订单号：ORD-2026-0001，座位：A区12排8号", str(out))
    assert out.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"
