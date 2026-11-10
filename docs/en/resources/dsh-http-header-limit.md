---
title: "dsh-http-header-limit"
description: "DeepSeek Harness (DSH) desktop startup crash fix. Accumulated dsh-auth-* cookies overflow Node's 16 KB request-header limit, so startup fails with HTTP 431 and \"desktop welcome: Web authentication failed\". This plugin raises maxHeaderSize to 256 KB. 修复 DSH 桌面版重启多次后启动崩溃。"
keywords: "dsh-http-header-limit, desktop, client, coding, deepseek harness, dsh"
---
# dsh-http-header-limit

> ⭐ **1** · ✅ active · client

| | | | |
|---|---|---|---|
| Type | client | Category | Desktop |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [divelife](https://github.com/divelife) | Updated | — |

## One-liner

> DeepSeek Harness (DSH) desktop startup crash fix. Accumulated dsh-auth-* cookies overflow Node's 16 KB request-header limit, so startup fails with HTTP 431 and "desktop welcome: Web authentication failed". This plugin raises maxHeaderSize to 256 KB. 修复 DSH 桌面版重启多次后启动崩溃。

## About

DeepSeek Harness (DSH) desktop startup crash fix. Accumulated dsh-auth-* cookies overflow Node's 16 KB request-header limit, so startup fails with HTTP 431 and "desktop welcome: Web authentication failed". This plugin raises maxHeaderSize to 256 KB. 修复 DSH 桌面版重启多次后启动崩溃。

## 🔗 Links

- [GitHub Repository](https://github.com/divelife/dsh-http-header-limit)
- [Full README](https://github.com/divelife/dsh-http-header-limit#readme)
- [Back to the Clients (Desktop & TUI) list](../clients.md)
