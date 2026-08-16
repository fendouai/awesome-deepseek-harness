---
title: "dsh-web-billing"
description: "DSH Web 中英文金额 Token 计费：官方策略自动定价（含高峰/低谷），逐条消息费用台账。"
keywords: "dsh-web-billing, ui, plugin, observability, deepseek harness, dsh"
---
# dsh-web-billing

> ⭐ 6 · ✅ 活跃 · 插件

## 一句话介绍

DSH Web 中英文金额 Token 计费：官方策略自动定价（含高峰/低谷），逐条消息费用台账。

## 详细介绍

DeepSeek Harness（`dsh web`）的人民币/美元 token 计费插件：**按官方政策自动计价** （内置政策时间表，含 2026-08-17 起的峰谷定价），逐条消息记账，**实时显示账号余额**， 浏览器端展示费用（**界面语言自动切换 ¥/$**）。 - **记账（host 端）**：订阅 `session/event`，对每条带 usage 的 `assistant/message` 按消息时刻取价计费（CNY 与 USD 双币种，官方美元价独立发布），账本持久化到 `$DSH_HOME/storages/web-billing.json`。 - **账号余额（host 端）**：复用 provider 的 API key 调用官方 `GET /user/balance` （默认 60s 刷新、5s 超时、失败静默降级），CNY/USD 双币种随 `/billing/state` 返回。 - **本地模型节省统计**：配置 `localProviders` 后，本地（自托管）模型的调用按官方 价格计算「名义价值」，实际成本按 `localCostPerM`（

## 作者
**[bpc-oss](https://github.com/bpc-oss)**

## 链接

- [GitHub 仓库](https://github.com/bpc-oss/dsh-web-billing)
- [完整 README](https://github.com/bpc-oss/dsh-web-billing#readme)
- [返回dsh-web-billing所在分类](../plugins.md)
