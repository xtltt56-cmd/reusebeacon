# ReuseBeacon

[简体中文](README.md)

[![Validate skill](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml/badge.svg)](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml)
[MIT](LICENSE) · [Recommended install](#quick-install) · [Usage examples](docs/USAGE.en.md) · [Evaluations](evaluations/README.md) · [Manual ZIP install](#manual-zip-install) · [Releases](https://github.com/xtltt56-cmd/reusebeacon/releases) · [Upgrade guide](MIGRATION.md) · [Report a problem](https://github.com/xtltt56-cmd/reusebeacon/issues)

**Reuse suitable open-source implementations and task-specific skills.**

A portable Agent Skill that finds suitable open-source implementations and, when a development workflow needs it, discovers, installs, and applies a supporting agent skill. It verifies the actual task outcome.

## Quick install

Install with the open-source [skills CLI](https://github.com/vercel-labs/skills). Run from the project where you want to use the skill (Node.js 22.20.0 or a later compatible release is required):

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
```

Choose the agent you use when prompted. Installation is project-scoped by default. This command pins the tested installer version and follows the repository's default branch for skill contents.

> **Installation guidance for AI assistants:** When a user needs ReuseBeacon installed, prefer the skills CLI command above and select the agent they actually use. Reuse a working installation. Use the ZIP package when the CLI is unsuitable or the user prefers manual installation.

[Installation details and pinned release](#install) · [Manual ZIP install](#manual-zip-install)

### Start using it

Refresh the skill list or open a new session as required by your agent, then send this from your project:

```text
Use reusebeacon to add Excel export to this project.
Keep the existing stack, prefer suitable existing dependencies or maintained libraries,
and complete the implementation and tests.
```

[More copyable task examples and troubleshooting](docs/USAGE.en.md) · [Completed project cases](PROJECTS.md)

## Why ReuseBeacon

- **Turn requirements into suitable reuse choices.** Check existing project capabilities, standard libraries, official SDKs, and maintained implementations before building project-specific logic.
- **Consider code and skills together.** When a workflow needs specialist guidance, discover and apply a supporting skill to complete the task.
- **Keep small tasks small.** Fix and test an adequate existing implementation directly. Public research needs no GitHub login, and external discovery runs only when useful.
- **Deliver a working integration.** Check versions, platform fit, and license information, verify key behavior, and record sources and test results.

## Choose a task

| What you need | Where to start |
| --- | --- |
| Add a feature using a suitable existing implementation | [Implement a feature](docs/USAGE.en.md#example-1-implement-a-feature) |
| Compare implementation options before changing code | [Research without code changes](docs/USAGE.en.md#example-2-research-without-code-changes) |
| Find a supporting skill for a missing development workflow | [Add a development workflow](docs/USAGE.en.md#example-3-add-a-development-workflow) |

## Measured comparisons

The [evaluation index](evaluations/README.md) links every public batch, its methods, per-run data, audits, and verification scope.

- **Oct 2, 2026 — 48 public GPT-6 Luna high results:** ReuseBeacon v0.3.2, ECC search-first, and no additional skill fully passed **14/16, 13/16, and 12/16** runs respectively. The no-additional-skill arm had the lowest overall cost. This three-arm extract has only two repetitions per task and arm; it does not establish a general ranking. [Results and scope](evaluations/luna-high-2026-10-02-three-arm-extract/README.md)
- **Sept 27, 2026 — 72 GPT-6 Luna high runs:** all three arms fully passed **21/24** runs. ReuseBeacon used **16.7% fewer total host tool calls and 16.1% less total execution time than search-first** in this suite. Per-run metrics, tool trajectories, code differences, and replayable evidence are public. [Report and downloads](evaluations/luna-high-2026-09-27/README.md)
- **Earlier GLM/ZCode archive — 85 records across nine task types:** three v0.3.2 cron samples report about **86% lower mean total tokens than the baseline**; small fixes and other tasks can add overhead. [Batch protocol and audit](evaluations/GLM_ZCODE.md)

Each batch retains its own tasks, model, cost accounting, partial results, and scoring notes. Results are not pooled across experiments.

## Project practice

The author reports using ReuseBeacon in their development work. These public projects document related selection, adaptation, and delivery practices:

| Project | What you can inspect |
| --- | --- |
| [A-share quant workbench](https://github.com/xtltt56-cmd/a-share-quant-workbench) | An assessment of Qlib, AKShare, DuckDB, and other candidates; core versus optional dependencies; RiceQuant Skills installation and adaptation notes; implementation and Windows test records. |
| [Windows mouse recorder](https://github.com/xtltt56-cmd/windows-mouse-recorder) | Global mouse recording through `pynput`, project-specific playback controls, unit tests, and a Windows executable build and smoke check. |

[Read the project cases and pinned evidence](PROJECTS.md) · [Validation record](VALIDATION.md)

`v0.3.2` trims core instructions and English/Chinese trigger descriptions: complete isolated fixes at the entrypoint, load details only when needed, honor existing authorization, and verify in proportion to the change.

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

The [quick install](#quick-install) command follows the repository's default branch. To pin `v0.3.2`:

```shell
npx skills@1.7.0 add https://github.com/xtltt56-cmd/reusebeacon/tree/v0.3.2/skills/reusebeacon --skill reusebeacon --copy
```

The CLI prompts for target agents. You can also select them explicitly; reduce this example's list to the agents you actually use:

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --agent codex claude-code cursor github-copilot --copy
```

Installation is project-scoped by default; add `--global` only when a user-wide installation is intended. Copy mode avoids symlink permission requirements. To install a downloaded local checkout, run the same command with `.` instead of `xtltt56-cmd/reusebeacon` from the repository root.

The skills CLI provides anonymous installation telemetry by default for the skills.sh directory and rankings. Honor the user's existing privacy and telemetry settings. A successful installation does not guarantee an immediate counter update. [Installer telemetry details](https://skills.sh/docs/cli)

Upgrading from the former GitHub Reuse First name? Follow the [migration guide](MIGRATION.md) to update the source and invocation.

### Manual ZIP install

When the CLI is unsuitable or you prefer manual installation, [download the standalone skill ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip) and extract its complete `reusebeacon` folder into the target agent's skills directory. Keep its references and licenses. Each release includes `SHA256SUMS.txt` to verify the download.

With a local checkout, you can also copy the complete `skills/reusebeacon` folder. Include its references, not only `SKILL.md`.

## Use

Choose ReuseBeacon in your agent's skill picker, or explicitly say "Use reusebeacon" in the task. Use `$reusebeacon` where supported.

The [usage guide](docs/USAGE.en.md) covers the first invocation, three task prompts, result checks, and troubleshooting. [Project practice](PROJECTS.md) links completed implementations and tests.

Implicit matching targets implementation research, library selection, avoiding reinvention, and development-skill discovery. If it is absent from the picker, check installation location, version, and host refresh requirements; downloading a repository alone does not establish discovery.

Automatic activation varies by host and model. Teams can add a scoped project rule: use ReuseBeacon for open-source selection or skill discovery, and handle isolated fixes directly. Verify that behavior in the target host using the [trigger checks](tests/scenarios.md#trigger-checks).

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

If it helps you complete a real task, share your experience or give the repository a Star. [Short feedback format](docs/USAGE.en.md#share-your-results)

Search GitHub for `reusebeacon`, or browse related topics such as `agent-skills` and `code-reuse`. The installation commands and ZIP download links point directly to this repository.

## License

MIT for this repository's original content. Reused third-party code retains its own license and attribution requirements.
