---
title: "dsh-agent-messaging"
description: "Cross-session agent-to-agent messaging: address another session by name."
keywords: "dsh-agent-messaging, multi-agent, agent, deepseek harness, dsh"
---
# dsh-agent-messaging

> ⭐ **5** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [happyren](https://github.com/happyren) | Updated | 2026-08-15 |

## One-liner

> Cross-session agent-to-agent messaging: address another session by name.

## About

**Cross-session verification, claims and a decision ledger for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) — so two agent sessions don't repeat, contradict or deadlock each other.** Two sessions you started yourself — in the Web UI, in a headless run, in separate worktrees, in separate `dsh` processes — cannot tell each other anything. When one discovers a breaking change the other is about to trip over, you are the transport: you read it in one terminal and retype it in the other. This plugin gives them an address and a mailbox. One session names another and delivers a message into its inbox; the harness schedules it like any other model-facing input. session "payments-api" session "checkout-client" │ │ │ peer_send to: checkout-client │ │ mode: steer │ ├───────────

## 📦 Install

```bash
npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-agent-messaging
```

## 🚀 Quick Start

```bash
npx dsh-agent-messaging doctor
```

## 📚 Learn more

**Install**

npx -p @deepseek-ai/dsh dsh plugin --profile web add dsh-agent-messaging Restart the profile, then check the install from inside or outside a session: npx dsh-agent-messaging doctor OK node v24.13.1 OK build host and browser bundles present OK state-root /Users/you/.dsh/agent-messaging (writable) OK presence 2 live hosts, 0 stale records OK socket-permissions owner-only (0600) OK accounting record

**Configuration**

Override in your profile's `cordis.patch.yml`: config: inbound: accept spoolOffline: true To stop receiving entirely, set `inbound: refuse`. To stop sending, deny the tools in your permission rules.

## 🔗 Links

- [GitHub Repository](https://github.com/happyren/dsh-agent-messaging)
- [Full README](https://github.com/happyren/dsh-agent-messaging#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
