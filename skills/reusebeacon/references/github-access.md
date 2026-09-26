# GitHub access and public-source recovery

Use these instructions when choosing required GitHub access or recovering an unavailable public source. Keep existing account configuration and repositories intact. Local tasks and installed-skill use do not require a GitHub check.

## When a public source is unavailable

Use the first failed necessary read as evidence; do not probe every host beforehand. A failed website does not invalidate working API or Git access. When that route remains unavailable, choose one suitable alternative for the missing information: local/versioned docs, the official package registry, the project's actual upstream host, or a verifiable mirror. Follow official project links; Gitee and GitLab may host an upstream or a mirror, so establish which it is. Follow the [provenance checks](selection.md) before adopting mirrored material.

Stop when the evidence is sufficient. If the alternative is also unavailable or unverifiable, continue feasible local work and identify the unresolved requirement; expand only for a concrete need. Honor offline requests. A public mirror cannot supply private permissions or authorize moving the user's repository or data to another host.

For package downloads, keep existing registry configuration where it works. If a trusted alternative is necessary, scope changes to the command or project and preserve locked versions, integrity checks, and TLS verification.

## Choose the existing access path

For public research or downloads, use a working web tool, public API, or HTTPS Git access. Verify the actual relevant read; no plugin or login is mandatory. Some operations, such as authenticated API code search, require credentials even when their targets are public. Choose the access needed for that operation.

For authenticated operations, a working GitHub connector or MCP tool is sufficient; do not force GitHub CLI installation. Inspect its available operations and make the smallest appropriate authenticated read. A public search result alone does not prove login or private repository access. If the integration cannot verify required access, report that limit and use a supported alternative.

With a terminal, check the official GitHub CLI:

```text
gh --version
gh auth status --active --hostname github.com
gh api --hostname github.com user --jq .login
```

Use the actual hostname for an enterprise instance. A failing inactive account should not invalidate a working active account for the selected host. Older CLIs may lack `--active`; inspect their help and evaluate the selected account rather than repeatedly retrying unsupported flags.

Do not use `gh auth status --json`'s process exit code as proof of authentication: the CLI documents that this form may exit zero even when authentication has issues. Do not call `gh auth token`, use `--show-token`, print token environment variables, or include authentication output containing secrets in reports.

When a repository is required, check just that repository:

```text
gh api --hostname github.com repos/OWNER/REPO --jq .full_name
```

`OWNER/REPO` is a placeholder for a verified repository name. A 404 may indicate either an incorrect name or lack of access; do not conclude that a private repository does not exist. The local project does not need a GitHub remote merely to research open-source solutions.

## Recover according to the evidence

| Observation | Appropriate next step |
| --- | --- |
| No usable connector and `gh` missing | Public research may use web or HTTPS Git. If the operation needs authenticated API access, offer a supported host connection or official GitHub CLI setup from https://cli.github.com/. Follow existing authorization and host policy for environment changes. |
| No active account or invalid credentials | When authentication is required, guide the user through `gh auth login --hostname github.com --web`, then repeat the authenticated read. Otherwise use working public access. Let the user complete browser/device authorization. |
| Wrong account | Explain the account mismatch. Use the documented `gh auth switch` flow only after the intended account is established. |
| Identity read succeeds but repository read fails | Inspect repository name, permissions, and applicable organization SSO. Do not request broader scopes than the task requires. |
| HTTP 403 or 429 | Check the response evidence for rate limits or access policy. Respect retry timing; a 403 is not automatically an expired login. |
| DNS, timeout, proxy, or TLS error | Diagnose the actual network problem. Keep certificate checks enabled. Avoid repeated login or reinstall attempts for a network failure. |
| Environment-supplied token overrides stored login | Tell the user that the configured automation credential may need correction in their secret store. Do not print, export, or silently unset it. |

Use bounded timeouts where the host supports them. Retry only when a transient cause is supported by evidence; do not loop indefinitely. If connection still requires user action, say exactly which action is needed and continue independent local inspection.

Do not create/upload SSH keys or change Git credential defaults merely to enable research. Preserve existing Git settings; `--skip-ssh-key` is available when the CLI browser-login flow would otherwise offer key setup.

The browser login flow normally uses the system credential store, but the CLI may fall back to a file if secure storage is unavailable. Do not force insecure storage or silently create a plaintext token file. If secure storage cannot be used, explain the actual condition and let the user choose a suitable credential setup.

Label anonymous public access accurately; do not imply private access or authenticated identity. Recover only access required by the task. Respect an offline instruction and keep independent local work moving if recovery needs user action.

## Search after access is verified

The following are templates; replace example terms with the task's actual stack and capability. Reuse available structured tools when they provide the same information.

```text
gh search repos "streaming csv" --language Python --visibility public --archived=false --limit 5 --json fullName,url,description,isArchived,pushedAt,stargazersCount,license
gh search code "read_csv" --repo OWNER/REPO --limit 5 --json path,url
gh api repos/OWNER/REPO/releases/latest
gh api repos/OWNER/REPO/license
```

An empty result is not proof that a feature or project does not exist. GitHub CLI code search can differ from GitHub's website search; inspect the candidate's versioned docs and source directly. A missing latest release or API license classification is a reason to inspect tags/LICENSE, not a maturity verdict.

For GitHub Enterprise, use the documented per-command hostname option where available, or a process-scoped `GH_HOST` for commands that require it. Do not permanently change the user's default host. Verify public GitHub access separately if the research will use github.com.

## Official references

- [GitHub CLI installation](https://github.com/cli/cli#installation)
- [Authentication status and JSON exit behavior](https://cli.github.com/manual/gh_auth_status)
- [Browser login and credential storage](https://cli.github.com/manual/gh_auth_login)
- [Repository search and supported JSON fields](https://cli.github.com/manual/gh_search_repos)
- [Code search behavior](https://cli.github.com/manual/gh_search_code)
- [CLI host and environment settings](https://cli.github.com/manual/gh_help_environment)
