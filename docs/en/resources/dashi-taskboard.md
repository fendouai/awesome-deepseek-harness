---
title: "dashi-taskboard"
description: "Modern, flexibly embeddable task board supporting Codex and DeepSeek Harness: manage tasks across sessions in one panel."
keywords: "dashi-taskboard, ui, plugin, workflow, deepseek harness, dsh"
---
# dashi-taskboard

> ⭐ **2,813** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 2,813 | Status | ✅ active |
| Author | [chuspeeism](https://github.com/chuspeeism) | Updated | — |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | ui, workflow |

## One-liner

> Modern, flexibly embeddable task board supporting Codex and DeepSeek Harness: manage tasks across sessions in one panel.

## About

A local-first issue board that runs in a browser and can be embedded in Codex through the standalone CDP launcher or its injection script. The same HTTP API powers the React UI and the `taskctl` CLI used by the bundled Codex Skill.

## ✨ Key Features

- Node.js 22.5 or newer
- macOS App and DMG builds: Xcode Command Line Tools and Rust 1.88 or newer with the `aarch64-apple-darwin` and `x86_64-apple-darwin` targets. `npm install` insta
- Windows NSIS builds: the Microsoft Store Codex App, Rust 1.88 or newer, and Visual Studio Build Tools with the C++ workload and Windows SDK.

## 📦 Install

```bash
npm install
npm run build
npm start
```

## 🚀 Quick Start

```bash
npm run dev
```

## 📚 Learn more

**Install the Codex Skill**

Copy or symlink `skills/manage-taskboard` into the Codex skills directory, then start a new Codex task: ln -s /absolute/path/to/codex-taskboard/skills/manage-taskboard \ ~/.agents/skills/manage-taskboard The desktop app keeps this same directory synchronized with its bundled Skill. The Skill teaches Codex to inspect an issue, move it to `in_progress`, use optimistic versions, verify the work, and 

**Configuration**

`npm start` prints both the local URL and the available LAN URLs. Teammates on the same trusted network can open one of those LAN URLs and use the same taskboard service. Task, comment, and attachment changes are broadcast to every open client through server-sent events; reconnecting clients perform a full refresh so changes made while disconnected are not missed. A teammate using `taskctl` can po

## 🔗 Links

- [GitHub Repository](https://github.com/chuspeeism/dashi-taskboard)
- [Full README](https://github.com/chuspeeism/dashi-taskboard#readme)
- [Back to the Plugins list](../plugins.md)
