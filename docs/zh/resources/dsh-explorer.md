---
title: "dsh-explorer"
description: "DSH plugin: VS Code-style file-tree explorer (git decorations, preview, diff, drag-to-reference); install via dsh plugin --profile web add."
keywords: "dsh-explorer, search, plugin, coding, git, deepseek harness, dsh"
---
# dsh-explorer

> ⭐ **9** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [No-PRM](https://github.com/No-PRM) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, git |

## 一句话介绍

> DSH plugin: VS Code-style file-tree explorer (git decorations, preview, diff, drag-to-reference); install via dsh plugin --profile web add.

## 详细介绍

A file-tree sidebar for the DeepSeek Harness web UI. A blue round button on the right edge opens a drawer with the current workspace's files — lazy-loaded and virtualized, so even big directories stay responsive. The plugins only add UI and a few read-only routes. Nothing in the shipped dsh packages is touched, so dsh updates shouldn't break anything.

## 📦 安装

```bash
dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-explorer"
dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-client-ui-explorer"
# restart dsh
```

## 🚀 快速开始

```bash
- insert:
    - id: filetree
      name: dsh-explorer-v1
    - id: ui-filetree
      name: dsh-client-ui-explorer
```

## 📚 更多信息

**Install (two commands — monorepo)**

dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-explorer" dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-client-ui-explorer"

**Install**

You need both halves. Bundle install (monorepo — one command per package): dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-explorer" dsh plugin --profile web add "github:No-PRM/dsh-explorer#main&path:/dsh-plugins/dsh-client-ui-explorer"

## 🔗 链接

- [GitHub 仓库](https://github.com/No-PRM/dsh-explorer)
- [完整 README](https://github.com/No-PRM/dsh-explorer#readme)
- [返回dsh-explorer所在分类](../plugins.md)
