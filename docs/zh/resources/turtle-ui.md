---
title: "turtle-ui"
description: "官方 UI 插件参考实现。"
keywords: "turtle-ui, learning, example, ui, coding, deepseek harness, dsh"
---
# turtle-ui

> ⭐ **8** · ✅ 活跃 · 示例 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 示例 | 分类 | 学习 |
| 星数 | ⭐ 8 | 状态 | ✅ 活跃 |
| 作者 | [turtle1999](https://github.com/turtle1999) | 更新时间 | 2026-08-13 |

## 一句话介绍

> 官方 UI 插件参考实现。

## 详细介绍

This repository contains the former `packages/ui/tui` implementation, its unit and terminal snapshot tests, and a dsh profile bundle patch. The TUI owns terminal presentation and input; DeepSeek Harness owns the agent, model, tools, persistence, and `dsh` launcher.

## 📦 安装

```bash
(cd ../deepseek-harness && pnpm install && pnpm run build)
pnpm install
pnpm run build
```

## 🚀 快速开始

```bash
pnpm run build
dsh plugin --profile tui add file:.
dsh --profile tui
```

## 🔗 链接

- [GitHub 仓库](https://github.com/turtle1999/turtle-ui)
- [完整 README](https://github.com/turtle1999/turtle-ui#readme)
- [返回turtle-ui所在分类](../examples.md)
