# Candidate assessment and reuse

Apply this assessment to a real implementation decision. Scale the depth to the cost and risk; a small use of an existing dependency does not need a formal report.

## Establish whether the candidate can be used

First screen for required behavior, platform/version fit, and identifiable source/license. Investigate the remaining criteria only for plausible finalists, at a depth matching the integration risk. Popularity cannot compensate for a failed requirement.

- It demonstrably supports the necessary behavior on the target platform/runtime, or a small verified adaptation covers the gap.
- Identify the license text, relevant bundled notices, revision, and intended use (dependency, copied source, or service). Record evident requirements and unresolved questions against the user's stated constraints; do not claim legal clearance. If a material question remains, prefer an alternative with clearer terms or seek relevant guidance before adoption. Public readability or an API license label alone does not establish permission to copy every file.
- Its provenance is credible: package, repository, maintainers, version, and documentation refer to the same implementation. Check official links rather than trusting a similarly named package. For mirrors, establish the upstream relationship and required revision using maintainer links, trusted package metadata, or previously verified refs/checksums. A matching name is insufficient. Mirror sync time is not upstream maintenance activity; if currency cannot be verified, do not claim it is the latest release.
- Known unresolved vulnerabilities or unsafe behavior relevant to this use have a credible fix or mitigation. Do not call a dependency secure simply because no advisory was found.
- Required external services, data transfers, infrastructure, and ongoing costs fit the task's authorized constraints.

## Compare suitable candidates

| Dimension | Evidence to inspect | Interpretation |
| --- | --- | --- |
| Functional fit | Versioned API docs, maintained examples, tests, relevant source | Verify required edge cases; a similar screenshot or project name is insufficient. |
| Compatibility | Supported versions, platform matrix, dependency graph, packaging | Prefer a fit with the existing stack over framework migrations or runtime downgrades. |
| Maintenance and community | Release history, maintainer responses, relevant issues/fixes, contributor continuity | Judge activity in context. Stars and downloads show visibility, not support quality. A stable library may need few commits; a fresh commit may be automated. |
| Reliability | Relevant tests and CI, error handling, issue history, documented production use | Demonstrated behavior matters more than stars, forks, or unqualified claims. |
| Documentation | Getting-started path, versioned examples, migration notes | Estimate the work required for another maintainer to operate and update it. |
| Total cost | Integration, dependencies, operations, upgrades, customization | Include future ownership; the broadest framework may cost more than a focused library. |

Use qualitative conclusions tied to evidence. Avoid a fabricated numerical score or a universal stars/recency threshold. Archived projects need an explicit maintenance explanation, especially for networked or security-sensitive components.

Prefer official SDKs and existing compatible dependencies when they meet the requirements. Keep a table only as large as the real choice warrants:

| Candidate and ref | Fit and evidence | Cost or limitation | Decision |
| --- | --- | --- | --- |
| Repository/package link and version | Required capability and verification source | Actual integration constraint | Use / reject / verify next |

This is a template, not a requirement to add a comparison file to the user's repository.

## Choose a reuse method

Use the following decision paths after the requirements above are satisfied:

| Observed fit | Decision | Condition to verify |
| --- | --- | --- |
| Required behavior is available through a supported interface | Adopt | Normal configuration and use meet the acceptance criteria. |
| A sound implementation covers most of the work | Extend | The missing part is small and can be added without an invasive fork or a large compatibility layer. |
| Several focused components cover complementary needs | Compose | Interfaces, dependency versions, and license obligations are compatible; combined maintenance cost is lower than the alternatives. |
| No candidate meets the necessary constraints | Build | Research identifies the missing behavior and a small maintainable implementation is justified. |

These paths adapt the framing credited in [the upstream notice](../THIRD_PARTY_NOTICES.md). Avoid unsupported 9/10-style ratings: show the evidence behind each decision. MIT or Apache licensing can simplify some uses, but a label alone is not a complete compatibility assessment and other suitable licenses are not automatically excluded.

1. Call code or dependencies already present in the project.
2. Use a built-in feature, supported package, official SDK, or documented interface.
3. Adapt a maintained example at a verified version when its license permits it.
4. Vendor a minimal source subset only when packages/APIs cannot satisfy the requirement. Preserve attribution and notices, pin the upstream ref, and explain who will maintain local changes.
5. Fork an entire application only when the user needs that application as the foundation and its architecture fits. Avoid replacing an existing project to reuse one component.

Build new project-specific logic when existing solutions miss necessary constraints or add more complexity than they remove. State that tradeoff briefly.

## Validate before committing to a dependency

Identify the hardest uncertainty and use the smallest relevant test that can disprove the choice. Reuse a project test if it already answers that question; avoid a duplicate prototype. Test the actual runtime with representative synthetic or authorized data. Inspect package provenance and setup behavior before execution; use normal isolation and lockfile conventions.

Stop investigating when one suitable choice has sufficient evidence and the remaining uncertainties do not affect the task. If a candidate fails, record the observed failure, try the next plausible alternative, and revisit the approach when evidence no longer narrows the problem.

After integration, verify the user's observable behavior and the relevant failure path. A successful install, import, or upstream test suite alone does not validate the host application's integration. Report source/version and actual checks; preserve required notices in the delivered project.

For example, an HTTP client advertised as supporting retries may retry only connection failures rather than response statuses, read/write failures, or non-idempotent requests. Verify the required retry classes, limits, backoff, and idempotency rules against the exact client version before claiming that a dependency covers the requirement. Apply the same scrutiny to other broad capability labels.
