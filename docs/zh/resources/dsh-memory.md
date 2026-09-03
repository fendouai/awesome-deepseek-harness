---
title: "dsh-memory"
description: "Cross-session plaintext memory for DeepSeek Harness: suggested → human-approved, searchable, human owns the data · 跨会话明文记忆：模型写入待审核、人工确认生效，明文可审计"
keywords: "dsh-memory, memory, plugin, coding, search, deepseek harness, dsh"
---
# dsh-memory

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [Max-Null](https://github.com/Max-Null) | 更新时间 | — |
| 子分类 | 🧠 记忆系统 | 能力 | coding, memory, search |

## 一句话介绍

> Cross-session plaintext memory for DeepSeek Harness: suggested → human-approved, searchable, human owns the data · 跨会话明文记忆：模型写入待审核、人工确认生效，明文可审计

## 详细介绍

Cross-session memory vault for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). Every DSH session starts from zero. `dsh-memory` gives your agents a persistent second brain: facts, preferences, decisions, and project notes survive across sessions and are recalled automatically. - **3 model tools** — `memory_remember` / `memory_recall` / `memory_forget` - **Per-turn prompt injection** — the most recent entries are injected into every system-prompt assembly, so the agent starts each turn already aware of stored context - **Durable storage** — records live in a [storage domain](https://github.com/deepseek-ai/deepseek-harness) (`dsh_memory` unit, json backend by default; unit names are snake_case per `UNIT_NAME_RE`) - **Browser management page** — a "记忆库 / Memory" pag

## ✨ 核心特性

- **3 model tools** — `memory_remember` / `memory_recall` / `memory_forget`
- **Per-turn prompt injection** — the most recent entries are injected into every system-prompt assembly, so the agent starts each turn already aware of stored co
- **Durable storage** — records live in a [storage domain](https://github.com/deepseek-ai/deepseek-harness) (`dsh_memory` unit, json backend by default; unit name
- **Browser management page** — a "记忆库 / Memory" page in Settings to browse, add, and delete entries

## 📦 安装

```bash
dsh plugin --profile web add dsh-memory-vault
```

## 🚀 快速开始

```bash
npm install dsh-memory-vault
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-memory-vault The `dsh.bundle` manifest wires the `dsh-memory` row into the profile automatically. To install by hand instead: npm install dsh-memory-vault then add a row to your profile `cordis.yml` (or `cordis.patch.yml`): name: dsh-memory-vault

**Usage**

Tell your agent to remember things, or do it yourself: > "记住：这个项目的部署目标是 Windows，测试命令是 `pnpm test`。" The agent calls `memory_remember` with optional tags: memory_remember(content="User prefers Windows deployment; test command is `pnpm test`", tags=["project:demo", "user"]) When context from an earlier session matters, the agent calls `memory_recall(query="Windows deploy")` — entries are scored by t

## 🔗 链接

- [GitHub 仓库](https://github.com/Max-Null/dsh-memory)
- [完整 README](https://github.com/Max-Null/dsh-memory#readme)
- [返回dsh-memory所在分类](../plugins.md)
