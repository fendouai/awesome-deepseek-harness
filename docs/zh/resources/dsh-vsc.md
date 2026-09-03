---
title: "dsh-vsc"
description: "面向 DeepSeek Harness 的原生 VS Code 扩展：侧边栏面板 + 编辑器桥接（选中提问、审查 Agent 改动、审批与提问卡片）。纯协议客户端，基于 DSH 线协议构建，不启动第二个服务。"
keywords: "dsh-vsc, ide, integration, deepseek harness, dsh"
---
# dsh-vsc

> ⭐ **0** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | IDE 与编辑器 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [zhibailu](https://github.com/zhibailu) | 更新时间 | — |

## 一句话介绍

> 面向 DeepSeek Harness 的原生 VS Code 扩展：侧边栏面板 + 编辑器桥接（选中提问、审查 Agent 改动、审批与提问卡片）。纯协议客户端，基于 DSH 线协议构建，不启动第二个服务。

## 详细介绍

**Run [DeepSeek Harness](https://github.com/deepseek-ai/dsh) — the local AI agent — inside VS Code.** A native sidebar panel plus an editor bridge that connects to DSH as a **protocol client**, without rewriting it and without starting a second server. Read this in: **English** · [简体中文](README.zh.md) --- ---

## ✨ 核心特性

- Streaming agent replies, collapsible **reasoning** and per-turn **timing**.
- Adjacent tool calls merged into **"⚙ Actions"** collapsible blocks; **`+N-M`** change stats per turn.
- **Approval cards** when the agent asks to run a privileged operation — allow once / deny.
- **Question cards** for agent questions: single-choice (number keys), multi-select checkboxes, recommended badge, custom answer with ↑↓ recall, skip — answered v
- **Session modes** (standard / PTC / minimal / creative), **reasoning-effort** switch, and **permission-preset** switch (read-only / workspace-write / full-acces
- **Composer takeover**: the input bar hides while the agent is asking, so you can't accidentally send a message mid-question.
- **Ask DSH about a selection** — select code → right-click → *DSH: Ask about selection*, with a structured context card (file / selection / workspace / branch) i
- **Review Agent Changes** — watches `write` / `edit` / `str_replace_editor` tool calls, reports changed files per turn, opens the native VS Code **git diff** in 

## 📦 安装

```bash
git clone https://github.com/zhibailu/dsh-vsc.git
cd dsh-vsc
npm install
npm run package        # esbuild build + vsce package → dsh-vsc-<version>.vsix
code --install-extension dsh-vsc-<version>.vsix --force
```

## 🚀 快速开始

```bash
npm install
npm run typecheck   # tsc --noEmit (both configs)
npm run build       # esbuild → dist/extension.js + dist/media
npm run package     # build + package vsix
```

## 📚 更多信息

**Screenshots**

**Sidebar & chat** — the native DSH panel: session list, streaming reply, collapsible "⚙ Actions", per-turn timing, `+N-M` stats <p align="center"></p> **Ask about selection** — select code in the editor, right-click → *DSH: Ask about selection* <p align="center"></p> **Ask card** — structured context card (file / selection / workspace / branch) shown in the panel <p align="center"></p> **Approval

**Installation**

> Requires Windows / macOS / Linux + VS Code `^1.90.0`. DSH itself does not need to be installed separately — the extension auto-starts one when none is running. **Option A — Release package (recommended)** 1. Download the latest `dsh-vsc-<version>.vsix` from [Releases](https://github.com/zhibailu/dsh-vsc/releases). 2. Install it (VS Code `Ctrl+Shift+P` → **Install from VSIX**, or command line): `

**Quick start**

1. **Reload the window** — required after install. 2. Click the **DSH** icon in the left activity bar to open the sidebar. 3. If no harness is running, the extension silently starts one (no window pops up); if one is running, it reuses it. 4. Send a message and watch the agent work. **No API key needed in the extension.** Your key stays on the DSH side (configured the first time you run `dsh web`)

## 🔗 链接

- [GitHub 仓库](https://github.com/zhibailu/dsh-vsc)
- [完整 README](https://github.com/zhibailu/dsh-vsc#readme)
- [返回dsh-vsc所在分类](../integrations.md)
