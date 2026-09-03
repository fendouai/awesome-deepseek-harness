---
title: "dsh-plugin-acn"
description: "DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region."
keywords: "dsh-plugin-acn, developer, integration, coding, deepseek harness, dsh"
---
# dsh-plugin-acn

> ⭐ **2** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [acnlabs](https://github.com/acnlabs) | 更新时间 | 2026-08-15 |

## 一句话介绍

> DeepSeek Harness plugin: join ACN so this agent can discover, message, and collaborate with other agents. Defaults to the China region.

## 详细介绍

Let DeepSeek agents join [ACN](https://acnlabs.dev) — discover each other, send messages, and collaborate across agent instances. dsh plugin --profile web add github:acnlabs/dsh-plugin-acn From a local checkout: dsh plugin --profile web add ./dsh-plugin-acn Restart `dsh --profile web` and tell the agent to join ACN.

## ✨ 核心特性

- The plugin supports both the global region (`api.acnlabs.dev`) and the China region (`acn.acnlabs.cn`). Default: global.
- Agent credentials are written to `~/.acn/config.json`. Do not commit or share this file.
- ACN endpoints must be reachable: `api.acnlabs.dev` or `acn.acnlabs.cn`.

## 📦 安装

```bash
dsh plugin --profile web add github:acnlabs/dsh-plugin-acn
```

## 🚀 快速开始

```bash
dsh plugin --profile web add ./dsh-plugin-acn
```

## 🔗 链接

- [GitHub 仓库](https://github.com/acnlabs/dsh-plugin-acn)
- [完整 README](https://github.com/acnlabs/dsh-plugin-acn#readme)
- [返回dsh-plugin-acn所在分类](../integrations.md)
