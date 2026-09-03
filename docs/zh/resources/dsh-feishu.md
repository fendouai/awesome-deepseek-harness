---
title: "dsh-feishu"
description: "The Feishu UI for DeepSeek Harness  — a panel-driven control console: every slash command a button on the ⚙️ control-panel card, in-card approvals & questions, live streaming cards, one-QR setup. | DeepSeek Harness 的飞书 UI：面板驱动控制台——每个命令都是卡片按钮，卡内审批与提问，流式卡片，扫码一键配置。"
keywords: "dsh-feishu, channel, integration, coding, ui, deepseek harness, dsh"
---
# dsh-feishu

> ⭐ **26** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 26 | 状态 | ✅ 活跃 |
| 作者 | [PGZXB](https://github.com/PGZXB) | 更新时间 | — |

## 一句话介绍

> The Feishu UI for DeepSeek Harness  — a panel-driven control console: every slash command a button on the ⚙️ control-panel card, in-card approvals & questions, live streaming cards, one-QR setup. | DeepSeek Harness 的飞书 UI：面板驱动控制台——每个命令都是卡片按钮，卡内审批与提问，流式卡片，扫码一键配置。

## 详细介绍

The Feishu UI for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) — a dsh-native plugin with a **panel-driven control console**: every slash command is a button on the ⚙️ control-panel card, approvals and questions resolve inside the chat, and one QR scan sets the whole app up. https://github.com/user-attachments/assets/e9163793-52f2-4e2c-a08a-22b27372be61 *2.5-min demo: control panel, streaming card, approval and question.*

## ✨ 核心特性

- **Live streaming cards** — tool calls, reasoning, markdown, and tables stream in as the agent works.
- **One-tap control panel** — `/panel` renders the full command palette as buttons; no command syntax to remember, and each button is the exact equivalent of typi
- **In-card approvals & questions** — approve a permission escalation or answer the agent's questions in the chat.
- **Sessions survive restarts** — a chat's session (and its working directory) is persisted across daemon restarts.
- **Groups & mentions** — @-mention the bot; error notices, approvals, and questions @ the requester.
- **Reactions, allowlists, reminders, export, diagnostics** — reaction ack, `allowedChats` / `allowedUsers`, scheduled reminders, session-log files, and a status 

## 📦 安装

```bash
# remove the plugin from the profile
npx @deepseek-ai/dsh plugin --profile feishu remove @dsh-feishu/dsh-feishu

# optional — full clean slate: delete the profile and its surface data
# (paths shown for the default dsh home, ~/.dsh)
rm -rf ~/.dsh/profiles/feishu ~/.dsh/feishu
```

## 📚 更多信息

**4. one QR scan — create + configure the Feishu app**

npx --yes --package @dsh-feishu/dsh-feishu dsh-feishu-setup --new --profile feishu

**Usage**

A Feishu chat is a dsh session — the bot is the agent's avatar. A typical session goes like this: 1. **Start a chat.** Direct-message the bot, or run `/group <name>` to create a group the bot joins. In a group, @-mention the bot (the default policy; a group with just you and the bot also answers plain messages, and the policy is configurable). <p align="center"></p> 2. **Open the control panel.** 

## 🔗 链接

- [GitHub 仓库](https://github.com/PGZXB/dsh-feishu)
- [完整 README](https://github.com/PGZXB/dsh-feishu#readme)
- [返回dsh-feishu所在分类](../integrations.md)
