---
title: "dsh-balance-monitor"
description: "Multi-provider AI balance, quota, and token usage for the dsh sidebar, with a daily heatmap."
keywords: "dsh-balance-monitor, ui, plugin, coding, deepseek harness, dsh"
---
# dsh-balance-monitor

> ⭐ **10** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | UI & experience |
| Stars | ⭐ 10 | Status | ✅ active |
| Author | [jelly-000](https://github.com/jelly-000) | Updated | — |
| Subcategory | 🖥️ Sidebars & panels | Capabilities | coding, ui |

## One-liner

> Multi-provider AI balance, quota, and token usage for the dsh sidebar, with a daily heatmap.

## About

dsh-balance-monitor 是一个 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh) 插件，在侧边栏底部集中展示多个 AI 平台的余额、配额与用量，并提供基于本地会话日志的 Token 热力图看板。 插件按厂商逐行堆叠，每行展示剩余额度、剩余比例条、已用量与当日支出。同一厂商同时提供 Coding Plan（订阅套餐）与 API 按量两种计费方式时，可通过行内的模式圆点在两种口径之间切换；厂商未开放余额或计费接口时，自动退化为 DSH 本地实测用量。界面样式基于官方设计令牌，力求克制内敛。

## 📦 Install

```bash
dsh plugin --profile web add "github:<you>/dsh-balance-monitor#main"
```

## 🚀 Quick Start

```bash
{
  "deepseek:api": { "date": "2026-08-27", "dayStart": 100.0, "lastTotal": 99.5, "spent": 0.5, "updatedAt": 1755200000000 },
  "zhipu:coding": { "date": "2026-08-27", "dayStart": 500, "lastTotal": 372, "spent": 128, "updatedAt": 1755200000000 }
}
```

## 📚 Learn more

**配置密钥**

无需额外配置文件：配置了密钥的厂商会被自动展示，DSH 已接入的 provider 也会自动补入。密钥先读取环境变量，否则读取 `$DSH_HOME/.credentials.yaml`：

**可选配置**

{ "platforms": { "zhipu": { "label": "智谱GLM", "enabled": true, "mode": "coding" }, "deepseek": { "enabled": false } }, "custom": [ { "id": "custom-mygateway", "label": "我的网关", "baseUrl": "https://gw.example.com", "path": "/v1/user/balance", "auth": "bearer", "kind": "balance", "currency": "CNY", "pick": { "remaining": "balance", "total": "total_balance", "resetAt": "" } } ] }

**安装**

浏览器端 bundle 为手写 classic script，无构建步骤： dsh plugin --profile web add "github:<you>/dsh-balance-monitor#main" 完成后重启 Web UI（`dsh --profile web`）。修改 `lib/client.js` 后刷新页面即可生效；修改 `lib/index.js` / `providers.js` / `usage.js` 需重启 dsh。

**工作原理**

每日基线账本（`$DSH_HOME/storages/balance-monitor.json`）按 `平台id:模式` 记账，切换模式不会污染彼此的「当日已用」： { "deepseek:api": { "date": "2026-08-27", "dayStart": 100.0, "lastTotal": 99.5, "spent": 0.5, "updatedAt": 1755200000000 }, "zhipu:coding": { "date": "2026-08-27", "dayStart": 500, "lastTotal": 372, "spent": 128, "updatedAt": 1755200000000 } }

## 🔗 Links

- [GitHub Repository](https://github.com/jelly-000/dsh-balance-monitor)
- [Full README](https://github.com/jelly-000/dsh-balance-monitor#readme)
- [Back to the Plugins list](../plugins.md)
