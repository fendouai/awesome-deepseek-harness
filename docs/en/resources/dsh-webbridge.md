---
title: "dsh-webbridge"
description: "DSH combined with Kimi WebBridge for real browser control."
keywords: "dsh-webbridge, browser, plugin, deepseek harness, dsh"
---
# dsh-webbridge

> ⭐ **3** · ✅ active · plugin

| | | | |
|---|---|---|---|
| Type | plugin | Category | Browser control |
| Stars | ⭐ 3 | Status | ✅ active |
| Author | [bill9109](https://github.com/bill9109) | Updated | 2026-08-14 |

## One-liner

> DSH combined with Kimi WebBridge for real browser control.

## About

**Install:** `dsh plugin --profile web add github:omdsh-dev/dsh-webbridge` **A DeepSeek Harness host plugin: it bridges Kimi WebBridge's local daemon into eleven `webbridge_*` model tools, so the model operates **your own browser** — logins, cookies, and already-open tabs included — instead of a headless one.** [English](README.md) | [中文](README.zh.md)

## ✨ Key Features

- **Real browser, not headless**: logins, cookies, and live sessions preserved
- **Eleven model tools**: navigate / find_tab / snapshot / click / fill /
- **One task = one tab group**: a `session` name groups tabs, keeping tasks
- **Local-first**: the daemon runs on your machine; browser state never leaves it
- **No KV-cache burden**: browser state lives outside the model request

## 📦 Install

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-webbridge
```

## 🚀 Quick Start

```bash
# 1. Install the daemon:
curl -fsSL https://cdn.kimi.com/webbridge/install.sh | bash

# 2. Install the Kimi WebBridge browser extension and let it connect to the
#    daemon (search "Kimi WebBridge" in the Chrome Web Store), then check:
kimi-webbridge status   # expect "extension_connected": true
```

## 📚 Learn more

**Configuration**

The daemon address defaults to `http://127.0.0.1:10086`. The plugin accepts no configuration today; the `baseUrl` seam exists for tests.

**Install**

The plugin is a DSH **bundle** (`package.json` declares `dsh.bundle`, and `cordis.patch.yml` carries the patch). Install it into the `web` profile with the standard `dsh plugin` mechanism — **no DSH source changes and no hand-written patch**: dsh plugin --profile web add github:omdsh-dev/dsh-webbridge For a stable install, pin the version: `dsh plugin --profile web add github:omdsh-dev/dsh-webbrid

**Uninstall**

dsh plugin --profile web remove dsh-webbridge The command runs `pnpm remove <pkg>` in the profile directory and removes the package from `dsh.profile.bundles`. After uninstalling, restart web and refresh — the DSH built-in plugin (same row id `webbridge`) takes over again.

## 🔗 Links

- [GitHub Repository](https://github.com/bill9109/dsh-webbridge)
- [Full README](https://github.com/bill9109/dsh-webbridge#readme)
- [Back to the Plugins list](../plugins.md)
