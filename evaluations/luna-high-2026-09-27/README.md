# GPT-6 Luna high — 72-run comparison

ReuseBeacon v0.3.2 / ECC search-first / no additional general reuse skill. Eight tasks, three repetitions per arm, 2026-09-27.

| Arm | Fully passing runs | Host tool calls (total) | Uncached input tokens (total) | Agent wall seconds (total) |
| --- | ---: | ---: | ---: | ---: |
| ReuseBeacon | 21/24 | 368 | 517,553 | 8,026 |
| search-first | 21/24 | 442 | 1,059,121 | 9,562 |
| No general skill | 21/24 | 357 | 630,873 | 7,625 |

ReuseBeacon used 16.7% fewer host tool calls and 16.1% less total wall time than search-first in this suite, at the same full-pass rate. Relative to the no-general-skill arm, its paired median call/time changes were +2.9%/+3.1%. Totals and paired medians answer different questions. These are observed proxies, not a billing estimate or a universal benefit.

All remaining partial runs are T5; the frozen grader conflicts with a task instruction for empty output and tests exact CommonMark serialization. Raw scores and the audit are retained. Shared instructions already encouraged reuse, and several tasks named existing dependencies; native automatic activation was not measured.

- [Full report / 完整中文报告](REPORT.md)
- [72 per-run rows (CSV)](runs.csv) · [Detailed summary](SUMMARY.json) · [Aggregates](ANALYSIS.json)
- [Frozen source and grader hashes](MANIFEST.json) · [Grader audit](GRADER_AUDIT.md) · [Protocol deviations](PROTOCOL_DEVIATIONS.json)
- [Full evidence ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/download/eval-luna-high-2026-09-27/reusebeacon-luna-high-3arm-2026-09-27.zip) · [Release](https://github.com/xtltt56-cmd/reusebeacon/releases/tag/eval-luna-high-2026-09-27) · [SHA-256](SHA256SUMS.txt)
- [Publication replay](PUBLICATION_REPLAY.json): all 72 exported outputs rescored with identical results, including nine real-browser checks. 63 runs fully pass; nine T5 scores remain partial. No additional model samples were generated for this replay.

The ZIP includes prompts, baseline/final code, code diffs, frozen tests, skill snapshots with notices, test outputs and 86 sanitized session trajectories (81 canonical and five excluded). `verify_evidence.py` checks hashes and telemetry; `replay.py` reruns external scoring on project copies. Python dependencies are pinned; T7 retains its documented Windows Playwright CLI prerequisite. No private reasoning, credentials or unrelated conversation history is included. The two T8 secret strings are synthetic test canaries.

Archive SHA-256: `279ad7e71c75ae22ee4134083d40a545ad7433ffe1bedf25ff85068ddd3d1709`.

This evidence release does not change the seven-file installable skill or replace v0.3.2 as the latest installable release.
