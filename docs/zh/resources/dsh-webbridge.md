---
title: "dsh-webbridge"
description: "DSH 结合 Kimi WebBridge 操控真实浏览器。"
keywords: "dsh-webbridge, browser, plugin, deepseek harness, dsh"
---
# dsh-webbridge

> ⭐ **3** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 浏览器控制 |
| 星数 | ⭐ 3 | 状态 | ✅ 活跃 |
| 作者 | [bill9109](https://github.com/bill9109) | 更新时间 | 2026-08-14 |

## 一句话介绍

> DSH 结合 Kimi WebBridge 操控真实浏览器。

## 详细介绍

**Install:** `dsh plugin --profile web add github:omdsh-dev/dsh-webbridge` **A DeepSeek Harness host plugin: it bridges Kimi WebBridge's local daemon into eleven `webbridge_*` model tools, so the model operates **your own browser** — logins, cookies, and already-open tabs included — instead of a headless one.** [English](README.md) | [中文](README.zh.md)

## ✨ 核心特性

- **Real browser, not headless**: logins, cookies, and live sessions preserved
- **Eleven model tools**: navigate / find_tab / snapshot / click / fill /
- **One task = one tab group**: a `session` name groups tabs, keeping tasks
- **Local-first**: the daemon runs on your machine; browser state never leaves it
- **No KV-cache burden**: browser state lives outside the model request

## 📦 安装

```bash
dsh plugin --profile web add github:omdsh-dev/dsh-webbridge
```

## 🚀 快速开始

```bash
# 1. Install the daemon:
curl -fsSL https://cdn.kimi.com/webbridge/install.sh | bash

# 2. Install the Kimi WebBridge browser extension and let it connect to the
#    daemon (search "Kimi WebBridge" in the Chrome Web Store), then check:
kimi-webbridge status   # expect "extension_connected": true
```

## 📚 更多信息

**Configuration**

The daemon address defaults to `http://127.0.0.1:10086`. The plugin accepts no configuration today; the `baseUrl` seam exists for tests.

**Install**

The plugin is a DSH **bundle** (`package.json` declares `dsh.bundle`, and `cordis.patch.yml` carries the patch). Install it into the `web` profile with the standard `dsh plugin` mechanism — **no DSH source changes and no hand-written patch**: dsh plugin --profile web add github:omdsh-dev/dsh-webbridge For a stable install, pin the version: `dsh plugin --profile web add github:omdsh-dev/dsh-webbrid

**Uninstall**

dsh plugin --profile web remove dsh-webbridge The command runs `pnpm remove <pkg>` in the profile directory and removes the package from `dsh.profile.bundles`. After uninstalling, restart web and refresh — the DSH built-in plugin (same row id `webbridge`) takes over again.

## 🔗 链接

- [GitHub 仓库](https://github.com/bill9109/dsh-webbridge)
- [完整 README](https://github.com/bill9109/dsh-webbridge#readme)
- [返回dsh-webbridge所在分类](../plugins.md)
