# ReuseBeacon

[English](README.en.md)

[![Validate skill](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml/badge.svg)](https://github.com/xtltt56-cmd/reusebeacon/actions/workflows/validate.yml)
[MIT](LICENSE) · [下载技能 ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip) · [版本说明](https://github.com/xtltt56-cmd/reusebeacon/releases) · [升级说明](MIGRATION.md) · [问题反馈](https://github.com/xtltt56-cmd/reusebeacon/issues)

**开源复用导航** · 技能标识：`reusebeacon`

让 AI 按开发需求复用成熟开源方案；需要专门工作流时，发现、安装并使用合适的 Agent Skill，完成实际任务与验证。

**Reuse suitable open-source implementations and task-specific skills.** A portable Agent Skill for focused discovery, scoped installation, and verified reuse.

## 为什么使用 ReuseBeacon

- **把需求落实为可复用方案**：先看项目已有能力，再查标准库、官方 SDK 和适用的开源实现，把精力留给项目特有的需求。
- **代码与 Skill 一起考虑**：缺少专门工作流时，寻找并实际使用合适的辅助 Skill，覆盖选型、实现和验证。
- **小任务保持轻量**：已有实现足够就直接修复与测试；公开检索无需先登录 GitHub，外部搜索与安装按需进行。
- **以集成结果作交付**：检查版本、平台和许可证信息，验证关键行为，并留下采用来源与测试结果。

## 项目实践

作者已将 ReuseBeacon 用于自己的开发任务。以下公开项目记录展示相关的开源选型、适配和交付实践：

| 项目 | 可查看的实践 |
| --- | --- |
| [A 股量化工作台](https://github.com/xtltt56-cmd/a-share-quant-workbench) | 比较 Qlib、AKShare、DuckDB 等候选，明确核心与可选依赖；记录 RiceQuant Skills 的安装与适配；提供实现源码和 Windows 测试记录。 |
| [Windows 鼠标录制工具](https://github.com/xtltt56-cmd/windows-mouse-recorder) | 使用 `pynput` 完成全局鼠标录制，在项目中实现回放控制；通过单元测试、Windows 打包和可执行文件冒烟检查交付。 |

[查看项目案例与固定版本的证据链接](PROJECTS.md) · [查看验证记录](VALIDATION.md)

`v0.3.2` 精简任务分支和中英文触发描述：小修复直接处理，仅调研时交付结论，已有授权继续执行，并按改动风险选择必要验证。

这是一个遵循 [Agent Skills 格式](https://agentskills.io/specification)的指令型 Skill。核心流程不绑定特定模型，不包含自制的登录或搜索程序，也不需要运行自己的服务器。

## 工作流程

1. **理解需求与已有能力**：读取相关实现、依赖和验收条件，优先使用已安装且适用的 Skill。
2. **按需补充 Skill**：明确存在工作流缺口时再定向搜索，检查内容、来源和宿主能力，默认安装一个到当前项目并实际使用。
3. **检查必要访问**：公开资料可以匿名访问；只有私有资源或账号操作需要时才验证认证与权限。
4. **检索和筛选实现**：围绕技术栈选择相关渠道，核对功能、兼容性、许可证、维护证据和总成本。
5. **集成并验证**：验证关键不确定性和最终任务行为；记录采用来源，以及辅助 Skill 是否真正加载、执行。

```mermaid
flowchart LR
    A[理解需求与已有能力] --> B{需要补充工作流吗}
    B -->|需要| S[发现与检查 Skill]
    S --> T[限定范围安装并使用]
    T --> C[按需检索成熟实现]
    B -->|已有能力足够| C
    C --> D[检查适用性与总成本]
    D --> E[采用 / 扩展 / 组合 / 自建]
    E --> F[集成并测试实际行为]
```

公开检索不要求先登录 GitHub；对实际使用的访问路径进行最小验证，并区分网络、认证、权限和限流问题。离线请求直接使用本地证据。已有实现或技能足够时停止发现流程，不为小修复强制搜索或安装。

必要来源不可访问时，按任务选择可用的官方文档、包注册表、项目托管站或可核实的镜像。只在遇到问题时切换，不逐个平台预检；采用镜像前核对上游关系和所需版本。

实现筛选参考 [ECC 的 search-first](https://github.com/affaan-m/ECC/blob/db7f2a6fd5b013d56ec0ba0cfc547ba77baddbce/skills/search-first/SKILL.md)，技能发现参考 [Vercel 的 find-skills](https://github.com/vercel-labs/skills/blob/7407f3893ad4dceab546ac002c3ef806e4000c73/skills/find-skills/SKILL.md)。来源、固定提交与许可证见 [THIRD_PARTY_NOTICES.md](skills/reusebeacon/THIRD_PARTY_NOTICES.md)。两者都不是安装或运行前置依赖。

## Skill 发现如何保持轻量

- **先用已有能力**：只检查相关已安装 Skill；仅在用户要求寻找技能或存在具体工作流缺口时搜索外部目录。
- **限制初始范围**：默认一次查询，必要时换词一次；检查至多三个合理候选，通常采用一个。有明确未解决需求时才扩大。
- **检查实际内容**：核对 `SKILL.md`、会用到的脚本与资源、来源版本及宿主工具；不使用固定 Star 或安装量门槛。
- **按已有授权执行**：为已授权任务做必要、可逆的项目级安装可直接继续；仅研究时给建议。全局改动、付费服务或新数据传输遵守相应授权。
- **安装后实际使用**：核对安装范围和文件，使用宿主支持的加载方式，并验证原始任务结果；不将安装成功写成行为验证通过。

不会默认安装整套合集、递归寻找更多发现技能或升级已有技能。连接排障和外部技能发现的详细规则只在需要时读取。具体流程见 [技能发现与使用](skills/reusebeacon/references/skill-discovery.md)。

## 安装

推荐通过开源 [skills CLI](https://github.com/vercel-labs/skills) 安装。以下命令固定使用本项目验证的 CLI 版本 `1.7.0`，需要 Node.js 22.20.0 或更新的兼容版本。

在需要使用技能的项目目录运行：

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
```

该命令跟随仓库默认分支。需要固定本次版本时，使用标签路径：

```shell
npx skills@1.7.0 add https://github.com/xtltt56-cmd/reusebeacon/tree/v0.3.2/skills/reusebeacon --skill reusebeacon --copy
```

它会让用户选择目标工具。也可以指定多个工具：

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --agent codex claude-code cursor github-copilot --copy
```

默认安装到当前项目；确实需要用户级安装时加 `--global`。`--copy` 避免依赖符号链接权限，适合 Windows。使用第三方安装器前可先阅读其说明；不希望使用安装器时，把 `skills/reusebeacon` 整个目录复制到目标工具支持的 Skill 目录。只复制 `SKILL.md` 会丢失参考文件。

从旧名称 GitHub Reuse First 升级时，请按[迁移说明](MIGRATION.md)更新安装来源和调用名称。

也可以[下载独立技能包](https://github.com/xtltt56-cmd/reusebeacon/releases/latest/download/reusebeacon.zip)，解压后将完整的 `reusebeacon` 文件夹放入目标工具的 Skill 目录；保留包内参考文件和许可证。每个版本同时提供 `SHA256SUMS.txt`，便于核对下载完整性。

下载本仓库后，也可以在仓库目录安装本地版本：

```shell
npx skills@1.7.0 add . --skill reusebeacon --copy
```

## 使用

在支持 `$` 技能调用的 Codex 界面中：

```text
使用 $reusebeacon。给这个现有项目增加 Excel 导出功能。
请先评估现有依赖和适合的成熟方案，按需要检查访问，完成集成与测试。
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

```text
使用 reusebeacon，给现有网页补充浏览器端到端测试。
先使用已有工具和技能；确有工作流缺口时，可以寻找、检查并在当前项目安装一个合适的 Skill，实际使用它完成测试。
```

自动匹配面向“找成熟方案、技术选型、避免重复造轮子、找并使用开发 Skill”等需求。要明确使用它，可以在技能选择器中选中 ReuseBeacon，或按所用工具支持的方式点名调用。若选择器找不到，先核对安装位置、版本和工具的刷新要求；只下载仓库不代表工具已加载技能。

自动触发取决于工具和模型。需要项目持续采用这套流程时，可在项目规则中注明“涉及开源选型或技能发现时使用 ReuseBeacon，小修复直接处理”，并在目标工具中验证。触发检查示例见[场景清单](tests/scenarios.md#trigger-checks)。

## 兼容性和依赖

| 项目 | 说明 |
| --- | --- |
| Skill 格式 | 标准 `SKILL.md`、相对路径引用，适合支持 Agent Skills 的工具 |
| GitHub 访问 | 使用可用的网页、API、Git 或连接器；根据实际操作决定是否需要认证 |
| 辅助 Skill | 可选；所需工具和权限由宿主提供。没有对应工具时，下载 Skill 不能代替工具安装 |
| 执行能力 | 完整集成流程需要读取项目、运行命令、修改文件与测试的权限 |
| 模型差异 | 不同工具的调用方式和自动匹配效果需要分别验证 |
| Codex 元数据 | `agents/openai.yaml` 为可选界面信息；核心流程不依赖它 |
| Python/Node | Skill 本体不需要；上面的安装器需要 Node.js，目标项目使用自己的运行环境 |

## 获取版本、搜索和反馈

- [公开仓库](https://github.com/xtltt56-cmd/reusebeacon)：源文件、中英文说明和安装入口。
- [版本发布](https://github.com/xtltt56-cmd/reusebeacon/releases)：查看变更说明和下载版本归档。
- [问题与建议](https://github.com/xtltt56-cmd/reusebeacon/issues)：反馈安装问题、触发失效或筛选流程的缺陷；请隐去凭据和私有项目内容。

可以在 GitHub 搜索 `reusebeacon`，或使用 `agent-skills`、`code-reuse` 等主题发现相关项目。安装命令和 ZIP 下载链接都指向本仓库。

## 验证与维护

公开仓库安装、文件完整性和 Linux / Windows 包检查已完成；作者项目提供选型、实现与交付记录。具体版本、检查范围及任务复核结果见 [验证记录](VALIDATION.md)。[测试场景](tests/scenarios.md)覆盖访问恢复、依赖选择、任务范围和辅助 Skill 使用，便于持续回归。

每次提交和 PR 通过 GitHub Actions 在 Linux、Windows 上检查技能元数据、随包资源、许可证一致性和本地引用。贡献修改时，可以在独立 Python 3.10+ 环境运行：

```shell
python -m pip install -r requirements-dev.txt
python tests/validate_package.py
```

改动决策流程时，请同时提供最小复现场景和实际观察结果。欢迎提交其他工具的安装记录与行为测试证据；请区分“安装成功”和“模型完成了任务”。

不要把凭据、私有项目、真实客户样本或本机绝对路径加入此仓库。MIT 许可证覆盖本仓库原创内容；复用的第三方项目仍适用各自的许可证。

## 设计取舍与来源

保留它的先检索再实现、多渠道发现、现有代码优先、分级决策和避免依赖膨胀的思路。参考版本固定在来源说明中，以下是本版本主动调整的地方：

| 设计关注点 | 本版本处理 |
| --- | --- |
| 选型依据 | 记录可核查的证据、硬性约束和未确认项，支持用户复查取舍 |
| 多方案组合 | 先验证互补关系、接口、版本、许可证和总维护成本，再决定是否组合 |
| 许可证与使用方式 | 记录版本、许可证原文、相关声明和使用方式；有适用性疑问时明确指出 |
| 宿主工具适配 | 使用当前工具即可执行；只有工具支持、授权允许且有收益时才委派独立检索 |
| 连接失败时需要区分实际访问能力 | 公开检索允许匿名；必要认证失败时按原因恢复，继续独立本地工作 |
| 版本与功能边界 | 核对实际版本、功能边界和失败路径 |
| 集成交付 | 执行最小适配实验、项目测试、失败路径和最终差异检查 |

例如，参考文件把 HTTPX 概括为支持内置重试；[HTTPX 官方说明](https://www.python-httpx.org/advanced/transports/)将该传输层能力限定为连接错误和连接超时，503 或读写错误需要另行处理。这个例子说明“有重试”需要继续核实覆盖范围。本 Skill 因此保留判断方法，避免固化未经限定的库推荐。

## 文件

```text
skills/reusebeacon/
├── SKILL.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── agents/openai.yaml
└── references/
    ├── github-access.md
    ├── selection.md
    └── skill-discovery.md
```
