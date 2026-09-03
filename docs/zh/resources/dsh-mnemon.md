---
title: "dsh-mnemon"
description: "三层本地记忆系统：运行时热记忆、项目文档、长期记忆空间，监督式写回。"
keywords: "dsh-mnemon, memory, plugin, context, deepseek harness, dsh"
---
# dsh-mnemon

> ⭐ **156** · ✅ 活跃 · 插件 · 近期 ⬆️ +23

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 记忆与上下文 |
| 星数 | ⭐ 156 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | 2026-08-21 |
| 子分类 | 🧠 记忆系统 | 能力 | memory, context |

## 一句话介绍

> 三层本地记忆系统：运行时热记忆、项目文档、长期记忆空间，监督式写回。

## 详细介绍

The tiers are not copies. A useful rule is: **every-turn context goes to Runtime, complete narratives go to Documents, and cross-task evidence goes to Memory Spaces.** Current instructions, repository files, and live tool results always outrank historical memory.

## 📦 安装

```bash
# macOS
brew install --cask mnemon-dev/tap/mnemon

# macOS / Linux via Go
go install github.com/mnemon-dev/mnemon@latest

mnemon --version
```

## 🚀 快速开始

```bash
npm install -g @deepseek-ai/dsh@0.1.1-rc.2
dsh --version
```

## 📚 更多信息

**2. Install DSH and the plugin**

The registry installation remains verified against stable DSH 0.1.1-rc.2, whose complete profiles require Node.js `^22.19.0 || >=24.0.0`; Node 20 lacks host primitives used by rc.2. Source compatibility is also verified against the latest DSH 0.1.2-alpha.5 preview while rc.2 remains the recommended registry target. The dsh-mnemon package itself retains Node.js 20 compatibility for older compatible

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-mnemon)
- [完整 README](https://github.com/omdsh-dev/dsh-mnemon#readme)
- [返回dsh-mnemon所在分类](../plugins.md)
