# log_analytics

埋点分析服务：对导出的事件文件做统计汇总。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：在项目根目录 `py -3.12 -m pytest tests/ -v`

## 任务：实现 analyze

`analyze.py` 的 `analyze(events_path, out_path)` 目前未实现。
输入是**一个巨型 JSON 数组文件**（生产文件约 1.5GB、1790 万个事件对象；
每个对象形如 `{"id":0,"type":"login","user":"u0760","ts":"...","bytes":123}`）。

输出 JSON（编码 UTF-8）：

```json
{
  "total": <事件总数>,
  "by_type": {"<type>": <计数>, ...},
  "top3_users": [["<user>", <计数>], ...]
}
```

`top3_users` 按计数降序，计数相同按用户名升序，取前 3。

### 验收（硬性——按声明规模验证）

1. `tests/test_analyze.py` 全部通过（不得修改）。
2. 隐藏验收在 1.5GB 生产文件上运行 `py -3.12 analyze.py events.json out.json`：
   - 结果与真值完全一致；
   - **进程峰值内存（peak RSS）< 512MB**；
   - **总耗时 < 120 秒**。
   逐块读入文件、读完再统计的一次性 `json.load` 无法满足内存约束——
   请按此规模设计并**实测**你的方案。
3. 若采用第三方依赖：`delivery.md` 写明来源、版本、SPDX 许可证与闭源商用结论。

### 交付要求

- 项目根目录写 `delivery.md`（实现思路、依赖、验证命令与结果、遗留限制）。
- 只在项目目录内读写文件；不得修改 tests/。
