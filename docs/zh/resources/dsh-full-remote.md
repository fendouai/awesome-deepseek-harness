---
title: "dsh-full-remote"
description: "Auditable, token-gated DeepSeek Harness remote gateway: mobile QR access, per-device sessions, Host/Origin rewrite, settings/credentials/directory support."
keywords: "dsh-full-remote, vision, plugin, coding, deepseek harness, dsh"
---
# dsh-full-remote

> ⭐ **29** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 视觉与多模态 |
| 星数 | ⭐ 29 | 状态 | ✅ 活跃 |
| 作者 | [JUANWANG-BUAA](https://github.com/JUANWANG-BUAA) | 更新时间 | — |
| 子分类 | 👁️ 视觉工具 | 能力 | coding |

## 一句话介绍

> Auditable, token-gated DeepSeek Harness remote gateway: mobile QR access, per-device sessions, Host/Origin rewrite, settings/credentials/directory support.

## 详细介绍

**Listed in [awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin)** · DeepSeek Harness plugin `dsh-full-remote` is a plugin for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness). It places an authenticated reverse proxy in front of the Harness Web server, so the Web UI can be used through a public tunnel or from a device on the local network while privileged APIs such as settings, credentials, and directory browsing remain available.

## ✨ 核心特性

- `settings.*`
- `credentials.*`
- `host.listDirectory`

## 📦 安装

```bash
dsh plugin --profile web add dsh-full-remote
dsh --profile web
```

## 🚀 快速开始

```bash
flowchart LR
    A[Phone or remote browser] --> B[Public tunnel<br>cloudflared / ngrok / frp / SSH]
    B --> C[dsh-full-remote<br>127.0.0.1:3081<br>authentication + header rewrite]
    C --> D[DeepSeek Harness Web<br>127.0.0.1:3080]
```

## 📚 更多信息

**60-second quick start**

dsh plugin --profile web add dsh-full-remote dsh --profile web In **Settings → Reverse proxy**, press **Start proxy**, then **Start Cloudflare quick tunnel** and scan the generated QR code. The invite is one-time and never contains the standing access token. For a controlled network, point an existing SSH, frp, ngrok, Tailscale, or cloudflared tunnel at the proxy target shown in the panel instead.

**One-click public tunnel (Cloudflare quick tunnel)**

get a `https://…trycloudflare.com` address — no public IP or port forwarding required (2026.8.2), SHA256-verified download cache; failed checksums are discarded (rate limiting / CIDR / audit see real client IPs) and reverts when the tunnel stops; the tunnel forwards to the proxy listener, so the token gate, approval and audit all keep applying the QR, scan from the phone (the panel shows it and th

**Installation**

dsh plugin --profile web add dsh-full-remote dsh --profile web 1. Open `http://127.0.0.1:3080`. 2. Open **Settings → Reverse proxy** (last entry in the left navigation). 3. Press **Start proxy** and copy the local target. 4. Point the tunnel at the target:

**Examples only. The plugin does not execute these commands.**

cloudflared tunnel --url http://127.0.0.1:3081 ngrok http 3081 For devices on the same network, set the listen address to a LAN IP instead of using a tunnel. The package was previously published as `dsh-reverse-proxy`; that legacy name is deprecated. Install `dsh-full-remote` for new deployments.

## 🔗 链接

- [GitHub 仓库](https://github.com/JUANWANG-BUAA/dsh-full-remote)
- [完整 README](https://github.com/JUANWANG-BUAA/dsh-full-remote#readme)
- [返回dsh-full-remote所在分类](../plugins.md)
