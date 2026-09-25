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
| Local skill/package validation | Passed metadata, bundled resources, license consistency, local Markdown references, and the authoring skill validator. The decision workflow and supporting references are unchanged from v0.1.0. |
| Fresh public installation | skills CLI 1.7.0 cloned `xtltt56-cmd/reusebeacon`, discovered exactly one skill named `reusebeacon`, and installed it for Codex, Claude Code, Cursor, and GitHub Copilot. All six files in each of the two copied skill directories matched the source by SHA-256. |
| Linux and Windows CI | Both package jobs passed at commit `264e5948a50c5f0605bc89d6d50c60154e224846`: [run 36110165087](https://github.com/xtltt56-cmd/reusebeacon/actions/runs/36110165087). |
| Legacy repository and v0.1.0 download | The old repository URL returned HTTP 200 after redirecting to `xtltt56-cmd/reusebeacon`. The original v0.1.0 ZIP remained downloadable through its old URL and retained SHA-256 `50013ae919ff9afe9a0a7e04372a36e84f1c19cf2ff3c7ba9b0cce65bb4bfb19`. The v0.2.0 assets are checked separately when publishing the release. |
| Search visibility | GitHub repository search for `reusebeacon in:name` returned exactly one result after renaming: `xtltt56-cmd/reusebeacon`. This does not establish search-engine ranking or third-party directory inclusion. |

The first local Git clone failed with a connection reset. Python's network client used this host's existing system proxy, while Git had no proxy configured. Repeating the public installation with the same proxy supplied only to that command succeeded. No global Git configuration or certificate verification was changed. Installation checks used a disposable project and disabled telemetry.

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
