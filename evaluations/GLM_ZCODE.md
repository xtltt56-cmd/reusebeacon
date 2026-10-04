# GLM / ZCode：早期评测协议与记录

[返回测试与证据总览 / Evaluation index](README.md)

本批次涉及 ReuseBeacon v0.3.1 / v0.3.2、ECC search-first 和无 Skill 条件，归档为 iteration-1 至 iteration-7 共 **85 条互异记录、9 个题型**；早期部分轮次为双臂设计，并非每轮均为完整三臂矩阵。

公开材料包括任务模板、评分套件、参考实现及各轮计时和判分 JSON，可用于核对归档指标和复用测试设计。Issue 中的行为描述仍需结合对应过程证据理解；这里不将归档 JSON 等同于完整会话重放材料。

以下保留原批次的协议说明，统计范围与后续修正见文末。它不适用于后来的 GPT-6 Luna 批次。

## 三臂设计（原批次记录）

每个任务在**完全相同的任务说明、项目模板与环境约束**下并行运行三个独立 agent：

| 臂 | 注入方式 |
|---|---|
| `with_skill` | 开头告知：本机已安装 ReuseBeacon（v0.3.1 轮次 / v0.3.2 起为 `fake-project-v032` 安装），先完整阅读 SKILL.md 并遵循其工作流，需要时按其指示读 references/ |
| `with_search_first` | 同样方式注入 ECC search-first（固定版本 `db7f2a6`） |
| `without_skill`（基线） | 无技能注入 |

其余提示词逐字一致。原协议记录臂间在批次中交叉排列，以降低时段偏差。**skill 为强制加载
（指路式注入），自动触发行为未测**；模型为 GLM（ZCode harness），Windows 11 / Python 3.12。

## 判分原则

- **确定性判分，无 LLM 主观评分**：pytest 断言套件、CommonMark 官方 652 例逐字节
  精确匹配、psutil 实测子进程峰值 RSS 与墙钟。
- **判分套件先冻结再运行**：全部隐藏套件先经独立参考实现
  （markdown-it-py / croniter / icalendar + recurring-ical-events / segno + zxing-cpp / ijson）
  交叉验证到参考实现可满分，才用于给候选实现判分。开发期抓出并修复了两个判分器缺陷
  （OpenCV 对中文 QR 解码不可靠 → 换 zxing-cpp；事件文件生成器尾逗号 → 修复重生成），
  均如实记录在 Issue #3。
- **对己不利的记录同样保留**：保留一次护栏误判的报告与相关结果（Issue #4 观察 2）；公开 JSON 不包含完整逐工具轨迹。

## 目录结构

```
evaluations/
├── README.md            # 全部评测的统一入口
├── GLM_ZCODE.md         # 本批次协议、判分原则、局限
├── suites/              # 冻结的隐藏评分套件、判分脚本、参考实现、规范语料
│   ├── hidden_test_*.py   # 逐任务隐藏验收（判分时拷入各臂项目 tests/）
│   ├── grade_eval*.py     # E4/E5/E8/E9 的独立判分器
│   ├── ref_*.py           # 参考实现（用于冻结前交叉验证）
│   ├── gen_expectations.py
│   ├── e9/                # 1.5GB 事件文件生成器（不含文件本体）与期望真值
│   └── commonmark/spec.json
├── tasks/               # 9 个任务项目模板（README、占位实现、可见测试、fixtures）
│   │                     # 与 E7 使用的本地技能索引（优质/陷阱/无关三技能）
│   └── skill-registry/
└── results/             # 每轮每臂每运行的 timing.json / grading.json（合并归档）
    └── iteration-N.json
```

## 运行协议

1. 从 `tasks/` 复制项目模板到独立运行目录（每臂一份，互不可见）；
2. 按上表注入技能说明，任务提示词逐字一致；
3. 运行结束后把对应 `suites/` 隐藏套件拷入 `tests/` 判分（E4/E5/E8/E9 用 `grade_eval*.py`）；
4. 记录 tokens / 墙钟 / 工具调用数，与判分结果一并写入 `grading.json` / `timing.json`；
5. 汇总时以 **n≥2 的均值 ± 波动**为口径（单次运行不足以评价，见 Issue #4 观察 4）。

## 局限（发布口径的一部分）

- 每格样本 n=1–3，为方向性证据而非统计显著结论；
- 强制加载而非真实触发；单一模型与 Windows 沙箱（如 zoneinfo 需 tzdata）；
- 判分套件公开后不再具备"隐藏"性质，后续轮次应按同协议换用等价新套件；
- 评测由作者委托的独立运行方执行，协议与判分器公开以供审查。

## 数据索引与后续审计

Issue 是当时的报告和讨论；以下链接对应已上传文件，批次之间存在引用重叠，不按 Issue 中的累计数字相加。

| Issue | 报告范围 | 已上传记录 |
|---|---|---|
| [#1](https://github.com/xtltt56-cmd/reusebeacon/issues/1) | 第一批优势项 | [iteration-1](results/iteration-1.json)、[iteration-2](results/iteration-2.json) |
| [#2](https://github.com/xtltt56-cmd/reusebeacon/issues/2) | 早期 34 条累计记录与结论修订 | [iteration-1](results/iteration-1.json)、[iteration-2](results/iteration-2.json)、[iteration-3](results/iteration-3.json)、[iteration-4](results/iteration-4.json) |
| [#3](https://github.com/xtltt56-cmd/reusebeacon/issues/3) | E7–E9 扩展 | [iteration-6](results/iteration-6.json) |
| [#4](https://github.com/xtltt56-cmd/reusebeacon/issues/4) | v0.3.2 后续矩阵与行为观察 | [iteration-5](results/iteration-5.json)、[iteration-6](results/iteration-6.json)、[iteration-7](results/iteration-7.json)；这三个文件共 51 条，不能直接沿用标题中的 42 条 |

七个 JSON 合计 **85 条互异记录、9 个题型**。旧报告中的“约 87 条”“8 个题型”和“42 条矩阵”与归档文件的计数范围不一致，引用这些数量时以明确列出的文件和筛选条件为准。

三条 CommonMark 记录同时包含 `pass_rate=1` 与 `649/652`：iteration-3 search-first、iteration-4 search-first、iteration-7 ReuseBeacon。二元字段记录的门槛通过不能改写成每条断言全过；保留原 JSON 和原评分。

[机器可读审计](prior-records-audit.json)由 [review_prior_records.py](review_prior_records.py)重新计算归档 JSON 生成，核对数量与统计口径，不代表重跑全部模型会话。[详细审计与当时的改进建议](NEXT_STEPS.md)。
