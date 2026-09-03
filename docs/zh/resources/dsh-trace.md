---
title: "dsh-trace"
description: "DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP."
keywords: "dsh-trace, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-trace

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [vibeinging](https://github.com/vibeinging) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP.

## 详细介绍

`dsh-trace` stores DeepSeek Harness session telemetry in a local embedded yiTrace database. It observes records after the host's `telemetry/record` waterfall, projects each DSH turn into one yiTrace trace, and writes SDK-native start, log, and end events through yiTrace's Node-API database. No HTTP server, port, or token is required. The plugin is opt-in, adds no model-visible context, and lives outside the DeepSeek Harness monorepo.

## ✨ 核心特性

- **Embedded local storage** — writes directly through `@yitrace/db`; no HTTP service, port, or access token.
- **Complete agent trace tree** — records one root trace per DSH turn, model-step spans below it, and tool-call spans below each step.
- **Debugging context** — keeps model identity, token usage, message and tool input/output, error state, and generic in-turn log events.
- **Lifecycle recovery** — marks traces that begin mid-turn, closes unfinished spans as failed, flushes on natural boundaries, and recovers committed data when th
- **Local queries** — supports yiTrace trace, span, full-text search, and aggregate APIs against the configured directory.

## 📦 安装

```bash
dsh plugin --profile web add -w github:dsh-external/dsh-trace#<reviewed-commit>
```

## 🚀 快速开始

```bash
dsh --profile web --dump-config
dsh --profile web
```

## 📚 更多信息

**Quick start**

The bundle disables the shipped OTLP telemetry backend and replaces it with local embedded yiTrace. It can store user and assistant text, reasoning, tool arguments and results, session ids, and configured identities. Do not boot the profile until its local retention and redaction policy is acceptable. 1. Choose an absolute local data directory: export DSH_TRACE_DATA_DIR=/absolute/path/to/dsh-trace

**Configuration reference**

An empty data directory, invalid unsigned 64-bit tenant id, invalid node id, or non-positive size/deadline fails at plugin load. The telemetry seam admits one backend per Cordis context. Loading this package together with `session-telemetry-otel` fails as a duplicate service instead of recording twice. A host-level privacy switch must disable every configured telemetry row; the plugin does not byp

## 🔗 链接

- [GitHub 仓库](https://github.com/vibeinging/dsh-trace)
- [完整 README](https://github.com/vibeinging/dsh-trace#readme)
- [返回dsh-trace所在分类](../plugins.md)
