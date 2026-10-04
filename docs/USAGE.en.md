# Getting started with ReuseBeacon

[简体中文](USAGE.md) · [Home](../README.en.md) · [Project practice](../PROJECTS.md) · [Evaluations](../evaluations/README.md)

Start with a real development task: add a feature to an existing project, compare implementation options, or add a specialist workflow. Copy one of the prompts below and adjust it to your project.

## 1. Install in your project

Run from the project directory with Node.js 22.20.0 or a later compatible release:

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
```

Choose the agent you use and project scope when prompted. If a suitable installation already exists, continue to the next step.

[Pin v0.3.2 or select an agent](../README.en.md#install) · [Manual ZIP installation](../README.en.md#manual-zip-install)

## 2. Invoke it for a task

Refresh the skill list or open a new session as required by your agent. Select ReuseBeacon or explicitly say "Use reusebeacon." Use `$reusebeacon` where supported.

Choose a feature your project needs, and include its input, output, and acceptance requirements. An understood, isolated fix can be handled directly; it usually needs no additional selection or discovery workflow.

### Example 1: Implement a feature

Use this for adding export support while checking existing dependencies and suitable maintained implementations.

```text
Use reusebeacon to add Excel export to this project.
Keep the existing stack, prefer suitable existing dependencies or maintained libraries,
preserve fields and data types, and complete the implementation and tests.
```

Review the chosen implementation and version, code changes, and actual test results. The export should produce a readable file and verify fields, data types, and the project's relevant edge cases.

### Example 2: Research without code changes

Use this to understand implementation choices and integration costs before deciding to build.

```text
Use reusebeacon to compare scheduled-task implementations for this project.
Consider time zones, runtime requirements, and existing dependencies.
Recommend an approach without changing code.
```

Review candidate sources, versions, and the evidence that determines the recommendation. Research ends at the recommendation; request implementation when ready.

### Example 3: Add a development workflow

Use this when a task needs specialist guidance, such as browser testing, and a suitable supporting skill could help.

```text
Use reusebeacon to add browser end-to-end tests for this website.
Use existing tools and skills first. If a workflow gap remains, find a suitable skill,
install it in this project, apply it, and test the main user flows.
```

Review the skill's source, installed location, actual invocation, and test results. Execution capabilities such as browser tools must be provided by the host; installing instructions does not supply a missing tool.

## 3. Review the delivery

Check the changes, reused sources, and actual verification results. [Project practice](../PROJECTS.md) links completed code and tests. The [evaluation index](../evaluations/README.md) links versioned comparisons with other approaches.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| ReuseBeacon is missing from the skill list | Check the selected agent and project directory, then refresh or open a new session as the host requires. Keep the complete folder for manual installation. |
| The skill is installed but not invoked | Select it in the skill picker or explicitly say "Use reusebeacon." Automatic matching varies by host and model. |
| External sources cannot be reached | Report the failed source and error; use available official documentation or local implementations. State offline constraints when relevant. |
| A supporting skill installs but cannot run | Check required host tools, permissions, runtime, and the supported loading mechanism. |

## Share your results

Share a successful use or a specific problem in [GitHub Issues](https://github.com/xtltt56-cmd/reusebeacon/issues). A short record is enough:

```text
Agent / model:
ReuseBeacon version:
Task and selected implementation:
Actual test results:
Problems or repeated work, if any:
```

Remove credentials and private project details. If it helps with a real task, consider a Star or share it with other developers.
