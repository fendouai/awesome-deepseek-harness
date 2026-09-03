---
title: "dsh-surfing-plugin"
description: "SearXNG search and Crawl4AI fetch providers for DeepSeek Harness"
keywords: "dsh-surfing-plugin, search, plugin, coding, deepseek harness, dsh"
---
# dsh-surfing-plugin

> ⭐ **12** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 12 | Status | ✅ active |
| Author | [cyijun](https://github.com/cyijun) | Updated | 2026-08-14 |
| Subcategory | 🌐 Web search | Capabilities | coding, search |

## One-liner

> SearXNG search and Crawl4AI fetch providers for DeepSeek Harness

## About

`dsh-surfing-plugin` adds self-hosted web access to [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness): `web_search` uses SearXNG and `web_fetch` uses Crawl4AI. It registers providers with DSH's `ctx.web` service, so the native tool names, arguments, rendering, timeouts, cancellation, and result limits remain unchanged.

## ✨ Key Features

- Node.js `^22.19.0` or `>=24.0.0`
- DeepSeek Harness `>=0.1.0-rc.6 <0.2.0`
- Reachable SearXNG and Crawl4AI services
- JSON enabled in SearXNG's `search.formats`

## 📦 Install

```bash
dsh plugin --profile web add .
dsh --profile web --dump-config
dsh --profile web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-surfing-plugin
```

## 📚 Learn more

**Architecture**

flowchart LR A[Native DSH web_search] --> B[surfing-searxng provider] B --> C[SearXNG /search] D[Native DSH web_fetch] --> E[surfing-crawl4ai provider] E --> F[Crawl4AI /crawl] The bundled `cordis.patch.yml` mounts this plugin, selects `surfing-searxng` and `surfing-crawl4ai`, and adds a fetch-only native tool consumer. The separate consumer works in both DSH assemblies: headless keeps its host-le

**Quick start**

The endpoint values may be service roots or complete `/search` and `/crawl` URLs: export SEARXNG_URL=http://127.0.0.1:8080 export CRAWL4AI_URL=http://127.0.0.1:11235

**Configuration**

Explicit configuration wins over environment values. Override this plugin's row in `$DSH_HOME/profiles/web/cordis.patch.yml`: config: searxng: url: https://search.example.com apiKeyEnv: MY_SEARXNG_KEY authHeader: X-API-Key authScheme: '' language: en categories: general,news safeSearch: 1 timeRange: month crawl4ai: url: https://crawl.example.com apiKeyEnv: CRAWL4AI_API_TOKEN authHeader: Authorizat

**GitHub installation**

Git installation builds from source through `prepare`. Pin a commit: dsh plugin --profile web add github:cyijun/surfing-plugin#COMMIT_SHA pnpm 10 and newer require build-script approval for Git dependencies. If the first install is blocked, copy its exact package key into the profile's `pnpm-workspace.yaml` and retry: allowBuilds: dsh-surfing-plugin: true npm packages and `pnpm pack` tarballs alre

## 🔗 Links

- [GitHub Repository](https://github.com/cyijun/dsh-surfing-plugin)
- [Full README](https://github.com/cyijun/dsh-surfing-plugin#readme)
- [Back to the Plugins list](../plugins.md)
