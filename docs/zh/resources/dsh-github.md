---
title: "dsh-github"
description: "DeepSeek Harness plugin: GitHub repository & issue search, repo/issue details, and file reading tools (github_search / github_get) · DeepSeek Harness 插件:GitHub 仓库与 issue 检索、详情与文件读取,匿名可用,可选只读 token 解锁代码搜索"
keywords: "dsh-github, search, plugin, coding, git, deepseek harness, dsh"
---
# dsh-github

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 搜索与研究 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [moxingovo](https://github.com/moxingovo) | 更新时间 | — |
| 子分类 | 🌐 网页搜索 | 能力 | coding, git, search |

## 一句话介绍

> DeepSeek Harness plugin: GitHub repository & issue search, repo/issue details, and file reading tools (github_search / github_get) · DeepSeek Harness 插件:GitHub 仓库与 issue 检索、详情与文件读取,匿名可用,可选只读 token 解锁代码搜索

## 详细介绍

**GitHub PRs, reviews, issues, and CI for DeepSeek Harness — every write gated by human approval, token never logged.** *Create, review, merge, and search GitHub from the agent, with a CI composite action, polling review bot, and status-check gate.* - **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add @perrylink/dsh-github` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ 核心特性

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add @perrylink/dsh-github` (counts toward the [deepseek1024.com](https://dee

## 📦 安装

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-github#main"

# or from npm (published releases)
dsh plugin --profile web add @perrylink/dsh-github

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: dsh-github'
```

## 📚 更多信息

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 链接

- [GitHub 仓库](https://github.com/moxingovo/dsh-github)
- [完整 README](https://github.com/moxingovo/dsh-github#readme)
- [返回dsh-github所在分类](../plugins.md)
