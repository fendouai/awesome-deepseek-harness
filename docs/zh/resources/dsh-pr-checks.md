---
title: "dsh-pr-checks"
description: "DSH 插件（宿主端 + Web 客户端）：在侧边栏底部按工作区/项目分组展示各打开 PR 的 GitHub Actions 检查状态与进度。"
keywords: "dsh-pr-checks, ui, plugin, git, deepseek harness, dsh"
---
# dsh-pr-checks

> ⭐ **0** · 🧪 实验性 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 0 | 状态 | 🧪 实验性 |
| 作者 | [pauloapoloni](https://github.com/pauloapoloni) | 更新时间 | — |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui, git |

## 一句话介绍

> DSH 插件（宿主端 + Web 客户端）：在侧边栏底部按工作区/项目分组展示各打开 PR 的 GitHub Actions 检查状态与进度。

## 详细介绍

[DSH](https://github.com/deepseek-ai/deepseek-harness) plugin (host + web client) that shows, in the sidebar footer, the **status and progress of the checks** (GitHub Actions) of the open PRs, grouped by **Workspace → Project → PR**. - Progress bar per PR (`done/total`), colored dots per check (tooltip with the name) and a "PR checks" header. - Only PRs with checks **still running** (`IN_PROGRESS`/`QUEUED`/`PENDING`) are shown: when they finish, the PR drops out of the list — and with nothing running, the whole widget **hides** (it comes back when a check starts running again). - Hidden when the sidebar is collapsed. - **Durable**: complete profile plugin, no patch to the DSH runtime files — survives DSH updates.

## ✨ 核心特性

- Progress bar per PR (`done/total`), colored dots per check (tooltip with the name) and a "PR checks" header.
- Only PRs with checks **still running** (`IN_PROGRESS`/`QUEUED`/`PENDING`) are shown: when they finish, the PR drops out of the list — and with nothing running, 
- Hidden when the sidebar is collapsed.
- **Durable**: complete profile plugin, no patch to the DSH runtime files — survives DSH updates.

## 📦 安装

```bash
dsh plugin --profile <name> add dsh-pr-checks
# or directly from the git repository:
# dsh plugin --profile <name> add github:pauloapoloni/dsh-pr-checks
```

## 🚀 快速开始

```bash
cd ~/.dsh/profiles/web
npm install github:pauloapoloni/dsh-pr-checks
```

## 📚 更多信息

**Installation**

The package is a DSH **bundle** (manifest `dsh.bundle`): it ships its own `cordis.patch.yml` layer, so installing it also registers the plugin row. Published on npm as `dsh-pr-checks`. To install it in a profile: dsh plugin --profile <name> add dsh-pr-checks

## 🔗 链接

- [GitHub 仓库](https://github.com/pauloapoloni/dsh-pr-checks)
- [完整 README](https://github.com/pauloapoloni/dsh-pr-checks#readme)
- [返回dsh-pr-checks所在分类](../plugins.md)
