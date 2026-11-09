---
title: "dsh-cookie-guard"
description: "修复 DeepSeek Harness 桌面端（Windows）每次启动都会新增一条 dsh-auth-* 登录 Cookie、从不清理，攒到约 70 条后 Cookie 请求头超过 16KB 被回 431（Web authentication failed）打不开的问题。插件在 DSH 启动时挂一个后台清理器，DSH 退出即清掉上一轮及更早的 Cookie；只删 dsh-auth-*，其他 Cookie 不动。"
keywords: "dsh-cookie-guard, desktop, client, coding, deepseek harness, dsh"
---
# dsh-cookie-guard

> ⭐ **1** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [M0Yun](https://github.com/M0Yun) | Updated | — |

## One-liner

> 修复 DeepSeek Harness 桌面端（Windows）每次启动都会新增一条 dsh-auth-* 登录 Cookie、从不清理，攒到约 70 条后 Cookie 请求头超过 16KB 被回 431（Web authentication failed）打不开的问题。插件在 DSH 启动时挂一个后台清理器，DSH 退出即清掉上一轮及更早的 Cookie；只删 dsh-auth-*，其他 Cookie 不动。

## About

修复 DeepSeek Harness 桌面端（Windows）每次启动都会新增一条 dsh-auth-* 登录 Cookie、从不清理，攒到约 70 条后 Cookie 请求头超过 16KB 被回 431（Web authentication failed）打不开的问题。插件在 DSH 启动时挂一个后台清理器，DSH 退出即清掉上一轮及更早的 Cookie；只删 dsh-auth-*，其他 Cookie 不动。

## 🔗 Links

- [GitHub Repository](https://github.com/M0Yun/dsh-cookie-guard)
- [Full README](https://github.com/M0Yun/dsh-cookie-guard#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
