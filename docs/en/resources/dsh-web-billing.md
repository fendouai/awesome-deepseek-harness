---
title: "dsh-web-billing"
description: "RMB/USD token billing for the DSH web: official-policy auto pricing with peak/off-peak hours and per-message cost ledger."
keywords: "dsh-web-billing, ui, plugin, observability, deepseek harness, dsh"
---
# dsh-web-billing

> ⭐ 6 · ✅ active · plugin

## One-liner

RMB/USD token billing for the DSH web: official-policy auto pricing with peak/off-peak hours and per-message cost ledger.

## About

DeepSeek Harness（`dsh web`）的人民币/美元 token 计费插件：**按官方政策自动计价** （内置政策时间表，含 2026-08-17 起的峰谷定价），逐条消息记账，**实时显示账号余额**， 浏览器端展示费用（**界面语言自动切换 ¥/$**）。 - **记账（host 端）**：订阅 `session/event`，对每条带 usage 的 `assistant/message` 按消息时刻取价计费（CNY 与 USD 双币种，官方美元价独立发布），账本持久化到 `$DSH_HOME/storages/web-billing.json`。 - **账号余额（host 端）**：复用 provider 的 API key 调用官方 `GET /user/balance` （默认 60s 刷新、5s 超时、失败静默降级），CNY/USD 双币种随 `/billing/state` 返回。 - **本地模型节省统计**：配置 `localProviders` 后，本地（自托管）模型的调用按官方 价格计算「名义价值」，实际成本按 `localCostPerM`（

## Author
**[bpc-oss](https://github.com/bpc-oss)**

## Links

- [GitHub Repository](https://github.com/bpc-oss/dsh-web-billing)
- [Full README](https://github.com/bpc-oss/dsh-web-billing#readme)
- [Back to the Plugins list](../plugins.md)
