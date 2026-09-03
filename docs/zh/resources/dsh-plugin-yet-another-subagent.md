---
title: "dsh-plugin-yet-another-subagent"
description: "可配置子代理 profile 系统：单一 subagent 工具 + profile 参数，含 Web UI 设置与实时进度。"
keywords: "dsh-plugin-yet-another-subagent, multi-agent, agent, ui, deepseek harness, dsh"
---
# dsh-plugin-yet-another-subagent

> ⭐ **12** · ✅ 活跃 · 智能体 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 智能体 | 分类 | 多智能体 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-20 |

## 一句话介绍

> 可配置子代理 profile 系统：单一 subagent 工具 + profile 参数，含 Web UI 设置与实时进度。

## 详细介绍

可配置的子代理（subagent）profile 系统，提供单一 `subagent` 工具 + `profile` 参数选择，支持 Web UI 设置、实时进度展示（工具调用/token/活动）、子代理树标签页、点击跳转子会话。

## ✨ 核心特性

- **Host 半**（`src/index.ts`）：
- **Client 半**（`src/client/index.ts`）：

## 📦 安装

```bash
pnpm install          # 安装开发依赖 + zod（唯一运行时 npm 依赖）
pnpm run typecheck    # tsc --noEmit（通过 ../dsh 解析 DSH 源码）
pnpm test             # vitest run
pnpm run build        # tsc + tsdown → lib/index.js, lib/invariant.js, lib/client.js
```

## 🚀 快速开始

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-yet-another-subagent

# 本地引用（开发热更新）
dsh plugin --profile web add "link:D:/Projects/deepseek-harness/yet-another-subagent"
```

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent#readme)
- [返回dsh-plugin-yet-another-subagent所在分类](../agents.md)
