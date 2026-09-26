# 项目实践 / Project practice

作者已在自己的开发任务中使用 ReuseBeacon。下面整理作者公开项目中的相关复用实践，并提供固定提交的文档、源码和测试记录。作者提供使用经历，公开记录支持读者查看具体的选型与交付内容。

The author reports using ReuseBeacon in development. These author-maintained projects illustrate related reuse practices through pinned documentation, implementation, and test records. Follow the links to inspect the specific choices and outputs described here.

## A 股量化工作台 / A-share quant workbench

**需求：** 在 Windows 上组合数据接入、本地存储、研究与报告能力，同时保留可选组件的替换空间。

**做法：** 候选评估记录了 Qlib、AKShare、DuckDB 等框架的职责、平台约束和采用理由。核心路径与可选研究组件分开，通过适配器和公开 API 接入。实际存储代码使用 DuckDB 与 Parquet；RiceQuant Skills 文档记录了 `idea-generation`、`report-renderer` 的安装，以及与项目数据入口的适配方式。

**可借鉴之处：** 将成熟组件接入现有架构，并按实际工具、数据和运行环境调整辅助 Skill 的使用方式。

This workbench composes existing data, storage, research, and reporting capabilities through explicit interfaces. It documents candidate selection and optional dependencies, implements DuckDB/Parquet storage, and records how installed RiceQuant skills fit the project's data workflow.

- [候选评估 / Candidate assessment](https://github.com/xtltt56-cmd/a-share-quant-workbench/blob/50ccb79c36c6fced40a14d2afc2a0fb232b4f38c/docs/OPEN_SOURCE_EVALUATION.md)
- [辅助 Skill 安装与适配 / Skill installation and adaptation](https://github.com/xtltt56-cmd/a-share-quant-workbench/blob/50ccb79c36c6fced40a14d2afc2a0fb232b4f38c/docs/RICEQUANT_SKILLS_ADAPTER.md)
- [实际存储实现 / Storage implementation](https://github.com/xtltt56-cmd/a-share-quant-workbench/blob/50ccb79c36c6fced40a14d2afc2a0fb232b4f38c/src/a_share_quant/storage/market_store.py)
- [Windows tests：成功 / Successful CI run](https://github.com/xtltt56-cmd/a-share-quant-workbench/actions/runs/34825835392)

## Windows 鼠标录制工具 / Windows mouse recorder

**需求：** 录制全局鼠标事件，并提供模板、倒计时和回放控制，交付可直接运行的 Windows 程序。

**做法：** 项目锁定 `pynput==1.8.2`，录制器直接使用 `pynput.mouse.Listener`；项目代码处理事件模型和录制、回放状态。发布流程执行单元测试、Windows 打包和打包后冒烟检查，再提供下载。

**可借鉴之处：** 复用适用的底层能力，把自行实现集中在产品行为，并将测试与可下载产物接起来。

This tool uses a pinned `pynput` dependency for global mouse capture and keeps event models and playback controls in project code. Its release workflow runs unit tests, builds the Windows executable, and performs a packaged smoke check before publication.

- [依赖版本 / Pinned dependency](https://github.com/xtltt56-cmd/windows-mouse-recorder/blob/cea92f02b57132671d5c5b4b50e4fcd732f629e4/requirements.txt)
- [录制器实现 / Recorder implementation](https://github.com/xtltt56-cmd/windows-mouse-recorder/blob/cea92f02b57132671d5c5b4b50e4fcd732f629e4/mouse_clicker/recorder.py)
- [测试和打包流程 / Test and build workflow](https://github.com/xtltt56-cmd/windows-mouse-recorder/blob/cea92f02b57132671d5c5b4b50e4fcd732f629e4/.github/workflows/release.yml)
- [Windows 发布检查：成功 / Successful release checks](https://github.com/xtltt56-cmd/windows-mouse-recorder/actions/runs/34827047453)

## 记录方式 / About these records

上述源码、文档和 CI 状态于 2026-09-26 核对。项目案例说明实际工程用法；Skill 对照实验的版本、方法和结论范围单独记录在 [VALIDATION.md](VALIDATION.md)。欢迎用“任务 → 采用方案 → 项目适配 → 测试结果”的结构补充自己的案例。

The linked source, documentation, and CI status were checked on 2026-09-26. These cases describe engineering practice; versioned skill evaluations are tracked in [VALIDATION.md](VALIDATION.md). To contribute a case, record the task, selected implementation, integration work, and observed test results.
