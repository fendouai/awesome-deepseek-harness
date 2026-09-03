---
title: "dsh-qqbot-panel"
description: "Visual web settings panel for the official @tencent-connect/dsh-qqbot plugin: manage AppID/AppSecret, c2c & group access/allowlists, workspace picker, and scan-to-bind from the DSH web settings page."
keywords: "dsh-qqbot-panel, automation, plugin, ui, deepseek harness, dsh"
---
# dsh-qqbot-panel

> ⭐ **0** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Automation |
| Stars | ⭐ 0 | Status | ✅ active |
| Author | [zhengjy01](https://github.com/zhengjy01) | Updated | — |

## One-liner

> Visual web settings panel for the official @tencent-connect/dsh-qqbot plugin: manage AppID/AppSecret, c2c & group access/allowlists, workspace picker, and scan-to-bind from the DSH web settings page.

## About

A visual settings panel for the official [@tencent-connect/dsh-qqbot](https://github.com/tencent-connect/dsh-qqbot) plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (dsh). The official QQ bot plugin is a pure CLI plugin with no Web UI; this companion plugin adds a **Settings → QQ Bot** page so you can configure everything — and even bind your bot by scanning a QR code — right from the web GUI.

## ✨ Key Features

- **Settings panel** — web GUI: Settings → QQ Bot. Manage `appId` / `appSecret`, private-chat (c2c) & group access modes (`open` / `allowlist` / `disabled`) and t
- **Scan-to-bind** — one click generates a QR code inside the panel; scan it with the QQ app and the returned `appId` / `appSecret` are written back automatically
- **Workspace picker** — choose which workspace the QQ bot's agent sessions live in (`cwd`); the panel lists every workspace that already has sessions and its ses
- Reads/writes the `im-qqbot` row in the qqbot profile's `cordis.patch.yml` via a loopback-only `/api/dsh-qqbot-panel` route family.
- `appSecret` is only ever returned masked and is never overwritten by an empty value.

## 📦 Install

```bash
# after publishing (repo tagged with the `dsh-plugin` topic)
dsh plugin --profile web add github:zhengjy01/dsh-qqbot-panel

# local development
dsh plugin --profile web add link:/path/to/dsh-qqbot-panel
```

## 🚀 Quick Start

```bash
# the official QQ bot plugin (required companion), in its own profile
dsh plugin --profile qqbot add @tencent-connect/dsh-qqbot
dsh --profile qqbot          # prints a QR to bind, or use the panel's scan-to-bind
```

## 📚 Learn more

**Configuration**

Everything is managed from the panel: Settings → QQ Bot. There you can set `appId` / `appSecret`, the access modes and allowlists, whether group chats need `@bot` (`requireMention`), and the workspace the QQ bot sessions land in. The panel persists changes to the qqbot profile's `cordis.patch.yml` (`~/.dsh/profiles/qqbot/cordis.patch.yml`), which the running QQ bot hot-reloads.

## 🔗 Links

- [GitHub Repository](https://github.com/zhengjy01/dsh-qqbot-panel)
- [Full README](https://github.com/zhengjy01/dsh-qqbot-panel#readme)
- [Back to the Plugins list](../plugins.md)
