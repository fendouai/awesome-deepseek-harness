---
title: "desktop-cc-gui"
description: "Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI."
keywords: "desktop-cc-gui, desktop, client, coding, ui, deepseek harness, dsh"
---
# desktop-cc-gui

> ⭐ **4,058** · ✅ 活跃 · 客户端 · 近期 ⬆️ +5

| | | | |
|---|---|---|---|
| 类型 | 客户端 | 分类 | 桌面端 |
| 星数 | ⭐ 4,058 | 状态 | ✅ 活跃 |
| 作者 | [zhukunpenglinyutong](https://github.com/zhukunpenglinyutong) | 更新时间 | 2026-08-21 |

## 一句话介绍

> Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI.

## 详细介绍

**English** · [简体中文](./README.zh-CN.md) ![][github-contributors-shield] ![][github-forks-shield] ![][github-stars-shield] ![][github-issues-shield] **ccgui** is an open-source **multi-engine AI coding desktop client**. In plain words: it brings command-line AI coding runtimes such as Claude Code, Codex CLI, Gemini CLI, OpenCode, and **DeepSeek Harness (DSH)** into one graphical interface. It is **not** a DSH Web UI shell and **not** a `dsh-plugin`. DSH is one of several native engines; models and API keys for DSH still live in the DSH host / Web UI, while ccgui provides the unified chat, files, Git, and project intelligence surface. No more staring at a black terminal. Open ccgui, pick a project, and chat with AI to write code, fix bugs, and commit to Git. File and tool activity is visible

## ✨ 核心特性

- Registers runtime adapters for **Claude Code**, **Codex CLI**, **Gemini CLI**, **OpenCode**, and **DeepSeek Harness (DSH)**. Gemini is enabled by default; OpenC
- Claude and Codex support managed provider profiles. Gemini and OpenCode retain the provider/configuration model exposed by their own runtimes.
- **DeepSeek Harness** is a native engine (`dsh-host-rpc`): ccgui can adopt a running local `dsh web` host or start one, then create / resume / fork DSH sessions 
- Sessions survive restarts: close the app and your conversation history is still there. Resume broken sessions and see how much context each one is using.

## 📦 安装

```bash
git clone https://github.com/zhukunpenglinyutong/desktop-cc-gui.git
cd desktop-cc-gui
npm install
```

## 🚀 快速开始

```bash
# macOS / Linux
npm run tauri:dev

# Windows
npm run tauri:dev:win
```

## 📚 更多信息

**Step 2: Install dependencies**

git clone https://github.com/zhukunpenglinyutong/desktop-cc-gui.git cd desktop-cc-gui npm install Note: **you must use npm**. pnpm and yarn are blocked by a script (so everyone gets identical dependency versions).

**Building installers**

npm run build:mac-arm64 # macOS Apple Silicon npm run build:mac-x64 # macOS Intel npm run build:mac-universal # macOS Universal npm run build:win-x64 # Windows x64 npm run build:linux-x64 # Linux x64 npm run build:linux-arm64 # Linux arm64 ---

## 🔗 链接

- [GitHub 仓库](https://github.com/zhukunpenglinyutong/desktop-cc-gui)
- [完整 README](https://github.com/zhukunpenglinyutong/desktop-cc-gui#readme)
- [返回desktop-cc-gui所在分类](../clients.md)
