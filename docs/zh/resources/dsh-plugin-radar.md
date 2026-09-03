---
title: "dsh-plugin-radar"
description: "Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works"
keywords: "dsh-plugin-radar, vision, plugin, coding, git, deepseek harness, dsh"
---
# dsh-plugin-radar

> ⭐ **1** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 1 | 状态 | ✅ 活跃 |
| 作者 | [DshMarketPlace](https://github.com/DshMarketPlace) | 更新时间 | 2026-08-20 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding, git |

## 一句话介绍

> Userscript: marks DeepSeek Harness plugins on GitHub and npm, with the install command that actually works

## 详细介绍

`dsh plugin add` is a thin forward to pnpm inside a profile directory, so `--profile` is **mandatory**: $ dsh plugin add some-plugin error: required option '--profile ' not specified Plenty of READMEs print the short form anyway. This script reads the command from the [DSH Marketplace](https://dshmarketplace.dev) catalogue, where every listing carries the flag, and drops it on the page you are already looking at.

## 📦 安装

```bash
$ dsh plugin add some-plugin
error: required option '--profile <name>' not specified
```

## 🚀 快速开始

```bash
{
  "fields": ["fullName", "category", "install", "path", "npm"],
  "plugins": [
    ["liustack/modlens", "vision", "dsh plugin --profile web add @liustack/modlens", "/plugins/liustack-modlens", "@liustack/modlens"]
  ]
}
```

## 📚 更多信息

**Install**

1. Install a userscript manager — [Tampermonkey](https://www.tampermonkey.net/), [Violentmonkey](https://violentmonkey.github.io/) or [Userscripts](https://apps.apple.com/app/userscripts/id1463298887) for Safari. 2. **[Install from Greasy Fork](https://greasyfork.org/scripts/591735-dsh-plugin-radar)**, or open [`dsh-plugin-radar.user.js`](dsh-plugin-radar.user.js) raw and your manager will offer t

## 🔗 链接

- [GitHub 仓库](https://github.com/DshMarketPlace/dsh-plugin-radar)
- [完整 README](https://github.com/DshMarketPlace/dsh-plugin-radar#readme)
- [返回dsh-plugin-radar所在分类](../plugins.md)
