---
title: "dsh-annotate"
description: "Visual browser element annotation for DeepSeek Harness, capturing DOM, styles, accessibility data, comments, and viewport screenshots. DeepSeek Harness 浏览器元素标注插件，捕获 DOM、样式、可访问性数据、评论和视口截图。"
keywords: "dsh-annotate, browser, integration, coding, deepseek harness, dsh"
---
# dsh-annotate

> ⭐ **11** · ✅ active · integration

| | | | |
|---|---|---|---|
| Type | integration | Category | Browser control |
| Stars | ⭐ 11 | Status | ✅ active |
| Author | [BrambleXu](https://github.com/BrambleXu) | Updated | — |

## One-liner

> Visual browser element annotation for DeepSeek Harness, capturing DOM, styles, accessibility data, comments, and viewport screenshots. DeepSeek Harness 浏览器元素标注插件，捕获 DOM、样式、可访问性数据、评论和视口截图。

## About

=24"> English | 中文 Visual browser feedback for DeepSeek Harness. `/annotate` asks the companion Chrome extension to enter selection mode; each selected element contributes a selector, DOM facts, computed style highlights, accessibility data, a comment, and an optional viewport screenshot to the agent's next turn.

## ✨ Key Features

- Select elements directly in Chrome or Chromium through `/annotate`.
- Capture selectors, DOM facts, computed-style highlights, accessibility data, comments, and optional viewport screenshots.
- Send structured annotations to the Agent through a local loopback WebSocket bridge.
- Restrict browser connections by loopback host, extension origin, and optional extension ID.

## 📦 Install

```bash
dsh plugin --profile demo add ./dsh-annotate
```

## 🚀 Quick Start

```bash
/annotate
/annotate http://localhost:3000
```

## 📚 Learn more

**Install 📦**

Add the plugin project to a Harness profile: dsh plugin --profile demo add ./dsh-annotate Then install the companion extension: 1. Open `chrome://extensions` in Chrome or Chromium. 2. Enable **Developer mode**. 3. Choose **Load unpacked** and select this project's `browser-extension` directory. 4. Open the extension popup and keep the default bridge endpoint. For tighter local authorization, copy 

**Configure ⚙️**

name: dsh-annotate config: host: 127.0.0.1 port: 43119 allowedExtensionId: abcdefghijklmnopqrstuvwxyzabcdef requestTimeoutMs: 300000 maxPayloadBytes: 16777216 includeScreenshot: true The server refuses non-loopback hosts and browser connections whose origin is not `chrome-extension://`. An empty `allowedExtensionId` accepts any locally installed Chrome extension; set the exact ID for stricter isol

## 🔗 Links

- [GitHub Repository](https://github.com/BrambleXu/dsh-annotate)
- [Full README](https://github.com/BrambleXu/dsh-annotate#readme)
- [Back to the MCP & Integrations list](../integrations.md)
