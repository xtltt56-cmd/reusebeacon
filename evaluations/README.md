# 评测协议与工件（三臂对照实测）

[新增：GPT-6 Luna high 的 72 次对照与完整证据](luna-high-2026-09-27/README.md) · [10月2日三组公开摘录（不含 v0.3.3 数据）](luna-high-2026-10-02-three-arm-extract/README.md) · [统计复核与改进方向](NEXT_STEPS.md)

下文为原 GLM/ZCode 批次。已上传七个 JSON 共 85 条互异记录、9 个题型；其二元 `pass_rate` 不等于逐条断言全过，三条 CommonMark 记录为 649/652。原始记录保留，复核详情见 [prior-records-audit.json](prior-records-audit.json)。不同模型和成本口径不合并。

本目录承载 Issue #1–#4 中全部实测结论的**可复现层**：任务模板、冻结的判分套件、参考实现、
各轮运行的计时与判分原始记录（JSON），以及运行协议。所有数字均可由本目录核对。

## 三臂设计

每个任务在**完全相同的任务说明、项目模板与环境约束**下并行运行三个独立 agent：

| 臂 | 注入方式 |
|---|---|
| `with_skill` | 开头告知：本机已安装 ReuseBeacon（v0.3.1 轮次 / v0.3.2 起为 `fake-project-v032` 安装），先完整阅读 SKILL.md 并遵循其工作流，需要时按其指示读 references/ |
| `with_search_first` | 同样方式注入 ECC search-first（固定版本 `db7f2a6`） |
| `without_skill`（基线） | 无技能注入 |

其余提示词逐字一致。臂间在批次中交叉排列以消除时段偏差。**skill 为强制加载
（指路式注入），自动触发行为未测**；模型为 GLM（ZCode harness），Windows 11 / Python 3.12。

## 判分原则

- **确定性判分，无 LLM 主观评分**：pytest 断言套件、CommonMark 官方 652 例逐字节
  精确匹配、psutil 实测子进程峰值 RSS 与墙钟。
- **判分套件先冻结再运行**：全部隐藏套件先经独立参考实现
  （markdown-it-py / croniter / icalendar + recurring-ical-events / segno + zxing-cpp / ijson）
  交叉验证到参考实现可满分，才用于给候选实现判分。开发期抓出并修复了两个判分器缺陷
  （OpenCV 对中文 QR 解码不可靠 → 换 zxing-cpp；事件文件生成器尾逗号 → 修复重生成），
  均如实记录在 Issue #3。
- **对己不利的记录同样保留**：含一次护栏误判的完整过程（Issue #4 观察 2）。

## 目录结构

```
evaluations/
├── README.md            # 本文件：协议、判分原则、局限
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

## 数据索引

| Issue | 内容 | 数据 |
|---|---|---|
| [#1](https://github.com/xtltt56-cmd/reusebeacon/issues/1) | 第一批·优势项 | `results/iteration-1.json`、`iteration-2.json` |
| [#2](https://github.com/xtltt56-cmd/reusebeacon/issues/2) | 多试验统计（34 组） | `results/iteration-2.json`、`iteration-4.json` |
| [#3](https://github.com/xtltt56-cmd/reusebeacon/issues/3) | 新题型 E7–E9 | `results/iteration-6.json` |
| [#4](https://github.com/xtltt56-cmd/reusebeacon/issues/4) | v0.3.2 全量矩阵（42 组） | `results/iteration-5.json`、`iteration-6.json`、`iteration-7.json` |
