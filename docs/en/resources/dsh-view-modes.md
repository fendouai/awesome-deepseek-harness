---
title: "dsh-view-modes"
description: "Output modes with Verbose, Normal and Summary views plus semantic grouping for tool calls and thinking."
keywords: "dsh-view-modes, ui, plugin, deepseek harness, dsh"
---
# dsh-view-modes

> ⭐ **2** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [NigelYao](https://github.com/NigelYao) | Updated | 2026-08-13 |

## One-liner

> Output modes with Verbose, Normal and Summary views plus semantic grouping for tool calls and thinking.

## About

**English** · [简体中文](./README.zh-CN.md) Three output modes for DeepSeek Harness (DSH) Web: Verbose, Normal, and Summary. Keep the full trace when debugging, reduce process noise during daily work, or focus on the result. This is an official-style DSH bundle plugin (`dsh.bundle` + `dsh.client`). It changes only browser-side presentation and does not patch DSH core files.

## 📦 Install

```bash
dsh plugin --profile web add git+https://github.com/NigelYao/dsh-view-modes.git
```

## 🚀 Quick Start

```bash
$pluginRoot = Join-Path $env:USERPROFILE ".dsh\local-plugins\dsh-view-modes"
git clone https://github.com/NigelYao/dsh-view-modes.git $pluginRoot
Set-Location $pluginRoot
dsh plugin --profile web add link:$pluginRoot
```

## 📚 Learn more

**Public GitHub install (recommended)**

No npm account is required: dsh plugin --profile web add git+https://github.com/NigelYao/dsh-view-modes.git

## 🔗 Links

- [GitHub Repository](https://github.com/NigelYao/dsh-view-modes)
- [Full README](https://github.com/NigelYao/dsh-view-modes#readme)
- [Back to the Plugins list](../plugins.md)
