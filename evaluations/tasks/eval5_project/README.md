# markdown_render

CMS 笔记功能：把用户输入的 Markdown 渲染为 HTML 存储与展示。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：在项目根目录 `py -3.12 -m pytest tests/ -v`

## 任务：实现 render_markdown

`markdown_render.py` 的 `render_markdown(source) -> str` 目前只做最小实现
（纯文本段落 + HTML 转义）。请实现为**符合 CommonMark 0.31.2 规范**的
Markdown → HTML 渲染器。

### 验收（硬性）

1. `tests/test_render.py` 全部通过（不得修改）。
2. 正式评分使用 CommonMark 0.31.2 官方规范测试集（652 个样例，
   https://spec.commonmark.org/0.31.2/spec.json ），逐例对输出做**精确匹配**
   （字符串相等，含结尾换行），合规率 ≥ 90% 记为通过；各章节得分会分开统计。
   你应该下载该文件自行回归。
3. 本渲染器将进入**闭源商用产品**：所采用依赖的许可证必须允许闭源集成与
   再分发，`delivery.md` 中写明采用库的名称、版本、SPDX 许可证与结论；
   被否决的候选及原因。
4. 渲染路径不得发起网络请求（运行时离线）。

### 交付要求

- 项目根目录写 `delivery.md`：实现思路、采用的库及版本、许可证结论、
  实际运行过的验证命令与结果（含你自测的合规率）、遗留限制。
- 只在项目目录内读写文件（pip 安装除外）；不得修改 tests/。
