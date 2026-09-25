# ReuseBeacon

[English](README.en.md)

[![Validate skill](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml/badge.svg)](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml)
[MIT](LICENSE) · [下载技能 ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip) · [版本说明](https://github.com/xtltt56-cmd/reusebeacon/releases) · [升级说明](MIGRATION.md) · [问题反馈](https://github.com/xtltt56-cmd/reusebeacon/issues)

**开源复用导航** · 技能标识：`reusebeacon`

让 AI 在编程前检查 GitHub 连接，筛选适合当前项目的成熟开源方案，并完成复用、集成和验证。

**Find, assess, and integrate mature open-source solutions.** A portable Agent Skill for GitHub access checks, dependency assessment, and verified code reuse.

ReuseBeacon 从 `v0.2.0` 起采用此名称，原名为 GitHub Reuse First。旧用户请按照[迁移说明](MIGRATION.md)更新安装来源和技能调用名称。

这是一个遵循 [Agent Skills 格式](https://agentskills.io/specification)的指令型 Skill。核心流程不绑定特定模型，不包含自制的登录或搜索程序，也不需要运行自己的服务器。

## 工作流程

1. **检查连接**：优先使用已连接的 GitHub 工具，或通过官方 `gh` 检查当前账号；区分网络、登录、权限和限流问题。
2. **理解项目**：读取已有实现、依赖、运行环境和验收条件。
3. **检索候选**：围绕所需功能与实际技术栈，查找官方 SDK、成熟库和开源案例。
4. **按证据筛选**：比较功能覆盖、版本兼容、许可证、维护和测试情况，以及集成维护成本。
5. **集成并验证**：先验证最关键的不确定点，再接入项目，完成必要测试和来源记录。

```mermaid
flowchart LR
    A[验证 GitHub 连接] --> B[理解项目已有能力]
    B --> C[定向检索成熟方案]
    C --> D[检查适用性与总成本]
    D --> E[采用 / 扩展 / 组合 / 自建]
    E --> F[集成并测试实际行为]
```

默认先验证 GitHub 认证，连接失败时指导用户连接；等待期间可以继续读取本地项目。用户明确选择匿名公开检索或离线工作时，按用户选择执行。已有实现满足需求时直接复用，不为每个小改动强制引入新依赖。

筛选框架参考了 [ECC 的 search-first](https://github.com/affaan-m/ECC/blob/db7f2a6fd5b013d56ec0ba0cfc547ba77baddbce/skills/search-first/SKILL.md)，包含“直接采用、少量扩展、组合使用、自行实现”四条路径。这里增加了 GitHub 认证恢复、渠道覆盖说明、项目约束检查和实际集成验证，并在 [THIRD_PARTY_NOTICES.md](skills/reusebeacon/THIRD_PARTY_NOTICES.md) 保留来源与许可证。

## 安装

推荐通过开源 [skills CLI](https://github.com/vercel-labs/skills) 安装。以下命令固定使用本项目验证的 CLI 版本 `1.7.0`，需要 Node.js 22.20.0 或更新的兼容版本。

在需要使用技能的项目目录运行：

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
```

它会让用户选择目标工具。也可以指定多个工具：

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --agent codex claude-code cursor github-copilot --copy
```

默认安装到当前项目；确实需要用户级安装时加 `--global`。`--copy` 避免依赖符号链接权限，适合 Windows。使用第三方安装器前可先阅读其说明；不希望使用安装器时，把 `skills/reusebeacon` 整个目录复制到目标工具支持的 Skill 目录。只复制 `SKILL.md` 会丢失参考文件。

也可以[下载独立技能包](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip)，解压后将完整的 `reusebeacon` 文件夹放入目标工具的 Skill 目录；包内包含两个参考文件和许可证。每个版本同时提供 `SHA256SUMS.txt`，便于核对下载完整性。

下载本仓库后，也可以在仓库目录安装本地版本：

```shell
npx skills@1.7.0 add . --skill reusebeacon --copy
```

## 使用

在支持 `$` 技能调用的 Codex 界面中：

```text
使用 $reusebeacon。给这个现有项目增加 Excel 导出功能。
请先检查 GitHub，再评估现有依赖和适合的成熟方案，完成集成与测试。
```

其他工具可使用其技能选择器，或明确要求使用 `reusebeacon`：

```text
使用 reusebeacon，帮我实现一个支持断点续传的文件下载功能。
保留当前 Python 技术栈，优先复用成熟实现。
```

```text
使用 reusebeacon，给项目接入 Markdown 编辑器。
先比较可维护的候选方案，再实现适合现有界面的方案。
```

Skill 能否自动触发取决于工具和模型。它不能在所有工具中强制拦截每次代码修改。若需要团队每次编程前都执行，可在项目现有的 `AGENTS.md` 或相应工具规则中加入一条明确要求，并按目标工具实际测试。

## 兼容性和依赖

| 项目 | 说明 |
| --- | --- |
| Skill 格式 | 标准 `SKILL.md`、相对路径引用，适合支持 Agent Skills 的工具 |
| GitHub 访问 | 已配置的 GitHub 连接器/MCP，或官方 GitHub CLI；研究需要相应网络访问 |
| 执行能力 | 完整集成流程需要读取项目、运行命令、修改文件与测试的权限 |
| 模型差异 | 不同工具的调用方式和自动匹配效果需要分别验证 |
| Codex 元数据 | `agents/openai.yaml` 为可选界面信息；核心流程不依赖它 |
| Python/Node | Skill 本体不需要；上面的安装器需要 Node.js，目标项目使用自己的运行环境 |

## 获取版本、搜索和反馈

- [公开仓库](https://github.com/xtltt56-cmd/reusebeacon)：源文件、中英文说明和安装入口。
- [版本发布](https://github.com/xtltt56-cmd/reusebeacon/releases)：查看变更说明和下载版本归档。
- [问题与建议](https://github.com/xtltt56-cmd/reusebeacon/issues)：反馈安装问题、触发失效或筛选流程的缺陷；请隐去凭据和私有项目内容。

可以在 GitHub 搜索 `reusebeacon`，或使用 `agent-skills`、`code-reuse` 等主题发现相关项目。第三方目录的收录、排名和推荐由平台决定，发布仓库不保证立即收录；参见 [skills.sh 目录说明](https://skills.sh/docs)。

上传 GitHub 不会自动进入 OpenAI 公共插件目录。若需要该目录分发，可另行包装为 skills-only plugin 并按[官方流程](https://developers.openai.com/plugins/deploy/submission)提交审核。

## 验证与维护

见 [测试场景](tests/scenarios.md)和[本次验证记录](VALIDATION.md)。结构及安装验证不能替代各模型的行为测试。升级规则时，重点回归连接失败、许可证不明、现有依赖足够和用户仅要求方案等情况。

每次提交和 PR 通过 GitHub Actions 在 Linux、Windows 上检查技能元数据、随包资源、许可证一致性和本地引用。贡献修改时，可以在独立 Python 3.10+ 环境运行：

```shell
python -m pip install -r requirements-dev.txt
python tests/validate_package.py
```

改动决策流程时，请同时提供最小复现场景和实际观察结果。欢迎提交其他工具的安装记录与行为测试证据；请区分“安装成功”和“模型完成了任务”。

不要把凭据、私有项目、真实客户样本或本机绝对路径加入此仓库。MIT 许可证覆盖本仓库原创内容；复用的第三方项目仍适用各自的许可证。

## 对 search-first 的取舍

保留它的先检索再实现、多渠道发现、现有代码优先、分级决策和避免依赖膨胀的思路。参考版本固定在来源说明中，以下是本版本主动调整的地方：

| 原参考方案的薄弱处 | 本版本处理 |
| --- | --- |
| 示例出现 8/10、9/10，但没有对应评分依据 | 记录可核查的证据、硬性约束和未确认项，不制造精确评分 |
| 将多个弱匹配方案直接导向组合 | 先验证互补关系、接口、版本、许可证和总维护成本，再决定是否组合 |
| 使用“匹配、维护良好、MIT/Apache”作为采用信号 | 检查具体版本、实际许可证文本、相关组件与项目分发约束；不以标签替代判断 |
| 复杂任务默认调用特定 researcher agent | 使用当前工具即可执行；只有工具支持、授权允许且有收益时才委派独立检索 |
| GitHub 不可用时降级研究，未覆盖完整连接恢复流程 | 按用户要求默认指导连接并验证；仅在用户选择后使用匿名/离线路径 |
| 静态示例容易让模型把库名称当成功能保证 | 必须核对实际版本、功能边界和失败路径 |
| 对检索与采用的步骤较完整，但实际集成验收不够具体 | 增加最小适配实验、项目测试、失败路径和最终差异检查 |

例如，参考文件把 HTTPX 概括为支持内置重试；[HTTPX 官方说明](https://www.python-httpx.org/advanced/transports/)将该传输层能力限定为连接错误和连接超时，503 或读写错误需要另行处理。这个例子说明“有重试”需要继续核实覆盖范围。本 Skill 因此保留判断方法，避免固化未经限定的库推荐。

Skill 是给模型的流程指令。是否每次自动触发、是否准确执行，还需要在实际工具中测试；安装成功不能证明这两点。

## 文件

```text
skills/reusebeacon/
├── SKILL.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── agents/openai.yaml
└── references/
    ├── github-access.md
    └── selection.md
```
