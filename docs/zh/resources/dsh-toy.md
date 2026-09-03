---
title: "dsh-toy"
description: "Toy Control Protocol for DSH"
keywords: "dsh-toy, developer, plugin, coding, deepseek harness, dsh"
---
# dsh-toy

> ⭐ **64** · ✅ 活跃 · 插件

| | | | |
|---|---|---|---|
| 类型 | 插件 | 分类 | 开发者工具 |
| 星数 | ⭐ 64 | 状态 | ✅ 活跃 |
| 作者 | [c3ll256](https://github.com/c3ll256) | 更新时间 | — |

## 一句话介绍

> Toy Control Protocol for DSH

## 详细介绍

`dsh-toy` is a DeepSeek Harness plugin for connecting small toys to DSH. At connection time, the agent first asks for the brand and model, then selects the connection method automatically. If the user genuinely does not know, the agent starts unknown-hardware discovery: - On macOS, unknown hardware first uses read-only raw **CoreBluetooth** advertisement discovery, without starting Intiface or connecting to devices. - Regular Bluetooth, serial, and USB models use **Buttplug / Intiface**. The plugin starts local Intiface Engine automatically when needed. - Known sharing-link models from Ankni (安可尼), MizzZee (谜姬), and Zuiqingfeng (醉清风) use **MonsterParty**. Known dual-output devices expose their channels separately. Users do not need to understand or select an underlying connection method, o

## ✨ 核心特性

- On macOS, unknown hardware first uses read-only raw **CoreBluetooth** advertisement discovery, without starting Intiface or connecting to devices.
- Regular Bluetooth, serial, and USB models use **Buttplug / Intiface**. The plugin starts local Intiface Engine automatically when needed.
- Known sharing-link models from Ankni (安可尼), MizzZee (谜姬), and Zuiqingfeng (醉清风) use **MonsterParty**. Known dual-output devices expose their channels separately

## 📦 安装

```bash
npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy
```

## 🚀 快速开始

```bash
npx -y @deepseek-ai/dsh web
```

## 📚 更多信息

**Install**

Requirements: Node.js 22.19 or newer and pnpm on `PATH`. Raw macOS BLE discovery additionally uses the Swift compiler from Xcode Command Line Tools. Install pnpm once if needed with `npm install --global pnpm@10`, then add the plugin directly from GitHub: npx -y @deepseek-ai/dsh plugin --profile web add github:c3ll256/dsh-toy Start DSH with the same profile: npx -y @deepseek-ai/dsh web The first c

**Quick start**

You can tell the agent directly: My toy is a Lovense Lush 3. Connect it and scan for devices. When the brand or model is unknown, say: I do not know the brand or model. Try Bluetooth discovery directly. On macOS, the agent first calls `toy_scan_raw_ble`. If the scan exposes a plausible advertised name, it uses that hardware-reported name for `toy_connect`; otherwise it falls back to `unknown`, con

## 🔗 链接

- [GitHub 仓库](https://github.com/c3ll256/dsh-toy)
- [完整 README](https://github.com/c3ll256/dsh-toy#readme)
- [返回dsh-toy所在分类](../plugins.md)
