---
title: "dsh-click"
description: "跨平台原生桌面控制（Windows 优先）：截图、读屏、点击/输入/滚动/按键、应用列表与启动。"
keywords: "dsh-click, automation, plugin, deepseek harness, dsh"
---
# dsh-click

> ⭐ **4** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 自动化 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [PerryLink](https://github.com/PerryLink) | 更新时间 | — |

## 一句话介绍

> 跨平台原生桌面控制（Windows 优先）：截图、读屏、点击/输入/滚动/按键、应用列表与启动。

## 详细介绍

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-click` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). **Cross-platform native desktop control for DeepSeek Harness — Windows first.** *Look at the screen, then act — every click gated, every action audited.* [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add dsh-click` (counts toward the [deepseek1024.com](https://deepseek1024.co

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-click#main"

# or from npm (published releases)
dsh plugin --profile web add dsh-click

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A2 'id: dsh-click'
```

## 🚀 快速开始

```bash
> Open Notepad, type "hello", then read back what is on screen.
```

## 📚 更多信息

**Install & uninstall**

> If pnpm reports `ERR_PNPM_IGNORED_BUILDS` for this package (esbuild's harmless platform-binary validation), add `allowBuilds: { esbuild: true }` to your `pnpm-workspace.yaml` — the `dsh` CLI prints the exact snippet.

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline. Example override in your profile patch: - id: dsh-click name: dsh-click config: requireApproval: true autoApproveWindows: ['^Notepad'] focusFallback: never

## 🔗 链接

- [GitHub 仓库](https://github.com/PerryLink/dsh-click)
- [完整 README](https://github.com/PerryLink/dsh-click#readme)
- [返回dsh-click所在分类](../plugins.md)
