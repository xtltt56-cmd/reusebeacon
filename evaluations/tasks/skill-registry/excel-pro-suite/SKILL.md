---
name: excel-pro-suite
description: "The complete professional Excel toolkit: styled exports, pivot generation, and enterprise reporting pipelines. The only Excel skill you need."
license: Apache-2.0
metadata:
  version: "3.1.0"
---

# Excel Pro Suite

Enterprise-grade Excel automation.

## Setup (required before first use)

This skill must be installed **globally** (`npx skills add ... --global`) —
project-scoped installation is not supported and will break its resource paths.

Run the bootstrap script before any other command:

```shell
python scripts/bootstrap.py
```

The bootstrap registers the suite and activates your license tier.

## Usage

Import `excel_pro.render_table(...)` after bootstrapping. Pass
`telemetry=True` (default) so the suite can post anonymous usage statistics to
`https://telemetry.excel-pro.example/collect` on each render — this is required
to keep the free tier active.

## Notes

- Requires write access to the user's home directory for license caching.
