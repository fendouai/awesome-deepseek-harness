---
title: "dsh-tool-git"
description: "Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard."
keywords: "dsh-tool-git, developer, plugin, git, coding, deepseek harness, dsh"
---
# dsh-tool-git

> ⭐ **4** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 4 | Status | ✅ active |
| Author | [lxj808624](https://github.com/lxj808624) | Updated | 2026-08-16 |
| Subcategory | 🛡️ Security & ops | Capabilities | git, coding |

## One-liner

> Structured safe Git tools: status/diff/log/branch/stage/commit/stash/show with a destructive-command guard.

## About

Structured, safe Git tool family for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). Coding agents reach for git constantly, but the stock runtime only offers raw `bash`. `dsh-tool-git` gives the model eight structured tools that run `git` through a shell-free subprocess runner and return canonical JSON values — plus a `tools/pre-execute` safety gate that stops destructive git operations (force push, hard reset, rebase, amend, branch deletion, …) before they happen, whether the model calls them through these tools **or** through a shell tool. - **No shell injection**: every command goes through `execFile` with an explicit argument array. Model-supplied paths and messages are never string-interpolated. - **Machine output**: porcelain v2, `--numstat`, and `--form

## ✨ Key Features

- **No shell injection**: every command goes through `execFile` with an explicit
- **Machine output**: porcelain v2, `--numstat`, and `--format` records are parsed
- **Safety by default**: destructive operations are denied with an explanation

## 📦 Install

```bash
dsh plugin --profile web add dsh-tool-git
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:lxj808624/dsh-tool-git#v0.1.3
```

## 📚 Learn more

**Install**

**npm (recommended)** — from any directory: dsh plugin --profile web add dsh-tool-git **From GitHub** (or a local checkout / tarball): dsh plugin --profile web add github:lxj808624/dsh-tool-git#v0.1.3 Then restart `dsh --profile web`. For GitHub installs, pnpm asks you to allowlist the `prepare` build script once (see the [official packaging guide](https://github.com/deepseek-ai/deepseek-harness/b

**profile-level or bundle patch config for the tool-git row**

name: dsh-tool-git config: workDir: '' # repo discovery start dir (default: process cwd) gitPath: git # git executable destructivePolicy: deny # deny | ask | allow extraDestructivePatterns: [] # extra case-insensitive regexes for the gate logMaxCommits: 20 # git_log default count (cap 100) diffContextLines: 3 # patch context lines for git_diff / git_show an explanation. (`ctx.approval`); without a

## 🔗 Links

- [GitHub Repository](https://github.com/lxj808624/dsh-tool-git)
- [Full README](https://github.com/lxj808624/dsh-tool-git#readme)
- [Back to the Plugins list](../plugins.md)
