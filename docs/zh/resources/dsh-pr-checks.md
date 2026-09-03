---
title: "dsh-pr-checks"
description: "DSH 插件（宿主端 + Web 客户端）：在侧边栏底部按工作区/项目分组展示各打开 PR 的 GitHub Actions 检查状态与进度。"
keywords: "dsh-pr-checks, ui, plugin, git, deepseek harness, dsh"
---
# dsh-pr-checks

> ⭐ 0 · 🧪 实验性 · 插件

## 一句话介绍

DSH 插件（宿主端 + Web 客户端）：在侧边栏底部按工作区/项目分组展示各打开 PR 的 GitHub Actions 检查状态与进度。

## 详细介绍

[DSH](https://github.com/deepseek-ai/deepseek-harness) plugin (host + web client) that shows, in the sidebar footer, the **status and progress of the checks** (GitHub Actions) of the open PRs, grouped by **Workspace → Project → PR**. - Progress bar per PR (`done/total`), colored dots per check (tooltip with the name) and a "PR checks" header. - Only PRs with checks **still running** (`IN_PROGRESS`/`QUEUED`/`PENDING`) are shown: when they finish, the PR drops out of the list — and with nothing ru

## 作者
**[pauloapoloni](https://github.com/pauloapoloni)**

## 链接

- [GitHub 仓库](https://github.com/pauloapoloni/dsh-pr-checks)
- [完整 README](https://github.com/pauloapoloni/dsh-pr-checks#readme)
- [返回dsh-pr-checks所在分类](../plugins.md)
