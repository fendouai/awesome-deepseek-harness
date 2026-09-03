---
title: "dsh-mneme"
description: "Local cross-session memory with memory sovereignty: SQLite + human-editable Markdown mirror and background autoDream consolidation."
keywords: "dsh-mneme, memory, plugin, deepseek harness, dsh"
---
# dsh-mneme

> ⭐ **31** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Memory & context |
| Stars | ⭐ 31 | Status | ✅ active |
| Author | [modusensus](https://github.com/modusensus) | Updated | 2026-08-21 |
| Subcategory | 🧠 Memory systems | Capabilities | memory |

## One-liner

> Local cross-session memory with memory sovereignty: SQLite + human-editable Markdown mirror and background autoDream consolidation.

## About

`dsh-mneme` 是一个 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness) 插件，为 Agent 提供持久的跨会话记忆能力。**Mneme**（Μνήμη）——希腊记忆女神 Mnemosyne 之名，掌管记忆与梦境，正如 autoDream 在后台巩固记忆。

## ✨ Key Features

- **跨会话记忆** — 对话中 AI 自动记录关键信息，新会话自动注入相关记忆
- **自动整理** — 后台自动去重、合并、归档，记忆库越用越精炼
- **删对话 ≠ 删记忆** — 删除聊天窗口不会丢掉已保存的记忆（可配置）
- **你的数据你做主** — 所有记忆以 Markdown 格式存于本地，随时打开查看和编辑
- **完全离线** — 默认无需 API Key，所有处理在本地完成

## 📦 Install

```bash
# 安装插件（自动注册 bundle 层）
dsh plugin --profile web add @modusensus/dsh-mneme
dsh web
```

## 🚀 Quick Start

```bash
🧬 基因（v0.3.0）→ 🛡️ 审计加固（v0.3.6–0.3.9）→ 💤 睡眠维护（v0.4.0）→ 🕸️ 召回融合与图谱（v0.5.0）→ ✨ 面板增强（v0.6.x）→ 🌡️ 自进化记忆（v0.7.0）→ 🕸️ 图谱增强（v0.8.0）
```

## 📚 Learn more

**安装插件（自动注册 bundle 层）**

dsh plugin --profile web add @modusensus/dsh-mneme dsh web > 需要 Node 24+（`node:sqlite`）。完整安装 / 配置 / 架构见 [插件文档](dsh-mneme/README.md)。

**🗺️ 路线图**

🧬 基因（v0.3.0）→ 🛡️ 审计加固（v0.3.6–0.3.9）→ 💤 睡眠维护（v0.4.0）→ 🕸️ 召回融合与图谱（v0.5.0）→ ✨ 面板增强（v0.6.x）→ 🌡️ 自进化记忆（v0.7.0）→ 🕸️ 图谱增强（v0.8.0）

**Install**

dsh plugin --profile web add @modusensus/dsh-mneme dsh web > Requires Node 24+ (`node:sqlite`). Full install / config / architecture docs in the [plugin README](dsh-mneme/README.md).

**Quick Config (Optional)**

Works out of the box. Enable these as needed: > Change in DSH Settings Panel → Memory Settings. Full config docs [here](dsh-mneme/docs/CONFIG.md).

## 🔗 Links

- [GitHub Repository](https://github.com/modusensus/dsh-mneme)
- [Full README](https://github.com/modusensus/dsh-mneme#readme)
- [Back to the Plugins list](../plugins.md)
