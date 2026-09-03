---
title: "dsh-pet-corner"
description: "DSH Pet Corner: a floating pet, keyless pet-image proxy, favorites, and plugin-owned settings API"
keywords: "dsh-pet-corner, ui, plugin, coding, multimodal, deepseek harness, dsh"
---
# dsh-pet-corner

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [omdsh-dev](https://github.com/omdsh-dev) | 更新时间 | — |
| 子分类 | 🐋 桌面宠物 | 能力 | coding, multimodal |

## 一句话介绍

> DSH Pet Corner: a floating pet, keyless pet-image proxy, favorites, and plugin-owned settings API

## 详细介绍

**Author / Maintainer:** [@Zacklinkk](https://github.com/Zacklinkk) DSH 的轻量摸鱼角：右下角是一只可拖动的小猫，点击后可浏览猫、狗和狐狸图片、 猫咪知识与收藏。所有第三方请求都先经过宿主白名单代理，浏览器不会直接访问外站。

## ✨ 核心特性

- 小猫挂件、来源开关、默认狗狗品种和自动换图周期；
- 收藏仅保存在当前浏览器的 `localStorage`；
- 图片面板打开后才会通过宿主白名单代理访问 Cataas、Dog CEO、RandomFox、
- 设置通过插件自有的 `/plugins/dsh-pet-corner/api/settings` 读写，不依赖 DSH rc.3
- 插件不需要 API Key。上游不可用或返回非成功状态时，代理会以 HTTP 200 返回

## 📦 安装

```bash
# 已登录私有 npm registry
dsh plugin --profile web add @deepseek-ai/dsh-pet-corner@0.0.1-rc.3

# 本地开发 checkout
dsh plugin --profile web add link:/path/to/dsh-pet-corner
```

## 🚀 快速开始

```bash
npm install --legacy-peer-deps
DSH_NODE_MODULES=/path/to/dsh-runtime/node_modules npm run setup:dsh-workspace
npm run typecheck
npm test
npm run build
npm pack
```

## 🔗 链接

- [GitHub 仓库](https://github.com/omdsh-dev/dsh-pet-corner)
- [完整 README](https://github.com/omdsh-dev/dsh-pet-corner#readme)
- [返回dsh-pet-corner所在分类](../plugins.md)
