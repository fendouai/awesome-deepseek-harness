---
title: "dsh-web-search-exa"
description: "零配置 Exa 网页搜索：免密钥匿名 MCP 回退 + API Key REST 搜索。"
keywords: "dsh-web-search-exa, search, plugin, deepseek harness, dsh"
---
# dsh-web-search-exa

> ⭐ **6** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [TonyDua](https://github.com/TonyDua) | 更新时间 | 2026-08-14 |
| 子分类 | 🌐 网页搜索 | 能力 | search |

## 一句话介绍

> 零配置 Exa 网页搜索：免密钥匿名 MCP 回退 + API Key REST 搜索。

## 详细介绍

Built with [deepseek-v4-flash](https://api-docs.deepseek.com) inside DeepSeek Harness (dsh).

## ✨ 核心特性

- 🆓 **Zero-config, keyless by default** — searches route through Exa's hosted MCP
- 🔑 **Keyed REST upgrade** — set `EXA_API_KEY` and it automatically switches to
- 🔌 **Drop-in provider** — registers into the dsh `ctx.web` seam; the existing
- 🎛️ **`providerId` switch** — can coexist with the official
- 📦 **npm-publishable** — MIT, ESM, bundled types, `files` limited to `lib/`.

## 📦 安装

```bash
dsh plugin --profile web add @tonydua/dsh-web-search-exa
```

## 🚀 快速开始

```bash
- id: web
  name: '@deepseek-ai/dsh-web'
  config:
    searchProvider: exa
```

## 📚 更多信息

**Installation (into a dsh profile)**

**One command from npm** (v0.1.3+ ships the `dsh.bundle` manifest — the bundle patch inserts the provider row, so no manual patch editing is needed): dsh plugin --profile web add @tonydua/dsh-web-search-exa Restart `dsh web`. **Without an API key** the official DeepSeek search provider is unavailable, so the seam auto-selects this provider — fully zero-config. **With a key configured**, select Exa

**FAQ**

**Q: Do I need an Exa API key?** No. Without a key the provider uses Exa's free anonymous hosted MCP. With a key it uses the REST API for higher limits. **Q: I got HTTP 429 / rate limited.** That's Exa's anonymous-MCP rate limit. Configure `EXA_API_KEY` (or the `apiKey` field) and the provider switches to the REST path automatically. **Q: Can I run this alongside the official Exa provider?** Yes —

## 🔗 链接

- [GitHub 仓库](https://github.com/TonyDua/dsh-web-search-exa)
- [完整 README](https://github.com/TonyDua/dsh-web-search-exa#readme)
- [返回dsh-web-search-exa所在分类](../plugins.md)
