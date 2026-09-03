---
title: "dsh-plugin-radar"
description: "Find DSH plugins by asking in plain language, then security-scan them before install"
keywords: "dsh-plugin-radar, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-radar

> ⭐ **2** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [dshplugin-me](https://github.com/dshplugin-me) | 更新时间 | 2026-08-16 |
| 子分类 | 🎨 皮肤与主题 | 能力 | coding, ui |

## 一句话介绍

> Find DSH plugins by asking in plain language, then security-scan them before install

## 详细介绍

**Find · Vet · Install — DSH plugins, with a security scan before anything touches your profile.** Ask DSH *"is there a plugin that can…"* and this plugin searches the live [`dsh-plugin` GitHub topic](https://github.com/topics/dsh-plugin) with server-side keyword filtering, cross-checks candidates against two curated registries, then runs a **pre-install security scan** — lifecycle scripts, external domains, subprocesses, credential reads, prompt injection — reports findings either way, and only installs after you say go. It also works in reverse: already eyeing a plugin? Ask *"is XX safe to install?"* and it runs the same checklist and hands you the report.

## 📦 安装

```bash
dsh plugin --profile web add 'github:dshplugin-me/dsh-plugin-radar#v0.1.1'
```

## 🚀 快速开始

```bash
dsh --profile web --dump-config   # shows a "# == dsh-plugin-radar" layer
dsh --profile web
```

## 🔗 链接

- [GitHub 仓库](https://github.com/dshplugin-me/dsh-plugin-radar)
- [完整 README](https://github.com/dshplugin-me/dsh-plugin-radar#readme)
- [返回dsh-plugin-radar所在分类](../plugins.md)
