---
title: "dsh-trace"
description: "DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP."
keywords: "dsh-trace, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-trace

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [vibeinging](https://github.com/vibeinging) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> DeepSeek Harness telemetry backend that exports turns, model steps, and tool calls to yiTrace over HTTP.

## About

`dsh-trace` stores DeepSeek Harness session telemetry in a local embedded yiTrace database. It observes records after the host's `telemetry/record` waterfall, projects each DSH turn into one yiTrace trace, and writes SDK-native start, log, and end events through yiTrace's Node-API database. No HTTP server, port, or token is required. The plugin is opt-in, adds no model-visible context, and lives outside the DeepSeek Harness monorepo.

## ✨ Key Features

- **Embedded local storage** — writes directly through `@yitrace/db`; no HTTP service, port, or access token.
- **Complete agent trace tree** — records one root trace per DSH turn, model-step spans below it, and tool-call spans below each step.
- **Debugging context** — keeps model identity, token usage, message and tool input/output, error state, and generic in-turn log events.
- **Lifecycle recovery** — marks traces that begin mid-turn, closes unfinished spans as failed, flushes on natural boundaries, and recovers committed data when th
- **Local queries** — supports yiTrace trace, span, full-text search, and aggregate APIs against the configured directory.

## 📦 Install

```bash
dsh plugin --profile web add -w github:dsh-external/dsh-trace#<reviewed-commit>
```

## 🚀 Quick Start

```bash
dsh --profile web --dump-config
dsh --profile web
```

## 📚 Learn more

**Quick start**

The bundle disables the shipped OTLP telemetry backend and replaces it with local embedded yiTrace. It can store user and assistant text, reasoning, tool arguments and results, session ids, and configured identities. Do not boot the profile until its local retention and redaction policy is acceptable. 1. Choose an absolute local data directory: export DSH_TRACE_DATA_DIR=/absolute/path/to/dsh-trace

**Configuration reference**

An empty data directory, invalid unsigned 64-bit tenant id, invalid node id, or non-positive size/deadline fails at plugin load. The telemetry seam admits one backend per Cordis context. Loading this package together with `session-telemetry-otel` fails as a duplicate service instead of recording twice. A host-level privacy switch must disable every configured telemetry row; the plugin does not byp

## 🔗 Links

- [GitHub Repository](https://github.com/vibeinging/dsh-trace)
- [Full README](https://github.com/vibeinging/dsh-trace#readme)
- [Back to the Plugins list](../plugins.md)
