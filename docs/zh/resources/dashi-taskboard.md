---
title: "dashi-taskboard"
description: "现代化可灵活嵌入的任务面板，支持 Codex 与 DeepSeek Harness，一个面板统一管理跨会话任务。"
keywords: "dashi-taskboard, ui, plugin, workflow, deepseek harness, dsh"
---
# dashi-taskboard

> ⭐ **2,813** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 2,813 | 状态 | ✅ 活跃 |
| 作者 | [chuspeeism](https://github.com/chuspeeism) | 更新时间 | — |
| 子分类 | 🖥️ 侧边栏与面板 | 能力 | ui, workflow |

## 一句话介绍

> 现代化可灵活嵌入的任务面板，支持 Codex 与 DeepSeek Harness，一个面板统一管理跨会话任务。

## 详细介绍

A local-first issue board that runs in a browser and can be embedded in Codex through the standalone CDP launcher or its injection script. The same HTTP API powers the React UI and the `taskctl` CLI used by the bundled Codex Skill.

## ✨ 核心特性

- Node.js 22.5 or newer
- macOS App and DMG builds: Xcode Command Line Tools and Rust 1.88 or newer with the `aarch64-apple-darwin` and `x86_64-apple-darwin` targets. `npm install` insta
- Windows NSIS builds: the Microsoft Store Codex App, Rust 1.88 or newer, and Visual Studio Build Tools with the C++ workload and Windows SDK.

## 📦 安装

```bash
npm install
npm run build
npm start
```

## 🚀 快速开始

```bash
npm run dev
```

## 📚 更多信息

**Install the Codex Skill**

Copy or symlink `skills/manage-taskboard` into the Codex skills directory, then start a new Codex task: ln -s /absolute/path/to/codex-taskboard/skills/manage-taskboard \ ~/.agents/skills/manage-taskboard The desktop app keeps this same directory synchronized with its bundled Skill. The Skill teaches Codex to inspect an issue, move it to `in_progress`, use optimistic versions, verify the work, and 

**Configuration**

`npm start` prints both the local URL and the available LAN URLs. Teammates on the same trusted network can open one of those LAN URLs and use the same taskboard service. Task, comment, and attachment changes are broadcast to every open client through server-sent events; reconnecting clients perform a full refresh so changes made while disconnected are not missed. A teammate using `taskctl` can po

## 🔗 链接

- [GitHub 仓库](https://github.com/chuspeeism/dashi-taskboard)
- [完整 README](https://github.com/chuspeeism/dashi-taskboard#readme)
- [返回dashi-taskboard所在分类](../plugins.md)
