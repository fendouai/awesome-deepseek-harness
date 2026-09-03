---
title: "dsh-session-hub"
description: "Aggregate and natively control multiple remote DeepSeek Harness (DSH) servers' sessions from one official Web UI — hub gateway + official-UI bridge. 多服务器 DSH 会话聚合与原生操控"
keywords: "dsh-session-hub, developer, integration, coding, ui, deepseek harness, dsh"
---
# dsh-session-hub

> ⭐ **4** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [Asaiuta](https://github.com/Asaiuta) | Updated | — |

## One-liner

> Aggregate and natively control multiple remote DeepSeek Harness (DSH) servers' sessions from one official Web UI — hub gateway + official-UI bridge. 多服务器 DSH 会话聚合与原生操控

## About

**把散在各处的会话收进 DSH 的同一棵树。** 远端服务器上的 DSH 会话，本机 Codex CLI、Claude Code、opencode、Pi 的历史对话， 一起进官方 Web UI。侧边栏和对话区都用官方的，插件只搬数据。两件事互相独立，可以只装一件。

## 📦 Install

```bash
dsh plugin --profile web add dsh-session-hub@alpha
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add https://github.com/Asaiuta/dsh-session-hub/archive/refs/tags/v0.1.0-alpha.2.tar.gz
```

## 📚 Learn more

**安装**

dsh plugin --profile web add dsh-session-hub@alpha 装完重启 `dsh web`（`kill -TERM <pid>` 并等待退出，别用 `kill -9`，会在写入中途撕裂会话 zstd 日志），刷新页面。 **设置 → 插件** 里出现 **会话枢纽** 标签页即成功。 `dsh plugin` 把参数原样转发给 profile 目录里的 pnpm（本机需要 pnpm）。当前只有 alpha 版，`@alpha` 与不带标签装到的是同一个版本。 <details> <summary><b>不走 npm：直接装 GitHub tarball</b></summary> dsh plugin --profile web add https://github.com/Asaiuta/dsh-session-hub/archive/refs/t

## 🔗 Links

- [GitHub Repository](https://github.com/Asaiuta/dsh-session-hub)
- [Full README](https://github.com/Asaiuta/dsh-session-hub#readme)
- [Back to the MCP & Integrations list](../integrations.md)
