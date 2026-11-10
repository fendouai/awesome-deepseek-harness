---
title: "dsh-http-header-limit"
description: "DeepSeek Harness (DSH) desktop startup crash fix. Accumulated dsh-auth-* cookies overflow Node's 16 KB request-header limit, so startup fails with HTTP 431 and \"desktop welcome: Web authentication failed\". This plugin raises maxHeaderSize to 256 KB. 修复 DSH 桌面版重启多次后启动崩溃。"
keywords: "dsh-http-header-limit, desktop, client, coding, deepseek harness, dsh"
---
# dsh-http-header-limit

> ⭐ **1** · ✅ 活跃 · 客户端

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [divelife](https://github.com/divelife) | 更新时间 | — |

## 一句话介绍

> DeepSeek Harness (DSH) desktop startup crash fix. Accumulated dsh-auth-* cookies overflow Node's 16 KB request-header limit, so startup fails with HTTP 431 and "desktop welcome: Web authentication failed". This plugin raises maxHeaderSize to 256 KB. 修复 DSH 桌面版重启多次后启动崩溃。

## 详细介绍

DeepSeek Harness (DSH) desktop startup crash fix. Accumulated dsh-auth-* cookies overflow Node's 16 KB request-header limit, so startup fails with HTTP 431 and "desktop welcome: Web authentication failed". This plugin raises maxHeaderSize to 256 KB. 修复 DSH 桌面版重启多次后启动崩溃。

## 🔗 链接

- [GitHub 仓库](https://github.com/divelife/dsh-http-header-limit)
- [完整 README](https://github.com/divelife/dsh-http-header-limit#readme)
- [返回dsh-http-header-limit所在分类](../clients.md)
