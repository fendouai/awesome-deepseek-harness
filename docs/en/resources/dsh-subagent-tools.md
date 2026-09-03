---
title: "dsh-subagent-tools"
description: "Per-call model/provider/persona/toolFilter overrides for subagent delegation with @preset references."
keywords: "dsh-subagent-tools, multi-agent, agent, deepseek harness, dsh"
---
# dsh-subagent-tools

> ⭐ **2** · ✅ active · agent

| | | | |
|---|---|---|---|
| Type | agent | Category | Multi-agent |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [lynx-gt](https://github.com/lynx-gt) | Updated | 2026-08-14 |

## One-liner

> Per-call model/provider/persona/toolFilter overrides for subagent delegation with @preset references.

## About

Enhanced subagent delegation tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh): **per-call model / provider / persona / toolFilter overrides**, **`@preset:` persona references**, and **`provider/model` composite model ids** — shipped as a standard **bundle** that patches **no official package file**.

## 📦 Install

```bash
dsh plugin --profile web add dsh-subagent-tools          # npm
# or: dsh plugin --profile web add github:lynx-gt/dsh-subagent-tools#main
# or: dsh plugin --profile web add ./dsh-subagent-tools  # local checkout
```

## 🚀 Quick Start

```bash
powershell -ExecutionPolicy Bypass -File install-preset.ps1   # Windows
# or: ./install-preset.sh                                     # POSIX
```

## 📚 Learn more

**or: ./install-preset.sh                                     **

It copies the `standard` preset into `$DSH_HOME/.agent-presets/standard-plus`, rewrites its `tool-subagent` / `tool-subagent-fork` rows to point at this package, and switches the default preset. Then **restart `dsh web` and start a NEW session** (presets are read at session creation and cannot be switched in a live session). To revert: pick `standard` again in the UI (General > Agent preset) and d

**Example**

Delegate a task to a subagent using model kimi-code/k3 with the reviewer persona: subagent(description="Review the translation", prompt="...", model="kimi-code/k3", persona="@preset:审校员")

## 🔗 Links

- [GitHub Repository](https://github.com/lynx-gt/dsh-subagent-tools)
- [Full README](https://github.com/lynx-gt/dsh-subagent-tools#readme)
- [Back to the Agents & Multi-Agent list](../agents.md)
