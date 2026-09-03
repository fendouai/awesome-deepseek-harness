---
title: "dsh-plugin-anti-ads"
description: "DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin"
keywords: "dsh-plugin-anti-ads, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-anti-ads

> ⭐ **10** · ✅ 活跃 · 插件 · 近期 ⬆️ +3

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 10 | 状态 | ✅ 活跃 |
| 作者 | [HuanLinOTO](https://github.com/HuanLinOTO) | 更新时间 | 2026-08-15 |

## 一句话介绍

> DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin

## 详细介绍

给 DSH Web UI 安装的广告拦截器——拦截对象只有 [dsh-ads](https://github.com/dsh-external/dsh-ads) 一个。右下角一枚小徽章，广告没了，徽章记着拦掉了几个弹层。

## 📦 安装

```bash
# 从 npm 安装（推荐）：
dsh plugin --profile web add @huanlin/dsh-plugin-anti-ads

# 从本地 clone 开发安装：
dsh plugin --profile web add link:/path/to/dsh-anti-ads
# 重启 dsh web，刷新页面
```

## 🚀 快速开始

```bash
pnpm install          # devDeps 用 link: 指向本机 ~/.dsh/source/current
pnpm run typecheck    # 类型门禁（tsconfig.json + tsconfig.client.json）
pnpm test             # vitest 全量（3 个 spec，54 个用例）
pnpm run build        # tsdown 双 bundle：lib/index.js（node stub）+ lib/client.js（浏览器半）
```

## 🔗 链接

- [GitHub 仓库](https://github.com/HuanLinOTO/dsh-plugin-anti-ads)
- [完整 README](https://github.com/HuanLinOTO/dsh-plugin-anti-ads#readme)
- [返回dsh-plugin-anti-ads所在分类](../plugins.md)
