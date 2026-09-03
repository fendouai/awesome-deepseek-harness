---
title: "dsh-subscription-auth"
description: "dsh对接openai、grok、anthropic、kimi订阅渠道"
keywords: "dsh-subscription-auth, developer, integration, coding, deepseek harness, dsh"
---
# dsh-subscription-auth

> ⭐ **5** · ✅ active · integration · ⬆️ +1 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 5 | Status | ✅ active |
| Author | [Khellendros97](https://github.com/Khellendros97) | Updated | 2026-08-15 |

## One-liner

> dsh对接openai、grok、anthropic、kimi订阅渠道

## About

给 dsh 增加**订阅会员 OAuth 登录**支持（模型提供商按订阅账号登录，而不是 API key）。内置四个订阅渠道： 每个渠道是一个自包含模块（`src/channels/.ts`，实现 `ChannelDefinition` 契约），`src/index.ts` 是薄的通用驱动（遍历渠道定义注册 settings / provider / adapter / 路由）。OAuth 常量与 wire 格式以 omp（`@oh-my-pi/pi-ai`、`@oh-my-pi/pi-catalog`）源码为准。对接方法见内置 skill：`subscription-channel-migration`。

## 📦 Install

```bash
dsh plugin --profile web add dsh-subscription-auth
```

## 🚀 Quick Start

```bash
- insert:
       - id: dsh-subscription-auth
         name: dsh-subscription-auth
```

## 📚 Learn more

**安装**

**前置**：已装好 DSH（`dsh web` 能正常运行），Node.js ≥ 20，`pnpm` 可用（`dsh plugin add` 内部使用；没有的话先 `npm install -g pnpm`）。

**标准安装（npm 发布，推荐）**

插件以 npm 包 `dsh-subscription-auth` 发布，包内声明了 `dsh.bundle.patch`（随包的 `cordis.patch.yml`）：CLI 安装后会自动注册进 profile 的 `dsh.profile.bundles`，下次启动即挂载——**一条命令完成安装与挂载，无需手改任何配置文件**： dsh plugin --profile web add dsh-subscription-auth 装完**重启 dsh** 并**硬刷新浏览器**（Cmd/Ctrl+Shift+R）。 > 若报 `minimum release age`（发布不足 24h 的新版本）：等 24h，或直接重跑一次上面的命令（pnpm 会自动补 `minimumReleaseAgeExclude` 放行）。 **更新**： dsh plugin --profile web 

**源码安装 / 开发（可选，替代 npm 方式）**

调试本地改动或跟随开发分支时使用（**仅在未通过 npm 通道安装时使用**，否则会与 npm 版双挂载）： 1. git clone https://github.com/Khellendros97/dsh-subscription-auth.git cd dsh-subscription-auth && bun scripts/build-bun.mjs # 递归转译 src → lib 2. 依赖解析：把 running dsh 的依赖指进来（Windows 示例）： cmd /c mklink /J "$HOME\dsh-plugins\dsh-subscription-auth\node_modules" "<dsh 安装目录>\node_modules\@deepseek-ai\dsh\node_modules" 3. 注册到插件锚点： cmd /c mklink /J "$H

**使用**

1. 打开 **设置 → 订阅服务**：列出四个订阅提供商，显示登录状态、账号与可用模型（折叠列表）。 2. 点「登录」： - **ChatGPT / Claude**：浏览器自动打开授权页 → 登录并授权 → 跳回 localhost 回调 → 页面轮询到「已登录」→ 自动拉取官方模型列表。 - **Grok / Kimi**：页面显示验证链接 + 设备授权码 → 在浏览器打开链接并输入代码 → 页面轮询到「已登录」→ 自动拉取模型列表。 3. 在模型选择里切到对应的提供商（如「Claude (订阅)」），选一个模型即可对话。 模型选择器可为订阅模型选择**思考强度（推理等级）**： - ChatGPT：`minimal / low / medium / high`（默认 `medium`，作为 codex Responses 的 `reasoning.effort` 发送） - Cla

## 🔗 Links

- [GitHub Repository](https://github.com/Khellendros97/dsh-subscription-auth)
- [Full README](https://github.com/Khellendros97/dsh-subscription-auth#readme)
- [Back to the MCP & Integrations list](../integrations.md)
