---
title: "dsh-plugin-check"
description: "Plugin health checks: manifest protocol, patch format, build pitfalls and hub listing status, zero-dependency read-only."
keywords: "dsh-plugin-check, developer, plugin, observability, deepseek harness, dsh"
---
# dsh-plugin-check

> ⭐ **27** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 27 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |
| Subcategory | 🛡️ Security & ops | Capabilities | observability |

## One-liner

> Plugin health checks: manifest protocol, patch format, build pitfalls and hub listing status, zero-dependency read-only.

## About

[English](README.en.md) DSH 插件健康检查工具 —— 扫描插件仓库，诊断**清单协议 / patch 格式 / 构建陷阱 / hub 收录状态**，输出合规报告与修复建议。**只读**，不修改、不构建被检查仓库。

## ✨ Key Features

- **只读**：仅 `readdir/stat/readFile`，绝不修改或构建被检查仓库
- **零业务依赖**：仅 node 内置模块（fs/path/child_process）
- **hub 检查离线优先**：先读本地 hub catalog（`DSH_HUB_SOURCE` 或 cwd/hub/ 下），再通过 `gh` 读取公开 `omdsh-dev/dsh-hub-workshop/catalog.json`；兼容 `dsh-hub-index/v0.4` 与旧 `repos[].name`
- **不执行 tsc**：构建陷阱全部静态文本扫描（快、无副作用）

## 📦 Install

```bash
# 交互式（web）profile
dsh plugin --profile web add github:omdsh-dev/dsh-plugin-check
# 一次性任务（headless）profile —— dsh run 默认使用 headless
dsh plugin --profile headless add github:omdsh-dev/dsh-plugin-check
```

## 🚀 Quick Start

```bash
# tarball 方式（web 为例；headless 同）
npm pack
dsh plugin --profile web add <npm pack 产物 tarball 路径>
```

## 📚 Learn more

**示例**

plugin_check { action: "check", path: "C:/Users/admin/Desktop/dshext/dsh-tool-csv" } → {"repo":"dsh-tool-csv","kind":"tool-bundle","verdict":"pass","checks":{"total":24,"passed":24,...}} plugin_check { action: "scan", path: "C:/Users/admin/Desktop/dshext" } → {"root":"...","scanned":11,"reports":[...]} # dsh-my-rsi 等不合规仓库会带 error+suggestions

**一次性任务（headless）profile —— dsh run 默认使用 headless**

dsh plugin --profile headless add github:omdsh-dev/dsh-plugin-check 包内 `dsh.bundle.patch` 会在安装后自动把插件加入 profile 的 layer stack（row id：`tool-plugin-check`）。插件缺失的 peer 依赖（`cordis`、`@deepseek-ai/dsh-tools`）由 profile 的 healed `profiles/node_modules` 回退安装提供。 > ⚠️ web 与 headless 是**不同 profile**：web 安装不会自动覆盖 headless；`dsh run` 默认使用 headless profile。Windows 路径使用正斜杠（`C:/...`）。

**手动安装与旧版本兼容**

旧场景（monorepo 集成、不支持 Profile Bundle 的旧快照或插件开发调试环境——本地 junction/symlink、手动编辑 profile 层）。

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-plugin-check)
- [Full README](https://github.com/omdsh-dev/dsh-plugin-check#readme)
- [Back to the Plugins list](../plugins.md)
