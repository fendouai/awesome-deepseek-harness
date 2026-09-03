---
title: "dsh-diagram"
description: "Turn articles in DeepSeek Harness into editable Excalidraw canvases."
keywords: "dsh-diagram, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-diagram

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [hanzhangzzz](https://github.com/hanzhangzzz) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Turn articles in DeepSeek Harness into editable Excalidraw canvases.

## About

Your DSH session already understands the article. Turn that understanding into an Excalidraw canvas you can keep editing. The Agent creates the first structure; you refine it in DSH, autosave it, and export it. The result stays editable instead of becoming disposable Mermaid output. Install it in one command, then type `/` and pick **canvas-diagram** in any DSH session: npx -y @deepseek-ai/dsh@0.1.1-rc.2 plugin --profile web add dsh-diagram@latest Full requirements and verification: [Quick install](#quick-install).

## ✨ Key Features

- **Editable, not disposable.** Continue working in a full Excalidraw canvas instead of accepting a static generated image.
- **Clean or sketchnote.** Keep the default precise diagram, or ask for a warm-paper editorial sketch with handwritten text, marker washes, and editable semantic 
- **Built into the conversation.** A live preview card lands in the chat flow right after creation, and the **Canvas** tab opens the full editor without leaving t
- **Saved and ready to share.** Revision-safe autosave protects newer work, and export produces `.excalidraw`, SVG, or PNG.

## 📦 Install

```bash
pnpm dsh plugin --profile web add dsh-diagram@latest
pnpm dsh --profile web --dump-config
pnpm dsh web
```

## 🚀 Quick Start

```bash
dsh plugin --profile web add dsh-diagram@latest
dsh --profile web --dump-config
dsh web
```

## 📚 Learn more

**Quick install**

Requirements: DeepSeek Harness does not install a global `dsh` command by default; the official way to launch it is through `npx`. The commands below work on any machine that meets the requirements: npx -y @deepseek-ai/dsh@0.1.1-rc.2 plugin --profile web add dsh-diagram@latest npx -y @deepseek-ai/dsh@0.1.1-rc.2 --profile web --dump-config npx -y @deepseek-ai/dsh@0.1.1-rc.2 web The config dump shou

**Install the exact latest public GitHub Release artifact**

The release page publishes the same prebuilt tarball with a SHA-256 checksum: dsh plugin --profile web add \ https://github.com/hanzhangzzz/dsh-diagram/releases/download/v0.4.0/dsh-diagram-0.4.0.tgz See [v0.4.0](https://github.com/hanzhangzzz/dsh-diagram/releases/tag/v0.4.0) for the checksum and release notes.

## 🔗 Links

- [GitHub Repository](https://github.com/hanzhangzzz/dsh-diagram)
- [Full README](https://github.com/hanzhangzzz/dsh-diagram#readme)
- [Back to the Plugins list](../plugins.md)
