---
title: "dsh-drag-and-drop"
description: "DSH Web UI 跨平台文件拖拽与原始路径插入，无需复制文件。"
keywords: "dsh-drag-and-drop, input-editing, plugin, files, ui, deepseek harness, dsh"
---
# dsh-drag-and-drop

> ⭐ **20** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 输入与编辑 |
| 星数 | ⭐ 20 | 状态 | ✅ 活跃 |
| 作者 | [bill9109](https://github.com/bill9109) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH Web UI 跨平台文件拖拽与原始路径插入，无需复制文件。

## 详细介绍

**Install:** `dsh plugin --profile web add github:omdsh-dev/dsh-drag-and-drop` **A DeepSeek Harness Web UI plugin: drag local files or folders onto any part of the page and their original absolute filesystem paths are inserted into the current conversation input — without uploading, moving, or copying anything.** [English](README.md) | [中文](README.zh.md)

## ✨ 核心特性

- Drag files onto any part of the Web UI to insert their original absolute paths
- Full-page dim + blur hint while dragging
- Supports files and folders; drag multiple items at once — one path per line
- Native paths on macOS, Linux, and Windows
- POSIX paths, Windows drive-letter paths, and UNC network paths
- No uploading, moving, or copying of files
- Locates files in the current Workspace and registered Workspaces first
- When the browser hides the original path, uses the local file index and bounded directory search

## 📦 安装

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-drag-and-drop
# or from a local checkout:
dsh plugin --profile web add /path/to/dsh-drag-and-drop
```

## 🚀 快速开始

```bash
dsh plugin --profile web update github:omdsh-dev/dsh-drag-and-drop
```

## 📚 更多信息

**Usage**

Drag files or folders from Finder, a Linux file manager, or Windows Explorer onto any part of the DSH Web UI. Release the mouse when the full-page drag hint appears; the plugin writes the resolved original absolute path into the current conversation input. Dropping multiple items at once inserts one path per line.

**Install**

The plugin is a DSH **bundle** (`package.json` declares `dsh.bundle` + `dsh.client`). Install it into the `web` profile with the standard `dsh plugin` mechanism — **no DSH source changes and no `config.yaml` needed**: dsh plugin --profile web add github:omdsh-dev/dsh-drag-and-drop

**Uninstall**

dsh plugin --profile web remove dsh-drag-and-drop The command removes the package from the profile and from `dsh.profile.bundles`. After uninstalling, restart the Web UI and hard-refresh the browser.

## 🔗 链接

- [GitHub 仓库](https://github.com/bill9109/dsh-drag-and-drop)
- [完整 README](https://github.com/bill9109/dsh-drag-and-drop#readme)
- [返回dsh-drag-and-drop所在分类](../plugins.md)
