"""Event log analytics. Not implemented yet."""
import json
import sys


def analyze(events_path: str, out_path: str) -> None:
    """Summarize a giant JSON-array events file within the README limits."""
    raise NotImplementedError("analyze not implemented yet")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: py -3.12 analyze.py events.json out.json", file=sys.stderr)
        sys.exit(2)
    analyze(sys.argv[1], sys.argv[2])
    print(f"written: {sys.argv[2]}")
