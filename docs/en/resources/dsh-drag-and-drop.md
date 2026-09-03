---
title: "dsh-drag-and-drop"
description: "Cross-platform drag & drop for DSH Web UI with original-path insertion, no file copying."
keywords: "dsh-drag-and-drop, input-editing, plugin, files, ui, deepseek harness, dsh"
---
# dsh-drag-and-drop

> ⭐ **20** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Input & editing |
| Stars | ⭐ 20 | Status | ✅ active |
| Author | [bill9109](https://github.com/bill9109) | Updated | 2026-08-21 |

## One-liner

> Cross-platform drag & drop for DSH Web UI with original-path insertion, no file copying.

## About

**Install:** `dsh plugin --profile web add github:omdsh-dev/dsh-drag-and-drop` **A DeepSeek Harness Web UI plugin: drag local files or folders onto any part of the page and their original absolute filesystem paths are inserted into the current conversation input — without uploading, moving, or copying anything.** [English](README.md) | [中文](README.zh.md)

## ✨ Key Features

- Drag files onto any part of the Web UI to insert their original absolute paths
- Full-page dim + blur hint while dragging
- Supports files and folders; drag multiple items at once — one path per line
- Native paths on macOS, Linux, and Windows
- POSIX paths, Windows drive-letter paths, and UNC network paths
- No uploading, moving, or copying of files
- Locates files in the current Workspace and registered Workspaces first
- When the browser hides the original path, uses the local file index and bounded directory search

## 📦 Install

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-drag-and-drop
# or from a local checkout:
dsh plugin --profile web add /path/to/dsh-drag-and-drop
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update github:omdsh-dev/dsh-drag-and-drop
```

## 📚 Learn more

**Usage**

Drag files or folders from Finder, a Linux file manager, or Windows Explorer onto any part of the DSH Web UI. Release the mouse when the full-page drag hint appears; the plugin writes the resolved original absolute path into the current conversation input. Dropping multiple items at once inserts one path per line.

**Install**

The plugin is a DSH **bundle** (`package.json` declares `dsh.bundle` + `dsh.client`). Install it into the `web` profile with the standard `dsh plugin` mechanism — **no DSH source changes and no `config.yaml` needed**: dsh plugin --profile web add github:omdsh-dev/dsh-drag-and-drop

**Uninstall**

dsh plugin --profile web remove dsh-drag-and-drop The command removes the package from the profile and from `dsh.profile.bundles`. After uninstalling, restart the Web UI and hard-refresh the browser.

## 🔗 Links

- [GitHub Repository](https://github.com/bill9109/dsh-drag-and-drop)
- [Full README](https://github.com/bill9109/dsh-drag-and-drop#readme)
- [Back to the Plugins list](../plugins.md)
