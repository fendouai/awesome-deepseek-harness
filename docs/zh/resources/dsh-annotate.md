---
title: "dsh-annotate"
description: "Visual browser element annotation for DeepSeek Harness, capturing DOM, styles, accessibility data, comments, and viewport screenshots. DeepSeek Harness 浏览器元素标注插件，捕获 DOM、样式、可访问性数据、评论和视口截图。"
keywords: "dsh-annotate, browser, integration, coding, deepseek harness, dsh"
---
# dsh-annotate

> ⭐ **11** · ✅ 活跃 · 集成

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 浏览器控制 |
| 星数 | ⭐ 11 | 状态 | ✅ 活跃 |
| 作者 | [BrambleXu](https://github.com/BrambleXu) | 更新时间 | — |

## 一句话介绍

> Visual browser element annotation for DeepSeek Harness, capturing DOM, styles, accessibility data, comments, and viewport screenshots. DeepSeek Harness 浏览器元素标注插件，捕获 DOM、样式、可访问性数据、评论和视口截图。

## 详细介绍

=24"> English | 中文 Visual browser feedback for DeepSeek Harness. `/annotate` asks the companion Chrome extension to enter selection mode; each selected element contributes a selector, DOM facts, computed style highlights, accessibility data, a comment, and an optional viewport screenshot to the agent's next turn.

## ✨ 核心特性

- Select elements directly in Chrome or Chromium through `/annotate`.
- Capture selectors, DOM facts, computed-style highlights, accessibility data, comments, and optional viewport screenshots.
- Send structured annotations to the Agent through a local loopback WebSocket bridge.
- Restrict browser connections by loopback host, extension origin, and optional extension ID.

## 📦 安装

```bash
dsh plugin --profile demo add ./dsh-annotate
```

## 🚀 快速开始

```bash
/annotate
/annotate http://localhost:3000
```

## 📚 更多信息

**Install 📦**

Add the plugin project to a Harness profile: dsh plugin --profile demo add ./dsh-annotate Then install the companion extension: 1. Open `chrome://extensions` in Chrome or Chromium. 2. Enable **Developer mode**. 3. Choose **Load unpacked** and select this project's `browser-extension` directory. 4. Open the extension popup and keep the default bridge endpoint. For tighter local authorization, copy 

**Configure ⚙️**

name: dsh-annotate config: host: 127.0.0.1 port: 43119 allowedExtensionId: abcdefghijklmnopqrstuvwxyzabcdef requestTimeoutMs: 300000 maxPayloadBytes: 16777216 includeScreenshot: true The server refuses non-loopback hosts and browser connections whose origin is not `chrome-extension://`. An empty `allowedExtensionId` accepts any locally installed Chrome extension; set the exact ID for stricter isol

## 🔗 链接

- [GitHub 仓库](https://github.com/BrambleXu/dsh-annotate)
- [完整 README](https://github.com/BrambleXu/dsh-annotate#readme)
- [返回dsh-annotate所在分类](../integrations.md)
