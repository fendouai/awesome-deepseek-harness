---
title: "dsh-cookie-guard"
description: "修复 DeepSeek Harness 桌面端（Windows）每次启动都会新增一条 dsh-auth-* 登录 Cookie、从不清理，攒到约 70 条后 Cookie 请求头超过 16KB 被回 431（Web authentication failed）打不开的问题。插件在 DSH 启动时挂一个后台清理器，DSH 退出即清掉上一轮及更早的 Cookie；只删 dsh-auth-*，其他 Cookie 不动。"
keywords: "dsh-cookie-guard, desktop, client, coding, deepseek harness, dsh"
---
# dsh-cookie-guard

> ⭐ **1** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [M0Yun](https://github.com/M0Yun) | 更新时间 | — |

## 一句话介绍

> 修复 DeepSeek Harness 桌面端（Windows）每次启动都会新增一条 dsh-auth-* 登录 Cookie、从不清理，攒到约 70 条后 Cookie 请求头超过 16KB 被回 431（Web authentication failed）打不开的问题。插件在 DSH 启动时挂一个后台清理器，DSH 退出即清掉上一轮及更早的 Cookie；只删 dsh-auth-*，其他 Cookie 不动。

## 详细介绍

修复 DeepSeek Harness 桌面端（Windows）每次启动都会新增一条 dsh-auth-* 登录 Cookie、从不清理，攒到约 70 条后 Cookie 请求头超过 16KB 被回 431（Web authentication failed）打不开的问题。插件在 DSH 启动时挂一个后台清理器，DSH 退出即清掉上一轮及更早的 Cookie；只删 dsh-auth-*，其他 Cookie 不动。

## 🔗 链接

- [GitHub 仓库](https://github.com/M0Yun/dsh-cookie-guard)
- [完整 README](https://github.com/M0Yun/dsh-cookie-guard#readme)
- [返回dsh-cookie-guard所在分类](../clients.md)
