---
title: "dsh-observe"
description: "OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/step/tool/LLM spans, token and cost metrics, sanitized prompt/completion capture, async batching, bounded offline buffering, retry with backoff"
keywords: "dsh-observe, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-observe

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/step/tool/LLM spans, token and cost metrics, sanitized prompt/completion capture, async batching, bounded offline buffering, retry with backoff

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-observe` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **OpenTelemetry and Langfuse observability exporter for DeepSeek Harness.** *Turn session events into OTLP traces and Langfuse observations — sanitized, buffered, off by default.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-observe` (counts toward the [deepseek1024.com](https://deepseek1024.

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-observe#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-observe

# 2. configure a backend in your profile patch (cordis.yml) and restart
dsh --profile web
```

## 🚀 Quick Start

```bash
- insert:
    - id: dsh-observe
      name: dsh-observe
      config:
        enabled: true
        otlp:
          endpoint: http://localhost:4318
```

## 📚 Learn more

**2. configure a backend in your profile patch (cordis.yml) an**

dsh --profile web Minimal OTLP configuration (the row ships commented out in `cordis.patch.yml`): - id: dsh-observe name: dsh-observe config: enabled: true otlp: endpoint: http://localhost:4318 Then verify the row mounts: dsh --profile web --dump-config | grep -A2 'id: dsh-observe'

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-observe)
- [Full README](https://github.com/PerryLink/dsh-observe#readme)
- [Back to the Plugins list](../plugins.md)
