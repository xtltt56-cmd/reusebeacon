"""Issue export. Minimal placeholder — not Excel-safe yet."""
import json
from typing import List, Dict


def export_issues(issues: List[Dict], out_path: str) -> None:
    """Export issue rows to `out_path` as Excel-compatible CSV."""
    header = ["id", "title", "body", "reporter", "labels"]
    lines = [",".join(header)]
    for it in issues:
        cells = [
            str(it.get("id", "")),
            str(it.get("title", "")),
            str(it.get("body", "")),
            str(it.get("reporter", "")),
            ";".join(it.get("labels", [])),
        ]
        lines.append(",".join(cells))
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    import sys
    with open(sys.argv[1], encoding="utf-8") as f:
        export_issues(json.load(f), sys.argv[2])
    print(f"written: {sys.argv[2]}")
