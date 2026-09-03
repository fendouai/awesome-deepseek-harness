---
title: "dsh-plugin"
description: "OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend."
keywords: "dsh-plugin, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin

> ⭐ **14** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 14 | Status | ✅ active |
| Author | [loongsuite](https://github.com/loongsuite) | Updated | 2026-08-17 |
| Subcategory | 👁️ Vision tools | Capabilities | coding, multi-agent |

## One-liner

> OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend.

## About

`@loongsuite/dsh-plugin` is a standalone, open-source observability plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It observes DSH's native session, agent loop, LLM stream, and tool lifecycle, converts them into OpenTelemetry GenAI traces and metrics, and exports standard OTLP/HTTP protobuf to any compatible backend. LoongSuite is an open-source observability collection ecosystem built on OpenTelemetry. This repository is its native DSH integration. The plugin does **not** depend on or require LoongSuite Pilot, a sidecar, a local JSONL tap, or any particular vendor's backend. One DSH turn exported over OTLP into self-hosted Langfuse: four react steps, per-call latency and token counts, a failed web_search followed by bash fallbacks, and the ENTRY sp

## 📦 Install

```bash
dsh plugin --profile web add @loongsuite/dsh-plugin
dsh plugin --profile headless add @loongsuite/dsh-plugin
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add /absolute/path/to/dsh-plugin
```

## 📚 Learn more

**Install and run**

If you have no OTLP backend yet, [`examples/quickstart`](examples/quickstart/README.md) starts a local Jaeger backend and gets you a trace in three commands. Add the plugin to every DSH profile you want to observe: dsh plugin --profile web add @loongsuite/dsh-plugin dsh plugin --profile headless add @loongsuite/dsh-plugin For local development, replace the package name with the checkout path: dsh 

**Configure the plugin**

Environment variables are enough for most deployments. You can also edit the plugin row in `$DSH_HOME/profiles/<profile>/cordis.patch.yml` (by default under `~/.dsh`): config: endpoint: http://localhost:4318 serviceName: dsh-agent headers: authorization: Bearer your-token resourceAttributes: deployment.environment.name: development captureContent: false exportMetrics: true Explicit plugin settings

## 🔗 Links

- [GitHub Repository](https://github.com/loongsuite/dsh-plugin)
- [Full README](https://github.com/loongsuite/dsh-plugin#readme)
- [Back to the Plugins list](../plugins.md)
