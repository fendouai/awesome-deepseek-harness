---
title: "weshop-dsh-plugin"
description: "Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills."
keywords: "weshop-dsh-plugin, developer, plugin, coding, deepseek harness, dsh"
---
# weshop-dsh-plugin

> ⭐ **12** · ✅ 活跃 · 插件 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 12 | 状态 | ✅ 活跃 |
| 作者 | [weshopai](https://github.com/weshopai) | 更新时间 | 2026-08-20 |

## 一句话介绍

> Native WeShop Cordis plugin for DeepSeek Harness. Allow you to use infinite canvas with infinite creative skills.

## 详细介绍

**An AI visual workspace for e-commerce creation, built into DeepSeek Harness.** Select products, models, or reference images on an infinite canvas. Describe the result you want in natural language, and watch it appear right next to the conversation. [Read the Chinese README](./README.zh-CN.md) · [Get a WeShop API Key](https://www.weshop.ai/apiKey) · [Contact us](mailto:hi@weshop.ai)

## ✨ 核心特性

- Turning a product shot into a clean, on-brand main image or lifestyle scene
- Trying garments and accessories on a model with virtual try-on
- Swapping, extending, or cleaning up backgrounds without leaving the chat
- Batching photography, edits, and short video from a single natural-language brief

## 📦 安装

```bash
npx @deepseek-ai/dsh plugin --profile web add weshop-dsh-plugin
```

## 🚀 快速开始

```bash
npx @deepseek-ai/dsh web
```

## 📚 更多信息

**First installation**

With Harness closed, run one command: npx @deepseek-ai/dsh plugin --profile web add weshop-dsh-plugin This installs WeShop, creates the Harness Web profile when needed, and enables its bundle automatically. No GitHub account, access token, `pnpm` configuration, or manual file editing is required. Then restart Harness: npx @deepseek-ai/dsh web Create or open a task, then choose the **WeShop Canvas*

**Install through dsh-market**

If you use the community plugin market, install it once and restart Harness: dsh plugin --profile web add dshmarket Then open **Settings → Plugin Market**, search for **WeShop**, and install it there.

**⚙️ Configure WeShop OpenAPI**

Open the canvas and select **Configure API Key** in the top bar. The key is saved by the local Harness Host with restricted file permissions and is never returned to the browser, canvas state, or model. You may instead provide the key before starting Harness: export WESHOP_API_KEY="your-key" npx @deepseek-ai/dsh web Get a key from [WeShop OpenAPI](https://www.weshop.ai/apiKey).

## 🔗 链接

- [GitHub 仓库](https://github.com/weshopai/weshop-dsh-plugin)
- [完整 README](https://github.com/weshopai/weshop-dsh-plugin#readme)
- [返回weshop-dsh-plugin所在分类](../plugins.md)
