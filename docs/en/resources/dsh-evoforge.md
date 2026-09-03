---
title: "dsh-evoforge"
description: "Evidence-driven, cache-stable extensions for DeepSeek Harness"
keywords: "dsh-evoforge, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-evoforge

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Vision & multimodal |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [deepseek-harness-evoforge](https://github.com/deepseek-harness-evoforge) | Updated | 2026-08-21 |
| Subcategory | 👁️ Vision tools | Capabilities | coding |

## One-liner

> Evidence-driven, cache-stable extensions for DeepSeek Harness

## About

EvoForge 是一组安装到 [DeepSeek Harness（DSH）](https://github.com/deepseek-ai/deepseek-harness) 的原生插件。它把常驻渠道、可追踪的内部经验进化、软件交付和统一 Web 控制面接到 DSH 的 Bundle、Cordis、Agent、Session、Goal、Skill、Tool、Approval、Jobs 和 Workspace 上。 DSH 仍然是唯一的 Agent Host 和状态权威。EvoForge 不是 Codex 插件，不 fork DSH，不另造 Session、Goal、Agent Runtime、Scheduler、权限系统或插件市场。

## 📦 Install

```bash
pnpm install --frozen-lockfile
pnpm run pack:suite -- --suite core --out ./dist/evoforge-packs
dsh plugin --profile web add ./dist/evoforge-packs/core/*.tgz
dsh --profile web --dump-config
```

## 🚀 Quick Start

```bash
pnpm run pack:suite -- --suite channels --channel feishu --out ./dist/evoforge-packs
dsh plugin --profile web add ./dist/evoforge-packs/channels-feishu/*.tgz

pnpm run pack:suite -- --suite delivery --out ./dist/evoforge-packs
dsh plugin --profile web add ./dist/evoforge-packs/delivery/*.tgz
```

## 📚 Learn more

**安装**

先准备 Node.js 22.19+、pnpm 11，并安装与本项目匹配的 DSH alpha.5。然后在本仓库执行： pnpm install --frozen-lockfile pnpm run pack:suite -- --suite core --out ./dist/evoforge-packs dsh plugin --profile web add ./dist/evoforge-packs/core/*.tgz dsh --profile web --dump-config 按需安装渠道或交付能力： pnpm run pack:suite -- --suite channels --channel feishu --out ./dist/evoforge-packs dsh plugin --profile web add ./dist/evoforge-packs/ch

**第一次使用飞书**

安装 `channels` 后，在同一个 DSH profile 启用 Gateway 和 `dsh-feishu`，并通过环境变量提供飞书 App ID/Secret。Gateway 是常驻 Host：Adapter 启动即连接，陌生用户在飞书私聊机器人发送任意消息后，会先收到一次性配对码；首条消息不会进入 Agent。管理员在 DSH Web 的“控制台 → 渠道”页面批准待处理请求，用户发送下一条消息即可进入绑定的原生 DSH Session，不需要 Session 命令、不需要打开第二个网页、不需要重启。 飞书配置、最小权限内容读取、撤销和故障语义见 [`dsh-feishu` 用户文档](packages/dsh-feishu/README.md)；Gateway 的路由、持久投递和配对边界见 [`dsh-gateway` 用户文档](packages/dsh-gateway/R

**设计与证据**

欢迎通过 Issue 或 Pull Request 提交可复现的 DSH revision、测试结果和用户体验反馈。请不要在 Issue 中提交飞书 App Secret、访问令牌或真实消息内容。

## 🔗 Links

- [GitHub Repository](https://github.com/deepseek-harness-evoforge/dsh-evoforge)
- [Full README](https://github.com/deepseek-harness-evoforge/dsh-evoforge#readme)
- [Back to the Plugins list](../plugins.md)
