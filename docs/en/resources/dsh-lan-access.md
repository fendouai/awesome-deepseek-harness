---
title: "dsh-lan-access"
description: "LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure contexts."
keywords: "dsh-lan-access, developer, integration, automation, deepseek harness, dsh"
---
# dsh-lan-access

> ⭐ **9** · ✅ active · integration · ⬆️ +2 recently

| | | | |
|---|---|---|---|
| Type | integration | Category | Developer tools |
| Stars | ⭐ 9 | Status | ✅ active |
| Author | [Leon0555](https://github.com/Leon0555) | Updated | 2026-08-18 |
| Subcategory | 🛡️ Security & ops | Capabilities | automation |

## One-liner

> LAN access for the Web GUI: 0.0.0.0 bind plus a crypto.randomUUID polyfill for non-secure contexts.

## About

让 DeepSeek Harness Web GUI 可在局域网内被其他设备访问的 DSH 插件（可信内网专用）。 同一局域网下，手机/平板/电脑打开浏览器即可直接访问你某台设备上的 DSH——无需 SSH、无需内网穿透，npm 一键安装。 - **npm**: https://www.npmjs.com/package/dsh-lan-access - **GitHub**: https://github.com/Leon0555/dsh-lan-access

## ✨ Key Features

- **npm**: https://www.npmjs.com/package/dsh-lan-access
- **GitHub**: https://github.com/Leon0555/dsh-lan-access

## 📦 Install

```bash
dsh plugin --profile web add dsh-lan-access
```

## 🚀 Quick Start

```bash
launchctl kickstart -k gui/$(id -u)/com.dsh.web   # 如果用 launchd 常驻
```

## 📚 Learn more

**安装（从 npm）**

dsh plugin --profile web add dsh-lan-access > 需要 pnpm（`npm i -g pnpm`）。本地开发安装可用 > `dsh plugin --profile web add file:/path/to/dsh-lan-access`。 安装后重启服务生效： launchctl kickstart -k gui/$(id -u)/com.dsh.web # 如果用 launchd 常驻

**远程访问限制（安全设计，本插件有意不绕过）**

DSH 把"配置平面"——**设置页、模型/Provider 管理、凭据、Agent Preset、 目录选择、`llm.discoverModels`（模型探测）**等接口——**硬性限制为仅本机回环 （127.0.0.1）可访问**。即使本插件将 Web 服务绑定到 `0.0.0.0`，这些接口从 局域网 IP 访问仍会返回 `HTTP 403`（如"加载提供方目录失败: ... HTTP 403"）。 这是 DSH 官方刻意的安全边界（`dsh-client-connection` 的 `PRIVILEGED_METHODS`）： `trustedHosts` 白名单只是 DNS 反绑定栅栏，**不是认证**；在真正的认证层出现 之前，设置/凭据域必须保持仅本机可访问。 **本插件不绕过这个栅栏**，也不提供代理/端口转发去改写请求头——那会把设置与 凭据侦察能力暴露给局域网内任何设

**技术说明**

`ctx.webStartup.port ?? 3080` 表达式）。 index.html `<head>` 注入内联脚本；带幂等守卫，非安全上下文才生效， 本机 localhost 访问不受影响。 选择器针对 DSH 的 `data-slot` / `data-chat-flow` / `data-composer-card` / `role="dialog"` 等稳定结构属性）。

## 🔗 Links

- [GitHub Repository](https://github.com/Leon0555/dsh-lan-access)
- [Full README](https://github.com/Leon0555/dsh-lan-access#readme)
- [Back to the MCP & Integrations list](../integrations.md)
