# Validation record

- Version: `0.2.0` — ReuseBeacon naming and distribution update
- Date: 2026-09-25
- Authoring environment: Windows, Node.js 24.19.0, skills CLI 1.7.0, Python 3.12.

## Name checks before publication

Authenticated GitHub searches returned zero results for `reusebeacon in:name`, `"reuse-beacon" in:name`, `reusebeacon filename:SKILL.md`, and `"reuse-beacon" filename:SKILL.md`. The responses reported `incomplete_results: false`. Exact-name web queries, including searches scoped to skills.sh and GitHub skill files, did not identify an existing skill using this name.

These are point-in-time checks over available indexes, not a guarantee that every private or unindexed project has been checked. The reason for changing the old identifier and the upgrade procedure are documented in [MIGRATION.md](MIGRATION.md).

## Version 0.2.0 checks

| Check | Result and scope |
| --- | --- |
| Local skill/package validation | Pending final renamed-package check. |
| Fresh public installation | Pending installation from `xtltt56-cmd/reusebeacon`. |
| Linux and Windows CI | Pending checks on the renamed repository. |
| Legacy URLs and release assets | Pending public redirect and download verification. |
| Search visibility | Pending repository search after rename. |

## Prior release evidence

The `v0.1.0` release completed fresh public installation for Codex, Claude Code, Cursor, and GitHub Copilot; all six installed files matched the published source by SHA-256. Public raw-file retrieval and GitHub repository search succeeded. Linux and Windows package validation passed. See the [historical validation record](https://github.com/xtltt56-cmd/reusebeacon/blob/v0.1.0/VALIDATION.md) for its original evidence.

This naming update preserves the workflow and both supporting references. Earlier installation checks do not substitute for verification of the new identifier and URLs.

## Limits

- Actual model behavior across all advertised agents has not been independently evaluated. [Sixteen behavioral scenarios](tests/scenarios.md) are prepared; they are not claims of completed tests.
- The author's GitHub connection and publication use an authenticated connector and existing Git credentials. A real `gh` browser-login workflow has not been tested on this host because `gh` is absent.
- Third-party skills-directory indexing, ranking, and recommendations are unverified. Internal installation checks disable telemetry and are not evidence of organic adoption.
- Some installation targets share `.agents/skills`; Claude Code uses `.claude/skills`. Four selected targets do not imply four completed model sessions.

## Reproduce package and installation checks

In an isolated Python 3.10+ environment:

```shell
python -m pip install -r requirements-dev.txt
python tests/validate_package.py
```

In a disposable project directory:

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --list
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --agent codex claude-code cursor github-copilot --copy --yes
```

The installer commands require Node.js 22.20.0 or a later compatible version. They test discovery and copying, not model decision quality.
