---
title: "dsh-git-status"
description: "Git status (Git Graph) plugin for DSH: commit DAG lane graph + uncommitted changes/stash + inline diffs + branch operations. DSH 插件：Git 状态浮窗（泳道图/未提交/stash/diff/分支操作）。"
keywords: "dsh-git-status, developer, plugin, coding, git, deepseek harness, dsh"
---
# dsh-git-status

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [Wongzexu](https://github.com/Wongzexu) | 更新时间 | — |
| 子分类 | 🧪 代码·测试·审查 | 能力 | coding, git |

## 一句话介绍

> Git status (Git Graph) plugin for DSH: commit DAG lane graph + uncommitted changes/stash + inline diffs + branch operations. DSH 插件：Git 状态浮窗（泳道图/未提交/stash/diff/分支操作）。

## 详细介绍

[**English**](README_EN.md) · **简体中文** 独立 Git 状态（Git Graph）插件：DSH Web 右缘 **Git 状态浮窗** —— commit DAG 泳道图 + 未提交改动/stash + 行内详情 diff + 分支操作。 🔖 **v1.0.0** · 🧩 纯前端自渲染 DOM（greeter 模式，零 React、零构建链）· 🛠 Node half 只读/写路由 · 📜 MIT · 📦 npm `@wongzexu/dsh-git-status`

## ✨ 核心特性

- **浮窗交互**：面板可**拖拽**、位置**自动记忆**；右上角悬浮开关按钮（与面板角重合、拖拽跟随、关闭后原位悬浮重开）；
- **commit DAG 泳道图**：第一父链成线、列分配贪心最左、泳道复用、合并提交连线；
- **行内 refs 徽标**：H（红，游离 HEAD）/ 分支（金）/ 远程（蓝）/ 标签（绿）；当前 checkout 分支 pill 亮金高亮
- **未提交改动虚拟行**：工作区有改动时图顶部插入虚拟行（空心圆 + 灰色虚线连 HEAD），
- **暂存与提交**：右键未提交改动虚拟行可「暂存全部改动」（`git add -A`）、
- **stash 显示**：`git reflog refs/stash` 插入图中（双层圆 + `stash@{n}` 徽标），
- **行内展开详情**：点击 commit 行 → 展开提交信息 + 变更文件（+/- 行数）+ 逐文件 diff
- **分支操作**：

## 📦 安装

```bash
dsh plugin --profile web add @wongzexu/dsh-git-status
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:Wongzexu/dsh-git-status
```

## 📚 更多信息

**安装插件**

**方式一：npm 安装（推荐，发布版）** dsh plugin --profile web add @wongzexu/dsh-git-status **方式二：从 GitHub 安装（源码版）** dsh plugin --profile web add github:Wongzexu/dsh-git-status **方式三：本地目录安装（开发/自用）** dsh plugin --profile web add /path/to/dsh-git-status 把 `/path/to/dsh-git-status` 换成插件目录的实际路径（例如本仓库根目录）。 > ⚠️ 注意：npm 上另有同名（无作用域）包 `dsh-git-status`（其他作者的 React 实现，与本插件无关）；安装请认准 **`@wongzexu/dsh-git-status`**。

**使用**

> 📖 完整操作指南（中英双语）：[docs/USAGE.md](docs/USAGE.md) —— 界面速览、Git 图阅读、分支操作、冲突处理、远程拉取全流程详解。 1. 进入任意聊天视图（对话界面）； 2. 点击面板右上角外侧的 **分支图标** 按钮，展开「Git 状态」浮窗（浮窗可拖拽，位置自动记忆；按钮始终贴在浮窗右上角，关闭后留在原位悬浮，点击重新展开；首次使用有引导提示）； 3. 浮窗头部可切换「所有分支 / 当前分支」、手动刷新（↻）；打开期间 SSE 即时刷新（断连时 10s 轮询兜底）； 4. 点击 commit 行展开详情（提交信息 / 变更文件 / 逐文件 diff）；点击文件行查看该文件 patch； 5. 右键分支徽标：本地「切换到 x / 推送到远程… / 合并 x / 重命名 x / 删除 x（可强删）/ 变基当前分支到 x（红色确认，重写历史）」；远程「

## 🔗 链接

- [GitHub 仓库](https://github.com/Wongzexu/dsh-git-status)
- [完整 README](https://github.com/Wongzexu/dsh-git-status#readme)
- [返回dsh-git-status所在分类](../plugins.md)
