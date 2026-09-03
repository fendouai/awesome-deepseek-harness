---
title: "dsh-find-plugin"
description: "Agent-assisted plugin discovery: search the live GitHub dsh-plugin topic from inside DSH."
keywords: "dsh-find-plugin, discovery, plugin, search, workflow, deepseek harness, dsh"
---
# dsh-find-plugin

> ⭐ **73** · ✅ active · plugin · ⬆️ +5 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Plugin discovery |
| Stars | ⭐ 73 | Status | ✅ active |
| Author | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin) | Updated | 2026-08-19 |

## One-liner

> Agent-assisted plugin discovery: search the live GitHub dsh-plugin topic from inside DSH.

## About

**A plugin that finds plugins** — think [`/find-skills`](https://skills.sh) from skills.sh, for DSH. Tell your agent what you want ("notify me on WeChat when a task finishes"), and it searches the DSH plugin ecosystem on GitHub for you — top results by stars, each with a one-line description and an install command.

## 📦 Install

```bash
# from npm (prebuilt, recommended)
dsh plugin --profile web add dsh-find-plugin

# or from GitHub
dsh plugin --profile web add github:awesome-dsh-plugin/dsh-find-plugin
```

## 📚 Learn more

**Usage**

Restart `dsh web` after installing, then just talk to the agent — it calls `find_dsh_plugin` on its own whenever plugin discovery helps: Each result comes back with stars, a description, the repo link, and a ready-to-run `dsh plugin add` command — ask the agent to install one and it can run the command for you.

## 🔗 Links

- [GitHub Repository](https://github.com/awesome-dsh-plugin/dsh-find-plugin)
- [Full README](https://github.com/awesome-dsh-plugin/dsh-find-plugin#readme)
- [Back to the Plugins list](../plugins.md)
