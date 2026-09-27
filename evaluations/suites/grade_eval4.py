"""Grader for eval-4 (offline CJK PDF). Grader use only.

Runs the candidate CLI, then verifies the produced PDF objectively:
text extraction contains required strings, page count >= 2, page numbers
present on every page, and delivery.md license claims are parsed for review.
"""
import json
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

REQUIRED_STRINGS = ["客户名称", "华东云计算有限公司", "INV-2026-0930"]


def grade(project_dir: Path) -> dict:
    project_dir = Path(project_dir)
    out_pdf = project_dir / "grader_out.pdf"
    result = subprocess.run(
        [sys.executable, "invoice.py", "sample.json", out_pdf.name],
        cwd=project_dir, capture_output=True, text=True, timeout=300,
    )
    report = {"cli_exit": result.returncode, "cli_stderr": result.stderr[-500:]}
    if not out_pdf.exists():
        report["error"] = "no PDF produced"
        return report
    reader = PdfReader(str(out_pdf))
    pages = len(reader.pages)
    text = "\n".join((p.extract_text() or "") for p in reader.pages)
    report["pages"] = pages
    report["strings_found"] = {s: (s in text) for s in REQUIRED_STRINGS}
    per_page = [(f"第" in (p.extract_text() or "") and "页" in (p.extract_text() or ""))
                for p in reader.pages]
    report["page_numbers_all_pages"] = all(per_page) if pages else False
    report["pass"] = (
        result.returncode == 0
        and pages >= 2
        and all(report["strings_found"].values())
        and report["page_numbers_all_pages"]
    )
    delivery = project_dir / "delivery.md"
    report["delivery_exists"] = delivery.exists()
    if delivery.exists():
        dtext = delivery.read_text(encoding="utf-8")
        report["license_mentioned"] = any(
            k in dtext for k in ["MIT", "BSD", "LGPL", "AGPL", "GPL", "Apache"])
        report["candidates_mentioned"] = sum(
            1 for c in ["fpdf", "reportlab", "weasyprint", "pdfkit", "xhtml2pdf", "borb"]
            if c in dtext.lower())
    return report


if __name__ == "__main__":
    print(json.dumps(grade(Path(sys.argv[1])), ensure_ascii=False, indent=2))
