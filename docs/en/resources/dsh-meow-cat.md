---
title: "dsh-meow-cat"
description: "A cat runs across the bottom of the DeepSeek Harness web UI with a synthesized meow every time a conversation turn ends."
keywords: "dsh-meow-cat, channel, integration, coding, ui, deepseek harness, dsh"
---
# dsh-meow-cat

> ⭐ **2** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Channels |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [dsh-pub](https://github.com/dsh-pub) | Updated | 2026-08-14 |

## One-liner

> A cat runs across the bottom of the DeepSeek Harness web UI with a synthesized meow every time a conversation turn ends.

## About

Every time a conversation turn ends in the DeepSeek Harness web UI, a small cat 🐈 runs across the bottom of the window with a "喵~" speech bubble and a meow. The meow is synthesized at runtime — no audio assets, no external URLs, no dependencies — and the whole plugin is two plain JavaScript files plus a one-row bundle patch.

## ✨ Key Features

- **Node half** (`lib/index.js`): counts finished turns on the host-plane `agent/status` event (`idle` = no driver remains scheduled) and serves the count at `GET
- **Browser half** (`lib/client.js`): polls the endpoint, and on every increment runs a pure-CSS cat animation across a click-through fixed layer and plays the sy
- **Meow synthesis**: a 16-bit mono WAV is generated in memory — a 520→760→430 Hz pitch contour ("mi-aa-ou") with mid-note vibrato and a nasal harmonic stack — an

## 🚀 Quick Start

```bash
npx dshpub add dsh-pub/dsh-meow-cat --profile web
```

## 📚 Learn more

**Install**

npx dshpub add dsh-pub/dsh-meow-cat --profile web The command pins the current public commit, validates the bundle contract, and forwards to the native `dsh plugin --profile web add …`. Restart your `dsh web` process afterwards; the cat loads with the next page load and runs for the first time when the in-flight turn ends.

**Configuration**

Defaults work out of the box. To tune it live, set a JSON override in your browser console (re-read on every poll): localStorage.setItem("dsh-meow-cat.config", JSON.stringify({ enabled: true, // master switch pollMs: 1500, // status poll interval, min 250 volume: 1.0, // meow volume 0~1 debug: false, // console diagnostics }))

## 🔗 Links

- [GitHub Repository](https://github.com/dsh-pub/dsh-meow-cat)
- [Full README](https://github.com/dsh-pub/dsh-meow-cat#readme)
- [Back to the MCP & Integrations list](../integrations.md)
