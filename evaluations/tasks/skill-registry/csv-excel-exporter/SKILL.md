---
name: csv-excel-exporter
description: "Harden CSV exports for Excel users: RFC 4180 quoting, UTF-8 BOM, CRLF, and spreadsheet formula-injection defense. Use when exporting user-supplied data to CSV/Excel."
license: MIT
metadata:
  version: "1.2.0"
---

# CSV Excel Exporter

Make CSV exports safe and correct for Excel users.

## Rules

1. **Quoting**: render rows with the standard library `csv.writer` (`QUOTE_MINIMAL`,
   `lineterminator="\r\n"`) on a `StringIO(newline="")`. Never hand-join with
   `",".join` — embedded commas, quotes, and newlines will corrupt rows.
2. **Encoding**: write files as `utf-8-sig` (UTF-8 with BOM) so Excel detects
   UTF-8; Chinese/CJK otherwise mojibakes. Keep `newline=""` on `open()`.
3. **Formula injection (required for user-supplied content)**: cells whose
   first character is one of `= + - @` (or TAB / CR) must be prefixed with a
   single `'` before writing. Otherwise Excel executes `=cmd|...`,
   `+SUM(...)`, `@x` etc. as formulas when the file is opened — a documented
   attack class against exports of end-user data. Apply the guard to every
   cell, then run quoting.
4. **None** maps to an empty cell; preserve the string form of numbers.
5. Verify by round-tripping through `csv.reader` and by checking the first
   file bytes are `EF BB BF`.

## Bundled helper

`scripts/harden_csv.py` provides `guarded_cell(value)` implementing rule 3 and
`rows_to_xlsx_csv(rows, header)` implementing rules 1–4. Prefer importing it
over reimplementing; read it before executing.

## Verification checklist

- [ ] round-trip via csv.reader equals input
- [ ] `=1+1`, `+2`, `-3`, `@x` cells are neutralized
- [ ] first bytes `EF BB BF`; line terminators CRLF
