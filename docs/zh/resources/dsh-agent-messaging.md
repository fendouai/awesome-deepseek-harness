---
title: "dsh-agent-messaging"
description: "跨会话 Agent 互发消息：按名称寻址其他会话。"
keywords: "dsh-agent-messaging, multi-agent, agent, deepseek harness, dsh"
---
# dsh-agent-messaging

> ⭐ **5** · ✅ 活跃 · 智能体 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [happyren](https://github.com/happyren) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 跨会话 Agent 互发消息：按名称寻址其他会话。

## 详细介绍

**Cross-session verification, claims and a decision ledger for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — so two agent sessions don't repeat, contradict or deadlock each other.** Two sessions you started yourself — in the Web UI, in a headless run, in separate worktrees, in separate `dsh` processes — cannot tell each other anything. When one discovers a breaking change the other is about to trip over, you are the transport: you read it in one terminal and retype it in the other. This plugin gives them an address and a mailbox. One session names another and delivers a message into its inbox; the harness schedules it like any other model-facing input. session "payments-api" session "checkout-client" │ │ │ peer_send to: checkout-client │ │ mode: steer │ ├───────────

## 📦 安装

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-agent-messaging
```

## 🚀 快速开始

```bash
npx dsh-agent-messaging doctor
```

## 📚 更多信息

**Install**

npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-agent-messaging Restart the profile, then check the install from inside or outside a session: npx dsh-agent-messaging doctor OK node v24.13.1 OK build host and browser bundles present OK state-root /Users/you/.dsh/agent-messaging (writable) OK presence 2 live hosts, 0 stale records OK socket-permissions owner-only (0600) OK accounting record

**Configuration**

Override in your profile's `cordis.patch.yml`: config: inbound: accept spoolOffline: true To stop receiving entirely, set `inbound: refuse`. To stop sending, deny the tools in your permission rules.

## 🔗 链接

- [GitHub 仓库](https://github.com/happyren/dsh-agent-messaging)
- [完整 README](https://github.com/happyren/dsh-agent-messaging#readme)
- [返回dsh-agent-messaging所在分类](../agents.md)
