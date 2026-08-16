---
title: "dsh-subscription-auth"
description: "dsh对接openai、grok、anthropic、kimi订阅渠道"
keywords: "dsh-subscription-auth, developer, integration, coding, deepseek harness, dsh"
---
# dsh-subscription-auth

> ⭐ 4 · ✅ 活跃 · 集成

## 一句话介绍

dsh对接openai、grok、anthropic、kimi订阅渠道

## 详细介绍

给 dsh 增加**订阅会员 OAuth 登录**支持（模型提供商按订阅账号登录，而不是 API key）。内置四个订阅渠道： 每个渠道是一个自包含模块（`src/channels/<id>.ts`，实现 `ChannelDefinition` 契约），`src/index.ts` 是薄的通用驱动（遍历渠道定义注册 settings / provider / adapter / 路由）。OAuth 常量与 wire 格式以 omp（`@oh-my-pi/pi-ai`、`@oh-my-pi/pi-catalog`）源码为准。对接方法见内置 skill：`subscription-channel-migration`。

## 作者
**[Khellendros97](https://github.com/Khellendros97)**

## 链接

- [GitHub 仓库](https://github.com/Khellendros97/dsh-subscription-auth)
- [完整 README](https://github.com/Khellendros97/dsh-subscription-auth#readme)
- [返回dsh-subscription-auth所在分类](../integrations.md)
