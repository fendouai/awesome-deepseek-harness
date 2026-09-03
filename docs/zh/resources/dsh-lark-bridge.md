---
title: "dsh-lark-bridge"
description: "A native DeepSeek Harness (dsh) plugin bridging dsh coding agents to Feishu/Lark group chats — one group, one project directory."
keywords: "dsh-lark-bridge, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-lark-bridge

> ⭐ **36** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 36 | 状态 | ✅ 活跃 |
| 作者 | [bihangchi9-creator](https://github.com/bihangchi9-creator) | 更新时间 | — |

## 一句话介绍

> A native DeepSeek Harness (dsh) plugin bridging dsh coding agents to Feishu/Lark group chats — one group, one project directory.

## 详细介绍

A secure, bidirectional Feishu/Lark controller for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). Send a task from a DM, group, or topic. The Bridge runs it in the right Harness Project and Session, updates one native card as work progresses, and routes approvals, questions, files, images, and controls back to the same conversation. Tested with DeepSeek Harness `0.1.0-rc.6`. Harness is still in developer preview.

## ✨ 核心特性

- Start, continue, steer, stop, resume, and inspect Harness Sessions from Lark.
- Map each group to a Project, working directory, model route, access policy, and card preset.
- Map each topic or thread to an isolated Session by default.
- Update one card from running to completed, blocked, cancelled, or failed.
- Approve one tool call or answer structured Agent questions from card buttons.
- Receive text, images, and files. The Agent can send safe workspace files back with `lark_deliver`.

## 📦 安装

```bash
git clone https://github.com/imetn/dsh-lark-bridge.git
cd dsh-lark-bridge
pnpm install --frozen-lockfile
pnpm run check
```

## 🚀 快速开始

```bash
pnpm dlx github:imetn/dsh-lark-bridge setup --project "$PWD"
```

## 📚 更多信息

**Quick start**

Requirements: Node.js 22+, `pnpm`, a working DeepSeek Harness model configuration, and either an installed `dsh` CLI or an official Harness source checkout nearby. Run this from the Project you want the bot to control: pnpm dlx github:imetn/dsh-lark-bridge setup --project "$PWD" The setup command: 1. Opens the official Feishu/Lark authorization page for a new bot app. 2. Requests only the messagin

## 🔗 链接

- [GitHub 仓库](https://github.com/bihangchi9-creator/dsh-lark-bridge)
- [完整 README](https://github.com/bihangchi9-creator/dsh-lark-bridge#readme)
- [返回dsh-lark-bridge所在分类](../integrations.md)
