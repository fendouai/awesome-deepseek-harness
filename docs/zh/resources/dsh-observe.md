---
title: "dsh-observe"
description: "OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/step/tool/LLM spans, token and cost metrics, sanitized prompt/completion capture, async batching, bounded offline buffering, retry with backoff"
keywords: "dsh-observe, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-observe

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> OpenTelemetry and Langfuse observability exporter for DeepSeek Harness: turn/step/tool/LLM spans, token and cost metrics, sanitized prompt/completion capture, async batching, bounded offline buffering, retry with backoff

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-observe` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **OpenTelemetry and Langfuse observability exporter for DeepSeek Harness.** *Turn session events into OTLP traces and Langfuse observations — sanitized, buffered, off by default.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-observe` (counts toward the [deepseek1024.com](https://deepseek1024.

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-observe#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-observe

# 2. configure a backend in your profile patch (cordis.yml) and restart
dsh --profile web
```

## 🚀 快速开始

```bash
- insert:
    - id: dsh-observe
      name: dsh-observe
      config:
        enabled: true
        otlp:
          endpoint: http://localhost:4318
```

## 📚 更多信息

**2. configure a backend in your profile patch (cordis.yml) an**

dsh --profile web Minimal OTLP configuration (the row ships commented out in `cordis.patch.yml`): - id: dsh-observe name: dsh-observe config: enabled: true otlp: endpoint: http://localhost:4318 Then verify the row mounts: dsh --profile web --dump-config | grep -A2 'id: dsh-observe'

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-observe)
- [完整 README](https://github.com/PerryLink/dsh-observe#readme)
- [返回dsh-observe所在分类](../plugins.md)
