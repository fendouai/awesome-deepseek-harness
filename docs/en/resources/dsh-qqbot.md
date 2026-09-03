---
title: "dsh-qqbot"
description: "让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件"
keywords: "dsh-qqbot, channel, integration, coding, deepseek harness, dsh"
---
# dsh-qqbot

> ⭐ **70** · ✅ active · integration · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 70 | Status | ✅ active |
| Author | [tencent-connect](https://github.com/tencent-connect) | Updated | 2026-08-18 |

## One-liner

> 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件

## About

QQ 用户 → QQ WebSocket → dsh-im-qqbot → ctx.agents → dsh agent loop → LLM ↑ │ └── session/event ──────────┘ (assistant reply → QQ sendMarkdown)

## 📦 Install

```bash
# 安装到 profile
npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot

# 启动
npx @deepseek-ai/dsh --profile qqbot
```

## 🚀 Quick Start

```bash
# 构建
cd /path/to/dsh-qqbot
pnpm install && pnpm build

# 安装到 profile（本地路径）
npx @deepseek-ai/dsh plugin --profile qqbot add /path/to/dsh-qqbot

# 启动
export QQBOT_APPID="你的AppID" QQBOT_SECRET="你的AppSecret"
npx @deepseek-ai/dsh --profile qqbot
```

## 🔗 Links

- [GitHub Repository](https://github.com/tencent-connect/dsh-qqbot)
- [Full README](https://github.com/tencent-connect/dsh-qqbot#readme)
- [Back to the MCP & Integrations list](../integrations.md)
