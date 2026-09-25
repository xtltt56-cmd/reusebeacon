# Validation record

## Version 0.3.0

- Date: 2026-09-25.
- Scope: optional task-specific skill discovery, inspection, project installation, loading, and outcome evidence; operation-specific GitHub access replaces mandatory authentication for public research.
- Reviewed upstream: Vercel `find-skills` at `7407f3893ad4dceab546ac002c3ef806e4000c73`, including its MIT license. Source attribution is bundled with the skill.

| Check | Observed result and limits |
| --- | --- |
| Package validation | `python tests/validate_package.py` passed metadata, bundled resources, license consistency, and local references. |
| Authoring validator | The skill-creator `quick_validate.py` passed using Python 3.12.14, PyYAML 6.0.3, and UTF-8 mode on Windows. The initial runtime lacked PyYAML; existing isolated validation dependencies were reused. The validator's default GBK read failed until UTF-8 mode was enabled for the process. |
| CLI syntax | Existing skills CLI 1.7.0 reported its version and confirmed the documented `find`, `--list`, `--skill`, `--agent`, `--copy`, and `--yes` options. This was a syntax check, not a live CLI directory search. |
| Isolated local installation | From a disposable project on D:, `skills add <local-checkout> --list` discovered exactly one skill; `skills add <local-checkout> --skill reusebeacon --agent claude-code --copy --yes` installed it to `.claude/skills/reusebeacon`. All seven installed files matched the working source by SHA-256. Telemetry was disabled. This used a local checkout, not the public repository or a model session. |
| Release archive | All seven files in the prepared `reusebeacon.zip` matched the source. Archive SHA-256: `033aa2ef6866072961ccb5e23d50d9c74a4329c56f4b9c936e583530b5b236de`. The legacy filename alias has identical contents. Public download verification follows publication. |
| Entrypoint size | Whitespace-delimited word count changed from 1,286 to 1,253. The new conditional reference contains 808 words. These are file measurements, not token, latency, or cost savings. |
| Behavioral evaluation | Cases 17–24 were added and access cases revised in the [scenario list](tests/scenarios.md). No model behavior runs were performed for this update; automatic selection, loading, usefulness, and cost remain unverified. |

Do not replace the pinned skill snapshot in an ongoing comparison with this working tree. Evaluate the new workflow as a separate version, with the same tasks, model, tool access, and permissions. Package checks and manual file comparisons cannot establish a behavioral advantage.

## Published v0.2.0 record

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

- Actual model behavior across all advertised agents has not been independently evaluated. [Sixteen v0.2.0 behavioral scenarios](https://github.com/xtltt56-cmd/reusebeacon/blob/v0.2.0/tests/scenarios.md) were prepared; they are not claims of completed tests.
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
