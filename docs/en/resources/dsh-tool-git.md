---
title: "dsh-tool-git"
description: "Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard."
keywords: "dsh-tool-git, developer, plugin, git, coding, deepseek harness, dsh"
---
# dsh-tool-git

> ⭐ 3 · ✅ active · plugin

## One-liner

Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard.

## About

Structured, safe Git tool family for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). Coding agents reach for git constantly, but the stock runtime only offers raw `bash`. `dsh-tool-git` gives the model eight structured tools that run `git` through a shell-free subprocess runner and return canonical JSON values — plus a `tools/pre-execute` safety gate that stops destructive git operations (force push, hard reset, rebase, amend, branch deletion, …) before they happen, 

## Author
**[lxj808624](https://github.com/lxj808624)**

## Links

- [GitHub Repository](https://github.com/lxj808624/dsh-tool-git)
- [Full README](https://github.com/lxj808624/dsh-tool-git#readme)
- [Back to the Plugins list](../plugins.md)
