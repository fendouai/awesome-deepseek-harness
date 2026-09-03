---
title: "dsh-pet-corner"
description: "DSH Pet Corner: a floating pet, keyless pet-image proxy, favorites, and plugin-owned settings API"
keywords: "dsh-pet-corner, ui, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-pet-corner

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [omdsh-dev](https://github.com/omdsh-dev) | Updated | — |
| Subcategory | 🐋 Desktop pets | Capabilities | coding, multimodal |

## One-liner

> DSH Pet Corner: a floating pet, keyless pet-image proxy, favorites, and plugin-owned settings API

## About

**Author / Maintainer:** [@Zacklinkk](https://github.com/Zacklinkk) DSH 的轻量摸鱼角：右下角是一只可拖动的小猫，点击后可浏览猫、狗和狐狸图片、 猫咪知识与收藏。所有第三方请求都先经过宿主白名单代理，浏览器不会直接访问外站。

## ✨ Key Features

- 小猫挂件、来源开关、默认狗狗品种和自动换图周期；
- 收藏仅保存在当前浏览器的 `localStorage`；
- 图片面板打开后才会通过宿主白名单代理访问 Cataas、Dog CEO、RandomFox、
- 设置通过插件自有的 `/plugins/dsh-pet-corner/api/settings` 读写，不依赖 DSH rc.3
- 插件不需要 API Key。上游不可用或返回非成功状态时，代理会以 HTTP 200 返回

## 📦 Install

```bash
# 已登录私有 npm registry
dsh plugin --profile web add @deepseek-ai/dsh-pet-corner@0.0.1-rc.3

# 本地开发 checkout
dsh plugin --profile web add link:/path/to/dsh-pet-corner
```

## 🚀 Quick Start

```bash
npm install --legacy-peer-deps
DSH_NODE_MODULES=/path/to/dsh-runtime/node_modules npm run setup:dsh-workspace
npm run typecheck
npm test
npm run build
npm pack
```

## 🔗 Links

- [GitHub Repository](https://github.com/omdsh-dev/dsh-pet-corner)
- [Full README](https://github.com/omdsh-dev/dsh-pet-corner#readme)
- [Back to the Plugins list](../plugins.md)
