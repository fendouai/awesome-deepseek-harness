---
title: "dsh-agent-message"
description: "DeepSeek Harness 跨会话 Agent 通信插件｜Cross-session agent-to-agent messaging with offline delivery, receipts and session navigation for DeepSeek Harness."
keywords: "dsh-agent-message, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-agent-message

> ⭐ **6** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 6 | Status | ✅ active |
| Author | [GengDaPeng](https://github.com/GengDaPeng) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> DeepSeek Harness 跨会话 Agent 通信插件｜Cross-session agent-to-agent messaging with offline delivery, receipts and session navigation for DeepSeek Harness.

## About

在 DeepSeek Harness 里，一个进程会同时挂着多个 Agent 会话。本插件给每个会话装上三个工具，让它们能互相"发消息"： - 发消息前，先**列出所有可发送的独立会话**（未归档、排除真实子代理，含离线未打开的），按标题找到目标； - 找到后，**把消息投递到目标会话**——普通消息统一进入独立的新 turn；目标离线（进程重启后还没打开）时，插件通过 Harness 公开接口恢复会话、投递，并保持加载供后续通信，插件卸载时再释放 handle； - 需要时，可以**按需查询**某条消息的送达状态（排队中/已认领/被丢弃/未知），并单独查看目标是否正在运行，供监督场景使用。 典型场景：编排者 Agent 给开发 Agent 派活、两个 Agent 协作接力、主会话给测试会话发指令、监督者 Agent 盯梢多个 worker。

## ✨ Key Features

- 发消息前，先**列出所有可发送的独立会话**（未归档、排除真实子代理，含离线未打开的），按标题找到目标；
- 找到后，**把消息投递到目标会话**——普通消息统一进入独立的新 turn；目标离线（进程重启后还没打开）时，插件通过 Harness 公开接口恢复会话、投递，并保持加载供后续通信，插件卸载时再释放 handle；
- 需要时，可以**按需查询**某条消息的送达状态（排队中/已认领/被丢弃/未知），并单独查看目标是否正在运行，供监督场景使用。

## 📦 Install

```bash
dsh plugin --profile web add dsh-agent-message
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:GengDaPeng/dsh-agent-message
```

## 📚 Learn more

**发送方导航示例**

当前 relay 消息显示为可见的 Agent 消息卡片；点击消息头即可跳转到发送方会话。持久化来源仍是插件 `relay`，不会伪装成人类输入。完整会话 ID 同时保留在 typed source 和 Host 生成的模型可见协议头中，避免接收 Agent 猜测发送方。

**使用**

1. 在会话 A 的输入框中键入 `@`，从 Harness 原生候选菜单中选择目标会话； 2. Harness 会把该 Session 的有界、只读、不可信快照提供给 A，但不会向 B 发消息或唤醒 B。只有当前请求或用户已授予的编排职责明确要求跨会话传递信息时，A 才调用 `send_agent_message`。例如 `@B 告诉他最后提交 PR draft 就停止` 会发送；`@B 帮我分析他最新的对话结果` 只使用引用快照； 3. 显式要求转告时，A 只负责投递并报告“已接受”或失败，不代为执行被转发的任务，也不要求 B 额外回复“收到”；如果正文明确要求 B 把业务内容返回 A，B 才向 `senderSessionId` 发送消息； 4. 也可以让 Agent 调 `list_peer_agents`，再用完整会话 ID 直接发送； 5. 会话 B 收到的是带 typed r

**原理**

每个 Agent 都有一个收件箱 `Inbox`，里面是两条 FIFO 队列： `send_agent_message` 的投递路径： 会话枚举、批量标题和离线日志读取分别使用 Harness 的 `sessionQuery.listSessions()`、`readTitleSnapshots()` 与 `readSession()`。`SessionId` 是唯一地址；`parentSession` 只记录分叉血缘，只有 `origin: subagent` 才会被识别为真实子代理。插件不直接扫描 `sessionPersistence` 重建另一份会话目录。 `send_agent_message` 成功把原生消息提交给目标 Inbox 后立即返回 `accepted` 和该消息的原生 `messageId`；精简工具结果和完整工具卡片都会显示可选择复制的 `messageId`，完

## 🔗 Links

- [GitHub Repository](https://github.com/GengDaPeng/dsh-agent-message)
- [Full README](https://github.com/GengDaPeng/dsh-agent-message#readme)
- [Back to the Plugins list](../plugins.md)
