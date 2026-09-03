---
title: "modsearch"
description: "DSH 网页插件：为没有原生联网能力的模型提供搜索桥梁。"
keywords: "modsearch, search, plugin, deepseek harness, dsh"
---
# modsearch

> ⭐ **207** · ✅ 活跃 · 插件 · 近期 ⬆️ +20

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 207 | 状态 | ✅ 活跃 |
| 作者 | [liustack](https://github.com/liustack) | 更新时间 | 2026-08-20 |
| 子分类 | 🌐 网页搜索 | 能力 | search |

## 一句话介绍

> DSH 网页插件：为没有原生联网能力的模型提供搜索桥梁。

## 详细介绍

Hit a problem? [Open an issue](https://github.com/liustack/modsearch/issues/new/choose). Everything else is welcome on X: **[@liustack](https://x.com/liustack)**. What you built with it, which harness you are on, what should come next. New releases land there first. A community space is on the way.

## ✨ 核心特性

- **🥇 The strongest free web search plugin for DeepSeek Harness (dsh):** one command installs it, `npx -y @deepseek-ai/dsh plugin --profile web add @liustack/mods
- **Free out of the box, no signup.** Search and page fetch run on Firecrawl Keyless by default: [1,000 free credits/month](https://www.firecrawl.dev/blog/firecra
- **Automatic failover.** When a channel fails or exhausts its quota, the next one takes over.
- **Per-engine key rotation.** Give Tavily, Exa, or Firecrawl multiple comma-separated keys. Authentication, rate-limit, and quota failures rotate to the next key
- **Searches X (Twitter).** With Grok Build installed, ModSearch queries the corpus that web indexes cannot reach.
- **Install once, use everywhere.** Works in Claude Code, Codex, Pi, and OpenCode.

## 🚀 快速开始

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy                                                           # sign in, then exit
```

## 📚 更多信息

**Installation**

**Step 1, hand it to your AI.** Search and page fetch work as soon as the skill lands, on Firecrawl's free keyless quota, so installation is one message: > Install and configure the modsearch skill following INSTALL.md at https://github.com/liustack/modsearch, then run the health check and tell me the result. **Step 2 (optional), add more free engines.** Antigravity CLI writes better synthesized a

**Usage**

Once installed, you do not need to remember any commands. Just chat. Ask anything that needs checking, or paste a URL, and the skill triggers on its own: it picks an engine, runs the search or fetch, and the answer comes back with sources.

## 🔗 链接

- [GitHub 仓库](https://github.com/liustack/modsearch)
- [完整 README](https://github.com/liustack/modsearch#readme)
- [返回modsearch所在分类](../plugins.md)
