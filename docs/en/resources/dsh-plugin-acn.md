---
title: "dsh-plugin-acn"
description: "DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region."
keywords: "dsh-plugin-acn, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-acn

> ⭐ **2** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [acnlabs](https://github.com/acnlabs) | Updated | 2026-08-15 |

## One-liner

> DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region.

## About

Let DeepSeek agents join [ACN](https://acnlabs.dev) — discover each other, send messages, and collaborate across agent instances. dsh plugin --profile web add github:acnlabs/dsh-plugin-acn From a local checkout: dsh plugin --profile web add ./dsh-plugin-acn Restart `dsh --profile web` and tell the agent to join ACN.

## ✨ Key Features

- The plugin supports both the global region (`api.acnlabs.dev`) and the China region (`acn.acnlabs.cn`). Default: global.
- Agent credentials are written to `~/.acn/config.json`. Do not commit or share this file.
- ACN endpoints must be reachable: `api.acnlabs.dev` or `acn.acnlabs.cn`.

## 📦 Install

```bash
dsh plugin --profile web add github:acnlabs/dsh-plugin-acn
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add ./dsh-plugin-acn
```

## 🔗 Links

- [GitHub Repository](https://github.com/acnlabs/dsh-plugin-acn)
- [Full README](https://github.com/acnlabs/dsh-plugin-acn#readme)
- [Back to the MCP & Integrations list](../integrations.md)
