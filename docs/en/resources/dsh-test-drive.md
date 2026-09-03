---
title: "dsh-test-drive"
description: "Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a repo or npm package into a throwaway DSH_HOME profile, verifies the bundle patch layer and boot logs, records a structured pass/fail result matrix (JSON/Markdown) for scoring pipelines, and quarantines every temp directory it owns"
keywords: "dsh-test-drive, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-test-drive

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [PerryLink](https://github.com/PerryLink) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a repo or npm package into a throwaway DSH_HOME profile, verifies the bundle patch layer and boot logs, records a structured pass/fail result matrix (JSON/Markdown) for scoring pipelines, and quarantines every temp directory it owns

## About

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-test-drive` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Isolated install-and-smoke test drives for DeepSeek Harness plugins.** *Install, smoke, verify, and clean up in a throwaway profile — your real `~/.dsh` stays untouched.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-test-drive` (counts toward the [deepseek1024.com](https://deepseek10

## 📦 Install

```bash
dsh plugin --profile web add github:PerryLink/dsh-test-drive#<commit-sha>
```

## 🚀 Quick Start

```bash
allowBuilds:
  'dsh-test-drive': true
```

## 📚 Learn more

**Install & uninstall**

dsh plugin --profile web add dsh-test-drive # install (npm) — or the git form above dsh plugin --profile web remove dsh-test-drive # uninstall

## 🔗 Links

- [GitHub Repository](https://github.com/PerryLink/dsh-test-drive)
- [Full README](https://github.com/PerryLink/dsh-test-drive#readme)
- [Back to the Plugins list](../plugins.md)
