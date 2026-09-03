---
title: "dsh-view-modes"
description: "Verbose/Normal/Summary 三种输出模式，工具调用与思考语义分组。"
keywords: "dsh-view-modes, ui, plugin, deepseek harness, dsh"
---
# dsh-view-modes

> ⭐ **2** · ✅ 活跃 · 插件 · 近期 ⬆️ +1

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 界面与体验 |
| 星数 | ⭐ 2 | 状态 | ✅ 活跃 |
| 作者 | [NigelYao](https://github.com/NigelYao) | 更新时间 | 2026-08-13 |

## 一句话介绍

> Verbose/Normal/Summary 三种输出模式，工具调用与思考语义分组。

## 详细介绍

**English** · [简体中文](./README.zh-CN.md) Three output modes for DeepSeek Harness (DSH) Web: Verbose, Normal, and Summary. Keep the full trace when debugging, reduce process noise during daily work, or focus on the result. This is an official-style DSH bundle plugin (`dsh.bundle` + `dsh.client`). It changes only browser-side presentation and does not patch DSH core files.

## 📦 安装

```bash
dsh plugin --profile web add git+https://github.com/NigelYao/dsh-view-modes.git
```

## 🚀 快速开始

```bash
$pluginRoot = Join-Path $env:USERPROFILE ".dsh\local-plugins\dsh-view-modes"
git clone https://github.com/NigelYao/dsh-view-modes.git $pluginRoot
Set-Location $pluginRoot
dsh plugin --profile web add link:$pluginRoot
```

## 📚 更多信息

**Public GitHub install (recommended)**

No npm account is required: dsh plugin --profile web add git+https://github.com/NigelYao/dsh-view-modes.git

## 🔗 链接

- [GitHub 仓库](https://github.com/NigelYao/dsh-view-modes)
- [完整 README](https://github.com/NigelYao/dsh-view-modes#readme)
- [返回dsh-view-modes所在分类](../plugins.md)
