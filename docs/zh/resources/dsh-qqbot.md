---
title: "dsh-qqbot"
description: "让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件"
keywords: "dsh-qqbot, channel, integration, coding, deepseek harness, dsh"
---
# dsh-qqbot

> ⭐ **70** · ✅ 活跃 · 集成 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 70 | 状态 | ✅ 活跃 |
| 作者 | [tencent-connect](https://github.com/tencent-connect) | 更新时间 | 2026-08-18 |

## 一句话介绍

> 让 QQ 机器人接入 DeepSeek Harness（dsh）的官方插件

## 详细介绍

QQ 用户 → QQ WebSocket → dsh-im-qqbot → ctx.agents → dsh agent loop → LLM ↑ │ └── session/event ──────────┘ (assistant reply → QQ sendMarkdown)

## 📦 安装

```bash
# 安装到 profile
npx @deepseek-ai/dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot

# 启动
npx @deepseek-ai/dsh --profile qqbot
```

## 🚀 快速开始

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

## 🔗 链接

- [GitHub 仓库](https://github.com/tencent-connect/dsh-qqbot)
- [完整 README](https://github.com/tencent-connect/dsh-qqbot#readme)
- [返回dsh-qqbot所在分类](../integrations.md)
