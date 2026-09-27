"""Invoice rendering. Currently text-only; PDF rendering is not implemented."""
import json
import sys
from typing import Dict, List


def render_text(invoice: Dict) -> str:
    lines = []
    lines.append(f"客户名称: {invoice['customer']}")
    lines.append(f"发票号: {invoice['invoice_no']}")
    lines.append(f"开票日期: {invoice['date']}")
    lines.append("-" * 60)
    lines.append(f"{'项目':<30}{'数量':>6}{'单价':>12}{'金额':>12}")
    total = 0.0
    for item in invoice["items"]:
        amount = item["qty"] * item["price"]
        total += amount
        lines.append(f"{item['name']:<30}{item['qty']:>6}{item['price']:>12.2f}{amount:>12.2f}")
    lines.append("-" * 60)
    lines.append(f"合计: {total:.2f} 元")
    return "\n".join(lines)


def render_pdf(invoice: Dict, out_path: str) -> None:
    """Render the invoice as a real PDF file (multi-page, CJK-capable)."""
    raise NotImplementedError("PDF rendering not implemented yet")


def main() -> None:
    if len(sys.argv) != 3:
        print("usage: py -3.12 invoice.py sample.json out.pdf", file=sys.stderr)
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        invoice = json.load(f)
    out = sys.argv[2]
    if out.lower().endswith(".pdf"):
        render_pdf(invoice, out)
    else:
        with open(out, "w", encoding="utf-8") as f:
            f.write(render_text(invoice))
    print(f"written: {out}")


if __name__ == "__main__":
    main()
