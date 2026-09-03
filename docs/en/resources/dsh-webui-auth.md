---
title: "dsh-webui-auth"
description: "WebUI 身份认证：HTTP/传输层强制登录（资源、插件 bundle、/api、WebSocket 四层防护），服务端会话 + HttpOnly Cookie。"
keywords: "dsh-webui-auth, search, plugin, coding, ui, deepseek harness, dsh"
---
# dsh-webui-auth

> ⭐ **9** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Search & research |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [Yuuz12](https://github.com/Yuuz12) | Updated | — |
| Subcategory | 🌐 Web search | Capabilities | coding, ui |

## One-liner

> WebUI 身份认证：HTTP/传输层强制登录（资源、插件 bundle、/api、WebSocket 四层防护），服务端会话 + HttpOnly Cookie。

## About

[English](README.en.md) | 中文 DSH WebUI 身份认证插件（持久化插件）。在「设置 → 身份认证」或首次访问登录页创建账号密码后，**未认证的浏览器无法加载 WebUI 的任何资源、调用任何接口或建立任何实时连接**——认证在 HTTP/传输层强制执行，不可通过浏览器开发者工具绕过。

## ✨ Key Features

- **不修改核心包**：dsh 升级不会覆盖补丁、不会产生「升级后 /api 裸奔」的窗口。插件每次启动对路由表重做包装，并用 2s→10s 重扫捕获晚注册路由。**v0.1.2-alpha.2 及更新核心的事件流 WebSocket 位于 `/api/remote.mux`（由 dsh-api-gateway 注册），
- **fail-closed**：若预期路由缺失（dsh 内部结构变化导致包装不上），`setup`/`configure` 会**拒绝启用认证**，并在宿主日志与设置页同时报错——宁可不可用，不可「开了登录却裸奔 /api」。
- **与核心自带浏览器认证（v0.1.2-alpha.2+）协作**：该版本核心自带 launch-token 交换的签名 Cookie（`dsh-auth-*`）认证 `/` 与 `/api`。插件登录成功后自动把浏览器引导到核心的带 token 根 URL 完成核心 Cookie 交换；`/api` 请求在插件会话校
- **反代/局域网旧核心下的特权方法**（≤alpha.1）：已认证请求由插件在会话校验后以「回环形状」转交核心，使核心中**回环钉死的特权方法**（settings/credentials/agentPreset/llm.discoverModels）在反代部署下可用——会话 Cookie 闸门是比 Host 启发式更
- **WebSocket 与 trustedHosts**：WS 升级握手仍受核心自身 `requestRejection` / `isTrustedApiRequest` 限制，因此**反代/局域网（非回环 Host）部署下，WS 下行需要同时在 dsh 配置中把对外域名加入 `client-connection.tr

## 📦 Install

```bash
npx @deepseek-ai/dsh plugin --profile web add dsh-webui-auth
```

## 🚀 Quick Start

```bash
npx @deepseek-ai/dsh plugin --profile web add github:Yuuz12/dsh-webui-auth
```

## 📚 Learn more

**安装**

本插件是标准**组合包（bundle）**，已发布到 npm，推荐用 DSH 官方 `plugin` 命令安装；手动方式保留作备用。前提：机器上有 pnpm（Node 自带 corepack，执行 `corepack enable pnpm` 即可启用）。

**方式一：npm 安装（推荐）**

npx @deepseek-ai/dsh plugin --profile web add dsh-webui-auth 从 npm registry 拉取预构建代码（纯 JS 包，无 prepare 脚本、无需构建授权），加入依赖并追加到 `dsh.profile.bundles` 列表，插件行随组合包层自动插入。

**方式二：GitHub 安装**

npx @deepseek-ai/dsh plugin --profile web add github:Yuuz12/dsh-webui-auth 拉取仓库源码（同样直接可用，无需构建步骤）；网络不佳时优先用方式一。

**方式一：`dsh plugin` 命令（对应方式一安装）**

1. `npx @deepseek-ai/dsh plugin --profile web remove dsh-webui-auth`（同时移除依赖与组合包层） 2. 重启 DSH

## 🔗 Links

- [GitHub Repository](https://github.com/Yuuz12/dsh-webui-auth)
- [Full README](https://github.com/Yuuz12/dsh-webui-auth#readme)
- [Back to the Plugins list](../plugins.md)
