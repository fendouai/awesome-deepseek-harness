---
title: "dsh-qqbot-panel"
description: "为官方 @tencent-connect/dsh-qqbot 提供的可视化配置面板：管理 AppID/AppSecret、私聊/群聊访问模式与白名单、工作区选择、扫码绑定（Web 设置页）。"
keywords: "dsh-qqbot-panel, automation, plugin, ui, deepseek harness, dsh"
---
# dsh-qqbot-panel

> ⭐ **0** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 自动化 |
| 星数 | ⭐ 0 | 状态 | ✅ 活跃 |
| 作者 | [zhengjy01](https://github.com/zhengjy01) | 更新时间 | — |

## 一句话介绍

> 为官方 @tencent-connect/dsh-qqbot 提供的可视化配置面板：管理 AppID/AppSecret、私聊/群聊访问模式与白名单、工作区选择、扫码绑定（Web 设置页）。

## 详细介绍

A visual settings panel for the official [@tencent-connect/dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh). The official QQ bot plugin is a pure CLI plugin with no Web UI; this companion plugin adds a **Settings → QQ Bot** page so you can configure everything — and even bind your bot by scanning a QR code — right from the web GUI.

## ✨ 核心特性

- **Settings panel** — web GUI: Settings → QQ Bot. Manage `appId` / `appSecret`, private-chat (c2c) & group access modes (`open` / `allowlist` / `disabled`) and t
- **Scan-to-bind** — one click generates a QR code inside the panel; scan it with the QQ app and the returned `appId` / `appSecret` are written back automatically
- **Workspace picker** — choose which workspace the QQ bot's agent sessions live in (`cwd`); the panel lists every workspace that already has sessions and its ses
- Reads/writes the `im-qqbot` row in the qqbot profile's `cordis.patch.yml` via a loopback-only `/api/dsh-qqbot-panel` route family.
- `appSecret` is only ever returned masked and is never overwritten by an empty value.

## 📦 安装

```bash
# after publishing (repo tagged with the `dsh-plugin` topic)
dsh plugin --profile web add github:zhengjy01/dsh-qqbot-panel

# local development
dsh plugin --profile web add link:/path/to/dsh-qqbot-panel
```

## 🚀 快速开始

```bash
# the official QQ bot plugin (required companion), in its own profile
dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot
dsh --profile qqbot          # prints a QR to bind, or use the panel's scan-to-bind
```

## 📚 更多信息

**Configuration**

Everything is managed from the panel: Settings → QQ Bot. There you can set `appId` / `appSecret`, the access modes and allowlists, whether group chats need `@bot` (`requireMention`), and the workspace the QQ bot sessions land in. The panel persists changes to the qqbot profile's `cordis.patch.yml` (`~/.dsh/profiles/qqbot/cordis.patch.yml`), which the running QQ bot hot-reloads.

## 🔗 链接

- [GitHub 仓库](https://github.com/zhengjy01/dsh-qqbot-panel)
- [完整 README](https://github.com/zhengjy01/dsh-qqbot-panel#readme)
- [返回dsh-qqbot-panel所在分类](../plugins.md)
