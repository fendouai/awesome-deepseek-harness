---
title: "dsh-plugin-template"
description: "Minimal, verified template for DeepSeek Harness plugins: bundle manifest, one tool, runtime peer guard, tests, and CI that really invokes the tool (dsh 0.1.0-rc.6)."
keywords: "dsh-plugin-template, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-template

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [zoahdev](https://github.com/zoahdev) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Minimal, verified template for DeepSeek Harness plugins: bundle manifest, one tool, runtime peer guard, tests, and CI that really invokes the tool (dsh 0.1.0-rc.6).

## 详细介绍

A complete dual-side [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) plugin template. It demonstrates the full plugin surface — a **host** plugin exposing a Typert Remote, and a **client** plugin mounting that Remote into a React view — with type-checking, linting, unit tests, CI, and publishing metadata wired up. Out of the box it registers a `greet` Remote: the host composes `"Hello, "` from a configurable prefix, and the client renders the result in a new "Greet" tab.

## ✨ 核心特性

- Node.js `>= 22.19` (or `>= 24`)
- pnpm `>= 9`
- DeepSeek Harness `>=0.1.0-rc.6`

## 📦 安装

```bash
pnpm install
pnpm run build
dsh plugin --profile web add .
```

## 🚀 快速开始

```bash
dsh plugin --profile web remove dsh-plugin-template
```

## 📚 更多信息

**Install from a local checkout**

pnpm install pnpm run build dsh plugin --profile web add . Restart the Web Harness after rebuilding the plugin. A "Greet" tab appears in the session view ring showing `Hello, DSH`. Remove it with: dsh plugin --profile web remove dsh-plugin-template

**Install from Git**

dsh plugin --profile web add github:you/dsh-plugin-template A Git install fetches sources, not built artifacts, so pnpm runs the `prepare` script to build `lib/`. pnpm ≥10 blocks that build until you allow it; on the first failed `add`, `dsh` prints the fix — copy the package key it shows into the profile's `pnpm-workspace.yaml`: allowBuilds: dsh-plugin-template: true then re-run the `add`. That a

## 🔗 链接

- [GitHub 仓库](https://github.com/zoahdev/dsh-plugin-template)
- [完整 README](https://github.com/zoahdev/dsh-plugin-template#readme)
- [返回dsh-plugin-template所在分类](../plugins.md)
