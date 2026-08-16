---
title: "tokenledger"
description: "Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing"
keywords: "tokenledger, vision, plugin, coding, deepseek harness, dsh"
---
# tokenledger

> ⭐ 3 · ✅ active · plugin

## One-liner

Token usage accounting for DeepSeek Harness, reconciled against New API and Sub2API relay-site billing

## About

**统计 DeepSeek Harness 的 Token 消耗，并归属到实际服务这次请求的中转站——不用配置，不用凭据。** 用量统计本身在 DSH 生态里已经有几十个实现。TokenLedger 的差别是**按站点身份而不是按路由名归属**——它读 provider 的 baseURL，按 origin 分组，所以同一个中转站上的多把 key 会合并成一行、对应你收到的那一张账单，站名就是域名而不是你自己起的路由别名。

## Author
**[zh667](https://github.com/zh667)**

## Links

- [GitHub Repository](https://github.com/zh667/TokenLedger)
- [Full README](https://github.com/zh667/TokenLedger#readme)
- [Back to the Plugins list](../plugins.md)
