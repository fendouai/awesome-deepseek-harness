---
title: "dsh-file-mentions"
description: "回复中文件路径可点击：内联打开、文件管理器揭示、提及文件芯片列表。"
keywords: "dsh-file-mentions, developer, plugin, files, ui, deepseek harness, dsh"
---
# dsh-file-mentions

> ⭐ **11** · ✅ 活跃 · 插件 · 近期 ⬆️ +5

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [a903067276-rgb](https://github.com/a903067276-rgb) | 更新时间 | 2026-08-21 |
| 子分类 | 📁 文件与导入 | 能力 | files, ui |

## 一句话介绍

> 回复中文件路径可点击：内联打开、文件管理器揭示、提及文件芯片列表。

## 详细介绍

[English](README.md) | [简体中文](README.zh-CN.md) **Clickable file paths in DSH replies** — a DeepSeek Harness (DSH) web plugin with a Codex-style experience. *Unofficial project: independently developed and maintained by a community member, not an official DeepSeek product.*

## 📦 安装

```bash
dsh plugin --profile web add "github:a903067276-rgb/dsh-file-mentions#main"
```

## 📚 更多信息

**Screenshot**

Inline paths wrapped in backticks (`` `~/...` ``, absolute, relative, or Chinese paths) become **click-to-open**; each clickable path carries a small folder-icon button that reveals the file in your file manager; a "📎 mentioned files" chip list at the turn tail covers the rest. URLs are already auto-linked by the official renderer, so this plugin leaves them alone. The external-drive whitelist (Se

**Install**

This repository is an official **bundle plugin** (`dsh.bundle` + `dsh.client` in the root `package.json`), installed through the official profile manager: dsh plugin --profile web add "github:a903067276-rgb/dsh-file-mentions#main" Then **restart `dsh web`** (bundle layers are composed at startup; HMR does not apply). Requires `pnpm` on PATH (`dsh plugin` forwards to pnpm). Manual mount fallback: s

**Usage**

Have the agent wrap paths in backticks (e.g. `` `~/docs/plan.md` ``) to make them clickable inline. The tail chip list appears automatically — no configuration.

## 🔗 链接

- [GitHub 仓库](https://github.com/a903067276-rgb/dsh-file-mentions)
- [完整 README](https://github.com/a903067276-rgb/dsh-file-mentions#readme)
- [返回dsh-file-mentions所在分类](../plugins.md)
