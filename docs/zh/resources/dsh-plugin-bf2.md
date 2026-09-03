---
title: "dsh-plugin"
description: "OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend."
keywords: "dsh-plugin, vision, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-plugin

> ⭐ **14** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 14 | 状态 | ✅ 活跃 |
| 作者 | [loongsuite](https://github.com/loongsuite) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, multi-agent |

## 一句话介绍

> OpenTelemetry tracing for DeepSeek Harness (dsh): turns each agent turn into a GenAI span tree — steps, LLM calls with TTFT, tool executions, token usage — exported over standard OTLP to Jaeger, Grafana Tempo, SigNoz, Langfuse, or any compatible backend.

## 详细介绍

`@loongsuite/dsh-plugin` is a standalone, open-source observability plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). It observes DSH's native session, agent loop, LLM stream, and tool lifecycle, converts them into OpenTelemetry GenAI traces and metrics, and exports standard OTLP/HTTP protobuf to any compatible backend. LoongSuite is an open-source observability collection ecosystem built on OpenTelemetry. This repository is its native DSH integration. The plugin does **not** depend on or require LoongSuite Pilot, a sidecar, a local JSONL tap, or any particular vendor's backend. One DSH turn exported over OTLP into self-hosted Langfuse: four react steps, per-call latency and token counts, a failed web_search followed by bash fallbacks, and the ENTRY sp

## 📦 安装

```bash
dsh plugin --profile web add @loongsuite/dsh-plugin
dsh plugin --profile headless add @loongsuite/dsh-plugin
```

## 🚀 快速开始

```bash
dsh plugin --profile web add /absolute/path/to/dsh-plugin
```

## 📚 更多信息

**Install and run**

If you have no OTLP backend yet, [`examples/quickstart`](examples/quickstart/README.md) starts a local Jaeger backend and gets you a trace in three commands. Add the plugin to every DSH profile you want to observe: dsh plugin --profile web add @loongsuite/dsh-plugin dsh plugin --profile headless add @loongsuite/dsh-plugin For local development, replace the package name with the checkout path: dsh 

**Configure the plugin**

Environment variables are enough for most deployments. You can also edit the plugin row in `$DSH_HOME/profiles/<profile>/cordis.patch.yml` (by default under `~/.dsh`): config: endpoint: http://localhost:4318 serviceName: dsh-agent headers: authorization: Bearer your-token resourceAttributes: deployment.environment.name: development captureContent: false exportMetrics: true Explicit plugin settings

## 🔗 链接

- [GitHub 仓库](https://github.com/loongsuite/dsh-plugin)
- [完整 README](https://github.com/loongsuite/dsh-plugin#readme)
- [返回dsh-plugin所在分类](../plugins.md)
