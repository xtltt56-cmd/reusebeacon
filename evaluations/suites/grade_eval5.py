"""Grader for eval-5: exact-match compliance against CommonMark 0.31.2 spec.

Grader use only. Loads the official spec examples and runs the candidate's
render_markdown over all of them.
"""
import json
import sys
from pathlib import Path


def grade(project_dir: Path) -> dict:
    project_dir = Path(project_dir)
    sys.path.insert(0, str(project_dir))
    try:
        from markdown_render import render_markdown  # noqa
    finally:
        pass
    spec = json.load(open(Path(__file__).parent / "commonmark" / "spec.json",
                          encoding="utf-8"))
    sections = {}
    total = passed = 0
    fails = []
    for ex in spec:
        total += 1
        sec = ex["section"]
        try:
            got = render_markdown(ex["markdown"])
        except Exception as e:  # noqa
            got = f"<EXCEPTION {type(e).__name__}: {e}>"
        if got == ex["html"]:
            passed += 1
            sections.setdefault(sec, [0, 0])[0] += 1
        else:
            sections.setdefault(sec, [0, 0])[1] += 1
            if len(fails) < 8:
                fails.append({"example": ex["example"], "section": sec,
                              "markdown": ex["markdown"][:60],
                              "expected": ex["html"][:80],
                              "got": got[:80]})
    rate = passed / total
    return {"compliance": round(rate, 4), "passed": passed, "total": total,
            "threshold": 0.90, "pass": rate >= 0.90,
            "sections": {k: f"{v[0]}/{v[0]+v[1]}" for k, v in sorted(sections.items())},
            "first_fails": fails}


if __name__ == "__main__":
    print(json.dumps(grade(Path(sys.argv[1])), ensure_ascii=False, indent=2))
