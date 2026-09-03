---
title: "webdsh"
description: "Running DeepSeek Harness on web"
keywords: "webdsh, search, plugin, coding, deepseek harness, dsh"
---
# webdsh

> ⭐ **18** · ✅ active · plugin · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 18 | Status | ✅ active |
| Author | [futrime](https://github.com/futrime) | Updated | 2026-08-21 |
| Subcategory | 🌐 Web search | Capabilities | coding |

## One-liner

> Running DeepSeek Harness on web

## About

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`) is an agent harness where everything is a plugin. `dsh web` runs a Node host and serves a browser client to it. **webdsh is that, as static files** — the host runs inside the page, and the agent's commands run in [WebContainers](https://webcontainers.io): Node itself, in the tab. - ⚡ **Nothing to run.** No server, no install, no local Node — the harness boots in the page. - 🌍 **The container is online too.** The page's CORS policy is preloaded into every Node process it starts, so `fetch` inside the container retries a refused host through the proxy on its own — `http://example.com` answers there now, and it did not before. - 🖥️ **Real Node, real Python.** `npm install` and `pip install` both work, and the terminal

## ✨ Key Features

- ⚡ **Nothing to run.** No server, no install, no local Node — the harness boots in the page.
- 🌍 **The container is online too.** The page's CORS policy is preloaded into every Node process it starts, so `fetch` inside the container retries a refused host
- 🖥️ **Real Node, real Python.** `npm install` and `pip install` both work, and the terminal and the agent share one container.
- 💾 **Or a whole PC.** Settings → Machine swaps the container for [v86](https://github.com/copy/v86) and offers **128 machines** — the whole of v86's catalog, fro
- 🧭 **Or a browser.** The third machine is real tabs of the real web, and the assistant drives them three ways: the page structure (a labelled tree with a handle 
- 🤖 **And it can be programmed.** One action per turn is the wrong shape for a table with twenty rows in it, so the browser machine also takes *programs*: `browse

## 🚀 Quick Start

```bash
npm ci
npm run build        # → dist/
node scripts/serve.mjs 4173
```

## 📚 Learn more

**Install**

Nothing to install — [open the page](https://dsh.zjzh.me/). To run it yourself: npm ci npm run build # → dist/ node scripts/serve.mjs 4173 Node 22 or newer. `dist/` is plain static files with relative URLs, so it works at a domain root, a project path, or a local directory.

**Usage**

Open the page, choose a workspace, start talking. 42 models across six routes are registered up front, so it answers before it asks you for anything. Three things live in the sidebar: in; take a file, a directory or a tick-box selection back out. Click a path the assistant mentions to open it here. container, the live screen for an emulated PC, the tab strip and address bar for the browser. Click 

## 🔗 Links

- [GitHub Repository](https://github.com/futrime/webdsh)
- [Full README](https://github.com/futrime/webdsh#readme)
- [Back to the Plugins list](../plugins.md)
