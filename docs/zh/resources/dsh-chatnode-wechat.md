---
title: "dsh-chatnode-wechat"
description: "Chat with, monitor, and approve your DSH agents from WeChat — an iLink gateway + conversation node bundle for DeepSeek Harness"
keywords: "dsh-chatnode-wechat, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-chatnode-wechat

> ⭐ **7** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 渠道 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [Jesse-njx](https://github.com/Jesse-njx) | 更新时间 | — |

## 一句话介绍

> Chat with, monitor, and approve your DSH agents from WeChat — an iLink gateway + conversation node bundle for DeepSeek Harness

## 详细介绍

**Chat with, monitor, and approve your DSH agents from WeChat.** A [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) bundle that connects a DSH profile to a WeChat personal account over Tencent's unofficial **iLink bot gateway** (`ilinkai.weixin.qq.com`) — the same mechanism hermes-agent and OpenClaw use. Text and images go both ways (inbound images are downloaded, decrypted and handed to the agent; `/send` sends an image back), session targeting works with `/sessions /use /new /stop /status`, permission requests are answered with `/yes` / `/no` right in the chat, and progress is reported as digest-style messages instead of a tool-call firehose. 你 (WeChat) ⇄ iLink ⇄ wechat-gateway ⇄ wechat-conversation-node ⇄ DSH agent session The bundle ships **two separable Cordis plugi

## ✨ 核心特性

- **One poller per account.** iLink allows exactly ONE authenticated poller
- **Unofficial gateway.** This rides the same unofficial mechanism as
- **Unofficial protocol.** iLink details are reconstructed from hermes-agent

## 📦 安装

```bash
git clone https://github.com/Jesse-njx/dsh-chatnode-wechat.git
cd dsh-chatnode-wechat
pnpm install && pnpm build
dsh plugin --profile <your-profile> add .
```

## 🚀 快速开始

```bash
pnpm login          # prints a QR URL; scan it with WeChat and confirm
```

## 📚 更多信息

**Install**

git clone https://github.com/Jesse-njx/dsh-chatnode-wechat.git cd dsh-chatnode-wechat pnpm install && pnpm build dsh plugin --profile <your-profile> add . Credentials are stored through the **dsh credentials service** — never in the patch file. Pair your WeChat account once: pnpm login # prints a QR URL; scan it with WeChat and confirm This writes `WEIXIN_ACCOUNT_ID` / `WEIXIN_BOT_TOKEN` / `WEIXIN

**Usage**

Send text or images to the bot. Everything is zero-config once one session exists — the **most recent session** is the default target.

**Roadmap**

commands, approvals, digests, allowlist. directions, outbound voice replies. shared-poller proxy so the bundle can coexist with hermes/openclaw.

## 🔗 链接

- [GitHub 仓库](https://github.com/Jesse-njx/dsh-chatnode-wechat)
- [完整 README](https://github.com/Jesse-njx/dsh-chatnode-wechat#readme)
- [返回dsh-chatnode-wechat所在分类](../integrations.md)
