---
title: "deepseek-harness-workbench-plugin"
description: "Deepseek-harness-workbench-plugin"
keywords: "deepseek-harness-workbench-plugin, vision, plugin, coding, deepseek harness, dsh"
---
# deepseek-harness-workbench-plugin

> ⭐ **29** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 29 | Status | ✅ active |
| Author | [loadingvx](https://github.com/loadingvx) | Updated | — |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Deepseek-harness-workbench-plugin

## About

The workbench uses a three-column layout. Conversation stays on the left. The two columns on the right are the capability area: editor (**Agent Control Plane**, syntax highlighting, smart terminal) in the center; file tree, Git, Usage, and Ultra Slash on the far right. The right dock tabs are **Files**, **Source Control**, **Usage**, and **Ultra Slash**. The editor’s first tab is **Control Plane** by default.

## ✨ Key Features

- **Usage** — official API balance, this-machine observed spend, this-session tokens and context. Pin it above the left **Settings** button so you can see spend w
- **Agent Control Plane** — the editor’s first tab by default. Two pages: **Execution trajectory** (timeline fishbone of user → LLM → tools → agent reply, with ex
- **Ultra Slash** — slash commands that inject guidance **without stopping the current turn**. Manage them in the right dock; send them from the bottom group of t
- **Canvas** — live React previews for product prototypes, dashboards, and custom visuals. Agent-written files live under `.canvas/*.canvas.tsx` in the workspace 
- **Smart terminal** — a local PTY in the editor. Real shell lines (including pasted `$ ls`) run as-is. Natural language is translated by **AI command assist** (<
- **Add to chat** — hand the model anything without copying and pasting. Drag a file from the tree (or a DevTools network request) into the chat box; right-click 

## 📦 Install

```bash
dsh plugin --profile web add dsh-workbench-plugin@0.1.32
```

## 🚀 Quick Start

```bash
minimumReleaseAgeExclude:
  - dsh-workbench-plugin
```

## 📚 Learn more

**Usage panel**

Open the right-dock **Usage** tab (gauge icon). To keep spend in view while you chat, click the pin: the panel moves above the left **Settings** button. Click pin again to send it back to the right dock. Pin still works when the left rail is collapsed — you get a compact strip with balance, spend, and tokens. Drag the top handle to change height; double-click resets. The session list above stays v

## 🔗 Links

- [GitHub Repository](https://github.com/loadingvx/deepseek-harness-workbench-plugin)
- [Full README](https://github.com/loadingvx/deepseek-harness-workbench-plugin#readme)
- [Back to the Plugins list](../plugins.md)
