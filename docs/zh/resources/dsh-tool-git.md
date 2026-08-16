---
title: "dsh-tool-git"
description: "结构化安全 Git 工具：status/diff/log/branch/stage/commit/stash/show，带破坏性命令防护。"
keywords: "dsh-tool-git, developer, plugin, git, coding, deepseek harness, dsh"
---
# dsh-tool-git

> ⭐ 3 · ✅ 活跃 · 插件

## 一句话介绍

结构化安全 Git 工具：status/diff/log/branch/stage/commit/stash/show，带破坏性命令防护。

## 详细介绍

Structured, safe Git tool family for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`). Coding agents reach for git constantly, but the stock runtime only offers raw `bash`. `dsh-tool-git` gives the model eight structured tools that run `git` through a shell-free subprocess runner and return canonical JSON values — plus a `tools/pre-execute` safety gate that stops destructive git operations (force push, hard reset, rebase, amend, branch deletion, …) before they happen, 

## 作者
**[lxj808624](https://github.com/lxj808624)**

## 链接

- [GitHub 仓库](https://github.com/lxj808624/dsh-tool-git)
- [完整 README](https://github.com/lxj808624/dsh-tool-git#readme)
- [返回dsh-tool-git所在分类](../plugins.md)
