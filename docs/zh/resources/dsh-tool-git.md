---
title: "dsh-tool-git"
description: "结构化安全 Git 工具：status/diff/log/branch/stage/commit/stash/show，带破坏性命令防护。"
keywords: "dsh-tool-git, developer, plugin, git, coding, deepseek harness, dsh"
---
# dsh-tool-git

> ⭐ **4** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 4 | 状态 | ✅ 活跃 |
| 作者 | [lxj808624](https://github.com/lxj808624) | 更新时间 | 2026-08-16 |
| 子分类 | 🛡️ 安全与运维 | 能力 | git, coding |

## 一句话介绍

> 结构化安全 Git 工具：status/diff/log/branch/stage/commit/stash/show，带破坏性命令防护。

## 详细介绍

Structured, safe Git tool family for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). Coding agents reach for git constantly, but the stock runtime only offers raw `bash`. `dsh-tool-git` gives the model eight structured tools that run `git` through a shell-free subprocess runner and return canonical JSON values — plus a `tools/pre-execute` safety gate that stops destructive git operations (force push, hard reset, rebase, amend, branch deletion, …) before they happen, whether the model calls them through these tools **or** through a shell tool. - **No shell injection**: every command goes through `execFile` with an explicit argument array. Model-supplied paths and messages are never string-interpolated. - **Machine output**: porcelain v2, `--numstat`, and `--form

## ✨ 核心特性

- **No shell injection**: every command goes through `execFile` with an explicit
- **Machine output**: porcelain v2, `--numstat`, and `--format` records are parsed
- **Safety by default**: destructive operations are denied with an explanation

## 📦 安装

```bash
dsh plugin --profile web add dsh-tool-git
```

## 🚀 快速开始

```bash
dsh plugin --profile web add github:lxj808624/dsh-tool-git#v0.1.3
```

## 📚 更多信息

**Install**

**npm (recommended)** — from any directory: dsh plugin --profile web add dsh-tool-git **From GitHub** (or a local checkout / tarball): dsh plugin --profile web add github:lxj808624/dsh-tool-git#v0.1.3 Then restart `dsh --profile web`. For GitHub installs, pnpm asks you to allowlist the `prepare` build script once (see the [official packaging guide](https://github.com/deepseek-ai/deepseek-harness/b

**profile-level or bundle patch config for the tool-git row**

name: dsh-tool-git config: workDir: '' # repo discovery start dir (default: process cwd) gitPath: git # git executable destructivePolicy: deny # deny | ask | allow extraDestructivePatterns: [] # extra case-insensitive regexes for the gate logMaxCommits: 20 # git_log default count (cap 100) diffContextLines: 3 # patch context lines for git_diff / git_show an explanation. (`ctx.approval`); without a

## 🔗 链接

- [GitHub 仓库](https://github.com/lxj808624/dsh-tool-git)
- [完整 README](https://github.com/lxj808624/dsh-tool-git#readme)
- [返回dsh-tool-git所在分类](../plugins.md)
