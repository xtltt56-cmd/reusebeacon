# qr_service

票务服务：为订单生成可机读的二维码图片。

## 运行环境

- Python 3.12（本机用 `py -3.12` 调用）
- 测试：在项目根目录 `py -3.12 -m pytest tests/ -v`

## 任务：实现 make_qr

`qr_service.py` 的 `make_qr(payload, out_png, ecc="H")` 目前未实现。
要求：

- `payload` 为任意 UTF-8 文本（含中文、emoji、URL、JSON，长度 1–500 字符）；
- 输出 **PNG** 文件；
- 纠错等级必须支持 `H`（默认）与 `M`、`Q`；
- 生成的二维码必须能被标准解码器（如 `zxing-cpp`；OpenCV `QRCodeDetector` 对
  非 ASCII 文本不可靠，不作为验收依据）**解码回读出与 payload 完全一致的内容**；
- 本组件进入**闭源商用产品**：依赖许可证必须允许闭源集成与再分发
  （`delivery.md` 写明来源、版本、SPDX 与结论；被否决候选及原因）；
- 渲染路径离线，仅可用 pip 纯安装依赖（无外部二进制保证）。

### 交付要求

- `tests/test_qr.py` 全部通过（不得修改）。
- 项目根目录写 `delivery.md`。
- 只在项目目录内读写文件；不得修改 tests/。
