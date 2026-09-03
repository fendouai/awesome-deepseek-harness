---
title: "dsh-movein"
description: "Migrate Claude Code setup into DeepSeek Harness. Import skills, commands, agents, hooks, permission rules, and MCP config. Codex and OpenCode supported."
keywords: "dsh-movein, mcp, integration, coding, multi-agent, deepseek harness, dsh"
---
# dsh-movein

> ⭐ **15** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | MCP |
| 星数 | ⭐ 15 | 状态 | ✅ 活跃 |
| 作者 | [sjh9714](https://github.com/sjh9714) | 更新时间 | — |

## 一句话介绍

> Migrate Claude Code setup into DeepSeek Harness. Import skills, commands, agents, hooks, permission rules, and MCP config. Codex and OpenCode supported.

## 详细介绍

[中文](./docs/README.zh.md) Migrate your Claude Code setup into [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness) without rebuilding it by hand. Preview instructions, skills, commands, agents, hooks, permission rules, and MCP servers before DSH writes anything. Existing destinations stay untouched. This GIF uses two screenshots from a live DSH `0.1.1-rc.2` run. The first shows the dry run and the second shows the applied result. If this saves you setup time, [star dsh-movein](https://github.com/sjh9714/dsh-movein).

## ✨ 核心特性

- Claude Code is the primary path
- Dry run is the default
- Every category can be included or excluded
- Conflicts and unsupported entries appear before apply
- Codex and OpenCode stay available under the secondary origin panel

## 📦 安装

```bash
dsh plugin --profile web add dsh-movein
```

## 🚀 快速开始

```bash
# Claude Code
npx dsh-movein
npx dsh-movein --apply

# Codex
npx dsh-movein --from codex
npx dsh-movein --from codex --apply

# OpenCode
npx dsh-movein --from opencode
npx dsh-movein --from opencode --apply
```

## 🔗 链接

- [GitHub 仓库](https://github.com/sjh9714/dsh-movein)
- [完整 README](https://github.com/sjh9714/dsh-movein#readme)
- [返回dsh-movein所在分类](../integrations.md)
