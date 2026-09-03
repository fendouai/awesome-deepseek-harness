---
title: "dsh-mneme"
description: "记忆主权归用户的本地跨会话记忆：SQLite + 可人工编辑的 Markdown 镜像，autoDream 后台巩固。"
keywords: "dsh-mneme, memory, plugin, deepseek harness, dsh"
---
# dsh-mneme

> ⭐ **31** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 31 | 状态 | ✅ 活跃 |
| 作者 | [modusensus](https://github.com/modusensus) | 更新时间 | 2026-08-21 |
| 子分类 | 🧠 记忆系统 | 能力 | memory |

## 一句话介绍

> 记忆主权归用户的本地跨会话记忆：SQLite + 可人工编辑的 Markdown 镜像，autoDream 后台巩固。

## 详细介绍

`dsh-mneme` 是一个 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness) 插件，为 Agent 提供持久的跨会话记忆能力。**Mneme**（Μνήμη）——希腊记忆女神 Mnemosyne 之名，掌管记忆与梦境，正如 autoDream 在后台巩固记忆。

## ✨ 核心特性

- **跨会话记忆** — 对话中 AI 自动记录关键信息，新会话自动注入相关记忆
- **自动整理** — 后台自动去重、合并、归档，记忆库越用越精炼
- **删对话 ≠ 删记忆** — 删除聊天窗口不会丢掉已保存的记忆（可配置）
- **你的数据你做主** — 所有记忆以 Markdown 格式存于本地，随时打开查看和编辑
- **完全离线** — 默认无需 API Key，所有处理在本地完成

## 📦 安装

```bash
# 安装插件（自动注册 bundle 层）
dsh plugin --profile web add @modusensus/dsh-mneme
dsh web
```

## 🚀 快速开始

```bash
🧬 基因（v0.3.0）→ 🛡️ 审计加固（v0.3.6–0.3.9）→ 💤 睡眠维护（v0.4.0）→ 🕸️ 召回融合与图谱（v0.5.0）→ ✨ 面板增强（v0.6.x）→ 🌡️ 自进化记忆（v0.7.0）→ 🕸️ 图谱增强（v0.8.0）
```

## 📚 更多信息

**安装插件（自动注册 bundle 层）**

dsh plugin --profile web add @modusensus/dsh-mneme dsh web > 需要 Node 24+（`node:sqlite`）。完整安装 / 配置 / 架构见 [插件文档](dsh-mneme/README.md)。

**🗺️ 路线图**

🧬 基因（v0.3.0）→ 🛡️ 审计加固（v0.3.6–0.3.9）→ 💤 睡眠维护（v0.4.0）→ 🕸️ 召回融合与图谱（v0.5.0）→ ✨ 面板增强（v0.6.x）→ 🌡️ 自进化记忆（v0.7.0）→ 🕸️ 图谱增强（v0.8.0）

**Install**

dsh plugin --profile web add @modusensus/dsh-mneme dsh web > Requires Node 24+ (`node:sqlite`). Full install / config / architecture docs in the [plugin README](dsh-mneme/README.md).

**Quick Config (Optional)**

Works out of the box. Enable these as needed: > Change in DSH Settings Panel → Memory Settings. Full config docs [here](dsh-mneme/docs/CONFIG.md).

## 🔗 链接

- [GitHub 仓库](https://github.com/modusensus/dsh-mneme)
- [完整 README](https://github.com/modusensus/dsh-mneme#readme)
- [返回dsh-mneme所在分类](../plugins.md)
