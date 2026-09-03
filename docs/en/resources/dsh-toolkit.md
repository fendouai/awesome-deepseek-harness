---
title: "dsh-toolkit"
description: "Zero-dependency tool suite: calculator, CSV, diff, encoding, JSON, Markdown, regex and time utilities."
keywords: "dsh-toolkit, developer, plugin, files, coding, deepseek harness, dsh"
---
# dsh-toolkit

> ⭐ **24** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 24 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |
| Subcategory | 🧪 Code, tests & review | Capabilities | files, coding |

## One-liner

> Zero-dependency tool suite: calculator, CSV, diff, encoding, JSON, Markdown, regex and time utilities.

## About

[English](README.en.md) DSH 零依赖工具包 collection —— time / encoding / json / calculator / csv / regex / markdown / diff / stat / schema 十个确定性工具，**统一入口一键安装**。

## 📦 Install

```bash
# 安装单个工具到 web profile
dsh plugin --profile web add github:omdsh-dev/dsh-tool-csv
# 一次性任务（headless）profile
dsh plugin --profile headless add github:omdsh-dev/dsh-tool-diff
```

## 🚀 Quick Start

```bash
./scripts/install-web.sh       # 全部 10 工具 → web profile
./scripts/install-headless.sh  # 全部 10 工具 → headless profile（dsh run 使用面）
./scripts/install-all.sh       # 两个 profile 都装
```

## 📚 Learn more

**手动安装与旧版本兼容**

旧场景（monorepo 集成、不支持 Profile Bundle 的旧快照或插件开发调试环境——本地 junction/symlink、手动编辑 profile 层）。

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-toolkit)
- [Full README](https://github.com/omdsh-dev/dsh-toolkit#readme)
- [Back to the Plugins list](../plugins.md)
