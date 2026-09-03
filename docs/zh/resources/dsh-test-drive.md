---
title: "dsh-test-drive"
description: "Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a repo or npm package into a throwaway DSH_HOME profile, verifies the bundle patch layer and boot logs, records a structured pass/fail result matrix (JSON/Markdown) for scoring pipelines, and quarantines every temp directory it owns"
keywords: "dsh-test-drive, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-test-drive

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Isolated install-and-smoke test drives for DeepSeek Harness plugins: installs a repo or npm package into a throwaway DSH_HOME profile, verifies the bundle patch layer and boot logs, records a structured pass/fail result matrix (JSON/Markdown) for scoring pipelines, and quarantines every temp directory it owns

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-test-drive` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Isolated install-and-smoke test drives for DeepSeek Harness plugins.** *Install, smoke, verify, and clean up in a throwaway profile — your real `~/.dsh` stays untouched.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-test-drive` (counts toward the [deepseek1024.com](https://deepseek10

## 📦 安装

```bash
dsh plugin --profile web add github:PerryLink/dsh-test-drive#<commit-sha>
```

## 🚀 快速开始

```bash
allowBuilds:
  'dsh-test-drive': true
```

## 📚 更多信息

**Install & uninstall**

dsh plugin --profile web add dsh-test-drive # install (npm) — or the git form above dsh plugin --profile web remove dsh-test-drive # uninstall

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-test-drive)
- [完整 README](https://github.com/PerryLink/dsh-test-drive#readme)
- [返回dsh-test-drive所在分类](../plugins.md)
