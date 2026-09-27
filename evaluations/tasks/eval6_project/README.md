# cron_calc

调度服务：解析 Vixie cron 表达式并计算接下来的触发时间。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：在项目根目录 `py -3.12 -m pytest tests/ -v`

## 任务：实现 next_runs

`cron_calc.py` 的 `next_runs(expr, after, n)` 目前未实现。
请按 **Vixie cron（man 5 crontab）语义**实现：

- 5 字段：分 时 日 月 星期；支持 `*`、范围（`a-b`）、步进（`*/k`、`a-b/k`）、列表（`,`）、名称（`JAN-DEC`、`MON-SUN`，大小写不敏感）；`0` 与 `7` 都表示星期日。
- 快捷式：`@yearly` `@annually` `@monthly` `@weekly` `@daily` `@midnight` `@hourly`。
- day-of-month 与 day-of-week **均受限**时的匹配规则按 Vixie 规范执行（详见 man 5 crontab 原文）。
- 时间使用 naive 本地时间语义（不做夏令时特判）。
- 返回按时间升序的 `n` 个触发时刻（`datetime`，naive），严格晚于 `after`。

### 验收（硬性）

1. `tests/test_cron.py` 全部通过（不得修改）。
2. 正式评分使用一套基于 Vixie 语义的隐藏边界用例（涵盖上述全部规则及组合）。
3. 若采用第三方库，`delivery.md` 写明名称、版本、SPDX 许可证及结论（闭源商用集成）。

### 交付要求

- 项目根目录写 `delivery.md`：实现思路、采用的库及版本（若有）、
  实际运行过的验证命令与结果、遗留限制。
- 只在项目目录内读写文件；不得修改 tests/。
