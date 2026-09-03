---
title: "dsh-gitflow"
description: "Git status, diff, log, commit, branch, and optional Change Ledger tools for DeepSeek Harness."
keywords: "dsh-gitflow, vision, plugin, coding, git, deepseek harness, dsh"
---
# dsh-gitflow

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [lonelymoon87](https://github.com/lonelymoon87) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding, git |

## One-liner

> Git status, diff, log, commit, branch, and optional Change Ledger tools for DeepSeek Harness.

## About

Git status, diff, log, commit, branch, and optional restore-point tools for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). The v0.1.3 release is tested with DSH 0.1.0-rc.8 and 0.1.1-rc.1 while retaining the rc.6-compatible peer range. Prebuilt packages are distributed through GitHub Releases; npm publication is prepared but not yet live. [简体中文](./README.zh-CN.md)

## ✨ Key Features

- `git_status` reads branch and working-tree counts.
- `git_diff` reads unstaged or staged unified diffs without touching the index.
- `git_log` returns bounded structured commit history and handles unborn repositories.
- `git_commit` commits only existing staged changes and requires DSH approval.
- `git_branch` lists local branches; create and switch require approval.
- `/commit` loads a staged-change review skill before calling `git_commit`.

## 📦 Install

```bash
dsh plugin --profile web add https://github.com/lonelymoon87/dsh-gitflow/releases/download/v0.1.3/dsh-gitflow-0.1.3.tgz
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add github:lonelymoon87/dsh-gitflow#v0.1.3
```

## 📚 Learn more

**Install**

The package supports DSH `>=0.1.0-rc.6 <0.2.0` plugin APIs and Node.js `^22.19 || >=24`. dsh plugin --profile web add https://github.com/lonelymoon87/dsh-gitflow/releases/download/v0.1.3/dsh-gitflow-0.1.3.tgz The release tarball is prebuilt and needs no build allowance. A pinned source install is also supported: dsh plugin --profile web add github:lonelymoon87/dsh-gitflow#v0.1.3 The source install

**Configuration**

name: dsh-gitflow config: timeoutMs: 30000 maxOutputBytes: 2097152 maxLogEntries: 100 conventionalCommits: true autoCheckpoint: false checkpointTools: - write - edit - str_replace_editor - git_commit - git_branch `autoCheckpoint` is disabled by default. Enabling it without a Change Ledger service does not pretend recovery exists; it leaves calls unchanged.

## 🔗 Links

- [GitHub Repository](https://github.com/lonelymoon87/dsh-gitflow)
- [Full README](https://github.com/lonelymoon87/dsh-gitflow#readme)
- [Back to the Plugins list](../plugins.md)
