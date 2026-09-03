---
title: "dsh-multica-runtime"
description: "在 Multica 上支持 dsh 运行时。"
keywords: "dsh-multica-runtime, desktop, client, deepseek harness, dsh"
---
# dsh-multica-runtime

> ⭐ **53** · ✅ 活跃 · 客户端 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 53 | 状态 | ✅ 活跃 |
| 作者 | [multica-ai](https://github.com/multica-ai) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 在 Multica 上支持 dsh 运行时。

## 详细介绍

Private, out-of-tree runtime bridge between Multica and the public [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It exposes a versioned JSONL protocol over stdio and composes over `@deepseek-ai/dsh-base`. It does not require changes to DeepSeek Harness.

## ✨ 核心特性

- This repository contains only the Multica integration layer. It does not
- Never commit API keys, MCP secrets, session logs, or generated profiles.
- DSH telemetry is disabled by the bundle patch.
- stdout is protocol-only; diagnostics go to stderr.

## 📦 安装

```bash
pnpm install
pnpm check
pnpm build
```

## 🚀 快速开始

```bash
dsh plugin --profile multica add /absolute/path/to/multica-dsh-runtime
```

## 🔗 链接

- [GitHub 仓库](https://github.com/multica-ai/dsh-multica-runtime)
- [完整 README](https://github.com/multica-ai/dsh-multica-runtime#readme)
- [返回dsh-multica-runtime所在分类](../clients.md)
