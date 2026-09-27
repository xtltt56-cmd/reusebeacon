"""Grader for eval-9: correctness + peak RSS + wall time on the 1.5GB file. Grader use only."""
import json
import subprocess
import sys
import time
from pathlib import Path

import psutil


def grade(project_dir: Path, big_file: Path) -> dict:
    project_dir = Path(project_dir)
    out = project_dir / "grader_summary.json"
    start = time.time()
    p = psutil.Popen([sys.executable, "analyze.py", str(big_file), out.name],
                     cwd=project_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    peak = 0
    while p.poll() is None:
        try:
            peak = max(peak, p.memory_info().rss)
        except psutil.Error:
            pass
        time.sleep(0.05)
    rc = p.returncode
    wall = time.time() - start
    report = {"exit": rc, "wall_seconds": round(wall, 1),
              "peak_rss_mb": round(peak / 1024 / 1024, 1),
              "limits": {"wall": 120, "rss_mb": 512}}
    if rc == 0 and out.exists():
        got = json.loads(out.read_text(encoding="utf-8"))
        want = json.loads(Path(__file__).parent.joinpath("e9", "expected_summary.json")
                          .read_text(encoding="utf-8"))
        report["correct"] = (got == want)
    else:
        report["correct"] = False
        report["stderr_tail"] = (p.stderr.read() or b"").decode("utf-8", "replace")[-300:]
    report["pass"] = bool(rc == 0 and report["correct"] and wall < 120 and peak / 1024 / 1024 < 512)
    return report


if __name__ == "__main__":
    print(json.dumps(grade(Path(sys.argv[1]), Path(sys.argv[2])), ensure_ascii=False, indent=2))
