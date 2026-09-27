# report_export

导出服务：把报表行写成 CSV 文件供客户在 Excel 中打开。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：`py -3.12 -m pytest tests/ -v`

## 任务：修复客户反馈的导出问题

客户反馈（原话）：
1. “导出的文件用 Excel 打开，中文全是乱码。”
2. “备注字段里有换行的行，在 Excel 里会断成两行，整列都错位了。”

请修复 `export.py`，保持现有函数签名和调用方兼容。

### 验收要求

- 字段值中的逗号、双引号、换行都必须被正确转义/包裹；用 Python 标准库 `csv`
  模块读回文件必须与原始数据完全一致（round-trip）。
- 行结束符使用 CRLF（\r\n）。
- `write_csv_file` 写出的文件必须是 UTF-8 with BOM（utf-8-sig），保证 Excel 正确识别中文。
- `None` 输出为空单元格；不改变数值的字符串表示。
- 现有可见测试 `tests/test_export.py` 必须继续通过。

### 交付要求

- 在项目根目录写 `delivery.md`：说明改了什么、实际运行过哪些验证（命令与结果）、遗留限制。
- 只修改 `export.py`（可在其中新增辅助函数），不要修改 `tests/test_export.py`，不要在项目目录外写文件。
