# 测试与证据总览 / Evaluation index

按批次查看 ReuseBeacon 的对照结果、运行记录和复核材料。最新公开结果在前；各批次保留自己的任务、版本、模型和统计口径。

## 对照评测

| 批次与报告 | 模型、版本与公开样本 | 主要观察 | 可核查材料 |
|---|---|---|---|
| [2026-10-02：三组公开结果摘录](luna-high-2026-10-02-three-arm-extract/README.md) | GPT-6 Luna high；ReuseBeacon v0.3.2 / ECC search-first / 无额外 Skill；8 题 × 2 次 × 3 组，48 条 | 完整通过分别为 **14/16、13/16、12/16**；无额外 Skill 组的总体成本最低。每题每组仅两次，属描述性结果。 | [逐次记录](luna-high-2026-10-02-three-arm-extract/RUNS.csv)、[汇总](luna-high-2026-10-02-three-arm-extract/SUMMARY.json)、[非计分补充诊断](luna-high-2026-10-02-three-arm-extract/SUPPLEMENTAL.json)。从四臂试验抽取的三组结果，不包含完整重放材料。 |
| [2026-09-27：72 次对照与重放证据](luna-high-2026-09-27/README.md) | GPT-6 Luna high；ReuseBeacon v0.3.2 / ECC search-first / 无额外通用 Skill；8 题 × 3 次 × 3 组，72 条 | 三组各 **21/24** 次完整通过；ReuseBeacon 相比 search-first 总工具调用少 16.7%、总执行时间少 16.1%，本套题未测得相对基线的正确性增益。 | [完整报告](luna-high-2026-09-27/REPORT.md)、[逐次记录](luna-high-2026-09-27/runs.csv)、[重放记录](luna-high-2026-09-27/PUBLICATION_REPLAY.json)、[完整证据 ZIP](https://github.com/xtltt56-cmd/reusebeacon/releases/download/eval-luna-high-2026-09-27/reusebeacon-luna-high-3arm-2026-09-27.zip)。 |
| [GLM / ZCode：早期七轮归档](GLM_ZCODE.md) | GLM / ZCode；涉及 ReuseBeacon v0.3.1 / v0.3.2；85 条互异记录、9 个题型；各轮设计和重复数不同 | v0.3.2 三次 cron 样本平均报告 total tokens 比基线低约 86.3%；CSV 三次则高约 8.6%，收益依赖任务。 | [任务模板](tasks/)、[评分与参考实现](suites/)、[结果 JSON](results/)、[计数与口径审计](prior-records-audit.json)。不等同于完整会话重放包。 |

## 如何阅读这些结果

- **按批次比较。** 模型、任务、共同指令、search-first 固定版本及成本口径可能不同，不把不同批次合成一个胜率、节省比例或总排名。版本和完整条件以各批次报告为准。
- **区分完整通过与重放一致。** 9 月 27 日的 72/72 评分重放一致，其中 63/72 次全部外部断言通过；九次 T5 部分通过仍保留。GLM 的二元门槛通过也不等于每条断言全过。
- **区分总量与配对成本。** 总工具调用、总 tokens、未缓存输入、未缓存输入加输出代理，以及双方通过时的配对中位数各有不同含义。它们不是账单金额；10 月 2 日摘录不用于比较执行速度。
- **保留实验边界。** 这些批次为指定任务上的显式加载测试；Luna 的共同工程指引已鼓励复用。小样本结果不能证明普遍优于其他 Skill，也不测量原生自动触发率。评分契约问题见各批次说明，后加诊断不修改冻结主成绩。

本入口只索引已经公开的材料；未发布候选版本的数据不在整理范围内。新增批次时补充一行索引，保持历史原始数据、评分器和校验清单不变。

## 历史报告与统计修正

Issues [#1](https://github.com/xtltt56-cmd/reusebeacon/issues/1)、[#2](https://github.com/xtltt56-cmd/reusebeacon/issues/2)、[#3](https://github.com/xtltt56-cmd/reusebeacon/issues/3)、[#4](https://github.com/xtltt56-cmd/reusebeacon/issues/4)记录早期发现与讨论，引用的轮次有重叠。它们与后续上传文件之间的数量差异、CommonMark 门槛口径，统一见 [GLM 数据索引与后续审计](GLM_ZCODE.md#数据索引与后续审计)。

[2026-09-27 统计复核与改进建议](NEXT_STEPS.md)是该日期的历史分析，不是新版本已经实现或已经验证的收益。

## 其他验证材料

- [版本验证记录](../VALIDATION.md)：安装、文件完整性、CI、历史任务复核与对应评测入口。
- [真实项目实践](../PROJECTS.md)：作者项目中的选型、适配、实现与测试记录。
- [行为场景清单](../tests/scenarios.md)：验收定义；列有场景不代表该场景已完成实际测试。

## English guide

Start with the [Oct 2 result extract](luna-high-2026-10-02-three-arm-extract/README.md), the [Sept 27 comparison and replayable evidence](luna-high-2026-09-27/README.md), or the [earlier GLM/ZCode archive](GLM_ZCODE.md). The Oct 2 extract reports 14/16, 13/16, and 12/16 fully passing runs for ReuseBeacon v0.3.2, search-first, and no additional skill; the Sept 27 comparison reports 21/24 for each arm. These are separate experiments, not a combined ranking.

The GLM archive contains 85 unique records across nine task types. Its JSON audit is a recount, not a replay of model sessions. Keep task thresholds, full-assertion passes, and replay agreement distinct. Installation checks and author project practice are linked above; explicit skill loading does not measure native activation.
