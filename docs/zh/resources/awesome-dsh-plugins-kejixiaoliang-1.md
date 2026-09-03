---
title: "awesome-dsh-plugins (kejixiaoliang)"
description: "DSH 插件精选目录：14 类 280+ 个社区插件，覆盖 MCP/Skill/TUI/多 Agent/上下文记忆/UI 皮肤。"
keywords: "awesome-dsh-plugins (kejixiaoliang), registry, awesome-list, search, deepseek harness, dsh"
---
# awesome-dsh-plugins (kejixiaoliang)

> ⭐ **22** · ✅ 活跃 · 精选列表

| | | | |
|---|---|---|---|
| 类型 | 精选列表 | 分类 | 注册表 |
| 星数 | ⭐ 22 | 状态 | ✅ 活跃 |
| 作者 | [kejixiaoliang](https://github.com/kejixiaoliang) | 更新时间 | 2026-08-21 |

## 一句话介绍

> DSH 插件精选目录：14 类 280+ 个社区插件，覆盖 MCP/Skill/TUI/多 Agent/上下文记忆/UI 皮肤。

## 详细介绍

**A curated directory of 306+ [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) plugins across 14 categories — every entry with ⭐ stars and a `dsh plugin add` command. Bilingual (EN + 中文), machine-readable data, auto-sync CI.** **English** · [中文版](README.zh.md) [Quick Start](#quick-start) · [Hot Plugins](#hot-plugins) · [Categories](#categories) · [Browse All](#browse-all-plugins) · [Full Index](INDEX.md) · [Contributing](CONTRIBUTING.md) ---

## ✨ 核心特性

- ✅ Official install: `dsh plugin --profile <name> add <pkg>` (forwards to pnpm; npm / git / tarball)
- ✅ Official discovery: npm + the GitHub [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic (**no built-in marketplace**)

## 📦 安装

```bash
# Install a plugin (forwards to pnpm; npm / git / tarball all supported)
dsh plugin --profile <name> add <pkg>

# Example
dsh plugin add dsh-cc-tui
```

## 🚀 快速开始

```bash
import type { Context } from '@deepseek-ai/cordis'
export const name = 'hello-plugin'
export function apply(ctx: Context) {
  // register a tool, a command, a UI node, ...
}
```

## 📚 更多信息

**⚡ Quick Start**

Three ways to use this directory: 1. **Browse** — expand any category below (or jump into a category file); each entry links straight to its GitHub repo. 2. **Search** — press `t` (or `Ctrl+F`) on the repo page and search keywords like `mcp`, `memory`, `TUI`, `multi-agent`. 3. **Consume programmatically** — read [`web/data.js`](web/data.js) (generated from the category files; see [web/README.md](w

**Example**

dsh plugin add dsh-cc-tui Each enriched entry above shows its install command, e.g. `` `dsh plugin add <npm-package>` ``.

## 🔗 链接

- [GitHub 仓库](https://github.com/kejixiaoliang/awesome-dsh-plugins)
- [完整 README](https://github.com/kejixiaoliang/awesome-dsh-plugins#readme)
- [返回awesome-dsh-plugins (kejixiaoliang)所在分类](../awesome-lists.md)
