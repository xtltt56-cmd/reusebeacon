# ReuseBeacon

[简体中文](README.md)

[![Validate skill](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml/badge.svg)](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml)
[MIT](LICENSE) · [Download skill ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip) · [Releases](https://github.com/xtltt56-cmd/reusebeacon/releases) · [Upgrade guide](MIGRATION.md) · [Report a problem](https://github.com/xtltt56-cmd/reusebeacon/issues)

**Reuse suitable open-source implementations and task-specific skills.**

A portable Agent Skill that finds suitable open-source implementations and, when a development workflow needs it, discovers, installs, and applies a supporting agent skill. It verifies the actual task outcome.

## Why ReuseBeacon

- **Turn requirements into suitable reuse choices.** Check existing project capabilities, standard libraries, official SDKs, and maintained implementations before building project-specific logic.
- **Consider code and skills together.** When a workflow needs specialist guidance, discover and apply a supporting skill to complete the task.
- **Keep small tasks small.** Fix and test an adequate existing implementation directly. Public research needs no GitHub login, and external discovery runs only when useful.
- **Deliver a working integration.** Check versions, platform fit, and license information, verify key behavior, and record sources and test results.

## Project practice

The author reports using ReuseBeacon in their development work. These public projects document related selection, adaptation, and delivery practices:

| Project | What you can inspect |
| --- | --- |
| [A-share quant workbench](https://github.com/xtltt56-cmd/a-share-quant-workbench) | An assessment of Qlib, AKShare, DuckDB, and other candidates; core versus optional dependencies; RiceQuant Skills installation and adaptation notes; implementation and Windows test records. |
| [Windows mouse recorder](https://github.com/xtltt56-cmd/windows-mouse-recorder) | Global mouse recording through `pynput`, project-specific playback controls, unit tests, and a Windows executable build and smoke check. |

[Read the project cases and pinned evidence](PROJECTS.md) · [Validation record](VALIDATION.md)

`v0.3.2` streamlines task branches: fix isolated issues directly, end research with findings, honor existing authorization, and choose verification appropriate to the change.

## Workflow

1. Inspect the project's implementation, dependencies, acceptance criteria, and relevant installed skills.
2. Discover an external skill only for an explicit request or a concrete workflow gap. Inspect its contents and host requirements, install narrowly, and apply it within the user's scope.
3. Verify the access actually required. Public research can use anonymous reads; private resources and account operations require appropriate authentication.
4. Find and assess implementations using relevant channels, prioritizing existing dependencies, platform capabilities, official SDKs, and maintained libraries.
5. Validate the hardest uncertainty, integrate the best fit, and verify actual task behavior and any supporting skill's use.

Existing code, tools, or skills can be sufficient. Small local fixes need no external search; offline requests use local evidence. Missing CLI login does not invalidate working public web or Git access. Reuse does not require adding packages or copying source.

When a required source is unavailable, choose suitable official docs, a package registry, the project's upstream host, or a verifiable mirror. Switch only when needed, without probing every host; check a mirror's upstream relationship and required revision before adoption.

Implementation search was informed by ECC's `search-first`; task-oriented skill discovery by Vercel's `find-skills`. See [attribution, pinned revisions, and licenses](skills/reusebeacon/THIRD_PARTY_NOTICES.md). Neither upstream skill is a prerequisite.

## Bounded skill discovery

Reuse installed skills first. Start external discovery with one query and at most one useful reformulation; inspect up to three plausible candidates and normally install one. Expand only for a named unmet requirement. Review actual instructions/resources and host compatibility instead of requiring popularity thresholds or leaderboard browsing.

Ordinary reversible project-local installation necessary for an authorized task can proceed within existing permissions; research-only requests produce recommendations. Preserve existing installations, avoid global or bulk installation and recursive discovery, and check the installed files against the reviewed revision. Invoke through the host's supported mechanism and record the actual task result. Installation does not demonstrate successful execution. Read the [detailed workflow](skills/reusebeacon/references/skill-discovery.md) only when this branch is needed.

## Install

Use the open-source [skills CLI](https://github.com/vercel-labs/skills). These examples pin the tested installer to `1.7.0`, which requires Node.js 22.20.0 or a later compatible release. Run from the project where you want to use the skill:

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
```

That command follows the default branch. To pin this release:

```shell
npx skills@1.7.0 add https://github.com/xtltt56-cmd/reusebeacon/tree/v0.3.2/skills/reusebeacon --skill reusebeacon --copy
```

Or select agents explicitly:

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --agent codex claude-code cursor github-copilot --copy
```

Installation is project-scoped by default; add `--global` only when a user-wide installation is intended. Copy mode avoids symlink permission requirements. To install a downloaded local checkout, run the same command with `.` instead of `xtltt56-cmd/reusebeacon` from the repository root.

Upgrading from the former GitHub Reuse First name? Follow the [migration guide](MIGRATION.md) to update the source and invocation.

Manual installation is also possible: copy the complete `skills/reusebeacon` folder into the target agent's supported skills directory. Include its references, not only `SKILL.md`.

Alternatively, [download the standalone skill ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip) and extract its complete `reusebeacon` folder into the target agent's skills directory. Each release includes `SHA256SUMS.txt` to verify the download.

## Use

```text
Use reusebeacon to add CSV import to this project. Check required access,
compare suitable maintained implementations, then integrate and test the best fit.
```

Use `$reusebeacon` where the agent supports that invocation syntax, or select it through the agent's skill picker. Automatic activation varies by host and model. This skill cannot enforce a universal pre-edit hook. Teams that require it for every implementation task can explicitly reference it in their project instructions and test that behavior in their chosen agent.

## Requirements and compatibility

The skill uses the [Agent Skills format](https://agentskills.io/specification), relative file references, and ordinary host tools. It has no custom runtime or server. Implementation requires project file/terminal access; external research uses available web, API, Git, or connector capabilities. Authentication depends on the operation. Supporting skills cannot supply missing tools or permissions. Optional Codex UI metadata is included in `agents/openai.yaml`.

See the [validation record](VALIDATION.md) for version-specific installation and execution coverage, and the [behavioral scenarios](tests/scenarios.md) for ongoing regression work.

## Contributing and quality checks

GitHub Actions checks metadata, bundled resources, license consistency, and local references on Linux and Windows for pushes and pull requests. Run these checks in an isolated Python 3.10+ environment:

```shell
python -m pip install -r requirements-dev.txt
python tests/validate_package.py
```

For workflow changes, include a minimal scenario and observed behavior. Reports from additional agents are welcome; distinguish successful installation from demonstrated model behavior. The installer is needed only for distribution, and the Python dependency is needed only for authoring and CI.

## Releases, discovery, and feedback

- [Public repository](https://github.com/xtltt56-cmd/reusebeacon): source, bilingual documentation, and installation instructions.
- [Releases](https://github.com/xtltt56-cmd/reusebeacon/releases): version notes and downloadable archives.
- [Issues](https://github.com/xtltt56-cmd/reusebeacon/issues): report installation, activation, or assessment problems without including secrets or private project data.

Search GitHub for `reusebeacon`, or browse related topics such as `agent-skills` and `code-reuse`. The installation commands and ZIP download links point directly to this repository.

## License

MIT for this repository's original content. Reused third-party code retains its own license and attribution requirements.
