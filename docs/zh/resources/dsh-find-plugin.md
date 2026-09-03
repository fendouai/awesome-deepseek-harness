---
title: "dsh-find-plugin"
description: "会话内插件发现：直接在 DSH 中搜索 GitHub dsh-plugin 主题的实时插件。"
keywords: "dsh-find-plugin, discovery, plugin, search, workflow, deepseek harness, dsh"
---
# dsh-find-plugin

> ⭐ **73** · ✅ 活跃 · 插件 · 近期 ⬆️ +5

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 73 | 状态 | ✅ 活跃 |
| 作者 | [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin) | 更新时间 | 2026-08-19 |

## 一句话介绍

> 会话内插件发现：直接在 DSH 中搜索 GitHub dsh-plugin 主题的实时插件。

## 详细介绍

**A plugin that finds plugins** — think [`/find-skills`](https://skills.sh) from skills.sh, for DSH. Tell your agent what you want ("notify me on WeChat when a task finishes"), and it searches the DSH plugin ecosystem on GitHub for you — top results by stars, each with a one-line description and an install command.

## 📦 安装

```bash
# from npm (prebuilt, recommended)
dsh plugin --profile web add dsh-find-plugin

# or from GitHub
dsh plugin --profile web add github:awesome-dsh-plugin/dsh-find-plugin
```

## 📚 更多信息

**Usage**

Restart `dsh web` after installing, then just talk to the agent — it calls `find_dsh_plugin` on its own whenever plugin discovery helps: Each result comes back with stars, a description, the repo link, and a ready-to-run `dsh plugin add` command — ask the agent to install one and it can run the command for you.

## 🔗 链接

- [GitHub 仓库](https://github.com/awesome-dsh-plugin/dsh-find-plugin)
- [完整 README](https://github.com/awesome-dsh-plugin/dsh-find-plugin#readme)
- [返回dsh-find-plugin所在分类](../plugins.md)
