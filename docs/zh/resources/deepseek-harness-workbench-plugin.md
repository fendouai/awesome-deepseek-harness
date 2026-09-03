---
title: "deepseek-harness-workbench-plugin"
description: "Deepseek-harness-workbench-plugin"
keywords: "deepseek-harness-workbench-plugin, vision, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-workbench-plugin

> ⭐ **29** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 29 | 状态 | ✅ 活跃 |
| 作者 | [loadingvx](https://github.com/loadingvx) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Deepseek-harness-workbench-plugin

## 详细介绍

The workbench uses a three-column layout. Conversation stays on the left. The two columns on the right are the capability area: editor (**Agent Control Plane**, syntax highlighting, smart terminal) in the center; file tree, Git, Usage, and Ultra Slash on the far right. The right dock tabs are **Files**, **Source Control**, **Usage**, and **Ultra Slash**. The editor’s first tab is **Control Plane** by default.

## ✨ 核心特性

- **Usage** — official API balance, this-machine observed spend, this-session tokens and context. Pin it above the left **Settings** button so you can see spend w
- **Agent Control Plane** — the editor’s first tab by default. Two pages: **Execution trajectory** (timeline fishbone of user → LLM → tools → agent reply, with ex
- **Ultra Slash** — slash commands that inject guidance **without stopping the current turn**. Manage them in the right dock; send them from the bottom group of t
- **Canvas** — live React previews for product prototypes, dashboards, and custom visuals. Agent-written files live under `.canvas/*.canvas.tsx` in the workspace 
- **Smart terminal** — a local PTY in the editor. Real shell lines (including pasted `$ ls`) run as-is. Natural language is translated by **AI command assist** (<
- **Add to chat** — hand the model anything without copying and pasting. Drag a file from the tree (or a DevTools network request) into the chat box; right-click 

## 📦 安装

```bash
dsh plugin --profile web add dsh-workbench-plugin@0.1.32
```

## 🚀 快速开始

```bash
minimumReleaseAgeExclude:
  - dsh-workbench-plugin
```

## 📚 更多信息

**Usage panel**

Open the right-dock **Usage** tab (gauge icon). To keep spend in view while you chat, click the pin: the panel moves above the left **Settings** button. Click pin again to send it back to the right dock. Pin still works when the left rail is collapsed — you get a compact strip with balance, spend, and tokens. Drag the top handle to change height; double-click resets. The session list above stays v

## 🔗 链接

- [GitHub 仓库](https://github.com/loadingvx/deepseek-harness-workbench-plugin)
- [完整 README](https://github.com/loadingvx/deepseek-harness-workbench-plugin#readme)
- [返回deepseek-harness-workbench-plugin所在分类](../plugins.md)
