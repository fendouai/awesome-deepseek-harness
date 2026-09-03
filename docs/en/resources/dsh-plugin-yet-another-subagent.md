---
title: "dsh-plugin-yet-another-subagent"
description: "Configurable subagent profile system: a single subagent tool with profile parameters, Web UI settings and live progress."
keywords: "dsh-plugin-yet-another-subagent, multi-agent, agent, ui, deepseek harness, dsh"
---
# dsh-plugin-yet-another-subagent

> ⭐ **12** · ✅ active · agent · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-20 |

## One-liner

> Configurable subagent profile system: a single subagent tool with profile parameters, Web UI settings and live progress.

## About

可配置的子代理（subagent）profile 系统，提供单一 `subagent` 工具 + `profile` 参数选择，支持 Web UI 设置、实时进度展示（工具调用/token/活动）、子代理树标签页、点击跳转子会话。

## ✨ Key Features

- **Host 半**（`src/index.ts`）：
- **Client 半**（`src/client/index.ts`）：

## 📦 Install

```bash
pnpm install          # 安装开发依赖 + zod（唯一运行时 npm 依赖）
pnpm run typecheck    # tsc --noEmit（通过 ../dsh 解析 DSH 源码）
pnpm test             # vitest run
pnpm run build        # tsc + tsdown → lib/index.js, lib/invariant.js, lib/client.js
```

## 🚀 Quick Start

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-yet-another-subagent

# 本地引用（开发热更新）
dsh plugin --profile web add "link:D:/Projects/deepseek-harness/yet-another-subagent"
```

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
