---
title: "dsh-at-file"
description: "Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts."
keywords: "dsh-at-file, search, plugin, coding, deepseek harness, dsh"
---
# dsh-at-file

> ⭐ **505** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 505 | 状态 | ✅ 活跃 |
| 作者 | [FSMargoo](https://github.com/FSMargoo) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, search |

## 一句话介绍

> Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their path to prompts.

## 详细介绍

Workspace path references for the DeepSeek Harness web interface. Type `@` in the composer to search the current workspace and insert a file or directory path.

## 📦 安装

```bash
dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.7.0.tar.gz
```

## 🚀 快速开始

```bash
- id: dsh-at-file
  config:
    maxIndexedFiles: 10000
```

## 📚 更多信息

**Usage**

Choose a result from the `@` menu. The selected path remains visible in the draft and can be opened or removed from the reference bar. Review @docs/spec.pdf Before the agent starts a step, the plugin confirms that the path exists inside the active workspace. It then adds a short reference message: <workspace-reference path="docs/spec.pdf" kind="file" /> The reference contains the workspace-relativ

**Install or Update**

dsh plugin --profile web add https://github.com/omdsh-dev/dsh-at-file/archive/refs/tags/v0.7.0.tar.gz Use the same command to update an existing installation. Restart `dsh web` after installation so the Host and browser client load version `0.7.0`. Version `0.7.0` supports both the 0.1.1 and 0.1.2 Harness client package layouts. It also restores the default file ignores for installations that pers

**Configuration**

The available options apply to the path picker index: Add the complete configuration to the selected profile's `cordis.patch.yml`. The usual path is `~/.dsh/profiles/web/cordis.patch.yml`. config: maxIndexedFiles: 10000 Omitting `ignoreDirs` keeps the built-in list. When you provide it, include every directory name you want excluded.

## 🔗 链接

- [GitHub 仓库](https://github.com/FSMargoo/dsh-at-file)
- [完整 README](https://github.com/FSMargoo/dsh-at-file#readme)
- [返回dsh-at-file所在分类](../plugins.md)
