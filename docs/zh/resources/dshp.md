---
title: "dshp"
description: "Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file."
keywords: "dshp, discovery, plugin, coding, deepseek harness, dsh"
---
# dshp

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [asdf17128](https://github.com/asdf17128) | 更新时间 | 2026-08-16 |

## 一句话介绍

> Manage DeepSeek Harness profiles — list, create, clone, diff, and share a whole dsh setup as one portable file.

## 详细介绍

**Hand your whole dsh setup to someone as one file — and they get the exact same tree.** npx github:asdf17128/dshp ls Shows every profile on your machine in one line each. Read-only, zero dependencies. ---

## 📦 安装

```bash
dshp clone web web-试验田      # instant, keeps node_modules
dsh plugin --profile web-试验田 add some-experimental-plugin
dshp diff web web-试验田
```

## 🚀 快速开始

```bash
web -> web-试验田

plugins
  + some-experimental-plugin@^0.2.0
```

## 📚 更多信息

**Install and uninstall**

As a CLI: `npx dshp ls` — nothing to install. As a plugin: dsh plugin --profile web add github:asdf17128/dshp # install dsh plugin --profile web remove dshp # uninstall Removing it drops the `list_profiles` and `export_profile` tools. Your profiles are untouched — the plugin only reads.

## 🔗 链接

- [GitHub 仓库](https://github.com/asdf17128/dshp)
- [完整 README](https://github.com/asdf17128/dshp#readme)
- [返回dshp所在分类](../plugins.md)
