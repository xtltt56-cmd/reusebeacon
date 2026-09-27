# meeting_service

内部会议服务：存储会议定义，并把周期性会议展开为具体日程。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：`py -3.12 -m pytest tests/ -v`

## 任务：实现周期会议展开

`meetings.py` 中的 `expand()` 目前只支持一次性会议（`recurrence="none"`）。
需要实现 `weekly` 与 `monthly_nth` 两种周期规则，并把每个发生时刻转换为 UTC。

### 规则定义

- `Meeting.weekday`：0=周一 … 6=周日，是周期会议的锚定星期。
- `"weekly"`：从 >= start_date 的第一个匹配 weekday 起，每 7 天一次。
- `"monthly_1st"` … `"monthly_5th"`：每月的第 N 个 <weekday>（不足则当月不发生）。
- 展开范围含 start_date 与 end_date 两端。

### 时刻语义（验收硬性要求）

- 每个发生时刻的本地挂钟时间必须恒等于 Meeting 的 hour:minute（tz 的时区规则，含夏令时）。
- 对应 UTC 时刻由 tz 的官方规则决定：跨夏令时切换时，同一挂钟时间的 UTC 表示允许且必须改变。
- 若某日期的该挂钟时间不存在（春季跳变日）：使用时区库对不存在时刻的默认语义（fold=0）。
- 若某日期的该挂钟时间出现两次（秋季回拨日）：取较早的那一次（fold=0）。
- `Occurrence.start_utc` 必须是带时区的 UTC datetime；`local_start` 是带原时区信息的 datetime。

### 交付要求

- 让 `tests/test_recurrence.py` 全部通过。
- 在项目根目录写 `delivery.md`：简述实现思路、采用/参考的库（若有）及版本、
  实际运行过哪些验证（写明命令与结果）、遗留限制。
- 不要修改 `tests/test_recurrence.py`，也不要在项目目录外写文件。
