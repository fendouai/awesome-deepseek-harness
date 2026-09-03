---
title: "dsh-im-bridge"
description: "DSH 插件：把 DeepSeek Harness 桥接到 IM（v0.1 微信/iLink；钉钉/飞书/Telegram 预留）。turn/approval 推送 + 远程批准/注入，持久去重/收敛分段/合并窗口。"
keywords: "dsh-im-bridge, channel, integration, coding, deepseek harness, dsh"
---
# dsh-im-bridge

> ⭐ **9** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [BiBoyang](https://github.com/BiBoyang) | Updated | — |

## One-liner

> DSH 插件：把 DeepSeek Harness 桥接到 IM（v0.1 微信/iLink；钉钉/飞书/Telegram 预留）。turn/approval 推送 + 远程批准/注入，持久去重/收敛分段/合并窗口。

## About

DSH（DeepSeek Harness）插件：把 DSH 桥接到 IM。v0.1 先落地微信（iLink 通道），架构上通道层（`src/ilink.ts` 协议客户端）与桥接层（`src/index.ts` 事件/批准/注入）分离，后续按同样模式接钉钉、飞书、Telegram。 当前（微信通道）能力：在电脑上跑长任务，离开后用微信远程监控、批准、追加指令。 - DSH → 微信：turn 完成 / 出错 / 被阻塞、批准请求（含工具名与原因）实时推送 - 微信 → DSH：回复文本注入绑定会话；回复「批准 / 拒绝」应答 pending approval；`/bind ` 切换绑定会话 - iLink 扫码登录，单用户白名单，消息去重、长回复分段、`..` / `!!` / 超时合并

## ✨ Key Features

- DSH → 微信：turn 完成 / 出错 / 被阻塞、批准请求（含工具名与原因）实时推送
- 微信 → DSH：回复文本注入绑定会话；回复「批准 / 拒绝」应答 pending approval；`/bind <session>` 切换绑定会话
- iLink 扫码登录，单用户白名单，消息去重、长回复分段、`..` / `!!` / 超时合并

## 📦 Install

```bash
dsh plugin --profile web add <本仓库目录>
# headless profile 需单独安装：
dsh plugin --profile headless add <本仓库目录>
```

## 🚀 Quick Start

```bash
pnpm install
pnpm build     # tsc，产物在 lib/（提交入库，git 安装不跑构建）
pnpm test      # vitest
```

## 📚 Learn more

**使用**

1. 启动 DSH Web 后查看日志获取微信扫码链接，手机扫码完成登录 2. 扫码确认的用户自动成为白名单用户（也可在配置里显式指定 `allowedUserId`） 3. 微信里发消息即注入当前绑定会话；`/bind <session-id>` 切换；`/status` 查看状态 4. agent 请求批准时收到推送，回复「批准」或「拒绝」

## 🔗 Links

- [GitHub Repository](https://github.com/BiBoyang/dsh-im-bridge)
- [Full README](https://github.com/BiBoyang/dsh-im-bridge#readme)
- [Back to the MCP & Integrations list](../integrations.md)
