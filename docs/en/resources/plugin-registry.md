---
title: "plugin-registry"
description: "DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill."
keywords: "plugin-registry, registry, awesome-list, workflow, ui, deepseek harness, dsh"
---
# plugin-registry

> ⭐ **57** · ✅ active · awesome-list · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 57 | Status | ✅ active |
| Author | [vlln](https://github.com/vlln) | Updated | 2026-08-19 |

## One-liner

> DSH plugin ecosystem infrastructure: thin console to manage official repository plugins (0 patch) plus the make-dsh-plugin skill.

## About

DeepSeek Harness's official mechanisms define "what a plugin is and how it runs"; this repository adds two things (panel structure: [console README](packages/plugin/console/README.md); guidance: below): 1. **Thin console** (`packages/plugin/console`) — browser panel managing a profile's plugin install state + 4 agent tools 2. **Development spec and guidance** — `make-dsh-plugin` skill + cookbook for creating official bundle/cordis plugins

## 📦 Install

```bash
dsh plugin --profile web add "github:vlln/plugin-registry#path:/packages/plugin/console"
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add @vlln/plugin-console@0.1.0
```

## 📚 Learn more

**Installation**

**Option 1: git source, direct install (recommended, one line)** dsh plugin --profile web add "github:vlln/plugin-registry#path:/packages/plugin/console" Build artifacts are committed (git source skips the build); one command installs directly (~15 s). > **Windows note**: this uses the `#path:` form (no `&`) on purpose — on win32 `dsh plugin` forwards > args through cmd.exe, where `&` is a command

## 🔗 Links

- [GitHub Repository](https://github.com/vlln/plugin-registry)
- [Full README](https://github.com/vlln/plugin-registry#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
