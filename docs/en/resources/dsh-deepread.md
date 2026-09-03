---
title: "dsh-deepread"
description: "Evidence-first deep reading for AI agents — trace claims, evidence, confidence and knowledge maps across articles, books and PDFs."
keywords: "dsh-deepread, developer, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-deepread

> ⭐ **41** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 41 | Status | ✅ active |
| Author | [xiehuan123](https://github.com/xiehuan123) | Updated | — |
| Subcategory | 📁 Files & import | Capabilities | coding, multi-agent |

## One-liner

> Evidence-first deep reading for AI agents — trace claims, evidence, confidence and knowledge maps across articles, books and PDFs.

## About

[Website](https://xiehuan123.github.io/dsh-deepread/) · [Real outputs](examples/README.md) · English · [中文](README.zh.md) DeepRead is available in two compatible forms: - **Portable Agent Skill** for Codex, Claude Code, and other Agent Skills-compatible tools. Zero runtime dependencies; the agent follows the evidence-first reading workflow with its own file and web tools. - **Host plugin package** for DeepSeek Harness Web/headless and dsh-TUI, with a `deepread` tool, PDF extraction, optional persistence/jobs/Web route, batch comparison, cost preview, and HTML/XMind-compatible export. Its browser client is an optional Web-only entry.

## ✨ Key Features

- **Portable Agent Skill** for Codex, Claude Code, and other Agent Skills-compatible tools. Zero runtime dependencies; the agent follows the evidence-first readin
- **Host plugin package** for DeepSeek Harness Web/headless and dsh-TUI, with a `deepread` tool, PDF extraction, optional persistence/jobs/Web route, batch compar

## 📦 Install

```bash
dsh plugin --profile web add dsh-deepread
```

## 🚀 Quick Start

```bash
# Stable npm release (after 1.0.0 is published)
dsh plugin --profile web add dsh-deepread

# Exact npm version (after 1.0.0 is published)
dsh plugin --profile web add dsh-deepread@1.0.0

# Exact GitHub tag (after v1.0.0 is created)
dsh plugin --profile web add "github:xiehuan123/dsh-deepread#v1.0.0"
```

## 📚 Learn more

**Installation**

DeepRead `1.0.0` requires Node.js **22.19 or 24 and higher** (`^22.19 || >=24`). The same npm package exposes the TypeScript Host entry at `lib/types/index.js`, the dsh-TUI Community Consensus v0.15 manifest at `dsh-plugin.json`, and an optional DeepSeek Harness Web client at `lib/client.js`.

**Examples**

Please deep-read this link: https://mp.weixin.qq.com/s/xxxx Read book.pdf in knowledge-map mode and export html Quickly summarize this article: <paste text>

**Plugin configuration (Config)**

`timeoutMs` (default 900000), `chunkChars` (default 6000), `maxParts` (default 20), `maxInputChars` (default 400000), `cacheEnabled` (default true), `cacheTtlHours` (default 168, 0 disables caching) can all be overridden in the cordis row, for example: - id: deepread name: dsh-deepread config: timeoutMs: 600000 cacheTtlHours: 24

## 🔗 Links

- [GitHub Repository](https://github.com/xiehuan123/dsh-deepread)
- [Full README](https://github.com/xiehuan123/dsh-deepread#readme)
- [Back to the Plugins list](../plugins.md)
