---
title: "dsh-genui"
description: "Generative UI inside conversations: layouts, charts, forms, quizzes, Mermaid and interactive events rendered inline."
keywords: "dsh-genui, ui, plugin, deepseek harness, dsh"
---
# dsh-genui

> ⭐ **282** · ✅ active · plugin · ⬆️ +19 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 282 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | 2026-08-21 |
| Subcategory | 💡 Generative UI | Capabilities | ui |

## One-liner

> Generative UI inside conversations: layouts, charts, forms, quizzes, Mermaid and interactive events rendered inline.

## About

**English** · [简体中文](./README.zh-CN.md) [**Open the live product site**](https://omdsh-dev.github.io/dsh-genui/) · [**Watch the real demo**](#watch-the-real-interface) · [**Install in DSH**](#quick-start) `dsh-genui` turns a model reply into a **safe, interactive DSH surface**. Ask “how are this month’s orders doing?” and the answer can include a sortable data panel, a native video, a draggable plot, a local quiz, or a persistent session panel — without replacing the surrounding text.

## ✨ Key Features

- **Answer-as-UI**: components are embedded in the reply and appear as they stream — no waiting for the whole message
- **30+ components**: cards, tables, charts, forms, tabs, accordions, file trees, timelines, diffs…
- **Native media**: audio and video play inline from browser-reachable http(s) or same-origin relative URLs, with user-controlled playback, video posters/aspect r
- **ECharts integration**: the `echart` node renders full ECharts charts with theme-aware colors, tooltips, and legends. Two modes: **preset shorthand** (`preset:
- **Quiz**: `quiz` grades on click with explanation and retry; with `action`, the answer is also sent back to the model (grading stays local and instant)
- **Local grading (submit)**: a multiple-choice set = one `radio` per question with `group` + `answer` (correct answer) + `explanation`, plus one `submit` button 
- **State persistence**: answers, submission locks, and input values are saved per "session + content fingerprint" — refresh or reopen restores everything; re-ren
- **Form semantics**: `input` Enter / `textarea` Ctrl+Enter submits immediately (`submit:true`), no blur needed; fields with an `id` are collected into the submit

## 📦 Install

```bash
# Public npm package (works without an npm account)
dsh plugin --profile web add @changfenhuang/dsh-genui
```

## 🚀 Quick Start

```bash
npm install @changfenhuang/dsh-genui
```

## 📚 Learn more

**🚀 Quick start**

Prerequisites — all required: 1. **dsh installed** (any open-source build works — the plugin picks its rendering channel at startup, see "dual-channel rendering" above) 2. **`pnpm` on your PATH**: the `dsh plugin` command depends on it. If missing: `corepack enable` (or `npm i -g pnpm`), then **open a new terminal** and confirm `pnpm -v` prints a version Install and activate in DSH (one command, a

**Verify the install in 60 seconds**

After the command completes, restart dsh web and hard-refresh the browser. In a **new** session, say: Use dsh-ui to draw a stats dashboard with a sortable service table. You should see the reply turn into an in-place dashboard rather than a code block. For an unambiguous technical check, open the browser console: successful activation prints `[genui] client active; fence-channel=registry|dom`.

**📄 Example**

The model outputs this fence (written for the browser — you don't need to read it): {"title":"Order overview","items":[ {"type":"stat","label":"Total revenue","value":"¥128,430","delta":"+12.4%"}, {"type":"stat","label":"Orders","value":"1,024","delta":"-3.1%"} ]} What you see: two stat cards.

**ECharts example**

{"title":"Q1 Revenue","items":[ {"type":"echart","title":"Monthly Revenue","preset":"bar","data":[ {"label":"Jan","value":98}, {"label":"Feb","value":112}, {"label":"Mar","value":128} ]} ]} What you see: a themed bar chart with tooltips and axis labels — rendered by ECharts, lazy-loaded on demand.

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-genui)
- [Full README](https://github.com/omdsh-dev/dsh-genui#readme)
- [Back to the Plugins list](../plugins.md)
