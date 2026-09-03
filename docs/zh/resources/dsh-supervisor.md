---
title: "dsh-supervisor"
description: "同运行时跨会话发现与通信。"
keywords: "dsh-supervisor, multi-agent, agent, deepseek harness, dsh"
---
# dsh-supervisor

> ⭐ **1** · ✅ 活跃 · 智能体

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [Wha1eChai](https://github.com/Wha1eChai) | 更新时间 | 2026-08-14 |

## 一句话介绍

> 同运行时跨会话发现与通信。

## 详细介绍

Let live [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Sessions discover, message, and coordinate with each other inside the same running DSH process. - Runs inside the existing `dsh` runtime - Starts no daemon, second agent runtime, or separate network port - Installs as a normal DSH plugin **Current release:** `@wha1echai/dsh-cross-session@0.1.0-rc.1` for DSH `0.1.0-rc.6`. This is an independent community project and is not affiliated with or endorsed by DeepSeek AI. *Composite of two real DSH Session views for readability. The plugin provides the Fleet communication tools, not a split-screen or multi-Session UI.*

## ✨ 核心特性

- Runs inside the existing `dsh` runtime
- Starts no daemon, second agent runtime, or separate network port
- Installs as a normal DSH plugin

## 📦 安装

```bash
dsh plugin --profile web add @wha1echai/dsh-cross-session@0.1.0-rc.1
dsh --profile web --dump-config
```

## 🚀 快速开始

```bash
- id: dsh-cross-session-tools
  name: '@wha1echai/dsh-cross-session/tool'
  config:
    controlMode: message
```

## 📚 更多信息

**1. Install the prerelease**

dsh plugin --profile web add @wha1echai/dsh-cross-session@0.1.0-rc.1 dsh --profile web --dump-config Use an isolated `DSH_HOME` when evaluating the plugin without changing an existing profile. npm requires every package to retain `latest`. Because this is currently the only published version, both `latest` and `next` resolve to `0.1.0-rc.1`; using the exact version or `next` makes the prerelease i

**Roadmap**

Detailed delivered milestones, future layers, and non-goals are maintained in [docs/plan/](docs/plan/README.md).

## 🔗 链接

- [GitHub 仓库](https://github.com/Wha1eChai/dsh-supervisor)
- [完整 README](https://github.com/Wha1eChai/dsh-supervisor#readme)
- [返回dsh-supervisor所在分类](../agents.md)
