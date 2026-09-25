# Upgrade to ReuseBeacon / 升级到 ReuseBeacon

## 简体中文

`v0.2.0` 将本项目从 **GitHub Reuse First** 更名为 **ReuseBeacon（开源复用导航）**，用于减少与其他同名 Skill 的混淆。功能仍围绕 GitHub 连接检查、成熟方案筛选、复用集成和验证。

| 项目 | v0.1.0 | v0.2.0 起 |
| --- | --- | --- |
| 展示名称 | GitHub Reuse First | ReuseBeacon |
| 技能标识 | `github-reuse-first` | `reusebeacon` |
| 仓库 | `xtltt56-cmd/github-reuse-first` | `xtltt56-cmd/reusebeacon` |
| 技能目录 | `skills/github-reuse-first` | `skills/reusebeacon` |
| Codex 调用 | `$github-reuse-first` | `$reusebeacon` |

### 已安装旧版本

1. 在原来的项目或用户安装范围内安装新技能。以下命令默认安装到当前项目；原来使用用户级安装的用户可加 `--global`，目标工具沿用原来的选择。

   ```shell
   npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
   ```

2. 核对旧技能的来源是否为 `xtltt56-cmd/github-reuse-first`。其他作者也使用过相同技能标识，不能仅凭名称卸载。
3. 确认旧技能没有需要保留的本地修改后，通过目标工具的技能管理功能停用或移除本项目旧版本，避免两个版本同时触发。
4. 将项目说明、技能选择器和常用提示词中的本项目调用改为 `reusebeacon` 或 `$reusebeacon`。根据目标工具的要求重新加载技能或启动新会话。

更改技能标识后，不能假定安装器会把它识别为原技能的原地升级；请使用上面的新安装命令。

### 链接和旧版本

- GitHub 会将原仓库地址转向新地址。旧的仓库 URL 可继续定位项目，但 `--skill github-reuse-first` 选择器需要改成 `--skill reusebeacon`。
- `v0.1.0` 标签、发布说明和原始下载包保留；[旧版本页面](https://github.com/xtltt56-cmd/reusebeacon/releases/tag/v0.1.0)可用于查看原内容。
- `v0.2.0` 提供推荐下载包 `reusebeacon.zip`，同时提供旧文件名 `github-reuse-first.zip` 的兼容下载。两者内容相同，解压后的目录和技能标识均为 `reusebeacon`。
- 旧链接若指向 `main` 分支内的 `skills/github-reuse-first/`，需要更新为 `skills/reusebeacon/`；查看历史文件可使用 `v0.1.0` 标签。
- 本地源码克隆可执行：`git remote set-url origin https://github.com/xtltt56-cmd/reusebeacon.git`。

原有 MIT 版权署名和第三方来源声明保留。维护者应保留旧仓库地址的重定向，避免用同一账号重新创建旧名称仓库；参见 [GitHub 仓库更名说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)。

## English

Starting with `v0.2.0`, **GitHub Reuse First** is named **ReuseBeacon**. The skill identifier is `reusebeacon`, the source is `xtltt56-cmd/reusebeacon`, and Codex invocation is `$reusebeacon`.

Install the new identifier at the same project/user scope and for the same agents as your previous installation:

```shell
npx skills@1.7.0 add xtltt56-cmd/reusebeacon --skill reusebeacon --copy
```

Add `--global` only if your old installation was user-wide. Verify that the old `github-reuse-first` skill came from this repository before disabling or removing it: other authors have used the same identifier. Preserve local edits, update project instructions and invocation examples, and reload skills as your agent requires. An identifier change may not be treated as an in-place update by your installer.

The old repository URL redirects to the new repository. The old `--skill github-reuse-first` selector must still change. The `v0.1.0` tag and original release remain available. The `v0.2.0` release provides both `reusebeacon.zip` and a legacy filename alias, `github-reuse-first.zip`; both contain the same `reusebeacon` folder. Old `main`-branch file links under `skills/github-reuse-first/` must be updated, or pinned to the historical tag.

The original copyright and third-party notices remain intact. Do not recreate the old repository name under this account, because that would replace GitHub's redirect.
