# GitHub Reuse First

[简体中文](README.md)

[![Validate skill](https://github.com/xtltt56-cmd/github-reuse-first/actions/workflows/validate.yml/badge.svg)](https://github.com/xtltt56-cmd/github-reuse-first/actions/workflows/validate.yml)
[MIT](LICENSE) · [Releases](https://github.com/xtltt56-cmd/github-reuse-first/releases) · [Report a problem](https://github.com/xtltt56-cmd/github-reuse-first/issues)

A portable Agent Skill that checks GitHub access before implementation, finds suitable open-source solutions, evaluates their fit, and integrates and tests the selected solution in the user's project.

## Workflow

1. Verify the agent's actual GitHub authentication and relevant repository access. Guide the user through recovery when needed.
2. Inspect the project's existing implementation, dependencies, environment, and acceptance criteria.
3. Find focused candidates, prioritizing existing dependencies, platform capabilities, official SDKs, and maintained libraries.
4. Assess functional fit, compatibility, license conditions, maintenance evidence, reliability, and total integration cost.
5. Validate the hardest uncertainty, integrate the best fit, and verify actual behavior.

The default workflow waits for verified authentication before GitHub-backed selection and integration. A user's explicit choice to work anonymously or offline takes precedence. Reuse can mean calling an existing dependency; adding another package or copying source is not always necessary.

The search-channel preflight and adopt/extend/compose/build framing were informed by ECC's `search-first`. See [attribution and license](skills/github-reuse-first/THIRD_PARTY_NOTICES.md). This version adds authenticated recovery, portable capability discovery, constraint checks, and end-to-end integration verification.

## Install

Use the open-source [skills CLI](https://github.com/vercel-labs/skills). These examples pin the tested installer to `1.7.0`, which requires Node.js 22.20.0 or a later compatible release. Run from the project where you want to use the skill:

```shell
npx skills@1.7.0 add xtltt56-cmd/github-reuse-first --skill github-reuse-first --copy
```

Or select agents explicitly:

```shell
npx skills@1.7.0 add xtltt56-cmd/github-reuse-first --skill github-reuse-first --agent codex claude-code cursor github-copilot --copy
```

Installation is project-scoped by default; add `--global` only when a user-wide installation is intended. Copy mode avoids symlink permission requirements. To install a downloaded local checkout, run the same command with `.` instead of `xtltt56-cmd/github-reuse-first` from the repository root.

Manual installation is also possible: copy the complete `skills/github-reuse-first` folder into the target agent's supported skills directory. Include its references, not only `SKILL.md`.

## Use

```text
Use github-reuse-first to add CSV import to this project. Check GitHub access,
compare suitable maintained implementations, then integrate and test the best fit.
```

Use `$github-reuse-first` where the agent supports that invocation syntax, or select it through the agent's skill picker. Automatic activation varies by host and model. This skill cannot enforce a universal pre-edit hook. Teams that require it for every implementation task can explicitly reference it in their project instructions and test that behavior in their chosen agent.

## Requirements and compatibility

The skill uses the [Agent Skills format](https://agentskills.io/specification), relative file references, and ordinary host tools. It has no custom runtime or server. Full execution requires project file/terminal access and a configured GitHub connector/MCP integration or GitHub CLI. Optional Codex UI metadata is included in `agents/openai.yaml`.

Installation compatibility is different from verified model behavior. See [validation results](VALIDATION.md) and [behavioral scenarios](tests/scenarios.md).

## Contributing and quality checks

GitHub Actions checks metadata, bundled resources, license consistency, and local references on Linux and Windows for pushes and pull requests. Run these checks in an isolated Python environment:

```shell
python -m pip install -r requirements-dev.txt
python tests/validate_package.py
```

For workflow changes, include a minimal scenario and observed behavior. Reports from additional agents are welcome; distinguish successful installation from demonstrated model behavior. The installer is needed only for distribution, and the Python dependency is needed only for authoring and CI.

## Releases, discovery, and feedback

- [Public repository](https://github.com/xtltt56-cmd/github-reuse-first): source, bilingual documentation, and installation instructions.
- [Releases](https://github.com/xtltt56-cmd/github-reuse-first/releases): version notes and downloadable archives.
- [Issues](https://github.com/xtltt56-cmd/github-reuse-first/issues): report installation, activation, or assessment problems without including secrets or private project data.

Search GitHub for `github-reuse-first`, or browse related topics such as `agent-skills` and `code-reuse`. Third-party directory indexing, ranking, and recommendations are controlled by each platform and are not guaranteed immediately after publication. See [skills.sh documentation](https://skills.sh/docs) for its discovery ecosystem.

GitHub hosting does not automatically list the skill in OpenAI's public plugin directory. That distribution route uses a separate [plugin submission process](https://developers.openai.com/plugins/deploy/submission).

## License

MIT for this repository's original content. Reused third-party code retains its own license and attribution requirements.
