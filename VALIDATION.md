# Validation record

Version: `0.1.0`
Date: 2026-09-25
Environment: Windows, Node.js 24.19.0, skills CLI 1.7.0, Python 3.12 for authoring checks.

## Checks performed

| Check | Result and scope |
| --- | --- |
| Skill metadata | OpenAI's bundled `quick_validate.py` accepted the name, description, YAML frontmatter, and completed body. |
| Authenticated connector | The configured GitHub connector returned the publishing account from its authenticated profile API. This verifies that connection path, not every host's GitHub integration. |
| Installer discovery | `skills@1.7.0 add <local-source> --list` found exactly one skill, `github-reuse-first`. |
| Installation | Project-scoped copy installation succeeded with explicit targets `codex claude-code cursor github-copilot` in a disposable directory. No user-wide installation was performed. |
| Installed files | Final packaged skill files were compared with installed copies using SHA-256 hashes, including the references and license notices. |
| Reference integrity | Relative Markdown file links, UTF-8 text, metadata bounds, and absence of author-machine paths or unfinished scaffolding were checked. |
| Upstream review | ECC `search-first` revision `db7f2a6fd5b013d56ec0ba0cfc547ba77baddbce` and its MIT license were inspected. Attribution is included inside the installable skill. |

The installer maps some targets to a shared `.agents/skills` location and Claude Code to `.claude/skills`; the target count is not a count of distinct copies or completed agent sessions.

## Not yet verified

- Actual model behavior in Codex, Claude Code, Cursor, or GitHub Copilot. [Sixteen behavioral scenarios](tests/scenarios.md) are prepared for this purpose; they have not been executed as independent agent sessions.
- A real authenticated `gh` workflow on the author's test host; `gh` was not available on the command path. Public documentation/reference retrieval is not an authenticated workflow test.
- Installation from the intended public repository, `xtltt56-cmd/github-reuse-first`; publication and the remote installation check are pending.
- GitHub or skills-directory search indexing, ranking, or automatic recommendations.

Before advertising production behavior or broad agent compatibility, run representative scenarios in the actual target agents and record the evidence. After publishing, test a fresh installation from the real URL and verify discoverability separately.

## Reproducing installation checks

In a disposable directory, replace the source path with a checkout of this repository:

```shell
npx skills@1.7.0 add /path/to/github-reuse-first-skill --list
npx skills@1.7.0 add /path/to/github-reuse-first-skill --skill github-reuse-first --agent codex claude-code cursor github-copilot --copy --yes
```

These commands test discovery and copying. They do not test a model's decision quality or grant permission for publication.
