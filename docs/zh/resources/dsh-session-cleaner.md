---
title: "dsh-session-cleaner"
description: "为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口"
keywords: "dsh-session-cleaner, discovery, plugin, coding, deepseek harness, dsh"
---
# dsh-session-cleaner

> ⭐ **5** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 插件发现 |
| 星数 | ⭐ 5 | 状态 | ✅ 活跃 |
| 作者 | [fountunt](https://github.com/fountunt) | 更新时间 | 2026-08-15 |

## 一句话介绍

> 为 DeepSeek Harness 提供会话删除能力，支持侧边栏 ⋮ 菜单入口

## 详细介绍

[English](README.md) | [中文](README.zh.md) Delete DeepSeek Harness sessions from a **running** web runtime — files, live store, and workspace records — without restarting `dsh web`. The official web API only offers `workspace.archiveSession` (hide); there is no `session.delete`. This bundle closes that gap.

## 📦 安装

```bash
dsh plugin --profile web add dsh-session-cleaner            # from npm
dsh plugin --profile web add github:fountunt/dsh-session-cleaner   # from git

# or from a local checkout
dsh plugin --profile web add file:/path/to/dsh-session-cleaner
```

## 🚀 快速开始

```bash
POST /api-ext/session.delete
Content-Type: application/json

{ "sessionId": "session-1bb8d361-ea6b-4b92-bab2-c858c92e8822" }
```

## 📚 更多信息

**Install**

dsh plugin --profile web add dsh-session-cleaner # from npm dsh plugin --profile web add github:fountunt/dsh-session-cleaner # from git

## 🔗 链接

- [GitHub 仓库](https://github.com/fountunt/dsh-session-cleaner)
- [完整 README](https://github.com/fountunt/dsh-session-cleaner#readme)
- [返回dsh-session-cleaner所在分类](../plugins.md)
