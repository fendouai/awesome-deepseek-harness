---
title: "dsh-cross-session"
description: "Same-runtime cross-session discovery and communication for DeepSeek Harness."
keywords: "dsh-cross-session, multi-agent, agent, deepseek harness, dsh"
---
# dsh-cross-session

> ⭐ **1** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [Wha1eChai](https://github.com/Wha1eChai) | Updated | 2026-08-14 |

## One-liner

> Same-runtime cross-session discovery and communication for DeepSeek Harness.

## About

Let live [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) Sessions discover, message, and coordinate with each other inside the same running DSH process. - Runs inside the existing `dsh` runtime - Starts no daemon, second agent runtime, or separate network port - Installs as a normal DSH plugin **Current release:** `@wha1echai/dsh-cross-session@0.1.0-rc.1` for DSH `0.1.0-rc.6`. This is an independent community project and is not affiliated with or endorsed by DeepSeek AI. *Composite of two real DSH Session views for readability. The plugin provides the Fleet communication tools, not a split-screen or multi-Session UI.*

## ✨ Key Features

- Runs inside the existing `dsh` runtime
- Starts no daemon, second agent runtime, or separate network port
- Installs as a normal DSH plugin

## 📦 Install

```bash
dsh plugin --profile web add @wha1echai/dsh-cross-session@0.1.0-rc.1
dsh --profile web --dump-config
```

## 🚀 Quick Start

```bash
- id: dsh-cross-session-tools
  name: '@wha1echai/dsh-cross-session/tool'
  config:
    controlMode: message
```

## 📚 Learn more

**1. Install the prerelease**

dsh plugin --profile web add @wha1echai/dsh-cross-session@0.1.0-rc.1 dsh --profile web --dump-config Use an isolated `DSH_HOME` when evaluating the plugin without changing an existing profile. npm requires every package to retain `latest`. Because this is currently the only published version, both `latest` and `next` resolve to `0.1.0-rc.1`; using the exact version or `next` makes the prerelease i

**Roadmap**

Detailed delivered milestones, future layers, and non-goals are maintained in [docs/plan/](docs/plan/README.md).

## 🔗 Links

- [GitHub Repository](https://github.com/Wha1eChai/dsh-cross-session)
- [Full README](https://github.com/Wha1eChai/dsh-cross-session#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
