"""Grader for eval-8: decode candidate QR PNGs with zxing-cpp. Grader use only.

Note: OpenCV's QRCodeDetector mishandles non-ASCII UTF-8 payloads, so the
authoritative decoder here is zxing-cpp (UTF-8 correct).
"""
import json
import sys
from pathlib import Path

from PIL import Image
import zxingcpp

PAYLOADS = [
    "TICKET-2026-0001",
    "订单号：ORD-2026-0001，座位：A区12排8号",
    "https://tickets.example.com/e/9f8b7c6d?ref=email&utm=x",
    "x" * 500,
    "emoji 🎟️ 😀 payload",
    '{"oid": 42, "seat": "B3", "gate": "北门"}',
    "0123456789012345678901234567890123456789",
    "a",
]


def grade(project_dir: Path) -> dict:
    project_dir = Path(project_dir)
    sys.path.insert(0, str(project_dir))
    from qr_service import make_qr
    results = []
    for p in PAYLOADS:
        out = project_dir / f"grader_qr_{abs(hash(p)) % 10**8}.png"
        try:
            make_qr(p, str(out))
        except Exception as e:  # noqa
            results.append({"payload": p[:24], "error": f"{type(e).__name__}: {e}"})
            continue
        raw = out.read_bytes()
        ok_png = raw[:8] == b"\x89PNG\r\n\x1a\n"
        try:
            res = zxingcpp.read_barcodes(Image.open(out))
            decoded = res[0].text if res else None
        except Exception as e:  # noqa
            decoded = None
        results.append({"payload": p[:24], "ok_png": ok_png,
                        "decoded": bool(decoded), "match": decoded == p})
    ok = all(r.get("match") for r in results)
    return {"decoder": "zxingcpp", "pass": ok, "results": results}


if __name__ == "__main__":
    print(json.dumps(grade(Path(sys.argv[1])), ensure_ascii=False, indent=2))
