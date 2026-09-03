---
title: "dsh-github"
description: "DeepSeek Harness plugin: GitHub repository & issue search, repo/issue details, and file reading tools (github_search / github_get) · DeepSeek Harness 插件:GitHub 仓库与 issue 检索、详情与文件读取,匿名可用,可选只读 token 解锁代码搜索"
keywords: "dsh-github, search, plugin, coding, git, deepseek harness, dsh"
---
# dsh-github

> ⭐ **1** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 1 | Status | ✅ active |
| Author | [moxingovo](https://github.com/moxingovo) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, git, search |

## One-liner

> DeepSeek Harness plugin: GitHub repository & issue search, repo/issue details, and file reading tools (github_search / github_get) · DeepSeek Harness 插件:GitHub 仓库与 issue 检索、详情与文件读取,匿名可用,可选只读 token 解锁代码搜索

## About

**GitHub PRs, reviews, issues, and CI for DeepSeek Harness — every write gated by human approval, token never logged.** *Create, review, merge, and search GitHub from the agent, with a CI composite action, polling review bot, and status-check gate.* - **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add @perrylink/dsh-github` (counts toward the [deepseek1024.com](https://deepseek1024.com) install ranking). [English](README.md) · [简体中文](README.zh.md) · [Español](README.es.md) · [Português](README.pt.md) · [हिन्दी](README.hi.md) ---

## ✨ Key Features

- **1024 store channel**: `npm i -g dsh1024` once, then `dsh1024 plugin --profile web add @perrylink/dsh-github` (counts toward the [deepseek1024.com](https://dee

## 📦 Install

```bash
# 1. install the bundle into your profile
dsh plugin --profile web add "github:PerryLink/dsh-github#main"

# or from npm (published releases)
dsh plugin --profile web add @perrylink/dsh-github

# 2. restart and verify the row
dsh --profile web --dump-config | grep -A3 'id: dsh-github'
```

## 📚 Learn more

**Configuration**

All tunables are Schemastery `Config` fields (changeable from cordis.yml). An id-targeted override replaces the whole row — restate every key you need. `cordis.patch.yml` documents each key inline.

## 🔗 Links

- [GitHub Repository](https://github.com/moxingovo/dsh-github)
- [Full README](https://github.com/moxingovo/dsh-github#readme)
- [Back to the Plugins list](../plugins.md)
