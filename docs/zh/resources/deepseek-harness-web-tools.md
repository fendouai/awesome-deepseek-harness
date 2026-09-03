---
title: "DeepSeek-Harness-Web-Tools"
description: "免费免密钥的 web_search/web_fetch，DuckDuckGo 驱动，无需注册。"
keywords: "DeepSeek-Harness-Web-Tools, search, plugin, deepseek harness, dsh"
---
# DeepSeek-Harness-Web-Tools

> ⭐ **17** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 17 | 状态 | ✅ 活跃 |
| 作者 | [tonyd2wild](https://github.com/tonyd2wild) | 更新时间 | 2026-08-13 |
| 子分类 | 🌐 网页搜索 | 能力 | search |

## 一句话介绍

> 免费免密钥的 web_search/web_fetch，DuckDuckGo 驱动，无需注册。

## 详细介绍

**Free, keyless `web_search` and `web_fetch` for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).** Out of the box, `dsh`'s `web_search` requires a paid API key and `web_fetch` ships disabled. If you run `dsh` against a local model, you probably wanted neither of those things. This repo gets you both, for free, with no signup: - **`web_search`** — a local shim backed by DuckDuckGo, plus a `dsh` plugin that registers it with the `ctx.web` seam. - **`web_fetch`** — configuration to enable the provider DeepSeek already publishes. Everything here is upgrade-safe: it lives in your profile patch layer and `$DSH_HOME`, not in shipped package files. ---

## ✨ 核心特性

- **`web_search`** — a local shim backed by DuckDuckGo, plus a `dsh` plugin that registers it with the `ctx.web` seam.
- **`web_fetch`** — configuration to enable the provider DeepSeek already publishes.

## 📦 安装

```bash
plugin/    a dsh plugin registering a DuckDuckGo-backed WebSearchProvider
shim/      a small local HTTP service that queries DuckDuckGo
examples/  a cordis.patch.yml showing the wiring
```

## 🚀 快速开始

```bash
cd shim
python -m venv venv

# Windows
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe server.py

# macOS / Linux
venv/bin/python -m pip install -r requirements.txt
venv/bin/python server.py
```

## 📚 更多信息

**Configuration**

The plugin takes one option: name: 'dsh-plugin-ddg-search' config: baseURL: http://127.0.0.1:8899 The shim takes `--host`, `--port`, and `--verbose`.

## 🔗 链接

- [GitHub 仓库](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools)
- [完整 README](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools#readme)
- [返回DeepSeek-Harness-Web-Tools所在分类](../plugins.md)
