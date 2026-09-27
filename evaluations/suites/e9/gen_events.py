"""Generate a single giant JSON array file + expected summary (grader side)."""
import json, random, collections, os, sys

TARGET_MB = 1500
random.seed(42)
types = ["login", "search", "view_item", "add_cart", "purchase", "logout"]
weights = [30, 25, 20, 12, 8, 5]
counts = collections.Counter()
users = collections.Counter()

path = sys.argv[1] if len(sys.argv) > 1 else "events.json"
written = 0
n = 0
first = True
with open(path, "w", encoding="utf-8") as f:
    f.write("[")
    buf = []
    while written < TARGET_MB * 1024 * 1024:
        t = random.choices(types, weights)[0]
        u = f"u{random.randint(0, 999):04d}"
        ev = {"id": n, "type": t, "user": u,
              "ts": f"2026-09-{random.randint(1,28):02d}T{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}Z",
              "bytes": random.randint(64, 8192)}
        counts[t] += 1
        users[u] += 1
        buf.append(json.dumps(ev, separators=(",", ":")))
        n += 1
        if len(buf) >= 20000:
            chunk = ",".join(buf)
            if not first:
                f.write(",")
            f.write(chunk)
            written += len(chunk) + (1 if not first else 0)
            first = False
            buf = []
    if buf:
        if not first:
            f.write(",")
        f.write(",".join(buf))
        written += len("".join(buf))
    f.write("]")

summary = {"total": n, "by_type": dict(counts),
           "top3_users": sorted(users.items(), key=lambda kv: (-kv[1], kv[0]))[:3]}
json.dump(summary, open("expected_summary.json", "w"), indent=1)
print(f"events={n} size={written/1024/1024:.0f}MB")
print(json.dumps(summary, indent=1)[:300])
