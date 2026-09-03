---
title: "dsh-conversation-share"
description: "分享任意段落的 DSH 对话"
keywords: "dsh-conversation-share, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-conversation-share

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Developer tools |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [bill9109](https://github.com/bill9109) | Updated | — |
| Subcategory | 📁 Files & import | Capabilities | coding |

## One-liner

> 分享任意段落的 DSH 对话

## About

**Install:** `dsh plugin --profile web add github:omdsh-dev/dsh-conversation-share` **Render a selected range of a DeepSeek Harness conversation into a PNG long image with a branded footer, ready to share.** [English](README.md) | [中文](README.zh.md)

## ✨ Key Features

- **Share capsule** to the left of the Session log button in the top-right corner (same style as log; clicking activates a blue highlight, with `[Cancel][Confirm]
- **Two draggable range markers** (horizontal labels: "Start here" / "End here") with magnetic snapping
- **Scrolling model**: handles follow the pointer 1:1 within the viewport without scrolling; only when the pointer enters the top/bottom edge zones (64px) does th
- **Capture**: 40pt theme-background padding (symmetric on all sides) + a DeepSeek Harness brand icon at the bottom (with the BETA badge text); extra-long content
- **Preview modal**: image width adapts, vertical scroll to review, download PNG, copy image

## 📦 Install

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-conversation-share

# Or pin a branch/commit
dsh plugin --profile web add github:omdsh-dev/dsh-conversation-share#main

# Or install from a local checkout (development — rebuild and it takes effect)
dsh plugin --profile web add /path/to/your/dsh-conversation-share
```

## 🚀 Quick Start

```bash
dsh plugin --profile web update github:omdsh-dev/dsh-conversation-share
```

## 📚 Learn more

**Usage**

1. Click the share capsule next to the Session log button in the top-right corner; it activates (blue highlight) and the `[Cancel][Confirm]` controls appear 2. Drag the two range markers to select the conversation range — they snap to message rows, markdown blocks, and line-level text; the start handle snaps to a top edge, the end handle to a bottom edge 3. Click **Confirm** to render the selectio

**Install**

Install into the `web` profile with the standard `dsh plugin` mechanism (no source changes, no manual package.json edits): dsh plugin --profile web add github:omdsh-dev/dsh-conversation-share

**Or install from a local checkout (development — rebuild and **

dsh plugin --profile web add /path/to/your/dsh-conversation-share Internally the command runs `pnpm add <spec>` in the profile directory and automatically appends packages that declare `dsh.bundle` to `dsh.profile.bundles`. The repository ships its build output (`lib/`), so no consumer-side build is needed. After installing, **restart web** and **hard-refresh** the browser (Cmd+Shift+R) — old tabs

**Uninstall**

dsh plugin --profile web remove dsh-conversation-share The command runs `pnpm remove <pkg>` in the profile directory and removes it from `dsh.profile.bundles`. After uninstalling, **restart web** and **hard-refresh** the browser.

## 🔗 Links

- [GitHub Repository](https://github.com/bill9109/dsh-conversation-share)
- [Full README](https://github.com/bill9109/dsh-conversation-share#readme)
- [Back to the Plugins list](../plugins.md)
