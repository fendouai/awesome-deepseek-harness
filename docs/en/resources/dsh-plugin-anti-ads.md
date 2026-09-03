---
title: "dsh-plugin-anti-ads"
description: "DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin"
keywords: "dsh-plugin-anti-ads, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-anti-ads

> ⭐ **10** · ✅ active · plugin · ⬆️ +3 recently

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [HuanLinOTO](https://github.com/HuanLinOTO) | Updated | 2026-08-15 |

## One-liner

> DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin

## About

给 DSH Web UI 安装的广告拦截器——拦截对象只有 [dsh-ads](https://github.com/dsh-external/dsh-ads) 一个。右下角一枚小徽章，广告没了，徽章记着拦掉了几个弹层。

## 📦 Install

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-anti-ads

# 从本地 clone 开发安装：
dsh plugin --profile web add link:/path/to/dsh-anti-ads
# 重启 dsh web，刷新页面
```

## 🚀 Quick Start

```bash
pnpm install          # devDeps 用 link: 指向本机 ~/.dsh/source/current
pnpm run typecheck    # 类型门禁（tsconfig.json + tsconfig.client.json）
pnpm test             # vitest 全量（3 个 spec，54 个用例）
pnpm run build        # tsdown 双 bundle：lib/index.js（node stub）+ lib/client.js（浏览器半）
```

## 🔗 Links

- [GitHub Repository](https://github.com/HuanLinOTO/dsh-plugin-anti-ads)
- [Full README](https://github.com/HuanLinOTO/dsh-plugin-anti-ads#readme)
- [Back to the Plugins list](../plugins.md)
