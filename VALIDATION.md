# Validation record

- Version: `0.1.0`
- Date: 2026-09-25
- Environment: Windows, Node.js 24.19.0, skills CLI 1.7.0, Python 3.12 for authoring checks.

## Checks performed

| Check | Result and scope |
| --- | --- |
| Skill metadata | OpenAI's bundled `quick_validate.py` accepted the name, description, YAML frontmatter, and completed body. |
| Authenticated connector | The configured GitHub connector returned the publishing account from its authenticated profile API. This verifies that connection path, not every host's GitHub integration. |
| Installer discovery | `skills@1.7.0 add <local-source> --list` found exactly one skill, `github-reuse-first`. |
| Installation | Project-scoped copy installation succeeded with explicit targets `codex claude-code cursor github-copilot` in a disposable directory. No user-wide installation was performed. |
| Installed files | Final packaged skill files were compared with installed copies using SHA-256 hashes, including the references and license notices. |
| Public installation | A fresh project-scoped install from `xtltt56-cmd/github-reuse-first` succeeded for `codex claude-code cursor github-copilot`. All six installable files matched the published source by SHA-256. Tested skill content was published in commit `c23821803493bf557906cabc362ebf3e42d4f562`. |
| Public access | Unauthenticated retrieval of the raw `SKILL.md` returned HTTP 200 and matched the local published file byte for byte. |
| Continuous integration | Both `Package (ubuntu-latest)` and `Package (windows-latest)` passed in [GitHub Actions run 36106718500](https://github.com/xtltt56-cmd/github-reuse-first/actions/runs/36106718500). These are package checks, not model evaluations. |
| GitHub discovery | Public repository search for `github-reuse-first in:name user:xtltt56-cmd` returned `xtltt56-cmd/github-reuse-first`. Nine relevant repository topics were added. |
| Reference integrity | Relative Markdown file links, UTF-8 text, metadata bounds, and absence of author-machine paths or unfinished scaffolding were checked. |
| Upstream review | ECC `search-first` revision `db7f2a6fd5b013d56ec0ba0cfc547ba77baddbce` and its MIT license were inspected. Attribution is included inside the installable skill. |

The installer maps some targets to a shared `.agents/skills` location and Claude Code to `.claude/skills`; the target count is not a count of distinct copies or completed agent sessions.

## Not yet verified

- Actual model behavior in Codex, Claude Code, Cursor, or GitHub Copilot. [Sixteen behavioral scenarios](tests/scenarios.md) are prepared for this purpose; they have not been executed as independent agent sessions.
- A real authenticated `gh` workflow on the author's test host; `gh` was not available on the command path. Public documentation/reference retrieval is not an authenticated workflow test.
- Third-party skills-directory indexing, ranking, or automatic recommendations. Internal install checks disable telemetry; they are not evidence of organic adoption.

Before advertising production behavior or broad agent compatibility, run representative scenarios in the actual target agents and record the evidence. Future versions should repeat a fresh public installation check; directory indexing and popularity remain separate from package correctness.

## Reproducing installation checks

In a disposable directory:

```shell
npx skills@1.7.0 add xtltt56-cmd/github-reuse-first --list
npx skills@1.7.0 add xtltt56-cmd/github-reuse-first --skill github-reuse-first --agent codex claude-code cursor github-copilot --copy --yes
```

These commands test discovery and copying. They do not test a model's decision quality or grant permission for publication.
