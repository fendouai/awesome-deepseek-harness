---
title: "dsh-session-search"
description: "免索引跨 Agent 会话搜索。"
keywords: "dsh-session-search, developer, plugin, search, files, deepseek harness, dsh"
---
# dsh-session-search

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [Tieboyh](https://github.com/Tieboyh) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 免索引跨 Agent 会话搜索。

## 详细介绍

Cross-agent session search plugin for DeepSeek Harness — directly scan past conversations from dsh, Codex, Claude Code, pi, and OpenCode without creating a derived database. [中文](README.zh-CN.md)

## 📦 安装

```bash
git clone https://github.com/dsh-external/dsh-session-search.git
dshx install dsh-session-search ./dsh-session-search
```

## 🚀 快速开始

```bash
# ~/.dsh/config.yaml
- insert:
    - id: dsh-session-search
      name: '/absolute/path/to/dsh-session-search/lib/index.js'
      config:
        sources: { dsh: true, codex: true, claude: true, pi: true, opencode: true }
        maxResults: 10
        readWindow: 10
```

## 📚 更多信息

**Install (marisa / dshx)**

git clone https://github.com/dsh-external/dsh-session-search.git dshx install dsh-session-search ./dsh-session-search Or install directly from a git URL. The plugin is mounted into `~/.dsh/config.yaml` and takes effect on the next `dsh web`/TUI start (hot with Web HMR).

**~/.dsh/config.yaml**

- id: dsh-session-search name: '/absolute/path/to/dsh-session-search/lib/index.js' config: sources: { dsh: true, codex: true, claude: true, pi: true, opencode: true } maxResults: 10 readWindow: 10

## 🔗 链接

- [GitHub 仓库](https://github.com/Tieboyh/dsh-session-search)
- [完整 README](https://github.com/Tieboyh/dsh-session-search#readme)
- [返回dsh-session-search所在分类](../plugins.md)
