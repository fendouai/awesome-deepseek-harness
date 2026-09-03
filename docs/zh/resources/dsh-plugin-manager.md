---
title: "dsh-plugin-manager"
description: "DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停写入全局层补丁并实时热生效，备注保存到本地覆盖文件长期生效。"
keywords: "dsh-plugin-manager, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-manager

> ⭐ **6** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 6 | 状态 | ✅ 活跃 |
| 作者 | [2768651338](https://github.com/2768651338) | 更新时间 | 2026-08-17 |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> DeepSeek Harness 的图形化插件管理插件：在 设置 → 插件 里新增「插件管家」标签页，用中文名和说明展示每个插件是做什么的，并提供一键启停开关与内置备注编辑——启停写入全局层补丁并实时热生效，备注保存到本地覆盖文件长期生效。

## 详细介绍

**Settings → Plugins → Plugin Manager** · 165 plugins cataloged, one click to toggle, notes edited in place. [Overview](#overview) · [Compatibility](#compatibility) · [Install / Uninstall](#install--uninstall) · [Quick Start](#quick-start) · [Configuration](#configuration) · [Permissions & Data](#permissions--data) · [Features](#features) · [Troubleshooting](#troubleshooting) · [Development](#development) [**中文**](docs/lang/README_ZH.md) · [**Español**](docs/lang/README_ES.md) · [**日本語**](docs/lang/README_JA.md) · [**Deutsch**](docs/lang/README_DE.md) · [**Русский**](docs/lang/README_RU.md) · [**Português**](docs/lang/README_PT.md) · [**한국어**](docs/lang/README_KO.md) --- ---

## 📦 安装

```bash
# 1. Install
dsh plugin --profile web add github:2768651338/dsh-plugin-manager#main
# 2. Restart DeepSeek Harness, press Ctrl+F5 in the web page
```

## 🚀 快速开始

```bash
{
  "@dsh-external/dsh-navbar": { "name": "对话导航条", "desc": "对话区右缘的消息节点导航" }
}
```

## 🔗 链接

- [GitHub 仓库](https://github.com/2768651338/dsh-plugin-manager)
- [完整 README](https://github.com/2768651338/dsh-plugin-manager#readme)
- [返回dsh-plugin-manager所在分类](../plugins.md)
