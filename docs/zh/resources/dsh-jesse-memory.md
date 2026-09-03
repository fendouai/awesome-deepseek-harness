---
title: "dsh-memory (Jesse-njx)"
description: "基于 DSH 无损会话日志的引用式记忆：可人工审计的蒸馏事实，带引用来源。"
keywords: "dsh-memory (Jesse-njx), memory, plugin, deepseek harness, dsh"
---
# dsh-memory (Jesse-njx)

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | 2026-08-13 |
| 子分类 | 🧠 记忆系统 | 能力 | memory |

## 一句话介绍

> 基于 DSH 无损会话日志的引用式记忆：可人工审计的蒸馏事实，带引用来源。

## 详细介绍

**Cited memory over DSH's lossless session log.** Distilled facts that can always escalate back to the exact original context. `dsh-memory` is a DeepSeek Harness bundle. When a session ends, a background distillation pass extracts durable facts — user preferences, project decisions, environment quirks, corrections — into small markdown files under `~/.dsh/memory/`. Every memory carries a **citation** `(sessionId, [start..end])` pointing at the exact log events it came from. The next session gets a compact index of those memories, plus two tools: `memory_read` (the full memory) and `memory_expand` (the cited original log excerpt). The key idea: **summaries are an index into ground truth, never the truth.** Retrieval surfaces the one-line distilled fact (cheap); when the agent needs more, `m

## 📦 安装

```bash
dsh plugin --profile web add @dsh-memory/bundle
```

## 🚀 快速开始

```bash
The user prefers TypeScript for new projects and tests.
```

## 📚 更多信息

**Install**

dsh plugin --profile web add @dsh-memory/bundle The distillation pass routes through `ctx.llm` — it reuses the session's own provider/model by default, so a polyglot-style provider chain or your normal model serves it too. Override with `distill.provider` / `distill.model`.

**Config**

All fields optional (profile patch or `cordis.patch.yml`): plugins: dsh-memory: enabled: true home: ~/.dsh/memory # memory root override (default: $DSH_HOME/memory or ~/.dsh/memory) maxIndexTokens: 800 # hard token cap for the injected recall index maxExpandBytes: 8192 # output byte cap for one memory_expand excerpt recall: enabled: true cacheMs: 5000 # index cache TTL distill: enabled: true provi

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-memory)
- [完整 README](https://github.com/Jesse-njx/dsh-memory#readme)
- [返回dsh-memory (Jesse-njx)所在分类](../plugins.md)
