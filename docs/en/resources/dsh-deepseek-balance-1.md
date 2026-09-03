---
title: "dsh-deepseek-balance"
description: "DeepSeek Harness bundle plugin: shows your DeepSeek account balance in the web sidebar footer, above Settings."
keywords: "dsh-deepseek-balance, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-deepseek-balance

> ⭐ **2** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 2 | Status | ✅ active |
| Author | [Choi-Peng](https://github.com/Choi-Peng) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> DeepSeek Harness bundle plugin: shows your DeepSeek account balance in the web sidebar footer, above Settings.

## About

A DeepSeek Harness plugin that shows your [DeepSeek API balance](https://api-docs.deepseek.com/zh-cn/api/get-user-balance) in the **web UI, pinned above the Settings button** at the sidebar foot.

## ✨ Key Features

- **Balance widget above Settings** — renders `total_balance` followed by the currency (e.g. `110.00 CNY`) in the sidebar foot, directly above the Settings trigge
- **Hover details** — hovering the widget opens an animated popover with the full balance information:
- **Configurable color** — a developer/user setting (Settings → 余额/Balance) changes the balance text and popover accent color; color changes animate smoothly.
- **Manual refresh** — a refresh button (with a spin animation) fetches the latest balance on demand; an optional auto-refresh interval can be enabled in settings
- **Transition animations** — popover fade/scale, value-change slide/fade, color transitions, refresh spin.
- **API key stays server-side** — the browser never sees the key. The host half proxies `GET <baseURL>/user/balance` and returns only public balance fields.

## 📦 Install

```bash
# from the profile directory
dsh plugin --profile web add dsh-deepseek-balance --link <path-to-this-package>
```

## 🚀 Quick Start

```bash
- insert:
       - id: dsh-deepseek-balance
         name: 'dsh-deepseek-balance'
```

## 📚 Learn more

**快速使用 Quick start**

1. 安装插件到 web profile（见下方「Installation」）并重启 `dsh web`。 2. 打开 **Settings → 余额 (Balance)**，填入你的 DeepSeek API Key（或在环境变量 `DEEPSEEK_API_KEY` / Models 页面里配置，见「API key resolution」）。 3. 点 **检查余额 (Check balance)** —— 显示 `Connection OK: <金额> <货币>` 即成功。 4. 侧边栏底部（设置按钮上方）随即出现余额小部件：**悬停**查看货币 / 总余额 / 赠金 / 充值详情，点**刷新**按钮手动刷新，也可在设置页开启自动刷新间隔与主题色。

**Installation**

The plugin ships as a normal out-of-tree dsh plugin package (host half + browser half). Install it into the `web` profile:

**Configuration**

All settings live under the `dsh-deepseek-balance:` section in `$DSH_HOME/settings.yaml`, or in the **Settings → 余额 (Balance)** page:

## 🔗 Links

- [GitHub Repository](https://github.com/Choi-Peng/dsh-deepseek-balance)
- [Full README](https://github.com/Choi-Peng/dsh-deepseek-balance#readme)
- [Back to the Plugins list](../plugins.md)
