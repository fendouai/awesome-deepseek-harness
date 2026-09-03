---
title: "dsh-plugin-cost"
description: "Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh)."
keywords: "dsh-plugin-cost, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-plugin-cost

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [yweilai77-dev](https://github.com/yweilai77-dev) | Updated | 2026-08-14 |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | coding |

## One-liner

> Session cost estimate in the DSH Web composer dock (tokenUsage × configurable price table, one-click official-price refresh).

## About

会话费用估算插件，用于 DeepSeek Harness（DSH）Web UI：把 token-meter 的 `tokenUsage` 投影（输入 / 缓存命中 / 缓存写入 / 输出四个桶）乘以可配置的价格表，在聊天输入框下方的统计条旁显示 `费用 ≈ ¥X.XX（估算）`，并提供"刷新价格"按钮手动拉取 DeepSeek 官方最新价格（Windows 更新时间式，平时不联网）。 **适合谁**：想直观了解每次会话大概花了多少钱的 DSH Web 用户；对 token 用量有概念的开发者也能看到四桶拆分（输入/缓存命中/缓存写入/输出）。

## ✨ Key Features

- **DSH 版本**：`0.1.0-rc.6`（web profile，Node.js ≥ 22，实测 Node 24）
- **最后验证日期**：2026-08-15
- **安装方式已验证**：本地目录 / tarball（`pnpm pack`）/ `github:yweilai77-dev/dsh-plugin-cost` 三种均通过 `dsh plugin add` 实测（全新 profile → 启动 → 插件生效）
- 依赖：`@deepseek-ai/cordis`、`@deepseek-ai/dsh-typert-protocol`、`@deepseek-ai/schemastery`（安装时自动从 npm 拉取）

## 📦 Install

```bash
# 1. 安装到你的 profile
dsh plugin --profile web add github:yweilai77-dev/dsh-plugin-cost

# 2. 重启 dsh web
# 3. 打开 Web UI，聊天输入框下方的统计条下会出现：
#    费用 ≈ ¥0.0123（估算）  [刷新价格]
# 4. 点"刷新价格"→ 显示"已更新 HH:MM"（从官方中文价格页拉取最新价）
```

## 🚀 Quick Start

```bash
- id: cost
  name: dsh-plugin-cost
  config:
    prices:
      input: 1.5
      cacheRead: 0.05
      cacheWrite: 1.5
      output: 4.5
      currency: CNY
    fetchUrl: 'https://api-docs.deepseek.com/zh-cn/quick_start/pricing/'
```

## 📚 Learn more

**配置**

插件行 `cost` 的 `config` 可覆盖默认价格表（每百万 tokens）： 在你的 profile 的 `cordis.patch.yml` 里按行 id 覆盖，例如： name: dsh-plugin-cost config: prices: input: 1.5 cacheRead: 0.05 cacheWrite: 1.5 output: 4.5 currency: CNY fetchUrl: 'https://api-docs.deepseek.com/zh-cn/quick_start/pricing/' > 注意：覆盖整行时需重述全部键（补丁替换整行 config，不做深合并）。

## 🔗 Links

- [GitHub Repository](https://github.com/yweilai77-dev/dsh-plugin-cost)
- [Full README](https://github.com/yweilai77-dev/dsh-plugin-cost#readme)
- [Back to the Plugins list](../plugins.md)
