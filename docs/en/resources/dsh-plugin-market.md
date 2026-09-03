---
title: "dsh-plugin-market"
description: "Plugin marketplace for DeepSeek Harness Web settings: install, update and remove plugins across any local profile."
keywords: "dsh-plugin-market, registry, awesome-list, coding, deepseek harness, dsh"
---
# dsh-plugin-market

> ⭐ **9** · ✅ active · awesome-list

| | | | |
|---|---|---|---|
| Type | awesome-list | Category | Registries |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [springbrand-lab](https://github.com/springbrand-lab) | Updated | — |

## One-liner

> Plugin marketplace for DeepSeek Harness Web settings: install, update and remove plugins across any local profile.

## About

在 DeepSeek Harness「设置 → 插件」里发现、确认并安装社区插件；另有公开目录站供浏览与复制安装命令。 公开浏览：[https://dsh-plugin-market.vercel.app](https://dsh-plugin-market.vercel.app)

## ✨ Key Features

- 设置内「插件市场」Tab：搜索、分类、展开说明、确认后安装 / 卸载
- 安装走官方 `dsh plugin add/remove`，不执行第三方安装脚本
- 公开目录站：浏览、⌘K 搜索、中英 / 亮暗主题、复制安装命令
- 对话 Agent 工具：搜索、详情、安装、列出已装插件

## 📦 Install

```bash
dsh plugin --profile web add github:chnjames/dsh-plugin-market
# 或
npx @deepseek-ai/dsh plugin --profile web add github:chnjames/dsh-plugin-market
```

## 🚀 Quick Start

```bash
dsh plugin --profile web remove dsh-plugin-market
```

## 📚 Learn more

**使用**

设置内卡片： 1. 标题行：名称 · 星标 · 展开 2. 简介（最多两行） 3. 底栏：已安装 / 作者 / 提示 · **查看仓库** · **安装**（安装前确认） 卸载本市场插件： dsh plugin --profile web remove dsh-plugin-market

**配置**

常用项（写入 `cordis.patch.yml` 中本插件的 `config`）： 完整默认块见 [`cordis.yml`](cordis.yml)。 <details> <summary>完整配置示例</summary> - id: plugin-market name: dsh-plugin-market config: catalog: fallbackToSearch: true # urls: ["https://your-domain/registry.json"] sources: github: enabled: true topic: "dsh-plugin" npm: enabled: true keyword: "dsh-plugin" cache: ttl: 21600 autoRefresh: true refreshInterval: 21600 ui: s

## 🔗 Links

- [GitHub Repository](https://github.com/springbrand-lab/dsh-plugin-market)
- [Full README](https://github.com/springbrand-lab/dsh-plugin-market#readme)
- [Back to the Awesome Lists & Registries list](../awesome-lists.md)
