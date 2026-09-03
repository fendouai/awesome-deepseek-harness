---
title: "dsh-slack"
description: "DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents."
keywords: "dsh-slack, channel, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-slack

> ⭐ **4** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [STARDUSTLC666](https://github.com/STARDUSTLC666) | Updated | 2026-08-18 |

## One-liner

> DeepSeek Harness Slack 插件：slack_notify/channels/inbox/reply 四工具，Socket Mode 免公网回调收消息，收件箱队列 + 线程回复，支持自定义 slackApiUrl 对接代理网关；内置假 Slack 服务器做协议级验收测试。· Two-way Slack messaging for DeepSeek Harness agents.

## About

- `slack_notify`：向指定频道（或线程）发送一条 Markdown 文本消息，返回消息 `ts`。 - `slack_channels`：列出机器人当前可见的频道（`conversations.list`，自动沿 `next_cursor` 翻页拉全）。 - `slack_inbox`：读取通过 Socket Mode 收到的消息（内存队列，最多保留 200 条；自动去重，`markRead=true` 原子消费）。 - `slack_reply`：以线程回复形式回复某条收件箱消息（`chat.postMessage` 带 `thread_ts`）。 - WebClient 按 `token + slackApiUrl` 缓存复用，配置变更时自动重建。 - 配置走 `cordis.patch.yml`，令牌支持环境变量回退（`DSH_SLACK_TOKEN` / `DSH_SLACK_APP_TOKEN`）。

## ✨ Key Features

- `slack_notify`：向指定频道（或线程）发送一条 Markdown 文本消息，返回消息 `ts`。
- `slack_channels`：列出机器人当前可见的频道（`conversations.list`，自动沿 `next_cursor` 翻页拉全）。
- `slack_inbox`：读取通过 Socket Mode 收到的消息（内存队列，最多保留 200 条；自动去重，`markRead=true` 原子消费）。
- `slack_reply`：以线程回复形式回复某条收件箱消息（`chat.postMessage` 带 `thread_ts`）。
- WebClient 按 `token + slackApiUrl` 缓存复用，配置变更时自动重建。
- 配置走 `cordis.patch.yml`，令牌支持环境变量回退（`DSH_SLACK_TOKEN` / `DSH_SLACK_APP_TOKEN`）。

## 📦 Install

```bash
dsh plugin --profile web add dsh-slack
```

## 🚀 Quick Start

```bash
# 在启动 dsh 的进程里设置
export DSH_SLACK_TOKEN=xoxb-你的机器人令牌
export DSH_SLACK_APP_TOKEN=xapp-你的App级令牌
```

## 📚 Learn more

**安装**

插件运行在宿主进程内，通过 `dsh plugin` 安装进 profile，重启后生效： dsh plugin --profile web add dsh-slack 安装后重启你的 dsh Web 服务，`slack_notify` / `slack_channels` / `slack_inbox` / `slack_reply` 四个工具即对模型可见。

**配置**

配置在 profile 的 `cordis.patch.yml` 里按 `id: slack` 覆盖本插件的行（覆盖会整体替换该行的 `config`，不会合并）。可用配置项： `*` `token` 在「配置层」可留空，此时回退环境变量；两者都为空时插件照常加载，但调用发消息/列频道/ 回复工具时会返回中文报错。`appToken` 留空则只告警、不崩溃，`slack_inbox` 返回空队列（单向模式）。 **方式一：环境变量（推荐，不写死令牌）**

**覆盖 dsh-slack 的 slack 行配置（整体替换）**

config: token: 'xoxb-你的机器人令牌' appToken: 'xapp-你的App级令牌' defaultChannel: '#general' > 优先级：`config.token` > 环境变量 `DSH_SLACK_TOKEN`；`config.appToken` > 环境变量 > `DSH_SLACK_APP_TOKEN`。

## 🔗 Links

- [GitHub Repository](https://github.com/STARDUSTLC666/dsh-slack)
- [Full README](https://github.com/STARDUSTLC666/dsh-slack#readme)
- [Back to the MCP & Integrations list](../integrations.md)
