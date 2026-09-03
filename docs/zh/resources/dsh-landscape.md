---
title: "dsh-landscape"
description: "Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and generate build-ready briefs."
keywords: "dsh-landscape, ui, plugin, coding, multi-agent, deepseek harness, dsh"
---
# dsh-landscape

> ⭐ **7** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 7 | 状态 | ✅ 活跃 |
| 作者 | [cyanseek](https://github.com/cyanseek) | 更新时间 | 2026-08-21 |
| 子分类 | 💡 生成式界面 | 能力 | coding, multi-agent, ui |

## 一句话介绍

> Agent-first DeepSeek Harness plugin intelligence: verify existing plugins, identify missing capabilities, and generate build-ready briefs.

## 详细介绍

[简体中文](README.zh-CN.md) · [Website](https://cyanseek.github.io/dsh-landscape/) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md) DSH Landscape is a read-only capability preflight: describe one change in natural language and get an evidence-backed decision before you install, replace, upgrade, compose, or build. Try needs like: - “Should I install browser automation, or is it already covered?” - “Compare the GitHub integrations that could fit this DSH setup.” - “Can I replace my current search plugin without losing capabilities?” - “Before we build a Linear integration, show what not to duplicate.” No Landscape account. No API key. No initialization. No required configuration. If runtime inspection or live discovery is unavailable, Landscape still uses its bundled snapshot and state

## ✨ 核心特性

- “Should I install browser automation, or is it already covered?”
- “Compare the GitHub integrations that could fit this DSH setup.”
- “Can I replace my current search plugin without losing capabilities?”
- “Before we build a Linear integration, show what not to duplicate.”

## 📦 安装

```bash
dsh plugin --profile web add github:cyanseek/dsh-landscape#2d3570aadbbd291dbfc58e2484e287bd14fa92e0
```

## 🚀 快速开始

```bash
npx -y skills use cyanseek/dsh-landscape --skill dsh-landscape --agent codex
```

## 📚 更多信息

**Quick start**

Install the pinned, reproducible DSH bundle into an existing profile: dsh plugin --profile web add github:cyanseek/dsh-landscape#2d3570aadbbd291dbfc58e2484e287bd14fa92e0 Then ask DSH normally: > Before adding browser automation, check this environment and the ecosystem. Tell me what to use, what not to build, and the safest next action. The native tool is named `dsh_landscape`. Landscape itself ne

## 🔗 链接

- [GitHub 仓库](https://github.com/cyanseek/dsh-landscape)
- [完整 README](https://github.com/cyanseek/dsh-landscape#readme)
- [返回dsh-landscape所在分类](../plugins.md)
