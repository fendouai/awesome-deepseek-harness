---
title: "dsh-open-in-vscode"
description: "从 Web GUI 直接在工作区中打开 VS Code 目录/文件。"
keywords: "dsh-open-in-vscode, developer, plugin, ide, coding, files, deepseek harness, dsh"
---
# dsh-open-in-vscode

> ⭐ **53** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 53 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-16 |
| 子分类 | 📁 文件与导入 | 能力 | ide, coding, files |

## 一句话介绍

> 从 Web GUI 直接在工作区中打开 VS Code 目录/文件。

## 详细介绍

Open a workspace directory in VS Code straight from the DeepSeek Harness web GUI: every real Workspace row in the sidebar gains an **Open in VSCode** row inside its **…** overflow menu.

## ✨ 核心特性

- The client half uses the harness's `sidebar.workspaces.row-menu` slot when
- The row's click closes the menu and calls the host over the strict Typert
- The host half spawns the configured editor CLI on that directory

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz
```

## 🚀 快速开始

```bash
dsh plugin --profile web list dsh-open-in-vscode --depth 0
```

## 📚 更多信息

**Install**

Add the plugin to your web profile (this runs pnpm inside the profile and reconciles the bundle layer): dsh plugin --profile web add https://github.com/omdsh-dev/dsh-open-in-vscode/archive/refs/tags/v0.1.6.tar.gz Restart the web server (`kill -TERM <pid>` and wait for exit — never `kill -9`, it tears the session zstd log mid-frame), then refresh the page. The host plugin mounts under `dsh-open-in-

**Configuration**

Deployment-varying choices are validated `Config` fields, changeable from cordis.yml: A missing executable fails loud with a fix hint; relative paths are refused.

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-open-in-vscode)
- [完整 README](https://github.com/omdsh-dev/dsh-open-in-vscode#readme)
- [返回dsh-open-in-vscode所在分类](../plugins.md)
