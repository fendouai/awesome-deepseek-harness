---
title: "dsh-lan-access"
description: "Web GUI 局域网访问：0.0.0.0 绑定 + 非安全上下文 polyfill。"
keywords: "dsh-lan-access, developer, integration, automation, deepseek harness, dsh"
---
# dsh-lan-access

> ⭐ **9** · ✅ 活跃 · 集成 · 近期 ⬆️ +2

| | | | |
|---|---|---|---|
| 类型 | 集成 | 分类 | 开发者工具 |
| 星数 | ⭐ 9 | 状态 | ✅ 活跃 |
| 作者 | [Leon0555](https://github.com/Leon0555) | 更新时间 | 2026-08-18 |
| 子分类 | 🛡️ 安全与运维 | 能力 | automation |

## 一句话介绍

> Web GUI 局域网访问：0.0.0.0 绑定 + 非安全上下文 polyfill。

## 详细介绍

让 DeepSeek Harness Web GUI 可在局域网内被其他设备访问的 DSH 插件（可信内网专用）。 同一局域网下，手机/平板/电脑打开浏览器即可直接访问你某台设备上的 DSH——无需 SSH、无需内网穿透，npm 一键安装。 - **npm**: https://www.npmjs.com/package/dsh-lan-access - **GitHub**: https://github.com/Leon0555/dsh-lan-access

## ✨ 核心特性

- **npm**: https://www.npmjs.com/package/dsh-lan-access
- **GitHub**: https://github.com/Leon0555/dsh-lan-access

## 📦 安装

```bash
dsh plugin --profile web add dsh-lan-access
```

## 🚀 快速开始

```bash
launchctl kickstart -k gui/$(id -u)/com.dsh.web   # 如果用 launchd 常驻
```

## 📚 更多信息

**安装（从 npm）**

dsh plugin --profile web add dsh-lan-access > 需要 pnpm（`npm i -g pnpm`）。本地开发安装可用 > `dsh plugin --profile web add file:/path/to/dsh-lan-access`。 安装后重启服务生效： launchctl kickstart -k gui/$(id -u)/com.dsh.web # 如果用 launchd 常驻

**远程访问限制（安全设计，本插件有意不绕过）**

DSH 把"配置平面"——**设置页、模型/Provider 管理、凭据、Agent Preset、 目录选择、`llm.discoverModels`（模型探测）**等接口——**硬性限制为仅本机回环 （127.0.0.1）可访问**。即使本插件将 Web 服务绑定到 `0.0.0.0`，这些接口从 局域网 IP 访问仍会返回 `HTTP 403`（如"加载提供方目录失败: ... HTTP 403"）。 这是 DSH 官方刻意的安全边界（`dsh-client-connection` 的 `PRIVILEGED_METHODS`）： `trustedHosts` 白名单只是 DNS 反绑定栅栏，**不是认证**；在真正的认证层出现 之前，设置/凭据域必须保持仅本机可访问。 **本插件不绕过这个栅栏**，也不提供代理/端口转发去改写请求头——那会把设置与 凭据侦察能力暴露给局域网内任何设

**技术说明**

`ctx.webStartup.port ?? 3080` 表达式）。 index.html `<head>` 注入内联脚本；带幂等守卫，非安全上下文才生效， 本机 localhost 访问不受影响。 选择器针对 DSH 的 `data-slot` / `data-chat-flow` / `data-composer-card` / `role="dialog"` 等稳定结构属性）。

## 🔗 链接

- [GitHub 仓库](https://github.com/Leon0555/dsh-lan-access)
- [完整 README](https://github.com/Leon0555/dsh-lan-access#readme)
- [返回dsh-lan-access所在分类](../integrations.md)
