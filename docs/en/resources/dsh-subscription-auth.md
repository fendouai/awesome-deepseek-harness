---
title: "dsh-subscription-auth"
description: "dsh对接openai、grok、anthropic、kimi订阅渠道"
keywords: "dsh-subscription-auth, developer, integration, coding, deepseek harness, dsh"
---
# dsh-subscription-auth

> ⭐ 4 · ✅ active · integration

## One-liner

dsh对接openai、grok、anthropic、kimi订阅渠道

## About

给 dsh 增加**订阅会员 OAuth 登录**支持（模型提供商按订阅账号登录，而不是 API key）。内置四个订阅渠道： 每个渠道是一个自包含模块（`src/channels/<id>.ts`，实现 `ChannelDefinition` 契约），`src/index.ts` 是薄的通用驱动（遍历渠道定义注册 settings / provider / adapter / 路由）。OAuth 常量与 wire 格式以 omp（`@oh-my-pi/pi-ai`、`@oh-my-pi/pi-catalog`）源码为准。对接方法见内置 skill：`subscription-channel-migration`。

## Author
**[Khellendros97](https://github.com/Khellendros97)**

## Links

- [GitHub Repository](https://github.com/Khellendros97/dsh-subscription-auth)
- [Full README](https://github.com/Khellendros97/dsh-subscription-auth#readme)
- [Back to the MCP & Integrations list](../integrations.md)
