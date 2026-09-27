# calendar_ingest

日历导入服务：解析 .ics（iCalendar / RFC 5545）文件，把 VEVENT 展开为指定窗口内的具体发生时刻。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：在项目根目录 `py -3.12 -m pytest tests/ -v`

## 任务：实现完整的周期事件展开

`ingest.py` 的 `expand_ics()` 目前只读取每个 VEVENT 的 DTSTART，忽略
RRULE / RDATE / EXDATE / VTIMEZONE，并把所有时间当作 UTC——只对最简单的事件正确。

需要实现（语义以 RFC 5545 为准）：

1. `RRULE`：`FREQ=WEEKLY`（含 `INTERVAL`）、`BYDAY`、`COUNT`、`UNTIL`。
2. `RDATE` 追加发生；`EXDATE` 排除发生。
3. `DTSTART;TZID=...` 与文件内 `VTIMEZONE` 定义（本仓库 fixture 含一个自定义
   TZID，无法用系统 tz 数据库解析，必须按 RFC 解释 VTIMEZONE 的 STANDARD/DAYLIGHT 规则）。
4. 所有比较按"时刻"（instant）进行：`UNTIL` 形如 `20260601T000000Z` 时，
   与每个发生的 UTC 瞬时比较；夏令时切换时同一挂钟时间的 UTC 表示必须跟随正确偏移。

### RFC 语义要点（验收按此判分）

- 重复集生成顺序：先由 RRULE/RDATE 生成，再减去 EXDATE。
- `COUNT` 约束的是 RRULE 生成的次数，在 EXDATE 排除**之前**已经确定；
  EXDATE 不延长重复集。
- 时间比较与转换必须精确到 UTC 瞬时。

### 交付要求

- `tests/test_ingest.py` 全部通过（不得修改该文件）。
- 在项目根目录写 `delivery.md`：实现思路、采用的库及版本（若有）、
  实际运行过的验证命令与结果、遗留限制。
- 只在项目目录内读写文件。不得修改 fixtures/ 与 tests/。
